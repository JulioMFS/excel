import os
# from psutil import process_iter
import psutil
import stat
def delFileIfExists(f):
    # os.system("taskkill /f /im  scalc.exe")
    file_name = f
    for proc in psutil.process_iter():
        if proc.name() == 'scalc.exe' or proc.name() == 'excel.exe':
            print('Killing: ', proc.name())
            proc.kill


    # try:
    #     os.remove(file_name)
    # except PermissionError:
    #     print('PermissionError do change')
    #     os.chmod(file_name, stat.S_IWRITE)
    #     os.remove(file_name)
    # for proc in psutil.process_iter():
    #     if proc.name() == 'scalc.exe' or proc.name() == 'excel.exe':
    #         print('Killing: ', proc.name())
    #         proc.kill
    PATH = f
    if os.path.isfile(PATH) and os.access(PATH, os.R_OK):
        print(f + " exists and is readable - Removed")
        if os.path.exists(f):
            os.remove(f)
        return True
    else:
        print(f + " is missing or not readable")
        return False






