list = ['Kevin', 'Elva', 'Angwyn', 'Sukma', 'Rafi', 'Marvi', 'Shama', 'Gusti', 'Salsa', 'Nonik']
print (list)

#Menampilkan indeks nomor 4,6,7
print ('list indeks nomor 4,6,7 adalah: ', list[4],',', list[6],',', list[7])

#Mengganti nama pada indeks 3,5,9
list[3] = 'Tata'
list[5] = 'Ojat'
list[9] = 'Abel'
print ('nama list indeks nomor 3,5,9 telah diganti menjadi: ', list[3],',', list[5],',', list[9])

#Menambahkan 2 nama teman
list.append('Jun')
list.append('Fahmi')
print(list)

#Menampilkan semua nama teman dengan perulangan
for nama in list:
    print(nama)

#Menampilkan panjang list
print('Panjang listnya adalah: ',len(list))