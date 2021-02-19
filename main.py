#########################################################################
#Title: PYTHON Project Scenario - Data Analysis
#Description: This program allows user to analyse.......
#Name: BryanAw
#Group Name: JAB
#Class: PN2004L
#Date: 10 Feb 2021
#Version: 1.0.0.0
#########################################################################

#########################################################################
#IMPORT Pandas Library for Data Analysis
#########################################################################
#import pandas for data analysis
import pandas as pd

import csv
#creates table-like custom objects from the items in CSV files

#########################################################################
#IMPORT Pandas Library for Data Analysis
#########################################################################

#########################################################################
#CLASS Branch - Data Analysis
#load excel data (CSV format) to dataframe
#########################################################################
class South_East_Asia:
  def __init__(self):

    #load excel data (CSV format) to dataframe - 'df'
    dataframe = pd.read_csv('MonthyVisitors.csv')
    #show specific country dataframe
    sortCountry_SEA(dataframe)
#######################################################
class Asia_Pacific:
  def __init__(self):

    #load excel data (CSV format) to dataframe - 'df'
    dataframe = pd.read_csv('MonthyVisitors.csv')
    #show specific country dataframe
    sortCountry_AP(dataframe)
##################
#CLASS Branch: End of Code
#########################################################################

#########################################################################
#FUNCTION Branch - sortCountry
#parses data and displays sorted result(s)
#########################################################################
def sortCountry_SEA(df):

  #display dataframe (rows and columns) of S.E.A between the year 2000-2010
  print("This is the dataframe of S.E.A region between the year 2000-2010: \n")
  print(df.iloc[264:396, 2:9])
  
  #Abstracting the coulumn ' Brunei Darussalam ' between the year 2000-2010
  BN= df[' Brunei Darussalam '][264:396].to_list()
  #convert the BN into numeric (decimal / float)
  for b in range(0, len(BN)):
    BN[b] = float(BN[b])
  #finding the total amount of visiters
  Total_BN=sum(BN)
  #making the value an integer
  Brunei_Darussalam=int(Total_BN)
  

  #Abstracting the coulumn ' Indonesia ' between the year 2000-2010
  IDN= df[' Indonesia '][264:396].to_list()
  #convert the IDN into numeric (decimal / float)
  for b in range(0, len(IDN)):
    IDN[b] = float(IDN[b])
  #finding the total amount of visiters
  Total_IDN=sum(IDN)
  #making the value an integer
  Indonesia=int(Total_IDN)
  
  
  #Abstracting the coulumn ' Malaysia ' between the year 2000-2010
  MY= df[' Malaysia '][264:396].to_list()
  #convert the MY into numeric (decimal / float)
  for b in range(0, len(MY)):
    MY[b] = float(MY[b])
  #finding the total amount of visiters
  Total_MY=sum(MY)
  #making the value an integer
  Malaysia=int(Total_MY)
  

  #Abstracting the coulumn ' Philippines ' between the year 2000-2010
  PH= df[' Philippines '][264:396].to_list()
  #convert the PH into numeric (decimal / float)
  for b in range(0, len(PH)):
    PH[b] = float(PH[b])
  #finding the total amount of visiters
  Total_PH=sum(PH)
  #making the value an integer
  Philippines=int(Total_PH)
   

  #Abstracting the coulumn ' Thailand ' between the year 2000-2010
  TH= df[' Thailand '][264:396].to_list()
  #convert the TH into numeric (decimal / float)
  for b in range(0, len(TH)):
    TH[b] = float(TH[b])
  #finding the total amount of visiters
  Total_TH=sum(TH)
  #making the value an integer
  Thailand=int(Total_TH)


  #Abstracting the coulumn ' Viet Nam ' between the year 2000-2010
  VN= df[' Viet Nam '][264:396].to_list()
  #convert the VN into numeric (decimal / float)
  for b in range(0, len(VN)):
    VN[b] = float(VN[b])
  #finding the total amount of visiters
  Total_VN=sum(VN)
  #making the value an integer
  Viet_Nam=int(Total_VN)
   

  #Abstracting the coulumn ' Myanmar ' between the year 2000-2010
  MM= df[' Myanmar '][264:396].to_list()
  #convert the MM into numeric (decimal / float)
  for b in range(0, len(MM)):
    MM[b] = float(MM[b])
  #finding the total amount of visiters
  Toatl_MM=sum(MM)
  #making the value an integer
  Myanmar=int(Toatl_MM)

  #creating a dictionary for S.E.A region
  countries_population={"Brunei Darussalam":Brunei_Darussalam,"Indonesia":Indonesia,"Malaysia":Malaysia,"Philippines":Philippines,"Thailand":Thailand,"Viet Nam":Viet_Nam,"Myanmar":Myanmar}
  #creating a one-dimensional labeled array of the S.E.A region dictionary
  s = pd.Series(countries_population)
  #displaying the titles
  print("\nCountry   "+"\t Amount of people \n")
  #displaying the top 3 countries of the most amount of visiters in S.E.A region between the year 2000-2010
  print(s.nlargest(3))
  return
