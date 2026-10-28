import json
import uuid

def create_ticket():
    title = input("Enter title: ")
    if not title:
        print("Title must not be empty")
        return

    description = input("Enter description: ")
    if not description:
        print("Description must not be empty")
        return

    ticket = {
        "id": str(uuid.uuid4()),
        "title": title,
        "description": description,
        
    }
    try:
        with open("tickets.json", "r")as file:
            json.load(file)

    except FileNotFoundError:
        tickets = []
        tickets.append(ticket)

    with open("tickets.json", "w")as file:
        json.dump(tickets, file, indent=4)
        
        print("Ticket added successfully")
        print("Ticket Id: ", ticket["id"])

def main():
    while True:
        print("CAMPUS FLOW")
        print("1.create ticket")
        print("2. Quite")

        choice = input("\nchoose option 1 or 2: ")
        if choice == "1":
            create_ticket()

        elif choice == "2":
            print("GOODBYE")
            break

        else:
            print("Invalid input choose 1 or 2")
            continue
main()