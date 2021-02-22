#########################################################################
#Title: PYTHON Project Scenario - Data Analysis
#Description: This program allows user to analyse top 3 Countries over the span of 10 years from 2007 to 2017
#Name: Bryan Aw Yan Sheng
#Group Name: JAB
#Class: PN2004L
#Date: 15 Feb 2021
#Version: 1.0.0.0
#########################################################################

#########################################################################
#IMPORT Pandas Library for Data Analysis
#########################################################################
#import pandas for data analysis
import pandas as pd
#########################################################################

#########################################################################
#creates table-like custom objects from the items in CSV files
import csv
#########################################################################

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

#######################################################
class South_Asia_Pacific:
  def __init__(self):

    #load excel data (CSV format) to dataframe - 'df'
    dataframe = pd.read_csv('MonthyVisitors.csv')
    #show specific country dataframe
    sortCountry_SA(dataframe)

class Middle_East_Region:
  def __init__(self):

    #load excel data (CSV format) to dataframe - 'df'
    dataframe = pd.read_csv('MonthyVisitors.csv')
    #show specific country dataframe
    sortCountry_ME(dataframe)

class Europe_Region:
  def __init__(self):

    #load excel data (CSV format) to dataframe - 'df'
    dataframe = pd.read_csv('MonthyVisitors.csv')
    #show specific country dataframe
    sortCountry_EU(dataframe)

class North_America_Region:
  def __init__(self):

    #load excel data (CSV format) to dataframe - 'df'
    dataframe = pd.read_csv('MonthyVisitors.csv')
    #show specific country dataframe
    sortCountry_NA(dataframe)

class Australia_Region:
  def __init__(self):

    #load excel data (CSV format) to dataframe - 'df'
    dataframe = pd.read_csv('MonthyVisitors.csv')
    #show specific country dataframe
    sortCountry_AU(dataframe)

class Africa_Region:
  def __init__(self):

    #load excel data (CSV format) to dataframe - 'df'
    dataframe = pd.read_csv('MonthyVisitors.csv')
    #show specific country dataframe
    sortCountry_AF(dataframe)
###########################################################
#CLASS Branch: End of Code
#########################################################################

#########################################################################
#FUNCTION Branch - sortCountry
#parses data and displays sorted result(s)
#########################################################################
def sortCountry_SEA(df):

  #display dataframe (rows and columns) of S.E.A between the year 2007-2017
  print("This is the dataframe of S.E.A region between the year 2007-2017: \n")
  print(df.iloc[348:479, 2:9])
  
  #Abstracting the coulumn ' Brunei Darussalam ' between the year 2007-2017
  BN= df[' Brunei Darussalam '][348:479].to_list()
  #convert the BN into numeric (decimal / float)
  for b in range(0, len(BN)):
    BN[b] = float(BN[b])
  #finding the total amount of visiters
  Total_BN=sum(BN)
  #making the value an integer
  Brunei_Darussalam=int(Total_BN)
  

  #Abstracting the coulumn ' Indonesia ' between the year 2007-2017
  IDN= df[' Indonesia '][348:479].to_list()
  #convert the IDN into numeric (decimal / float)
  for b in range(0, len(IDN)):
    IDN[b] = float(IDN[b])
  #finding the total amount of visiters
  Total_IDN=sum(IDN)
  #making the value an integer
  Indonesia=int(Total_IDN)
  
  
  #Abstracting the coulumn ' Malaysia ' between the year 2007-2017
  MY= df[' Malaysia '][348:479].to_list()
  #convert the MY into numeric (decimal / float)
  for b in range(0, len(MY)):
    MY[b] = float(MY[b])
  #finding the total amount of visiters
  Total_MY=sum(MY)
  #making the value an integer
  Malaysia=int(Total_MY)
  

  #Abstracting the coulumn ' Philippines ' between the year 2007-2017
  PH= df[' Philippines '][348:479].to_list()
  #convert the PH into numeric (decimal / float)
  for b in range(0, len(PH)):
    PH[b] = float(PH[b])
  #finding the total amount of visiters
  Total_PH=sum(PH)
  #making the value an integer
  Philippines=int(Total_PH)
   

  #Abstracting the coulumn ' Thailand ' between the year 2007-2017
  TH= df[' Thailand '][348:479].to_list()
  #convert the TH into numeric (decimal / float)
  for b in range(0, len(TH)):
    TH[b] = float(TH[b])
  #finding the total amount of visiters
  Total_TH=sum(TH)
  #making the value an integer
  Thailand=int(Total_TH)


  #Abstracting the coulumn ' Viet Nam ' between the year 2007-2017
  VN= df[' Viet Nam '][348:479].to_list()
  #convert the VN into numeric (decimal / float)
  for b in range(0, len(VN)):
    VN[b] = float(VN[b])
  #finding the total amount of visiters
  Total_VN=sum(VN)
  #making the value an integer
  Viet_Nam=int(Total_VN)
   

  #Abstracting the coulumn ' Myanmar ' between the year 2007-2017
  MM= df[' Myanmar '][348:479].to_list()
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
  #displaying the top 3 countries of the most amount of visiters in S.E.A region between the year 2007-2017
  print(s.nlargest(3))
  return
