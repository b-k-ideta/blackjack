import os
import time

def error_message():
    return print("無効な数値です。正しい値を入力してください。")

def title_aa():
    os.system('cls')
    print("BBBBB    LL          AAA       CCCCCC  KK  KKK ")
    print("BB   BB  LL         AA AA     CCC      KK KKK  ")
    print("BBBBB    LL        AA   AA    CC       KKKK    ")
    print("BB   BB  LL       AAAAAAAAA   CCC      KK KKK   ")
    print("BBBBB    LLLLLL  AAA     AAA   CCCCCC  KK  KKK \n")

    print("             JJ      AAA       CCCCCC  KK  KKK ")
    print("             JJ     AA AA     CCC      KK KKK  ")
    print("             JJ    AA   AA    CC       KKKK    ")
    print("         JJ  JJ   AAAAAAAAA   CCC      KK KKK   ")
    print("         JJJJJ   AAA     AAA   CCCCCC  KK  KKK \n")
    
def title_menu():
    print("\n[0]START GAME  [1]QUIT GAME")

def game_over():
    print("\nゲームを続けますか？ [0]はい [1]いいえ")

def pl_com_disp(player_cards:list,player_win:int,com_cards:list,com_win:int,total_game:int, result=False):
        os.system('cls')
        print(
            f"プレイヤー:{player_win}勝    COM:{com_win}勝    引き分け:{total_game - (player_win+com_win)}\n")
        print("プレイヤー")
        for i in range(len(player_cards)):
            print(
                f"手札{i+1}: {player_cards[i].suits}{player_cards[i].number}")
        print("\nCOM")
        if result == True:
            for i in range(len(com_cards)):
                print(f"手札{i+1}: {com_cards[i].suits}{com_cards[i].number}")
        else:
            print(f"表カード: {com_cards[0].suits}{com_cards[0].number}")
            for i in range(len(com_cards)-1):
                print("伏せカード")
    
def hit_or_stand():
    print("\nヒット[0]（カードを引く）　スタンド[1]（手持ちで勝負）")

def split_message():
    print("\nスプリットしますか？ [0]はい [1]いいえ")

def post_msg(winner, pl_total, com_total, fst=False):
    # 初回ターンブラックジャック
    if fst == True:
        print("\nBLACK JACK!")
        time.sleep(1.5)
    match winner:
        case 'Player':
            print("\nYou win!")
            print(pl_total, com_total)
        case 'COM':
            print("\nYou lose!")
            print(pl_total, com_total)
        case 'Draw':
            print("\nDraw!")
            print(pl_total, com_total)
