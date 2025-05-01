# -*- coding: utf-8 -*-

# Importa as classes necessárias da biblioteca reportlab
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Image, Table, TableStyle
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
import os

# Registrar as fontes CMU Serif (Computer Modern)
pdfmetrics.registerFont(TTFont('CMU-Roman', 'cmu.serif-roman.ttf'))
pdfmetrics.registerFont(TTFont('CMU-Bold', 'cmu.serif-bold.ttf'))
pdfmetrics.registerFont(TTFont('CMU-Italic', 'cmu.serif-italic.ttf'))

# --- Conteúdo Extraído do PDF ---
pages_content = [
"""
DomPII: Um Sistema de Aprendizado Autodidata com IA

Yan Vidal
contact@dompii.com
www.dompii.com

Resumo. DomPII é uma plataforma educacional open source baseada em
inteligência artificial, projetada para empoderar aprendizes autodidatas em
qualquer área do conhecimento. Combinando tecnologias de ponta como
LLMS, RAG, grafos de conhecimento e geração dinâmica de interfaces (via
MCPs), o sistema oferece uma jornada personalizada, interativa e
multimodal de aprendizagem. Mais que um ambiente de estudo, o DomPII
funciona como uma extensão do pensamento, permitindo ao usuário
navegar em seus próprios registros, conteúdos e conexões cognitivas por
meio de buscas inteligentes, linhas do tempo. e
visualizações
interdisciplinares. Com modos de aprendizado flexíveis (Especialista ou
Polímata), gamificação inteligente e um sistema de recompensas reais, o
DomPII transforma o ato de aprender em uma experiência criativa, livre e
estimulante onde o usuário não apenas absorve conhecimento, mas o
transforma.

1. Introdução

O DomPII é uma plataforma de aprendizagem autodidata baseada em
inteligência artificial, criada para oferecer uma nova forma de explorar,
construir e aplicar o conhecimento. Em vez de seguir trilhas rígidas de ensino,
Ο DomPII respeita a singularidade de cada aprendiz, proporcionando
flexibilidade, autonomia e personalização profunda do processo educacional.
No coração da plataforma está o uso inovador de Modelos de Linguagem de
Grande Escala (LLMs), que atuam não apenas como tutores inteligentes
capazes de explicar, questionar e avaliar, mas também como motores que
geram interfaces e experiências de aprendizagem completas.

Através de um sistema modular chamado MCP (Model Context Protocol), o próprio
modelo de IA constrói dinamicamente o front-end da aplicação, gerando páginas
interativas, multimodais e responsivas diretamente em HTML para
renderização em canvas, possibilitando uma liberdade inédita no design e na
estrutura das interações educacionais.

O DomPII transforma o ambiente de aprendizado em um espaço vivo e
expansível, onde o estudante pode subir documentos, vídeos e áudios que são
processados e incorporados à sua base de conhecimento pessoal. Essa base pode
ser consultada de forma natural via RAG (Retrieval-Augmented Generation),
grafos relacionais ou até uma linha do tempo interativa, permitindo não apenas
o estudo ativo, mas também o acesso contínuo ao próprio histórico intelectual
como se o sistema fosse uma extensão digital da mente.
Além disso, o DomPII integra mecânicas de gamificação, como sistemas de
frequência diaria e recompensas reais (gift cards, metas configuráveis e 
incentivos de amigos ou familiares), promovendo o engajamento sem abrir mão da
profundidade cognitiva. Desde o início, o usuário escolhe entre dois modos: o
modo Especialista, voltado para aprofundamento em uma área específica, ou o
modo Polímata, que incentiva a exploração transversal e interconectada de
múltiplos saberes.

2. Arquitetura do Sistema

Diagram.jpg
""",
"""
2.1. Frontend

O frontend do DomPII é intencionalmente minimalista, composto apenas por
um chat principal, um menu de configurações e uma área de canvas para
renderização HTML. Toda a complexidade das interfaces interativas é delegada
ao próprio modelo de linguagem, que gera dinamicamente o conteúdo visual e
funcional por meio das ferramentas MCP. Essa abordagem reduz
significativamente a necessidade de desenvolvimento manual de interfaces
tradicionais, permitindo que a IA componha páginas completas conforme o
contexto e os objetivos do usuário. Além disso, também é possível utilizar
layouts pré-definidos, que são dinamicamente preenchidos pela IA conforme a
necessidade. Os detalhes sobre esse processo de geração dinâmica estão
descritos no tópico 2.3, que aborda o funcionamento do MCP.

2.2. ΑΡΙ

A API do DomPII é baseada em arquitetura REST e oferece endpoints para
operações de CRUD voltadas à personalização do usuário e configurações do
sistema. É integrada ao protocolo MCP (Model Context Protocol), que atua
como intermediário entre a lógica do sistema e os modelos de linguagem,
utilizando a IA como motor principal de operação. A estrutura é compatível
com diferentes LLMs disponíveis no mercado, incluindo modelos abertos
executados localmente, desde que implementem suporte ao protocolo MCP.
Grande parte da comunicação entre frontend e backend ocorre por meio de
endpoints de streaming, conectando a interface do usuário às ferramentas MCP
de forma contínua, responsiva e multimodal.

2.3. MCP Servers

O Model Context Protocol (MCP) é um padrão criado pela Anthropic para
conectar modelos de linguagem a ferramentas externas por meio de uma
interface de comunicação unificada, funcionando como uma "porta USB" entre
o LLM e o ambiente de execução. No DomPII, o MCP é adotado como uma
camada fundamental que permite à IA operar diretamente sobre componentes
do sistema, sejam eles geradores de mídia, renderizadores de HTML, interfaces
visuais, ou manipuladores de banco de dados. Por meio do MCP, é possível definir 
formatos esperados de entrada e saída, bem como uma breve descrição do 
comportamento de cada ferramenta. Isso permite criar Ferramentas MCP que 
representam interfaces interativas ou blocos funcionais reutilizáveis.

Essas ferramentas podem ser pré-definidas ou geradas sob demanda pela IA, que 
compreende seus parâmetros e retorna a representação completa do conteúdo, normalmente 
em HTML pronto para ser renderizado no canvas. Quando uma interface requer 
manipulação de dados (como salvar progresso ou registrar ações do usuário), um 
segundo MCP pode ser encadeado ao primeiro, atuando como seu par lógico. O primeiro 
gera a interface e o prompt de ação; o segundo executa operações no banco de dados 
de acordo com os comandos embutidos no contexto.
Além disso, MCPs são utilizados para geração de conteúdos físicos e
digitais, como PDFs de exercícios para impressão, vídeos explicativos, áudios
ou imagens criadas dinamicamente para enriquecer o processo de aprendizado.

Inicialmente, essas ferramentas MCP precisam ser definidas manualmente,
mas o DomPII prevê o desenvolvimento de dois recursos chave: Um MCP expansível,
capaz de aceitar da IA não apenas os dados a serem preenchidos, mas também a 
descrição da interface, e um MCP genérico, projetado para registro e 
modificação de dados de forma universal, que poderá ser utilizado para a 
manipulação de qualquer tipo de dado que o MCP de interface dinamica necessitar.

Com esses recursos, torna-se possível eliminar a necessidade de desenvolver
novas interfaces manualmente, delegando à IA o papel de designer,
implementador e executor de funcionalidades visuais e operacionais, desde que
respeitados princípios formais e de segurança.
Esse modelo arquitetônico transforma o DomPII em um sistema modular,
flexível e altamente desacoplado. Cada funcionalidade é um MCP autônomo,
que pode ser adicionado, removido ou combinado com outros de maneira livre.
Isso reduz drasticamente a complexidade de manutenção e desenvolvimento, e
ao mesmo tempo abre espaço para um novo tipo de sistema educacional:
interconectado, fluido e talvez até caótico onde telas não seguem uma
hierarquia rígida, mas emergem como ambientes interativos que se conectam
dinamicamente, conforme a jornada de cada usuário.
Essa estrutura também habilita um altíssimo grau de personalização,
permitindo que cada usuário, ou mesmo cada comunidade, monte seu próprio
DomPII com conjuntos de ferramentas MCP que atendam seus estilos,
objetivos e temas preferidos, como um sistema educacional vivo, que se adapta
e se reconfigura à medida que aprende com quem o usa.
""",
"""
Exemplos de MCP:

Tipo de MCP            | Função Principal                           | Exemplos no DomPII
MCP de Interface       | Geração e preenchimento de interfaces HTML | Quiz, Mapa Mental, Linha do Tempo
MCP de Dados          | Manipulação de registros no banco de dados | Salvar respostas, Atualizar progresso
MCP de Geração de Mídias | Produção de conteúdos digitais baseados em contexto | PDFs de exercícios, Imagens de revisão
MCP de Interface Expandida | Criação dinâmica de novas interfaces via IA | Geração de telas sob demanda
MCP Genérico de Registros | Registro e modificação de dados universais | Registros imprevisíveis

Exemplo de fluxo de uso:

- O usuário solicita no chat um "teste sobre Inteligência Artificial".
- A API aciona o LLM, que identifica a necessidade de utilizar o MCP de Interface "Quiz Generator".
- O LLM acessa o MCP de geração de quiz e retorna para o frontend a página com o conteúdo preenchido com o tema solicitado.
- O usuário responde diretamente na interface renderizada, que se comunica com a API em linguagem natural.
- As respostas são enviadas novamente ao LLM, que as direciona para o MCP de Dados "Quiz Result Recorder".
- O sistema registra o desempenho do usuário no banco de dados.
""",
"""
2.4. Bancos de Dados

O DomPII utiliza diferentes bancos de dados, combinando suas características específicas 
para oferecer a flexibilidade, escalabilidade e separação de
responsabilidades necessárias para a proposta dinâmica do sistema.
O PostgreSQL, banco relacional, é utilizado para armazenar informações
mais estruturadas e estáveis, como perfis de usuários, configurações, permissões
e outros registros administrativos. Ele garante integridade referencial,
desempenho em consultas transacionais e segurança para os dados centrais que
sustentam a operação básica da plataforma.
O MongoDB é empregado para armazenar o conhecimento bruto gerado e
manipulado nas interfaces de aprendizado. Sua natureza orientada a
documentos e sem schema fixo permite que cada MCP defina livremente seus
próprios formatos de dados, mantendo a independência entre as ferramentas e
""",
"""
adaptando-se à diversidade das experiências de aprendizado.

Por fim, o Neo4j é utilizado para representar as relações entre conteúdos,
contextos e atividades através de grafos inteligentes. Esses grafos são
sintonizados com o apoio de algoritmos de IA, permitindo tanto que o sistema
construa trilhas de aprendizagem dinâmicas quanto que o próprio aprendiz
explore suas conexões cognitivas de maneiras personalizadas e visuais.
Essa combinação de bancos proporciona não apenas robustez e velocidade, mas
também abre caminhos para novas formas de interação com o
conhecimento, que serão aprofundadas nos tópicos seguintes.

2.5. Storage e RAG

O DomPII incorpora um sistema de armazenamento de documentos e mídias,
permitindo que o usuário envie conteúdos para complementar sua jornada de
aprendizado ou até mesmo construir trilhas formativas exclusivamente a
partir de seu próprio material.

Todo o conteúdo armazenado, assim como os registros de aprendizado
salvos no MongoDB e suas relações no Neo4j, pode ser embebido por meio de
técnicas de embedding, gerando uma representação vetorial única de cada
elemento de conhecimento. Esses vetores permitem que o sistema, utilizando
Retrieval-Augmented Generation (RAG), recupere informações relevantes de
maneira eficiente e semântica, respondendo a solicitações do usuário de forma
personalizada e contextualizada.
Essa arquitetura transforma o DomPII em uma verdadeira extensão da
memória do aprendiz, um segundo cérebro digital onde o conhecimento
não é apenas armazenado, mas também pode ser explorado de formas
inovadoras.

O acesso a esses conteúdos pode ocorrer através de diferentes MCPs visuais,
que representam o conhecimento sob diversas perspectivas, como em mapas
mentais, registros cronológicos interativos ou outras interfaces dinâmicas que
poderão ser continuamente desenvolvidas para enriquecer a experiência de
navegação e descoberta.

3. Gamificação

O DomPII incorpora elementos de gamificação para fortalecer o engajamento e
a continuidade da jornada de aprendizado dos usuários. Será implementado um
sistema de frequência diaria, que contabiliza a quantidade de dias consecutivos em que
""",
"""
o usuário interage com a plataforma, incentivando a criação de hábitos de
estudo consistentes. Essa dinâmica poderá ser explorada de diversas maneiras, incluindo a
integração com um sistema de recompensas semelhante a um cofre, onde prêmios são
armazenados e desbloqueados ao atingir metas específicas.

Os usuários poderão adicionar seus próprios gift cards ou receber contribuições de amigos e
familiares, configurando condições personalizadas para o resgate.
As metas para liberação das recompensas serão flexíveis, podendo incluir
critérios como a quantidade de dias consecutivos de uso, o tempo total
dedicado à plataforma, o avanço no conteúdo estudado, entre outras métricas
que poderão ser incorporadas conforme a evolução do sistema.
Esse mecanismo visa transformar o processo de aprendizagem em uma
experiência tangível de conquista, reforçando o ciclo de motivação e progresso
pessoal.

4. Limitações e Desafios

À medida que o volume de informações armazenadas pelo usuário cresce dentro
do sistema, pode se tornar desafiador para os modelos de linguagem lidarem
com contextos extensos de maneira eficiente. No entanto, a evolução contínua
dos LLMs, especialmente o aumento acelerado da janela de tokens,
combinada a boas práticas de representação e compressão de conhecimento,
permite mitigar significativamente essa limitação.

Outro desafio reside na natureza modular e ativa do DomPII. Usuários
acostumados a métodos tradicionais de aprendizagem, mais passivos e
linearmente estruturados, podem inicialmente estranhar a liberdade e a
dinâmica oferecidas pela plataforma. Contudo, a própria arquitetura modular
baseada em MCPs permite a criação de fluxos mais dirigidos e interfaces
adaptativas, oferecendo opções de navegação e estudo mais lineares para
aqueles que preferirem uma experiência de aprendizado mais convencional.
Esses fatores, longe de serem barreiras definitivas, são considerados
oportunidades de evolução contínua do sistema, tanto no suporte à diversidade
de perfis de aprendizes quanto na adoção das tecnologias mais avançadas em
processamento de linguagem.

5. Conclusão

O DomPII representa uma nova abordagem para plataformas de aprendizado:
""",
"""
mais aberta, flexível, profundamente integrada à evolução da inteligência
artificial e direcionada para o aprendizado ativo e independente, sem a necessidade
de instituições tradicionais. 

Ao estruturar seu núcleo em torno da modularidade, da
personalização e da autonomia do aprendiz, o sistema se posiciona não apenas
como uma ferramenta educacional, mas como uma extensão ativa do
pensamento e da construção de conhecimento.
Ao adotar conceitos como o Model Context Protocol, o uso de bancos de
dados especializados e a busca assistida por RAG, o DomPII oferece uma
arquitetura capaz de crescer organicamente com seus usuários e acompanhar os
avanços da IA de maneira contínua.

Embora desafios técnicos e pedagógicos estejam presentes, eles são
encarados como parte natural do processo de inovação. A flexibilidade do
sistema garante que ele possa se adaptar a novos modelos, novos perfis de
usuários e novas formas de explorar o conhecimento.
Com o DomPII, aprender deixa de ser apenas uma questão de acumular
informações: torna-se um ato criativo, dinâmico e pessoal onde cada jornada
é única, e onde cada conquista é também uma expansão real do que somos
capazes de conhecer e construir.
"""
]

