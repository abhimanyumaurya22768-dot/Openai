import os
import sys

from openai import OpenAI


def main() -> None:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("Error: OPENAI_API_KEY is not set.")
        print("Set it in your terminal with: $env:OPENAI_API_KEY='your-key-here'")
        sys.exit(1)

    client = OpenAI(api_key=api_key)

    prompt = " ".join(sys.argv[1:])
    if not prompt:
        prompt = "Write a short greeting message in Python."

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": prompt},
            ],
            temperature=0.7,
            max_tokens=200,
        )
        print(response.choices[0].message.content)
    except Exception as exc:
        print(f"Error: API call failed: {exc}")
        sys.exit(1)


if __name__ == "__main__":
    main()
