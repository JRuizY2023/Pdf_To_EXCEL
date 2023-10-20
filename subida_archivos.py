import xlrd
import os
import openpyxl
import tabula

def up_xlsx(ubicacion,sheet_name):
    libro=openpyxl.load_workbook(ubicacion)
    sheet=libro[sheet_name]
    return sheet, libro

def up_xls(ubicacion,sheet_position):
    libro=xlrd.open_workbook(ubicacion, logfile=open(os.devnull,"w"))
    sheet=libro.sheet_by_index(sheet_position)
    return sheet

def pdf_to_df(carpet,pdf,pag,pos,ncol):
        archivo=carpet+"/"+pdf
        lista_datos=tabula.read_pdf(archivo,pages=pag,area=pos,guess=True,pandas_options={'header': None})
        df_0=lista_datos[0]
        df_0_0=df_0.dropna(thresh=ncol)
        df=df_0_0.dropna(axis='columns')
        return df