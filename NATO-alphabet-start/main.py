import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_data_frame = pandas.DataFrame(data)

phonetic_dictionary = {row.letter: row.code for (index, row) in nato_data_frame.iterrows()}

print(phonetic_dictionary)

word = input("Enter a word: ").upper()
word_split = [phonetic_dictionary[letter] for letter in word]

print(word_split)
