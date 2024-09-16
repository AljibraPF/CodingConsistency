class DictionaryLooper:
    def __init__(self, data):
        self.data = data 
    
    def iterate_dict(self):
        for key, value in self.data.items():
            print(f"Key: {key}, Value: {value}")

my_dict = {
    "apple": 1,
    "banana": 2,
    "cherry": 3
}

obj = DictionaryLooper(my_dict)

obj.iterate_dict()
