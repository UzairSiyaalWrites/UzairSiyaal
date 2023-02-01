import os,time,platform
os.system('clear')
print('[•] Checking Updates...')
os.system('git pull')
green = ('\033[1;32m')
white = ('\033[1;37m')
red = ('\033[1;31m')

print('<------------------------------------>')
bit = platform.architecture()[0]
if bit=='64bit':
    print(f'{pink}[•] Join Over Facebook Group {red}')
    os.system('xdg-open fb://group/418548776339920?ref=share&mibextid=NSMWBT')
    time.sleep(0.05)
    import trt1
elif bit=='32bit':
    import trt32
else:
    print(f'{green}[×] Sorry System Not Support{white}')
