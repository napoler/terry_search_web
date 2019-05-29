import subprocess
 
import os
from random import choice
 

# cmd = "mkdir "+training_path
# print("开始处理: "+cmd)
# print(subprocess.call(cmd, shell=True))

# for item in corpu_list:
i=0
while i<10000:
  #重新选择未处理的文件
 

  cmd = "python3 ./baidu_run.py" 
  print("开始处理: "+cmd)
  print(subprocess.call(cmd, shell=True))
  i=i+1