# Bot de pesquisa

- Este código foi feito para fazer pesquisas, através de um
Bot que escreve o que for requisitado, procura pra você e te retorna os títulos da pesquisa em uma tabela de formato csv.

- Mais sobre: Foi usado o Chrome como navegador para as pesquisas; foi escolhido a palavra "Mamão" para ser pesquisada, mas caso queira falar para o Bot pesquisar outras coisas, como "Banana", na mesma região de pesquisa do quinto passo "#5" do arquivo "main.py", linha 19 do código, na função ".send_keys("Mamão", Keys.RETURN)" no código e vai te retornar os títulos em arquivo csv, é só trocar a palavra do que você quer pesquisar.

- O arquivo que executa o código é o "main.py"

- O arquivo output é o "test.csv", que irá retornar os valores dos titulos no arquivo csv e terminar sua execussão

## Bibliotecas usadas

- Foi usado o Selenium para a automação, WebDriver-Manager para a comunicação com o navegador e Unidecode, para a padronização dos caracteres.

- Para utilizar o código, é necessário instalar as bibliotecas, com a escrita, no Terminal: pip install -r requirements.txt, que irá instalar todas as biblíotecas necessárias.

| Command | Description |
| --- | --- |
| pip install -r requirements.txt | Irá instalar todas as biblíotecas necessárias |

- Ou você pode ir no terminal e instalar as biblíotecas uma por uma, digitando: pip install selenium (Para instalar o Selenium), pip install webdriver-manager (Para instalar o webdriver manager) e pip install unidecode (Para instalar o Unidecode) e usando depois da escrita código, a tecla RETURN-ENTER.

| Command | Description |
| --- | --- |
| pip install selenium | Irá instalar a biblíoteca selenium |
| pip install webdriver-manager | Irá instalar a biblíoteca Webdriver Manager |
| pip install unidecode | Irá instalar a biblíoteca Unidecode|


## Autor

- Iago Silva