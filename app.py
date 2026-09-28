from flask import Flask, request, jsonify, render_template

from services.hindsight import recall_memories, remember_interaction
from services.llm import generate_response

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json()

    customer_message = data.get("message", "").strip()

    if not customer_message:
        return jsonify({
            "error": "Message cannot be empty"
        }), 400

    # 1. Retrieve relevant memories
    result = recall_memories(customer_message)

    # 2. Generate response using memories
    response = generate_response(
        customer_message,
        result.results
    )

    # 3. Store the new interaction
    remember_interaction(
        customer_message,
        response
    )

    # 4. Send response + memory information to frontend
    memories = [
        memory.text
        for memory in result.results
    ]

    return jsonify({
        "response": response,
        "memories": memories
    })


if __name__ == "__main__":
    app.run(debug=True)
