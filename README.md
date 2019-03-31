# Twitter media scraping

Com este script é possível pegar as imagens do perfil que informar.  
Ele baixa as imagens mais recentes do perfil, de 10 a 20 imagens.

## Requisitos?

1. Web Driver do Google Chrome 59+ [ChromeDriver](http://chromedriver.chromium.org/downloads)
2. Python 3.7
3. Selenium

As dependencias podem ser instaladas utilizando o comando

```
pip install -r requeriments.txt
```

## Como utilizar?

```
python media-scraping.py [perfil] [diretorio-para-salvar-imagens]
```

**Exemplo**  

Rodando o comando abaixo, irá baixar as últimas imagens do perfil informado na raiz do projeto.
```
python media-scraping.py lcomino .
```

## Todo

* [ ] Baixar os vídeos
* [ ] Definir um período para baixar as fotos