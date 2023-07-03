#from engine.wordhelper import wordchecker as wc
from random import choice
import json

json_lib = "5letterWords.json"
txt_lib = "sgb-words.txt"

def reload_json():
    txt_list = []
    with open(txt_lib, "r") as words:
        for word in words:
            txt_list.append(word.strip())

    with open(json_lib, "w+") as jdoc:
        for line in jdoc:
            del line
        json_list = json.dump(txt_list, jdoc)

def load_json():
    reload_json()
    try:
        with open(json_lib, "r") as jl:
            if jl is None:
                return []
            jlines = jl.read()         
            load_list = json.loads(jlines)
            return load_list
    except FileNotFoundError:
       raise Exception("file not found")


class Game:
    tries = 6
    history_list = []
    answer = ""
    guage = []


    def start(self):
        self.answer = choice(load_json())
        return {"answer": self.answer, "history": self.history_list}


    def restart(self):
        self.history_list.append(self.answer)
        self.start()


    def guager(self, c, lst):
        g_list = ["", "", "", "", ""]
        exist = []
        for num in range(5):
            if c[num] is lst[num]:
                g_list[num] = "X"
                exist.append(c[num])
            elif c[num] in lst:
                l_num = lst.count(c[num])
                if l_num == 1 and c[num] not in exist:
                    exist.append(c[num])
                    g_list[num] = "O"
                elif l_num == 1 and c[num] in exist:
                    g_list[num] = "-"
                elif l_num > 2:
                    if c[num] in exist and exist.count(c[num]) < l_num:
                        exist.append(c[num])
                        g_list[num] = "O"
                    else:
                        g_list[num] = "-"
                else:
                    g_list[num] = "O"
            else:
                g_list[num] = "-"
        self.guage = g_list
        return g_list


    def gamerun(self, uinput):
        c_list = []
        a_list = []
        for c in uinput:
            c_list.append(c)
        for a in self.answer:
            a_list.append(a)
        if uinput == self.answer:
            if len(self.history_list) != 0 and self.history_list[-1] == (self.answer):
                pass
            else:
                self.history_list.append(self.answer)
            self.guager(c_list, a_list)
            return True
        else:
            self.guager(c_list, a_list)
            return False


    def history(self, lent=0):
        temp = []
        if lent == None:
            return self.history_list
        elif int(lent) == 0:
            if len(self.history_list) < 5:
                return self.history_list
            else:
                return self.history_list
        elif len(self.history_list) < int(lent):
            return self.history_list
        else:
            for j in range(int(lent)):
                temp[j] = self.history_list[j]
                return temp

    def gameHistory(self):
        ...