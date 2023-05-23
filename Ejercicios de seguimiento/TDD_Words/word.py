from letter import Character

class Word:
    def __init__(self, word):
        self.characters = self.convert(word)

    def convert(self, string):
        character_list = []
        for char in string:
            character = Character(char)
            character_list.append(character)
        return character_list

    def count_vowels(self):
        vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        count = 0
        for char in self.characters:
            if char.attribute in vowels:
                count += 1
        print(f"The word has {count} vowels")
        return count

    def reverse_word(self):
        reversed_list = self.characters.copy()
        reversed_list.reverse()

        original_word = ""
        reversed_word = ""
        for char in self.characters:
            original_word += char.attribute
        for char in reversed_list:
            reversed_word += char.attribute
        print(f"The reversed form of {original_word} is: {reversed_word}")
        return reversed_word

word_obj = Word("Executing")
print(word_obj.characters)
word_obj.count_vowels()
word_obj.reverse_word()
