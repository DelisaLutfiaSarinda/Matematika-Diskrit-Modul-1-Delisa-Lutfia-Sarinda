
kartu_aktif = True
tidak_terlambat = True

boleh_meminjam = kartu_aktif and tidak_terlambat

if boleh_meminjam:
    print("Boleh meminjam buku")
else:
    print("Tidak boleh meminjam buku")