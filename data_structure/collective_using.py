
#共通を見つけ出すときに使える

my_friends = {'A', 'B', 'C'}
a_friends = {'A', 'B', 'E', 'G'}
print(my_friends & a_friends)
#共通を出す

f = ['apple', 'banana', 'apple', 'banana']
kind = set(f)#重複を削除して　setで型を集合からリストに型を変える
print(kind)
#アプリの追加していくときにリストだが、ユニークは集合使って追加、実行する
