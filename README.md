# Bot de pesquisa

- Este código foi feito para fazer pesquisas, através de um
Bot que escreve o que for requisitado, procura pra você e te retorna os títulos da pesquisa em uma tabela de formato csv.

- Mais sobre: Foi usado o Chrome como navegador para as pesquisas; foi escolhido a palavra "Mamão" para ser pesquisada, mas caso queira falar para o Bot pesquisar outras coisas, como "Banana", na mesma região de pesquisa do quinto passo "#5" do arquivo "main.py", linha 19 do código, na função ".send_keys("Mamão", Keys.RETURN)" no código e vai te retornar os títulos em arquivo csv, é só trocar a palavra do que você quer pesquisar.

- O arquivo que executa o código é o "main.py"
## Bibliotecas usadas

- Foi usado o Selenium para a automação, WebDriver-Manager para a comunicação com o navegador e Unidecode, para a padronização dos caracteres.
- Para utilizar o código, é necessário instalar as bibliotecas, pelos comandos, no Terminal: pip install selenium (Para instalar o Selenium), pip install webdriver-manager (Para instalar o webdriver manager) e pip install unidecode (Para instalar o Unidecode)

| Command | Description |
| --- | --- |
| pip install selenium | Irá instalar a biblíoteca selenium |
| pip install webdriver-manager | Irá instalar a biblíoteca Webdriver Manager |
| pip install unidecode | Irá instalar a biblíoteca Unidecode|

## Autor

- Iago Silva