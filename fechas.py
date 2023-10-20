import datetime
import subida_archivos

def limit(año, mes):
    if mes == 12:
        limit_date=datetime.datetime(año+1,1,1,1,00)
    else:
        limit_date=datetime.datetime(año,mes+1,1,1,00)
    return limit_date

def fechas_mes(year, month, hoja,st,row):
    new_date=datetime.datetime(year,month,1,1,0,0)
    i=0
    while new_date<limit(year,month):
        s=st
        n=row+i
        n1=str(n)
        s1=s+n1
        if new_date.hour>23:
            new_date=datetime.datetime(year,month,new_date.day,00,00)+datetime.timedelta(days=1)
            hoja[s1].value=new_date
        else:
            hoja[s1].value=new_date
            new_date=new_date+datetime.timedelta(hours=1)
        i+=1