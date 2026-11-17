from flask import Flask, render_template, request, jsonify
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

app = Flask(__name__)

load_dotenv()

# Gemini API configuration
api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key) if api_key else None

MODEL = "gemini-3.8-flash"


def generate_ai_response(prompt, system_instruction, temperature=0.7):
    if not client:
        raise ValueError("Gemini API key is missing. Please configure GEMINI_API_KEY.")

    response = client.models.generate_content(
        model=MODEL,
        contents=prompt,
        config=types.GenerateContentConfig(
            system_instruction=system_instruction,
            temperature=temperature,
            max_output_tokens=1024
        )
    )

    if not response.text:
        raise ValueError("The AI returned an empty response. Please try again.")

    return response.text.strip()


@app.route("/")
def hello_world():
    return render_template("index.html")


# Ask Anything
@app.route("/ask", methods=["POST"])
def ask():
    question = request.form.get("question", "").strip()

    if not question:
        return jsonify({"response": "Please enter a question."}), 400

    try:
        answer = generate_ai_response(
            prompt=question,
            system_instruction="Act like a helpful, friendly and intelligent personal AI assistant.",
            temperature=0.7
        )

        return jsonify({"response": answer}), 200

    except Exception as e:
        app.logger.exception("Ask AI error")
        return jsonify({"response": f"AI Error: {str(e)}"}), 500


# Email Summarizer
@app.route("/summarize", methods=["POST"])
def summarize():
    email_text = request.form.get("email", "").strip()

    if not email_text:
        return jsonify({"response": "Please paste an email to summarize."}), 400

    try:
        summary = generate_ai_response(
            prompt=f"Summarize the following email in 2-3 clear sentences:\n\n{email_text}",
            system_instruction="Act like an expert email assistant. Create accurate, concise and easy-to-understand email summaries.",
            temperature=0.3
        )

        return jsonify({"response": summary}), 200

    except Exception as e:
        app.logger.exception("Email summarizer error")
        return jsonify({"response": f"AI Error: {str(e)}"}), 500


if __name__ == "__main__":
    app.run(debug=True)
