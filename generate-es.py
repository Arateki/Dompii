# -*- coding: utf-8 -*-

# Importa las clases necesarias de la biblioteca reportlab
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

# Registrar las fuentes CMU Serif (Computer Modern)
pdfmetrics.registerFont(TTFont('CMU-Roman', 'assets/cmu.serif-roman.ttf'))
pdfmetrics.registerFont(TTFont('CMU-Bold', 'assets/cmu.serif-bold.ttf'))
pdfmetrics.registerFont(TTFont('CMU-Italic', 'assets/cmu.serif-italic.ttf'))

# --- Contenido Extraído del PDF ---
pages_content = [
"""
DomPII: Un Sistema de Aprendizaje Autodidacta con IA

Yan Vidal
contact@dompii.com
www.dompii.com

Resumen. DomPII es una plataforma educativa open source basada en
inteligencia artificial, diseñada para empoderar a aprendices autodidactas en
cualquier área del conocimiento. Combinando tecnologías de vanguardia como
LLMs, RAG, grafos de conocimiento y generación dinámica de interfaces (vía
MCPs), el sistema ofrece un viaje de aprendizaje personalizado, interactivo y
multimodal. Más que un entorno de estudio, DomPII
funciona como una extensión del pensamiento, permitiendo al usuario
navegar por sus propios registros, contenidos y conexiones cognitivas
mediante búsquedas inteligentes, líneas de tiempo y
visualizaciones
interdisciplinarias. Con modos de aprendizaje flexibles (Experto o
Polímata), gamificación inteligente y un sistema de recompensas reales,
DomPII transforma el acto de aprender en una experiencia creativa, libre y
estimulante donde el usuario no solo absorbe conocimiento, sino que lo
transforma.

1. Introducción

DomPII es una plataforma de aprendizaje autodidacta basada en
inteligencia artificial, creada para ofrecer una nueva forma de explorar,
construir y aplicar el conocimiento. En lugar de seguir rutas rígidas de enseñanza,
DomPII respeta la singularidad de cada aprendiz, proporcionando
flexibilidad, autonomía y personalización profunda del proceso educativo.
En el corazón de la plataforma está el uso innovador de Modelos de Lenguaje de
Gran Escala (LLMs), que actúan no solo como tutores inteligentes
capaces de explicar, cuestionar y evaluar, sino también como motores que
generan interfaces y experiencias de aprendizaje completas.

A través de un sistema modular llamado MCP (Model Context Protocol), el propio
modelo de IA construye dinámicamente el front-end de la aplicación, generando páginas
interactivas, multimodales y responsivas directamente en HTML para
renderización en canvas, posibilitando una libertad sin precedentes en el diseño y
estructura de las interacciones educativas.

DomPII transforma el ambiente de aprendizaje en un espacio vivo y
expandible, donde el estudiante puede subir documentos, vídeos y audios que son
procesados e incorporados a su base de conocimiento personal. Esta base puede
ser consultada de forma natural vía RAG (Retrieval-Augmented Generation),
grafos relacionales o incluso una línea de tiempo interactiva, permitiendo no solo
el estudio activo, sino también el acceso continuo a su propio historial intelectual
como si el sistema fuera una extensión digital de la mente.
Además, DomPII integra mecánicas de gamificación, como sistemas de
racha diaria y recompensas reales (tarjetas de regalo, metas configurables e
incentivos de amigos o familiares), promoviendo el compromiso sin renunciar a la
profundidad cognitiva. Desde el inicio, el usuario elige entre dos modos: el
modo Experto, orientado a profundizar en un área específica, o el
modo Polímata, que incentiva la exploración transversal e interconectada de
múltiples saberes.

2. Arquitectura del Sistema

Diagram.jpg
""",
"""
2.1. Frontend

El frontend de DomPII es intencionalmente minimalista, compuesto solo por
un chat principal, un menú de configuraciones y un área de canvas para
renderización HTML. Toda la complejidad de las interfaces interactivas se delega
al propio modelo de lenguaje, que genera dinámicamente el contenido visual y
funcional mediante las herramientas MCP. Este enfoque reduce
significativamente la necesidad de desarrollo manual de interfaces
tradicionales, permitiendo que la IA componga páginas completas según el
contexto y los objetivos del usuario. Además, también es posible utilizar
layouts predefinidos, que son dinámicamente completados por la IA según la
necesidad. Los detalles sobre este proceso de generación dinámica están
descritos en el tema 2.3, que aborda el funcionamiento del MCP.

2.2. API

La API de DomPII está basada en arquitectura REST y ofrece endpoints para
operaciones de CRUD orientadas a la personalización del usuario y configuraciones del
sistema. Está integrada al protocolo MCP (Model Context Protocol), que actúa
como intermediario entre la lógica del sistema y los modelos de lenguaje,
utilizando la IA como motor principal de operación. La estructura es compatible
con diferentes LLMs disponibles en el mercado, incluyendo modelos abiertos
ejecutados localmente, siempre que implementen soporte al protocolo MCP.
Gran parte de la comunicación entre frontend y backend ocurre mediante
endpoints de streaming, conectando la interfaz del usuario a las herramientas MCP
de forma continua, responsiva y multimodal.

2.3. Servidores MCP

El Model Context Protocol (MCP) es un estándar creado por Anthropic para
conectar modelos de lenguaje a herramientas externas mediante una
interfaz de comunicación unificada, funcionando como un "puerto USB" entre
el LLM y el entorno de ejecución. En DomPII, el MCP se adopta como una
capa fundamental que permite a la IA operar directamente sobre componentes
del sistema, sean generadores de medios, renderizadores de HTML, interfaces
visuales, o manipuladores de bases de datos. A través del MCP, es posible definir
formatos esperados de entrada y salida, así como una breve descripción del
comportamiento de cada herramienta. Esto permite crear Herramientas MCP que
representan interfaces interactivas o bloques funcionales reutilizables.

Estas herramientas pueden ser predefinidas o generadas bajo demanda por la IA, que
comprende sus parámetros y devuelve la representación completa del contenido, normalmente
en HTML listo para ser renderizado en el canvas. Cuando una interfaz requiere
manipulación de datos (como guardar progreso o registrar acciones del usuario), un
segundo MCP puede ser encadenado al primero, actuando como su par lógico. El primero
genera la interfaz y el prompt de acción; el segundo ejecuta operaciones en la base de datos
de acuerdo con los comandos incluidos en el contexto.
Además, los MCPs se utilizan para generación de contenidos físicos y
digitales, como PDFs de ejercicios para impresión, vídeos explicativos, audios
o imágenes creadas dinámicamente para enriquecer el proceso de aprendizaje.

Inicialmente, estas herramientas MCP necesitan ser definidas manualmente,
pero DomPII prevé el desarrollo de dos recursos clave: Un MCP expandible,
capaz de aceptar de la IA no solo los datos a ser completados, sino también la
descripción de la interfaz, y un MCP genérico, diseñado para registro y
modificación de datos de forma universal, que podrá ser utilizado para la
manipulación de cualquier tipo de dato que el MCP de interfaz dinámica necesite.

Con estos recursos, se hace posible eliminar la necesidad de desarrollar
nuevas interfaces manualmente, delegando a la IA el papel de diseñador,
implementador y ejecutor de funcionalidades visuales y operacionales, siempre que
se respeten principios formales y de seguridad.
Este modelo arquitectónico transforma DomPII en un sistema modular,
flexible y altamente desacoplado. Cada funcionalidad es un MCP autónomo,
que puede ser añadido, removido o combinado con otros de manera libre.
Esto reduce drásticamente la complejidad de mantenimiento y desarrollo, y
al mismo tiempo abre espacio para un nuevo tipo de sistema educativo:
interconectado, fluido y tal vez hasta caótico donde las pantallas no siguen una
jerarquía rígida, sino que emergen como ambientes interactivos que se conectan
dinámicamente, según el viaje de cada usuario.
Esta estructura también habilita un altísimo grado de personalización,
permitiendo que cada usuario, o incluso cada comunidad, monte su propio
DomPII con conjuntos de herramientas MCP que atiendan sus estilos,
objetivos y temas preferidos, como un sistema educativo vivo, que se adapta
y se reconfigura a medida que aprende con quien lo usa.
""",
"""
Ejemplos de MCP:

Tipo de MCP          | Función Principal                           | Ejemplos en DomPII
MCP de Interfaz      | Generación y llenado de interfaces HTML     | Quiz, Mapa Mental, Línea de Tiempo
MCP de Datos         | Manipulación de registros en la base de datos | Guardar respuestas, Actualizar progreso
MCP de Generación de Medios | Producción de contenidos digitales basados en contexto | PDFs de ejercicios, Imágenes de revisión
MCP de Interfaz Expandida | Creación dinámica de nuevas interfaces vía IA | Generación de pantallas bajo demanda
MCP Genérico de Registros | Registro y modificación de datos universales | Registros imprevisibles

Ejemplo de flujo de uso:

- El usuario solicita en el chat un "test sobre Inteligencia Artificial".
- La API activa el LLM, que identifica la necesidad de utilizar el MCP de Interfaz "Generador de Quiz".
- El LLM accede al MCP de generación de quiz y devuelve al frontend la página con el contenido completado con el tema solicitado.
- El usuario responde directamente en la interfaz renderizada, que se comunica con la API en lenguaje natural.
- Las respuestas son enviadas nuevamente al LLM, que las dirige al MCP de Datos "Registrador de Resultados de Quiz".
- El sistema registra el desempeño del usuario en la base de datos.
""",
"""
2.4. Bases de Datos

DomPII utiliza diferentes bases de datos, combinando sus características específicas 
para ofrecer la flexibilidad, escalabilidad y separación de
responsabilidades necesarias para la propuesta dinámica del sistema.
PostgreSQL, base de datos relacional, se utiliza para almacenar información
más estructurada y estable, como perfiles de usuarios, configuraciones, permisos
y otros registros administrativos. Garantiza integridad referencial,
desempeño en consultas transaccionales y seguridad para los datos centrales que
sustentan la operación básica de la plataforma.
MongoDB se emplea para almacenar el conocimiento bruto generado y
manipulado en las interfaces de aprendizaje. Su naturaleza orientada a
documentos y sin esquema fijo permite que cada MCP defina libremente sus
propios formatos de datos, manteniendo la independencia entre las herramientas y
""",
"""
adaptándose a la diversidad de las experiencias de aprendizaje.

Finalmente, Neo4j se utiliza para representar las relaciones entre contenidos,
contextos y actividades a través de grafos inteligentes. Estos grafos son
sintonizados con el apoyo de algoritmos de IA, permitiendo tanto que el sistema
construya trayectorias de aprendizaje dinámicas como que el propio aprendiz
explore sus conexiones cognitivas de maneras personalizadas y visuales.
Esta combinación de bases de datos proporciona no solo robustez y velocidad, sino
también abre caminos para nuevas formas de interacción con el
conocimiento, que serán profundizadas en los temas siguientes.

2.5. Almacenamiento y RAG

DomPII incorpora un sistema de almacenamiento de documentos y medios,
permitiendo que el usuario envíe contenidos para complementar su jornada de
aprendizaje o incluso construir trayectorias formativas exclusivamente a
partir de su propio material.

Todo el contenido almacenado, así como los registros de aprendizaje
guardados en MongoDB y sus relaciones en Neo4j, puede ser incorporado mediante
técnicas de embedding, generando una representación vectorial única de cada
elemento de conocimiento. Estos vectores permiten que el sistema, utilizando
Retrieval-Augmented Generation (RAG), recupere informaciones relevantes de
manera eficiente y semántica, respondiendo a solicitudes del usuario de forma
personalizada y contextualizada.
Esta arquitectura transforma DomPII en una verdadera extensión de la
memoria del aprendiz, un segundo cerebro digital donde el conocimiento
no es solo almacenado, sino que también puede ser explorado de formas
innovadoras.

El acceso a estos contenidos puede ocurrir a través de diferentes MCPs visuales,
que representan el conocimiento bajo diversas perspectivas, como en mapas
mentales, registros cronológicos interactivos u otras interfaces dinámicas que
podrán ser continuamente desarrolladas para enriquecer la experiencia de
navegación y descubrimiento.

3. Gamificación

DomPII incorpora elementos de gamificación para fortalecer el compromiso y
la continuidad de la jornada de aprendizaje de los usuarios. Se implementará un
sistema de racha diaria, que contabiliza la cantidad de días consecutivos en que
""",
"""
el usuario interactúa con la plataforma, incentivando la creación de hábitos de
estudio consistentes. Esta dinámica podrá ser explorada de diversas maneras, incluyendo la
integración con un sistema de recompensas similar a una caja fuerte, donde premios son
almacenados y desbloqueados al alcanzar metas específicas.

Los usuarios podrán añadir sus propias tarjetas de regalo o recibir contribuciones de amigos y
familiares, configurando condiciones personalizadas para el rescate.
Las metas para liberación de las recompensas serán flexibles, pudiendo incluir
criterios como la cantidad de días consecutivos de uso, el tiempo total
dedicado a la plataforma, el avance en el contenido estudiado, entre otras métricas
que podrán ser incorporadas conforme a la evolución del sistema.
Este mecanismo busca transformar el proceso de aprendizaje en una
experiencia tangible de logro, reforzando el ciclo de motivación y progreso
personal.

4. Limitaciones y Desafíos

A medida que el volumen de información almacenada por el usuario crece dentro
del sistema, puede volverse desafiante para los modelos de lenguaje lidiar
con contextos extensos de manera eficiente. Sin embargo, la evolución continua
de los LLMs, especialmente el aumento acelerado de la ventana de tokens,
combinada con buenas prácticas de representación y compresión de conocimiento,
permite mitigar significativamente esta limitación.

Otro desafío reside en la naturaleza modular y activa de DomPII. Usuarios
acostumbrados a métodos tradicionales de aprendizaje, más pasivos y
linealmente estructurados, pueden inicialmente extrañar la libertad y la
dinámica ofrecidas por la plataforma. Sin embargo, la propia arquitectura modular
basada en MCPs permite la creación de flujos más dirigidos e interfaces
adaptativas, ofreciendo opciones de navegación y estudio más lineales para
aquellos que prefieran una experiencia de aprendizaje más convencional.
Estos factores, lejos de ser barreras definitivas, son considerados
oportunidades de evolución continua del sistema, tanto en el soporte a la diversidad
de perfiles de aprendices como en la adopción de las tecnologías más avanzadas en
procesamiento de lenguaje.

5. Conclusión

DomPII representa un nuevo enfoque para plataformas de aprendizaje:
""",
"""
más abierto, flexible, profundamente integrado a la evolución de la inteligencia
artificial y dirigido hacia el aprendizaje activo e independiente, sin la necesidad
de instituciones tradicionales.

Al estructurar su núcleo en torno a la modularidad, la
personalización y la autonomía del aprendiz, el sistema se posiciona no solo
como una herramienta educativa, sino como una extensión activa del
pensamiento y la construcción de conocimiento.
Al adoptar conceptos como el Model Context Protocol, el uso de bases de
datos especializadas y la búsqueda asistida por RAG, DomPII ofrece una
arquitectura capaz de crecer orgánicamente con sus usuarios y acompañar los
avances de la IA de manera continua.

Aunque desafíos técnicos y pedagógicos estén presentes, son
encarados como parte natural del proceso de innovación. La flexibilidad del
sistema garantiza que pueda adaptarse a nuevos modelos, nuevos perfiles de
usuarios y nuevas formas de explorar el conocimiento.
Con DomPII, aprender deja de ser apenas una cuestión de acumular
información: se convierte en un acto creativo, dinámico y personal donde cada jornada
es única, y donde cada logro es también una expansión real de lo que somos
capaces de conocer y construir.
"""
]

