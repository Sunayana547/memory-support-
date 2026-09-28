from services.hindsight import client, BANK_ID, remember_interaction
from services.llm import generate_response


customer_message = "My payment failed again."

# 1. Retrieve relevant memories
result = client.recall(
    bank_id=BANK_ID,
    query=customer_message
)

print("MEMORIES RETRIEVED:")

for memory in result.results:
    print("-", memory.text)


# 2. Generate response using memory + current message
response = generate_response(
    customer_message,
    result.results
)

print("\nAI AGENT RESPONSE:")
print(response)


# 3. Store this new interaction
remember_interaction(
    customer_message,
    response
)

print("\nNew interaction stored in Hindsight.")

client.close()