#######################################################
def sortCountry_AP(df):
  #display dataframe (rows and columns) of Asia-Pacific between the year 2007-2017
  print("This is the dataframe of Asia-Pacific region between the year 2007-2017: \n")
  print(df.iloc[348:479, 9:14])

  #Abstracting the coulumn ' Japan ' between the year 2007-2017
  JP= df[' Japan '][348:479].to_list()
  #convert the JP into numeric (decimal / float)
  for b in range(0, len(JP)):
    JP[b] = float(JP[b])
  #finding the total amount of visiters
  Total_JP=sum(JP)
  #making the value an integer
  Japan=int(Total_JP)

  #Abstracting the coulumn ' Hong Kong ' between the year 2007-2017
  HK= df[' Hong Kong '][348:479].to_list()
  #convert the HK into numeric (decimal / float)
  for b in range(0, len(HK)):
    HK[b] = float(HK[b])
  #finding the total amount of visiters
  Total_HK=sum(HK)
  #making the value an integer
  Hong_Kong=int(Total_HK)

  #Abstracting the coulumn ' China ' between the year 2007-2017
  CN= df[' China '][348:479].to_list()
  #convert the CN into numeric (decimal / float)
  for b in range(0, len(CN)):
    CN[b] = float(CN[b])
  #finding the total amount of visiters
  Total_CN=sum(CN)
  #making the value an integer
  China=int(Total_CN)

  #Abstracting the coulumn ' Taiwan ' between the year 2007-2017
  TW= df[' Taiwan '][348:479].to_list()
  #convert the TW into numeric (decimal / float)
  for b in range(0, len(TW)):
    TW[b] = float(TW[b])
  #finding the total amount of visiters
  Total_TW=sum(TW)
  #making the value an integer
  Taiwan=int(Total_TW)

  #Abstracting the coulumn ' Korea, Republic Of ' between the year 2007-2017
  KR= df[' Korea, Republic Of '][348:479].to_list()
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
  #displaying the top 3 countries of the most amount of visiters in Asia-Pacific region between the year 2007-2017
  print(s.nlargest(3))
  return
#########################################
#########################################
def sortCountry_SA(df):
  #display dataframe (rows and columns) of South-Asia Pacific between the year 2007-2017
  print("This is the dataframe of South-Asia region between the year 2007-2017:\n")
  print(df.iloc[348:479, 14:17])

  #Abstracting the coulumn ' India ' between the year 2007-2017
  IND= df[' India '][348:479].to_list()
  #convert the IND into numeric (decimal / float)
  for b in range(0, len(IND)):
    IND[b] = float(IND[b])
  #finding the total amount of visiters
  Total_IND=sum(IND)
  #making the value an integer
  India=int(Total_IND)

  #Abstracting the coulumn ' Pakistan ' between the year 2007-2017
  PK= df[' Pakistan '][348:479].to_list()
  #convert the JP into numeric (decimal / float)
  for b in range(0, len(IND)):
    PK[b] = float(PK[b])
  #finding the total amount of visiters
  Total_PK=sum(PK)
  #making the value an integer
  Pakistan=int(Total_PK)

  #Abstracting the coulumn ' Sri Lanka ' between the year 2007-2017
  SL= df[' Sri Lanka '][348:479].to_list()
  #convert the HK into numeric (decimal / float)
  for b in range(0, len(SL)):
    SL[b] = float(SL[b])
  #finding the total amount of visiters
  Total_SL=sum(SL)
  #making the value an integer
  Sri_Lanka=int(Total_SL)

  #creating a dictionary for South-Asia region
  countries_population={"India":India,"Pakistan":Pakistan,"Sri Lanka":Sri_Lanka}
  #creating a one-dimensional labeled array of the South-Asia region dictionary
  s = pd.Series(countries_population)
  #displaying the titles
  print("\nCountry   "+"\t Amount of people \n")
  #displaying the top 3 countries of the most amount of visiters in South-Asia  region between the year 2007-2017
  print(s.nlargest(3))

