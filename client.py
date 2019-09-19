#!/usr/bin/env python

import socket
import select
import sys
import json
from time import sleep

MESSAGE_ENCODING = 'utf8'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if len(sys.argv) != 3:
    print("Correct usage:\n\t%s IP_ADDRESS PORT_NUMBER" % (sys.argv[0]))
    exit(1)

ip_address = str(sys.argv[1])
port = int(sys.argv[2])
host = str(ip_address)
self_username = '<You | ' + host + '>'
server.connect((ip_address, port))

def send_message_to_connection(message, conn):
    conn.send(bytearray(message, MESSAGE_ENCODING))

first_line = True

while True:

    # maintains a list of possible input streams
    sockets_list = [sys.stdin, server]

    read_sockets, _, _ = select.select(sockets_list, [], [])
    for sockets in read_sockets:
        if sockets == server:
            encoded_message = sockets.recv(2048)
            message = encoded_message.decode(MESSAGE_ENCODING).strip()
            to_print = ''
            if not first_line:
                to_print += '\n'
            else:
                first_line = False
            to_print += message + '\n'
            to_print += self_username + ' '
            sys.stdout.flush()
        else:
            message = sys.stdin.readline()
            send_message_to_connection(message, server)
            sys.stdout.write(self_username + ' ')
            sys.stdout.flush()
        sleep(1)
server.close()
