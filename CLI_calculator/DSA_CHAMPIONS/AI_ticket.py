import json
import uuid
import os
import urllib.request
import urllib.error


def get_ai_suggestions(description):
    api_key = os.environ.get("GEMINI_API_KEY")

    if not api_key:
        print("AI unavailable: GEMINI_API_KEY is not set.")
        return

    url = (
        "https://googleapis.com"
        "v1beta/models/gemini-2.5-flash:generateContent"
    )

    prompt = (
        "You are a campus IT support assistant. "
        "Analyze the following campus support ticket. "
        "Suggest practical steps to investigate or fix the problem. "
        "Number your suggestions and explain them clearly.\n\n"
        f"Ticket description: {description}"
    )

    # Corrected JSON payload format for Gemini 2.5 API
    data = {
        "contents": [
            {
                "role": "user",
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }

    request = urllib.request.Request(
        url,
        data=json.dumps(data).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "x-goog-api-key": api_key
        },
        method="POST"
    )

    print("\nGetting AI suggestions...\n")

    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            result = json.loads(response.read().decode("utf-8"))

        suggestions = result["candidates"][0]["content"]["parts"][0]["text"]

        print("AI SUGGESTIONS")
        print(suggestions)

    except urllib.error.HTTPError as error:
        print(f"AI request failed (HTTP {error.code}).")
        try:
            # Reads and prints the exact error response message from Google's servers
            error_details = error.read().decode("utf-8")
            print(f"Details: {error_details}")
        except Exception:
            pass
        print("Check your API key, model availability, and usage limits.")

    except urllib.error.URLError:
        print("AI request failed. Check your internet connection.")

    except (KeyError, IndexError, TypeError, json.JSONDecodeError):
        print("AI returned an unexpected response. Please try again.")

    except TimeoutError:
        print("The AI request timed out. Please try again.")


def create_ticket():
    title = input("Enter title: ").strip()

    if not title:
        print("Title must not be empty")
        return

    description = input("Enter description: ").strip()

    if not description:
        print("Description must not be empty")
        return

    ticket = {
        "id": str(uuid.uuid4()),
        "title": title,
        "description": description
    }

    try:
        with open("tickets.json", "r") as file:
            tickets = json.load(file)

    except FileNotFoundError:
        tickets = []

    except json.JSONDecodeError:
        print("Cannot read tickets.json because its JSON is invalid.")
        return

    tickets.append(ticket)

    try:
        with open("tickets.json", "w") as file:
            json.dump(tickets, file, indent=4)

    except OSError:
        print("Could not save the ticket.")
        return

    print("\nTicket created successfully!")
    print("ID:", ticket["id"])
    print("Description:", ticket["description"])

    get_ai_suggestions(ticket["description"])


def main():
    while True:
        print("=== CAMPUS FLOW ==== ")
        print("1. Create ticket")
        print("2. Quit")

        choice = input("\nChoose option 1 or 2: ")

        if choice == "1":
            create_ticket()

        elif choice == "2":
            print("GOODBYE")
            break

        else:
            print("Invalid input. Choose 1 or 2.")


if __name__ == "__main__":
    main()
