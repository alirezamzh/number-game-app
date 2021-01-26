# have a HELP command 
# have a SHOW command
# print out instructions on how use app 
def show_hlep():
    print("What should we pick up at the store?")
    print("""
Enter 'DONE' to stop adding items
Enter 'SHOW' to stop adding items
Enter 'HELP' to stop adding items
""")

def show_list():
    print("Here's your list: ")
    for item in shopping_list:
       print(item)
# add new items to out list
# print out the list 
# code refactoring

def add_to_list(new_item):
    shopping_list.append(new_item)
    print("Added {}. list now has {} items.".format(new_item,len(shopping_list)))
# make a list to hold into our items
shopping_list=[]


show_hlep()

# ask for new items
while True:
    new_item = input("> ")
    # be able to quit the app
    if new_item == 'DONE':
        break
    elif new_item=='HELP':
        show_hlep()
        continue

    elif new_item=='SHOW':
        show_list()
        continue
    add_to_list(new_item)
    

show_list()
# add new items to out list
# print out the list 
