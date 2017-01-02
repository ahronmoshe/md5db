import itertools
import hashlib

c='qaz'
fo = open("crackmd5_of_p3.txt","w+",encoding='utf-8')

for i in range(1,4):
     print (i);
     f= list(map(''.join,itertools.product(c, repeat=3)))
     for j in range(len (f)):
          fo.write(hashlib.md5(str(f[j]).encode('utf-8')).hexdigest()+" "+f[j]+"\n")
          fo.write(" ");

print (len (f))
fo.close();
