#contoh peta 
peta =  {'A':set(['B','C','D','E']),
         'B':set(['A','E','I']),
         'C':set(['A','F']),
         'D':set(['A','G']),
         'E':set(['A','B','F','H','J']),
         'F':set(['C','E','G','H']),
         'G':set(['D','F','H','K']),
         'H':set(['E','F','G','K']),
         'I':set(['B','J','L']),
         'J':set(['E','I','L']),
         'K':set(['G','H','J']),
         'L':set(['I','J'])}
   

def dfs(graf, mulai, tujuan):
    stack = [[mulai]]
    visited = set()

    while stack:
        #hitung panjang tumpukan dan masukkan ke variabel panjang_tumpukan
        panjang_tumpukan = len(stack)-1
        
        # masukkan tumpukan palinif state == tujuan:g atas ke variabel jalur
        jalur = stack.pop(panjang_tumpukan)

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
                    stack.append(jalur_baru) #update/tambah queue dengan jalur_baru
                    print(jalur_baru)

            # tandai state yang sudah dikunjungi sebagai visited
                visited.add(state)


        #cek isi tumpukan
        isi = len(stack)
        if isi == 0:
            print("Tidak ditemukan")

print(dfs(peta,'A','K'))

