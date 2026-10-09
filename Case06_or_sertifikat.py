
hadir_praktik = True
selesai_tugas = False

dapat_sertifikat = hadir_praktik or selesai_tugas

if dapat_sertifikat:
    print("Memenuhi syarat sertifikat")
else:
    print("Tidak memenuhi syarat sertifikat")