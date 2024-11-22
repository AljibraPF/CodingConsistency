import re

#Finds and counts how many of the same letters in a text

class TextAnalyzer:
    def __init__(self,text):
        self.text = text
    
    def count_many(self,char):
        matching = re.findall(re.escape(char), self.text)
        return len(matching)


text = "abccddeefffggghhhiiijjjkkllmmnnnoooppqqqrrrssstttuuuvvwwwxxxyyyzzz"
analyzing = TextAnalyzer(text)

character_to_find = "z"
count = analyzing.count_many(character_to_find)
print(f"Character {character_to_find} appears for {count}")