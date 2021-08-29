word = 'python'

print(word[0])#文字列一番目
print(word[1])#文字列２番目
print(word[-1])#文字列最後

print('**********************')
#スライス
print(word[0:2])#0,1の文字
print(word[2:5])#2,3,4の文字
print(word[:5])#省略可

print('******************')
word = 'j' + word[1:] #置き換える 0の文字を'j'に置換
print(word)

n = len(word) #len indexを調べる、文字数
print(n)

