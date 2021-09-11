y = [1, 2, 3]
x = 1

if x in y:
  print('in') #xがyに入っていれば inと表示

if 100 not in y: #
  print('not in')


"""
a = 1
b = 2

if not a == b:
  print('not in') #推奨されていない notで否定する一手間

if not a != b: #値同士を比較
  print('not in') 

if a > b:
  print('NOT EQUAL')

"""

is_ok = True
# if is_ok == True: 一度書かれているので Trueと書く必要がない
#if is_ok != True:#否定
if not is_ok: #半手する必要ないこの号令型使う時はnotを利用する
  print('hello')

