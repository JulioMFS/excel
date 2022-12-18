import os
items = os.listdir(".")
print("Dir: ", items)
newlist = []
for names in items:
    if names.endswith(".py"):
        newlist.append(names)
print (newlist)