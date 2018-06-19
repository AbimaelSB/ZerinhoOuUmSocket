#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 17:05:30 2018

@author: abimaelsb
"""

import socket

lista = []
players = []
zero = []
um = []
venc = "empate"
palp = "empate"
HOST = 'localhost'
PORT = 15000
n = 0
j = 0
aux = 0

S_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
end = (HOST, PORT)
S_udp.bind(end)
print "Rodando Servidor! \n"


while True:
    msg, cliente = S_udp.recvfrom(1024)
    if cliente not in lista:
        lista.append(cliente)
    aux += 1
    if msg == "Conectando":
        S_udp.sendto(str(aux), cliente)
    elif msg != "Conectando":
        if int(msg) > 2:
            j = int(msg)
            break
                
while True:
    if j > 2:
        if len(lista) >= j:
            for i in range(len(lista)):
                if i < j:
                    S_udp.sendto("ok", lista[i])
                else:
                    S_udp.sendto("erro", lista[i])
        msg, cliente = S_udp.recvfrom(1024)
        if len(lista) < j:
            if cliente not in lista:
                lista.append(cliente)
        if msg == "Conectando":
            S_udp.sendto(str(aux), cliente)

        elif msg == "0" or msg == "1":
            n += 1
            players.append(cliente)
            players.append(msg)
            if n < j:
                S_udp.sendto("Aguardando Demais Jogadores", cliente)    
            else:
                if n == j:
                    for i in range(0, len(players), +2):
                        if int(players[i+1]) == 0:
                            zero.append(players[i+1])
                        elif int(players[i+1]) == 1:
                            um.append(players[i+1])
                    if len(zero) == 1:
                        for i in range(0, len(players), +2):
                            if players[i+1] == zero[0]:
                                venc = players[i]
                                palp = 0
                                S_udp.sendto("Você venceu", venc)
                            else:
                                S_udp.sendto("Você perdeu", players[i])
                    elif len(um) == 1:
                        for i in range(0, len(players), +2):
                            if players[i+1] == um[0]:
                                venc = players[i]
                                palp = 1
                                S_udp.sendto("Você venceu", venc)
                            else:
                                S_udp.sendto("Você perdeu", players[i])
                    else:
                        for i in range(0, len(players), +2):
                            S_udp.sendto(venc, players[i])
                        
                        print "------------- Tabela de Palpites ----------------"
                        for i in range(0, len(players), +2):
                            print "Jogador: ",  players[i], "Palpite: ", players[i+1]
                        print "Vencedor: ", venc, "Palpite: ", palp
                        print
                        break
                else:
                    for i in range(0, len(players),+2):
                        S_udp.sendto("Aguardando Mais Jogadores", players[i])
S_udp.close()
