class Member_Vokal_Grup:
    '''Dasar kelas untuk semua member vokal grup'''
    jumlah_member_vokal_grup = 0
 
    def __init__(self, nama, umur, asal):
        self.nama = nama
        self.umur = umur
        self.asal = asal
        Member_Vokal_Grup.jumlah_member_vokal_grup += 1
 
    def tampilkan_jumlah(self):
        print("Total member vokal grup:", Member_Vokal_Grup.jumlah_member_vokal_grup)
 
    def tampilkan_profil(self):
        print("Nama :", self.nama)
        print("Umur :", self.umur)
        print("Asal :", self.asal)
 
# Membuat objek pertama dari kelas Member Vokal Grup
member_vokal_grup1 = Member_Vokal_Grup("Mark", 21, "Toronto")
# Membuat objek kedua dari kelas Member Vokal Grup
member_vokal_grup2 = Member_Vokal_Grup("Felix", 20, "Sydney")
# Membuat objek ketiga dari kelas Member Vokal Grup
member_vokal_grup3 = Member_Vokal_Grup("Ten", 25, "Bangkok")
# Membuat objek keempat dari kelas Member Vokal Grup
member_vokal_grup4 = Member_Vokal_Grup("Ruby", 17, "Yogyakarta")
# Membuat objek kelima dari kelas Member Vokal Grup
member_vokal_grup5 = Member_Vokal_Grup("Misellia", 16, "Surabaya")
 
member_vokal_grup1.tampilkan_profil()
member_vokal_grup2.tampilkan_profil()
member_vokal_grup3.tampilkan_profil()
member_vokal_grup4.tampilkan_profil()
member_vokal_grup5.tampilkan_profil()

print("Total member vokal grup :", Member_Vokal_Grup.jumlah_member_vokal_grup)