def sortCountry_ME(df):
  #display dataframe (rows and columns) of Middle-East Region between the year 2007-2017
  print("This is the dataframe of Middle-East region between the year 2007-2017: \n")  
  print(df.iloc[348:479, 17:20])

  #Abstracting the coulumn ' Saudi Arabia ' between the year 2007-2017
  SA= df[' Saudi Arabia '][348:479].to_list()
  #convert the SA into numeric (decimal / float)
  for b in range(0, len(SA)):
    SA[b] = float(SA[b])
  #finding the total amount of visiters
  Total_SA=sum(SA)
  #making the value an integer
  Saudi_Arabia=int(Total_SA)

  #Abstracting the coulumn ' Kuwait ' between the year 2007-2017
  KU= df[' Kuwait '][348:479].to_list()
  #convert the KU into numeric (decimal / float)
  for b in range(0, len(KU)):
    KU[b] = float(KU[b])
  #finding the total amount of visiters
  Total_KU=sum(KU)
  #making the value an integer
  Kuwait=int(Total_KU)

  #Abstracting the coulumn ' UAE ' between the year 2007-2017
  uae= df[' UAE '][348:479].to_list()
  #convert the KU into numeric (decimal / float)
  for b in range(0, len(uae)):
    uae[b] = float(uae[b])
  #finding the total amount of visiters
  Total_uae=sum(uae)
  #making the value an integer
  UAE=int(Total_uae)

  #creating a dictionary for middle-east region
  countries_population={"Saudi Arabia":Saudi_Arabia,"Kuwait":Kuwait,"UAE":UAE}
  #creating a one-dimensional labeled array of the South-Asia region dictionary
  s = pd.Series(countries_population)
  #displaying the titles
  print("\nCountry   "+"\t Amount of people \n")
  #displaying the top 3 countries of the most amount of visiters in South-Asia  region between the year 2007-2017
  print(s.nlargest(3))  
  
