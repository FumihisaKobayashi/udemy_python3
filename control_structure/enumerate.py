i = 0
for fruit in ['apple', 'banana', 'orange']:
  print(i, fruit)
  i += 1
#index番号とstr

for i, fruit in enumerate(['apple', 'banana', 'orange']):#始めのループの時にiの番号に入れてくれる(上と同じ)
  print(i, fruit)