
def calculate_area(radius):
    pi = 3.14159
    Area = pi * radius * radius
    return Area

def main():
    radius = float(input("Enter the radius of the circle: "))

    ret = calculate_area(radius)
    print("The area of the circle is : ", ret)

if __name__ == "__main__":
    main() 