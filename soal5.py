nama = input("Nama: ")
nilai = int(input("Nilai: "))

if nilai < 0 or nilai > 100:
    print("Nilai salah")
else:
    if nilai > 60:
        print("Lulus")
    elif nilai > 40 and nama == "Budi":
        print("Remidial")
    else:
        print("Tidak lulus")