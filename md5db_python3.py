import itertools
import hashlib

c='qazwsxedcrfvtgbyhnujmikolp'
fo = open("crackmd5_of_p3.txt","w+")

for i in range(1,6):
     print ("strat with "+str(i)+" combination");
     for  j in list(map(''.join,itertools.product(c, repeat=i))):
          fo.write(hashlib.md5(j.encode('utf-8')).hexdigest()+" "+j+"\n")
          fo.write(" ");
fo.close();
