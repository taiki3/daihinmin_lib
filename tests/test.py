import unittest
import dhlib

class TestGetACardFromString(unittest.TestCase):

    def test_blank(self):
        string = ""
        card = dhlib.get_a_card_from_string(string)
        self.assertEqual(card, 0)

    def test_jkr_upper(self):
        string = "JKR"
        card = dhlib.get_a_card_from_string(string)
        self.assertEqual(card, 0b1<<52)

    def test_jkr_lower(self):
        string = "jkr"
        card = dhlib.get_a_card_from_string(string)
        self.assertEqual(card, 0b1<<52)

    def test_jkr_upper_camel(self):
        string = "Jkr"
        card = dhlib.get_a_card_from_string(string)
        self.assertEqual(card, 0b1<<52)

    def test_joker_upper(self):
        string = "JOKER"
        card = dhlib.get_a_card_from_string(string)
        self.assertEqual(card, 0b1<<52)

    def test_joker_lower(self):
        string = "joker"
        card = dhlib.get_a_card_from_string(string)
        self.assertEqual(card, 0b1<<52)

    def test_joker_upper_camel(self):
        string = "Joker"
        card = dhlib.get_a_card_from_string(string)
        self.assertEqual(card, 0b1<<52)

    def test_jk_upper(self):
        string = "JK"
        card = dhlib.get_a_card_from_string(string)
        self.assertEqual(card, 0b1<<52)

    def test_jk_upper_camel(self):
        string = "Jk"
        card = dhlib.get_a_card_from_string(string)
        self.assertEqual(card, 0b1<<52)

    def test_jk_lower(self):
        string = "jk"
        card = dhlib.get_a_card_from_string(string)
        self.assertEqual(card, 0b1<<52)

    def test_red_joker_upper(self):
        string = "RED_JOKER"
        card = dhlib.get_a_card_from_string(string)
        self.assertEqual(card, 0b1<<52)

    def test_red_joker_lower(self):
        string = "red+joker"
        card = dhlib.get_a_card_from_string(string)
        self.assertEqual(card, 0b1<<52)

    def test_red_joker_upper_camel(self):
        string = "RedJoker"
        card = dhlib.get_a_card_from_string(string)
        self.assertEqual(card, 0b1<<52)

    def test_jkr1_upper(self):
        string = "JKR1"
        card = dhlib.get_a_card_from_string(string)
        self.assertEqual(card, 0b1<<52)

    def test_jkr1_upper_camel(self):
        string = "Jkr1"
        card = dhlib.get_a_card_from_string(string)
        self.assertEqual(card, 0b1<<52)

    def test_joker1_upper(self):
        string = "JOKER1"
        card = dhlib.get_a_card_from_string(string)
        self.assertEqual(card, 0b1<<52)

    def test_joker1_upper_camel(self):
        string = "Joker1"
        card = dhlib.get_a_card_from_string(string)
        self.assertEqual(card, 0b1<<52)

    def test_jk1_upper(self):
        string = "JK1"
        card = dhlib.get_a_card_from_string(string)
        self.assertEqual(card, 0b1<<52)

    def test_jk1_upper_camel(self):
        string = "Jk1"
        card = dhlib.get_a_card_from_string(string)
        self.assertEqual(card, 0b1<<52)

    def test_jk1_lower(self):
        string = "jk1"
        card = dhlib.get_a_card_from_string(string)
        self.assertEqual(card, 0b1<<52)

    def test_black_joker_upper(self):
        string = "BLACK_JOKER"
        card = dhlib.get_a_card_from_string(string)
        self.assertEqual(card, 0b1<<53)

    def test_black_joker_lower(self):
        string = "black*joker"
        card = dhlib.get_a_card_from_string(string)
        self.assertEqual(card, 0b1<<53)

    def test_black_joker_upper_camel(self):
        string = "Black-joker"
        card = dhlib.get_a_card_from_string(string)
        self.assertEqual(card, 0b1<<53)

    def test_jkr2_upper(self):
        string = "JKR2"
        card = dhlib.get_a_card_from_string(string)
        self.assertEqual(card, 0b1<<53)

    def test_jkr2_lower(self):
        string = "jkr2"
        card = dhlib.get_a_card_from_string(string)
        self.assertEqual(card, 0b1<<53)

    def test_jkr2_upper_camel(self):
        string = "Jkr2"
        card = dhlib.get_a_card_from_string(string)
        self.assertEqual(card, 0b1<<53)

    def test_joker2_upper(self):
        string = "JOKER2"
        card = dhlib.get_a_card_from_string(string)
        self.assertEqual(card, 0b1<<53)

    def test_joker2_lower(self):
        string = "joker2"
        card = dhlib.get_a_card_from_string(string)
        self.assertEqual(card, 0b1<<53)

    def test_joker2_upper_camel(self):
        string = "Joker2"
        card = dhlib.get_a_card_from_string(string)
        self.assertEqual(card, 0b1<<53)

    def test_jk2_upper(self):
        string = "JK2"
        card = dhlib.get_a_card_from_string(string)
        self.assertEqual(card, 0b1<<53)

    def test_jk2_upper_camel(self):
        string = "Jk2"
        card = dhlib.get_a_card_from_string(string)
        self.assertEqual(card, 0b1<<53)

    def test_jk2_lower(self):
        string = "jk2"
        card = dhlib.get_a_card_from_string(string)
        self.assertEqual(card, 0b1<<53)

    def test_bad_joker(self):
        string = "JKRRRRR"
        cards = dhlib.get_a_card_from_string(string)
        self.assertEqual(cards, False)

    def test_bad_joker2(self):
        string = "BBBLACK_JOKER"
        cards = dhlib.get_a_card_from_string(string)
        self.assertEqual(cards, False)

    def test_suit_only(self):
        string = "s"
        card = dhlib.get_a_card_from_string(string)
        self.assertEqual(card, False)

    def test_num_only(self):
        string = "11"
        card = dhlib.get_a_card_from_string(string)
        self.assertEqual(card, False)

    def test_bad_string(self):
        string = "Z"
        card = dhlib.get_a_card_from_string(string)
        self.assertEqual(card, False)

    def test_not_string(self):
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

    def test_suit_upper(self):
        string = "S12"
        card = dhlib.get_a_card_from_string(string)
        self.assertEqual(card, 0b1<<39)

    def test_bad_suit(self):
        string = "t4"
        card = dhlib.get_a_card_from_string(string)
        self.assertEqual(card, False)

    def test_bad_num(self):
        string = "d14"
        card = dhlib.get_a_card_from_string(string)
        self.assertEqual(card, False)


