import bangunruang as br
import bangundatar as bd

print(">>>>>>BANGUN RUANG<<<<<<")
print(f"volum kubus dengan sisi 3 adalah {br.kubus(3)}")
print(f"volum balok adalah {br.balok(4, 5, 2,)}")
print(f"volum prisma segitiga adalah {br.prisma(5,4,5)}")
print(f"volum tabung adalah r=5 t=10 {br.tabung(4,7)}")
print(f"volum kerucut adalah r=3 t=13 {br.kerucut(6,10)}")


print(">>>>>>>>>BANGUN DATAR<<<<<<<<<")
print(f"Luas Persegi adalah {bd.persegi(5)}")
print(f"Luas Persegi Panjang adalah {bd.persegi_panjang(3,8)}")
print(f"Luas Segitiga adalah {bd.segitiga(10,11)}")
print(f"Luas Lingkaran adalah ")
print(f"Luas jajargenjang adalah a=5 t=8 {bd.jajargenjang(4,8)}")