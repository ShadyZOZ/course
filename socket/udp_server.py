import socketserver

clientSocket = []

class MyUDPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        global clientSocket
        if self.client_address not in clientSocket:
            clientSocket.append(self.client_address)
        data = self.request[0].strip()
        socket = self.request[1]
        if data == b'88':
            clientSocket.pop(clientSocket.index(self.client_address))
        print(len(clientSocket), 'client connected')
        print("{} wrote:".format(self.client_address))
        print(data)
        for client in clientSocket:
            if client != self.client_address:
                print('sending to ', client)
                socket.sendto(data, client)

if __name__ == "__main__":
    print('------------------')
    print(' written by shady')
    print('------------------')
    HOST, PORT = "localhost", 9999
    server = socketserver.UDPServer((HOST, PORT), MyUDPHandler)
    server.serve_forever()
