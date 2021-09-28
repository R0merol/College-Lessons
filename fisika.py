from sympy import *


class Fisika:
    def __init__(self, t1):
        self.t1 = t1
        self.t2 = 10
        self.s1 = 0
        self.s2 = 0
        self.d_t = 0
        self.d_s = 0

    def jalankan(self):
        print(f"Waktu t1: {self.t1}")
        print(f"Waktu t2: {self.t2}")
        self.s1 = self.hitung_s(self.t1)
        print(f"Jarak s1: {self.s1}")
        self.s2 = self.hitung_s(self.t2)
        print(f"Jarak s2: {self.s2}")
        self.hitung_delta_s()
        self.hitung_delta_t()
        self.hitung_laju_rata2()
        print("-----------------------------------")

    @staticmethod
    def hitung_s(t):
        # s(t) = 2t^2 + 4t
        return round(2 * pow(t, 2) + 4 * t, 10)

    def hitung_delta_s(self):
        self.d_s = round(self.s2 - self.s1, 10)
        print(f"Delta s: {self.d_s}")

    def hitung_delta_t(self):
        self.d_t = round(self.t2 - self.t1, 10)
        print(f"Delta t: {self.d_t}")

    def hitung_laju_rata2(self):
        hasil = round(self.d_s / self.d_t, 10)
        print(f"Laju rata-rata: {hasil}")
