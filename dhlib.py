import re
import itertools

#####
# BitCard(BitCards) における各ビット位置（下記）はそれぞれのカードの所持/非所持を意味する
# スートの強さは s > h > d > c とする
# ジョーカーを1枚だけ用いるときは52を利用する
# RANK 0  1  2  3  4  5  6  7  8  9 10 11 12 -
#     -------------------------------------------
#  NUM 3  4  5  6  7  8  9 10  J  Q  K  A  2 JKR
#  c|  0  4  8 12 16 20 24 28 32 36 40 44 48 52 (RED_JOKER)
#  d|  1  5  9 13 17 21 25 29 33 37 41 45 49 53 (BLACK_JOKER)
#  h|  2  6 10 14 18 22 26 30 34 38 42 46 50
#  s|  3  7 11 15 19 23 27 31 35 39 43 47 51
# SUIT
#####
SUIT_INDEX = {"c":0,"d":1,"h":2,"s":3}
RANK_INDEX = {3:0,4:1,5:2,6:3,7:4,8:5,9:6,10:7,11:8,12:9,13:10,1:11,2:12}
FACE_INDEX = {"J":8,"Q":9,"K":10,"A":11}

def get_card_index():
    cards = list(itertools.product(RANK_INDEX.keys(),SUIT_INDEX.keys()))
    return {str(c[1])+str(c[0]):0b1<<i for i,c in enumerate(cards)}
CARD_INDEX = get_card_index()
CARD_INDEX.update({"JOKER":0b1<<52})
CARD_INDEX_WITH_TWO_JOKER = get_card_index()
CARD_INDEX_WITH_TWO_JOKER.update({"RED_JOKER":0b1<<52,"BLACK_JOKER":0b1<<53})
# CARD_INDEXは上記のBitCard型とStringの対応表。{"string": ビット位置)
SUIT_MASK = {0: 0x0001111111111111,
             1: 0x0001111111111111*2,
             2: 0x0001111111111111*4,
             3: 0x0001111111111111*8}
RANK_MASK = {0: 0b1111, 1: 0b1111<<4,
             2: 0b1111<<8, 3: 0b1111<<12,
             4: 0b1111<<16, 5: 0b1111<<20,
             6: 0b1111<<24, 7: 0b1111<<28,
             8: 0b1111<<32, 9: 0b1111<<36,
             10: 0b1111<<40, 11: 0b1111<<44,
             12: 0b1111<<48}
JOKER = 0b1<<52
ALL_JOKER = 0b1<<52 | 0b1<<53
RED_JOKER = 0b1<<52
BLACK_JOKER = 0b1<<53

pattern_num_card = r"^([SHDCshdc](((?<!\d)([1-9]|1[0-3])(?!\d))|[JQKAjqka]))$"
pattern_face_card = r"^[JQKAjqka]$"
pattern_joker = r"^(JKR|JOKER|[Jj][Kk]|[Jj]kr|[Jj]oker)(?![12])$"
pattern_red_joker = r"^(RED.*(JOKER)|JKR1|JOKER1|[Jj][Kk]1|[Rr]ed.*([Jj]oker)|[Jj]kr1|[Jj]oker1)$"
pattern_black_joker = r"^(BLACK.*(JOKER)|JKR2|JOKER2|[Jj][Kk]2|[Bb]lack.*([Jj]oker)|[jJ]kr2|[Jj]oker2)$"

def get_suit_from_string(string_suit):
    return SUIT_INDEX[string_suit.lower()]

def get_rank_from_string(string_num):
    if string_num.upper() in FACE_INDEX.keys() :
    # FACEは[JQKA]を指す
        return FACE_INDEX[string_num]

    if string_num.isdigit:
        card_num = int(string_num)
    else: return False

    if 1 <= card_num <= 13:
        return RANK_INDEX[card_num]
    else: return False

def get_a_card_from_string(string_card):
    if not isinstance(string_card, str): return False

    match_num_card = re.match(pattern_num_card, string_card)
    if match_num_card:
        match_string = match_num_card.group()
        suit = get_suit_from_string(match_string[0:1])
        rank = get_rank_from_string(match_string[1:])
        return 0b1 << (rank*4 + suit)
    elif string_card is "" : return 0
    elif re.match(pattern_joker, string_card): return JOKER
    elif re.match(pattern_red_joker, string_card): return RED_JOKER
    elif re.match(pattern_black_joker, string_card): return BLACK_JOKER
    else:
        return False

def get_suit_from_a_card(bit_card):
    if bit_card & ALL_JOKER: return False
    return [k for k in SUIT_MASK.keys() if bit_card & SUIT_MASK[k]]

def get_rank_from_a_card(bit_card):
    if bit_card & ALL_JOKER: return False
    return [k for k in RANK_MASK.keys() if bit_card & RANK_MASK[k]]

def get_cards_from_string(string_cards):
    if not isinstance(string_cards, str): return False

    elements = [e for e in re.split('[ ,\\t]', string_cards) if e != ""]
    bit_card_list = [get_a_card_from_string(e) for e in elements]
    if not all(bit_card_list): return False
    bit_card_list = list(set(bit_card_list)) #重複除外
    bit_cards = sum(bit_card_list)

    return bit_cards

def get_string_from_cards(bit_cards):
    if not isinstance(bit_cards, int): return False
    if bit_cards >= JOKER<<1 : return False
    strings = [k for k,v in CARD_INDEX.items() if bit_cards & v]
    if not all(strings): return False
    return " ".join(strings)

def get_string_from_cards_with_two_joker(bit_cards):
    if not isinstance(bit_cards, int): return False
    if bit_cards >= BLACK_JOKER<<1: return False
    strings = [k for k,v in CARD_INDEX_WITH_TWO_JOKER.items() if bit_cards & v]
    if not all(strings): return False
    return " ".join(strings)

def get_number_of_cards(bit_cards):
    return bin(bit_cards).count("1")

def get_lower_rank_cards(rank):
    return (0b1 << rank*4) - 0b1

def get_upper_rank_cards(rank):
    all_cards = (0b1 << 52) - 0b1
    return all_cards & ~get_lower_rank_cards(rank+1)

def print_exist_cards_table(cards):
#主にデバッグ用
    string_table = "   3 4 5 6 7 8 9 X J Q K A 2\n"
    for string_suit, suit in SUIT_INDEX.items():
        string_table += (string_suit+"|")

        for rank in RANK_INDEX.values():
            if(cards & pow(2,rank*4+suit)):
                string_table += "{:>2}".format(1)
            else:
                string_table += " -"
        string_table += "\n"

    string_table += "JOKER1:[ 1 ]" if(cards & pow(2,52)) else "JOKER1:[ - ]"
    string_table += "  JOKER2:[ 1 ]" if(cards & pow(2,53)) else "  JOKER2:[ - ]"
    print(string_table)
    return

if __name__ == '__main__':
    pass
    print_exist_cards_table(get_upper_rank_cards(10))
    #get_string_from_cards(0b1<<3|0b1<<5)


#####
###以下、未改修 2018.05.19
#####

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

