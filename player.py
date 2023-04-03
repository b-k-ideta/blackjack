
class Player:



    def __init__(self) -> None:
        self.__win_cnt = 0
        self.__cards = []
        self.__total_value = 0
        self.__stand = False
    
    def reset_player(self):
        self.__cards = []
        self.__total_value = 0
        self.__stand = False

    def add_cards(self, card):
        self.__cards.append(card)
        self.__calculation()

    
    @property
    def win_cnt(self):
        return self.__win_cnt
    
    @property
    def cards(self):
        return self.__cards
    
    @property
    def total_value(self):
        return self.__total_value
   
    # 集計メソッド
    def __calculation(self):
        cards = self.__cards
        numbers = {"A": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,"7": 7, "8": 8, "9": 9, "10": 10, "K": 10, "Q": 10, "J": 10}
        
        # 合計の一時的な集計
        def total_calc(cards):
            total_tmp = 0
            for i in cards:
                temp = numbers[i.number]
                total_tmp += temp
            return total_tmp

        # エース持ち２１以上にならないように計算
        def ace_calc(total_recalc, aces_cnt):
            if total_recalc <= 21:
                return total_recalc
            else:
                if aces_cnt > 0:
                    total_recalc = total_recalc - 10
                    aces_cnt -= 1
                    return ace_calc(total_recalc, aces_cnt)
                else:
                    return total_recalc

        aces = 0
        total = total_calc(cards)

        for i in cards:
            if i.number == "A":
                aces += 1
        if aces > 0:
            total += 10*aces
            total = ace_calc(total, aces)
        
        self.__total_value = total

    # def com_draw(self):
    #     if self.__total_value < 17:
    #         self.add_cards()
    
    def stand(self):
        self.__stand = True

    @property
    def player_stand(self):
        return self.__stand
    
    def can_split(self, first_turn=False):
        if first_turn == True:
            if self.__cards[0].number == self.__cards[1].number:
                return True
    
    def card_split(self,card):
        self.__cards.pop()
        self.__cards.append(card)
        self.__calculation()

    def add_win(self):
        self.__win_cnt += 1


    