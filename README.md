# Bot de pesquisa

- Este código foi feito para fazer pesquisas, através de um
Bot que escreve o que for requisitado, procura pra você e te retorna os títulos da pesquisa em uma tabela de formato csv.

- Mais sobre: Foi usado o Chrome como navegador para as pesquisas; foi escolhido a palavra "Mamão" para ser pesquisada, mas caso queira falar para o Bot pesquisar outras coisas, como "Banana", na função parte da função: ".send_keys("Mamão", Keys.RETURN)", em `def pesquisa_google(navegador):`, no arquivo "main.py" e vai te retornar os títulos em arquivo csv, é só trocar a palavra do que você quer pesquisar.

- O arquivo que executa o código é o `main.py`

- O arquivo output é o "test.csv", que irá retornar os valores dos titulos no arquivo csv e terminar sua execussão tambem pode ser configurado na variavel de configuracao `OUPUT_FILE`

## Bibliotecas usadas

- Foi usado o Selenium para a automação, WebDriver-Manager para a comunicação com o navegador e Unidecode, para a padronização dos caracteres.

- Para utilizar o código, é necessário instalar as bibliotecas, com a escrita, no Terminal: pip install -r requirements.txt, que irá instalar todas as biblíotecas necessárias.

| Command | Description |
| --- | --- |
| pip install -r requirements.txt | Irá instalar todas as biblíotecas necessárias |

## Autor

- Iago Silva