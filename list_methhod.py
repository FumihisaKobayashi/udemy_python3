r = [1, 2, 3, 4, 5, 1, 2, 3]
print(r.index(3))#3の場所
print(r.index(3, 3))#3から始める

print(r.count(3))#3の個数計算

#もし５がrのリストに入っていればアクション
if 5 in r:
    print('exist')
print("**********")

r.sort()#rをsort
print(r)
r.sort(reverse=True) #逆から出力
print(r)
r.reverse()#元に戻す

s = 'My name is Mike.'
to_split = s.split(' ') #' '(スペースで区切ってリスト化する)
print(to_split)

x = ' '.join(to_split) #listを受け付ける
print(x)


# print(help(list(x))) help表示 