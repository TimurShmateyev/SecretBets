# Secret bets game
import os
import time


class Bet:
    """One bet contains price and name user who has created this bet"""
    def __init__(self, price: int, user_name: str):
        self.price = price
        self.name = user_name

    def won(self):
        """Returns a winning string"""
        return f"User {self.name} with bet price {self.price} won"


class BetList:
    """List of all contained bets"""
    def __init__(self):
        self.max_bet = Bet(0, "NoName")
        self.bet_list = []

    def append(self, price: int, user_name: str):
        f"""Appends new bet into a bet list."""
        self.bet_list.append(Bet(price, user_name))

    def max(self):
        f"""Counts max bet price and return it\n
        Return: Object class: Bet"""
        for bet in self.bet_list:
            self.max_bet = bet if bet.price > self.max_bet.price else self.max_bet
        return self.max_bet


bet_list = BetList()
game_not_ended = True
while game_not_ended:
    name = input("Enter you name: ")
    bet_price = int(input("Enter bet price: "))
    bet_list.append(bet_price, name)
    is_game_ended = input('Finish the auction? Yes/No')
    if is_game_ended == "Yes":
        game_not_ended = False
    else:
        os.system('CLS')

win_bet = bet_list.max()
print(win_bet.won())
time.sleep(5)
