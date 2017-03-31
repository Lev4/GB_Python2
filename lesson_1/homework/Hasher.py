import hashlib

filename = 'need_hashes.csv'

def hasher(line):

   subline = line.split(';')
   if subline[1] == 'md5':
       h = hashlib.md5()     
   elif subline[1] == 'sha1':
       h = hashlib.sha1()            
   elif subline[1] == 'sha512':
       h = hashlib.sha512()       
   else:
       print("Такого алгоритма не знаем")
   h.update(subline[0].encode('koi8-r'))
   subline[2] = h.hexdigest()
   newline = []
   for el in subline:
       newline.append(el) 
   return newline

with open(filename,'r') as f:
    hstring = f.readlines()

with open(filename,'w') as f:
    for item in hstring:
        x = hasher(item)
        newlinestr = ';'.join(x)
        f.write(newlinestr + '\n')
