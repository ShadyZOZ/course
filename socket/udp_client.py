import socket
import threading

def send():
    while 1:
        data = input()
        while len(data) != 0:
            sock.sendto(bytes(data + "\n", "utf-8"), (HOST, PORT))
            data = input()
        data = "88"

def receive():
    while 1:
        received = str(sock.recv(1024), "utf-8")
        if len(received) != 0:
            print("Received: {}".format(received))

def main():
    threads = []
    tSend = threading.Thread(target = send, args = ())
    threads.append(tSend)
    tReceive = threading.Thread(target = receive, args = ())
    threads.append(tReceive)

    for i in range(2):
        threads[i].start()

if __name__ == '__main__':
    print('------------------')
    print(' written by shady')
    print('------------------')
    HOST = input('HOST: ')
    PORT = int(input('PORT: '))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    data = "hello"
    sock.sendto(bytes(data + "\n", "utf-8"), (HOST, PORT))
    main()
