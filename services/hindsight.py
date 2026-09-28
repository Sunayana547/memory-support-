import os
from dotenv import load_dotenv
from hindsight_client import Hindsight

load_dotenv()

BANK_ID = "customer-support-agent"


def _new_client():
    """Create a request-scoped client so aiohttp sessions never cross loops."""
    return Hindsight(
        base_url=os.environ["HINDSIGHT_BASE_URL"],
        api_key=os.environ["HINDSIGHT_API_KEY"]
    )


def recall_memories(query):
    with _new_client() as request_client:
        return request_client.recall(
            bank_id=BANK_ID,
            query=query
        )


def remember_interaction(customer_message, agent_response):
    content = f"""
    Customer interaction:

    Customer message:
    {customer_message}

    Support agent response:
    {agent_response}
    """

    with _new_client() as request_client:
        request_client.retain(
            bank_id=BANK_ID,
            content=content,
            context="Customer support interaction"
        )
