class Anagram:
    def __init__(self, word):
        self.word = word
    def match(self, word_list): 
        anagrams = [letter for letter in word_list if self.is_anagram(letter)]
        return anagrams 
    def is_anagram(self, new_word):
        return sorted(self.word.lower()) == sorted(new_word.lower())