# --- Definición de Estilos ---
styles = getSampleStyleSheet()

# Márgenes siguiendo el estilo del whitepaper de Bitcoin
left_margin = 1.5 * inch
right_margin = 1.46 * inch
top_margin = 1.3 * inch
bottom_margin = 1.0 * inch

# Modificar estilos existentes para usar las fuentes CMU
styles['Normal'].fontName = 'CMU-Roman'
styles['Normal'].fontSize = 10
styles['Normal'].leading = 12
styles['Normal'].alignment = TA_JUSTIFY
styles['Normal'].firstLineIndent = 0
styles['Normal'].spaceAfter = 0

# Estilo para párrafos con sangría en la primera línea (después del primer párrafo)
styles.add(ParagraphStyle(
    name='NormalIndented',
    parent=styles['Normal'],
    firstLineIndent=24,  # Añade sangría en la primera línea de los párrafos
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

# Añadir estilos personalizados
# Estilo para información del autor
styles.add(ParagraphStyle(
    name='Author',
    fontName='CMU-Roman',
    fontSize=10,
    leading=12,
    alignment=TA_CENTER,
    spaceAfter=0
))

# Estilo para texto en cursiva
styles.add(ParagraphStyle(
    name='ItalicText',  # Nombre diferente para evitar conflictos
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


# Estilo para resumen
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

# --- Función para añadir numeración de página ---
def add_page_number(canvas, doc):
    """Añade el número de página en el pie de página, estilo del whitepaper de Bitcoin"""
    page_num = canvas.getPageNumber()
    text = "%d" % page_num
    canvas.saveState()
    canvas.setFont('CMU-Roman', 9)
    canvas.drawCentredString(letter[0]/2.0, 0.5 * inch, text)
    canvas.restoreState()

# --- Construcción del Documento ---
output_filename = "docs/dompii-whitepaper_es.pdf"

# Define la personalización del canvas para añadir metadatos al PDF
class PdfDocTemplate(SimpleDocTemplate):
    def __init__(self, *args, **kwargs):
        SimpleDocTemplate.__init__(self, *args, **kwargs)
        self.title = "DomPII: Un Sistema de Aprendizaje Autodidacta con IA"
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

story = [] # Lista que contendrá los elementos del PDF

# Procesar todo el contenido de forma continua
# Primero añadir título e información del autor
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

# Extraer y añadir el resumen
abstract_text = ""
abstract_found = False
for line in pages_content[0].strip().split('\n'):
    if line.startswith("Resumen."):
        abstract_found = True
        # Mantener la palabra "Resumen." al inicio, como en el whitepaper de Bitcoin
        abstract_text = line[8:].strip() + " "
    elif abstract_found and not line.strip():
        break
    elif abstract_found:
        abstract_text += line.strip() + " "

# Crear un párrafo de resumen personalizado con "Resumen." en negrita
bold_abstract = Paragraph("<font face='CMU-Bold'>Resumen.</font> " + abstract_text, styles['Abstract'])
story.append(bold_abstract)
story.append(Spacer(1, 0.3*inch))

# Ahora procesar todo el contenido de forma continua
current_paragraph = ""
in_abstract = True  # Comenzamos ignorando el resumen pues ya fue procesado
in_table_header = False
skip_lines = 0
is_first_paragraph_of_section = False  # Variable para controlar si estamos en el primer párrafo de una sección

# Unir todo el contenido en una única lista de líneas
all_lines = []
for page in pages_content:
    lines = page.strip().split('\n')
    all_lines.extend(lines)

i = 0
while i < len(all_lines):
    line = all_lines[i]
    
    # Tratamiento especial para la sección 2.4
    if line.strip() == '2.4. Bases de Datos':
        # Añadir el título de la sección
        if current_paragraph:
            story.append(Paragraph(current_paragraph, styles['Normal']))
            current_paragraph = ""
        story.append(Paragraph(line, styles['Heading2']))
        
        # Saltar líneas vacías hasta encontrar la primera línea con contenido
        next_i = i + 1
        while next_i < len(all_lines) and not all_lines[next_i].strip():
            next_i += 1
        
        # Verificar si la siguiente línea es la que esperamos para la sección 2.4
        if next_i < len(all_lines) and "utiliza diferentes bases" in all_lines[next_i]:
            # Construir el primer párrafo
            first_para = "DomPII utiliza diferentes bases de datos, combinando sus características específicas para ofrecer la flexibilidad, escalabilidad y separación de responsabilidades necesarias para la propuesta dinámica del sistema."
            story.append(Paragraph(first_para, styles['Normal']))
            
            # Construir el segundo párrafo sobre "PostgreSQL"
            second_para = "PostgreSQL, base de datos relacional, se utiliza para almacenar información más estructurada y estable, como perfiles de usuarios, configuraciones, permisos y otros registros administrativos. Garantiza integridad referencial, desempeño en consultas transaccionales y seguridad para los datos centrales que sustentan la operación básica de la plataforma."
            story.append(Paragraph(second_para, styles['NormalIndented']))
            
            # Construir el tercer párrafo sobre "MongoDB"
            third_para = "MongoDB se emplea para almacenar el conocimiento bruto generado y manipulado en las interfaces de aprendizaje. Su naturaleza orientada a documentos y sin esquema fijo permite que cada MCP defina libremente sus propios formatos de datos, manteniendo la independencia entre las herramientas y adaptándose a la diversidad de las experiencias de aprendizaje."
            story.append(Paragraph(third_para, styles['NormalIndented']))
            
            # Avanzar para después de la sección 2.4
            i = next_i + 12  # Saltar aproximadamente al siguiente encabezado
            continue
    
    # Saltar líneas vacías al inicio
    if i < 6:  # Saltar título e información del autor
        i += 1
        continue
    
    # Saltar el resumen, pues ya fue procesado
    if line.startswith("Resumen."):
        in_abstract = True
        i += 1
        continue
    elif in_abstract:
        if not line.strip():
            in_abstract = False
        i += 1
        continue
    
    # Saltar la etiqueta de inserción del diagrama e insertar el diagrama
    if line.startswith("Diagram.jpg"):
        if current_paragraph:
            story.append(Paragraph(current_paragraph, styles['Normal']))
            current_paragraph = ""
        
        # Añadir el diagrama
        diagram_path = "Diagram.png"
        if os.path.exists(diagram_path):
            img = Image(diagram_path, width=3.5*inch, height=3.5*inch)
            img.hAlign = 'CENTER'
            story.append(Spacer(1, 0.2*inch))
            story.append(img)
            story.append(Spacer(1, 0.2*inch))
        i += 1
        continue
    
    # Título de sección principal (ej: "3. Gamificación")
    if line.strip() and line.strip()[0].isdigit() and '. ' in line and '.' in line.strip()[:3]:
        if current_paragraph:
            story.append(Paragraph(current_paragraph, styles['Normal']))
            current_paragraph = ""
        story.append(Paragraph(line, styles['Heading1']))
        is_first_paragraph_of_section = True  # Marcar el siguiente párrafo como siendo el primero de la sección
    
    # Subtítulo de sección (ej: "2.1. Frontend" o "2.4. Bases de Datos")
    elif line.strip() == "2.4. Bases de Datos" or (line.strip() and '.' in line.strip()[:4] and line.strip()[0].isdigit() and 
          (line.strip()[2].isdigit() or (len(line.strip()) > 3 and '.' in line.strip()[2:4]))):
        # Imprimir detalles cuando encontrar un 2.x
        if line.strip().startswith("2."):
            print(f"DEBUGGER: Verificando línea '{line.strip()}' en la posición {i}")
            print(f"DEBUGGER: Condiciones: isdigit[0]={line.strip()[0].isdigit()}, '.' in [:4]={'.' in line.strip()[:4]}")
            if len(line.strip()) > 2:
                print(f"DEBUGGER: isdigit[2]={line.strip()[2].isdigit() if len(line.strip()) > 2 else 'N/A'}")
            if len(line.strip()) > 3:
                print(f"DEBUGGER: '.' in [2:4]={'.' in line.strip()[2:4] if len(line.strip()) > 3 else 'N/A'}")
        if current_paragraph:
            story.append(Paragraph(current_paragraph, styles['Normal']))
            current_paragraph = ""
        story.append(Paragraph(line, styles['Heading2']))
        is_first_paragraph_of_section = True  # Marcar el siguiente párrafo como siendo el primero de la sección
        print(f"DEBUGGER: Encontrado título {line.strip()} en la línea {i}")
    
    # Línea en blanco (separación de párrafos)
    elif not line.strip():
        if current_paragraph:
            # Elegir el estilo apropiado basado en si es el primer párrafo después de un título
            if is_first_paragraph_of_section:
                story.append(Paragraph(current_paragraph, styles['Normal']))
                is_first_paragraph_of_section = False  # Resetear la bandera
            else:
                story.append(Paragraph(current_paragraph, styles['NormalIndented']))
            current_paragraph = ""
    
    # Ítem de lista con asterisco
    elif line.strip().startswith('*'):
        if current_paragraph:
            # Elegir el estilo apropiado basado en si es el primer párrafo después de un título
            if is_first_paragraph_of_section:
                story.append(Paragraph(current_paragraph, styles['Normal']))
                is_first_paragraph_of_section = False  # Resetear la bandera
            else:
                story.append(Paragraph(current_paragraph, styles['NormalIndented']))
            current_paragraph = ""
        
        item_text = line.strip()[1:].strip()
        story.append(Paragraph('• ' + item_text, styles['ListItem']))
    
    # Ítem de lista numerado (1., 2., etc) o ítem con guión (-) al inicio
    elif (line.strip() and line.strip()[0].isdigit() and line.strip()[1:].startswith('. ')) or line.strip().startswith('-'):
        # Finalizar párrafo actual
        if current_paragraph:
            # Elegir el estilo apropiado basado en si es el primer párrafo después de un título
            if is_first_paragraph_of_section:
                story.append(Paragraph(current_paragraph, styles['Normal']))
                is_first_paragraph_of_section = False  # Resetear la bandera
            else:
                story.append(Paragraph(current_paragraph, styles['NormalIndented']))
            current_paragraph = ""
            
        # Formatear como ítem de lista (igual para todos)
        item_text = line.strip()
        story.append(Paragraph(item_text, styles['ListItem']))
    
    # Tabla
    elif line.strip().startswith('Tipo de MCP') and '|' in line:
        if current_paragraph:
            story.append(Paragraph(current_paragraph, styles['Normal']))
            current_paragraph = ""
        
        story.append(Spacer(1, 0.2*inch))
        
        # Título de la tabla
        table_title = "Tabla 1: Ejemplos de herramientas MCP en DomPII"
        story.append(Paragraph(table_title, styles['ItalicText']))
        story.append(Spacer(1, 0.1*inch))
        
        # Recopilar datos de la tabla
        table_data = []
        header_line = line.strip()
        headers = [head.strip() for head in header_line.split('|')]
        
        # Añadir encabezado con Paragraphs para formateo
        table_data.append([Paragraph(f"<b>{h}</b>", styles['Normal']) for h in headers if h])
        
        # Recopilar las siguientes líneas que contienen datos de la tabla
        data_line_count = 0
        j = i + 1
        while j < len(all_lines) and data_line_count < 5:
            data_line = all_lines[j].strip()
            if '|' in data_line:
                cells = [cell.strip() for cell in data_line.split('|')]
                row_data = []
                for cell in cells:
                    if cell:  # Ignorar celdas vacías
                        row_data.append(Paragraph(cell, styles['Normal']))
                if row_data:
                    table_data.append(row_data)
                data_line_count += 1
            j += 1
        
        # Configurar anchos de las columnas
        available_width = letter[0] - left_margin - right_margin
        col_widths = [available_width * 0.25, available_width * 0.40, available_width * 0.35]
        
        # Crear tabla
        table = Table(table_data, colWidths=col_widths)
        
        # Estilo de la tabla
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
        
        # Necesitamos saltar las líneas de la tabla - ahora basado en el número real de líneas encontradas
        in_table_header = True
        skip_lines = data_line_count + 1  # +1 para el encabezado
    
    # Título "Ejemplo de flujo de uso:"
    elif line.strip() == "Ejemplo de flujo de uso:":
        if current_paragraph:
            story.append(Paragraph(current_paragraph, styles['Normal']))
            current_paragraph = ""
        
        # Añadir el título en cursiva 
        story.append(Spacer(1, 0.2*inch))
        story.append(Paragraph("Ejemplo de flujo de uso:", styles['ItalicText']))
        story.append(Spacer(1, 0.1*inch))
        
        # Procesar los ítems del flujo como párrafos con fuente menor
        j = i + 1
        while j < len(all_lines) and j < i + 10:  # Verificar hasta 10 líneas adelante
            line_text = all_lines[j].strip()
            # Verificar si es un ítem con guión (-)
            if line_text and line_text.startswith('-'):
                # Añadir como texto normal, con el mismo estilo de las listas
                story.append(Paragraph(line_text, styles['ListItem']))
                j += 1
            else:
                # Si no es un ítem con guión, salir del bucle
                break
        
        # Saltar las líneas ya procesadas
        i = j - 1
    
    # Texto normal - acumular para formar párrafos
    else:
        if in_table_header:
            # Estamos en medio de la tabla, así que necesitamos saltar algunas líneas
            if skip_lines > 0:
                skip_lines -= 1
                if skip_lines == 0:
                    in_table_header = False
        elif "|" not in line:  # Ignorar líneas de la tabla
            # Verificar si es la primera línea después de un título
            is_first_after_heading = False
            for j in range(i-1, max(0, i-5), -1):
                if j < len(all_lines):
                    prev_line = all_lines[j].strip()
                    if not prev_line:
                        continue  # Saltar líneas en blanco
                    if ((prev_line[0].isdigit() and '. ' in prev_line and '.' in prev_line[:3]) or  # Título principal
                        ('.' in prev_line[:4] and prev_line[0].isdigit() and prev_line[2].isdigit())): # Subtítulo
                        is_first_after_heading = True
                        for k in range(j+1, i):
                            if k < len(all_lines) and all_lines[k].strip() and not all_lines[k].strip().startswith("Diagram"):
                                is_first_after_heading = False
                                break
                        break
                    break
            
            # Si es la primera línea de texto después de un título y no tenemos texto acumulado, marcamos el párrafo
            if is_first_after_heading and not current_paragraph:
                # Marcar como primer párrafo de la sección
                is_first_paragraph_of_section = True
            
            current_paragraph += line.strip() + " "
    
    i += 1

# Añadir el último párrafo pendiente
if current_paragraph:
    # Elegir el estilo apropiado basado en si es el primer párrafo después de un título
    if is_first_paragraph_of_section:
        story.append(Paragraph(current_paragraph, styles['Normal']))
    else:
        story.append(Paragraph(current_paragraph, styles['NormalIndented']))

# Construir el PDF
try:
    doc.build(story, onFirstPage=add_page_number, onLaterPages=add_page_number)
    print(f"Documento PDF recreado con estilo del whitepaper de Bitcoin como '{output_filename}' con éxito.")
except Exception as e:
    print(f"Error al generar el PDF '{output_filename}': {e}")