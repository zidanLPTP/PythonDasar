print("Queue dalam Python (FIFO)")

queue = []

while True:
    try:
        pilihan = int(input('''
Menu:
1. Push data
2. Pop first data
3. Exit
Pilih opsi (1/2/3): '''))
    except ValueError:
        print("Masukkan angka yang valid (1, 2, atau 3)!")
        continue

    if pilihan == 1:
        data_baru = input("Masukkan data: ")
        queue.append(data_baru)
        print("Isi queue:", queue)

    elif pilihan == 2:
        if len(queue) == 0:
            print("Queue kosong, tidak ada data untuk di-pop.")
        else:
            terhapus = queue.pop(0)  # ambil dan hapus elemen pertama
            print("Data dihapus:", terhapus)
            print("Isi queue:", queue)

    elif pilihan == 3:
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid. Masukkan 1, 2, atau 3.")
