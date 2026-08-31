def area(length, width):
    area = length * width
    return area

def main():
    house = area(50, 20)
    yard = area(50, 50)
    total = house + yard
    print(str(total) + " square feet")

main()