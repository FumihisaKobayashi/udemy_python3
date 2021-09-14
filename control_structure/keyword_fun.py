""""
def menu(entree, drink, dessert):#引数の指定複数できる(位置引数、)
  print(entree)
  print(drink)
  print(dessert)

#keywordを指定することもできる。
menu(entree='beef',dessert= 'ice',drink= 'beer')#値キーワード引数
#1引数とキーワードの順番に注意

"""

def menu(entree='beef', drink='wine', dessert='ice'):#デフォルトで引数入力
  print('entree =', entree)
  print('drink =', drink)
  print('dessert =', dessert)
menu()#引数を選択しないとデフォルト値が入力される
menu('chiken', drink = 'beer')#値を入力されると上書きされる
#キーワード引数も混ぜながら使用する