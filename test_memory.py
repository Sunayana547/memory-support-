from services.hindsight import client, BANK_ID

# Store a customer experience
client.retain(
    bank_id=BANK_ID,
    content="""
    Customer Rahul previously had a payment failure while using
    the Android mobile app. The support team asked Rahul to clear
    the application cache and retry the payment. The payment
    succeeded after this solution.
    """,
    context="Customer support interaction"
)

print("Memory stored successfully!")

# Retrieve the previous experience
result = client.recall(
    bank_id=BANK_ID,
    query="What happened when Rahul's payment failed previously?"
)

print("\nRelevant memories:")

for memory in result.results:
    print("-", memory.text)

client.close()