l = [1, 20, 4, 50, 2, 1, 2]

print(l)#list
print(l[0])#listから[num]番目を抽出
print(l[-1])#後ろから[-num]番目
print(l[0:2])#0~2
print(l[2:])#省略
print(len(l)) #データ数
print(type(l))#class 確認

print(list('abcdefg')) #文字列置換
#無い数字は index error

n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(n[::2]) #１つ飛ばしで抽出
print(n[::-1])#逆から抽出

#listの中にlist作成
a = ['a', 'b', 'c']
n = [1, 2, 3,]
x = [a, n,]
print(x)
print(x[0])#1番目のデータが出力
print(x[1])#2番目のデータが出力

print(x[0] [1]) #1番目のデータの 2個目のデータを抽出

print("**********")

print(x[1] [2])
