# Importações
import os
import zipfile
import pandas as pd
import tabula

# PDF que vamos tirar as tabelas
PDF_PATH = "Anexo_I_Rol_2021.pdf"

# Lendo as paginas do pdf escolhidas
tabelas = tabula.read_pdf(PDF_PATH, pages='3-180')

# Usando o pandas para unir os dados das tabelas
table_cat = pd.concat(tabelas, ignore_index=True)

# Transformando em csv e guardando o arquivo na pasta output
table_cat.to_csv(os.path.join("output","teste.csv"),index=False)

# Zipando o arquivo
with zipfile.ZipFile('Teste_Leticia_Calabria.zip', 'w', zipfile.ZIP_DEFLATED) as z:
    z.write('output/teste.csv')
