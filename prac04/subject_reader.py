"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    print(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        part = line.split(',')  # Separate the data into its parts
        print(part)  # See what the parts look like (notice the integer is a string)
        part[2] = int(part[2])  # Make the number an integer (ignore PyCharm's warning)
        print(part)  # See if that worked
        parts.append(part)
        print(parts)
        print("----------")
    input_file.close()


main()