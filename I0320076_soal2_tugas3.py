dict = {'Nama':'Nurki Putra Mahardika', 'Hobi': ['Menggambar', 'Menulis', 'Kuliner'], 'Sosial_Media' : ['IDLine : blenditblendit',
        'Instagram : @nurkiputra', 'Facebook : Nurki Mahardika'], 'Lagu_Favorit': ['Snow in California', 'Sampai Menutup Mata',
         'Perahu Kertas'], 'Makanan_Favorit': ['Indomie Goreng', 'Rendang', 'Gethuk']}

print ("Nama: ", dict['Nama'])
print ("Hobi: ", dict['Hobi'])
print ("Sosial Media: ", dict['Sosial_Media'])
print ("Lagu Favorit: ", dict['Lagu_Favorit'])
print ("Makanan Favorit: ", dict['Makanan_Favorit'])

#Mengubah salah satu hobi dan sosial media
dict['Hobi'][0] = 'Mabar'
print ("Hobi: ", dict['Hobi'])
dict['Sosial_Media'][2] = 'Nurki Putra'
print ('Sosial Media: ', dict['Sosial_Media'])

#Menghapus 2 makanan favorit
del dict['Makanan_Favorit'][:2]
print ("Makanan Favorit: ", dict['Makanan_Favorit'])

#Menambah 1 hobi
dict['Hobi'].append('Berenang')
print ('Hobi: ', dict['Hobi'])