#######################################################
def sortCountry_AP(df):
  #display dataframe (rows and columns) of Asia-Pacific between the year 2000-2010
  print("This is the dataframe of Asia-Pacific region between the year 2000-2010: \n")
  print(df.iloc[264:396, 9:14])

  #Abstracting the coulumn ' Japan ' between the year 2000-2010
  JP= df[' Japan '][264:396].to_list()
  #convert the JP into numeric (decimal / float)
  for b in range(0, len(JP)):
    JP[b] = float(JP[b])
  #finding the total amount of visiters
  Total_JP=sum(JP)
  #making the value an integer
  Japan=int(Total_JP)

  #Abstracting the coulumn ' Hong Kong ' between the year 2000-2010
  HK= df[' Hong Kong '][264:396].to_list()
  #convert the HK into numeric (decimal / float)
  for b in range(0, len(HK)):
    HK[b] = float(HK[b])
  #finding the total amount of visiters
  Total_HK=sum(HK)
  #making the value an integer
  Hong_Kong=int(Total_HK)

  #Abstracting the coulumn ' China ' between the year 2000-2010
  CN= df[' China '][264:396].to_list()
  #convert the CN into numeric (decimal / float)
  for b in range(0, len(CN)):
    CN[b] = float(CN[b])
  #finding the total amount of visiters
  Total_CN=sum(CN)
  #making the value an integer
  China=int(Total_CN)

  #Abstracting the coulumn ' Taiwan ' between the year 2000-2010
  TW= df[' Taiwan '][264:396].to_list()
  #convert the TW into numeric (decimal / float)
  for b in range(0, len(TW)):
    TW[b] = float(TW[b])
  #finding the total amount of visiters
  Total_TW=sum(TW)
  #making the value an integer
  Taiwan=int(Total_TW)

  #Abstracting the coulumn ' Korea, Republic Of ' between the year 2000-2010
  KR= df[' Korea, Republic Of '][264:396].to_list()
  #convert the KR into numeric (decimal / float)
  for b in range(0, len(KR)):
    KR[b] = float(KR[b])
  #finding the total amount of visiters
  Total_KR=sum(KR)
  #making the value an integer
  korea=int(Total_KR)

  #creating a dictionary for Asia-Pacific region
  countries_population={"Japan":Japan,"Hong Kong":Hong_Kong,"China":China,"Taiwan":Taiwan,"Korea, Republic Of":korea}
  #creating a one-dimensional labeled array of the Asia-Pacific region dictionary
  s = pd.Series(countries_population)
  #displaying the titles
  print("\nCountry   "+"\t Amount of people \n")
  #displaying the top 3 countries of the most amount of visiters in Asia-Pacific region between the year 2000-2010
  print(s.nlargest(3))
  return
##################
#FUNCTION Branch: End of Code
#########################################################################

#########################################################################
#Main Branch
#########################################################################
if __name__ == '__main__':
  
  #Project Title
  print('######################################')
  print('# Data Analysis App - PYTHON Project - JAB #')
  print('######################################')

  def wow(): 
    print("what region would you like?")
    print("Type 1 for South-East Asia" + "\nType 2 for Asia-Pacific"+ "\nType 3 for South-Asia Pacific"+ "\nType 4 for Middle-East"+ "\nType 5 for Europe"+ "\nType 6 for North-America"+ "\nType 7 for Australia"+ "\nType 8 for Africa")
    #Asking user for input 
    x = input()

    if not x.isnumeric():
      print("Invalid format,type a number between 1-8.")
      wow()
    else:
    #Making x an integer number,so that the computer can detect the value
      x=int(x)
    if(x==1):
      print("You have chosen South-East Asia")
      South_East_Asia()
    if(x==2):
      print("You have chosen Asia-Pacific")
      Asia_Pacific()
    if(x==3):
      print("You have chosen South-Asia Pacific")
    if(x==4):
      print("You have chosen Middle-East")
    if(x==5):
      print("You have chosen Europe")
    if(x==6):
      print("You have chosen North-America")
    if(x==7):
      print("You have chosen Australia")
    elif(x==8):
      print("You have chosen Africa")

  wow() 
  #perform data analysis on specific excel (CSV) file
  #DataAnalysis()
  

#########################################################################
#Main Branch: End of Code
#########################################################################