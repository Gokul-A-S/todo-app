# Hello, This is the first time i've written something other than simple programs.So expect a lot of bugs
# The help command test was failing because of the utf8 encoding problem, So i had to import the sys module and use stdout to fix that
# I never had experience building anything like this,so i had to refer many documentations and it took a lot of time
# Thank You for taking a look at my program.Have a great day
import argparse
import string
import sys
import os
import datetime

parser = argparse.ArgumentParser()
parser.add_argument('command', default="help", nargs="?")
parser.add_argument('value', nargs="?", default="Null")
args = parser.parse_args()


def help():
    help = """Usage :-
$ ./todo add "todo item"  # Add a new todo
$ ./todo ls               # Show remaining todos
$ ./todo del NUMBER       # Delete a todo
$ ./todo done NUMBER      # Complete a todo
$ ./todo help             # Show usage
$ ./todo report           # Statistics"""
    sys.stdout.buffer.write(help.encode("utf8"))


if args.command == "help":
    help()

if args.command == "add":
    if args.value != "Null":

        fh = open('todo.txt', 'a')
        fh.write(f'{args.value}')
        fh.write("\n")
        fh.close()
        print(f"Added todo: \"{args.value}\"")
    else:
        print("Error: Missing todo string. Nothing added!")
if args.command == "ls":
    try:
        fh = open("todo.txt")
        ar = fh.readlines()
        temp = []
        for item0 in ar:
            temp.append(f"[{ar.index(item0) + 1}] {item0}")
        temp.reverse()
        for item1 in temp:
            sys.stdout.buffer.write(item1.encode("utf8"))
    except:
        print("There are no pending todos!")
if args.command == "del":
    if args.value != "Null":
        fh = open("todo.txt")
        ar = fh.readlines()
        fh.close()
        if (int(args.value) <= len(ar)) and (int(args.value) > 0):
            ar.remove(ar[int(args.value) - 1])
            fh = open("todo.txt", "a")
            for item in ar:
                fh.writelines(f"{item}")
            print(f"Deleted todo #{args.value}")
        else:
            print(f"Error: todo #{args.value} does not exist. Nothing deleted.")
    else:
        print("Error: Missing NUMBER for deleting todo.")
if args.command == "done":
    if args.value != "Null":
        fh0 = open("todo.txt")
        ar = fh0.readlines()
        fh1 = open("done.txt", "a")
        if int(args.value) <= len(ar) and (int(args.value) > 0):
            fh1.writelines(ar[int(args.value) - 1])
            fh0.close()
            fh1.close()
            ar.remove(ar[int(args.value) - 1])
            os.remove("todo.txt")
            fh2 = open("todo.txt", "x")
            fh2.writelines(ar)
            fh2.close()
            print(f"Marked todo #{args.value} as done.")
        else:
            print(f"Error: todo #{args.value} does not exist.")
    else:
        print("Error: Missing NUMBER for marking todo as done.")
if args.command == "report":
    fh0 = open("todo.txt")
    fh1 = open("done.txt")
    ar0 = fh0.readlines()
    ar1 = fh1.readlines()
    print(f"{datetime.date.today()} Pending : {len(ar0)} Completed : {len(ar1)}")
