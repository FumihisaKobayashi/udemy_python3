days = ['Mon', 'Tue', 'Mad']
fruit = ['apple','banana','orange']
drinks = ['coffee','tea', 'beer']

"""
for i in range(len(days)):#days 曜日
  print(days[i], fruit[i], drinks[i])
"""

for days, fruit, drinks in zip(days, fruit, drinks):#一番始めのものをピックアップして変数に入れる
  print(days, fruit, drinks)
#indexをいちいち指定しなくて良くなる
