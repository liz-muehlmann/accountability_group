#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Jul 03, 2023 12:58:13

@author: boyun
"""
# Day 18 lectures

# adding complete and exit buttons


import functions
import time                     # standard module
# right click > go to > implementations

now = time.strftime("%b %d, %Y %H:%M:%S") # google python datetime format code for more
print ("It is", now)

while True:
    user_action = input("Type add, show, edit, complete, or exit. ")
    user_action = user_action.lower().strip()

    todos = functions.get_todos()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos.append(todo.capitalize() + "\n")

        functions.write_todos(todos)

    elif user_action.startswith("show"):
        print("You have ", len(todos), " items on your todo list")
        for index, item in enumerate(todos):
            item = item.title().strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])

            existing_todo = todos [number - 1]

            new_todo = input("What would you like to replace '" + existing_todo.strip('\n') + "' with? ")
            todos[number - 1] = new_todo + '\n'

            functions.write_todos(todos)                   # in the perenteses: the argument value

            print("Successfully edited!")
        except ValueError:
            print("Error: Invalid command.")
            continue                        # goes back to the beginning
        except IndexError:
            print("Error: There's no item with that number.")
            continue


    elif user_action.startswith('complete'):
         try:
            number = int(user_action[9:])
            index = number - 1
            todo_to_remove = todos[index].strip('\n')

            todos.pop(index)

            functions.write_todos(todos)

            print(f"'{todo_to_remove}' is complete. Good job!")
         except ValueError:
             print("Error: Invalid command.")
             continue
         except IndexError:
             print("Error: There's no item with that number.")
             continue

    elif user_action.startswith("exit") or user_action.startswith("done"):
        break

    else:
        print("Error: Command is not valid")

print("Bye!")

