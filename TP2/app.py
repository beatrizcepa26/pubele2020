from flask import Flask, render_template, request, redirect
import json
import requests
from re import *
from povoamento import relatorios, pessoas
import db
import shelve

app = Flask(__name__)

for relatorio in relatorios:
	db.insert(relatorio)

for pessoa in pessoas:
	db.insert_p(pessoa)

@app.route('/')
def index():

	res1 = requests.get('http://localhost:5000/api/relatorios')
	ps = json.loads(res1.content)

	res2 = requests.get('http://localhost:5000/api/pessoas')
	pessoas = json.loads(res2.content)

	res3 = requests.get('http://localhost:5000/api/relatorios/hashtags')
	h = json.loads(res3.content)

	return render_template('index.html', titles=ps, hashtags=h, pessoas=pessoas)


@app.route('/relatorios', methods=['GET'])
def get_relatorios():
    res = requests.get('http://localhost:5000/api/relatorios')
    ps = json.loads(res.content)

    return render_template('relatorios_view.html', title='Relatórios', relatorios=ps)


@app.route('/relatorios', methods=['POST'])
def post_relatorio():
    data = dict(request.form)
    requests.post('http://localhost:5000/api/relatorios', data=data)

    return redirect('http://localhost:5000/relatorios')


@app.route('/relatorios/<titulo>', methods=['POST'])
def delete_relatorio(titulo):

	requests.post('http://localhost:5000/api/relatorios/' + titulo)

	return redirect('http://localhost:5000/relatorios')


@app.route('/relatorios/<titulo>', methods=['GET'])
def get_relatorio(titulo):
    res = requests.get('http://localhost:5000/api/relatorios/' + titulo)
    p = json.loads(res.content)

    return render_template('relatorio_view.html', p=p) 


@app.route('/relatorios/procura', methods=['GET'])
def procura_view():

    return render_template('procura_view.html')


@app.route('/pessoas/<nome>', methods=['GET'])
def get_pessoa(nome):
    res = requests.get('http://localhost:5000/api/pessoas/' + nome)
    p = json.loads(res.content)
    return render_template('pessoa_view.html', p=p)


@app.route('/relatorios/procura', methods=['POST'])
def relatorios_resultado():
	pesquisa = request.form.get('procura').replace('#','')

	res = requests.post('http://localhost:5000/api/relatorios/procura/'+pesquisa)
	p = json.loads(res.content)

	return render_template('resultados_pesquisa_view.html', title=rf'Relatórios que contêm a palavra "{pesquisa}"', relatorios=p['relatorios'], i=len(p['relatorios']),texts=p['titulos'])


@app.route('/api/relatorios/procura/<pesquisa>', methods=['POST'])
def get_relatorios_resultado(pesquisa):

	ps = db.find_all()
	l = []
	t = []
	palavra = rf"(?i)\b{pesquisa}\b"

	for titulo in ps:
		relatorio = db.find_one(titulo)
		res = findall(palavra,relatorio['description'])
		if res:
			text = relatorio['description']
			if titulo not in l:
				l.append(titulo)
				pos = text.index(res[0])
				if (len(text) >= 500):
					t.append(text[pos:pos+len(res[0])+500].replace(res[0],'<b>'+res[0]+'</b>'))
				else:
					t.append(text.replace(res[0],'<b>'+res[0]+'</b>'))
		elif findall(palavra,relatorio['uc']):
			text = relatorio['uc']
			if titulo not in l:
				l.append(titulo)
				t.append(f'Unidade Curricular: <b>{text}</b>')
		elif findall(palavra,relatorio['title']):
			text = relatorio['title']
			if titulo not in l:
				l.append(titulo)
				t.append('Título: <b>'+text+'</b>')
		elif findall(palavra,relatorio['date']):
			text = relatorio['date']
			if titulo not in l:
				l.append(titulo)
				t.append('Data: '+'<b>'+text+'</b>')

	dic = {"relatorios":l,"titulos":t}

	return json.dumps(dic)


# API Relatórios
@app.route('/api/relatorios', methods=['GET'])
def api_get_relatorios():
    ps = db.find_all()
    return json.dumps(ps)


@app.route('/api/relatorios', methods=['POST'])
def api_post_relatorio():
	data = dict(request.form)

	h = data['hashtags'].split(' ')
	l = data['references'].split(' ')

	data['references'] = l
	data['hashtags'] = h
	data['authors'] = [{'name': 'Beatriz Cepa', 'number': '83813', 'email': 'a83813@alunos.uminho.pt'}, 
	{'name': 'Beatriz Soares', 'number': '85815', 'email': 'a85815@alunos.uminho.pt'}]

	db.insert(data)

	return json.dumps(db.find_all())

@app.route('/api/relatorios/<titulo>', methods=['GET'])
def api_get_relatorio(titulo):
    p = db.find_one(titulo)
    return json.dumps(p) 


@app.route('/api/relatorios/<titulo>', methods=['POST'])
def api_delete_relatorio(titulo):

	p = db.delete(titulo)
	return json.dumps(p)


@app.route('/api/relatorios/hashtags', methods=['GET'])
def api_get_hashtags():

	titulos = db.find_all()

	h = []
	for titulo in titulos:
		relatorio = db.find_one(titulo)
		for tag in relatorio['hashtags']:
			if tag not in h:
				h.append(tag)

	return json.dumps(h)


# API Pessoas
@app.route('/api/pessoas', methods=['GET'])
def api_get_pessoas():
    ps = db.find_all_p()
    return json.dumps(ps)


@app.route('/api/pessoas/<nome>', methods=['GET'])
def api_get_pessoa(nome):
    p = db.find_one_p(nome)
    return json.dumps(p)