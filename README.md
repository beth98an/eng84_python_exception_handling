# Dealing with files and Exception Handling in Python
## We have `try`, `except`, `raise`, and `finally` as our code blocks to handle the error or an exceptions


#### To understand the concept easily -
- Each block of code works as an if, elif, else block

```python
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
```
- Please ensure to create an `orders.text` if it does not exist
| Mode |Description|
| :----: |:---- |
|'r' |This is the default mode. It Opens a file for reading. |
|'w' |This Mode Opens file for writing. If file does not exist, it creates a new file. If, file exists it truncates the file.|
|'x' |Creates a new file. If file already exists, the operation fails.|
|'a' |Open file in append mode. If file does not exist, it creates a new file.|
|'t' |This is the default mode. It opens in text mode.|
|'b' |This opens in binary mode.
|'+' |This will open a file for reading and writing (updating)|

It is worth noting that the `+` operator can be used with

- Reading the data from a file and displaying it as a list
```
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
```

- Let's add an item to our `orders.text`
```
def write_to_file(f, order_item):
    try:
        with open(f, "w") as f:
            f.write(order_item + '\n')
    except FileNotFoundError:
        print("file cannot be found or directory is incorrect, please check the details provided")
        raise


write_to_file("order.text", "Ice Cream")
```