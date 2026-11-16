# 1. fázis – A projekt alapjai

Ebben a lépésben létrehoztuk a projekt kezdeti mappaszerkezetét és a közös beállításokat. Egyelőre még nincs adatbetöltés és gépi tanulás, csak előkészítettük a helyét a későbbi részeknek.

## Most felkerült fájlok

- `src/config.py` – a projekt gyökérmappáját és az adatok, modellek, eredmények mappáját állítja be.
- `src/__init__.py` – a `src` mappát Python-csomagként használhatóvá teszi.
- `.gitignore` – kizárja a virtuális környezetet, a gyorsítótárakat és a helyben előállított fájlokat.
- `data/`, `models/`, `reports/` – ezekbe kerülnek majd az adatok, a betanított modellek és a mérési eredmények.

Ebben a fázisban csak a Python beépített eszközeit használjuk, külső csomagot még nem kellett telepíteni.
