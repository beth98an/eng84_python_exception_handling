# Dealing with files and error/exception handling

# There is a built in method in python called open("")
file = open("orders.text") # Looks for a file called orders.text
# keyword try

try:
    file = open("orders.text")
    print("file was found")
except FileNotFoundError as errmsg:
    print(f"the above block of code was not executed {errmsg}")
    raise
finally:
    print("The file is found, your task is to read the data and display it as a list")

# second iteration
# your task is to read the data and display it as a list
f = open("orders.text", "r")
print(f.read())
# third iteration




