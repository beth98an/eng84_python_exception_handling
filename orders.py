# Dealing with files and error/exception handling

# There is a built in method in python called open("")
file = open("orders.text")  # Looks for a file called orders.text
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
def open_and_print(f):
    try:
        with open(f, "r"):
            for line in f.readlines():
                print(line.rstrip('\n'))
    except FileNotFoundError:
        print("file cannot be found or directory is incorrect, please check the details provided")
        raise
    finally:
        print("\nPlease chose the items from the list  and enjoy your HAPPY MEAL")


open_and_print("orders.text")


# third iteration
# Let's add an item to our orders.text
def write_to_file(f, order_item):
    try:
        with open(f, "w") as f:
            f.write(order_item + '\n')
    except FileNotFoundError:
        print("file cannot be found or directory is incorrect, please check the details provided")
        raise


write_to_file("order.text", "Ice Cream")



