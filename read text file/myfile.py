import time
import os

with open("fruits.txt") as file:
    content = file.read()
print(content)

# write text in a file
# w - write
# a - append
with open("vegetables.txt", "w+") as file:
    contentw = file.write("Tomato\nCucumber\nOnion")
    contentw = file.write("\nGarlic")
    contentw = file.seek(0)
    contentw = file.read()
print(contentw)

# uncomment me
while True:
    if os.path.exists("vegetable.txt"):
        with open("vegetables.txt") as file:
            contentw = file.read()
            print(contentw)
    else:
        print("File does not exists")
    time.sleep(3)

# check file path T or F
print(os.path.exists("vegetables.txt"))