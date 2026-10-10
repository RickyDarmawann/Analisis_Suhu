
def baca_data(nama_file):
    data = []

    try:
        with open(nama_file, "r") as file:
            for baris in file:
                hari, suhu = baris.strip().split(";")
                data.append({
                    "hari": hari,
                    "suhu": int(suhu)
                })

        return data

    except FileNotFoundError:
        print("File", nama_file, "tidak ditemukan.")
        return []


def analisis_suhu(data):
    if not data:
        raise ValueError("Data suhu tidak boleh kosong.")

    daftar_suhu = [item["suhu"] for item in data]

    rata_rata = sum(daftar_suhu) / len(daftar_suhu)
    tertinggi = max(data, key=lambda item: item["suhu"])
    terendah = min(data, key=lambda item: item["suhu"])

    for item in data:
        if item["suhu"] >= 32:
            item["kategori"] = "Panas"
        else:
            item["kategori"] = "Normal"

    jumlah_panas = sum(
        1 for item in data if item["suhu"] >= 32
    )

    return {
        "rata_rata": rata_rata,
        "tertinggi": tertinggi,
        "terendah": terendah,
        "jumlah_panas": jumlah_panas,
        "data_harian": data
    }


def tulis_laporan(hasil, nama_file="laporan_suhu.txt"):
    with open(nama_file, "w") as file:
        file.write("LAPORAN ANALISIS SUHU MINGGUAN\n")
        file.write("=============================\n")
        file.write(f"Rata-rata suhu: {hasil['rata_rata']:.2f} C\n")
        file.write(
            f"Suhu tertinggi: {hasil['tertinggi']['suhu']} C "
            f"({hasil['tertinggi']['hari']})\n"
        )
        file.write(
            f"Suhu terendah: {hasil['terendah']['suhu']} C "
            f"({hasil['terendah']['hari']})\n"
        )
        file.write(f"Jumlah hari panas: {hasil['jumlah_panas']}\n\n")
        file.write("Rincian suhu harian:\n")

        for item in hasil["data_harian"]:
            file.write(
                f"{item['hari']}: {item['suhu']} C - "
                f"{item['kategori']}\n"
            )

    with open(nama_file, "r") as file:
        print(file.read())


if __name__ == "__main__":
    data_suhu = baca_data("suhu.txt")

    if data_suhu:
        hasil = analisis_suhu(data_suhu)
        tulis_laporan(hasil)
