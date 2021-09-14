#まず関数定義から実行する

"""
def say_something():#関数定義def
  print('hi')

f = say_something()#()つける必要がある

f()#functionという型なので f で出力なども見える
"""

def say_nothing():
  s = 'hi！'#sの変数宣言
  return s #返り値 sで返す
result = say_nothing() #resultで返り値を出力
print(result)


def what_is_this(color):#color 引数
  if color == 'red':#colorがredなら
    return 'tomato' #トマトを返す
  elif color == 'green':
    return 'greeeen'
  else:
    return "Idon't know"
result = what_is_this('green') #文字列を呼び出す,funcitonよ呼び出すときに
result = what_is_this('red') 
print(result) 

#関数を設定しておけばifの部分など何回も書かなくて良くなる

