import threading
import socket
import sys
import select






if len(sys.argv) != 3:
	print("[*]Usage: python3 server.py [server_ip] [port].")
	exit(0)
 	
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

IP_address = arg[1]
PORT = int(sys.argv[2])



server.connect((IP_address, PORT))


print(f"[*]Connecting to {IP_address}:{PORT}...")

while True:

	sockets_list = [sys.stdin, server]

	read_socket, write_socket, error_socket = select.select(sockets_list, [], [])

	for sock in read_socket:
		if sock == server:
			message = sock.recv(2048)
			print(message)
		message = sys.stdin.readLine()
		server.send(message)
		sys.stdout.write("[You]:")
		sys.stdout.write(message)
		sys.stdout.flush()

server.close()

























