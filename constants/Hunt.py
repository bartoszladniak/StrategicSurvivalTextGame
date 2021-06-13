from enum import Enum


class Hunt(Enum):
    FOOD_RABBIT = "Nagły ruch w trawie zwraca twoją uwagę. Mignęła ci para długich uszu, ale zniknęły zaraz,\n" \
                  "    uciekając przed twoim wzrokiem. Zdaje się jednak, że znasz kierunek, w którym ruszyły zające\n" \
                  "    - możesz spróbować je upolować."
    FOOD_TURTLE = "Na plaży piaskiem obkopuje się żółw. Wydaje się, że chroni złożone jaja - a tym bardziej\n" \
                  "    nie wie o twojej obecności."
    FOOD_BOAR = "W lesie pod drzewami odnajdujesz głębokie bruzdy. Dziki ryły tutaj, poszukując pożywienia\n" \
                "    i wciąż mogą być niedaleko."
    FOOD_BEAR = "Kołysząc się, niedźwiedź przechadza się między drzewami, a jego młode idzie tuż za nim.\n" \
                "    Może możliwe będzie odciągnięcie go od rodzica."
    FOOD_NONE = "Las wydaje się być dziś pusty."
