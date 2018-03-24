import random

import os

report_book = []


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")
            

def show_help():
    clear_screen()
    print("Would you care to enter a new subject? ")
    print("""
Enter 'DONE' to stop adding subjects.
Enter 'HELP' for help.
Enter 'SHOW' to see your subjects .
Enter 'REMOVE' to delete a subject from your report_book.
""")
            
def add_to_report_book(subject):
    show_report_book()
    if len(report_book):
        position = input("Where should i add {}?\n"
                         "Press ENTER to add to the end of the report_book\n"
                         "> ".format(subject))
    else:
        position = 0
                
    try:
        position = abs(int(position))
    except ValueError:
        position = None
    if position is not None:
        report_book.insert(position-1, subject)
    else:
        report_book.append(new_subject)
    
    show_book()
            
def show_report_book():
    clear_screen()
            
    print("Here's your book:")
            

    for index, item in enumerate(report_book, start = 1):
        print("{}. {}".format(index, subject))
    
    print("-"*10)
    
def remove_from_report_book():
    show_list()
    what_to_remove = input("What would you like to remove?\n> ")
    try:
        report_book.remove(what_to_remove)
    except ValueError:
        pass
    show_report_book()

show_help()
            
while True:
    new_subject = input("> ")
            
    if new_subject.upper() == 'DONE' or new_subject.upper() == 'QUIT':
        break
    elif new_subject.upper() == 'HELP':
        show_help()
        continue
    elif new_subject.upper() == 'SHOW':
        show_list()
        continue
    elif new_subject.upper() == 'REMOVE':
        remove_from_report_book()
    else: 
        add_to_report_book(new_subject)

show_report_book()