# --- Definição de Estilos ---
styles = getSampleStyleSheet()

# Margens seguindo o estilo do Bitcoin whitepaper
left_margin = 1.5 * inch
right_margin = 1.46 * inch
top_margin = 1.3 * inch
bottom_margin = 1.0 * inch

# Modificar estilos existentes para usar as fontes CMU
styles['Normal'].fontName = 'CMU-Roman'
styles['Normal'].fontSize = 10
styles['Normal'].leading = 12
styles['Normal'].alignment = TA_JUSTIFY
styles['Normal'].firstLineIndent = 0
styles['Normal'].spaceAfter = 0

# Estilo para parágrafos com recuo na primeira linha (após o primeiro parágrafo)
styles.add(ParagraphStyle(
    name='NormalIndented',
    parent=styles['Normal'],
    firstLineIndent=24,  # Adiciona recuo na primeira linha dos parágrafos
))

styles['Title'].fontName = 'CMU-Bold'
styles['Title'].fontSize = 14
styles['Title'].leading = 16
styles['Title'].alignment = TA_CENTER
styles['Title'].spaceAfter = 6

styles['Heading1'].fontName = 'CMU-Bold'
styles['Heading1'].fontSize = 12
styles['Heading1'].leading = 14
styles['Heading1'].spaceBefore = 12
styles['Heading1'].spaceAfter = 6

