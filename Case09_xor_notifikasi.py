
notifikasi_suara = False
notifikasi_getar = True

pengaturan_valid = notifikasi_suara ^ notifikasi_getar

if pengaturan_valid:
    print("Pengaturan notifikasi valid")
else:
    print("Pengaturan notifikasi tidak valid")