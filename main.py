from random import randint
from os import system, name
import re
import json

class Game:
    def __init__(self):
        self.secret = ""
        self.running = True
        self.guessed_chars = []
        self.found_chars = []
        self.found_count = 0
        self.missed = 0
        self.missed_chars = []

    def check_win(self):
        if self.found_count == len(self.found_chars):
            print("YOU WIN!")
            self.running = False
            print("The word was: ", end="")
            print(*self.secret, sep="")
        elif self.missed > 5:
            print("YOU LOSE!")
            self.running = False
            print("The word was: ", end="")
            print(*self.secret, sep="")

    def clear_screen(self):
        if name == 'nt':
            _ = system('cls')
        else:
            _ = system('clear')

    def guess(self, char):
        if char == "":
            return

        g = re.compile(char)

        if(g.search(self.secret)):
            it = g.finditer(self.secret)
            for match in it:
                self.found_chars[match.span()[0]] = char
                self.found_count += 1
        else:
            self.missed += 1
            self.missed_chars.append(char)

    def init_secret(self):
        f = open('words.json')
        l = json.load(f)
        self.secret = l['data'][randint(0,2465)]

        for x in range(0, len(self.secret)):
            self.found_chars.append("_")

    def reset_guessed(self):
        self.guessed_chars = []

def main():
    game = Game()
    game.init_secret()
    game.clear_screen()

    while game.running:
        if game.missed > 0:
            print("Missed Characters: ", end="")
            for x in range(0, len(game.missed_chars)):
                if x == 0:
                    print(game.missed_chars[x], end="")
                else:
                    print(", " + game.missed_chars[x], end="")
            print(" ")

        print(*game.found_chars, sep=" ")
        player_guess = input("Guess a letter: ")
        game.clear_screen()
        game.guess(player_guess)
        game.check_win()

if __name__ == "__main__":
    main()
