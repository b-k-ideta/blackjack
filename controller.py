import time
from game import Game
from player import Player
import views

class Controller:

    def __init__(self) -> None:
        self.__state = 0
        self.__game_obj = Game()
        self.__player = Player()
        self.__com = Player()
        self.__loop_flag = True
        self.__who_win = ""
        self.__view_handler()
        

    def __view_handler(self):
        while 1:
            # __stateの値によって画面が変わる
            match self.__state:
                case 0:
                    self.__title_screen()
                case 1:
                    self.reset_loop_winner()
                    self.__main_loop()
                case 2:
                    self.__game_over()
                case 3:
                    exit()
    
    def player_input(self):
        while 1:
            try:
                inp = int(input(">>>"))
                if inp == 0:
                    return 0
                elif inp == 1:
                    return 1
                else:
                    views.error_message()
                    time.sleep(1)
            except ValueError:
                views.error_message()
                time.sleep(1)
    
    # タイトル画面
    def __title_screen(self):  
        while 1:
            views.title_aa()
            views.title_menu()
            start_game = self.player_input()
            if start_game == 0:
                self.__state = 1
                return
            elif start_game == 1:
                self.__state = 3
                return
    
    # メインループ
    def __main_loop(self):

        game_obj = self.__game_obj
        player = self.__player
        com = self.__com

        def reset_all():
            game_obj.reset_game()
            player.reset_player()
            com.reset_player()
        
        def main_display(result=False):
            views.pl_com_disp(player.cards,player.win_cnt,com.cards,com.win_cnt,game_obj.total_game,result)

        def game_condition():

            state = game_obj.judge(player.total_value,com.total_value)
            match state:
                case "ゲーム続行":
                    pass
                case "勝者:プレイヤー":
                    self.loop_break()
                    player.add_win()
                    game_obj.add_total_game()
                    self.who_won("Player")
                case "勝者:COM":
                    self.loop_break()
                    com.add_win()
                    game_obj.add_total_game()
                    self.who_won("COM")
                case "引き分け":
                    self.loop_break()
                    game_obj.add_total_game()
                    self.who_won("Draw")
                    
        reset_all()

        while self.loop_flag == True:
            if game_obj.first == True:
                for i in range(2):
                    player.add_cards(game_obj.draw_deck())
                # card1,card2 = game_obj.debug_bj()
                # player.add_cards(card1)
                # player.add_cards(card2)
                for i in range(2):
                    com.add_cards(game_obj.draw_deck())
                while 1:
                    main_display()
                    if player.can_split() == True:
                        views.split_message()
                        pl_input = self.player_input()
                        match pl_input:
                            case 0:
                                player.card_split(game_obj.draw_deck())
                            case 1:
                                break
                    else:
                        break  
                game_condition()
                if self.loop_flag == False:
                    break
                game_obj.first_turn_end()
            main_display()
            if player.player_stand == False:
                views.hit_or_stand()
                pl_input = self.player_input()
                match pl_input:
                    case 0:
                        player.add_cards(game_obj.draw_deck())
                        main_display()
                        game_condition()
                        if self.loop_flag == False:
                            break
                    case 1:
                        player.stand() 
            if com.total_value >= 17 and player.player_stand == True:
                game_obj.end_game()
                game_condition()
            elif com.total_value < 17:
                com.add_cards(game_obj.draw_deck())
                main_display()
                game_condition()

        main_display(result=True)
        views.post_msg(self.winner,player.total_value,com.total_value,game_obj.first)
        self.__state = 2
        return


    
    def __game_over(self):
        while 1:
            views.game_over()
            continue_or_not = self.player_input()
            if continue_or_not == 0:
                self.__state = 1
                return
            elif continue_or_not == 1:
                self.__state = 0
                return
            else:
                pass


    def who_won(self, who:str):
        self.__who_win = who

    def loop_break(self):
        self.__loop_flag = False

    def reset_loop_winner(self):
        self.__loop_flag = True
        self.__who_win = ""


    @property
    def loop_flag(self):
        return self.__loop_flag
    
    @property
    def winner(self):
        return self.__who_win