styles['Heading2'].fontName = 'CMU-Bold'
styles['Heading2'].fontSize = 10
styles['Heading2'].leading = 12
styles['Heading2'].spaceBefore = 12
styles['Heading2'].spaceAfter = 6

# Adicionar estilos personalizados
# Estilo para informações do autor
styles.add(ParagraphStyle(
    name='Author',
    fontName='CMU-Roman',
    fontSize=10,
    leading=12,
    alignment=TA_CENTER,
    spaceAfter=0
))

# Estilo para texto itálico
styles.add(ParagraphStyle(
    name='ItalicText',  # Nome diferente para evitar conflitos
    fontName='CMU-Italic',
    fontSize=10,
    leading=12,
    alignment=TA_JUSTIFY
))

# Estilo para listas
styles.add(ParagraphStyle(
    name='ListItem',
    fontName='CMU-Roman',
    fontSize=10,
    leading=12,
    alignment=TA_JUSTIFY,
    leftIndent=20,
    bulletIndent=10
))


# Estilo para resumo
styles.add(ParagraphStyle(
    name='Abstract',
    fontName='CMU-Roman',
    fontSize=10,
    leading=11,
    alignment=TA_JUSTIFY,
    firstLineIndent=0,
    leftIndent=40,
    rightIndent=40
))

