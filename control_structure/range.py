
#num_list = [0,1,2,3,4,5,6,7,8,9]
#一つずつlistで打つのはだるい
#for i in num_list:
#  print(i)

"""
for i in range(10): #0~9まで 数字抽出
  print(i)
for i in range(2, 10, 3): #2から始まって10(9)まで
  print(i)
#range(2(開始値),10(参照),3(３つ飛ばし))
"""

for _ in range(10):#_を見た時点でindexはforループで使われないことがわかる ()index番号使わない
  print('hello')#10回hello
