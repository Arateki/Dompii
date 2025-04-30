# -*- coding: utf-8 -*-

# Import necessary classes from reportlab library
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Image, Table, TableStyle
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

# Register CMU Serif fonts (Computer Modern)
pdfmetrics.registerFont(TTFont('CMU-Roman', 'cmu.serif-roman.ttf'))
pdfmetrics.registerFont(TTFont('CMU-Bold', 'cmu.serif-bold.ttf'))
pdfmetrics.registerFont(TTFont('CMU-Italic', 'cmu.serif-italic.ttf'))

# --- Content Extracted from PDF ---
pages_content = [
"""
DomPII: A Self-Learning System with AI

Yan Vidal
contact@dompii.com
www.dompii.com

Abstract. DomPII is an open source educational platform based on
artificial intelligence, designed to empower self-taught learners in
any field of knowledge. Combining cutting-edge technologies such as
LLMs, RAG, knowledge graphs, and dynamic interface generation (via
MCPs), the system offers a personalized, interactive, and
multimodal learning journey. More than a study environment, DomPII
functions as an extension of thought, allowing the user to
navigate through their own records, content, and cognitive connections
through intelligent searches, timelines, and
interdisciplinary
visualizations. With flexible learning modes (Expert or
Polymath), intelligent gamification, and a real reward system, 
DomPII transforms the act of learning into a creative, free, and
stimulating experience where the user not only absorbs knowledge but
transforms it.

1. Introduction

DomPII is a self-learning platform based on artificial intelligence,
created to offer a new way to explore, build, and apply knowledge.
Instead of following rigid teaching paths, DomPII respects the
uniqueness of each learner, providing flexibility, autonomy, and deep
personalization of the educational process. At the heart of the platform
is the innovative use of Large Language Models (LLMs), which act not
only as intelligent tutors capable of explaining, questioning, and
evaluating, but also as engines that generate complete learning
interfaces and experiences.

Through a modular system called MCP (Model Context Protocol), the AI
model itself dynamically builds the front-end of the application,
generating interactive, multimodal, and responsive pages directly in HTML
for canvas rendering, enabling unprecedented freedom in the design and
structure of educational interactions.

DomPII transforms the learning environment into a living and
expandable space, where the student can upload documents, videos, and audio
that are processed and incorporated into their personal knowledge base. This base can
be consulted naturally via RAG (Retrieval-Augmented Generation),
relational graphs, or even an interactive timeline, allowing not only
active study, but also continuous access to one's own intellectual history
as if the system were a digital extension of the mind.
In addition, DomPII integrates gamification mechanics, such as daily
streak systems and real rewards (gift cards, configurable goals, and
incentives from friends or family), promoting engagement without sacrificing
cognitive depth. From the beginning, the user chooses between two modes: the
Expert mode, focused on deepening a specific area, or the
Polymath mode, which encourages transversal and interconnected exploration of
multiple fields of knowledge.

2. System Architecture

Diagram.jpg
""",
"""
2.1. Frontend

The DomPII frontend is intentionally minimalist, consisting only of
a main chat, a settings menu, and a canvas area for
HTML rendering. All the complexity of the interactive interfaces is delegated
to the language model itself, which dynamically generates the visual and
functional content through MCP tools. This approach significantly reduces
the need for manual development of traditional interfaces,
allowing AI to compose complete pages according to the
context and user objectives. Additionally, it is also possible to use
predefined layouts, which are dynamically filled by AI as
needed. Details about this dynamic generation process are
described in topic 2.3, which addresses how MCP works.

2.2. API

The DomPII API is based on REST architecture and offers endpoints for
CRUD operations aimed at user customization and system configurations.
It is integrated with the MCP protocol (Model Context Protocol), which acts
as an intermediary between the system logic and language models,
using AI as the main operation engine. The structure is compatible
with different LLMs available in the market, including open models
run locally, as long as they implement support for the MCP protocol.
Much of the communication between frontend and backend occurs through
streaming endpoints, connecting the user interface to MCP tools
in a continuous, responsive, and multimodal way.

2.3. MCP Servers

The Model Context Protocol (MCP) is a standard created by Anthropic to
connect language models to external tools through a
unified communication interface, functioning as a "USB port" between
the LLM and the execution environment. In DomPII, MCP is adopted as a
fundamental layer that allows AI to operate directly on components
of the system, whether they are media generators, HTML renderers, visual
interfaces, or database handlers. Through MCP, it is possible to define
expected input and output formats, as well as a brief description of
the behavior of each tool. This allows creating MCP Tools that
represent interactive interfaces or reusable functional blocks.

These tools can be predefined or generated on demand by AI, which
understands their parameters and returns the complete representation of the content, typically
in HTML ready to be rendered on the canvas. When an interface requires
data manipulation (such as saving progress or recording user actions), a
second MCP can be chained to the first, acting as its logical pair. The first
generates the interface and action prompt; the second performs operations in the database
according to the commands embedded in the context.
Additionally, MCPs are used for generating physical and
digital content, such as printable exercise PDFs, explainer videos, audio
or dynamically created images to enrich the learning process.

Initially, these MCP tools need to be manually defined,
but DomPII anticipates the development of two key features: An expandable MCP,
capable of accepting from AI not only the data to be filled in, but also the
interface description, and a generic MCP, designed for the registration and
universal modification of data, which can be used for
manipulating any type of data that the dynamic interface MCP may need.

With these features, it becomes possible to eliminate the need to develop
new interfaces manually, delegating to AI the role of designer,
implementer, and executor of visual and operational functionalities, as long as
formal and security principles are respected.
This architectural model transforms DomPII into a modular,
flexible, and highly decoupled system. Each functionality is an autonomous MCP,
which can be added, removed, or combined with others freely.
This drastically reduces the complexity of maintenance and development, and
at the same time makes room for a new type of educational system:
interconnected, fluid, and perhaps even chaotic where screens don't follow a
rigid hierarchy, but emerge as interactive environments that connect
dynamically, according to each user's journey.
This structure also enables a very high degree of customization,
allowing each user, or even each community, to build their own
DomPII with sets of MCP tools that meet their styles,
objectives, and preferred themes, like a living educational system that adapts
and reconfigures itself as it learns from those who use it.
""",
"""
Examples of MCP:

MCP Type            | Main Function                           | Examples in DomPII
Interface MCP       | HTML interface generation and population | Quiz, Mind Map, Timeline
Data MCP            | Database record manipulation           | Save answers, Update progress
Media Generation MCP | Production of context-based digital content | Exercise PDFs, Review Images
Expanded Interface MCP | Dynamic creation of new interfaces via AI | On-demand screen generation
Generic Records MCP | Universal data registration and modification | Unpredictable records

Usage flow example:

- The user requests in the chat a "test about Artificial Intelligence".
- The API triggers the LLM, which identifies the need to use the "Quiz Generator" Interface MCP.
- The LLM accesses the quiz generation MCP and returns to the frontend the page filled with the requested theme.
- The user responds directly on the rendered interface, which communicates with the API in natural language.
- The answers are sent back to the LLM, which directs them to the "Quiz Result Recorder" Data MCP.
- The system registers the user's performance in the database.
""",
"""
2.4. Databases

DomPII uses different databases, combining their specific characteristics 
to offer the flexibility, scalability, and separation of
responsibilities needed for the dynamic proposal of the system.
PostgreSQL, a relational database, is used to store more
structured and stable information, such as user profiles, configurations, permissions,
and other administrative records. It ensures referential integrity,
performance in transactional queries, and security for the core data that
support the basic operation of the platform.
MongoDB is used to store the raw knowledge generated and
manipulated in the learning interfaces. Its document-oriented
nature and lack of fixed schema allow each MCP to freely define its
own data formats, maintaining independence between tools and
""",
"""
adapting to the diversity of learning experiences.

Finally, Neo4j is used to represent relationships between content,
contexts, and activities through intelligent graphs. These graphs are
tuned with the support of AI algorithms, allowing both the system
to build dynamic learning paths and the learner
to explore their cognitive connections in personalized and visual ways.
This combination of databases provides not only robustness and speed, but
also opens paths to new forms of interaction with
knowledge, which will be explored in more depth in the following topics.

2.5. Storage and RAG

DomPII incorporates a document and media storage system,
allowing the user to upload content to complement their learning
journey or even build formative paths exclusively from
their own material.

All stored content, as well as learning records
saved in MongoDB and their relationships in Neo4j, can be embedded through
embedding techniques, generating a unique vector representation of each
knowledge element. These vectors allow the system, using
Retrieval-Augmented Generation (RAG), to retrieve relevant information
efficiently and semantically, responding to user requests in a
personalized and contextualized way.
This architecture transforms DomPII into a true extension of the
learner's memory, a digital second brain where knowledge
is not only stored, but can also be explored in innovative
ways.

Access to this content can occur through different visual MCPs,
which represent knowledge from various perspectives, such as mind
maps, interactive chronological records, or other dynamic interfaces that
can be continuously developed to enrich the experience of
navigation and discovery.

3. Gamification

DomPII incorporates elements of gamification to strengthen engagement and
continuity of users' learning journey. A daily streak system will be implemented,
which counts the number of consecutive days in which
""",
"""
the user interacts with the platform, encouraging the creation of consistent
study habits. This dynamic can be explored in various ways, including
integration with a reward system similar to a vault, where prizes are
stored and unlocked upon reaching specific goals.

Users can add their own gift cards or receive contributions from friends and
family, configuring personalized conditions for redemption.
The goals for releasing rewards will be flexible and may include
criteria such as the number of consecutive days of use, total time
dedicated to the platform, progress in the studied content, among other metrics
that may be incorporated as the system evolves.
This mechanism aims to transform the learning process into a
tangible experience of achievement, reinforcing the cycle of motivation and
personal progress.

4. Limitations and Challenges

As the volume of information stored by the user grows within
the system, it can become challenging for language models to handle
extensive contexts efficiently. However, the continuous evolution
of LLMs, especially the accelerated increase in token window size,
combined with good practices in knowledge representation and compression,
allows significantly mitigating this limitation.

Another challenge lies in the modular and active nature of DomPII. Users
accustomed to traditional learning methods, which are more passive and
linearly structured, may initially find the freedom and
dynamics offered by the platform strange. However, the very modular
architecture based on MCPs allows the creation of more directed flows and
adaptive interfaces, offering more linear navigation and study options for
those who prefer a more conventional learning experience.
These factors, far from being definitive barriers, are considered
opportunities for continuous evolution of the system, both in supporting diversity
of learner profiles and in adopting the most advanced technologies in
language processing.

5. Conclusion

DomPII represents a new approach to learning platforms:
""",
"""
more open, flexible, deeply integrated with the evolution of artificial
intelligence, and directed towards active and independent learning, without the need
for traditional institutions.

By structuring its core around modularity,
personalization, and learner autonomy, the system positions itself not only
as an educational tool, but as an active extension of
thought and knowledge construction.
By adopting concepts such as the Model Context Protocol, the use of
specialized databases, and RAG-assisted search, DomPII offers an
architecture capable of growing organically with its users and keeping pace with
AI advances continuously.

Although technical and pedagogical challenges are present, they are
viewed as a natural part of the innovation process. The flexibility of the
system ensures that it can adapt to new models, new user
profiles, and new ways of exploring knowledge.
With DomPII, learning is no longer just about accumulating
information: it becomes a creative, dynamic, and personal act where each journey
is unique, and where each achievement is also a real expansion of what we are
capable of knowing and building.
"""
]

