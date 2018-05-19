import re

#####
# BitCard(BitCards) における各ビットはそれぞれのカードの所持/非所持を意味する
# スートの強さは s > h > d > c とする
#      3  4  5  6  7  8  9 10  J  Q  K  A  2 JKR
#  c|  0  4  8 12 16 20 24 28 32 36 40 44 48 52
#  d|  1  5  9 13 17 21 25 29 33 37 41 45 49 53
#  h|  2  6 10 14 18 22 26 30 34 38 42 46 50
#  s|  3  7 11 15 19 23 27 31 35 39 43 47 51
#####

SUIT = (0,1,2,3)
RANK = (0,1,2,3,4,5,6,7,8,9,10,11,12)

pattern_num_card = r"[SHDCshdc](((?<!\d)([1-9]|1[0-3])(?!\d))|[JQKAjqka])"
pattern_joker = r"(JKR|JOKER|jkr|joker)(?![12])$"
pattern_red_joker = r"RED_JOKER|JKR1|JOKER1|red_joker|jkr1|joker1"
pattern_black_joker = r"BLACK_JOKER|JKR2|JOKER2|black_oker|jkr2|joker2"

def get_joker():
    return 0b1 << 52

def get_red_joker():
    return 0b1 << 52

def get_black_joker():
    return 0b1 << 53

def get_suit_from_string(string_suit):
    if "c"  in string_suit.lower(): return 0
    elif "d"  in string_suit.lower(): return 1
    elif "h"  in string_suit.lower(): return 2
    elif "s"  in string_suit.lower(): return 3
    else:
        return False

def get_rank_from_string(string_num):
# 3をRANK0としたときのRANKを表す
    if isinstance(string_num, str):
        if "J"  in string_num.upper(): return 8
        elif "Q"  in string_num.upper(): return 9
        elif "K"  in string_num.upper(): return 10
        elif "A"  in string_num.upper(): return 11
        elif "1"  in string_num: return 11
        elif "2"  in string_num: return 12

    try:
        card_num = int(string_num)
    except ValueError:
        return False

    if card_num < 9 and card_num > 2 :
        return card_num - 3
    elif card_num is 1: return 11
    elif card_num is 2: return 12
    else:
        return False

def get_a_card_from_string(string_card):
    if not isinstance(string_card, str): return False

    match_num_card = re.match(pattern_num_card, string_card)
    if match_num_card:
        match_string = match_num_card.group()
        suit = get_suit_from_string(match_string[0:1])
        rank = get_rank_from_string(match_string[1:])
        return 0b1 << (rank*4 + suit)
    elif string_card is "" : return 0
    elif re.match(pattern_joker, string_card): return get_joker()
    elif re.match(pattern_red_joker, string_card): return get_red_joker()
    elif re.match(pattern_black_joker, string_card): return get_black_joker()
    else:
        return False


if __name__ == '__main__':
    print(bin(get_a_card_from_string("h5")))


#########
###以下、未改修
#########
def gen_bit_card_from_string(self, str):
    if str == "": return 0b0

    if "JKR" in str: return 0b1 << 52

    suit, num = str[0:1], str[1:]
    return 0b1 << BitCard.GRADE[num] * 4 + BitCard.SUIT[suit]

def genBitCardsFromString(self, str):
    bitCards = 0b0

    if (" " in str):
        delimiter = " "
    elif ("," in str):
        delimiter = ","
        str = str.replace(" ", "")
    else:
        return BitCard().genBitCardFromString(str)

    for s in str.split(delimiter):
        if s is not "":
            bitCards = bitCards | self.genBitCardFromString(s)

    return bitCards

def getCardsFromBitCards(self):
    cards = []
    if (self.bitCards & pow(2, 52)): cards.append(Card("JKR", "JKR"))

    for s, v in BitCard.SUIT.items():
        for r, u in BitCard.GRADE.items():
            if (self.bitCards & pow(2, u * 4 + v)): cards.append(Card(s, r))

    return cards

def getStringCardsFromBitCards(self):
    str = ""
    for c in BitCard.getCardsFromBitCards(self.bitCards):
        if (c.suit is "JKR"):
            str += "JKR "
        else:
            str += c.suit + c.num + " "

    return str.strip()

def getNumberOfBitCards(self):
    return bin(self.bitCards).count("1")

def getNumberOfBitCards(self, c):
    return bin(c).count("1")

def getStringTableFromBitCards(self):
    str = "   3 4 5 6 7 8 9 X J Q K A 2\n"
    for s, v in sorted(BitCard.SUIT.items()):
        str += s + "|"

        for u in sorted(BitCard.GRADE.values()):
            str += '{:>2}'.format(1 if (self.bitCards & pow(2, u * 4 + v)) else 0)
        str += "\n"

    str += "JKR:1" if (self.bitCards & pow(2, 52)) else "JKR:0"

    return str

def isLock(self, bc1, bc2):
    vBc1 = (bin(bc1 & 0x0001111111111111).count("1") * 1 +
            bin(bc1 & 0x0002222222222222).count("1") * 2 +
            bin(bc1 & 0x0004444444444444).count("1") * 4 +
            bin(bc1 & 0x0008888888888888).count("1") * 8)

    vBc2 = (bin(bc2 & 0x0001111111111111).count("1") * 1 +
            bin(bc2 & 0x0002222222222222).count("1") * 2 +
            bin(bc2 & 0x0004444444444444).count("1") * 4 +
            bin(bc2 & 0x0008888888888888).count("1") * 8)

    return True if (vBc1 is vBc2) else False

class Player:
    def __init__(self, name, hand=0b0, used=0b0):
        self.name = name
        self.hand = hand
        self.used = used

    def getCards(self):
        return [(card.suit, card.num) for card in self.cards]

    def getPlayer(self, name):
        return self

    def setCardsFromString(self, str):
        self.hand = BitCard().getBitCardsFromString(str)
        return self.hand

    def getCards(self):
        return BitCard().getStringCardsFromBitCards(self.hand)


class State:
    def __init__(self, gameId=0, board=0b0, order={}, nOrder="", pRank={}, nRank={}, player={}, pPlayer=[], lPlayer="",
                 bind=False, revo=False):
        self.gameId = gameId
        self.board = board
        self.order = order
        self.nOrder = nOrder
        self.pRank = pRank
        self.nRank = nRank
        self.player = player
        self.pPlayer = pPlayer
        self.lPlayer = lPlayer
        self.bind = bind
        self.revo = revo

    def getOrderNext(self, nOrder):
        for k, v in self.order.items():
            if (v is nOrder.name):
                if k < len(self.order):
                    return self.order[k + 1]
                else:
                    return self.order[1]

    def getState(self):
        return self.gameId, self.board, self.order, self.nOrder, self.pRank, self.nRank, self.player, self.pPlayer, self.lPlayer, self.bind, self.revo


class StateExch:
    def __init__(self, gameId=0, exchNum=0, exchTo=Player(""), exchFrom=Player(""), player=[]):
        self.gameId = gameId
        self.exchNum = exchNum
        self.exchTo = exchTo
        self.exchFrom = exchFrom
        self.player = player

    def getStateExch(self):
        return self.gameId, self.exchNum, self.exchTo, self.exchFrom, self.player

    def getPlayersCard(self):
        return [p.hand for p in self.player]

