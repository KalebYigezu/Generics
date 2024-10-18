from typing import List
'''
class IntList:
    def __init__(self, elements: List[int]) -> None:
        self.elements = elements

class FloatList:
    def __init__(self, elements: List[float]) -> None:
        self.elements = elements

class StringList:
    def __init__(self, elements: List[str]) -> None:
        self.elements = elements
'''
class GenericsList[T]:
    def __init__(self, elements: List[T]) -> None:
        self.elements = elements

i = GenericsList[int]([1, 2, 3, 4])
print(sum(i.elements))

f = GenericsList[float]([1.5, 2.5, 2.5, 3.5])
print(sum(f.elements))

s = GenericsList[str](["1", "2", "3", "4"])
print(s.elements)
----------------------------------------------------------------------

class Converter[T]:
    def __init__(self):
        self.__orig_class__ = None

    def convert(self, input_text: str) -> T:
        generic_type = self.__orig_class__.__args__[0]
        if input_text:
            return generic_type(input_text)
        else:
            return generic_type()


print(Converter[int]().convert("4"))
print(Converter[int]().convert(""))
print(Converter[float]().convert("2.3"))
print(Converter[float]().convert(""))


