print("Stack dalam Python (LIFO)")

stack = []

while True:
    try:
        pilihan = int(input('''
Menu:
1. Push data
2. Pop data
3. Exit
Pilih opsi (1/2/3): '''))
    except ValueError:
        print("Masukkan angka yang valid (1, 2, atau 3)!")
        continue

    if pilihan == 1:
        data_baru = input("Masukkan data: ")
        stack.append(data_baru)
        print("Isi stack:", stack)

    elif pilihan == 2:
        if len(stack) == 0:
            print("Stack kosong, tidak ada data untuk di-pop.")
        else:
            terhapus = stack.pop()
            print("Data dihapus:", terhapus)
            print("Isi stack:", stack)

    elif pilihan == 3:
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid. Masukkan 1, 2, atau 3.")
