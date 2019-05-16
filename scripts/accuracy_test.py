# -*- coding:utf-8 -*-

import os, re, shutil, time

client_dir=os.getcwd()
input_dir=r'C:\test'
op_time = time.strftime("%m%d%H%M%S", time.localtime())
os.mkdir(os.path.join(client_dir,"output_" + op_time))
output_dir = os.path.join(client_dir, "output_" + op_time)
result_file=os.path.join(output_dir,"cmccoutput.round1.txt")
os.mkdir(os.path.join(client_dir, "finished_" + op_time))
finished_dir = os.path.join(client_dir, "finished_" + op_time)
commandline="dotnet TranscribeCore.dll -i " + input_dir + " -o " + output_dir + " -h 172.22.242.8 -n 2 -l zh-CN -p 34932 --cmcc -t 4"

while True:
    if len(os.listdir(input_dir)) != 0:
        os.chdir(client_dir)
        os.system(commandline)
        if os.path.exists(result_file) == True:
            with open(result_file,"rb") as fls_ob:
                fls_context = fls_ob.read().decode('utf-8')
                successful_fls = re.findall(r'.+\.wav$',fls_context)
                for fl in successful_fls:
                    shutil.move(os.path.join(input_dir,fl),finished_dir)
                shutil.move(result_file,finished_dir)
                os.rename(os.path.join(finished_dir, result_file), os.path.join(finished_dir,time.strftime("%m%d%H%M%S", time.localtime())+'.txt'))
        for fl in os.listdir(output_dir):
            os.remove(os.path.join(output_dir,fl))
    elif len(os.listdir(input_dir)) == 0:
        print("All tasks is finished! ")
        break
    else:
        print("ERROR! Please check! ")
        break