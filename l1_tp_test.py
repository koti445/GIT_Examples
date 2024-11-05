import os
import sys

UL_Stats_List,UL_List,UL_Bler = [],[],[]

with open("l1_tp.log",'r') as l1tp:
    str1=l1tp.readlines()
    #print(str1)
    for tmp_str in str1:
        print(tmp_str)
        if "UL_Stats:" in tmp_str:
            print(tmp_str)
        else:
            print("UL_Stats not found")
    #print(line for line in  l1tp.readlines() if 'UL_Stats:' in line)

#print(line for line in open('l1_tp.log','r') if 'UL_Stats:' in line)
