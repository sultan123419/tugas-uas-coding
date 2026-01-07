
def get_input(prompt):
    try:
        return input(prompt).strip()
    except EOFError:
        return ""


def main():
    print("Masukkan biodata Anda:")
    nama = get_input("Nama: ")
    while not nama:
        nama = get_input("Nama (tidak boleh kosong): ")

    usia = get_input("Usia: ")
    while True:
        if usia.isdigit():
            usia_int = int(usia)
            break
        usia = get_input("Usia (masukkan angka): ")

    alamat = get_input("Alamat: ")
    hobi = get_input("Hobi: ")

    print("\n" + "=" * 40)
    print("Biodata")
    print("=" * 40)
    print(f"Nama   : {nama}")
