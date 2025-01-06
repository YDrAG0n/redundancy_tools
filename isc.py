import os
import hashlib as hl

Root = "."
WorkDir = '..' # where to find files
OutDir = "C:\\GIT\\priv_data\\"

List=[]
wList=[]
Dirs=[]
Hash={}
Zips=[]
NListed=0

def FlushwList():
 global wList
 f = open("Res.list", "a")
# try:
 for s in wList:
  print(s, file=f) # .encode("windows-1251")
 wList=[]
# except:
#  pass
 f.close()


def GetSha(fn, blocksize=65536):
    hash1 = hl.sha1()
    hash256 = hl.sha256()
    with open(fn, "rb") as f:
        for block in iter(lambda: f.read(blocksize), b""):
            hash1.update(block)
            hash256.update(block)
    return (hash1.hexdigest(),hash256.hexdigest())

def AppendDir(s, parent):
  global Dirs
  l=len(Dirs)
  print (parent, l, s)
  Dirs.append( (parent, l, s) )
  return l

def AppendFile( xtuple ):
     (parent, ndir, name, size, sha1, sha256) = xtuple
     List.append ( (parent, ndir, name, size, sha1, sha256) )

def ListDir(root, parent): # scan directory
  global NListed, List, Zips
  ND = AppendDir(root, parent)

  for s in os.listdir(root):
    N=root+'/'+s
    L=os.lstat(N)
    ss=s.lower()
    if L.st_mode & 0o40000: # is directory
     ListDir(N, ND) # recurrently
    elif ss.endswith('.rar') or ss.endswith('.zip') or ss.endswith('.7z') or \
           ss.endswith('.tar') or ss.endswith('.gz') or ss.endswith('.sqfs'): # processarchive
      Zips.append( (parent, ND, N, L.st_size, '', '') )
    else:
     NListed=NListed+1
     AppendFile ( (parent, ND, N, L.st_size, '', '') )


print ("Listing:")
D=os.getcwd()
DataDir=D+'/Data/'
os.chdir(WorkDir)
ListDir(Root, 0)

print ("Hashing:")
for i in range(len(List)):
 (parent, ndir, name, size, sha1, sha256) = List[i]
 if sha1=='':
   (SHA1,SHA256) = GetSha(name)
   try:
    print (SHA1, SHA256, parent, ndir, name, size)
   except:
    pass

   List[i] = (parent, ndir, name, size, SHA1, SHA256)
   if SHA256 in Hash:
     Hash[SHA256].append( (parent, ndir, name, size) )
   else:
      Hash[SHA256]= [ (parent, ndir, name, size) ]

os.chdir(D)


f = open(DataDir + "Reshash256.py", "w")
print("""# -*- coding: Windows-1251 -*-

Location=\"%s\"
Hash=""" % (D), end='')
try:
 print(Hash, file=f)
except:
 pass
f.close()

f = open(DataDir + "Reshash256.raw", "w")
try:
 print(Hash, file=f)
except:
 pass
f.close()

f = open(DataDir + "zips.list", "w")
for s in Zips:
 try:
  print(s, file=f)
 except:
  pass
f.close()

f = open(DataDir + "Res.dirs", "w")
try:
 for s in Dirs:
  print(s, file=f)
except:
 pass
f.close()

f = open(DataDir + "Res.hash256.utf8", "w")
try:
 print(str(Hash).encode("utf-8"), file=f)
except:
 pass
f.close()


