import zmq
import time
import socket as soki
hostname=soki.gethostname()
host_id= str(soki.gethostbyname(hostname)) #"10.194.118.229"
host_port=":5555" # Laptop

# signal.signal(signal.SIGINT, sigint_handler)

#publisher sever
context_pub = zmq.Context()
socket_pub = context_pub.socket(zmq.PUB)
host_pub=r"tcp://"+host_id+host_port
socket_pub.bind(host_pub)

try:
    while True:
        message = b"Hello from Server 1"
        socket_pub.send(message)
        print("Sent:", message)
        time.sleep(1)
except KeyboardInterrupt:
    print("\nExiting... no signal")
finally:
    socket_pub.close()
    context_pub.term()