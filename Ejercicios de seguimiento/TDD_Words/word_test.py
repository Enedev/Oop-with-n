import pytest
from word import Word
from letter import Character

class TestWord:

    def test_convert(self):
        word_str = "computer"
        character_list = []

        word_obj = Word(word_str)
        for char in word_str:
            character = Character(char)
            character_list.append(character)
        assert word_obj.characters == character_list

    def test_count_vowels(self):
        word_str = "Friend"
        word_obj = Word(word_str)
        assert word_obj.count_vowels() == 2

    def test_reverse_word(self):
        word_str = "Elephant"
        word_obj = Word(word_str)
        reversed_word = word_str[::-1]
        assert word_obj.reverse_word() == reversed_word
