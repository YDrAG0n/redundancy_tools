from Reshash256 import Hash
#from Reshash256U import HashU


HashU=Hash
print ("Working:")

BZ={}
BZList=['','']

def LoadBase(fn):
   f = open(fn)
   f.close()

def LoadBases():
  for fn in BZList:
    LoadBase(fn)

#for i in Hash:
#  if len(Hash[i])>1:
#    for s in Hash[i]:
#      print (s)
#    print ('-------')

for i in HashU:
   if i in Hash:
    (dir1U, dir2U, nameU, sizeU)=HashU[i][0]
    (dir1, dir2, name, size)=Hash[i][0]
    print ("Exists, Del, %s, %s, %s" %(i, nameU, name))