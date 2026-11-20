# 3. fázis – Az első gépi tanulási modell

Ebben a fázisban az adatbetöltés mellé bekerült az első osztályozó. A logisztikus regressziót választottuk első próbának, mert így külön ellenőrizhető a szövegfeldolgozás és a gépi tanulási modell kapcsolata.

## Most felkerült és módosult fájlok

- `src/config.py` – bekerült a tanításnál használt rögzített véletlenmag.
- `requirements.txt` – a `scikit-learn` is bekerült, mert ezt használjuk a TF-IDF-hez és a modellhez.
- `src/elso_modell.py` – létrehozza a TF-IDF-feldolgozást és a logisztikus regressziót egy közös feldolgozási folyamatban.
- `tests/test_elso_modell.py` – példaüzeneteken ellenőrzi, hogy a modell betanítható és tud új üzenetet besorolni.

A TF-IDF egy- és kétszavas kifejezéseket is figyelembe vesz. A szótár a tanítás során jön létre, így az új üzenetek feldolgozása ugyanazt a módszert használja.

## Ellenőrzés

```powershell
python -m unittest discover -s tests -v
```

A következő fázisban egy második modellt is kipróbálunk, és elkészítjük a tanítóprogramot meg a webes felületet.
