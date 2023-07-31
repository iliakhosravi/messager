import socket
import threading

HOST = "127.0.0.1"
PORT = 1234

def message_receiver(ClientSocket):
    try:
        while True:
            data = ClientSocket.recv(1024).decode("utf-8")

            if not data:
                print("there is no message \n disconnected from server.")
                break

            print("Received message from the server: {}".format(data))
    
    except:
        print("somethings wrong while receiving!!")
    finally:
        ClientSocket.close()


def start_client():
    '''
    running client server using socket
    '''
    ClientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # connecting to the server
    ClientSocket.connect((HOST,PORT))
    #using thread to receive & send messages
    receive_thread = threading.Thread(target=message_receiver, args=(ClientSocket,))
    receive_thread.start()
    try:
        while True:
            message = input("Enter your message: ")
            ClientSocket.sendall(message.encode("utf-8"))
    except:
        print("Error while sending messages.")
    finally:
        # Close the client socket on error or when the user stops sending messages
        ClientSocket.close()

if __name__ == "__main__":
    start_client()
