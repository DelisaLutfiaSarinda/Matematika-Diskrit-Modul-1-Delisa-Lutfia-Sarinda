#Pengujian 1
member = True
voucher = True

diskon = member or voucher

if diskon:
    print("Mendapat diskon")
else:
    print("Tidak mendapat diskon")

#Pengujian 2
member = False
voucher = False

diskon = member or voucher

if diskon:
    print("Mendapat diskon")
else:
    print("Tidak mendapat diskon")

#Pengujian 3
member = True
voucher = False

diskon = member or voucher

if diskon:
    print("Mendapat diskon")
else:
    print("Tidak mendapat diskon")