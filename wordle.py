#!/usr/bin/python3
""" """
import cmd
from engine.wordhelper import wordchecker as wc
from engine import main
from engine.main import Game


def parse(line=""):
    return line.split()

#main.load_json()

class WordleConsole(cmd.Cmd):
    """Simple command processor example."""
    tries = 6    
    prompt = f"< Wordle -- tries: 6 > "
    intro = "Enter your 5 letter word (you have 6 tries)!"
    game = Game()
    round = game.start()
    
    def do_describe(self, line):
        print("\tWorlde to you!")
        print("\tInput your 5 letter word to guess the answer")
        print("\tYou have 6 tries to guess correctly")

    def do_history(self, line):
        if line:
            args = parse(line)
            arg = int(args[0])
            print(self.game.history(arg))
        elif not line:
            print(self.game.history())


    def do_prompt(self, num):
        self.prompt = f"< Wordle -- tries: {num} > "

    def do_intro(self):
        print("==============Restarted new game========================")
        print("Enter your 5 letter word (you have 6 tries)!")
        self.prompt = f"< Wordle -- tries: {WordleConsole.tries} > "

    def do_checktries(self):
        if WordleConsole.tries == 0:
            print("You lose; End of Game")
            print("Correct answer: {}".format(self.game.answer))
            self.do_restart("")
        else:
            self.do_prompt(self.tries)
            return WordleConsole.tries

    def default(self, line):
        self.do_run(line)

    def do_run(self, line):
        args = parse(line)
        arg = str(args[0])
        #while WordleConsole.tries != 0:
        if wc.wlen(arg) == False:
            print("Invalid lenght: must be 5 letters long")
            return

        if wc.real(arg) == False:
            print("Invalid word: word doesn't exist")
            return

        else:
            if WordleConsole.game.gamerun(arg) is False:
                print(WordleConsole.game.guage)
                print("Wrong")
                WordleConsole.tries -= 1
                self.do_checktries()

            elif WordleConsole.game.gamerun(arg) is True:
                print(WordleConsole.game.guage)
                print("Correct: {} = {}".format(arg, WordleConsole.game.answer))
                self.do_restart("")
                self.do_prompt(self.tries)


    def do_cheat(self, line):
        if len(WordleConsole.game.history_list)!= 0 and \
            WordleConsole.game.history_list[-1] == WordleConsole.game.answer:
            pass
        else:
            WordleConsole.game.history_list.append(WordleConsole.game.answer)
        print(WordleConsole.game.answer)

    def do_restart(self, line):
        print("Do you want to restart?")
        response = input("[Yes|No]\n")
        pos = ["yes", "Yes", "YES", "y"]
        neg = ["no", "No", "NO", "n"]
        if response in pos:
            WordleConsole.game.start()
            WordleConsole.tries = 6
            self.do_intro()
        else:
            return True

    def do_exit(self, line):
        return True

    def do_quit(self, line):
        return True
    
    def do_EOF(self, line):
        return True

    def postloop(self):
        print("Bye!")

if __name__ == '__main__':
    WordleConsole().cmdloop()
