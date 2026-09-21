import helpers
def main():
    counts = {}
    words = helpers.get_words("address.txt")
    words = [word.lower() for word in words if len(word) > 4]
    counts = {word: words.count(word) for word in words}
    helpers.save_counts(counts)
main()# Refer to this module's readme