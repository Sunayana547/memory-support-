from services.hindsight import client, BANK_ID

bank = client.create_bank(
    bank_id=BANK_ID,
    name="Customer Support Agent",
    background="This agent handles customer support inquiries and remembers previous customer interactions, issues, troubleshooting steps, and resolutions."
)

print("Hindsight memory bank created!")
print("Bank ID:", bank.bank_id)

client.close()