print("Fibonaccinin ilk kaç sayısı yazılsın")
limit=int(input())
fib=[1,1]
for i in range(limit-2):
      a=fib[i]+fib[i+1]
      fib.append(a)
for i in fib:
      print(i)
print(" ")
#Golden Ratio
golden=[]
for i in range(len(fib)-1):
      a=fib[i+1]/fib[i]
      golden.append(a)
for i in golden:
      print(i)
