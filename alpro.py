import random


class Alpro:
    def run(self):
        print("Something something idk")
        print(self.hitung())
        self.hitung_luas()

    @staticmethod
    def hitung():
        num1 = input("Input first number: ")
        num2 = input("Input second number: ")
        result = int(num1) * int(num2)
        return result

    @staticmethod
    def hitung_luas():
        sisi = int(input("Masukkan sisi: "))
        hasil = sisi * sisi
        print(hasil)


def soal_1():
    a = input("Masukkan angkanya: ")
    i = 0
    jumlah = 0

    while i < int(a):
        print(jumlah)
        jumlah += 1
        i += 1


def soal_2():
    a = input("Masukkan angkanya: ")
    jumlah = 0

    for i in range(int(a)):
        print(jumlah)
        jumlah += 2


def jalankan(n):
    if n > 0:
        jalankan(n // 5)
        print(n % 5 + 1)


def xor_operator():
    # the ^ operator is an XOR operator
    x = [
        1 ^ 2,  # 0001 ^ 0010 = 0011 (3)
        2 ^ 2,  # 0010 ^ 0010 = 0000 (0)
        4 ^ 1,  # 0100 ^ 0001 = 0101 (5)
        3 ^ 3,  # 0011 ^ 0011 = 0000 (0)
        1 ^ 7,  # 0001 ^ 0111 = 0110 (6)
    ]
    for i in range(len(x)):
        print(x[i])


def compress_list():
    a = [x for x in range(1, 10)]
    print(a)

    b = [x**2 for x in range(1, 10)]
    print(b)

    c = [random.randint(1, 30) for _ in range(5)]
    print(c)

    games = ["Rimworld", "Roblox", "Raiden II", "Factorio", "Rob the robber", "Bambang", "Halo", "Yes"]
    r_games = [title for title in games if title.startswith("R")]
    print(r_games)

    movies = [("Avengers", 100), ("Blade Runner", 200), ("For Mankind", 300), ("Mr. Robot", 400), ("iCarly", 500)]
    expensive_movies = [title for (title, price) in movies if price >= 300]
    print(expensive_movies)

    v = [2, -3, 1]
    skalar_v = [x*4 for x in v]
    print(skalar_v)

    a = [1, 3]
    b = ['x', 'y']
    c = [(x, y) for x in a for y in b]
    print(c)


def soal_abiyaz():
    # Hitung jumlah bilangan prima
    num = int(input("N = "))
    list_prima = []
    for i in range(1, num + 1):
        if i != 0 and i != 1:
            n = 2
            prima = True
            while n < i and prima:
                if i % n == 0:
                    prima = False
                n = n + 1
            if prima:
                list_prima.append(i)
    print(f"Bilangan prima = {list_prima}")

    # Hitung jumlah penambahan yang mungkin
    jumlah_penambahan = 0
    ada_prima = False
    for i in list_prima:
        for j in list_prima:
            if i + j == num:
                print(f"{i} + {j} = {num}")
                list_prima.remove(list_prima[0])
                jumlah_penambahan += 1
                ada_prima = True

    # Cek apakah ada jumlah penambahan atau tidak
    if ada_prima:
        print(f"Jumlah penambahan bilangan prima = {jumlah_penambahan}")
    else:
        print("Tidak ada bilangan prima")
