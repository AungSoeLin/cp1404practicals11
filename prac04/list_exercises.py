numbers=[5,20,1,2,3]
print("The First Number is",numbers[0])
print("The Last Number is",numbers[4])
print("The Smallest Number is",min(numbers))
print("The Largest Number is",max(numbers))
average = sum(numbers)/5
print("The average of the numbers is",average)


usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
name = input("Enter your name:")
if name in usernames:
    print("Access Granted")
else:
    print("Access Denied")