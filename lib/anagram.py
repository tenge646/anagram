class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, word_list):
        anagrams = []
        normalized_word = sorted(self.word)
        
        for candidate in word_list:
            normalized_candidate = sorted(candidate.lower())
            
            if normalized_candidate == normalized_word and candidate.lower() != self.word:
                anagrams.append(candidate)

        return anagrams
listen = Anagram("listen")
result = listen.match(['enlists', 'google', 'inlets', 'banana'])
print(result)