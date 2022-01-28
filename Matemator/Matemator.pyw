
'''=============================== УРОВНИ ==============================='''

"""
    global mn
    global mx
    global count
    global ran
    global lst
    count = 4
    a = int(a)
"""

'''================='''

def Ruletka625(a):
    global mn
    global mx
    global count
    count = 4
    mn = -100000
    mx = 100000
    a = int(a)
    return randint(0, 1)

'''================='''

def Counofdivs(a):
    global mn
    global mx
    global count
    count = 4
    a = int(a)
    mn = 0
    mx = 64
    ans = 1
    for i in range(1, a // 2 + 1):
        if a % i == 0:
            ans += 1
    return ans

'''================='''    
    
def MultiPlus(a):
    global mn
    global mx
    global count
    global lst
    count = 3
    a = int(a)
    mn = -25
    mx = 25
    return a * a + a

'''================='''
    
def Binar(a):
    global mn
    global mx
    global count
    global lst
    count = 2
    a = int(a)
    mn = -128
    mx = 128
    sign = False
    if a < 0:
        sign = True
        
    if a != 0:
        i = 0
        if sign:
            a = -a
        
        while 2**(i + 1) < a:
            i += 1
        if 2**(i + 1) == a:
                i += 1

        a -= 2**i
        ans = '1'
        i -= 1     
        
        while i >= 0:
            if a >= 2**i:
                a -= 2**i
                i -= 1
                ans += '1'
            else:
                i -= 1
                ans += '0'
                
        ans = int(ans)
        if sign:
            ans = -ans
    else:
        ans = 0

    return ans
            
'''================='''

def Doubler(a):
    global mn
    global mx
    global count
    count = 4
    mn = 0
    mx = 100
    a = int(a)
    return a * 2

'''================='''

def OneHungredTwentyFive(a):
    global mn
    global mx
    global count
    count = 2
    mn = -100
    mx = 550
    a = int(a)
    return a + 125

'''================='''

def DivFour(a):
    global mn
    global mx
    global count
    count = 4
    mn = 0
    mx = 60
    a = int(a)
    return a // 4

'''================='''

def Revolution(a):
    global mn
    global mx
    global count
    count = 4
    mn = -10000
    mx = 10000
    a = int(a)
    return -a

'''================='''

def GIANT(a):
    global mn
    global mx
    global count
    count = 4
    mn = -10000
    mx = 10000
    a = int(a)
    return a * 1000000000000000000000000000000000000000000

'''================='''

def PlusMinus(a):
    global mn
    global mx
    global count
    global ran
    global lst
    count = 4

    a = int(a)
    if c == -1:
        ran = False
        
        for i in range(count):
            lst[i] = 0

        lst[randint(0, 3)] = randrange(10, 100, 10)

        while True:
            w = randint(0, 3)
            if lst[w] == 0:
                lst[w] = randrange(1, 100, 2)
                
                break
            
        while True:
            w = randint(0, 3)
            if lst[w] == 0:
                lst[w] = randrange(0, 100, 2)
                
                break
    
        for i in range(count):
            if lst[i] == 0:
                lst[i] = randint(0, 100)
                
    
    if a % 10 == 0:
        return a / 10
    elif a % 2 == 0:
        return a / 2
    else:
        return a + 1
            
'''================='''

def PrimeNumbers(a):
    global mn
    global mx
    global count
    global ran
    global lst
    count = 4
    prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

    a = int(a)
    x = True
    if a > 1:
        for i in range(2, (a // 2) + 1):
            if a % i == 0:
                x = False
                break
    else:
        x = False

    if c == -1:
        ran = False
        
        for i in range(count):
            lst[i] = 0

        lst[randint(0, 3)] = choice(prime)

        for i in range(count):
            if lst[i] == 0:
                lst[i] = randint(0, 100)

    
    if x:
        return 1
    else:
        return 0

'''================='''

def Fibonaccinums(a):
    global mn
    global mx
    global count
    global lst
    count = 3
    global fib
    a = int(a)
    mn = 1
    mx = 12
    if a > 0 and a < 202:
        return fib[a - 1]
    elif a < 1:
        return -1
    else:
        return 'Много'
    
    
"""
    global mn
    global mx
    global count
    global ran
    global lst
    count = 4
    a = int(a)
"""

'''================================ ИМПОРТЫ ================================'''

from random import *
import sys
from tkinter import *
from tkinter.ttk import Combobox
from tkinter.ttk import Checkbutton
from tkinter.ttk import Radiobutton
from tkinter import scrolledtext

'''================================ ФУНКЦИИ ================================'''
        
def clearall():
    sth = root.pack_slaves()
    for i in sth:
        i.destroy()

def click1():
    x = combo.get()
    try:
        if (int(x) > 0) and (int(x) <= len(combo['values'])):
            clearall()
            level(int(x))
        else:
            combo.current(len(combo['values']) - 1)
    except:
        combo.current(0)

def rulesopen():
    clearall()

    meru = Frame(bg = clrbg['text'])
    menubtn = Button(meru,
                     width = 7,
                     text = 'Меню',
                     bg = clrbg['menubtn'],
                     fg = clrfg['menubtn'],
                     command = gotomenu)

    meru.pack(fill = X)
    menubtn.pack(anchor = NW, side = LEFT)

    rulesword = Label(meru,
                      text = 'Правила     ',
                      fg = clrfg['text'],
                      bg = clrbg['text'],
                      font = ('Arial Bold', 30))
    rulesword.pack()
    rulestxt = Label(root,
                     text = 'Цель игры — разгадать алгоритм, заложенный в уровень.\nДля этого вводите целые числа в нижнюю панель, программа\nвыполнит ряд операций, используя это число, и выдаст\nрезультат в верхней панели. Путём ввода разных чисел\nвам предстоит разузнать алгоритм получения ответа.\nПосле, нажав на кнопку "Готов", вы меняетесь ролями\nс программой. Она задаёт вам числа, а вы пишете ответ,\nиспользуя алгоритм уровня. Это повторяется несколько раз,\nи, если вы верно отвечаете на все числа, то уровень пройден.',
                     fg = clrfg['text'],
                     bg = clrbg['text'],
                     font = ('Arial Bold', 10))
    rulestxt.pack(fill = Y)
    exampleword = Label(root,
                        text = 'Пример',
                        fg = clrfg['text'],
                        bg = clrbg['text'],
                        font = ('Arial Bold', 15))
    exampleword.pack(fill = Y)
    exampletxt = Label(root,
                       text = '1) Вы вводите число 10. После выполнения операций выводится 12.\n2) Вы вводите -14, выводится -17.\n3) Вводите 0, выводится 2.\nНа основании этих данных, можно предположить алгоритм:\n"Если число положительное или 0, то к нему добавляется 2,\nа если отрицательное, то вычитается 3"',
                       fg = clrfg['text'],
                       bg = clrbg['text'],
                       font = ('Arial Bold', 10))
    exampletxt.pack(fill = Y)
    
def startReturn(event):
    click1()

def gameover():
    endtxt = Label(root,
                   text = 'Больше уровней\nв новых версиях',
                   fg = clrfg['text'],
                   bg = clrbg['text'],
                   font = ('Arial Bold', 30))
    endtxt.pack(pady = 30)

    menubtn = Button(root,
                     text = 'Меню',
                     font = ('Arial Bold', 45),
                     bg = clrbg['menubtn'],
                     fg = clrfg['menubtn'],
                     command = gotomenu)

    my_frame = Frame()
    
    myname = Label(my_frame,
                   text = 'Made by Tarabukin Mark',
                   bg = clrbg['text'],
                   fg = clrfg['text'],
                   font = ('Courier New', 12))
    
    menubtn.pack(pady = 15)
    my_frame.pack()
    myname.pack(anchor = SW)



    
def gotomenu():
        clearall()
        menu()

def restart():
        clearall()
        global lvl
        level(lvl)

def whiteth():
    global THEME
    global MAINTH
    THEME = 1
    MAINTH = 1
    set_theme()

def blackth():
    global THEME
    global MAINTH
    THEME = 2
    MAINTH = 2
    set_theme()

def colorbtns():
    global THEME
    global colored_buttons
    if colored_buttons:
        THEME = MAINTH
        colored_buttons = False
    else:
        THEME = 3
    set_theme()
    
def set_theme():
    global THEME
    changetheme(THEME)
    clearall()
    menu()

def changetheme(a):
    global colored_buttons
    if a == 1:
            clrbg['startbtn'] = 'white'
            clrfg['startbtn'] = 'black'
            
            clrfg['text'] = 'black'
            clrbg['text'] = 'white'
            
            clrbg['colored'] = 'white'
            clrfg['colored'] = 'black'

            clrbg['root'] = 'white'

            clrbg['menubtn'] = 'white'
            clrfg['menubtn'] = 'black'

            clrbg['vvodbtn'] = 'white'
            clrfg['vvodbtn'] = 'black'

            clrbg['readybtn'] = 'white'
            clrfg['readybtn'] = 'black'

            clrbg['readybtn1'] = 'white'
            clrfg['readybtn1'] = 'black'

            clrbg['nextlvlbtn'] = 'white'
            clrfg['nextlvlbtn'] = 'black'

            clrbg['restartbtn'] = 'white'
            clrfg['restartbtn'] = 'black'

            clrbg['combobox'] = 'white'
            clrfg['combobox'] = 'gray50'

            clrbg['textbar'] = 'white'
            clrfg['textbar'] = 'black'
            clrbg['rulesbtn'] = 'white'
            clrfg['rulesbtn'] = 'black'
            
    elif a == 2:
            clrbg['startbtn'] = 'gray22'
            clrfg['startbtn'] = 'white'

            clrbg['text'] = 'gray22'
            clrfg['text'] = 'white'
            
            clrbg['colored'] = 'gray22'
            clrfg['colored'] = 'white'

            clrbg['root'] = 'gray22'

            clrbg['menubtn'] = 'gray22'
            clrfg['menubtn'] = 'white'

            clrbg['vvodbtn'] = 'gray22'
            clrfg['vvodbtn'] = 'white'

            clrbg['readybtn'] = 'gray22'
            clrfg['readybtn'] = 'white'

            clrbg['readybtn1'] = 'gray22'
            clrfg['readybtn1'] = 'white'

            clrbg['nextlvlbtn'] = 'gray22'
            clrfg['nextlvlbtn'] = 'white'

            clrbg['restartbtn'] = 'gray22'
            clrfg['restartbtn'] = 'white'

            clrbg['combobox'] = 'gray22'
            clrfg['combobox'] = 'white'

            clrbg['textbar'] = 'gray30'
            clrfg['textbar'] = 'white'
            clrbg['rulesbtn'] = 'gray22'
            clrfg['rulesbtn'] = 'white'
            
    elif a == 3:
            colored_buttons = True
            
            clrbg['startbtn'] = 'royal blue'
            clrfg['startbtn'] = 'snow'
            
            clrbg['colored'] = 'yellow'
            clrfg['colored'] = 'black'

            #clrbg['root'] = 'gray22'

            clrbg['menubtn'] = 'royal blue'
            clrfg['menubtn'] = 'snow'

            #clrbg['vvodbtn'] = 'orange'
            #clrfg['vvodbtn'] = 'snow'

            clrbg['readybtn'] = 'red'
            clrfg['readybtn'] = 'snow'
    
            clrbg['nextlvlbtn'] = 'lime green' 
            clrfg['nextlvlbtn'] = clrfg['text']

            clrbg['restartbtn'] = 'royal blue'
            clrfg['restartbtn'] = 'snow'

            clrbg['readybtn1'] = 'gray13'
            clrfg['readybtn1'] = 'gold'

            clrbg['rulesbtn'] = 'orange'
            clrfg['rulesbtn'] = 'black'

            
    
    
def menu():

    root["bg"] = clrbg['root']
    root.option_add("*TCombobox*Listbox*Background", clrbg['combobox'])
    root.option_add("*TCombobox*Listbox*Foreground", clrfg['combobox'])
    root.option_add("*TScrolledText*Listbox*Background", clrbg['combobox'])
    root.option_add("*TScrolledText*Listbox*Foreground", clrfg['combobox'])
    global lbl_1
    global lbl_2

    rume = Frame(bg = clrbg['text'])
    
    rules = Button(rume,
                   text = 'Правила',
                   bg = clrbg['rulesbtn'],
                   fg = clrfg['rulesbtn'],
                   command = rulesopen)
                   
    
    lbl_1 = Label(rume,
                  text = 'МЕНЮ   ',
                  fg = clrfg['text'],
                  bg = clrbg['text'],
                  font = ('Arial Bold', 50))
    rume.pack(fill = X)
    rules.pack(anchor = NW, side = LEFT)
    lbl_1.pack(pady = 10)

    lbl_2 = Label(root,
                  text = 'Выберите уровень',
                  fg = clrfg['text'],
                  bg = clrbg['text'],
                  font = ('Arial Bold', 15))
    lbl_2.pack()

    global combo
    
    combo = Combobox(root,
                     font = ('Arial Bold', 10))
    combo.pack(pady = 15)
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    combo['values'] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    combo.current(0)
    
    start_but = Button(root,
                 text = 'Старт',
                 font = ('Arial Bold', 35),
                 bg = clrbg['startbtn'],
                 fg = clrfg['startbtn'],
                 command = click1)
    start_but.pack()

    root.bind('<Return>', startReturn)
    
    thfr = Frame(bg = clrbg['text'])

    thlbl = Label(thfr,
                  text = 'Тема:',
                  fg = clrfg['text'],
                  bg = clrbg['text'],
                  font = ('Arial Bold', 15))

    white_th = Button(thfr,
                      text = 'Белая',
                      width = 7,
                      bg = 'white',
                      fg = 'black',
                      command = whiteth)  

    black_th = Button(thfr,
                      text = 'Тёмная',
                      width = 7,
                      bg = 'gray22',
                      fg = 'white',
                      command = blackth)  

    colored_th = Button(thfr,
                        text = 'Цветные кнопки',
                        width = 15,
                        bg = clrbg['colored'],
                        fg = clrfg['colored'],
                        command = colorbtns)
    
    thfr.pack(pady = 20)
    thlbl.pack(side = LEFT, padx = 10)
    white_th.pack(side = LEFT, padx = 7)
    black_th.pack(side = LEFT, padx = 7)
    colored_th.pack(side = RIGHT, padx = 30)
    thlbl.pack(side = LEFT, padx = 10)

                                  
    combo.focus()
 #
 #
 #
 #
 #
    root.mainloop()

    

def func(num, a):
    return eval(levels[num - 1] + '(a)')




    
def level(a):

    def gotomenuEscape(event):
        gotomenu()
    
    def nextlvl():
        clearall()
        if lvl <= len(levels):
            level(lvl)
        else:
            gameover()

    def restartReturn(event):
        restart()
    
    

    def readyR(event):
        click_ready()
    
    def click_ready():
        global vvodbtn
        
        vvodbtn = False
        sct_2.configure(state = 'normal')
        sct_main.delete(1.0, END)
        sct_2.delete(1.0, END)
        txt_in.delete(0, END)
        sct_2.insert(INSERT, '\n\n\nВведите ответ:')
        sct_2.configure(state = 'disabled')
        check_prepare()
        check(a)

    

    def vvodReturn(event):
        vvod()
        
    def nextlvlReturn(event):
        nextlvl()
        
    def vvod():
        try:
            global vvodbtn
            sct_2.configure(state =  'normal')
            sct_main.configure(state = 'normal')
            if vvodbtn:
                sct_2.delete(1.0, END)
                sct_2.insert(INSERT, '            Перейти к проверке (r) >>\n\n\nВведите любое целое число:')
                sct_main.delete(1.0, END)
                sct_main.insert(INSERT, str(func(a, txt_in.get())))
                txt_in.delete(0, END)
            else:
                global c

                sct_main.delete(1.0, END)
                sct_main.insert(INSERT, q)
                sct_2.delete(1.0, END)
                
                
                if int(txt_in.get()) == func(a, q):
                    sct_2.insert(INSERT, 'Верно\n\n\nВведите ответ:')
                    txt_in.delete(0, END)
                    txt_in.focus()
                    c += 1
                    check(a)
#                    
                elif int(txt_in.get()) == 8520:
                    c = count
                    txt_in.delete(0, END)
                    check(a)
#                    
                else:
                    k = 0
                    for i in root.pack_slaves():
                        if k == 4:
                            i.destroy()
                        k += 1
      
                    restartbtn = Button(root,
                                        text = 'Рестарт',
                                        bg = clrbg['restartbtn'],
                                        fg = clrfg['restartbtn'],
                                        font = ('Arial Bold', 35),
                                        command = restart)

                    restartbtn.pack(expand = 1, fill = BOTH)

                    txt_in.unbind('<Return>')
                    root.bind('<Return>', restartReturn)
                    
                    sct_2.insert(INSERT, 'Неверно\n\n\nПопробовать ещё раз?')
                    
                sct_main.configure(state =  'disabled')
                sct_2.configure(state =  'disabled')
                
        except ValueError:
            sct_2.delete(1.0, END)
            sct_2.insert(INSERT, 'Вводи cнова, вводить можно\nтолько целые числа и знак\nминус')
            sct_2.configure(state =  'disabled')
            sct_main.configure(state =  'disabled')

            
    def outmas(c):
            global q
            global mn
            global mx
            if ran:
                q = randint(mn, mx)
        
            else:
                q = lst[c]

            sct_main.configure(state =  'normal')
            sct_main.delete(1.0, END)
            sct_main.insert(INSERT, q)
            sct_main.configure(state =  'disabled')
            

            
    def check_prepare():
        global ran
        global c
        c = -1
        x = func(a, 1)
        c = 0

    def check(a):
        global c
        global q        
        global lvl
                
        if c == count:
            
            sct_2.configure(state =  'normal')

            c = 0
            lvl += 1    
            
            k = 0
            for i in root.pack_slaves():
                if k == 4:
                    i.destroy()
                k += 1
      
            nextlvlbtn = Button(root,
                                text = 'Следующий уровень',
                                font = ('Arial Bold', 28),
                                bg = clrbg['nextlvlbtn'],
                                fg = clrfg['nextlvlbtn'],
                                command = nextlvl)
            
            nextlvlbtn.pack(expand = 1, fill = BOTH)
            
            txt_in.unbind('<Return>')
            
            txt_in.bind('<Return>', nextlvlReturn)
            
            but_ready.configure(fg = clrfg['readybtn1'],
                                bg = clrbg['readybtn1'])
            
            
            sct_2.delete(1.0, END)
            sct_2.insert(INSERT, 'Уровень пройден!!!\n\n\nВыберете дальнешее действие:')
            
            sct_2.configure(state =  'disabled')
            
        else:
            outmas(c)

                   
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
    root.unbind('<Return>')       
    global vvodbtn
    vvodbtn = True
    mn = 0
    mx = 100
    global c
    c = -2
    global lst
    lst = list(range(10))
    global ran
    ran = True
    global lvl
    lvl = a
    
    x = func(a, 1)
    lst = list(range(count))

    fr_1 = Frame(bg = clrbg['text'])
    
    lbl_levelnum = Label(fr_1,
                         text = (' УРОВЕНЬ ' + str(a) + '      '),
                         fg = clrfg['text'],
                         bg = clrbg['text'],
                         font = ('Arial Bold', 20))

    menubtn = Button(fr_1,
                     text = 'Меню',
                     font = ('Arial Bold', 10),
                     bg = clrbg['menubtn'],
                     fg = clrfg['menubtn'],
                     command = gotomenu)
    
    fr_1.pack(expand = 1, fill = X)
    lbl_levelnum.pack(side = RIGHT, expand = 1, fill = X)
    menubtn.pack(side = LEFT, anchor = NE)
    
    root.bind('<Escape>', gotomenuEscape)
   

    global sct_main
    sct_main = scrolledtext.ScrolledText(root,
                                         font = ('Arial Bold', 35),
                                         bg = clrbg['textbar'],
                                         fg = clrfg['textbar'],
                                         height = 2)
    sct_main.pack(expand = 1, fill = BOTH)

    fr_2 = Frame()
    
    global sct_2
    sct_2 = scrolledtext.ScrolledText(fr_2,
                                      width = 29,
                                      font = ('Arial Bold', 13),
                                      bg = clrbg['textbar'],
                                      fg = clrfg['textbar'],
                                      height = 4)
    

    but_ready = Button(fr_2,
                       text = 'Готов',
                       font = ('Arial Bold', 30),
                       bg = clrbg['readybtn'],
                       fg = clrfg['readybtn'],
                       command = click_ready)

    root.bind('r', readyR)
    
    fr_2.pack()
    sct_2.pack(side = LEFT, expand = 1, fill = BOTH)
    but_ready.pack(side = RIGHT, expand = 1, fill = BOTH)

    
    
    
    global txt_1
    txt_in = Entry(root,
                   bg = clrbg['textbar'],
                   fg = clrfg['textbar'],
                   font = ('Arial Bold', 28))
    txt_in.pack(expand = 1, fill = BOTH)

    vvodbtn = Button(root,
                     text = 'Ввод',
                     bg = clrbg['vvodbtn'],
                     fg = clrfg['vvodbtn'],
                     font = ('Arial Bold', 30),
                     command = vvod)
    
    vvodbtn.pack(expand = 1, fill = BOTH)

    txt_in.bind('<Return>', vvodReturn)
    
    

    

        
    sct_2.insert(INSERT, '            Перейти к проверке (r) >>\n\n\nВведите любое число:')
    sct_2.configure(state =  'disabled')
    sct_main.configure(state =  'disabled')
    txt_in.focus()        
    root.mainloop()

    



        

'''============================== СПИСКИ =============================='''

fib = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817, 39088169, 63245986, 102334155, 165580141, 267914296, 433494437, 701408733, 1134903170, 1836311903, 2971215073, 4807526976, 7778742049, 12586269025, 20365011074, 32951280099, 53316291173, 86267571272, 139583862445, 225851433717, 365435296162, 591286729879, 956722026041, 1548008755920, 2504730781961, 4052739537881, 6557470319842, 10610209857723, 17167680177565, 27777890035288, 44945570212853, 72723460248141, 117669030460994, 190392490709135, 308061521170129, 498454011879264, 806515533049393, 1304969544928657, 2111485077978050, 3416454622906707, 5527939700884757, 8944394323791464, 14472334024676221, 23416728348467685, 37889062373143906, 61305790721611591, 99194853094755497, 160500643816367088, 259695496911122585, 420196140727489673, 679891637638612258, 1100087778366101931, 1779979416004714189, 2880067194370816120, 4660046610375530309, 7540113804746346429, 12200160415121876738, 19740274219868223167, 31940434634990099905, 51680708854858323072, 83621143489848422977, 135301852344706746049, 218922995834555169026, 354224848179261915075, 573147844013817084101, 927372692193078999176, 1500520536206896083277, 2427893228399975082453, 3928413764606871165730, 6356306993006846248183, 10284720757613717413913, 16641027750620563662096, 26925748508234281076009, 43566776258854844738105, 70492524767089125814114, 114059301025943970552219, 184551825793033096366333, 298611126818977066918552, 483162952612010163284885, 781774079430987230203437, 1264937032042997393488322, 2046711111473984623691759, 3311648143516982017180081, 5358359254990966640871840, 8670007398507948658051921, 14028366653498915298923761, 22698374052006863956975682, 36726740705505779255899443, 59425114757512643212875125, 96151855463018422468774568, 155576970220531065681649693, 251728825683549488150424261, 407305795904080553832073954, 659034621587630041982498215, 1066340417491710595814572169, 1725375039079340637797070384, 2791715456571051233611642553, 4517090495650391871408712937, 7308805952221443105020355490, 11825896447871834976429068427, 19134702400093278081449423917, 30960598847965113057878492344, 50095301248058391139327916261, 81055900096023504197206408605, 131151201344081895336534324866, 212207101440105399533740733471, 343358302784187294870275058337, 555565404224292694404015791808, 898923707008479989274290850145, 1454489111232772683678306641953, 2353412818241252672952597492098, 3807901929474025356630904134051, 6161314747715278029583501626149, 9969216677189303386214405760200, 16130531424904581415797907386349, 26099748102093884802012313146549, 42230279526998466217810220532898, 68330027629092351019822533679447, 110560307156090817237632754212345, 178890334785183168257455287891792, 289450641941273985495088042104137, 468340976726457153752543329995929, 757791618667731139247631372100066, 1226132595394188293000174702095995, 1983924214061919432247806074196061, 3210056809456107725247980776292056, 5193981023518027157495786850488117, 8404037832974134882743767626780173, 13598018856492162040239554477268290, 22002056689466296922983322104048463, 35600075545958458963222876581316753, 57602132235424755886206198685365216, 93202207781383214849429075266681969, 150804340016807970735635273952047185, 244006547798191185585064349218729154, 394810887814999156320699623170776339, 638817435613190341905763972389505493, 1033628323428189498226463595560281832, 1672445759041379840132227567949787325, 2706074082469569338358691163510069157, 4378519841510949178490918731459856482, 7084593923980518516849609894969925639, 11463113765491467695340528626429782121, 18547707689471986212190138521399707760, 30010821454963453907530667147829489881, 48558529144435440119720805669229197641, 78569350599398894027251472817058687522, 127127879743834334146972278486287885163, 205697230343233228174223751303346572685, 332825110087067562321196029789634457848, 538522340430300790495419781092981030533, 871347450517368352816615810882615488381, 1409869790947669143312035591975596518914, 2281217241465037496128651402858212007295, 3691087032412706639440686994833808526209, 5972304273877744135569338397692020533504, 9663391306290450775010025392525829059713, 15635695580168194910579363790217849593217, 25299086886458645685589389182743678652930, 40934782466626840596168752972961528246147, 66233869353085486281758142155705206899077, 107168651819712326877926895128666735145224, 173402521172797813159685037284371942044301, 280571172992510140037611932413038677189525, 453973694165307953197296969697410619233826]

'''============================ ЦВЕТА У ТЕМ ============================'''

global clrbg
global clrfg

clrbg = {'startbtn': 'white',
         
         'text': 'white',
         'root': 'white',
         'menubtn': 'white',
         'readybtn': 'white',
         'vvodbtn': 'white',
         'restartbtn': 'white',
         'nextlvlbtn': 'white',
         'readybtn1': 'white',
         'combobox': 'white',
         'textbar': 'white',
         'colored': 'white',
         'rulesbtn': 'white'
         }

clrfg = {'startbtn': 'black',
         'text': 'black',
         
         'menubtn': 'black',
         'readybtn': 'black',
         'vvodbtn': 'black',
         'restartbtn': 'black',
         'nextlvlbtn': 'black',
         'readybtn1': 'black',
         'combobox': 'gray50',
         'textbar': 'black',
         'colored': 'black',
         'rulesbtn': 'black'
         }
         
'''========================= НАЗВАНИЯ УРОВНЕЙ ========================='''

levels = [
    'Doubler',
    'OneHungredTwentyFive',
    'DivFour',
    'Revolution',
    'GIANT',
    'PlusMinus',
    'PrimeNumbers',
    'Fibonaccinums',
    'Binar',
    'MultiPlus',
    'Counofdivs',
    'Ruletka625'
    ]

'''============================== НАЧАЛО =============================='''

THEME = 1
MAINTH = 1
colored_buttons = False
root = Tk()
root.iconbitmap(r'images\Matemator.ico')
root.title('Математор')
root.geometry('420x340+550+200')
root.resizable(width=False, height=False)
menu()
    
root.mainloop()
