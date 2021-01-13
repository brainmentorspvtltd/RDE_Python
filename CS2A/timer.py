import time
from datetime import datetime as dt

while True:
    t = dt.now().time()
    print(t.strftime('%H:%M:%S, %p'))
    time.sleep(1)
    
