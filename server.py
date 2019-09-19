#!/usr/bin/env python

import socket
import select
import sys
import time
from _thread import start_new_thread

MESSAGE_ENCODING = 'utf8'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

if len(sys.argv) != 3:
    print("Correct usage:\n\t%s IP_ADDRESS PORT_NUMBER" % (sys.argv[0]))
    exit(1)

IP_address = str(sys.argv[1])

Port = int(sys.argv[2])

server.bind((IP_address, Port))

server.listen(100)

list_of_clients = []

'''
The function convert_to_bytes converts the string message into bytes and if the message
is already in bytes it will return the message.
'''
def convert_to_bytes(message):
    if type(message) == bytes:
        return message
    elif type(message) == str:
        return bytearray(message, MESSAGE_ENCODING)

'''
Function send_message_to_connection sends the message converted into bytes to the
connection.
'''
def send_message_to_connection(message, conn):

    conn.send(convert_to_bytes(message))

'''
function clientthread prints the address and message of the sender if there is a message
or else it will remove the connection.
'''
def clientthread(conn, addr):

    '''
    sends welcome message to the client.
    '''
    send_message_to_connection('Welcome to this chatroom!', conn)

    while True:
        try:
            encoded_message = conn.recv(2048)
            message = encoded_message.decode(MESSAGE_ENCODING)
            sender = '<' + str(addr[0]) + ':' + str(addr[1]) + '>'

            if message:
                print(sender, message)

                message_to_send = sender + ' ' + message
                broadcast(message_to_send, conn)
            else:
                remove(conn)
        except Exception as err:
            print(err)

'''
function broadcast will send the message to the function send_message_to_connection.
'''
def broadcast(message, connection):
    for client_connection in list_of_clients:
        if client_connection != connection:
            try:
                send_message_to_connection(message, client_connection)
            except:
                print('closing connection', client_connection)
                client_connection.close()
                remove(client_connection)

'''
function remove removes the connection from the list_of_clients.
'''
def remove(connection):
    if connection in list_of_clients:
        list_of_clients.remove(connection)

while True:

    accept_params = server.accept()

    conn, addr = accept_params

    list_of_clients.append(conn)

    print(addr[0], " connected")

    start_new_thread(clientthread, (conn, addr))

conn.close()
server.close()
