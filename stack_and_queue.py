def stack(our_list, operation, new_element=None):
    if operation == 'add':
        our_list.append(new_element)
    elif operation == 'remove':
        if our_list:
            our_list.pop()
        else:
            print("Stack is empty, cannot remove element.")
    return our_list

def queue(our_list, operation, new_element=None):
    if operation == 'add':
        our_list.append(new_element)
    elif operation == 'remove':
        if our_list:
            our_list.pop(0)
        else:
            print("Queue is empty, cannot remove element.")
    return our_list

# Example Usage
my_list = [1, 2, 3, 4]

print("Adding new element to the stack")
my_list = stack(my_list, 'add', 0)
print(my_list)

print("Adding remove an element to the stack")
my_list = stack(my_list, 'remove')
print(my_list)

print("Adding new element to the queue")
my_list = queue(my_list, 'add', 5)
print(my_list)

print("Adding remove an element to the queue")
my_list = queue(my_list, 'remove')
print(my_list)

