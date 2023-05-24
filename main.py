import zipfile
import tabula


PDF_PATH = "https://www.gov.br/ans/pt-br/assuntos/consumidor/o-que-o-seu-plano-de-saude-deve-cobrir-1/Anexo_I_Rol_2021RN_465.2021_RN473_RN478_RN480_RN513_RN536_RN537_RN538_RN539_RN541_RN542_RN544_546_571_577.pdf"


lista_tabelas = tabula.read_pdf(PDF_PATH, pages="all", stream=True)
print(len(lista_tabelas))


tabula.convert_into(PDF_PATH, "testeleticia.csv", pages="all", output_format="csv", stream=True)

z = zipfile.ZipFile('testeleticia.zip', 'w', zipfile.ZIP_DEFLATED)
z.write('testeleticia.csv')