"""Alapellenőrzés az első, logisztikus regressziós modellhez."""

import unittest

from src.elso_modell import logisztikus_modell_letrehozasa


class ElsoModellTeszt(unittest.TestCase):
    def test_a_modell_megtanul_es_uzenetet_osztalyoz(self):
        uzenetek = [
            "hello how are you", "see you tomorrow", "call me after class",
            "thanks for your help", "the train arrives soon", "have a nice day",
            "win a free prize now", "claim your cash reward", "free entry today",
            "you have won a gift", "urgent claim your prize", "call now to win",
        ] * 2
        cimkek = (["ham"] * 6 + ["spam"] * 6) * 2

        modell = logisztikus_modell_letrehozasa()
        modell.fit(uzenetek, cimkek)
        eredmeny = modell.predict(["claim your free prize now"])

        self.assertEqual(len(eredmeny), 1)
        self.assertIn(eredmeny[0], ["ham", "spam"])


if __name__ == "__main__":
    unittest.main()
