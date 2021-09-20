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
