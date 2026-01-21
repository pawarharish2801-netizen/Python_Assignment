
def calculate_area(length, width):
    return length * width
def main():
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))

    ret = calculate_area(length, width)
    print("The area of the rectangle is : ", ret)

if __name__ == "__main__":
    main() 