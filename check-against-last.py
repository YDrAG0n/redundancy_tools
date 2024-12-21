f=open('Reshash256.last', 'r')
s = f.read()
f.close()
Last = eval(s)
print ('Last',len(Last))

f=open('Reshash256.current', 'r')
s = f.read()
f.close()
Current = eval(s)
print ('Current',len(Current))

f_rm = open ("del_dupes.bat","w")
f_cp = open ("restore.bat","w")

for s in Current:
  if s in Last:
    V=Current[s]
    print ("", file=f_cp)
    for v in V:
     print ("rem \"%s\"" % Last[s][0][2], file=f_rm)
     print ("del \"%s\"" % v[2], file=f_rm)
     print ("copy \"%s\" \"%s\"" %( Last[s][0][2], v[2] ), file=f_cp)

f_rm.close()
f_cp.close()
