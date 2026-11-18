2. fázis – Az SMS-adatok betöltése
Ebben a lépésben elkészült az adatállomány letöltése és beolvasása. A program a UCI SMS Spam Collection adatait használja.
Most felkerült és módosult fájlok
`src/config.py` – bekerült az adatfájl helye és a letöltési cím.
`requirements.txt` – hozzáadtuk a `pandas` könyvtárat, amellyel táblázatos formában kezeljük az SMS-eket.
`src/data_loader.py` – letölti a ZIP-fájlt, kicsomagolja az SMS-listát, majd beolvassa az üzeneteket és a címkéket.
`tests/test_data_loader.py` – ellenőrzi a beolvasást és azt, hogy a hibás sorok kimaradnak.
A beolvasott adatok két oszlopba kerülnek: `label` és `message`. A `ham` normál üzenetet, a `spam` kéretlen üzenetet jelent. Az eredeti adatfájl a `data/` mappában marad.
Ellenőrzés
A projekt fő mappájából futtatható:
```powershell
python -m unittest discover -s tests -v
```
Ebben a fázisban még nem tanítunk modellt. A következő lépésben TF-IDF-fel számszerűsítjük az üzeneteket, és elkészítjük az első osztályozót.
