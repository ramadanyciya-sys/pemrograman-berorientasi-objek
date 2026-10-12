class PersegiPanjang:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def hitung_luas(self):
        return self.panjang * self.lebar

    def hitung_keliling(self):
        return 2 * (self.panjang + self.lebar)

    def info(self):
        print(f"Panjang   : {self.panjang}")
        print(f"Lebar     : {self.lebar}")
        print(f"Luas      : {self.hitung_luas()}")
        print(f"Keliling  : {self.hitung_keliling()}")


# Membuat object
pp1 = PersegiPanjang(8, 5)
pp2 = PersegiPanjang(12, 7)

print("=== Persegi Panjang 1 ===")
pp1.info()
print()
print("=== Persegi Panjang 2 ===")
pp2.info()
