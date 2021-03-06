import threading
import socket
import sys
import select



def clientthread(client, address):
	message = "Welcome to this chatroom!"	
	client.send(message.encode('utf-8'))

	while True:
		try:
			message = client.recv(2048)
			if message:
				message = message.decode("utf-8")
				print(f"[{address[0]}]: {message}")

				message_to_send = f"[{address[0]}]: {message}"

				broadcast(message_to_send.encode('utf-8'), client)
			else:
				remove(client)
		except:
			continue



def broadcast(message, connection):
	for client in list_of_clients:
		if client != connection:
			try:
				client.send(message)

			except:
				client.close()

				remove(client)



def remove(client):
	if client in list_of_clients:
		list_of_clients.remove(client)




if __name__ == '__main__':



	if len(sys.argv) != 2:
		print("[*]Usage: python3 server.py [port].")
		exit(0)
	 	

	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect(("8.8.8.8", 80))
	IP_address = s.getsockname()[0]
	s.close()
	PORT = int(sys.argv[1])

	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


	server.bind((IP_address, PORT))

	server.listen(100)

	list_of_clients = []



	print(f"[*]Server started.Listing for connections on {IP_address}:{PORT}...")

	while True:

		client, address = server.accept()
		list_of_clients.append(client)
		print(f"[+]{address[0]} Connected.")

		thread = threading.Thread(target=clientthread, args=(client, address))
		thread.start()

	client.close()
	server.close()

























