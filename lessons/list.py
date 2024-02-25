"""List"""

grocery_list: list[str] = list()
grocery_list: list[str] = []
print("Empty list: ")
print(grocery_list)

grocery_list.append("frosted flakes")
grocery_list.append("milk")
grocery_list.append("pizza")
print("After adding things: ")
print(grocery_list)


grocery_list2: list[str] = ["frosted flakes", "milk", "pizza"]
print("Already populated list: ")
print(grocery_list2)

grocery_list2.append("Whipping cream")
print("Add another thing: ")
print(grocery_list2)

print("Printing one item: ")
print(grocery_list2[2])

x: list[str] = ["c", "a", "r", "s"]
x[2] = "t"
print(x)

grocery_list.pop(0)
print(grocery_list)

def display(list: list[str]) -> None:
    print(list)

def create(item1: str, item2: str) -> list[str]:
    return [item1, item2]