def on_validi_muoto(sotu: str) -> bool:
    """Tarkistaa, että annettu sosiaaliturvatunnus on edes oikean muotoinen.

    Args:
        sotu (str): tarkistettava sosiaaliturvatunnus

    Returns:
        bool: True, jos annettu sosiaaliturvus on muodollisesti oikein
    """
    pass


def jaa_osiin(sotu: str) -> list:
    """Jakaa annetun sosiaaliturvatunnuksen osiin: syntymäajan päivään, kuukauteen ja vuoteen sekä tunnuksen loppuosaan.

    Args:
        sotu (str): sosiaaliturvatunnus, jonka validius halutaan tarkistaa

    Returns:
        list: lista, jonka alkiot ovat sosiaaliturvatunnuksen syntymäajan päivä, kuukausi ja vuosi ssekä tunnuksen loppuosa
        kokonaislukuina.
    """
    osat = []
    osat.append(int(sotu[:2]))
    osat.append(int(sotu[2:4]))
    osat.append(int(sotu[4:6]))
    osat.append(int(sotu[7:12]))
    return osat


def on_ok_paiva(paiva: int, kk: int, vuosi: int) -> bool:
    """Tarkistaa, että syntymäajassa päivä on validi

    Args:
        paiva (int): syntymäajan päivä
        kk (int): syntymäajan kuukausi
        vuosi (int): syntymäajan vuosi
    Returns:
        bool: True, jos annetun syntymäajan päivä on validi
    """
    pass


def on_ok_kuukausi(kk: int) -> bool:
    return kk < 13

def on_ok_loppuosa(sotu: str) -> bool:
    """Tarkistaa, että sosiaaliturvatunnuksen loppuosa on validi (tarkistusnumero on oikein)

    Args:
        sotu (str): sosiaaliturvatunnus, jonka validius halutaan tarkistaa

    Returns:
        bool: True, jos sosiaaliturvatunnuksen loppuosa on validi
    """
    pass

sotu = input("Anna tarkistettava sosiaaliturvatunnus: ")
osat = jaa_osiin(sotu)

    


