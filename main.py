def get_wordle_words() -> list[str]:
    """Reads the wordle words CSV file, and returns an all lowercase list of words."""
    file_path = "words.csv"
    data = ""
    with open(file_path, "r") as file:
        data = (file.read()).lower()
    return list(filter(lambda x: len(x) == 5, data.split("\n")))


def is_all_green_letter_correct(letters: str, word: str) -> bool:
    while len(letters) < 5:
        letters += "-"
    for i in range(min(len(letters), len(word))):
        if not letters[i].isalpha():
            continue
        if letters[i] != word[i]:
            return False
    return True


def is_any_orange_letter_in_wrong_place(letters: str, word: str) -> bool:
    result = True
    while len(letters) < 5:
        letters += "-"
    for i in range(min(len(letters), len(word))):
        if not letters[i].isalpha():
            continue
        if letters[i] == word[i]:
            result = False
    return result


def repl(possible_words: list[str]) -> tuple[bool, list[str]]:
    response = input(" ~ ")
    match response:
        case "help" | "?" | "what":
            print("  help: shows this message")
            print("  list: shows remaining words")
            print("  green: add green letters")
            print("  orange: add orange letters")
            print("  black: add black letters")
        case "quit" | "exit" | "close":
            return False, possible_words
        case "green":
            print("Letters in order (dashes for blanks):")
            found_placed = input(" ~ ")[:5].lower()
            possible_words = list(
                filter(
                    lambda x: is_all_green_letter_correct(found_placed, x),
                    possible_words,
                )
            )
        case "orange":
            print("Letters in order (dashes for blanks):")
            found_placed = input(" ~ ")[:5].lower()
            possible_words = list(
                filter(
                    lambda x: is_any_orange_letter_in_wrong_place(found_placed, x),
                    possible_words,
                )
            )
            for letter in found_placed:
                if not letter.isalpha():
                    continue
                possible_words = list(
                    filter(lambda x: x.count(letter) != 0, possible_words)
                )
        case "add":
            print("Letters out of order:")
            found_unplaced = input(" ~ ").lower()
            for letter in found_unplaced:
                possible_words = list(
                    filter(lambda x: x.count(letter) != 0, possible_words)
                )
        case "black":
            print("Letters eliminated:")
            eliminated = input(" ~ ").lower()
            for letter in eliminated:
                possible_words = list(filter(lambda x: letter not in x, possible_words))
        case "show" | "list":
            print("Possible answers include:", possible_words)

    return True, possible_words


def main() -> None:
    print("WORDLE HELPER")
    possible_words = get_wordle_words()
    print("Got", len(possible_words), "words.")

    looping = True
    while looping:
        looping, possible_words = repl(possible_words)
        print(len(possible_words), "words left.")
        if not looping:
            break


if __name__ == "__main__":
    main()
