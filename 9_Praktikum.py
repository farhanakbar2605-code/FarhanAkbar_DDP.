#nomor4
def bilangan(angka):
    for i in range (1,angka):
        if i % 2 != 0:
            print(i, end=", ")
bilangan(20)



#nomor 3
print()
def nilai(n = 0):
    if n <=60:
        print(f"nilai {n} tidak lulus")
    elif n > 60 and n <= 100:
        print(f"nilai {n} lulus")
    else:
        print("tidak diketahui")

nilai(80)
nilai(70)


#nomor 2
def is_genap(n):
    return n % 2== 0

print(is_genap(2))



#nomor 1 
def celcius_ke_fahreinheit(celcius):
    fahreinheit = (celcius*9/5)+32
    return fahreinheit

print(celcius_ke_fahreinheit(0))
print(celcius_ke_fahreinheit(100))

