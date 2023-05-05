import random
import time
from datetime import datetime
import socket

# Get current timestamp
timestamp = int(time.time())

# Generate random number between 0 and 9999
rand_num = random.randint(0, 9999)

# Generate transaction ID by concatenating timestamp and random number
transaction_id = timestamp * 10000 + rand_num

# Get current date and time
current_datetime = datetime.fromtimestamp(timestamp)

# Get user's IP address
ip_address = socket.gethostbyname(socket.gethostname())

# Print transaction details
print("Transaction ID:", transaction_id)
print("Date:", current_datetime.date())
print("Time:", current_datetime.time())
print("IP Address:", ip_address)
