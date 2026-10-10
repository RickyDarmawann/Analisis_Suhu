
import unittest
from main import analisis_suhu


class TestAnalisisSuhu(unittest.TestCase):

    def setUp(self):
        self.data = [
            {"hari": "Senin", "suhu": 31},
            {"hari": "Selasa", "suhu": 33},
            {"hari": "Rabu", "suhu": 29},
            {"hari": "Kamis", "suhu": 35},
            {"hari": "Jumat", "suhu": 32},
            {"hari": "Sabtu", "suhu": 30},
            {"hari": "Minggu", "suhu": 28}
        ]

    def test_rata_rata(self):
        hasil = analisis_suhu(self.data)
        self.assertAlmostEqual(
            hasil["rata_rata"], 31.142857, places=5
        )

    def test_suhu_tertinggi(self):
        hasil = analisis_suhu(self.data)
        self.assertEqual(hasil["tertinggi"]["suhu"], 35)
        self.assertEqual(hasil["tertinggi"]["hari"], "Kamis")

    def test_suhu_terendah(self):
        hasil = analisis_suhu(self.data)
        self.assertEqual(hasil["terendah"]["suhu"], 28)
        self.assertEqual(hasil["terendah"]["hari"], "Minggu")


if __name__ == "__main__":
    unittest.main()
