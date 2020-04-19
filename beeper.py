

import contextlib
with contextlib.redirect_stdout(None):
    try:    from pygame import mixer
    except: print('pygame required. Execute pip3 install pygame'); sys.exit(1)
import time
import os

mixer.init()
alert=mixer.Sound('./beep.wav')
while(True):
    print('beeping...')
    alert.play()
    time.sleep(1)
