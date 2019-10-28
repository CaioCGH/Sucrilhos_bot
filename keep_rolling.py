#!/usr/bin/python
from subprocess import Popen
import sys
from datetime import datetime


filename = sys.argv[1]
bot_name = sys.argv[2]
while True:
    print(str(datetime.now()) + " Starting " + filename )
    try:
        p = Popen("python3 " + filename + " "+ bot_name, shell=True)
    except ProtocolError as e:
        print(str(datetime.now()) + " ProtocolError while running " + filename)
    except ConnectionError as e:
        print(str(datetime.now()) + " ConnectionError while running " + filename)
    except KeyboardInterrup as e:
        print(str(datetime.now()) + " keyboardInterrupt while running " + filename)
    p.wait()