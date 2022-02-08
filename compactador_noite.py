# importing required modules
from zipfile import ZipFile
import os


def compactar_arquivo(nome_arquivo):
    # writing files to a zipfile
    with ZipFile('sddb_n.zip', 'w') as zip:
        # writing each file one by one
        zip.write(nome_arquivo)

    print('File zipped successfully!')


compactar_arquivo('SDDB_N.FBK')
