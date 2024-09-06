class ReferencingTest:
    def __init__(self,word,word2,word3) -> None:
        self.word = word
        self.word2 = word2
        self.word3 = word3
    
    def methodCalling(self):
        print(f"This is the first word {self.word}, and this is the {self.word2} and {self.word3}")


obj = ReferencingTest("FirstWord","SecondWord","ThirdWord")
obj.methodCalling()