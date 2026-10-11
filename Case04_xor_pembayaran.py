#Pengujian 1
tunai = True
qris = True

valid = tunai ^ qris

if valid:
    print("Pembayaran valid")
else:
    print("Pembayaran tidak valid")

#Pengujian 2
tunai = False
qris = False

valid = tunai ^ qris

if valid:
    print("Pembayaran valid")
else:
    print("Pembayaran tidak valid")

