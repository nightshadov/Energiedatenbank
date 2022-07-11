import pandas as pd




dfEnYear=pd.read_excel (r'./data/energiedaten-gesamt-xls-2022.xlsx', sheet_name='6', header=7, usecols="A:AF", nrows=9)
dfColumnsEnYear=dfEnYear.columns[1:]

row2EnergySource = {
    0:"Steinkohle",
    1:"Braunkohle",
    2:"Kraftstoff",
    3:"Schweroel",
    4:"Leichtoel",
    5:"Gas",
    6:"Strom",
    7:"Fernwaerme",
    8:"Sonstige"
}



dfEnYearSect=pd.read_excel (r'./data/energiedaten-gesamt-xls-2022.xlsx', sheet_name='6a', usecols="A:AF", header=8)
dfColumnsYearSect=dfEnYearSect.columns[1:]

#print(dfEnYearSect)
#print(dfColumnsYearSect)

row2EnSect = {
    0:["Industrie","Steinkohle"],
    1:["Industrie","Braunkohle"],
    2:["Industrie","Schweroel"],
    3:["Industrie","Leichtoel"],
    4:["Industrie","Restoel"],
    5:["Industrie","Gas"],
    6:["Industrie","Naturgas"],
    7:["Industrie","Strom"],
    8:["Industrie","Fernwaerme"],
    9:["Industrie","Erneuerbare"],
    15:["Verkehr","Kohle"],
    16:["Verkehr","Kraftstoff"],
    17:["Verkehr","Motorbenzin"],
    18:["Verkehr","Flugkraftstoff"],
    19:["Verkehr","Fluessiggas"],
    20:["Verkehr","Kraftstoffrest"],
    21:["Verkehr","Gas"],
    22:["Verkehr","Strom"],
    23:["Verkehr","Biokraftstoff"],
    29:["Haushalte","Steinkohle"],
    30:["Haushalte","Braunkohle"],
    31:["Haushalte","Erneuerbare"],
    32:["Haushalte","Heizoel"],
    33:["Haushalte","Restoel"],
    34:["Haushalte","Gas"],
    35:["Haushalte","Naturgas"],
    36:["Haushalte","Strom"],
    37:["Haushalte","Fernwaerme"],
    42:["GHD","Steinkohle"],
    43:["GHD","Braunkohle"],
    44:["GHD","Erneuerbare"],
    45:["GHD","Heizoel"],
    46:["GHD","Restoel"],
    47:["GHD","Gas"],
    48:["GHD","Naturgas"],
    49:["GHD","Strom"],
    50:["GHD","Fernwaerme"],


}

dfEnYearAppl=pd.read_excel (r'./data/energiedaten-gesamt-xls-2022.xlsx', sheet_name='7', usecols="A:P", header=7)
dfColumnsYearAppl=list(range(2008,2021))#dfEnYearAppl.columns[1:]



#print(dfEnYearAppl[2008])
#print(dfEnYearAppl.columns)
#print(dfColumnsYearAppl)

dfEnYearSectAppl=pd.read_excel (r'./data/energiedaten-gesamt-xls-2022.xlsx', sheet_name='7a', usecols="A:P", header=18)
dfEnYearSectApplColumns=list(range(2008,2021))



#print(dfEnYearSectAppl[2008])
#print(dfEnYearSectAppl.columns)
#print(dfEnYearSectApplColumns)

row2SectApplEn= {
    4:["Industrie","Raumwaerme","Oel"],
    5:["Industrie","Raumwaerme","Gas"],
    6:["Industrie","Raumwaerme","Strom"],
    7:["Industrie","Raumwaerme","Fernwaerme"],
    8:["Industrie","Raumwaerme","Kohle"],
    9:["Industrie","Raumwaerme","Erneuerbare"],
    10:["Industrie","Raumwaerme","Sonstige"],
    12:["Industrie","Warmwasser","Oel"],
    13:["Industrie","Warmwasser","Gas"],
    14:["Industrie","Warmwasser","Strom"],
    15:["Industrie","Warmwasser","Fernwaerme"],
    16:["Industrie","Warmwasser","Kohle"],
    17:["Industrie","Warmwasser","Erneuerbare"],
    18:["Industrie","Warmwasser","Sonstige"],

}


dfSample=pd.read_csv(r'./data/username.csv', header=0, delimiter=";",)

#print(dfSample)
#print(dfSample.columns)
#print(dfSample[" Identifier"])


dfSample2=pd.read_csv(r'./data/access-code-password-recovery-code.csv', header=0, delimiter=";",)

print(dfSample2)
print(dfSample2.columns)
print(dfSample2["Identifier"])