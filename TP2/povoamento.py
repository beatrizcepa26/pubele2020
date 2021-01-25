
relatorios = [
	{'title': 'ENCAPSULATION ANALYSIS', 'date': '17 novembro 2020', 'uc': 
	'Comunicações e Redes', 'authors': [{'name': 'Beatriz Cepa', 'number': '83813', 
	'email': 'a83813@alunos.uminho.pt'}, {'name': 'Beatriz Soares', 'number': '85815', 
	'email': 'a85815@alunos.uminho.pt'}], 'format': 'https://github.com/beatrizcepa26/pubele2020/blob/main/TP1/report4.pdf',  
	'description': '''O Wireshark é um programa capaz de monitorizar os pacotes que atravessam uma interface de rede de um 
  computador (host). Esta ferramenta captura o tráfego da rede local e armazena esses dados para análise offline.
	A figura exemplifica técnicas de encapsulamento, tomando como base o envio /receção de uma Mensagem Aplicacional HTTP. 
  A mensagem é enviada de cima para baixo, ou seja, desde o HTTP atravessa as restantes camadas: de transporte (segmento TCP), 
  de rede (pacote IP) e, finalmente, a camada física, Ethernet. Cada camada introduz o seu próprio Cabeçalho (Header), o que 
  implica a introdução de um overhead adicional aos dados (Payload) disponibilizados na camada acima. Esses cabeçalhos contêm 
  informações que são úteis aos vários protocolos, por exemplo, na camada de rede, é introduzido o cabeçalho IP que tem informações 
  como o endereço IP, o TTL do pacote e o número de saltos. A mensagem, depois de recebida, faz o percurso inverso. Assim, o 
  encapsulamento consiste na passagem da mensagem pelas várias camadas, sendo-lhe adicionados os vários cabeçalhos à medida que 
  atravessa cada uma delas
	Assim, no que diz respeito à articulação entre camadas, tem-se que [1]: 
	cada camada superior faz uso dos serviços da camada inferior e presta serviços à de cima; 
	quando uma camada recebe dados da camada acima, a existência de um protocolo obriga à adição    
	de informação de controlo com um determinado tamanho, que implica a introdução de um overhead 
	adicional aos dados;o resultado obtido é enviado para a camada abaixo; esse processo 
	de adicionar informação ao passar pelas diversas camadas chama-se encapsulamento;
	do lado do recetor, este processo é inverso e chama-se desencapsulamento.
	Esta disposição em camadas permite que um nível possa controlar também a informação tratada 
	num nível mais baixo, o que implica maior qualidade nos serviços oferecidos pela rede. 
	Esta é uma das vantagens das técnicas de encapsulamento. Existem outras como [1]: a 
	decomposição das comunicações de redes em partes menores, facilitando a sua aprendizagem e 
	compreensão; facilita a programação modular (independente), evitando que modificações numa 
	camada afetem outras; permite a comunicação entre diferentes sistemas; adoção de normas 
	(standards de protocolos).
	Pode considerar-se as normas ou protocolos um mal necessário pois, se é bom que elas 
	garantam que máquinas de diferentes fabricantes possam comunicar entre si, normalmente, a 
	definição de normas é um processo lento. Porém, elas são importantes, pois na comunicação são 
	necessárias regras que definam o que fazer em determinada situação e procedimentos que 
	determinem o caminho a dar a determinada informação. Porém, a introdução dos cabeçalhos que 
	contêm informações úteis aos vários protocolos, IP, TCP, etc., tem um custo, o tal overhead. 
	Ora, a introdução de cabeçalhos demasiado grandes para o tamanho da mensagem faz com que o 
	rendimento da transmissão seja baixo, isto é, o tamanho dos dados efetivamente úteis (os bytes 
	da mensagem aplicacional) é pequeno quando comparado com o tamanho de overhead que lhe foi 
	adicionado (Payload). Isto é o que acontece no caso da frame 43, cujo rendimento de transmissão é de apenas
	4 %, aproximadamente. Ou seja, se o tamanho da informação necessária para enviar uma mensagem 
	é maior do que o tamanho da própria mensagem, a transmissão não é rentável. Esta é uma das 
	desvantagens e quiçá a mais importante, associada às técnicas de encapsulamento. Por outro lado,
	para mensagens grandes, isto é, cujo tamanho seja superior à carga de transmissão de dados, 
	o rendimento de transmissão é alto. Isto é o que acontece no caso da frame 56, cujo rendimento 
	de transmissão é de 95 %.''',
	'image':'https://raw.githubusercontent.com/beatrizcepa26/pubele2020/main/TP1/imagem_report4.JPG',
	'hashtags': ['#encapsulamento'],
	'references':['https://tozehgamer.wordpress.com/vantagens-do-modelo-ozi-e-articulacao-entre-camadas/']},
	
	{'title': 'INTERNET INTRODUCTION AND SATELLITE COMMUNICATIONS', 'date': '27 outubro 2020', 'uc': 
	'Comunicações e Redes', 'authors': [{'name': 'Beatriz Cepa', 'number': '83813', 
	'email': 'a83813@alunos.uminho.pt'}, {'name': 'Beatriz Soares', 'number': '85815', 
	'email': 'a85815@alunos.uminho.pt'}], 'format': 'https://github.com/beatrizcepa26/pubele2020/blob/main/TP1/report1.pdf',  
	'description': '''Os satélites GORIZONT 29 e NILESAT 201 são classificados como TV Satellites (satélites TV), ou seja, 
  são geostacionários e transmitem sinais TV, além de serem usados para fins de comunicação global e 
  previsão meteorológica [1]. Os satélites geostacionários de comunicação são úteis, uma vez que são 
  visíveis numa grande área da superfície terrestre, e aparentam estar estacionários no céu, o que elimina 
  a necessidade de as antenas no solo se moverem. Ou seja, os observadores na Terra podem simplesmente 
  erguer antenas estacionárias, e estas ficam sempre direcionadas para o satélite pretendido. No entanto, 
  a latência nestes casos torna-se significativa (cerca de 240ms), o que é um problema para aplicações 
  sensíveis à latência, como as comunicações por voz. Além disso, à medida que a latitude do observador 
  aumenta, a comunicação torna-se mais difícil, devido a fatores como a refração atmosférica e reflexões 
  de sinal do solo ou estruturas próximas. Por isso, os satélites geostacionários de comunicação são usados 
  principalmente para entretenimento unidirecional e em aplicações nas quais alternativas de baixa latência 
  não estão disponíveis [2].
  Por sua vez, os satélites IRIDIUM 166 e ORBCOMM FM 15 são satélites de baixa órbita (LEO) [1]. Este tipo 
  de órbita exige menor quantidade de energia para colocação dos satélites no sítio pretendido e fornece 
  elevada largura de banda e baixa latência na comunicação. Mais ainda, como é necessária menos energia para 
  colocar um satélite numa órbita baixa, um satélite nessa órbita necessita de amplificadores menos eficazes 
  para que uma transmissão seja bem-sucedida. Este tipo de órbita é usado para várias aplicações na comunicação, 
  nomeadamente telecomunicações, como o Sistema Telefónico Iridium (usado para comunicações de voz e dados ao redor 
  do mundo através da rede de satélites Iridium, da qual o IRIDIUM 166 faz parte) [3]. Além disso, os sistemas 
  de telecomunicações baseados nos satélites de baixa altitude fornecem aos países subdesenvolvidos a capacidade 
  de adquirirem serviços telefónicos por satélite em áreas onde, de outra forma, seria muito dispendioso ou até 
  impossível estabelecer linhas terrestres.''',
	'image':'https://raw.githubusercontent.com/beatrizcepa26/pubele2020/main/TP1/imagem_report1.JPG',
	'hashtags': ['#satélites','#comunicações'],
	'references':['https://www.n2yo.com/','https://en.wikipedia.org/wiki/Geostationary_orbit',
  'https://pt.wikipedia.org/wiki/Request_for_Comments']},

	{'title': 'INTERNET PATHS AND DELAYS', 'date': '03 novembro 2020', 'uc': 
	'Comunicações e Redes', 'authors': [{'name': 'Beatriz Cepa', 'number': '83813', 
	'email': 'a83813@alunos.uminho.pt'}, {'name': 'Beatriz Soares', 'number': '85815', 
	'email': 'a85815@alunos.uminho.pt'}], 'format': 'https://github.com/beatrizcepa26/pubele2020/blob/main/TP1/report2.pdf',  
	'description': '''O Traceroute é um comando de monotorização comumente utilizado por administradores de rede e de sistemas 
  nas suas operações diárias. Esta ferramenta básica de diagnóstico de rede tem três objetivos principais, que 
  fornecem uma compreensão precisa e completa de um problema de rede. O Traceroute envia vários pacotes de dados 
  para um endereço de destino especificado e regista cada router (ou ponto intermediário) pelo qual os dados passam. 
  Cada router encontrado representa um salto (hop). É comum que os dados tenham vários saltos antes de chegarem ao 
  seu destino. Por exemplo, se a origem do path for em Braga, Portugal e o destino em Miami, na Califórnia, o Traceroute 
  identificará o caminho completo, cada salto no caminho e o tempo que demora a ir e voltar.
  É também importante referir que cada pacote IP enviado pela Internet possui um campo conhecido como Time-To-Live (TTL). 
  Este corresponde ao número máximo de saltos que um pacote pode dar pela Internet antes de ser descartado. O campo TTL num 
  pacote IP é essencial, porque, se não houvesse um, o pacote continuaria a fluir de um router para outro para sempre à procura 
  do seu destino, naquilo que seria designado por um loop infinito. Assim, o Traceroute depende do TTL para medir a distância 
  entre a origem e o destino e encontrar os saltos entre eles.
  Ora, como foi dito no início, o Traceroute é ferramenta de diagnóstico que fornece uma compreensão precisa 
  e completa de um problema de rede. Assim, os tempos rtt são os parâmetros mais importantes ao avaliar um Traceroute. 
  Tempos consistentes são o que se deve procurar. Pode haver saltos abruptos com tempos de latência maiores, mas isso pode 
  não indicar um problema; o importante é observar um padrão. Por exemplo, se ocorrer um aumento repentino de rtt num salto e 
  este continuar a aumentar até ao destino (se chegar lá), isso pode indicar um problema que começa no salto onde se verificou 
  esse aumento. Consequentemente, pode verificar-se a perda de pacotes (*) no relatório. Outro exemplo é a alta latência nos saltos 
  iniciais, o que pode indicar um possível problema ao nível da rede local [1]. É na avaliação de situações como as destes exemplos 
  que o Traceroute é extremamente útil.''',
	'image':'https://raw.githubusercontent.com/beatrizcepa26/pubele2020/main/TP1/imagem_report2.JPG',
	'hashtags': ['#traceroute'],
	'references':['https://www.inmotionhosting.com/support/website/ssh/read-traceroute/']},

	{'title': 'DATA TRANSMISSION AND DELAYS', 'date': '10 novembro 2020', 'uc': 
	'Comunicações e Redes', 'authors': [{'name': 'Beatriz Cepa', 'number': '83813', 
	'email': 'a83813@alunos.uminho.pt'}, {'name': 'Beatriz Soares', 'number': '85815', 
	'email': 'a85815@alunos.uminho.pt'}], 'format': 'https://github.com/beatrizcepa26/pubele2020/blob/main/TP1/report3.pdf',  
	'description': '''Neste trabalho prático, lidamos com dois tipos de atrasos: o atraso de transmissão, que corresponde ao tempo 
  necessário para transmitir todos os bits do pacote, ou seja, é dado pelo quociente entre o tamanho do pacote, em bits, e a taxa de 
  transmissão em bits por segundo; e o atraso de propagação, que é o tempo necessário para que cada bit se propague até ao 
  destino. Desta forma, este é obtido pelo quociente da distância entre a fonte e o destino e a velocidade de propagação. Da soma 
  destes dois atrasos resulta o atraso total ou também chamado end-to-end delay.
  Tendo em conta o que acabamos de definir, é bastante intuitivo perceber que, quanto maior for o tamanho do pacote a enviar, 
  para uma velocidade de transmissão constante, maior será o atraso de transmissão. Porém, o tamanho do pacote não tem influência 
  sobre o atraso de propagação, uma vez que esse, para uma dada velocidade de propagação, apenas depende da distância entre fonte e 
  destino. Ou seja, para 1 bit na fonte o atraso de propagação é exatamente o mesmo que ter 100 bits na fonte.
  Também importante comparar a situação em que temos apenas uma ligação entre fonte e destino e é enviado um só 
  pacote, com a situação em que existem duas ligações entre fonte e destino com um router a conectá-las, mais uma vez, 
  sendo enviado um só pacote. Ora, na primeira situação, o pacote “viaja” diretamente da fonte para o destino, sendo que o delay de 
  transmissão é proporcional ao tamanho do pacote enviado, e igual a 3s. Porém, na segunda situação, o pacote 
  primeiro “viaja” desde fonte até ao router e, só depois de toda a informação ter chegado a este, é que o pacote é transmitido para 
  o destino. Logo, o delay de transmissão duplica: são precisos 3s para o pacote ser transmitido até ao router, e mais 3s para a 
  informação ser transmitida do router até ao destino, perfazendo um total de 6s de delay de transmissão. No entanto, no que toca ao 
  delay de propagação, este é igual nas duas situações (0,05s), pois este, para a mesma velocidade de propagação, só depende da 
  distância entre a fonte e o destino, que, em ambas as situações, é de 10 000 km.
  Na transmissão store and forward, os pacotes são recebidos e armazenados na memória de um router e, depois de 
  inspecionados em busca de erros, sãoencaminhados para o destino seguinte. O envio de informação por pacotes, também designado por 
  packet switching tem vantagens como: ser ideal para dados, eventuais erros poderem ser recuperados no enlace onde ocorreram e o 
  facto de dividir uma mensagem em pacotes e transmiti-los simultaneamente reduzir o atraso de transmissão total da mensagem [1].''',
	'image':'https://raw.githubusercontent.com/beatrizcepa26/pubele2020/main/TP1/imagem_report2.JPG',
	'hashtags': ['#traceroute'],
	'references':['https://www.inmotionhosting.com/support/website/ssh/read-traceroute/']}

]


