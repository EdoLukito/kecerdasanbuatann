#awal = A
#tujuan = G
#jalur

peta1 =  {'A':set(['B','C','D','E']),
         'B':set(['A','E','I']),
         'C':set(['A','F']),
         'D':set(['A','G']),
         'E':set(['A','B','F','J','H']),
         'F':set(['C','E','G','H']),
         'G':set(['D','K','F','H']),
         'H':set(['E','F','G','K']),
         'I':set(['B','J','L']),
         'J':set(['E','L','I']),
         'K':set(['J','H','G']),
         'L':set(['I','J'])}

def bfs(graf, mulai, tujuan):
    queue = [[mulai]]
    visited = set()

    while queue:     
        # masukkan antrian paling depan ke variabel jalur
        jalur = queue.pop(0)

        # simpan node yang dipilih ke variabel state, misal jalur = C,B maka simpan B ke variabel state
        state = jalur[-1]

        # cek state apakah sama dengan tujuan, jika ya maka return jalur
        if state == tujuan:
            return jalur
        # jika state tidak sama dengan tujuan, maka cek apakah state tidak ada di visited
        elif state not in visited:
            # jika state tidak ada di visited maka cek cabang
            for cabang in graf.get(state, []): #cek semua cabang dari state
                jalur_baru = list(jalur) #masukkan isi dari variabel jalur ke variabel jalur_baru
                jalur_baru.append(cabang) #update/tambah isi jalur_baru dengan cabang
                queue.append(jalur_baru) #update/tambah queue dengan jalur_baru
                print(jalur_baru)

            # tandai state yang sudah dikunjungi sebagai visited
            visited.add(state)

        #cek isi antrian
        isi = len(queue)
        if isi == 0:
            print("Tidak ditemukan")


print(bfs(peta1,'A','K'))
