# Python3 program imitating a client process

from timeit import default_timer as timer
from dateutil import parser
import threading
import datetime
import socket
import time


# client thread function used to send time at client side
def startSendingTime(slave_client):

	while True:
		# provide server with clock time at the client
		slave_client.send(str(
					datetime.datetime.now()).encode())

		print("Recent time sent successfully",
										end = "\n\n")
		time.sleep(5)


# client thread function used to receive synchronized time
def startReceivingTime(slave_client):

	while True:
		# receive data from the server
		Synchronized_time = parser.parse(
						slave_client.recv(1024).decode())

		print("Synchronized time at the client is: " + \
									str(Synchronized_time),
									end = "\n\n")


# function used to Synchronize client process time
def initiateSlaveClient(port = 8080):

	slave_client = socket.socket()		
	
	# connect to the clock server on local computer
	slave_client.connect(('127.0.0.1', port))

	# start sending time to server
	print("Starting to receive time from server\n")
	send_time_thread = threading.Thread(
					target = startSendingTime,
					args = (slave_client, ))
	send_time_thread.start()


	# start receiving synchronized from server
	print("Starting to receiving " + \
						"synchronized time from server\n")
	receive_time_thread = threading.Thread(
					target = startReceivingTime,
					args = (slave_client, ))
	receive_time_thread.start()


# Driver function
if __name__ == '__main__':

	# initialize the Slave / Client
	initiateSlaveClient(port = 8080)








































'''
- Clock synchronization refers to the process of ensuring that the clocks of different nodes in the system are accurately synchronized with each other.
- The algorithms are used to ensure that the clocks in distributed system are accurate and consistent.
- In a distributed system, clocks can drift apart due to variations in clock speed.
- Two types are: Berkely and Ring.

- Berkeley’s Algorithm is a clock synchronization technique used in distributed systems.
- It assumes that each machine node in the network either doesn’t have an accurate time source or doesn’t possess a UTC server.
- The time server periodically sends a request message “time=?” to all nodes.
- Each node sends back its time value to the time server.
- The time server has an idea of message propagation of each node, and it readjusts the clock values in the reply message.
- It takes an average of clock values (including its own) and readjusts its own clock.
- It avoids reading from unreliable clocks.
- For adjustment, it sends the factor by which other nodes require adjustment.
- The readjustment values can be positive or negative.
- The time server being a centralized node, can be a single point of failure, and may not be able to serve all requests from a scalability point of view.

- Consistency
- Correctness
- Security
- Debugging
'''
	
