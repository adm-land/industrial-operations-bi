import csv
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"


class TestIndustrialData(unittest.TestCase):
    def test_production_has_valid_units(self):
        with open(RAW / "produccion.csv", encoding="utf-8-sig", newline="") as f:
            rows = list(csv.DictReader(f))
        self.assertGreater(len(rows), 100)
        for row in rows[:100]:
            total = int(row["unidades_totales"])
            good = int(row["unidades_buenas"])
            scrap = int(row["scrap_unidades"])
            self.assertEqual(total, good + scrap)
            self.assertGreaterEqual(total, 0)

    def test_logistics_dates_and_quantities(self):
        with open(RAW / "logistica.csv", encoding="utf-8-sig", newline="") as f:
            rows = list(csv.DictReader(f))
        self.assertGreater(len(rows), 50)
        for row in rows[:100]:
            self.assertGreater(int(row["cantidad_ordenada"]), 0)
            self.assertGreaterEqual(int(row["cantidad_recibida"]), 0)


if __name__ == "__main__":
    unittest.main()
