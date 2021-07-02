# GUI 계산기 만들기 (클론코딩 + 부족한 점이 있어서 스스로 보완하기)

import tkinter as tk
from typing import Collection, Text

win = tk.Tk()
win.title('계산기')

# 결과에 대한 변수 초기화
disValue = 0
operator = {'+': 1, '-': 2, '/': 3, '*': 4, 'C': 5, '=': 6}
stoValue = 0
opPre = 0
calc = ''
# 결과 넣기(문자로 변환)
str_value = tk.StringVar()  # 받아오기
str_value.set(str(disValue))  # 선언된 변수 넣어주기


def number_click(value):
    # print('숫자: ', value)
    global disValue

    disValue = (disValue*10) + value
    str_value.set(disValue)


def clear():
    global disValue, calc

    disValue = 0
    calc = ''


def operator_click(value):
    # print('명령: ', value)
    global disValue, calc

    op = operator[value]
    if(op == 5):
        clear()
        str_value.set(disValue)
    elif(op == 6):
        calc += str(disValue)
        disValue = eval(calc)

        str_value.set(disValue)
        calc = ''
    else:
        calc += (str(disValue) + value)
        disValue = 0


def button_click(value):
    # print(value)
    try:
        value = int(value)
        number_click(value)
    except:
        operator_click(value)


# textvarialbe -> set이란 명령어를 사용해 값이 자동으로 변경
# justify: 숫자를 어디에 배치 할 지 결정
dis = tk.Entry(win, textvariable=str_value,
               justify='right', bg='white', fg='red')
dis.grid(column=0, row=0, columnspan=4, ipadx=80, ipady=30)

calItem = [['1', '2', '3', '4'],
           ['5', '6', '7', '8'],
           ['9', '0', '+', '-'],
           ['/', '*', 'C', '=']]

# 아래의 코드들을 for문을 이용해 간편하게 정리
for i, items in enumerate(calItem):
    for k, item in enumerate(items):

        try:
            color = int(item)
            color = 'black'
        except:
            color = 'green'
        # bg->배경색, fg->폰트색, command->클릭시 이벤트
        bt = tk.Button(win, text=item, width=10,
                       height=5, bg=color, fg='white', command=lambda cmd=item: button_click(cmd))
        bt.grid(column=k, row=i+1)

# # btn = tk.Button(win, text='1', width=10, height=5)
# # btn.grid(column=0, row=1)
# ->
# tk.Button(win, text='1', width=10, height=5).grid(column=0, row=1)

# # btn = tk.Button(win, text='2', width=10, height=5)
# # btn.grid(column=1, row=1)
# ->
# tk.Button(win, text='2', width=10, height=5).grid(column=1, row=1)

# # btn = tk.Button(win, text='3', width=10, height=5)
# # btn.grid(column=2, row=1)
# ->
# tk.Button(win, text='3', width=10, height=5).grid(column=2, row=1)

# # btn = tk.Button(win, text='4', width=10, height=5)
# # btn.grid(column=3, row=1)
# ->
# tk.Button(win, text='4', width=10, height=5).grid(column=3, row=1)

# tk.Button(win, text='5', width=10, height=5).grid(column=0, row=2)
# tk.Button(win, text='6', width=10, height=5).grid(column=1, row=2)
# tk.Button(win, text='7', width=10, height=5).grid(column=2, row=2)
# tk.Button(win, text='8', width=10, height=5).grid(column=3, row=2)

# tk.Button(win, text='9', width=10, height=5).grid(column=0, row=3)
# tk.Button(win, text='0', width=10, height=5).grid(column=1, row=3)
# tk.Button(win, text='+', width=10, height=5).grid(column=2, row=3)
# tk.Button(win, text='-', width=10, height=5).grid(column=3, row=3)

# tk.Button(win, text='/', width=10, height=5).grid(column=0, row=4)
# tk.Button(win, text='*', width=10, height=5).grid(column=1, row=4)
# tk.Button(win, text='C', width=10, height=5).grid(column=2, row=4)
# tk.Button(win, text='=', width=10, height=5).grid(column=3, row=4)

win.mainloop()
