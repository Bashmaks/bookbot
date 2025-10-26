# Count words in the given text fragment
def count_words(text: str) -> int:
    return len(text.split())

# Counts frequency of characters in the given text
def count_char_frequency(text: str) -> dict:
    char_count = {}
    for c in text.lower():
        if c in char_count:
            char_count[c] += 1
        else:
            char_count[c] = 1
    return char_count

# Sorts the dictionary based on its content
def sort_frequencies(char_count: dict) -> list:
    def sort_on(items):
        return items["num"]
    char_count_list = [{"char": key, "num": value} for key,value in char_count.items()]
    char_count_list.sort(reverse=True, key=sort_on)
    return char_count_list

