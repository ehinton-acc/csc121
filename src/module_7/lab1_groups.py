import re

def main():
    locs = {"+1": "United States and Canada", "+62": "Indonesia", "+505": "Nicaragua"}
    pattern = r"(?P<country_code>\+\d{1,3}) \d{3}-\d{3}-\d{4}"
    num = input("Number: ")

    match = re.search(pattern, num)
    if match:
        cc = match.group("country_code")
        print(locs[cc])
    else:
        print("Unknown")

main()