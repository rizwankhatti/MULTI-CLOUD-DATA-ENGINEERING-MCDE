# Task 14 - Contact Manager
import json
import os

FILE = "contacts.json"

def load():                                   # storage: read
    if not os.path.exists(FILE):
        return []
    try:
        return json.load(open(FILE))
    except ValueError:
        print("File damaged - not touching it.")
        exit()

def save(contacts):                           # storage: write
    json.dump(contacts, open(FILE, "w"))

def find(contacts, cid):                      # logic: find by id
    for c in contacts:
        if c["id"] == cid:
            return c

contacts = load()
while True:
    choice = input("\n1 Add | 2 Search | 3 Update | 4 Delete | 5 List | 6 Exit: ")
    if choice == "1":
        cid = input("ID: ")
        if find(contacts, cid):
            print("ID already exists")
        else:
            contacts.append({"id": cid, "name": input("Name: "),
                             "phone": input("Phone: "), "email": input("Email: ")})
            save(contacts)
    elif choice == "2":
        text = input("Search: ").lower()
        for c in contacts:
            if text in c["name"].lower():
                print(c)
    elif choice == "3":
        c = find(contacts, input("ID: "))
        if c:
            c["name"] = input("New name: ")
            c["phone"] = input("New phone: ")
            c["email"] = input("New email: ")
            save(contacts)
        else:
            print("Not found")
    elif choice == "4":
        c = find(contacts, input("ID: "))
        if c:
            contacts.remove(c)
            save(contacts)
        else:
            print("Not found")
    elif choice == "5":
        for c in contacts:
            print(c)
    elif choice == "6":
        break
