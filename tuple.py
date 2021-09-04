t = (1, 2, 3, 4, 1, 2)
print(type(t))#()tupleは[]リストと違って後から数字をアサインできない

#printt[0] = 10  error

#数字のアサイン以外できる
print(t[-1]) 
print(t[2:5])

print(t.index(1)) #index1どこか
print(t.index(1, 1))
print(t.count(1)) #1何個から

#help(tuple) 読み込み専用で使ことが多い
print("*******")
t = ([1, 2, 3], [4, 5, 6])
print(t)

print(t[0][0]) #t0番目のリストの0番目表示
#リスト内のアサインはできる
t[0][0] = 100 
print(t)

t = 1, 2, 3, 4 #（）なくても,を付けた段階でtupleになる
t = ()#class tuple
t = (1)#class int になるので注意

#tuple同士は編集可能
new_tuple = (1, 2, 3) + (4, 5, 6)
print (new_tuple)

#tupleは, つける

