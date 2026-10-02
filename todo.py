l1=[]
def load():
    try:
        with open("lst.txt", "r") as f:
            for line in f:
                l1.append(line.strip())
    except :
        pass

def save():
    with open("lst.txt", "w") as f:
        for task in l1:
            f.write(task + "\n")
def add():
    print(" ONLY SMALL LETTER WORDS")
    work=input("Enter to-do work: ")
    l1.append(work)
    save()

def remove():
    print(" ONLY SMALL LETTER WORDS")
    rmv=input("Enter work to remove: ")
    if rmv in l1:
        l1.remove(rmv)
        save()
        print("Work removed from the list..")
        
    else:
        print("work not found in the list")

def view():
    if not l1:
        print("No tasks in the list.")
    else:
        print("\n--- To-do list ---")
        for i, task in enumerate(l1, start=1):
            print(f"{i}. {task}")

load()

print("---MENU---")
print("Click 1 to add work in list: ")
print("Click 2 to remove work in list: ")
print("Click 3 to VIEW work in list: ")
print("Click 4 to Exit from list: ")

while True:
    choice=int(input("Enter choice: "))
    match choice:
        case 1:
            
            add()
            
            print("Work added successfully..")
        case 2:
            remove()
            
        case 3:
            print("---To-do list..")
            view()
        case 4:
            print("Exting from list...")
            break 
        case _:
            print("Envalid choice enter( 1 to 4 only )")

