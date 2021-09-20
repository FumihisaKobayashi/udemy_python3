def say_something(*args): #*argsで複数をまとめてタプルに入れてくれる,*で引数に追加できる
  for arg in args:
    print(arg)

say_something("Hi", "mike", "Nancey")


def say_something(word, *args):#1番目のwordがword, 残りがargsに入る
  print('word =', word)
  for arg in args:
    print(arg)

say_something("Hi", "mike", "Nancey")