# -*- coding: utf-8 -*-
import pandas as pd;
import matplotlib as plt;
#df1=pd.ExcelFile("D:\\DataScience\\ml-1m\\ratings.xlsx");
#print (df);
#df=df1.parse('Sheet1');
#print(df);
#df2=pd.ExcelFile("D:\\DataScience\\ml-1m\\movies.xlsx");
#dfMovie=df2.parse('Sheet2');
#print(dfMovie);
df1=pd.read_csv("D:\\DataScience\\ml-1m\\ratings.dat",sep="::",names=['UID','MID','Rate','T'],header=0);
df1.head();
df2=pd.read_csv("D:\\DataScience\\ml-1m\\movies.dat",sep="::",names=['MID','MNAME','G'],header=0);
df2.head();
#MR=pd.merge(df1,df2,how='inner',left_on='MovieID',right_on='MovieID');