# --- Style Definitions ---
styles = getSampleStyleSheet()

# Margins following the Bitcoin whitepaper style
left_margin = 1.5 * inch
right_margin = 1.46 * inch
top_margin = 1.3 * inch
bottom_margin = 1.0 * inch

# Modify existing styles to use CMU fonts
styles['Normal'].fontName = 'CMU-Roman'
styles['Normal'].fontSize = 10
styles['Normal'].leading = 12
styles['Normal'].alignment = TA_JUSTIFY
styles['Normal'].firstLineIndent = 0
styles['Normal'].spaceAfter = 0

# Style for paragraphs with indentation in the first line (after the first paragraph)
styles.add(ParagraphStyle(
    name='NormalIndented',
    parent=styles['Normal'],
    firstLineIndent=24,  # Adds indentation to the first line of paragraphs
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

# Add custom styles
# Style for author information
styles.add(ParagraphStyle(
    name='Author',
    fontName='CMU-Roman',
    fontSize=10,
    leading=12,
    alignment=TA_CENTER,
    spaceAfter=0
))

# Style for italic text
styles.add(ParagraphStyle(
    name='ItalicText',  # Different name to avoid conflicts
    fontName='CMU-Italic',
    fontSize=10,
    leading=12,
    alignment=TA_JUSTIFY
))

# Style for lists
styles.add(ParagraphStyle(
    name='ListItem',
    fontName='CMU-Roman',
    fontSize=10,
    leading=12,
    alignment=TA_JUSTIFY,
    leftIndent=20,
    bulletIndent=10
))


# Style for abstract
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

# --- Function to add page number ---
def add_page_number(canvas, doc):
    """Adds the page number in the footer, Bitcoin whitepaper style"""
    page_num = canvas.getPageNumber()
    text = "%d" % page_num
    canvas.saveState()
    canvas.setFont('CMU-Roman', 9)
    canvas.drawCentredString(letter[0]/2.0, 0.5 * inch, text)
    canvas.restoreState()

# --- Document Construction ---
output_filename = "dompii_whitepaper_recreated_en.pdf"
doc = SimpleDocTemplate(
    output_filename, 
    pagesize=letter,
    leftMargin=left_margin,
    rightMargin=right_margin,
    topMargin=top_margin,
    bottomMargin=bottom_margin
)

story = [] # List that will contain the PDF elements

# Process all content continuously
# First add title and author information
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

# Extract and add abstract
abstract_text = ""
abstract_found = False
for line in pages_content[0].strip().split('\n'):
    if line.startswith("Abstract."):
        abstract_found = True
        # Keep the word "Abstract." at the beginning, like in the Bitcoin whitepaper
        abstract_text = line[9:].strip() + " "
    elif abstract_found and not line.strip():
        break
    elif abstract_found:
        abstract_text += line.strip() + " "

# Create a custom abstract paragraph with "Abstract." in bold
bold_abstract = Paragraph("<font face='CMU-Bold'>Abstract.</font> " + abstract_text, styles['Abstract'])
story.append(bold_abstract)
story.append(Spacer(1, 0.3*inch))

# Now process all content continuously
current_paragraph = ""
in_abstract = True  # We start by ignoring the abstract because it has already been processed
in_table_header = False
skip_lines = 0
is_first_paragraph_of_section = False  # Variable to track if we're in the first paragraph of a section

# Join all content into a single list of lines
all_lines = []
for page in pages_content:
    lines = page.strip().split('\n')
    all_lines.extend(lines)

i = 0
while i < len(all_lines):
    line = all_lines[i]
    
    # Special handling for section 2.4
    if line.strip() == '2.4. Databases':
        # Add the section title
        if current_paragraph:
            story.append(Paragraph(current_paragraph, styles['Normal']))
            current_paragraph = ""
        story.append(Paragraph(line, styles['Heading2']))
        
        # Skip empty lines until finding the first line with content
        next_i = i + 1
        while next_i < len(all_lines) and not all_lines[next_i].strip():
            next_i += 1
        
        # Check if the next line is the one we expect for section 2.4
        if next_i < len(all_lines) and "uses different databases" in all_lines[next_i]:
            # Build the first paragraph
            first_para = "DomPII uses different databases, combining their specific characteristics to offer the flexibility, scalability, and separation of responsibilities needed for the dynamic proposal of the system."
            story.append(Paragraph(first_para, styles['Normal']))
            
            # Build the second paragraph about "PostgreSQL"
            second_para = "PostgreSQL, a relational database, is used to store more structured and stable information, such as user profiles, configurations, permissions, and other administrative records. It ensures referential integrity, performance in transactional queries, and security for the core data that support the basic operation of the platform."
            story.append(Paragraph(second_para, styles['NormalIndented']))
            
            # Build the third paragraph about "MongoDB"
            third_para = "MongoDB is used to store the raw knowledge generated and manipulated in the learning interfaces. Its document-oriented nature and lack of fixed schema allow each MCP to freely define its own data formats, maintaining independence between tools and adapting to the diversity of learning experiences."
            story.append(Paragraph(third_para, styles['NormalIndented']))
            
            # Skip ahead to after section 2.4
            i = next_i + 12  # Skip approximately to the next heading
            continue
    
    # Skip empty lines at the beginning
    if i < 6:  # Skip title and author information
        i += 1
        continue
    
    # Skip the abstract, as it has already been processed
    if line.startswith("Abstract."):
        in_abstract = True
        i += 1
        continue
    elif in_abstract:
        if not line.strip():
            in_abstract = False
        i += 1
        continue
    
    # Skip the diagram insertion tag and insert the diagram
    if line.startswith("Diagram.jpg"):
        if current_paragraph:
            story.append(Paragraph(current_paragraph, styles['Normal']))
            current_paragraph = ""
        
        # Add the diagram
        diagram_path = "Diagram.png"
        if os.path.exists(diagram_path):
            img = Image(diagram_path, width=3.5*inch, height=3.5*inch)
            img.hAlign = 'CENTER'
            story.append(Spacer(1, 0.2*inch))
            story.append(img)
            story.append(Spacer(1, 0.2*inch))
        i += 1
        continue
    
    # Main section title (e.g., "3. Gamification")
    if line.strip() and line.strip()[0].isdigit() and '. ' in line and '.' in line.strip()[:3]:
        if current_paragraph:
            story.append(Paragraph(current_paragraph, styles['Normal']))
            current_paragraph = ""
        story.append(Paragraph(line, styles['Heading1']))
        is_first_paragraph_of_section = True  # Mark the next paragraph as being the first in the section
    
    # Subsection title (e.g., "2.1. Frontend" or "2.4. Databases")
    elif line.strip() == "2.4. Databases" or (line.strip() and '.' in line.strip()[:4] and line.strip()[0].isdigit() and 
          (line.strip()[2].isdigit() or (len(line.strip()) > 3 and '.' in line.strip()[2:4]))):
        # Print details when finding a 2.x
        if line.strip().startswith("2."):
            print(f"DEBUGGER: Checking line '{line.strip()}' at position {i}")
            print(f"DEBUGGER: Conditions: isdigit[0]={line.strip()[0].isdigit()}, '.' in [:4]={'.' in line.strip()[:4]}")
            if len(line.strip()) > 2:
                print(f"DEBUGGER: isdigit[2]={line.strip()[2].isdigit() if len(line.strip()) > 2 else 'N/A'}")
            if len(line.strip()) > 3:
                print(f"DEBUGGER: '.' in [2:4]={'.' in line.strip()[2:4] if len(line.strip()) > 3 else 'N/A'}")
        if current_paragraph:
            story.append(Paragraph(current_paragraph, styles['Normal']))
            current_paragraph = ""
        story.append(Paragraph(line, styles['Heading2']))
        is_first_paragraph_of_section = True  # Mark the next paragraph as being the first in the section
        print(f"DEBUGGER: Found title {line.strip()} at line {i}")
    
    # Blank line (paragraph separation)
    elif not line.strip():
        if current_paragraph:
            # Choose the appropriate style based on whether it's the first paragraph after a title
            if is_first_paragraph_of_section:
                story.append(Paragraph(current_paragraph, styles['Normal']))
                is_first_paragraph_of_section = False  # Reset the flag
            else:
                story.append(Paragraph(current_paragraph, styles['NormalIndented']))
            current_paragraph = ""
    
    # List item with asterisk
    elif line.strip().startswith('*'):
        if current_paragraph:
            # Choose the appropriate style based on whether it's the first paragraph after a title
            if is_first_paragraph_of_section:
                story.append(Paragraph(current_paragraph, styles['Normal']))
                is_first_paragraph_of_section = False  # Reset the flag
            else:
                story.append(Paragraph(current_paragraph, styles['NormalIndented']))
            current_paragraph = ""
        
        item_text = line.strip()[1:].strip()
        story.append(Paragraph('• ' + item_text, styles['ListItem']))
    
    # Numbered list item (1., 2., etc.) or item with hyphen (-) at the beginning
    elif (line.strip() and line.strip()[0].isdigit() and line.strip()[1:].startswith('. ')) or line.strip().startswith('-'):
        # Finish current paragraph
        if current_paragraph:
            # Choose the appropriate style based on whether it's the first paragraph after a title
            if is_first_paragraph_of_section:
                story.append(Paragraph(current_paragraph, styles['Normal']))
                is_first_paragraph_of_section = False  # Reset the flag
            else:
                story.append(Paragraph(current_paragraph, styles['NormalIndented']))
            current_paragraph = ""
            
        # Format as list item (same for all)
        item_text = line.strip()
        story.append(Paragraph(item_text, styles['ListItem']))
    
    # Table
    elif line.strip().startswith('MCP Type') and '|' in line:
        if current_paragraph:
            story.append(Paragraph(current_paragraph, styles['Normal']))
            current_paragraph = ""
        
        story.append(Spacer(1, 0.2*inch))
        
        # Table title
        table_title = "Table 1: Examples of MCP tools in DomPII"
        story.append(Paragraph(table_title, styles['ItalicText']))
        story.append(Spacer(1, 0.1*inch))
        
        # Collect table data
        table_data = []
        header_line = line.strip()
        headers = [head.strip() for head in header_line.split('|')]
        
        # Add header with Paragraphs for formatting
        table_data.append([Paragraph(f"<b>{h}</b>", styles['Normal']) for h in headers if h])
        
        # Collect the next lines containing table data
        data_line_count = 0
        j = i + 1
        while j < len(all_lines) and data_line_count < 5:
            data_line = all_lines[j].strip()
            if '|' in data_line:
                cells = [cell.strip() for cell in data_line.split('|')]
                row_data = []
                for cell in cells:
                    if cell:  # Ignore empty cells
                        row_data.append(Paragraph(cell, styles['Normal']))
                if row_data:
                    table_data.append(row_data)
                data_line_count += 1
            j += 1
        
        # Configure column widths
        available_width = letter[0] - left_margin - right_margin
        col_widths = [available_width * 0.25, available_width * 0.40, available_width * 0.35]
        
        # Create table
        table = Table(table_data, colWidths=col_widths)
        
        # Table style
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
        
        # We need to skip the table lines - now based on the actual number of lines found
        in_table_header = True
        skip_lines = data_line_count + 1  # +1 for the header
    
    # Title "Usage flow example:"
    elif line.strip() == "Usage flow example:":
        if current_paragraph:
            story.append(Paragraph(current_paragraph, styles['Normal']))
            current_paragraph = ""
        
        # Add the title in italic 
        story.append(Spacer(1, 0.2*inch))
        story.append(Paragraph("Usage flow example:", styles['ItalicText']))
        story.append(Spacer(1, 0.1*inch))
        
        # Process flow items as paragraphs with smaller font
        j = i + 1
        while j < len(all_lines) and j < i + 10:  # Check up to 10 lines ahead
            line_text = all_lines[j].strip()
            # Check if it's a numbered item (1., 2., etc.)
            if line_text and line_text[0] == '-':
                # Add as normal text, with the same style as lists
                story.append(Paragraph(line_text, styles['ListItem']))
                j += 1
            else:
                # If it's not a numbered item, exit the loop
                break
        
        # Skip the lines already processed
        i = j - 1
    
    # Normal text - accumulate to form paragraphs
    else:
        if in_table_header:
            # We're in the middle of the table, so we need to skip some lines
            if skip_lines > 0:
                skip_lines -= 1
                if skip_lines == 0:
                    in_table_header = False
        elif "|" not in line:  # Ignore table lines
            # Check if it's the first line after a title
            is_first_after_heading = False
            for j in range(i-1, max(0, i-5), -1):
                if j < len(all_lines):
                    prev_line = all_lines[j].strip()
                    if not prev_line:
                        continue  # Skip blank lines
                    if ((prev_line[0].isdigit() and '. ' in prev_line and '.' in prev_line[:3]) or  # Main title
                        ('.' in prev_line[:4] and prev_line[0].isdigit() and prev_line[2].isdigit())): # Subtitle
                        is_first_after_heading = True
                        for k in range(j+1, i):
                            if k < len(all_lines) and all_lines[k].strip() and not all_lines[k].strip().startswith("Diagram"):
                                is_first_after_heading = False
                                break
                        break
                    break
            
            # If it's the first line of text after a title and we don't have accumulated text, mark the paragraph
            if is_first_after_heading and not current_paragraph:
                # Mark as first paragraph of the section
                is_first_paragraph_of_section = True
            
            current_paragraph += line.strip() + " "
    
    i += 1

# Add the last pending paragraph
if current_paragraph:
    # Choose the appropriate style based on whether it's the first paragraph after a title
    if is_first_paragraph_of_section:
        story.append(Paragraph(current_paragraph, styles['Normal']))
    else:
        story.append(Paragraph(current_paragraph, styles['NormalIndented']))

# Build the PDF
try:
    doc.build(story, onFirstPage=add_page_number, onLaterPages=add_page_number)
    print(f"PDF document recreated with Bitcoin whitepaper style as '{output_filename}' successfully.")
except Exception as e:
    print(f"Error generating PDF '{output_filename}': {e}")