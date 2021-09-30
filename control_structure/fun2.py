def outer(a,b):
 
  def plus(c,d):#関数の中で冠す使うと繰り返しできる
    return c + d

  r1 = plus(a,b)
  r2 = plus(b,a)
  print(r1 + r2)

outer(1,2)

