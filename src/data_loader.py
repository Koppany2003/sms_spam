"""A nyilvános UCI SMS Spam Collection adatállomány letöltése és beolvasása."""

from __future__ import annotations

import csv
import io
import urllib.request
import zipfile
from pathlib import Path

import pandas as pd

from src.config import ADATFAJL, ADATFORRAS_URL


def adatallomany_letoltese(cel: Path = ADATFAJL) -> Path:
    """Letölti az UCI ZIP-állományt, majd kicsomagolja az SMS-adatokat.

    A letöltött fájl helyben, a ``data/`` mappában marad, így a későbbi
    futtatásokhoz már nem szükséges újra internetkapcsolat.
    """
    cel.parent.mkdir(parents=True, exist_ok=True)
    keres = urllib.request.Request(
        ADATFORRAS_URL,
        headers={"User-Agent": "Mozilla/5.0 (compatible; StudentSpamProject/1.0)"},
    )

    try:
        with urllib.request.urlopen(keres, timeout=30) as valasz:
            zip_adatok = valasz.read()
    except Exception as hiba:  # pragma: no cover - a hálózati elérhetőségtől függ
        raise RuntimeError(
            "Nem sikerült letölteni az adatállományt. Ellenőrizd az internetkapcsolatot, "
            "vagy töltsd le kézzel az UCI oldaláról, és másold ide: "
            f"{cel}"
        ) from hiba

    try:
        with zipfile.ZipFile(io.BytesIO(zip_adatok)) as zip_allomany:
            tag = next(
                (
                    nev
                    for nev in zip_allomany.namelist()
                    if nev.endswith("SMSSpamCollection")
                ),
                None,
            )
            if tag is None:
                raise RuntimeError(
                    "A letöltött ZIP-állományban nem található a SMSSpamCollection fájl."
                )
            cel.write_bytes(zip_allomany.read(tag))
    except zipfile.BadZipFile as hiba:
        raise RuntimeError("A letöltött adatállomány nem érvényes ZIP-fájl.") from hiba

    return cel


def adatallomany_betoltese(
    utvonal: Path = ADATFAJL, letoltes_hianyzaskor: bool = True
) -> pd.DataFrame:
    """Adatkeretet ad vissza ``label`` és ``message`` oszlopokkal.

    Az oszlopnevek az eredeti adatforrás formátumával való kompatibilitás
    érdekében változatlanok maradnak.
    """
    if not utvonal.exists():
        if not letoltes_hianyzaskor:
            raise FileNotFoundError(f"Nem található az adatállomány: {utvonal}")
        adatallomany_letoltese(utvonal)

    sorok: list[tuple[str, str]] = []
    with utvonal.open("r", encoding="utf-8", errors="replace", newline="") as fajl:
        olvaso = csv.reader(fajl, delimiter="\t")
        for sor in olvaso:
            if len(sor) < 2:
                continue
            cimke = sor[0].strip().lower()
            uzenet = "\t".join(sor[1:]).strip()
            if cimke in {"ham", "spam"} and uzenet:
                sorok.append((cimke, uzenet))

    adatkeret = pd.DataFrame(sorok, columns=["label", "message"])
    if adatkeret.empty:
        raise ValueError("Az adatállomány üres vagy nem a várt formátumú.")

    adatkeret = adatkeret.drop_duplicates(
        subset=["label", "message"]
    ).reset_index(drop=True)
    return adatkeret


def load_dataset(path: Path = ADATFAJL, download_if_missing: bool = True) -> pd.DataFrame:
    return adatallomany_betoltese(
        path, letoltes_hianyzaskor=download_if_missing
    )


def download_dataset(destination: Path = ADATFAJL) -> Path:
    return adatallomany_letoltese(destination)