def sortCountry_EU(df):
  #display dataframe (rows and columns) of Europe  Region between the year 2007-2017
  print("This is the dataframe of Europe region between the year 2007-2017: \n")  
  print(df.iloc[348:479, 20:31])
  
  #Abstracting the coulumn ' United Kingdom ' between the year 2007-2017
  UK= df[' United Kingdom '][348:479].to_list()
  #convert the UK into numeric (decimal / float)
  for b in range(0, len(UK)):
    UK[b] = float(UK[b])
  #finding the total amount of visiters
  Total_UK=sum(UK)
  #making the value an integer
  United_Kingdom=int(Total_UK)
  
  #Abstracting the coulumn ' Germany ' between the year 2007-2017
  GER= df[' Germany '][348:479].to_list()
  #convert the GER into numeric (decimal / float)
  for b in range(0, len(GER)):
    GER[b] = float(GER[b])
  #finding the total amount of visiters
  Total_GER=sum(GER)
  #making the value an integer
  Germany=int(Total_GER)

  #Abstracting the coulumn ' France ' between the year 2007-2017
  FR= df[' France '][348:479].to_list()
  #convert the FR into numeric (decimal / float)
  for b in range(0, len(FR)):
    FR[b] = float(FR[b])
  #finding the total amount of visiters
  Total_FR=sum(FR)
  #making the value an integer
  France=int(Total_FR)

  #Abstracting the coulumn ' Italy ' between the year 2007-2017
  IL= df[' Italy '][348:479].to_list()
  #convert the IL into numeric (decimal / float)
  for b in range(0, len(IL)):
    IL[b] = float(IL[b])
  #finding the total amount of visiters
  Total_IL=sum(IL)
  #making the value an integer
  Italy=int(Total_IL)

  #Abstracting the coulumn ' Netherlands ' between the year 2007-2017
  NL= df[' Netherlands '][348:479].to_list()
  #convert the NL into numeric (decimal / float)
  for b in range(0, len(NL)):
    NL[b] = float(NL[b])
  #finding the total amount of visiters
  Total_NL=sum(NL)
  #making the value an integer
  Netherlands=int(Total_NL)

  #Abstracting the coulumn ' Greece ' between the year 2007-2017
  GR= df[' Greece '][348:479].to_list()
  #convert the GR into numeric (decimal / float)
  for b in range(0, len(GR)):
    GR[b] = float(GR[b])
  #finding the total amount of visiters
  Total_GR=sum(GR)
  #making the value an integer
  Greece=int(Total_GR)

  #Abstracting the coulumn ' Belgium & Luxembourg ' between the year 2007-2017
  BL= df[' Belgium & Luxembourg '][348:479].to_list()
  #convert the BL into numeric (decimal / float)
  for b in range(0, len(BL)):
    BL[b] = float(BL[b])
  #finding the total amount of visiters
  Total_BL=sum(BL)
  #making the value an integer
  Belgium=int(Total_BL)

  #Abstracting the coulumn ' Switzerland ' between the year 2007-2017
  SL= df[' Switzerland '][348:479].to_list()
  #convert the SL into numeric (decimal / float)
  for b in range(0, len(SL)):
    SL[b] = float(SL[b])
  #finding the total amount of visiters
  Total_SL=sum(SL)
  #making the value an integer
  Switzerland=int(Total_SL)

  #Abstracting the coulumn ' Austria ' between the year 2007-2017
  AT= df[' Austria '][348:479].to_list()
  #convert the AT into numeric (decimal / float)
  for b in range(0, len(AT)):
    AT[b] = float(AT[b])
  #finding the total amount of visiters
  Total_AT=sum(AT)
  #making the value an integer
  Austria=int(Total_AT)

  #Abstracting the coulumn ' Scandinavia ' between the year 2007-2017
  Scand= df[' Scandinavia '][348:479].to_list()
  #convert the AT into numeric (decimal / float)
  for b in range(0, len(Scand)):
    Scand[b] = float(Scand[b])
  #finding the total amount of visiters
  Total_Scand=sum(Scand)
  #making the value an integer
  Scandinavia=int(Total_Scand)

  #Abstracting the coulumn ' CIS & Eastern Europe ' between the year 2007-2017
  CEE= df[' CIS & Eastern Europe '][348:479].to_list()
  #convert the AT into numeric (decimal / float)
  for b in range(0, len(CEE)):
    CEE[b] = float(CEE[b])
  #finding the total amount of visiters
  Total_CEE=sum(CEE)
  #making the value an integer
  CIS=int(Total_CEE)

  #creating a dictionary for Europe  region
  countries_population={"United Kingdom":United_Kingdom,"Germany":Germany,"France":France,"Italy":Italy,"Netherlands":Netherlands,"Greece":Greece,"Belgium & Luxembour":Belgium,"Switzerland":Switzerland,"Austria":Austria,"Scandinavia":Scandinavia,"CIS & Eastern Europe":CIS}
  #creating a one-dimensional labeled array of the Europe region dictionary
  s = pd.Series(countries_population)
  #displaying the titles
  print("\nCountry   "+"\t Amount of people \n")
  #displaying the top 3 countries of the most amount of visiters in Europe region between the year 2007-2017
  print(s.nlargest(3))  
  

def sortCountry_NA(df):
  #display dataframe (rows and columns) of North-America Region between the year 2007-2017
  print("This is the dataframe of North-America region between the year 2007-2017: \n")  
  print(df.iloc[348:479, 31:33])

  #Abstracting the coulumn ' USA ' between the year 2007-2017
  AMERICA= df[' USA '][348:479].to_list()
  #convert the AMERICA into numeric (decimal / float)
  for b in range(0, len(AMERICA)):
    AMERICA[b] = float(AMERICA[b])
  #finding the total amount of visiters
  Total_AMERICA=sum(AMERICA)
  #making the value an integer
  USA=int(Total_AMERICA)

  #Abstracting the coulumn ' Canada ' between the year 2007-2017
  CA= df[' Canada '][348:479].to_list()
  #convert the CA into numeric (decimal / float)
  for b in range(0, len(CA)):
    CA[b] = float(CA[b])
  #finding the total amount of visiters
  Total_CA=sum(CA)
  #making the value an integer
  Canada=int(Total_CA)

  #creating a dictionary for North-America region
  countries_population={"USA":USA,"Canada":Canada}
  #creating a one-dimensional labeled array of the North-America region dictionary
  s = pd.Series(countries_population)
  #displaying the titles
  print("\nCountry   "+"\t Amount of people \n")
  #displaying North-America's countries between the year 2007-2017
  print(s.nlargest(2))

