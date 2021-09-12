is_empty = None
#print(help(is_empty))
#変数は宣言するが何も入れないときに使用

if is_empty is not None:
  print('None!!')

print(1 == True)#1とTrueは真である
print(1 is True)#オブジェクトが同じであれば真である
print(True is True)#isはNoneなどのオブジェクトで使用、変数の値はどうかは＝＝統合を使う

a = 1 #==
a = None #is
