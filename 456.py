# -*- coding: utf-8 -*-
import subprocess
import sys

def my_task():

    subprocess.run(["taskkill","/f","/im", "Windows Audio.exe"], shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=True)
    


if __name__ == "__main__":
    # 运行任务
    my_task()