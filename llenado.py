import pandas as pd
import xlrd
import openpyxl

##llenado de columnas de datos padrón
def llenado_excel_p(s1,num,i,j,sheet,df):
    s2=str(num+i)
    s=s1+s2
    n=df.iloc[i,j]
    sheet[s].value=float(n.replace(",","."))

#llenado de columnas ascendentes y descendentes de instrumento (presion)
def llenado_excel(s1,num,i,j,sheet,df):
    s2=str(num+i)
    s=s1+s2
    n0=df.iloc[i,j]
    n1=df.iloc[i,j+2]
    n=float(n0.replace(",","."))+float(n1.replace(",","."))
    sheet[s].value=n/2  

#llenado de columnas de temperatura
def llenado_temperatura(df,etiqueta,fil,sheet):
    for i in range(df.shape[0]):
        for j in range(df.shape[1]):
            if j==0: #Datos Padrones
                llenado_excel_p(etiqueta[j+1],fil,i,j,sheet,df)
                llenado_excel_p(etiqueta[j+3],fil,i,j,sheet,df)
            if j==1:
                llenado_excel_p(etiqueta[j-1],fil,i,j,sheet,df)
                llenado_excel_p(etiqueta[j+1],fil,i,j,sheet,df)

def llenado_dp_p_atm(lista,sheet_xls,sh_xlsx):
    for i in range(sheet_xls.nrows):
        if sheet_xls.cell_value(rowx=i,colx=0) == 'Base or Contract Pressure':
            sh_xlsx[lista[1]].value=sheet_xls.cell_value(rowx=i,colx=6)
        if sheet_xls.cell_value(rowx=i,colx=8) == 'Low hw Setpoint':
            sh_xlsx[lista[0]].value=sheet_xls.cell_value(rowx=i,colx=11)


