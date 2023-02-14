# -*- coding: utf-8 -*-


import subprocess
import time


def start_lgr(i):
    lgr_user = 'desktop' + str(i)
    lgr_path = '"C:\\Program Files (x86)\\BIMGODesign\\data\\flutter_assets\\assets\\data\\lgR.exe"'
    lgr_parameter = '"用户名=' + lgr_user + '|密码=Abc123!@|主机ip=192.168.4.151|端口=3389|色彩深度=24|全屏=true|背景=data\\flutter_assets\\assets\\data\\0.jpg|标题=false|工具栏=false|auto=true|多屏显示=false|磁盘映射=|窗口大小=1024*768"'
    print(lgr_path + " " + lgr_parameter)
    child = subprocess.Popen(lgr_path + " " + lgr_parameter, shell=True)
    loop_i = 0
    while True:
        loop_i = loop_i + 1
        flag = 1
        print(f'{str(loop_i)} is running')
        result = child.poll()
        print(result)
        if result is None:
            flag = 0
        if flag:
            break
        else:
            print("Task is running")
            time.sleep(2)


    if child.returncode:
        print(f"instance {lgr_user} startup failed ...")
    else:
        print(f"instance {lgr_user} startup success ...")
    return


for i in range(2):
    start_lgr(i+1)

