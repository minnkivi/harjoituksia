# Ohjelma tarkistaa, onko sille annettu sosiaaliturvatunnus validi suomalainen sosiaaliturvatunnus.
# Validi tunnus on määritelty esim. Wikipediassa.
# Ohjelma tunnistaa oikeiksi vain väestörekisteriin kirjattavat viralliset sosiaaliturvatunnukset, ei
# tilapäisiä tunnuksia.

import re

def on_validi_muoto(sotu: str) -> bool:
    """Tarkistaa, että annettu sosiaaliturvatunnus on oikean muotoinen, eli 6 digitiä (henkilön syntymäaika muodossa ppkkvv), 
       välimerkkinä +,- tai A ja sen jälkeen 3 digitiä ja yksi tarkistusmerkki (numero tai kirjain), esim. 031187-846J.

    Args:
        sotu (str): tarkistettava sosiaaliturvatunnus

    Returns:
        bool: True, jos annettu sosiaaliturvatunnus on muodoltaan oikeanlainen
    """
    return bool(re.match("^[0-9]{6}['+'|'\-'|'A'][0-8][0-9][0-9][A-Y0-9]", sotu))


def jaa_osiin(sotu: str) -> list:
    """Jakaa annetun sosiaaliturvatunnuksen osiin: syntymäajan päivään, kuukauteen ja vuoteen sekä tunnuksen loppuosaan. 
       Sosiaaliturvatunnuksen kahden digitin pituiseen vuosiosaan lisätään vuosisadat, jotta saadaan täydellinen syntymävuosi
       (päivän oikeellisuuden tarkistuksessa on tiedettävä, onko kyseessä karkausvuosi). Vuosisata määräytyy välimerkin 
       mukaan seuraavasti: '+' 1800-luku, '-' 1900-luku, 'A' 2000-luku.

    Args:
        sotu (str): sosiaaliturvatunnus, jonka validius halutaan tarkistaa

    Returns:
        list: lista, jonka alkiot ovat sosiaaliturvatunnuksen syntymäajan päivä, kuukausi ja täydellinen vuosi kokonaislukuina
        sekä tunnuksen loppuosa merkkijonona.
    """
    osat = []
    osat.append(int(sotu[:2]))
    osat.append(int(sotu[2:4]))
    osat.append(int(sotu[4:6]))
    osat.append((sotu[7:12]))

    if sotu[6] == "+":
        osat[2] += 1800
    if sotu[6] == "-":
        osat[2] += 1900
    if sotu[6] == "A":
        osat[2] += 2000

    return osat


def on_karkausvuosi(vuosi: int) -> bool:
    """Tarkistaa, onko vuosi karkausvuosi. Vuosi on karkausvuosi, jos se on jaollinen 4:llä, paitsi täydet vuosisadat 
       (eli sadalla jaolliset vuodet) ovat karkausvuosia vain, jos ne ovat jaollisia myös 400:llä. 

    Args:
        vuosi (int): vuosi, josta halutaan selvittää, onko se karkausvuosi

    Returns:
        bool: True, jos vuosi on karkausvuosi
    """
    if (vuosi % 4) == 0:
        if (vuosi % 100) == 0:
            if (vuosi % 400) == 0:
                return True
            else:
                return False
        else:
            return True
    else:
       return False


def on_ok_paiva(paiva: int, kk: int, vuosi: int) -> bool:
    """Tarkistaa, että syntymäajassa päivä on validi (ei suurempi  kuin syntymäkuukaudessa olevien päivien lukumäärä).

    Args:
        paiva (int): syntymäajan päivä
        kk (int): syntymäajan kuukausi
        vuosi (int): syntymäajan vuosi

    Returns:
        bool: True, jos annetun syntymäajan päivä on validi
    """
    kk_ja_paivat = {
        1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:30
    }

    if on_karkausvuosi(vuosi):
        kk_ja_paivat[2] = 29

    if paiva > kk_ja_paivat[kk]:
        return False
    else:
        return True


def on_ok_kuukausi(kk: int) -> bool:
    """Tarkistaa, että sosiaaliturvatunnuksessa annettu syntymäajan kuukausi on validi (vähintään 1, korkeintaan 12).

    Args:
        kk (int): takistettava kuukausi

    Returns:
        bool: True, jos kuukausi on validi
    """
    return 0 < kk < 13


def on_ok_loppuosa(sotu: str) -> bool:
    """Tarkistaa, että sosiaaliturvatunnuksen loppuosa on validi (tarkistusnumero on oikein). Tarkistetaan myös, että
       loppuosan kolme ensimmäistä merkkiä eivät ole 000 tai 001, joita ei virallisissa tunnuksissa käytetä, vaikka
       menevätkin muodon oikeellisuuden tarkistuksesta läpi.
       Validin sosiaaliturvatunnuksen viimeinen merkki vastaa jakojäännöstä, joka saadaan jakamalla syntymäajan ja 
       loppuosan kolmen ensimmäisen numeron muodostama 9-numeroinen luku (ppkkvvnnn) 31:llä.

    Args:
        sotu (str): sosiaaliturvatunnus, jonka validius halutaan tarkistaa

    Returns:
        bool: True, jos sosiaaliturvatunnuksen loppuosa on validi
    """
    jakojaannokset = {
        0:"0", 1:"1", 2:"2", 3:"3", 4:"4", 5:"5", 6:"6", 7:"7", 8:"8", 9:"9", 10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F", 16: "H",
        17: "J", 18: "K", 19: "L", 20: "M", 21: "N", 22: "P", 23: "R", 24:"S", 25:"T", 26:"U", 27:"V", 28:"W", 29:"X", 30:"Y"
    }
    
    if sotu[7:9] == "00" and int(sotu[9]) < 2:
        return False
    else:
        jakojaannos = int(sotu[:6] + sotu[7:10])%31
        if sotu[10] == jakojaannokset[jakojaannos]:
            return True
        else:
            return False


def main():
    
    sotu = input("Anna tarkistettava sosiaaliturvatunnus: ")

    if not on_validi_muoto(sotu):
        print("Antamasi sosiaaliturvatunnus ei ole oikea.")
        exit()

    syntyma_paiva = jaa_osiin(sotu)[0]
    syntyma_kuukausi = jaa_osiin(sotu)[1]
    syntyma_vuosi = jaa_osiin(sotu)[2]
    loppuosa = jaa_osiin(sotu)[3]

    if not on_ok_kuukausi(syntyma_kuukausi):
        print("Antamasi sosiaaliturvatunnus ei ole oikea.")
        exit()

    if not on_ok_paiva(syntyma_paiva, syntyma_kuukausi, syntyma_vuosi):
        print("Antamasi sosiaaliturvatunnus ei ole oikea.")
        exit()
    
    if not on_ok_loppuosa(sotu):
        print("Antamasi sosiaaliturvatunnus ei ole oikea.")
        exit()        
    
    print("Antamasi sosiaaliturvatunnus on validi suomalainen sosiaaliturvatunnus.")


if __name__ == "__main__":
    main()

    


