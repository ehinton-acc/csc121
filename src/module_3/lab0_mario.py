def main():
    h = int(input("Height: "))
    pyramid(h)
def pyramid(n):
    for i in range(n):
        print("#" * i)
if __name__ == "__main__":
    main()