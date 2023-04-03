import random
from trump import Trump


class Game:

    # トランプ用
    __suits_types = ["♠", "♥", "♣", "♦"]
    __numbers_id = ["A", "2", "3", "4", "5", "6","7", "8", "9", "10", "K", "Q", "J"]


    def __init__(self) -> None:
        self.__total_game = 0
        self.__deck = []
        self.__first = True
        self.__last = False

    def reset_game(self):
        self.__deck = []
        self.__first = True
        self.__last = False
        self.__reset_deck()

    def __reset_deck(self):
        for i in Game.__suits_types:
            for j in Game.__numbers_id:
                self.__deck.append(Trump(i, j))
        random.shuffle(self.__deck)
    
    def draw_deck(self):
        return self.__deck.pop()
    
    def judge(self, pl_total, com_total):
        state = {0:"ゲーム続行",1:"勝者:プレイヤー",2:"勝者:COM",3:"引き分け"}
        # バスト勝敗
        if pl_total > 21:
            return state[2]
        elif com_total >21:
            return state[1]
        elif self.__last == True:
            if pl_total > com_total and pl_total < 22:
                return state[1]
            elif com_total > pl_total and com_total < 22:
                return state[2]
            else:
                return state[3]
        # 初回ターン処理
        elif self.__first == True:
            if pl_total == 21 and com_total < pl_total:
                return state[1]
            elif com_total == 21 and com_total > pl_total:
                return state[2]
            else:
                if pl_total == 21 and com_total == 21:
                    return state[3]
    
        return state[0]
    

    
    def first_turn_end(self):
        self.__first = False
    
    def end_game(self):
        self.__last = True

    @property
    def first(self):
        return self.__first
    
    @property
    def total_game(self):
        return self.__total_game
    
    def add_total_game(self):
        self.__total_game += 1

    def debug_bj(self):
        return Trump("♠","A"),Trump("♠","K")