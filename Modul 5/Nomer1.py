class MhsTIF(object):
    def __init__(self, nama, umur, kota, us,NIM):
        self.nama = nama
        self.umur = umur
        self.kotaTinggal = kota
        self.uangSaku = us
        self.NIM = NIM

    def __str__(self):
        x = self.NIM
        return x
    def getNIM(self):
        return self.NIM

c0 = MhsTIF('Ika', 10, 'Sukoharjo', 240000,'L200170001')
c1 = MhsTIF('Budi', 14, 'Klaten', 250000,'L200170002')
c2 = MhsTIF('Ahmad', 12, 'Surakarta', 295000,'L200170003')
c3 = MhsTIF('Chandra', 21, 'Wonogiri', 235000,'L200170004')
c4 = MhsTIF('Fia', 20, 'Solo', 350000,'L200170005')
c5 = MhsTIF('Fandi', 65, 'Purworejo', 140000,'L200170006')
c6 = MhsTIF('Hasan', 11, 'Bandung', 440000,'L200170007')
c7 = MhsTIF('Galuh', 43, 'Surabaya', 2750000,'L200170008')
c8 = MhsTIF('Deni', 56, 'Purwodadi', 220000,'L200170009')
c9 = MhsTIF('Danish', 6, 'Salatiga', 165000,'L200170010')
c10 = MhsTIF('Risa', 20, 'Purwodadi', 140000,'L200170011')

Daftar = [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]

def insertionSort(A):
    n = len(A)
    for i in range(1, n):
        nilai = A[i]
        pos = i
        while pos > 0 and nilai.NIM < A[pos - 1].NIM:
            A[pos] = A[pos - 1]
            pos = pos - 1
        A[pos] = nilai
        
def Daftarnya(d):
    for i in d:
        print(i)
        
insertionSort(Daftar)
Daftarnya(Daftar)
    
