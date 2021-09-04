s = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(s[0]) #sの１番目抽出
s[0] = 'X'#sの1番目を'X'に置換
print(s)

s[2:5] = 'C', 'D', 'E' #まとめて置換3
print(s)

s[2:5] = [] #空に変換
print(s)
#まとめて消去する時 s[:] = [] 

n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(n)

n.append(100) #リストの最後に100を追加
print(n)

n.insert(0, 200)#0番目に200を追加
print(n)

n.pop()#最後を取り除く
print(n)

n.pop(0)#0番目を削除
print(n)

del n[0] #0番目のデータ削除 del n だとリスト自体が消える

nu = [1, 2, 2, 3]
nu.remove(2)#２を削除
print(nu)
#消せるものないときはVelue Erro起きる