class TestGetCardsFromString(unittest.TestCase):

    def test_one_card(self):
        string = "h1"
        cards = dhlib.get_cards_from_string(string)
        self.assertEqual(cards, 0b1<<46)

    def test_two_card(self):
        string = "h1 s5"
        cards = dhlib.get_cards_from_string(string)
        self.assertEqual(cards, 0b1<<46 | 0b1<<11)

    def test_same_card(self):
        string = "S5 s5"
        cards = dhlib.get_cards_from_string(string)
        self.assertEqual(cards, 0b1<<11)

    def test_one_joker(self):
        string = "JOKER"
        cards = dhlib.get_cards_from_string(string)
        self.assertEqual(cards, 0b1<<52)

    def test_two_joker(self):
        string = "JKR1 joker2"
        cards = dhlib.get_cards_from_string(string)
        self.assertEqual(cards, 0b1<<52 | 0b1<<53)

    def test_same_joker(self):
        string = "JKR1 red_joker"
        cards = dhlib.get_cards_from_string(string)
        self.assertEqual(cards, 0b1<<52)

    def test_bad_joker(self):
        string = "JOOOkER"
        cards = dhlib.get_cards_from_string(string)
        self.assertEqual(cards, False)

    def test_one_card_and_joker(self):
        string = "s5 JKR"
        cards = dhlib.get_cards_from_string(string)
        self.assertEqual(cards, 0b1<<11 | 0b1<<52)

    def test_multiple_delimiters(self):
        string = "s8 d2, c4    h2"
        cards = dhlib.get_cards_from_string(string)
        bit_cards = 0b1<<23 | 0b1<<49 | 0b1<<4 | 0b1<<50
        self.assertEqual(cards, bit_cards)

    def test_no_delimiters(self):
        string = "s5c9hJd13"
        cards = dhlib.get_cards_from_string(string)
        self.assertEqual(cards, False)

    def test_bad_card(self):
        string = "q5"
        cards = dhlib.get_cards_from_string(string)
        self.assertEqual(cards, False)

    def test_two_bad_card(self):
        string = "q5 3"
        cards = dhlib.get_cards_from_string(string)
        self.assertEqual(cards, False)

    def test_sandwich_bad_card(self):
        string = "c8 q5 s3"
        cards = dhlib.get_cards_from_string(string)
        self.assertEqual(cards, False)

    def test_normal_card_and_bad_card(self):
        string = "s5 u8"
        cards = dhlib.get_cards_from_string(string)
        self.assertEqual(cards, False)

    def test_bad_delimiter(self):
        string = "s8|d2"
        cards = dhlib.get_cards_from_string(string)
        self.assertEqual(cards, False)

