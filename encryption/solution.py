ALPHABET = " abcdefghijklmnopqrstuvwxyz."
word_dict = {ALPHABET[i]: i for i in range(len(ALPHABET))}


def convert(word: str, key: str, dictionary: dict) -> str:
    """
    Decrypts a word
    :param dictionary: dictionary rule to go for
    :param key: the key
    :param word: the word to be decrypted
    :return: the resulting word
    """
    full_key = "".join([key[i % len(key)] for i in range(len(word))])
    message = ""

    for i in range(len(word) - 1):
        num = dictionary[word[i]] - dictionary[full_key[i]]
        if num < 0:
            num = len(ALPHABET) + num

        for key, value in dictionary.items():
            if value == num:
                message += key
    return message


if __name__ == "__main__":
    print(convert("wnlgbnovtezjznqquqtaoneejfmifxfb nez.j iem.", "genial boese", word_dict))
