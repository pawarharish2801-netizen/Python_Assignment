import os
import sys

def main():
    filename = input("Enter filename: ")
    search_string = input("Enter string to search: ")

    file = open(filename, 'r')
    content = file.read()
    file.close()

    count = content.count(search_string)

    print(f"'{search_string}' appears {count} times in {filename}")


if __name__ == "__main__":
    main()