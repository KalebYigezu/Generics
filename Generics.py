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

s = GenericsList[str](["1", "2", "3", 4])
print(s.elements)


