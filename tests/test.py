import unittest
import dhlib

class TestGetCardFromString(unittest.TestCase):

    def test_blank(self):
        string = ""
        card = dhlib.get_a_card_from_string(string)
        self.assertEqual(card, 0)

    def test_string_jkr(self):
        string = "JKR"
        card = dhlib.get_a_card_from_string(string)
        self.assertEqual(card, 0b1<<52)

    def test_string_joker(self):
        string = "JOKER"
        card = dhlib.get_a_card_from_string(string)
        self.assertEqual(card, 0b1<<52)

    def test_string_red_joker(self):
        string = "RED_JOKER"
        card = dhlib.get_a_card_from_string(string)
        self.assertEqual(card, 0b1<<52)

    def test_string_jkr1(self):
        string = "JKR1"
        card = dhlib.get_a_card_from_string(string)
        self.assertEqual(card, 0b1<<52)

    def test_string_joker1(self):
        string = "JOKER1"
        card = dhlib.get_a_card_from_string(string)
        self.assertEqual(card, 0b1<<52)

    def test_string_black_joker(self):
        string = "BLACK_JOKER"
        card = dhlib.get_a_card_from_string(string)
        self.assertEqual(card, 0b1<<53)

    def test_string_jkr2(self):
        string = "JKR2"
        card = dhlib.get_a_card_from_string(string)
        self.assertEqual(card, 0b1<<53)

    def test_string_joker2(self):
        string = "JOKER2"
        card = dhlib.get_a_card_from_string(string)
        self.assertEqual(card, 0b1<<53)

    def test_bad_case_num(self):
        string = "14"
        card = dhlib.get_a_card_from_string(string)
        self.assertEqual(card, False)

    def test_bad_case_string(self):
        string = "Z"
        card = dhlib.get_a_card_from_string(string)
        self.assertEqual(card, False)

    def test_bad_case_int(self):
        string = 5
        card = dhlib.get_a_card_from_string(string)
        self.assertEqual(card, False)

    def test_normal_card_num(self):
        string = "h5"
        card = dhlib.get_a_card_from_string(string)
        self.assertEqual(card, 0b1<<10)

    def test_normal_card_face(self):
        string = "cJ"
        card = dhlib.get_a_card_from_string(string)
        self.assertEqual(card, 0b1<<32)