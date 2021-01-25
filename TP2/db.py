import shelve


# relatorios
def find_all():
    with shelve.open('relatorios.db') as s:
        return list(s.keys())


def find_one(titulo):
    with shelve.open('relatorios.db') as s:
        return s[titulo]


def insert(relatorio):
    with shelve.open('relatorios.db', writeback=True) as s:
        s[relatorio['title']] = relatorio
        return list(s.keys())

def delete(titulo):
    with shelve.open('relatorios.db', writeback=True) as s:
        del s[titulo]
        return list(s.keys())


# pessoas
def find_all_p():
    with shelve.open('pessoas.db') as p:
        return list(p.keys())


def find_one_p(nome):
    with shelve.open('pessoas.db') as p:
        return p[nome]

def insert_p(pessoa):
    with shelve.open('pessoas.db', writeback=True) as p:
        p[pessoa['nome']] = pessoa
        return list(p.keys())
