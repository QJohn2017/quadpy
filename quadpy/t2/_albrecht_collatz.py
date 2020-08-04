from sympy import Rational as frac

from ..helpers import article
from ._helpers import T2Scheme, expand_symmetries

source = article(
    authors=["J. Albrecht", "L. Collatz"],
    title="Zur numerischen Auswertung mehrdimensionaler Integrale",
    journal="ZAMM",
    volume="38",
    number="1-2",
    year="1958",
    pages="1–15",
    url="https://doi.org/10.1002/zamm.19580380102",
)


def albrecht_collatz():
    d = {
        "s2": [[frac(2, 30), frac(9, 15)], [frac(1, 2), frac(1, 6)]]
    }
    points, weights = expand_symmetries(d)
    weights /= 2
    return T2Scheme("Albrecht-Collatz", weights, points, 3, source, 2.776e-16)
