s = 'My name is Mike. Hi Mike'
print(s)
is_start = s.startswith('My') #myから始まってるか調べる(s.starteith)
print(is_start)

print('*******************')

print(s.find('Mike'))#'Mike'文字列
print(s.rfind('Mike'))#後ろから検索
print(s.count('Mike'))#'Mike'の個数
print(s.capitalize())#最初大文字あと小文字
print(s.title())#全ての　文字列の最初大文字
print(s.upper())#大文字
print(s.lower())#小文字
print(s.replace('Mike', 'Nancy'))#文字列置換


