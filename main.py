from flask import Flask, render_template, request, jsonify
import os
import time
import random

from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

app = Flask(__name__)

# BOT NYRA configuration
APP_NAME = "BOT NYRA"
MODEL = "gemini-3.8-flash"

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key) if api_key else None


# NYRA AI engine
def generate_ai_response(
    prompt,
    system_instruction,
    temperature=0.7,
    max_retries=3
):
    if not client:
        raise ValueError(
            "NYRA needs a Gemini API key. "
            "Please configure GEMINI_API_KEY."
        )

    for attempt in range(max_retries):
        try:
            response = client.models.generate_content(
                model=MODEL,
                contents=prompt,
                config=types.GenerateContentConfig(
                    system_instruction=system_instruction,
                    temperature=temperature
                )
            )

            if not response.text:
                raise ValueError("NYRA returned an empty response.")

            return response.text.strip()

        except Exception as e:
            error = str(e).upper()

            temporary_errors = [
                "500", "502", "503", "504",
                "UNAVAILABLE", "INTERNAL",
                "DEADLINE_EXCEEDED"
            ]

            is_temporary = any(
                code in error for code in temporary_errors
            )

            app.logger.warning(
                "NYRA attempt %s failed: %s",
                attempt + 1, e
            )

            if is_temporary and attempt < max_retries - 1:
                delay = (2 ** attempt) + random.uniform(0, 1)
                time.sleep(delay)
                continue

            if is_temporary:
                raise ValueError(
                    "NYRA is experiencing heavy traffic. "
                    "Please try again shortly."
                )

            raise

    raise ValueError("NYRA could not complete your request.")


# NYRA home page
@app.route("/")
def home():
    return render_template("index.html")


# Ask NYRA
@app.route("/ask", methods=["POST"])
def ask():
    question = request.form.get("question", "").strip()

    if not question:
        return jsonify({
            "response": "Hey! What would you like to ask me?"
        }), 400

    try:
        answer = generate_ai_response(
            prompt=question,
            system_instruction=(
                "You are NYRA, a friendly, intelligent and "
                "helpful personal AI companion. "
                "Your personality is warm, natural, thoughtful "
                "and conversational. Give accurate, clear and "
                "useful answers. Introduce yourself as NYRA "
                "when appropriate."
            ),
            temperature=0.7
        )

        return jsonify({"response": answer}), 200

    except Exception as e:
        app.logger.exception("NYRA Ask error")
        return jsonify({"response": str(e)}), 500


# NYRA Email Summarizer
@app.route("/summarize", methods=["POST"])
def summarize():
    email_text = request.form.get("email", "").strip()

    if not email_text:
        return jsonify({
            "response": "Please paste an email to summarize."
        }), 400

    try:
        summary = generate_ai_response(
            prompt=(
                "Summarize this email in 2-3 clear sentences. "
                "Preserve important information:\n\n"
                + email_text
            ),
            system_instruction=(
                "You are NYRA, an expert email assistant. "
                "Create accurate, concise and easy-to-understand "
                "email summaries."
            ),
            temperature=0.3
        )

        return jsonify({"response": summary}), 200

    except Exception as e:
        app.logger.exception("NYRA Summarizer error")
        return jsonify({"response": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
