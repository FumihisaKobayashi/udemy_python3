#ターミナル上
'a is {}'.format('a')
#'>>>a is a'
'a is {}'.format('test')
#'>>>a is test'
'a is {}'.format(1, 2, 3)
#'>>>a is 1 2 3'

'a is {0} {1} {2}'.format(1, 2, 3) #indes指定
#'>>>a is 1 2 3'

'My name is {0} {1}'.format('Taro','Yamada')
#'My name is Yadmada Taro'

'My name is {0} {1}. Watashiha {1} {0}'.format('Taro','Yamada')
#順番入れ替え

'My name is {name} {family}. Watashiha {1} {0}'.format(name = 'Taro', family = 'Yamada')
#変数で代入

#1 数字 '1'文字列

str(1)#文字列で１
str(3.14)#もじ
str(True)#文字列
