from tabulate import tabulate

data = [
    {"Kode": 1,"Nama Siswa":"Kezia Warau","Nilai Pekan 1":80,"Nilai Pekan 2": 90, "Nilai Pekan 3": 76, "Nilai Pekan 4": 70, "Nilai Tertinggi": 90, "Nilai Terendah": 70, "Nilai Rata rata": 79, "Keterangan": "Lulus"},
    {"Kode": 2,"Nama Siswa":"Andhika Pratama","Nilai Pekan 1":60,"Nilai Pekan 2": 65, "Nilai Pekan 3": 68, "Nilai Pekan 4": 80, "Nilai Tertinggi": 80, "Nilai Terendah": 60, "Nilai Rata rata": 68.25, "Keterangan": "Tidak Lulus"},
    {"Kode": 3,"Nama Siswa":"Lyodra Ginting","Nilai Pekan 1":90,"Nilai Pekan 2": 80, "Nilai Pekan 3": 60, "Nilai Pekan 4": 55, "Nilai Tertinggi": 90, "Nilai Terendah": 55, "Nilai Rata rata": 71.2, "Keterangan": "Tidak Lulus"},
    {"Kode": 4,"Nama Siswa":"Boaz Salossa","Nilai Pekan 1":77,"Nilai Pekan 2": 68, "Nilai Pekan 3": 87, "Nilai Pekan 4": 65, "Nilai Tertinggi": 87, "Nilai Terendah": 65, "Nilai Rata rata": 74.25, "Keterangan": "Tidak Lulus"},
    {"Kode": 5,"Nama Siswa":"Shin Tae yong","Nilai Pekan 1":88,"Nilai Pekan 2": 77, "Nilai Pekan 3": 80, "Nilai Pekan 4": 75, "Nilai Tertinggi": 88, "Nilai Terendah": 75, "Nilai Rata rata": 80, "Keterangan": "Lulus"},
    {"Kode": 6,"Nama Siswa":"Gading Marten","Nilai Pekan 1":77,"Nilai Pekan 2": 80, "Nilai Pekan 3": 76, "Nilai Pekan 4": 90, "Nilai Tertinggi": 90, "Nilai Terendah": 76, "Nilai Rata rata": 80.75, "Keterangan": "Lulus"},
    {"Kode": 7,"Nama Siswa":"Raditya Dika","Nilai Pekan 1":89,"Nilai Pekan 2": 78, "Nilai Pekan 3": 77, "Nilai Pekan 4": 68, "Nilai Tertinggi": 89, "Nilai Terendah": 68, "Nilai Rata rata": 78, "Keterangan": "Lulus"},
    {"Kode": 8,"Nama Siswa":"Bima Satria","Nilai Pekan 1":88,"Nilai Pekan 2": 90, "Nilai Pekan 3": 68, "Nilai Pekan 4": 70, "Nilai Tertinggi": 90, "Nilai Terendah": 68, "Nilai Rata rata": 79, "Keterangan": "Lulus"},
    {"Kode": 9,"Nama Siswa":"Keisha hutama","Nilai Pekan 1":66,"Nilai Pekan 2": 72, "Nilai Pekan 3": 80, "Nilai Pekan 4": 70, "Nilai Tertinggi": 80, "Nilai Terendah": 66, "Nilai Rata rata": 72, "Keterangan": "Tidak Lulus"},
    {"Kode": 10,"Nama Siswa":"Mikha Angelo","Nilai Pekan 1":88,"Nilai Pekan 2": 70, "Nilai Pekan 3": 60, "Nilai Pekan 4": 70, "Nilai Tertinggi": 88, "Nilai Terendah": 60, "Nilai Rata rata": 72.5, "Keterangan": "Tidak Lulus"},
]

def read_data():
    while True:
        table = tabulate(data, headers="keys", tablefmt="pretty")
        print(table)
        read_opsi = input("ingin kembali ke menu utama? (Y/N)")
        if read_opsi == 'Y':
            break
        else:
            print("kembali ke data siswa")

