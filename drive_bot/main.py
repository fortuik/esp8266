# coding=utf-8
""" main """

import machine
import network
import utime
import ubinascii

from . import config

def connect_wlan():
    """connect to WLan"""
    print('Connecting to WLan...')
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    cstart_ms = utime.ticks_ms()
    if not wlan.isconnected():
        wlan.connect(config.WLAN_SSID, config.WLAN_PSK)
        while not wlan.isconnected():
            utime.sleep_ms(100)
            if utime.ticks_diff(cstart_ms, utime.ticks_ms()) > 10000:
                print('Connecting to WLAN timed out. Resetting!')
                machine.reset()
    mac_address = ubinascii.hexlify(wlan.config('mac')).decode('utf-8')


try:
    import usocket as socket
except:
    import socket

CONTENT = b"""\
HTTP/1.0 200 OK\r\n\
\r\n\
Hello from MicroPython!
"""

def main():
    """ main """
    s = socket.socket()
    ai = socket.getaddrinfo("0.0.0.0", 8080)
    addr = ai[0][-1]
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(addr)
    s.listen(5)
    print("Listening, connect your browser to http://<host>:8080/")
    counter = 0
    while True:
        res = s.accept()
        client_s = res[0]
        client_addr = res[1]
        http_req = client_s.recv(4096)
        req = http_req.split('\n', 1)[0].split()[1][1:]
        print("Request:")
        print(req)
        # client_s.send(CONTENT % counter)
        client_s.send(req)
        client_s.close()
        counter += 1
        print()


"""run main"""
main()
