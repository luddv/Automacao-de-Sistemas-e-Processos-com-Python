
# Automação de Sistemas e Processos com Python"
# Desafio:
    
#Todos os dias, o nosso sistema atualiza as vendas do dia anterior.
#O seu trabalho diário, como analista, é enviar um e-mail para a diretoria, assim que começar a trabalhar, com o faturamento e a quantidade de produtos vendidos no dia anterior"
  
    #E-mail da diretoria: seugmail+diretoria@gmail.com<br>",
    #Local onde o sistema disponibiliza as vendas do dia anterior: https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga?usp=sharing",
    
 
import pyautogui
import time
    
    #pyautogui.click -> clicar com o mouse
    #pyautogui.write -> escrever um texto
    #pyautogui.press -> aperta 1 tecla
    #pyautogui.hotkey -> combinação de teclas 
    
pyautogui.PAUSE = 0.5
    
    # Passo a passo do desafio
    # Passo 1: Entrar no sistema da empresa (link do drive)
    # abrir o edge
pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")

time.sleep(2)
    # escrever link  do sistema
link = "https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga"
pyautogui.write(link)
    # apertar enter e esperar
pyautogui.press("enter")
time.sleep(3)
    
    # Passo 2: Navegar no sistema para encontrar a base de dados
pyautogui.click(x=686, y=409, clicks = 2)
    # Passo 3: Exportar a base de dados (baixar o arquivo)
pyautogui.click(x=1790, y=404, clicks = 2)
pyautogui.click(x=1566, y=522, clicks = 2)


import pandas
    
    
    # Passo 4: Calcular os indicadores (faturamento e quantidade de produtos vendidos)
    # abrir a base de dados
caminho = r"c:\Users\almeidaLD\Downloads\Vendas - Dez.xlsx"
tabela = pandas.read_excel(caminho)
    
    # ver as informações da base de dados
print(tabela)
    # somar o faturamento de todos os produtos = somar a coluna do Valor final
faturamento = tabela["Valor Final"].sum()
    # somar a quantidade de produtos = somar a coluna de quantidade
qtdo_produtos = tabela["Quantidade"].sum()
    
print(faturamento)
print(qtdo_produtos)
    
import pyperclip
    
    # Passo 5: Enviar as informações por e-mail
    # nova aba
pyautogui.hotkey("ctrl", "t")
    
    # entrar no mail
pyautogui.write("http://mail.google.com/")
pyautogui.press("enter")
time.sleep(5)

    # escrever um e-mail
pyautogui.click(x=54, y=201)
time.sleep(8)

    # Para quem enviar o mail
pyautogui.write("almeidaludymilla6@gmail.com")
pyautogui.press("tab") # seleciona o e-mail
pyautogui.press("tab") # seleciona o assunto
time.sleep(3)

    # qual o assunto
pyperclip.copy("Relatório de Vendas")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("tab")
time.sleep(3)
    # qual o corpo do mail
texto = f"""
Prezados,

Segue o relatório de vendas de hoje.

Faturamento: R${faturamento:,.2f}
Quantidade de produtos vendidos: {qtdo_produtos:,}

Qualquer dúvida estou à disposição!
Abraços.

Ludymilla Almeida.
"""
pyperclip.copy(texto)
pyautogui.hotkey("ctrl", "v")
time.sleep(3)
    # enviar o mail
pyautogui.click(x=1180, y=968)
time.sleep(3)
   
    # Vamos agora ler o arquivo baixado para pegar os indicadores
   
    # Faturamento
    # Quantidade de Produtos
  
    # Vamos agora enviar um e-mail pelo gmail
 

