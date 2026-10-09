
sensor_gerak = False
tombol_ditekan = True

lampu_menyala = sensor_gerak or tombol_ditekan

if lampu_menyala:
    print("Lampu menyala")
else:
    print("Lampu mati")