# --- Função para adicionar numeração de página ---
def add_page_number(canvas, doc):
    """Adiciona o número da página no rodapé, estilo Bitcoin whitepaper"""
    page_num = canvas.getPageNumber()
    text = "%d" % page_num
    canvas.saveState()
    canvas.setFont('CMU-Roman', 9)
    canvas.drawCentredString(letter[0]/2.0, 0.5 * inch, text)
    canvas.restoreState()

# --- Construção do Documento ---
output_filename = "dompii-whitepaper_pt.pdf"

# Define a personalização do canvas para adicionar metadados ao PDF
class PdfDocTemplate(SimpleDocTemplate):
    def __init__(self, *args, **kwargs):
        SimpleDocTemplate.__init__(self, *args, **kwargs)
        self.title = "DomPII: Um Sistema de Aprendizado Autodidata com IA"
        self.author = "Yan Vidal"
        self.subject = "Whitepaper DomPII"
        self.creator = "ReportLab PDF Library"
        self.producer = "ReportLab PDF Library"

    def handle_documentBegin(self):
        SimpleDocTemplate.handle_documentBegin(self)
        self.canv.setTitle(self.title)
        self.canv.setAuthor(self.author)
        self.canv.setSubject(self.subject)
        self.canv.setCreator(self.creator)
        self.canv.setProducer(self.producer)

