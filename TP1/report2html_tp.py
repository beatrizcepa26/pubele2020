from re import *
import os
import jinja2 as j2
from bs4 import BeautifulSoup as bs



def readfile(filename):
# para ler um ficheiro (devolve texto)
    with open(filename) as f:
        report=f.read()
    return report


def extractDtd(filename):
# recebe o DTD do nosso XML e retorna uma lista com as tags todas
    content=readfile(filename)
    tags=[]
    for tag in findall(r'<!ELEMENT (.*?) ',content): 
        tags.append(tag)
    return(tags)


def extractDict(L,report):
# recebe uma lista com tags e devolve um dicionário com o que está dentro dessas tags para o report
    infoDict={}
    for el in L:
        v=search(rf'<{el}(.*?)>((?:.|\n)*?)</{el}>',report)
        # |\n é para incluir o newline na procura e ?: é para dizer que os parenteses no (?:.|\n) não são para
        #  atribuir a um grupo, são apenas para indicar prioridade.
        if v:
            infoDict[el]=v[2]
    return infoDict


def extrai_listaH(xml,tag):
# recebe uma string xml e uma tag e extrai uma lista homogenea com o miolo das tags
    infoH=[]
    for miolo in findall(rf'<{tag}(.*?)>((?:.|\n)*?)</{tag}>',xml): 
        infoH.append(miolo[1])
    return infoH


def preenche(info):
    t=j2.Template("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>{{title}}</title>
        <meta charset="UTF-8"/>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">
		<style>
	  	body {
  		background-color: LightYellow;
		margin: 0 auto;
		padding: 0 20px 20px 20px;
		}
		h1 {  
  		color: Chocolate;
  		padding: 20px 0;
  		text-shadow: 3px 3px 1px brown;
		}
		</style>
    </head>
    <body>
        <h1 align="center">{{title}}</h1>
        <h2 align="center">{{uc}}</h2>
        <p>{{date}}</p>
        <hr/>
        <a href="#section3">Conteúdo |</a>
        <a href="#section4">Referências |</a>
        <a href="index.html">Go back</a>
        <hr/>
        <h2 id="section1">Autores</h2>
        <hr/>
        <ul>
            {% for element in authors %}
            <li> {{element['name']}}
                <ul>
                    <li> <u>Número</u>: {{element['number']}}</li>
                    <li> <u>Email</u>: <a href= "mailto:{{element['email']}}">{{element['email']}}</a></li> 
                    <br>
                </ul>
            {% endfor %}
        </ul>
        <hr/>
        <h2 id="section2"><i>Link</i></h2>
        <ul>
            <li><a href= {{otherformat}} target="_blank">Report em PDF</a></li>
        </ul>
        <br>
        <h2 id="section3"> Conteúdo </h2>
        <br>
            {% for text in description %}
            <p align="justify">{{text}}</p>
            <br>
            {% endfor %}
        <center><img src= "{{image}}" ></center>
        <br>
        <h2 id="section4"> Referências </h2>
        <ol>
            {% for ref in references %}
            <li><a href = {{ref}} target="_blank"> {{ref}} </a></li>
            <br>
            {% endfor %}        
        </ol>
        <hr/>
        <a href="#section1">Autores |</a>
        <a href="#section2">Link |</a>
        <a href="index.html">Go back</a>
    </body>
    </html>
    """
    )
    return(t.render(info))



def preenche2(titles):
	t=j2.Template("""
		<!DOCTYPE html>
		<html>
		<head>
			<title>Índice</title>
			<meta charset="utf-8"/>
			<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
		</head>

		<body>
			<br>
			<h1 align="center"> Índice</h1>
			<hr>
			<br><br><br>
			{% for t in title %}
			<p align="center"> <a href= "report{{title.index(t)+1}}.html" title="Ir para Report{{title.index(t)+1}}" target="_blank"> {{t}}</a></p>
			<br>
			{% endfor %}
			<p align="center"> <a href= "" title="Ir para Código" target="_blank"> Código</a></p>
		</body>
		</html>""")

	return(t.render(titles))


def extractIndice(report):
	a = bs(report,"lxml")
	for el in a.find_all("title"):
		return el.text



def main():

    f = readfile("portefolio.xml")
    lista_tags = extractDtd("portefolio.dtd")

    if os.path.exists("./ReportsHTML" ) == False:
	    dir = "./ReportsHTML"      
	    os.mkdir(dir) # cria uma pasta onde vão ser guardados os Reports em HTML, SE ela ainda não existir

    i = 1
    t = {"title":[]}
    for report in f.split("</report>"): # faz o split para obter e guardar todos os reports numa lista como strings
        if "<report>" in report: # para ter a certeza que é um report válido, tem de ter a tag <report>
            d = extractDict(lista_tags,report)
            aux = extrai_listaH(d['authors'],'element')

            # para cada elemento de authors vai buscar o name, number e email
            d['authors'] = [extractDict(['name','number','email'],el) for el in aux]
            
            # vai buscar o conteúdo de cada ref
            d['references'] = extrai_listaH(d['references'],'ref')
            
            # vai buscar o conteúdo de cada text
            d['description'] = extrai_listaH(d['description'],'text')

            with open(rf"ReportsHTML/report{i}.html",'w') as file: 
                file.write(preenche(d)) # guarda os ficheiros HTML na pasta criada acima

            t["title"].append(extractIndice(report))

            with open(rf"ReportsHTML/index.html",'w') as f: 
                f.write(preenche2(t)) # guarda os ficheiros HTML na pasta criada acima'''

        i += 1

    print("Ficheiros HTML gerados e guardados com sucesso! :)")

main()