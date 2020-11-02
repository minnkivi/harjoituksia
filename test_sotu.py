import unittest

import sotu

class Tests(unittest.TestCase):

    def test_on_validi_muoto(self):
        self.assertTrue(sotu.on_validi_muoto("123456-1234"))
        self.assertTrue(sotu.on_validi_muoto("123456+1234"))
        self.assertTrue(sotu.on_validi_muoto("123456A1234"))
        self.assertFalse(sotu.on_validi_muoto("123456:1234"))
        self.assertFalse(sotu.on_validi_muoto("12345-1234"))
        self.assertTrue(sotu.on_validi_muoto("123456-123A"))
        self.assertFalse(sotu.on_validi_muoto("123456-123b"))
        self.assertFalse(sotu.on_validi_muoto("123456-123"))
        self.assertFalse(sotu.on_validi_muoto("1234561234"))
        self.assertFalse(sotu.on_validi_muoto("123a56-1234"))
        self.assertFalse(sotu.on_validi_muoto("123456-12AA"))
        self.assertFalse(sotu.on_validi_muoto("123456AA123"))
        self.assertFalse(sotu.on_validi_muoto("123456++1234"))
        self.assertTrue(sotu.on_validi_muoto("000000+0000"))
        self.assertFalse(sotu.on_validi_muoto("110475-9499"))


    def test_jaa_osiin(self):
        self.assertEqual(sotu.jaa_osiin("123456-1234"), [12, 34, 1956, "1234"])
        self.assertEqual(sotu.jaa_osiin("123456+1234"), [12, 34, 1856, "1234"])
        self.assertEqual(sotu.jaa_osiin("123456A1234"), [12, 34, 2056, "1234"])
        self.assertEqual(sotu.jaa_osiin("123456-123A"), [12, 34, 1956, "123A"])
        self.assertNotEqual(sotu.jaa_osiin("123456:1234"), [12, 34, 1956, "1234"])
        self.assertEqual(sotu.jaa_osiin("000000+0000"), [0, 0, 1800, "0000"])

    def test_on_karkausvuosi(self):
        self.assertTrue(sotu.on_karkausvuosi(1944))
        self.assertTrue(sotu.on_karkausvuosi(2000))
        self.assertTrue(sotu.on_karkausvuosi(2024))
        self.assertFalse(sotu.on_karkausvuosi(2010))
        self.assertFalse(sotu.on_karkausvuosi(1991))
        self.assertFalse(sotu.on_karkausvuosi(1900))

    def test_on_ok_paiva(self):
        self.assertTrue(sotu.on_ok_paiva(1, 1, 1990))
        self.assertTrue(sotu.on_ok_paiva(31, 1, 1990))
        self.assertTrue(sotu.on_ok_paiva(29, 2, 1992))
        self.assertTrue(sotu.on_ok_paiva(31, 12, 2019))
        self.assertFalse(sotu.on_ok_paiva(29, 2, 1990))
        self.assertFalse(sotu.on_ok_paiva(31, 4, 1990))
        self.assertFalse(sotu.on_ok_paiva(32, 8, 1990))
        self.assertFalse(sotu.on_ok_paiva(0, 1, 1990))

    def test_on_ok_kk(self):
        self.assertTrue(sotu.on_ok_kuukausi(1))
        self.assertTrue(sotu.on_ok_kuukausi(12))
        self.assertTrue(sotu.on_ok_kuukausi(6))
        self.assertFalse(sotu.on_ok_kuukausi(0))
        self.assertFalse(sotu.on_ok_kuukausi(-3))
        self.assertFalse(sotu.on_ok_kuukausi(17))

    def test_on_ok_loppuosa(self):
        self.assertTrue(sotu.on_ok_loppuosa("250159-797V"))
        self.assertTrue(sotu.on_ok_loppuosa("130545-353D"))
        self.assertTrue(sotu.on_ok_loppuosa("050804A4120"))
        self.assertTrue(sotu.on_ok_loppuosa("170272-0282"))
        self.assertFalse(sotu.on_ok_loppuosa("231164-0007"))
        self.assertFalse(sotu.on_ok_loppuosa("300899-001C"))
        self.assertFalse(sotu.on_ok_loppuosa("150413A1205"))


if __name__ == "__main__":
    unittest.main()