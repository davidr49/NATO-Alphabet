import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_data_frame = pandas.DataFrame(data)

phonetic_dictionary = {row.letter: row.code for (index, row) in nato_data_frame.iterrows()}

def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        word_split = [phonetic_dictionary[letter] for letter in word]
    except KeyError:
        print("Invalid entry. Use letters in the alphabet only.")
        generate_phonetic()
    else:
        print(word_split)

generate_phonetic()