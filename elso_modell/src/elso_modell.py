"""Az első SMS-osztályozó modell és a hozzá tartozó szövegfeldolgozás."""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

from src.config import VELETLEN_MAG


def szoveg_pipeline(osztalyozo) -> Pipeline:
    """A szövegeket TF-IDF jellemzőkké alakítja, majd osztályozza őket."""
    return Pipeline(
        steps=[
            (
                "tfidf",
                TfidfVectorizer(
                    ngram_range=(1, 2),
                    min_df=2,
                    strip_accents="unicode",
                    sublinear_tf=True,
                ),
            ),
            ("osztalyozo", osztalyozo),
        ]
    )


def logisztikus_modell_letrehozasa() -> Pipeline:
    """Létrehozza az elsőként kipróbált logisztikus regressziós modellt."""
    modell = LogisticRegression(max_iter=1000, random_state=VELETLEN_MAG)
    return szoveg_pipeline(modell)
