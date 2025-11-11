def count_word(string: str, word: str) -> int:
    count = 0

    for w in string:
        if w == word:
            count += 1

    return count    