doc = PdfDocTemplate(
    output_filename, 
    pagesize=letter,
    leftMargin=left_margin,
    rightMargin=right_margin,
    topMargin=top_margin,
    bottomMargin=bottom_margin
)

story = [] # Lista que conterá os elementos do PDF

# Processar todo o conteúdo de forma contínua
# Primeiro adicionar título e informações do autor
title_text = pages_content[0].strip().split('\n')[0]
author_name = pages_content[0].strip().split('\n')[2]
author_email = pages_content[0].strip().split('\n')[3]
author_website = pages_content[0].strip().split('\n')[4]

story.append(Paragraph(title_text, styles['Title']))
story.append(Spacer(1, 0.3*inch))
story.append(Paragraph(author_name, styles['Author']))
story.append(Paragraph(author_email, styles['Author']))
story.append(Paragraph(author_website, styles['Author']))
story.append(Spacer(1, 0.4*inch))

# Extrair e adicionar o resumo
abstract_text = ""
resumo_found = False
for line in pages_content[0].strip().split('\n'):
    if line.startswith("Resumo."):
        resumo_found = True
        # Manter a palavra "Resumo." no início, como no Bitcoin whitepaper
        abstract_text = line[8:].strip() + " "
    elif resumo_found and not line.strip():
        break
    elif resumo_found:
        abstract_text += line.strip() + " "

# Criar um parágrafo de resumo personalizado com "Resumo." em negrito
bold_abstract = Paragraph("<font face='CMU-Bold'>Resumo.</font> " + abstract_text, styles['Abstract'])
story.append(bold_abstract)
story.append(Spacer(1, 0.3*inch))

