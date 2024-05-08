import zmq
import time
import socket as soki
import threading



# host information
hostname=soki.gethostname()
host_id= str(soki.gethostbyname(hostname)) #"10.194.118.229"
host_port=":5555" # Laptop


# server information 
server_id="10.194.177.16"
server_port=":4444" # Desktop

#publisher sever
context_pub = zmq.Context()
socket_pub = context_pub.socket(zmq.PUB)
host_pub=r"tcp://"+host_id+host_port
socket_pub.bind(host_pub)


#subscriber server
context_sub = zmq.Context()
socket_sub = context_sub.socket(zmq.SUB)
server_connect=r"tcp://"+server_id+server_port #localhost:5555"
socket_sub.connect(server_connect)
socket_sub.setsockopt_string(zmq.SUBSCRIBE, "")

def action():
    print("action triggered ")
# subs function for a thread
def sub_function(socket_sub,context_sub):
    try:
        while True:
            print("zzfuck")
            message = socket_sub.recv()

            print("Received:", message)
            if message=="fuck":
                action()
    except KeyboardInterrupt:
        print("\nExiting... no signal")
    finally:
        socket_sub.close()
        context_sub.term()

# publisher function for a thread

def pub_function(socket_pub,context_pub):
    try:
        while True:
            msg=input(f"{hostname}: ")
            message_from_host=f"{hostname}: {msg}"
            message =message_from_host.encode('utf-8')
            socket_pub.send(message)
            print("Sent:", message)
            # sub_function(socket_sub,context_sub)
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nExiting... no signal")
    finally:
        socket_pub.close()
        context_pub.term()



# Start a thread to receive messages from the server
receive_thread = threading.Thread(target=sub_function, args=(socket_sub,context_sub))
receive_thread.daemon = True  # Make sure the thread ends when the main program exits
receive_thread.start()


pub_function(socket_pub,context_pub)