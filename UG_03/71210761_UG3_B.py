import math

bil = int(input('Masukan range data :'))
dctnry = dict()

for i in range(bil):
   if i % 2 ==0:
    n = i
    fact = 1
    for x in range(1, n+1):
        fact = fact *x
    dctnry[i] = fact

print(dctnry)
tampilkan = int(input("Data ditampilakan:"))

if tampilkan in dctnry.keys():
    print(dctnry[tampilkan])
else:
    print("Data tidak ditemukan")
    



