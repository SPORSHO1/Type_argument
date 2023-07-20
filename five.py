
def sum (a,*b):
  print(a)
  print(b)
  c=a
  for i in b:
    c = c+i
    print(c)

sum(4, 5, 34, 27)
  