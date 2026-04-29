# 30. Mini Contact Book (CRUD)

# Build a contact system using a dictionary:
# * Add
# * Search
# * Delete
# * Display

contacts = {}

while True:

    print("Enter your choice \n1.Add \t 2.Search \t 3.Delete \t 4.Display \t 5.Exit")

    try:
        choice = int(input())
    except:
        print("Invalid input")
        continue
    if choice == 1:
        name = input("Enter name : ").strip().capitalize()
        Pnum = input("Enter phone num : ")
        if name in contacts:
            print("Contact already exists. Updating number . ")
        contacts[name] = Pnum
    elif choice == 2:  # search
        name = input("Enter the name : ").strip().capitalize()
        if name in contacts:
            print(name, "->", contacts[name])
        else:
            print("No such contact found !")
    elif choice == 3:  # delete
        name = input("Enter name to delete : ").strip().capitalize()
        if name in contacts:
            del contacts[name]
            print("Deleted Successfully ")
        else:
            print("No such contact found ")
    elif choice == 4:  # display
        if not contacts:
            print("No contact available ")
        else:
            print("Contacts")
            for name, num in contacts.items():
                print(name, ":", num)
    elif choice == 5:
        with open("contacts.txt", "w") as file:
            for name in sorted(contacts):
                file.write(f"{name}:{contacts[name]}\n")
        print("You wished to exit the program ")
        break
    else:
        print("Select only between 1 to 5 :")
