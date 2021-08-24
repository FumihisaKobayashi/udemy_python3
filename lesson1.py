num = 1
name = 'Mike'
is_ok = True

#typeで型が分かる
print('num', type(num))
print(name, type(name))
print(is_ok, type(is_ok))

#型変換
new_num = int(name)
print(new_num, type(new_num))

#型宣言、書くこともできるが宣言は使わない
num: int = 1
name: str = "1"

#1から始めない　syntaxerrorでる