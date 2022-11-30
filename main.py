# 1-Bibliotecas que foram importadas
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

OUPUT_FILE = 'test.csv'

def open_browser():
    # 2-Escrita do Protocolo, para a chamada de navegador, usando as definições para o navegador Google Chrome
    # Foi também usado aqui o WebDriver Manager, ele faz uma busca dinâmica de qual é a sua versão do Chrome, para executar o Navegador
    servico = Service(ChromeDriverManager().install())
    navegador = webdriver.Chrome(service=servico)
    return navegador

def pesquisa_google(navegador):
    # 3-Abertura da página Google no Navegador
    navegador.get("https://www.google.com/")
    # 4-Localização da barra de pesquisa do google, usando, como seu localizador, o seu Xpath, com a função"find_elements" do selenium
    # 5-Depois de localizar, o Bot escreve a palavra destinada a fazer a busca, no caso "Mamão" e clica em ENTER-RETURN, através da fução"send_keys"
    navegador.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("Mamão", Keys.RETURN)

def resultado_pesquisa(navegador):
    # 6-Aqui é criado a lista, onde serão carregados os titulos
    titulos =[]

    # 7-Aqui é onde o bot pega os objetos-elementos, que são titulos das páginas, para isso, ele usa em comum a classe, em "find_elements", pois os titulos tem uma classe em comum
    objTitulos = navegador.find_elements(By.XPATH,"//h3[contains(@class,'LC20lb')]")

    # 8-Aqui, na lista retornada, voltavam espaços vazios, então, foi escrito no código que para cada espaço vazio, voltassem somente os el-elementos
    for el in objTitulos:
        if el.text != "":
            titulos.append(el.text)

    return titulos

def output_csv(titulos):
    # 10-Neste código, é transformado a lista de elementos em um csv, sendo chamado de "arquivo", o novo documento em csv escrito, depois é definido o titulo
    #dos titulos como 'Titulos' e adicionado uma quebra de linha. Depois disso, é dito que para cada item-i, em titulos, tenha uma quebra de linha depois de cada um
    with open(OUPUT_FILE,'w',encoding='utf-8') as arquivo:
        arquivo.write('Titulos:'+'\n')
        for i in titulos:
            arquivo.write(str(i) + '\n')

def main():

    navegador = open_browser()

    pesquisa_google(navegador)

    titulos = resultado_pesquisa(navegador)

    output_csv(titulos)


main()