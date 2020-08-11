import math
import warnings

from sympy import Rational as frac
from sympy import sqrt

from ..helpers import article
from ._helpers import (
    C2Scheme,
    concat,
    pm,
    pm2,
    symm_r0,
    symm_s,
    symm_s_t,
    zero,
    expand_symmetries,
)
from ._rabinowitz_richter import rabinowitz_richter_1
from ._tyler import tyler_2

source = article(
    authors=["Richard Franke"],
    title="Obtaining cubatures for rectangles and other planar regions by using orthogonal polynomials",
    journal="Math. Comp.",
    volume="25",
    year="1971",
    pages="803-817",
    url="https://doi.org/10.1090/S0025-5718-1971-0300440-5",
)


def franke_1(lmbda):
    assert -frac(9, 5) <= lmbda <= frac(9, 4)

    a = sqrt(frac(9 + 5 * lmbda, 15))
    b = sqrt(frac(9 - 4 * lmbda, 15))
    c = sqrt(frac(3, 5))

    weights, points = concat(
        zero(frac(16 * (4 + 5 * lmbda), 9 * (9 + 5 * lmbda))),
        pm2([frac(25, 9 * (9 - 4 * lmbda)), b, c]),
        pm(
            [frac(40, 9 * (9 + 5 * lmbda)), a, 0],
            [frac(40 * (1 - lmbda), 9 * (9 - 4 * lmbda)), 0, c],
        ),
    )
    weights /= 4
    return C2Scheme(f"Franke(1, {lmbda})", weights, points, 5, source)


def franke_2a():
    a = math.sqrt((15 + 2 * sqrt(30)) / 35)
    b = math.sqrt((15 - 2 * sqrt(30)) / 35)

    # closed forms not appearing in the article:
    c = 5 * (18 + math.sqrt(30)) / 324
    d = 2 * (18 + math.sqrt(30)) / 81

    weights, points = concat(
        pm2(
            [0.437841520872291e-1, 0.105784012371275e1, a],
            [c, math.sqrt(3 / 5), b],
            [0.304070693050225, 0.469253522127911, a],
        ),
        pm([d, 0, b]),
    )
    weights /= 4
    return C2Scheme("Franke 2a", weights, points, 7, source, 1.232e-14)


def franke_2b():
    a = math.sqrt((15 + 2 * sqrt(30)) / 35)
    b = math.sqrt((15 - 2 * sqrt(30)) / 35)

    weights, points = concat(
        pm2(
            [0.193252691743030, 0.774596669241483, a],
            [0.169049921219002, 0.915060523380880, b],
            [0.483095233643544, 0.396191039748320, b],
        ),
        pm([0.309204306788848, 0, a]),
    )
    weights /= 4
    return C2Scheme("Franke 2b", weights, points, 7, source)


def franke_3a():
    a = math.sqrt(5.0 / 9.0 + 2.0 / 63.0 * math.sqrt(70))
    b = math.sqrt(5.0 / 9.0 - 2.0 / 63.0 * math.sqrt(70))

    d = {
        "pm2": [
            [
                0.705065140564012e-1,
                0.721121511007611e-1,
                0.971492736037507e-1,
                0.368549048677049,
            ],
            [
                0.845927799771709,
                0.628901636732253,
                0.959681421214621,
                0.436030596273468,
            ],
            [a, a, b, b],
        ],
        "pmx": [[0.316049382716049], [0.774596669241483]],
        "pmy": [[0.188616439798053, 0.258606964371341e-1], [a, b]],
        "zero": [[0.505679012345679]],
    }
    points, weights = expand_symmetries(d)
    weights /= 4
    return C2Scheme("Franke 3a", weights, points, 9, source)


def franke_3b():
    a = math.sqrt(5.0 / 9.0 + 2.0 / 63.0 * math.sqrt(70))
    b = math.sqrt(5.0 / 9.0 - 2.0 / 63.0 * math.sqrt(70))

    d = {
        "pm2": [
            [
                0.499290623065150e-1,
                0.158445182284802,
                0.183383788151247,
                0.881476523665422e-1,
            ],
            [
                0.945813739519925,
                0.465346624836203,
                0.804253925742002,
                0.681385892163677,
            ],
            [a, a, b, b],
        ],
        "pmx": [
            [0.114456375561331, 0.454432513327558],
            [0.963018409085396, 0.428610143223121],
        ],
        "pmy": [[0.571052809297435e-1, 0.414194459963155], [a, b]],
    }
    points, weights = expand_symmetries(d)
    weights /= 4
    return C2Scheme("Franke 3b", weights, points, 9, source)


def franke_3c():
    a = math.sqrt(5.0 / 9.0 + 2.0 / 63.0 * math.sqrt(70))
    b = math.sqrt(5.0 / 9.0 - 2.0 / 63.0 * math.sqrt(70))

    d = {
        "pm2": [
            [0.494522019130682e-1, 0.163914731881061, 0.265904816944092,],
            [0.949307350001342, 0.458177548931134, 0.774596669241483,],
            [a, a, b],
        ],
        "pmx": [
            [0.113041839046410, 0.479922229600720,],
            [0.967776908976724, 0.417754671502987,],
        ],
        "pmy": [[0.471199025241204e-1, 0.425447707110548,], [a, b]],
        "zero": [[-0.481503595164821e-1]],
    }
    points, weights = expand_symmetries(d)
    weights /= 4
    return C2Scheme("Franke 3c", weights, points, 9, source)


def franke_5():
    # DUP Noted as a duplicate in the original article
    return tyler_2()


def franke_6():
    a = sqrt(frac(3, 2))
    b = sqrt(frac(3, 7) * (1 + sqrt(frac(10, 31))))
    c = sqrt(frac(3, 7) * (1 - sqrt(frac(10, 31))))

    weights, points = concat(
        zero(frac(392, 405)),
        symm_s([frac(16, 2025), a]),
        symm_s_t([frac(1519, 4050), b, c]),
    )
    weights /= 4
    return C2Scheme("Franke 6", weights, points, 7, source)


def franke_7():
    # DUP Noted as a duplicate in the original article
    return rabinowitz_richter_1()


def franke_8():
    # TODO find error in franke_8
    warnings.warn("Franke(8) only has degree 1.")

    weights, points = concat(
        symm_r0([0.454163960686749, 0.488926856974369]),
        symm_s(
            [0.214200360926862, 0.690880550486344],
            [0.427312318657758e-1, 0.939565258096838],
        ),
        symm_s_t([0.144452223260307, 0.918620441056722, 0.344872025364404]),
    )
    weights /= 4
    return C2Scheme("Franke 8", weights, points, 1, source)
