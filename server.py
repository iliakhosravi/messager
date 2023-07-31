import socket  
import threading
HOST = "127.0.0.1" 
PORT = 1234

def client_handler(ClientSocket, ClientAddress):
    '''
    handle two client with multithreading
    '''
    try:
        while True:
            # Received data
            data = ClientSocket.recv(1024).decode("utf-8")

            if not data:
                print("there is no message \n disconnected from server.")
                break
            print("Received message from {}: {}".format(ClientAddress, data))

            #send message
            for other_client in clients:
                if other_client != ClientSocket:
                    other_client.sendall(data.encode("utf-8"))
            
    except:
        print("there is something happend")
    finally:
        ClientSocket.close()
        #remove client from the list 
        clients.remove(ClientSocket)    

def start_server():
    '''
    start server local host 
    '''
    ServerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #ServerSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    ServerSocket.bind((HOST, PORT))
    
    # listening for max 2 connection
    ServerSocket.listen(2)

    print("Server listening on {}:{}".format(HOST, PORT))
    
        
        
    while True:
        try:
        #wait for client
            ClientSocket, ClientAddress = ServerSocket.accept()
            print("Connected to clinet on {}".format(ClientAddress))

            #add to the list
            clients.append(ClientSocket)

            #thread
            client_thread = threading.Thread(target=client_handler, args=(ClientSocket, ClientAddress))
            client_thread.start()

            
        except KeyboardInterrupt:
            ServerSocket.close()
            print("Server socket closed.")
            break



if __name__ == "__main__":
    # tracking clients
    clients = []
            
    start_server()


