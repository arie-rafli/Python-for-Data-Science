
#String
nama_depan = 'Arie'
nama_belakang = 'Rafli'
nama = nama_depan + " " + nama_belakang
umur = 21
hobi = 'Lari'
print('Biodata:\n', nama, "\n", umur, "\n", hobi)

#Integer
panjang = 10
lebar = 20
luas = panjang + lebar
print(luas)

#Booleran
nama = 'shift'
usia = 22
suda_menikah = False
print('nama: ', nama)
print('usia: ', usia)
print('sudah menikah: ', suda_menikah)


a, b, c = 100, "ASHIAP", 20
print('a: ',a)
print('b: ',b)
print('c: ',c)

#Integer
panjang = 10
lebar = 20
luas = panjang*lebar
print(panjang, '*', lebar, "=", luas)
print("Tipe data luas:", type(luas))

#Complex
a1 = 20 + 14j
b1 = 5 + 53j
ab = a1+b1
print(ab)
print('Type data ab:', type(ab))

#List
List = ['Arie', 'Rafli', 'Katami']
print(List[1])
print(List[-1])
List[2] = "Kasep"
print(List)

List2 = [['Arie'], ['Rafli']]
print(List2)

#Tuple
ini_variable = ('Arie', 'Rafli', 'Katami')
print(ini_variable)
contoh = tuple('Arie')
print(contoh)

tuple1 = (0,1,2,3,4)
tuple2 = ("Saya", "Bahagia")
tuple3 = (tuple1, tuple2)
print(tuple3)

#Slicing
#L[start:stop:step]
L = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(L[:10:-2])
L[1:9] = ['a', 'b', 'c', 'd']
print(L)

x = [5, 6, 1, 4, 7, 3, 4, 4, 0, 9]
x.sort()
print(x)

x.append(10)
print(x)

x.insert(2, [10,5])
print(x)

del(x[3:4])
print(x)

x.pop(1)
print(x)

x.remove([10,5])
print('ini adalah x terakhir:',x)
