#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 18:04:19 2018

@author: abimaelsb
"""

import socket

HOST = 'localhost'
PORT = 5001
C_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (HOST, PORT)
C_udp.sendto("Conectando", dest)
print ' Zerinho ou Um! \n Por favor Aguarde...'

while True:
    n = C_udp.recvfrom(1024)
    if n[0] == '1':
        while True:
            try:
                np = int(raw_input('Insira o numero de jogadores: '))
                if np > 2:
                    C_udp.sendto(str(np), dest)
                    print "Aguarde!"
                    break
                else:
                    print('Insira um numero maior ou igual a 3!!!')
            except ValueError:
                print('Insira um numero inteiro!!!')
        if np > 2:
            break
    else:
        break

while True:
    cod = C_udp.recvfrom(1024)
    if cod[0] == "ok":
        while True:
            msg = raw_input("Insira seu palpite: ")
            if msg != "0" and msg != "1":
                print "Insira somente 0 ou 1"
            else:
                C_udp.sendto(msg, dest)
                break
        if msg == "0" or msg == "1":
            break
    if cod[0] == "erro":
        print "Número de Jogadores já atingido!!!"
        print "Tente novamente."
        break
    
while True:
    resp = C_udp.recvfrom(1024)
    if resp[0] == "erro":
        break
    elif resp[0] != "ok":
        print "SERVIDOR: ", resp[0]
C_udp.close()