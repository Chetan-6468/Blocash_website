import random
import time

# Generate a random transaction ID
timestamp = str(time.time())
rand_num = str(random.randint(0, 9999))
transaction_id = timestamp + rand_num

# Transaction details
payer_info = {'name': 'John Doe', 'account': '1234567890'}
payee_info = {'name': 'Jane Doe', 'account': '0987654321'}
amount = 100.0

# Combine all transaction details into a single message string
message = f'Transaction ID: {transaction_id}\n' \
          f'Payer Information: {payer_info}\n' \
          f'Payee Information: {payee_info}\n' \
          f'Amount: {amount}'

print(message)
