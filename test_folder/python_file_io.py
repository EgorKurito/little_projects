import sys

def rememberer(thing):
    # open file
    with open("database.txt", "a") as file:
        # write thing file
        file.write(thing + "\n")

def show():
    with open("database.txt") as file:
        for line in file:
            print(len(line))

if __name__ == '__main__':
    if sys.argv[1].lower() == '--list':
        show()
    else:
        rememberer(' '.join(sys.argv[1:]))
