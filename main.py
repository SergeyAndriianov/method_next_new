
class StringIterator:
    def __init__(self, input_string):
        self.input_string = input_string
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.input_string):
            char = self.input_string[self.index]
            self.index += 1
            return char
        else:
            raise StopIteration


input_string = "Hello, Serg!"
iterator = StringIterator(input_string)
for char in iterator:
    print(char)
