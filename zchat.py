import zmq
import time
import socket as soki
import threading



# host information
hostname=soki.gethostname()
host_id= "10.194.168.125"#str(soki.gethostbyname(hostname)) #"10.194.118.229"
host_port=":5555" # Laptop

print(host_id)
# server information 
server_id="10.194.177.16"
server_port=":4444" # Desktop

# #publisher sever
# context_pub = zmq.Context()
# socket_pub = context_pub.socket(zmq.PUB)
# host_pub=r"tcp://"+host_id+host_port
# socket_pub.bind(host_pub)




def publisher():
    #publisher sever
    context_pub = zmq.Context()
    socket_pub = context_pub.socket(zmq.PUB)
    host_pub=r"tcp://"+host_id+host_port
    socket_pub.bind(host_pub)

    
    # context = zmq.Context()
    # socket = context.socket(zmq.PUB)
    # socket.bind("tcp://127.0.0.1:5556")
    while True:
        message = input("User 2: ")
        socket_pub.send_string(message)

def subscriber():
    #subscriber server
    context_sub = zmq.Context()
    socket_sub = context_sub.socket(zmq.SUB)
    server_connect=r"tcp://"+server_id+server_port #localhost:5555"
    socket_sub.connect(server_connect)
    socket_sub.setsockopt_string(zmq.SUBSCRIBE, "")

        
    
    # context = zmq.Context()
    # socket = context.socket(zmq.SUB)
    # socket.connect("tcp://127.0.0.1:5555")
    # socket.setsockopt_string(zmq.SUBSCRIBE, "")
    while True:
        message = socket_sub.recv_string()
        print("\nUser 1:", message)

if __name__ == "__main__":
    pub_thread = threading.Thread(target=publisher)
    sub_thread = threading.Thread(target=subscriber)
    pub_thread.start()
    sub_thread.start()