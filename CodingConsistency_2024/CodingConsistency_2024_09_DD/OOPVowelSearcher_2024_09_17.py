class FinderVowel:
    def __init__(self,words):
        self.words = words
        self.vowel = ["a","i","u","e","o"]
    
    def FindVowel(self):
        vowelfounded = []
        for i in self.words:
            if i in self.vowel:
                vowelfounded.append(i)
        return vowelfounded

vf = FinderVowel("This is a Text")

print(vf.FindVowel())