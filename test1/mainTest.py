

import time 
from datetime import datetime
from pathlib import Path
from SMWinservice import SMWinservice

def writeTofile(is_running):
    while is_running():
            DIR = "C:/Users/yakvl/Desktop/test1/log.txt"
            time.sleep(1)
            with open(DIR, 'a+') as file:
                file.write(f"{str(datetime.now())}\n")

class PythonCornerExample(SMWinservice):
    _svc_name_ = "PythonCornerExample123"
    _svc_display_name_ = "Python Corner's Winservice Example123"
    _svc_description_ = "That's a winservice!123"

    def start(self):
        self.isrunning = True

    def stop(self):
        self.isrunning = False

    def main(self):
        writeTofile(lambda: self.isrunning)

if __name__ == '__main__':
    PythonCornerExample.parse_command_line()
