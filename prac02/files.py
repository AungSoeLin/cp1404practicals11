name = input("Enter you name:")
files = open("name.txt", "w")
files.write(name)
files.close()

files = open("name.txt", "r")
print("Your name is", files.read())
files.close()

files = open("number.txt", "r")
total = 0
for i in range(2):
    number = int(files.readline())
    total = total + number
print(total)


files = open("number.txt","r")
print(files.readlines())

