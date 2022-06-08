import os

cookie=input('MASUKAN COOKIE :')
token=input('INPUT TOKEN : ')
open('.cookie.txt','w').write(cookie)
open('.token.txt','w').write(token)
os.system('python aerox.py')
