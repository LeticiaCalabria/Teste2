import pandas as pd
import os
import tabula

PDF_PATH = "Anexo_I_Rol_2021.pdf"

tables = tabula.read_pdf(PDF_PATH, pages='3-180')

#for df in tables:df = df.drop(index=0)
#tables[1] = tables[1].drop(index=0)

table_cat = pd.concat(tables, ignore_index=True)

table_cat.to_csv(os.path.join("output",f"31.csv"),index=False)