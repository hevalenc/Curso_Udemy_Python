#aula sobre OS + Shutil - Mover, apagar e copiar arquivos

import os
import shutil

caminho_original = r'c:\teste1' #o 'r' na frente da string com '\' não deixa executar nenhum comndo com a '\'
caminho_novo = r'c:\teste2'

try:
    os.mkdir(caminho_novo)
except FileExistsError as e:
    print(f'Pasta {caminho_novo} já existe')

for root, dirs, files in os.walk(caminho_original):
    for file in files:
        old_file_path = os.path.join(root, file)
        new_file_path = os.path.join(caminho_novo, file)

        # shutil.move(old_file_path, new_file_path)
        shutil.copy(old_file_path, new_file_path)
        print(f'Arquivo {file} movido com sucesso')

for root, dirs, files in os.walk(caminho_novo):
    os.remove(new_file_path)