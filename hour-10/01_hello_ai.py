import requests

# 🔹 Step 1: Add your AI API endpoint here
AI_API_URL = "https://your-lambda-function-url-id.lambda-url.region.on.aws/"
# Example: "https://abcd1234.lambda-url.us-east-1.on.aws/"

# 🔹 Step 2: Write your question here
QUESTION = "Hello, who are you?"

def ask_ai(question):
    """
    Send a question directly to the AI (Large Language Model) and get its response.
    This connects directly to the AI service to get intelligent answers.
    """
    try:
        # Send question directly to AI
        response = requests.post(AI_API_URL, json={"question": question}, timeout=30)
        response.raise_for_status()  # check for errors

        # AI returns JSON response with the answer
        result = response.json()
        return result.get("answer", "⚠️ No answer received from AI")

    except Exception as e:
        return "❌ AI Connection Error: " + str(e)

def main():
    print("Direct AI Communication Demo")
    print("=" * 40)

    print("Question: " + QUESTION)
    print("\n Connecting to AI...")

    answer = ask_ai(QUESTION)

    print("\n AI Response:")
    print(answer)

if __name__ == "__main__":
    main()
