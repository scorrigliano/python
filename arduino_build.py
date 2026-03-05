# Passo a passo do projeto
# Passo 1: Entrar no sistema da empresa 
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login

import os
from tkinter.filedialog import askdirectory #importa apenas a função desejada assim não é necessário aportar para a biblioteca na hora de usar
import pyautogui
import time
import shutil as sh

# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas
pyautogui.PAUSE = 0.3

#verifica o nome de usuário
username = os.environ.get('USERNAME')
print(f"Usuário atual: {username}")

teste_pasta_bin = False
lista_de_pastas=[]
#pasta_temp = "C:\\Users\\scorr\\AppData\\Local\\Temp"
#pasta_bin = "C:\\Users\\scorr\\OneDrive\\oNtARGET\\eng\projetos\\__bin\\esp"
pasta_temp = f"C:/Users/{username}/AppData/Local/Temp"
pasta_bin = f"C:/Users/{username}/OneDrive/oNtARGET/eng/projetos/__bin/esp"
lista_arquivos = os.listdir(pasta_temp)
#limpa temp
for arquivo in lista_arquivos:
    if not "." in arquivo:
        if "{" in arquivo:
            sh.rmtree(f"{pasta_temp}\\{arquivo}")
        elif "swx" in arquivo:
            sh.rmtree(f"{pasta_temp}\\{arquivo}")
    elif "TCD" in arquivo: #TCDxxx.tmp
        if ".tmp" in arquivo:
            sh.rmtree(f"{pasta_temp}\\{arquivo}")


for arquivo in lista_arquivos:
    if not "." in arquivo:
        if "arduino_build" in arquivo:
            lista_de_pastas.append(f"{pasta_temp}\\{arquivo}")

quantidade_de_pastas = len(lista_de_pastas)
#print(lista_de_pastas)

print()
if quantidade_de_pastas:
    if os.path.exists(pasta_bin):
        teste_pasta_bin = True
        print("abrindo a pasta", pasta_bin)
        # abre o Windows Explorer
        pyautogui.hotkey('win', 'e')
        time.sleep(1)
        #clica na área do endereço
        pyautogui.click(x=500, y=65)
        #entra com o endereço
        pyautogui.write(pasta_bin)
        pyautogui.press("enter")
        time.sleep(1)
    else:
        print("Não existe a pasta", pasta_bin)

    #esse laço enumera o índice conforme avança na lista
    #for indice, pasta in enumerate(lista_de_pastas):
    #    print()
    #    print(f"abrindo a pasta {indice}: {pasta}")
    #esse laço faz o for de acordo com a quantidade
    # for indice in range(quantidade_de_pastas):
    #     pasta = lista_de_pastas[indice]
    #     print()
    #     print(f"abrindo a pasta {indice}: {pasta}")
    #esse laço não considera o índice do ítem
    #print("total de pastas: ", quantidade_de_pastas)
    for pasta in lista_de_pastas:
        print("abrindo a pasta", pasta)
        if teste_pasta_bin == True:
            #abre uma aba na janela aberta
            pyautogui.hotkey('ctrl', 't')
        else:
            # abre o Windows Explorer
            pyautogui.hotkey('win', 'e')
        time.sleep(1)
        #clica na área do endereço
        pyautogui.click(x=500, y=65)
        #entra com o endereço
        pyautogui.write(pasta)
        pyautogui.press("enter")
        time.sleep(1)

else:
    print("não existe pasta de build para o Arduino IDE")

print()







"""



"""