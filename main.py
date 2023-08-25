import pandas as pd


def read_excel(file):
    df = pd.read_excel(file)
    rows, columns = df.shape
    result = list()
    for i in range(0, rows):
        values =[]
        for j in range(0,columns):
            val = df.loc[i][j]
            if val != val:
                val = ""
            values.append(val)
        tpl = tuple(values)
        result.append(tpl)
    with open("files\df.txt",'w')as file:
        file.write(str(result))


url= "files\Tabla de abonos.xlsx"
read_excel(url)