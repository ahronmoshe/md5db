import itertools
import hashlib

c='qaz'
fo = open("crackmd5_of_p3.txt","w+")

for i in range(1,4):
     print ("strat with "+str(i)+" combination");
     f= list(map(''.join,itertools.product(c, repeat=3)))
     for j in range(len (f)):
          fo.write(hashlib.md5(str(f[j]).encode('utf-8')).hexdigest()+" "+f[j]+"\n")
          fo.write(" ");
fo.close();

