import itertools
import hashlib

c='qazwsxedcrfvtgbyhnujmikolp'
fo = open("crackmd5.txt", "wb")
for i in range(1,16):      
      print i;
      f= map(''.join,itertools.product(c, repeat=i))
      for j in range (len (f)):
           fo.write(hashlib.md5(f[j]).hexdigest()+" >>> "+f[j]+"\n")
           fo.write(" ");
fo.close();
