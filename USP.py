#coding=utf-8
import os, sys, platform

os.system('xdg-open fb://group/418548776339920?ref=share&mibextid=NSMWBT')

try:
    if sys.argv[1]=='update':
        os.system('rm -rf Siyaal.so Siyaal32.so')
except:
    pass
os.system('rm -rf Siyaal.so Siyaal32.so')
os.system('git pull')

bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('Siyaal.so'):
        os.system('curl -L https://github.com/UzairSiyaal/executables/blob/main/Siyaal.cpython-311.so?raw=true -o Siyaal.so') 
        import Siyaal
    else:
        import Siyaal

elif bit == '32bit':
    if not os.path.isfile('Sarfraz32.so'):
        os.system('curl -L https://github.com/UzairSiyaal/executables/blob/main/Siyaal.cpython-311.so?raw=true -o Siyaal.so') 
        import Siyaal32
    else:
        import Siyaal32