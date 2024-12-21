f=open('Reshash256.raw', 'r')
s = f.read()
f.close()
D = eval(s)
print (len(D))

for s in D:
#  print (s)
#  for q in D[s]:
#    print (s,q)
  lD=len(D[s])
  if lD>2:
    print (D[s][0][3]*lD,D[s],s,lD)