def get_wordle_words() -> list[str]:
    """Reads the wordle words CSV file, and returns an all lowercase list of words."""
    file_path = "words.csv"
    data = ""
    with open(file_path, "r") as file:
        data = (file.read()).lower()
    return list(filter(lambda x: len(x) == 5, data.split("\n")))


def compare_placed_letters(letters: str, word: str) -> bool:
    while len(letters) < 5:
        letters += "-"
    for i in range(min(len(letters), len(word))):
        if not letters[i].isalpha():
            continue
        if letters[i] != word[i]:
            return False
    return True


def main():
    print("WORDLE GUESSER")
    possible_words = get_wordle_words()
    print("Got", len(possible_words), "words.")

    print("Letters in order (dashes for blanks):")
    found_placed = input(" ~ ")[:5].lower()
    print("Letters out of order:")
    found_unplaced = input(" ~ ").lower()
    print("Letters eliminated:")
    eliminated = input(" ~ ").lower()

    for letter in found_unplaced:
        possible_words = list(filter(lambda x: x.count(letter) != 0, possible_words))

    print("Got", len(possible_words), "words after eliminating unplaced.")

    possible_words = list(
        filter(lambda x: compare_placed_letters(found_placed, x), possible_words)
    )

    print("Got", len(possible_words), "words after eliminating placed.")

    for letter in eliminated:
        possible_words = list(filter(lambda x: letter not in x, possible_words))
    print("Got", len(possible_words), "words after eliminating eliminated.")

    print("Possible answers include:", possible_words)


if __name__ == "__main__":
    main()
