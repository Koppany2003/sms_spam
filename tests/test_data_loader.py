"""Hálózati kapcsolat nélkül futtatható tesztek az adatállomány betöltéséhez."""

import tempfile
import unittest
from pathlib import Path

from src.data_loader import adatallomany_betoltese


class AdatbetoltesTeszt(unittest.TestCase):
    def test_betolti_a_spam_es_nem_spam_cimkeket(self):
        with tempfile.TemporaryDirectory() as ideiglenes_mappa:
            adatfajl = Path(ideiglenes_mappa) / "minta.tsv"
            adatfajl.write_text(
                "ham\tHello there\nspam\tYou won a prize\n",
                encoding="utf-8",
            )
            adatkeret = adatallomany_betoltese(
                adatfajl, letoltes_hianyzaskor=False
            )

        self.assertEqual(list(adatkeret.columns), ["label", "message"])
        self.assertEqual(len(adatkeret), 2)
        self.assertEqual(adatkeret.loc[0, "label"], "ham")
        self.assertEqual(adatkeret.loc[1, "label"], "spam")

    def test_kihagyja_az_ervenytelen_sorokat(self):
        with tempfile.TemporaryDirectory() as ideiglenes_mappa:
            adatfajl = Path(ideiglenes_mappa) / "minta.tsv"
            adatfajl.write_text(
                "ham\tNormal message\nunknown\tInvalid label\nnot a row\n",
                encoding="utf-8",
            )
            adatkeret = adatallomany_betoltese(
                adatfajl, letoltes_hianyzaskor=False
            )

        self.assertEqual(len(adatkeret), 1)
        self.assertEqual(adatkeret.iloc[0]["message"], "Normal message")


if __name__ == "__main__":
    unittest.main()
