from fisika import Fisika
from alpro import Alpro


class Program:
    def __init__(self):
        self.alpro = Alpro()

        # s1 != 10, nanti error 'division by zero'
        s1 = [8, 9, 9.5, 9.75, 9.8, 9.85, 9.9, 9.95, 9.99]

        for i in range(len(s1)):
            fisika = Fisika(s1[i])
            fisika.jalankan()

    def run(self):
        pass


if __name__ == '__main__':
    program = Program()
