def fact(n):
   b=1
   if (n==0):
      print(1)
   elif(n<0):
      print("Enter valid no.")
   else:
      for i in range(n-1):
        b=b*n
        n=n-1
      print(b)
          


n = 6
fact(n)

n = 0
fact(n)