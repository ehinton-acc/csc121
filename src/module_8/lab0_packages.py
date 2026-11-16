class Package:
    def __init__(self, number, sender, recipient, weight):
        self.number = number
        self.sender = sender
        self.recipient = recipient
        self.weight = weight

def main():
    packages = [Package(1, "Alice", "Bob", 10), Package(2, "Bob", "Charlie", 5)]

main()