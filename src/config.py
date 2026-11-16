"""A projekt alapmappáinak közös beállításai."""

from pathlib import Path

PROJEKT_GYOKER = Path(__file__).resolve().parents[1]
ADAT_MAPPA = PROJEKT_GYOKER / "data"
MODELL_MAPPA = PROJEKT_GYOKER / "models"
EREDMENY_MAPPA = PROJEKT_GYOKER / "reports"
