import hashlib
import json

# Define transaction details
transaction = {
    "transaction_id": "abc123",
    "amount": 100.00,
    "payer": {
        "name": "John Doe",
        "email": "john@example.com",
        "address": "123 Main St, Anytown USA"
    },
    "payee": {
        "name": "Jane Smith",
        "email": "jane@example.com",
        "address": "456 Oak Ave, Anycity USA"
    }
}

# Convert transaction to a JSON string
transaction_string = json.dumps(transaction)

# Generate SHA256 hash of the transaction string
hash_object = hashlib.sha256()
hash_object.update(transaction_string.encode('utf-8'))
hash_value = hash_object.hexdigest()

# Combine transaction ID with transaction details
message_string = f"Transaction ID: {transaction['transaction_id']}\n" \
                 f"Amount: ${transaction['amount']}\n" \
                 f"Payer: {transaction['payer']['name']} ({transaction['payer']['email']})\n" \
                 f"Payee: {transaction['payee']['name']} ({transaction['payee']['email']})\n" \
                 f"Hash value: {hash_value}"

# Print the message string
print(message_string)
print("Hello world")