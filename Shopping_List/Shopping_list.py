import sys
import io

# print out instructions on how to use the app
def show_help():
    print("What should we pick up at the store?")
    print("""
    Enter 'DONE' to stop adding items".
    Enter 'HELP' for this help.
    Enter 'SHOW' to see your current list.
    Enter 'CLEAR' to clear your current list.
    """)

# print out the list
def show_list():
    with open("list.txt") as file:
        i = 1
        for thing in file:
            print("{} - {}".format(i, thing))
            i = i + 1

# add new items to our list
def add_to_list(new_item):
    # shopping_list.append(new_item)
    with open("list.txt", "a") as file:
        file.write(new_item + "\n")
    print("Added {}. List now has {} items.".format(new_item, len(open('list.txt').readlines())))

# clear the list
def clear():
    f = open('list.txt', 'w')
    f.close()

# main function
def main():
    show_help()

    while True:
        # ask for new items
        new_item = input("> ")

        # be able to quit the app
        if new_item == "DONE":
            break
        elif new_item == "HELP":
            show_help()
            continue
        elif new_item == "SHOW":
            show_list()
            continue
        elif new_item == "CLEAR":
            clear()
            continue
        else:
            add_to_list(new_item)

main()
