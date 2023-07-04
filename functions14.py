FILEPATH = "todos.txt"
# this makes it easier to edit later

def get_todos(filepath=FILEPATH):            # the "todos.txt" is a default argument
    """Read a text file and return 
    the list of to-do items
    """         # this is a doc string. Useful when I have multiple python files working in a program
    with open(filepath,'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

#print(help(get_todos))
def write_todos(todos_arg, filepath=FILEPATH):              # parameters have been added # non-default parameters should come first
    """Write the to-do items list in the text file"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)
                #function return

# print("hello from functions")
# note that importing in TodoList program executes the print
# print(x)
# this will produce an error, because x is not defined
# it will also immediately terminate the program

#print(__name__)                     # executes only when the functions itself is executed

if __name__ == "__main__":          # if conditional block
    print("Hello")
    print(get_todos())
