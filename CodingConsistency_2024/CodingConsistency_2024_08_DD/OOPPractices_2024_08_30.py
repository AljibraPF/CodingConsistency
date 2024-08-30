class OOP():

    def __init__(self,words,anotherword) -> None:
        self.words = words
        self.anotherword = anotherword

    def stringfunction(self) -> str:
        print("This is ", self.words, "And This is ", self.anotherword)


obj = OOP("Alan","Timmy")
obj.stringfunction()

#Make sure to make a variable and reference it to a method next time