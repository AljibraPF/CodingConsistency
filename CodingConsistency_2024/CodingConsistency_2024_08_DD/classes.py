class Hewan:
    def __init__(self,jenis,jumlahkaki,jumlahmata):
        self.jenis = jenis
        self.jumlahkaki = jumlahkaki
        self.jumlahmata = jumlahmata

Ins1 = Hewan("Kucing", "Empat", "Dua")

inputan = int(input("Nomor Ke Berapa: "))

if inputan == 1:
    print(Ins1.jenis)
elif inputan == 2:
    print(Ins1.jumlahkaki)
elif inputan == 3:
    print(Ins1.jumlahmata)
else:
    print("Error")