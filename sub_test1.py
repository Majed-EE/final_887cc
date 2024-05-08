import zmq
# import signal
# import sys

# def sigint_handler(sig, frame):
#     print("\nExiting...")
#     sys.exit(0)

# signal.signal(signal.SIGINT, sigint_handler)

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://localhost:5555")
socket.setsockopt_string(zmq.SUBSCRIBE, "")

try:
    while True:
        message = socket.recv()
        print("Received:", message)
except KeyboardInterrupt:
    print("\nExiting... no signal")
finally:
    socket.close()
    context.term()
