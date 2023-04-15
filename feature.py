# this is a function

def main(n,m):
  if n > m:
    return n , " is greater"
  elif m > n:
    return m , " is greater"
  else:
    return "these values are equal!"

x = eval(input("Enter the first value: "))
y = eval(input("Enter the first value: "))

print(main(x,y))