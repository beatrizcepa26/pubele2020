from re import *
import os
import jinja2 as j2


def read_file(filename):
# para ler um ficheiro.
    with open(filename) as f:
        report=f.read()
    return report


def extract_Dtd(filename):
# recebe o DTD do nosso XML e retorna uma lista com as tags todas.
    content=read_file(filename)
    tags=[]
    for tag in findall(r'<!ELEMENT (.*?) ',content): 
        tags.append(tag)
    return(tags)


def extract_Dict(L,report):
# recebe uma lista com tags e devolve um dicionário com o que está dentro dessas tags para o report.
    infoDict={}
    for el in L:
        v=search(rf'<{el}(.*?)>((?:.|\n)*?)</{el}>',report)
        # |\n é para incluir o newline na procura e ?: é para dizer que os parênteses no (?:.|\n) não são para
        # atribuir a um grupo, são apenas para indicar prioridade.
        if v:
            infoDict[el]=v[2]
    return infoDict


def extract_ListaH(xml,tag):
# recebe uma string xml e uma tag e extrai uma lista homogénea com o miolo da tag.
    infoH=[]
    for miolo in findall(rf'<{tag}(.*?)>((?:.|\n)*?)</{tag}>',xml): 
        infoH.append(miolo[1])
    return infoH


def preenche_Report(info):
    t=j2.Template("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>{{title}}</title>
        <meta charset="UTF-8"/>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">
		<style>
	  	body {background-color: Snow; margin: 0 auto; padding: 0 20px 20px 20px;}
		h1 {color: Navy; padding: 20px 0; text-shadow: 3px 3px 1px lightblue;}
		</style>
    </head>
    <body>
        <h1 align="center">{{title}}</h1>
        <h2 align="center">{{uc}}</h2>
        <p>{{date}}</p>
        <hr/>
        <a href="#section3">Conteúdo |</a>
        <a href="#section4">Referências |</a>
        <a href="#section5">Hashtags</a>
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
            {% for text in texts %}
            <p align="justify">{{text}}</p>
            <br>
            {% endfor %}
        <center><img src= "{{image}}" ></center>
        <br>
        <h2 id="section5"> Hashtags </h2>
        <p align="justify">    
            {% for hashtag in hashtags %}
            {{hashtag}}
            {% endfor %}
        </p>
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
        <a href="#section3">Conteúdo</a>
    </body>
    </html> """)

    return(t.render(info))


def preenche_Indice(info):
	t=j2.Template("""
		<!DOCTYPE html>
		<html>
		<head>
            <left><img align="left" src="https://raw.githubusercontent.com/beatrizcepa26/pubele2020/main/TP1/logoEEUM.png" width=150 height=100></left>
            <right><img align="right" src="https://raw.githubusercontent.com/beatrizcepa26/pubele2020/main/TP1/imagem.png?fbclid=IwAR1AAickXiDy-hHg7eHiY0fxvNQTUcqKCqJ6Y5fP2Kf8_Pija0Pmt3BUEOM" width=150 height=100></right>
            <br>
            <p align="center">Publicação Eletrónica 2020/2021</p>
            <br>
			<title align="center">Índice</title>
			<meta charset="utf-8"/>
			<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">
            <style>
            h1 {color: Navy; text-shadow: 4px 4px 2px lightblue;}
            p {color: Black; margin: 0 auto; padding: 0 10px 10px 10px;}
		    </style>
        </head>
		<body>
		    <br><br>
			<h1 align="center">Índice</h1>
			<hr>
			<br>
			{% for t in title %}
			<p align="center"> <a href= "report{{title.index(t)+1}}.html" title="Ir para Report{{title.index(t)+1}}" target="_blank"> {{t}}</a></p>
			<br>
			{% endfor %}
			<p align="center"> <a href= "https://github.com/beatrizcepa26/pubele2020/blob/main/TP1/report2html_tp.py" title="Ir para Código" target="_blank"> Código</a></p>
            <p align="center"> 
            {% for lista in hashtags %}
            {% for elemento in lista %}
            <a href="report{{hashtags.index(lista)+1}}.html" target="_blank">{{elemento}} |</a>
            {% endfor %}
            {% endfor %}
            <hr>
            <br>
            <p align="center">Mestrado Integrado em Engenharia Biomédica</p>
		</html> """)

	return(t.render(info))


def main():
    f = read_file("portefolio.xml")
    lista_tags = extract_Dtd("portefolio.dtd")

    if os.path.exists("./FilesHTML" ) == False:
	    dir = "./FilesHTML"      
	    os.mkdir(dir) # cria uma pasta onde vão ser guardados os Reports em HTML e o Índice, SE ela ainda não existir.

    i = 1
    info_indice = {"title":[],'hashtags':[]} # aqui estará a informação que vai povoar o template do Índice.
    for report in f.split("</report>"): 
    # faz o split para obter e guardar todos os reports numa lista, como strings.
        if "<report>" in report: 
        # para ter a certeza que é um report válido, tem de ter a tag <report>.
            info_report = extract_Dict(lista_tags,report) 
            # dicionário que tem as tags como chave e o miolo como valor.
            
            aux = extract_ListaH(info_report['authors'],'element')
            # para cada element de authors vai buscar o name, number e email.
            info_report['authors'] = [extract_Dict(['name','number','email'], el) for el in aux]
            # vai buscar o conteúdo de cada text na description e guarda.
            info_report['texts'] = extract_ListaH(info_report['description'],'text')
            # vai buscar o conteúdo de cada hashtag na description e guarda.						
            info_report['hashtags'] = extract_ListaH(info_report['description'],'hashtag')
            # vai buscar o conteúdo de cada ref em references e guarda.
            info_report['references'] = extract_ListaH(info_report['references'],'ref')

            with open(rf"FilesHTML/report{i}.html",'w') as file: 
                file.write(preenche_Report(info_report)) # preenche o template e guarda os reports HTML na pasta criada acima.

            # guarda a informação que estará no Índice.
            info_indice['title'].append(info_report['title'])
            info_indice['hashtags'].append(info_report['hashtags'])
            
            i += 1

    # finalmente cria o Índice com os títulos dos reports e as hashtags e guarda na mesma pasta.
    with open(rf"FilesHTML/index.html",'w') as f: 
                f.write(preenche_Indice(info_indice))
    
    print("Ficheiros HTML gerados e guardados com sucesso! :)")

main()