pessoas = [
    {'nome': 'Beatriz Soares','facebook':'https://www.facebook.com/Beatrizps99/','twitter':'https://twitter.com/Beatriz63678471',
    'interesses':'''Desde de sempre gostei de computadores, por causa de jogos principalmente. 
    No primeiro ano da universidade, programação foi um pesadelo e pensei que nunca seria capaz de 
    gostar disto. Pois bem...enganei-me. Os biomédicos são um autêntico "faz tudo" e como eu sempre
    gostei de tudo um pouco, mas de nada o suficiente, o curso de Engenharia Biomédica tem tudo a 
    ver comigo.''','ramo':'Finalmente, a aprender a programar a sério :)',
    'mestrado':'''Bem, como resumir...tantas cadeiras, tantos professores. Agora que fiz a minha 
    escolha, lamento bastante não ter tido a oportunidade de ter mais cadeiras relacionadas com a 
    informática :( Mas, pronto...já a minha avó dizia que "o saber não ocupa espaço" e, no meio de 
    tantas cadeiras que me possam parecer inúteis, sei seguramente muito mais do que sabia quando 
    entrei para o curso.''','escola':'Escola Secundária Carlos Amarante',
    'link_escola':'https://aecarlosamarante.pt/',
    'secundario':'''Que dizer...uma etapa que já vai longe, mas que deixa saudades, pois, para dizer 
    a verdade, foi das mais felizes da minha vida. Quem não gostaria de voltar para o secundário? :)''',
    'imagem':"https://raw.githubusercontent.com/beatrizcepa26/pubele2020/main/TP2/bia.jpg"
    },

    {'nome': 'Beatriz Cepa','facebook':'https://www.facebook.com/beatriz.cepa','twitter':'',
    'interesses':'''Música: sempre adorei música, e isso levou a que me inscrevesse numa escola de música.
    Estudei piano durante 5 anos e gostei tanto que tocar piano se tornou, sem dúvida, num dos meus hobbies.
    Leitura: desde que me conheço que adoro ler. Quando começo um livro, não descanso enquanto não o acabar.
    Romances históricos e policiais estão definitivamente no topo da minha lista de géneros favoritos. 
    Informática: na verdade só descobri que gostava desta área a meio do 2º ano do curso, mas a partir daí 
    fui ganhando cada vez mais vontade de trabalhar nela.''', 'ramo':'''Incrível. Tenho cada vez mais a certeza 
    de que estou na área certa para mim.''', 
    'mestrado':'''3 anos completamente multidisciplinares, em que aprendi um pouco 
    de tudo. Fiquei, definitivamente,com as bases necessárias para trabalhar em qualquer área. Quando comecei a 
    gostar da área de Informática, facilmente comecei a excluir das minhas opções de Mestrado as outras áreas do 
    curso, pelo que a escolha do ramo tornou-se óbvia para mim.''', 
    'escola':'Escola Secundária c/ 3º ciclo Henrique Medina',
    'link_escola':'https://www.escolahenriquemedina.org/',
    'secundario':'''Uma época que deixa muitas saudades, e na qual evoluí muito a nível académico e pessoal.''',
    'imagem':"https://raw.githubusercontent.com/beatrizcepa26/pubele2020/main/TP2/bea.JPG"
    }
]