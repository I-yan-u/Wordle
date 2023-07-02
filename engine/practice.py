#from wordhelper import wordchecker as wc
#from random import choice
#import json



if __name__ == "__main__":
    h = [1, 2, 3, 4, 5]

    while len(h) > 0:
        h.pop()
    print(h)

"""    a = ['a', 'p', 'p', 'l', 'e']
    b = ['p', 'l', 'a', 'c', 'e']
    #def :

    def guager(c, lst):
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
        #self.guage = g_list
        return g_list


    e = guager(a, b)
    print(e)"""