# Agora processar todo o conteúdo de forma contínua
current_paragraph = ""
in_abstract = True  # Começamos ignorando o resumo pois já foi processado
in_table_header = False
skip_lines = 0
is_first_paragraph_of_section = False  # Variável para controlar se estamos no primeiro parágrafo de uma seção

# Juntar todo o conteúdo em uma única lista de linhas
all_lines = []
for page in pages_content:
    lines = page.strip().split('\n')
    all_lines.extend(lines)

i = 0
while i < len(all_lines):
    line = all_lines[i]
    
    # Tratamento especial para a seção 2.4
    if line.strip() == '2.4. Bancos de Dados':
        # Adicionar o título da seção
        if current_paragraph:
            story.append(Paragraph(current_paragraph, styles['Normal']))
            current_paragraph = ""
        story.append(Paragraph(line, styles['Heading2']))
        
        # Pular linhas vazias até encontrar a primeira linha com conteúdo
        next_i = i + 1
        while next_i < len(all_lines) and not all_lines[next_i].strip():
            next_i += 1
        
        # Verificar se a próxima linha é a que esperamos para a seção 2.4
        if next_i < len(all_lines) and "utiliza diferentes bancos" in all_lines[next_i]:
            # Construir o primeiro parágrafo
            first_para = "O DomPII utiliza diferentes bancos de dados, combinando suas características específicas para oferecer a flexibilidade, escalabilidade e separação de responsabilidades necessárias para a proposta dinâmica do sistema."
            story.append(Paragraph(first_para, styles['Normal']))
            
            # Construir o segundo parágrafo sobre "O PostgreSQL"
            second_para = "O PostgreSQL, banco relacional, é utilizado para armazenar informações mais estruturadas e estáveis, como perfis de usuários, configurações, permissões e outros registros administrativos. Ele garante integridade referencial, desempenho em consultas transacionais e segurança para os dados centrais que sustentam a operação básica da plataforma."
            story.append(Paragraph(second_para, styles['NormalIndented']))
            
            # Construir o terceiro parágrafo sobre "O MongoDB"
            third_para = "O MongoDB é empregado para armazenar o conhecimento bruto gerado e manipulado nas interfaces de aprendizado. Sua natureza orientada a documentos e sem schema fixo permite que cada MCP defina livremente seus próprios formatos de dados, mantendo a independência entre as ferramentas e adaptando-se à diversidade das experiências de aprendizado."
            story.append(Paragraph(third_para, styles['NormalIndented']))
            
            # Avançar para depois da seção 2.4
            i = next_i + 12  # Pular aproximadamente para o próximo cabeçalho
            continue
    
    # Pular linhas vazias no início
    if i < 6:  # Pular título e informações do autor
        i += 1
        continue
    
    # Pular o resumo, pois já foi processado
    if line.startswith("Resumo."):
        in_abstract = True
        i += 1
        continue
    elif in_abstract:
        if not line.strip():
            in_abstract = False
        i += 1
        continue
    
    # Pular a tag de inserção do diagrama e inserir o diagrama
    if line.startswith("Diagram.jpg"):
        if current_paragraph:
            story.append(Paragraph(current_paragraph, styles['Normal']))
            current_paragraph = ""
        
        # Adicionar o diagrama
        diagram_path = "Diagram.png"
        if os.path.exists(diagram_path):
            img = Image(diagram_path, width=3.5*inch, height=3.5*inch)
            img.hAlign = 'CENTER'
            story.append(Spacer(1, 0.2*inch))
            story.append(img)
            story.append(Spacer(1, 0.2*inch))
        i += 1
        continue
    
    # Título de seção principal (ex: "3. Gamificação")
    if line.strip() and line.strip()[0].isdigit() and '. ' in line and '.' in line.strip()[:3]:
        if current_paragraph:
            story.append(Paragraph(current_paragraph, styles['Normal']))
            current_paragraph = ""
        story.append(Paragraph(line, styles['Heading1']))
        is_first_paragraph_of_section = True  # Marcar o próximo parágrafo como sendo o primeiro da seção
    
    # Subtítulo de seção (ex: "2.1. Frontend" ou "2.4. Bancos de Dados")
    elif line.strip() == "2.4. Bancos de Dados" or (line.strip() and '.' in line.strip()[:4] and line.strip()[0].isdigit() and 
          (line.strip()[2].isdigit() or (len(line.strip()) > 3 and '.' in line.strip()[2:4]))):
        # Imprimir detalhes quando encontrar um 2.x
        if line.strip().startswith("2."):
            print(f"DEBUGGER: Verificando linha '{line.strip()}' na posição {i}")
            print(f"DEBUGGER: Condições: isdigit[0]={line.strip()[0].isdigit()}, '.' in [:4]={'.' in line.strip()[:4]}")
            if len(line.strip()) > 2:
                print(f"DEBUGGER: isdigit[2]={line.strip()[2].isdigit() if len(line.strip()) > 2 else 'N/A'}")
            if len(line.strip()) > 3:
                print(f"DEBUGGER: '.' in [2:4]={'.' in line.strip()[2:4] if len(line.strip()) > 3 else 'N/A'}")
        if current_paragraph:
            story.append(Paragraph(current_paragraph, styles['Normal']))
            current_paragraph = ""
        story.append(Paragraph(line, styles['Heading2']))
        is_first_paragraph_of_section = True  # Marcar o próximo parágrafo como sendo o primeiro da seção
        print(f"DEBUGGER: Encontrado título {line.strip()} na linha {i}")
    
    # Linha em branco (separação de parágrafos)
    elif not line.strip():
        if current_paragraph:
            # Escolher o estilo apropriado baseado em se é o primeiro parágrafo após um título
            if is_first_paragraph_of_section:
                story.append(Paragraph(current_paragraph, styles['Normal']))
                is_first_paragraph_of_section = False  # Resetar a flag
            else:
                story.append(Paragraph(current_paragraph, styles['NormalIndented']))
            current_paragraph = ""
    
    # Item de lista com asterisco
    elif line.strip().startswith('*'):
        if current_paragraph:
            # Escolher o estilo apropriado baseado em se é o primeiro parágrafo após um título
            if is_first_paragraph_of_section:
                story.append(Paragraph(current_paragraph, styles['Normal']))
                is_first_paragraph_of_section = False  # Resetar a flag
            else:
                story.append(Paragraph(current_paragraph, styles['NormalIndented']))
            current_paragraph = ""
        
        item_text = line.strip()[1:].strip()
        story.append(Paragraph('• ' + item_text, styles['ListItem']))
    
    # Item de lista numerado (1., 2., etc) ou item com hífen (-) no início
    elif (line.strip() and line.strip()[0].isdigit() and line.strip()[1:].startswith('. ')) or line.strip().startswith('-'):
        # Finalizar parágrafo atual
        if current_paragraph:
            # Escolher o estilo apropriado baseado em se é o primeiro parágrafo após um título
            if is_first_paragraph_of_section:
                story.append(Paragraph(current_paragraph, styles['Normal']))
                is_first_paragraph_of_section = False  # Resetar a flag
            else:
                story.append(Paragraph(current_paragraph, styles['NormalIndented']))
            current_paragraph = ""
            
        # Formatar como item de lista (igual para todos)
        item_text = line.strip()
        story.append(Paragraph(item_text, styles['ListItem']))
    
    # Tabela
    elif line.strip().startswith('Tipo de MCP') and '|' in line:
        if current_paragraph:
            story.append(Paragraph(current_paragraph, styles['Normal']))
            current_paragraph = ""
        
        story.append(Spacer(1, 0.2*inch))
        
        # Título da tabela
        table_title = "Tabela 1: Exemplos de ferramentas MCP no DomPII"
        story.append(Paragraph(table_title, styles['ItalicText']))
        story.append(Spacer(1, 0.1*inch))
        
        # Coletar dados da tabela
        table_data = []
        header_line = line.strip()
        headers = [head.strip() for head in header_line.split('|')]
        
        # Adicionar cabeçalho com Paragraphs para formatação
        table_data.append([Paragraph(f"<b>{h}</b>", styles['Normal']) for h in headers if h])
        
        # Coletar as próximas linhas que contêm dados da tabela
        data_line_count = 0
        j = i + 1
        while j < len(all_lines) and data_line_count < 5:
            data_line = all_lines[j].strip()
            if '|' in data_line:
                cells = [cell.strip() for cell in data_line.split('|')]
                row_data = []
                for cell in cells:
                    if cell:  # Ignorar células vazias
                        row_data.append(Paragraph(cell, styles['Normal']))
                if row_data:
                    table_data.append(row_data)
                data_line_count += 1
            j += 1
        
        # Configurar larguras das colunas
        available_width = letter[0] - left_margin - right_margin
        col_widths = [available_width * 0.25, available_width * 0.40, available_width * 0.35]
        
        # Criar tabela
        table = Table(table_data, colWidths=col_widths)
        
        # Estilo da tabela
        table_style = TableStyle([
            ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
            ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
            ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'CMU-Bold'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
            ('TOPPADDING', (0, 0), (-1, 0), 8),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('ALIGN', (0, 1), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 1), (-1, -1), 'CMU-Roman'),
            ('BOTTOMPADDING', (0, 1), (-1, -1), 6),
            ('TOPPADDING', (0, 1), (-1, -1), 6),
        ])
        
        table.setStyle(table_style)
        story.append(table)
        story.append(Spacer(1, 0.2*inch))
        
        # Precisamos pular as linhas da tabela - agora baseado no número real de linhas encontradas
        in_table_header = True
        skip_lines = data_line_count + 1  # +1 para o cabeçalho
    
    # Título "Exemplo de fluxo de uso:"
    elif line.strip() == "Exemplo de fluxo de uso:":
        if current_paragraph:
            story.append(Paragraph(current_paragraph, styles['Normal']))
            current_paragraph = ""
        
        # Adicionar o título em itálico 
        story.append(Spacer(1, 0.2*inch))
        story.append(Paragraph("Exemplo de fluxo de uso:", styles['ItalicText']))
        story.append(Spacer(1, 0.1*inch))
        
        # Processar os itens do fluxo como parágrafos com fonte menor
        j = i + 1
        while j < len(all_lines) and j < i + 10:  # Verificar até 10 linhas à frente
            line_text = all_lines[j].strip()
            # Verificar se é um item numerado (1., 2., etc.)
            if line_text and line_text[0].isdigit() and line_text[1:].startswith('. '):
                # Adicionar como texto normal, com o mesmo estilo das listas
                story.append(Paragraph(line_text, styles['ListItem']))
                j += 1
            else:
                # Se não for um item numerado, sair do loop
                break
        
        # Pular as linhas já processadas
        i = j - 1
    
    # Texto normal - acumular para formar parágrafos
    else:
        if in_table_header:
            # Estamos no meio da tabela, então precisamos pular algumas linhas
            if skip_lines > 0:
                skip_lines -= 1
                if skip_lines == 0:
                    in_table_header = False
        elif "|" not in line:  # Ignorar linhas da tabela
            # Verificar se é a primeira linha após um título
            is_first_after_heading = False
            for j in range(i-1, max(0, i-5), -1):
                if j < len(all_lines):
                    prev_line = all_lines[j].strip()
                    if not prev_line:
                        continue  # Pular linhas em branco
                    if ((prev_line[0].isdigit() and '. ' in prev_line and '.' in prev_line[:3]) or  # Título principal
                        ('.' in prev_line[:4] and prev_line[0].isdigit() and prev_line[2].isdigit())): # Subtítulo
                        is_first_after_heading = True
                        for k in range(j+1, i):
                            if k < len(all_lines) and all_lines[k].strip() and not all_lines[k].strip().startswith("Diagram"):
                                is_first_after_heading = False
                                break
                        break
                    break
            
            # Se for a primeira linha de texto após um título e não tivermos texto acumulado, marcamos o parágrafo
            if is_first_after_heading and not current_paragraph:
                # Marcar como primeiro parágrafo da seção
                is_first_paragraph_of_section = True
            
            current_paragraph += line.strip() + " "
    
    i += 1

# Adiciona o último parágrafo pendente
if current_paragraph:
    # Escolher o estilo apropriado baseado em se é o primeiro parágrafo após um título
    if is_first_paragraph_of_section:
        story.append(Paragraph(current_paragraph, styles['Normal']))
    else:
        story.append(Paragraph(current_paragraph, styles['NormalIndented']))

# Constrói o PDF
try:
    doc.build(story, onFirstPage=add_page_number, onLaterPages=add_page_number)
    print(f"Documento PDF recriado com estilo do Bitcoin whitepaper como '{output_filename}' com sucesso.")
except Exception as e:
    print(f"Erro ao gerar o PDF '{output_filename}': {e}")