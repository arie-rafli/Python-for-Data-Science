# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 12:02:06 2021

@author: LENOVO
"""
#Slicing, Mengakses
warna = ('merah', 'jingga', 'kuning', 'hijau', 'biru', 'nila', 'ungu')
print(warna[2:4])
print(warna[1])

#Nested Tuple
tupel = 'aku', 'cinta', 'kamu'
tupel2 = 'selama', 1000, 'tahun'
tupel3 = (tupel+tupel2) #Nested Tuple
print(tupel3)

#Dasar Slicing
warna = ('merah', 'kuning', 'hijau', 'biru', 'nila', 'ungu')
print(warna[:4])
print(warna[:-2])
print(warna[::2])
print(warna[1::2])
print(warna[1:-3:2])
print(warna[-1:0:-1])
print(warna[-2:3:-1])

#Slice
nums = [1,2,3,4,5,6,7,8,9]
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
fungsi_slice = slice(2, 3+3)
print(nums[fungsi_slice])

#manipulate list
A = [1, 2, 3, 4]
A[1] = 'Cat'
print(A)
print(A.index('Cat'))

#Count Method
ex_list = [10, 20, 10, 50, 20, 10, 25, 12, 30, 40, 10, 50, 90, 86, 66]
print(ex_list.count(10))

#sort and reverse
ex_list2 = [1,4,5,2,3]
ex_list.sort()
print(ex_list)
ex_list.sort(reverse = True)
print(ex_list)

#Pop
Z = [9,7,5,3,1]
print(Z.pop(1))
print(Z)

#Append
Z.append(5)
print(Z)

#Insert
Z.insert(0, [1,2])
print(Z)

#Replace
Y = [1,2,3,4,5,6,7,8,9]
Y[:3] = [10,20,30, 40, 50]
print(Y)

#Ganti setiap element ke-N dengan step
Nums = [1,2,3,4,5,6,7,8,9]
Nums[::2] = [1,1,1,1,1]
print(Nums)
Nums2 = [1,2,3,4,5,6,7,8,9]
Nums2[::-2] = [1,2,3,4,5]
print(Nums2)

Nums3 = [1,2,3,4,5,6,7,8,9]
Nums3[1:5:2] = [1,2]
print(Nums3)

#Extend
Ext = [0, 0, 7]
Ext.extend([4,5])
print(Ext)
#Atau
print([0,0,7] + [4,5])

#Delete
keranjang = ['roti', 'mentega', 'susu']
del keranjang[0]
print(keranjang)

nums = [ 10 , 20 , 30 , 40 , 50 , 60 , 70 , 80 , 90 ]
del nums[3:7]
print(nums)