def create_data() :

    keterangan = ""

    last_kode = data[-1]["Kode"]
    kode = last_kode + 1

    nama = input("Masukkan Nama Siswa: ")
    nilai_pekan_1 = int(input("Masukkan Nilai Pekan 1: "))
    nilai_pekan_2 = int(input("Masukkan Nilai Pekan 2: "))
    nilai_pekan_3 = int(input("Masukkan Nilai Pekan 3: "))
    nilai_pekan_4 = int(input("Masukkan Nilai Pekan 4: "))

    nilai_tertinggi = max(nilai_pekan_1, nilai_pekan_2, nilai_pekan_3, nilai_pekan_4)
    nilai_terendah = min(nilai_pekan_1, nilai_pekan_2, nilai_pekan_3, nilai_pekan_4)
    nilai_rata_rata = (nilai_pekan_1 + nilai_pekan_2 + nilai_pekan_3 + nilai_pekan_4) / 4

    if nilai_rata_rata >= 75 :
        keterangan = 'Lulus'
    else: 
        keterangan = 'Tidak Lulus'

    new_data = {
        "Kode": kode,
        "Nama Siswa": nama,
        "Nilai Pekan 1": nilai_pekan_1,
        "Nilai Pekan 2": nilai_pekan_2,
        "Nilai Pekan 3": nilai_pekan_3,
        "Nilai Pekan 4": nilai_pekan_4,
        "Nilai Tertinggi": nilai_tertinggi,
        "Nilai Terendah": nilai_terendah,
        "Nilai Rata rata": nilai_rata_rata,
        "Keterangan": keterangan
    }

    data.append(new_data)
    print(f"Data siswa {nama} dengan kode {kode} berhasil ditambahkan!")

def update_data():
    kode_siswa = int(input("Masukkan Kode Siswa yang akan diperbarui: "))
    
    # Find the index of the student with the specified code
    index_to_update = next((index for index, student in enumerate(data) if student["Kode"] == kode_siswa), None)

    if index_to_update is not None:
        print(f"Data Siswa dengan Kode {kode_siswa} saat ini:")
        print(tabulate([data[index_to_update]], headers="keys", tablefmt="pretty"))

        # Update data
        data[index_to_update]["Nama Siswa"] = input("Masukkan Nama Siswa baru: ")
        data[index_to_update]["Nilai Pekan 1"] = int(input("Masukkan Nilai Pekan 1 baru: "))
        data[index_to_update]["Nilai Pekan 2"] = int(input("Masukkan Nilai Pekan 2 baru: "))
        data[index_to_update]["Nilai Pekan 3"] = int(input("Masukkan Nilai Pekan 3 baru: "))
        data[index_to_update]["Nilai Pekan 4"] = int(input("Masukkan Nilai Pekan 4 baru: "))

        # Recalculate other values
        data[index_to_update]["Nilai Tertinggi"] = max(data[index_to_update]["Nilai Pekan 1"],
                                                        data[index_to_update]["Nilai Pekan 2"],
                                                        data[index_to_update]["Nilai Pekan 3"],
                                                        data[index_to_update]["Nilai Pekan 4"])
        data[index_to_update]["Nilai Terendah"] = min(data[index_to_update]["Nilai Pekan 1"],
                                                       data[index_to_update]["Nilai Pekan 2"],
                                                       data[index_to_update]["Nilai Pekan 3"],
                                                       data[index_to_update]["Nilai Pekan 4"])
        data[index_to_update]["Nilai Rata rata"] = (data[index_to_update]["Nilai Pekan 1"] +
                                                     data[index_to_update]["Nilai Pekan 2"] +
                                                     data[index_to_update]["Nilai Pekan 3"] +
                                                     data[index_to_update]["Nilai Pekan 4"]) / 4

        if data[index_to_update]["Nilai Rata rata"] >= 75:
            data[index_to_update]["Keterangan"] = 'Lulus'
        else:
            data[index_to_update]["Keterangan"] = 'Tidak Lulus'

        print(f"Data Siswa dengan Kode {kode_siswa} berhasil diperbarui!")
    else:
        print(f"Tidak ada data siswa dengan Kode {kode_siswa}.")

def delete_data():
    kode_siswa = int(input("Masukkan Kode Siswa yang akan dihapus: "))

    # Find the index of the student with the specified code
    index_to_delete = next((index for index, student in enumerate(data) if student["Kode"] == kode_siswa), None)

    if index_to_delete is not None:
        print(f"Data Siswa dengan Kode {kode_siswa} yang akan dihapus:")
        print(tabulate([data[index_to_delete]], headers="keys", tablefmt="pretty"))

        confirmation = input("Apakah Anda yakin ingin menghapus data siswa ini? (Y/N): ")
        if confirmation.upper() == 'Y':
            del data[index_to_delete]
            print(f"Data Siswa dengan Kode {kode_siswa} berhasil dihapus!")
        else:
            print("Penghapusan data dibatalkan.")
    else:
        print(f"Tidak ada data siswa dengan Kode {kode_siswa}.")


def landingpage():
    print('''
    ##### RECAP NILAI SISWA #####
    ##### LIST MENU         #####
    1. Tampilkan Daftar Recap Nilai Bulan ini
    2. Tambah Data Siswa
    3. Perbarui Data Siswa
    4. Hapus Data Siswa
    5. Exit ''')


def main() :
    while True: 
        landingpage()
        menu_option = input("masukkan opsi: ")
        if menu_option == '1' :
            read_data()
        elif menu_option == '2' :
            create_data()
        elif menu_option == '3' :
            update_data()
        elif menu_option == '4' : 
            delete_data()
        elif menu_option == '5' :
            break

main()

