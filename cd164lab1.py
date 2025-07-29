n=('vishnu','akhil','nandu','bheeshma')
new=('nikhil','maggi')
a=int(input('enter a position to insert:'))
n1=tuple()
n1=n[:a-1]+new
n1=n1+n[a-1:]
print(n1)

