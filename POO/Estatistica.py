from collections import Counter

class Estatistica:
    def __init__(self, numbers: list[int]):
        self._numbers = numbers
    
    def media(self):
        return sum(self._numbers) / len(self._numbers)

    def mediana(self):
        numbers = sorted(self._numbers)
        index = len(numbers) // 2
        if len(numbers) % 2 == 0:
            return (numbers[index - 1] + numbers[index] / 2)
        return numbers[index]
    
    def moda(self):
        number, _ = Counter(self.numbers).most_common()[0]
        return number

