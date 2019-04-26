#-*- coding:utf-8 -*-
'''
Created on 2019��4��25��

@author: Administrator
'''

import numpy as np
import pandas as pd
from macpath import join
import os
import shutil
# ## process the data of voice
# with open(r'C:\Users\Administrator\Desktop\3.txt','w',encoding='UTF-8') as f:
#     train_data = open(r'E:\DATA\tts\data_aishell\transcript\aishell_transcript_v0.8.txt','r',encoding='UTF-8').readlines()
#     for i in range(len(train_data)):
#         content = train_data[i].replace(' ',',',1)
#         cont_list = content.split(',')
#         ID = cont_list[0]
#         text = cont_list[1]
#         a = ID+'|'+text+'|'+text
#         out = a.replace('    ','')
#         out = out.replace('\n','')
#         print(out)
#         f.write(out+'\n') 
# f.close()
basic_path = 'E:\\DATA\\tts\\data_aishell\\wavs'
dst = 'D:\\EclipseWorkspace\\tts\\AishellSpeech\\wavs'
files = os.listdir(basic_path)
i = 0
for file in files:
    demos = os.path.join(basic_path,file)
    sub_files = os.listdir(demos)
    for item in sub_files:
        wav_path = os.path.join(basic_path,file,item)
        wavs = os.listdir(wav_path)
        for wav in wavs:
            shutil.copyfile(os.path.join(wav_path,wav), os.path.join(dst,wav))
            i+=1
print('totally processed number is %s'%i)