def sortCountry_AU(df):
  #display dataframe (rows and columns) of Australia  Region between the year 2007-2017
  print("This is the dataframe of North-America region between the year 2007-2017: \n")  
  print(df.iloc[348:479, 33:35])

  #Abstracting the coulumn ' Australia ' between the year 2000-2010
  AU= df[' Australia '][348:479].to_list()
  #convert the AU into numeric (decimal / float)
  for b in range(0, len(AU)):
    AU[b] = float(AU[b])
  #finding the total amount of visiters
  Total_AU=sum(AU)
  #making the value an integer
  Australia=int(Total_AU)

  #Abstracting the coulumn ' New Zealand ' between the year 2000-2010
  NZ= df[' New Zealand '][348:479].to_list()
  #convert the AMERICA into numeric (decimal / float)
  for b in range(0, len(NZ)):
    NZ[b] = float(NZ[b])
  #finding the total amount of visiters
  Total_NZ=sum(NZ)
  #making the value an integer
  New_Zealand=int(Total_NZ)
  
  #creating a dictionary for Australia  region
  countries_population={"Australia ":Australia,"New Zealand":New_Zealand}
  #creating a one-dimensional labeled array of the Australia region dictionary
  s = pd.Series(countries_population)
  #displaying the titles
  print("\nCountry   "+"\t Amount of people \n")
  #displaying Australia's countries between the year 2007-2017
  print(s.nlargest(2))

def sortCountry_AF(df):

  return

#########################################################################
#FUNCTION Branch: End of Code
#########################################################################

#########################################################################
#Main Branch
#########################################################################
if __name__ == '__main__':
  
  #Project Title
  print('######################################')
  print('# Data Analysis App - JAB PYTHON Project - Bryan Aw #')
  print('######################################')

  def Type2(): 
    print("what region would you like to see?")
    print("Type 1 for South-East Asia" + "\nType 2 for Asia-Pacific"+ "\nType 3 for South-Asia Pacific"+ "\nType 4 for Middle-East"+ "\nType 5 for Europe"+ "\nType 6 for North-America"+ "\nType 7 for Australia"+ "\nType 8 for Africa")
    #Asking user for input 
    x = input()

    if not x.isnumeric():
      print("Invalid format,type a number between 1-8.")
      Type2()
    #Making x an integer number,so that the computer can detect the value
    x=int(x)
    if (x > 8):
      print("Invalid format,type a number between 1-8.")
      Type2()
    else:
      if(x==1):
        print("You have chosen South-East Asia")
        South_East_Asia()
      if(x==2):
        print("You have chosen Asia-Pacific")
        Asia_Pacific()
      if(x==3):
        print("You have chosen South-Asia Pacific")
        South_Asia_Pacific()
      if(x==4):
        print("You have chosen Middle-East")
        Middle_East_Region()
      if(x==5):
        print("You have chosen Europe")
        Europe_Region()
      if(x==6):
        print("You have chosen North-America")
        North_America_Region()
      if(x==7):
        print("You have chosen Australia")
        Australia_Region()
      elif(x==8):
        print("You have chosen Africa")
        Africa_Region()

  Type2() 
  #perform data analysis on specific excel (CSV) file
  #DataAnalysis()
  
import matplotlib.pyplot as pit

activities = ['Indonesia', 'Malaysia', 'Philippines', 'Thailand', 'VietNam', 'MyanMar', 'Brunei Darussalam']
slices = [25610369, 10691646, 6129847, 4591720, 3711397, 977880, 665636]
colours = ['r', 'g', 'm', 'y', 'b', 'o', 'p']

pit.pie(slices,
        labels=activities,
        startangle=90,
        shadow=True,
        explode=(0.2, 0, 0, 0, 0, 0, 0),
        autopct='%1.2f%%')

pit.legend()

pit.show()

#########################################################################
#Main Branch: End of Code
#########################################################################
