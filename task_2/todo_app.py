import csv
import datetime

STORAGE = "data/storage.csv"


def addItem(data: dict) -> None:
    with open(STORAGE, "a", newline="") as csv_file:
        write_dict = csv.DictWriter(csv_file, fieldnames=["Item", "Date"])
        write_dict.writerow(data)
    print(f"'{data['Item']}' is added into storage !")


def getAllItems() -> None:
    with open(STORAGE) as csv_file:
        rows = csv.reader(csv_file, delimiter=",")
        cnt = 1
        for row in rows:
            print(str(cnt) + "\t\t" + row[0] + "\t\t" + row[1] + "\n")
            cnt += 1


def deleteItem(name: str) -> None:
    updated_storage = []
    with open(STORAGE, newline="") as csv_file:
      rows = csv.reader(csv_file, delimiter=",")  
      for row in rows:            
        if row[0] != name:
            updated_storage.append(row)
      update(updated_storage)
    print(f"Task '{name}' is deleted from the storage !")


def doneItem(name: str) -> None:
    updated_storage = []
    day = datetime.datetime.today().strftime("%Y.%m.%d")
    with open(STORAGE, newline="") as csv_file:
        rows = csv.reader(csv_file, delimiter=",")
        for row in rows:            
            if row[0] == name:
                row[1] = f"{day}"
            updated_storage.append(row)
        update(updated_storage)
    print(f"{day} : you've completed task -> '{name}' !")


def update(updated_storage: list) -> None:
    with open(STORAGE,"w",newline="") as csv_file:
        write = csv.writer(csv_file)
        write.writerows(updated_storage)


def clearStorage() -> None:
    with open(STORAGE,"w") as csv_file:
        csv_file.truncate()
    print("Your storage is clear !")


def menu() -> None:
    print(
    """
         MENU
    ---------------

    1.) Add an item
    2.) Delete an item
    3.) Mark an item as done
    4.) List all items
    5.) Clear storage
    6.) Exit
    """
    )


if __name__ == "__main__":
    print("\n << Welcome to the TODO list app >> ")

    while True:
        menu()
        user_input = int(input("Enter your choice : "))

        if user_input == 1:
            count = int(input("How many items do you want to add : "))
            for _ in range(count):
                task = {'Item': '', 'Date': 'Not completed yet'}
                name = input("Enter your task name to add : ")
                task["Item"] = name
                addItem(task)

        elif user_input == 2:
            count = int(input("How many items do you want to delete : "))
            for _ in range(count):
                name = input("Enter your task name to delete : ")
                deleteItem(name)

        elif user_input == 3:
            name = input("Enter your task name which is done : ")
            doneItem(name)

        elif user_input == 4:
            print("\nNUMBER\t\tITEM NAME\tDATE OF FINISH\n")
            getAllItems()
        
        elif user_input == 5:
            clearStorage()
        
        else:
            print("\nSee you soon !\n")
            break
