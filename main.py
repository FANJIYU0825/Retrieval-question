from .Src import Crewing
from .Src import TrivailProcess
import pandas as pd
import json
import argparse  

parser = argparse.ArgumentParser()
parser = argparse.ArgumentParser(description='Open Domain Qustion',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('--path', default='./My_Test_Data', type=str, help='Path of source images')
parser.add_argument('--trivail', action='store_true', help='Disable cropping')
args = parser.parse_args()
if __name__ == '__main__':
    searchnum=input("Search Number of :")
    searchnum = int(searchnum)
    alllst=Crewing.finout(searchnum)
    allinone=Crewing.url_finder(alllst,searchnum)
    jsonIT=Crewing.Qacrewing(allinone,searchnum)
    
    #pandas 寫法
    df_all=pd.DataFrame(jsonIT)
    json_Name = '/Src/NLP_LAB_Homework.json'
    with open(json_Name, 'w', encoding='utf-8') as file:
       df_all.to_json(file, force_ascii=False)
     
 
    