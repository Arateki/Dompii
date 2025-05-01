# -*- coding: utf-8 -*-

# 从reportlab库导入必要的类
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

# 注册CMU Serif字体（Computer Modern）
pdfmetrics.registerFont(TTFont('CMU-Roman', 'NotoSerifSC-Regular.ttf'))
pdfmetrics.registerFont(TTFont('CMU-Bold', 'NotoSerifSC-Bold.ttf'))
pdfmetrics.registerFont(TTFont('CMU-Italic', 'NotoSerifSC-Light.ttf'))

# --- 从PDF提取的内容 ---
pages_content = [
"""
DomPII: 一个具有人工智能的自学系统

Yan Vidal
contact@dompii.com
www.dompii.com

摘要。DomPII是一个基于人工智能的开源教育平台，旨在赋能各个知识领域的
自学者。它结合了前沿技术，如大型语言模型（LLM）、检索增强生成（RAG）、
知识图谱和动态界面生成（通过MCP），提供个性化、互动和多模态的学习旅程。
DomPII不仅是一个学习环境，而且能作为思维的延伸，使用户能够通过智能
搜索、时间线和跨学科可视化来浏览他们自己的记录、内容和认知联系。凭借
灵活的学习模式（专家或博学者）、智能游戏化和真实奖励系统，DomPII将
学习转变为一种创造性、自由和有激励性的体验，用户不仅能吸收知识，还能
转化知识。

1. 引言

DomPII是一个基于人工智能的自学平台，旨在提供探索、构建和应用知识的
新方式。与其遵循僵化的教学路径，DomPII尊重每个学习者的独特性，提供
教育过程的灵活性、自主性和深度个性化。平台的核心是大型语言模型（LLM）
的创新使用，它们不仅作为能够解释、提问和评估的智能导师，还作为生成
完整学习界面和体验的引擎。

通过名为MCP（Model Context Protocol）的模块化系统，AI模型本身动态
构建应用程序的前端，直接以HTML生成互动、多模态和响应式页面，用于
画布渲染，使教育互动的设计和结构拥有前所未有的自由度。

DomPII将学习环境转变为一个活跃的可扩展空间，学生可以上传文档、视频
和音频，这些内容经过处理后被纳入他们的个人知识库。这个知识库可以通过
RAG（检索增强生成）、关系图或交互式时间线自然地查询，不仅允许主动
学习，还可以持续访问自己的知识历史，仿佛系统是心灵的数字延伸。
此外，DomPII整合了游戏化机制，如每日连续使用系统和真实奖励（礼品卡、
可配置目标和来自朋友或家人的激励），在不牺牲认知深度的情况下促进参与。
从一开始，用户就可以选择两种模式之一：专注于深入特定领域的专家模式，
或鼓励横向和相互连接的多领域知识探索的博学者模式。

2. 系统架构

Diagram.jpg
""",
"""
2.1. 前端

DomPII的前端有意设计得极简，仅由主聊天界面、设置菜单和用于HTML渲染的
画布区域组成。互动界面的所有复杂性都委托给语言模型本身，它通过MCP工具
动态生成视觉和功能内容。这种方法显著减少了传统界面手动开发的需求，
允许AI根据用户的上下文和目标构建完整页面。此外，也可以使用预定义的
布局，由AI根据需要动态填充。关于这个动态生成过程的详细信息在主题2.3中
描述，该主题阐述了MCP的工作原理。

2.2. API

DomPII的API基于REST架构，为用户定制和系统配置提供CRUD操作端点。
它与MCP协议（Model Context Protocol）集成，作为系统逻辑和语言模型之间
的中介，使用AI作为主要操作引擎。该结构与市场上可用的不同LLM兼容，
包括本地运行的开放模型，只要它们实现对MCP协议的支持。前端和后端之间
的大部分通信通过流式端点进行，以连续、响应式和多模态的方式将用户界面
连接到MCP工具。

2.3. MCP服务器

Model Context Protocol (MCP)是由Anthropic创建的标准，通过统一的通信
接口将语言模型连接到外部工具，功能类似于LLM和执行环境之间的"USB端口"。
在DomPII中，MCP被采用为基础层，允许AI直接操作系统组件，无论是媒体
生成器、HTML渲染器、视觉界面还是数据库处理器。通过MCP，可以定义
期望的输入和输出格式，以及每个工具行为的简要描述。这使得创建MCP工具
成为可能，这些工具代表交互式界面或可重用的功能块。

这些工具可以预先定义，也可以由AI按需生成，AI理解其参数并返回内容的
完整表示，通常以准备在画布上渲染的HTML形式。当界面需要数据操作
（如保存进度或记录用户行为）时，第二个MCP可以链接到第一个，作为其
逻辑伙伴。第一个生成界面和动作提示；第二个根据嵌入在上下文中的命令
在数据库中执行操作。
此外，MCP还用于生成物理和数字内容，如可打印的练习PDF、解释视频、
音频或动态创建的图像，以丰富学习过程。

最初，这些MCP工具需要手动定义，但DomPII预计开发两个关键功能：一个
可扩展的MCP，能够接受来自AI的不仅是要填充的数据，还有界面描述，以及
一个通用MCP，设计用于通用数据的注册和修改，可用于处理动态界面MCP
可能需要的任何类型的数据。

有了这些功能，只要遵守形式和安全原则，就可以消除手动开发新界面的需求，
将视觉和操作功能的设计师、实施者和执行者角色委托给AI。
这种架构模型将DomPII转变为一个模块化、灵活和高度解耦的系统。每个功能
都是一个自主的MCP，可以自由地添加、删除或与其他功能组合。这显著减少了
维护和开发的复杂性，同时为新型教育系统创造了空间：互连、流动，甚至可能
是混沌的，屏幕不遵循僵化的层次结构，而是根据每个用户的旅程动态连接，
形成交互环境。
这种结构还实现了高度定制，允许每个用户，甚至每个社区，使用符合其风格、
目标和偏好主题的MCP工具集构建自己的DomPII，像一个活的教育系统，
随着向使用者学习而适应和重构自己。
""",
"""
MCP示例：

MCP类型             | 主要功能                        | DomPII中的例子
界面MCP             | HTML界面生成和填充              | 测验、思维导图、时间线
数据MCP             | 数据库记录操作                  | 保存答案、更新进度
媒体生成MCP         | 基于上下文的数字内容制作        | 练习PDF、复习图像
扩展界面MCP         | 通过AI动态创建新界面            | 按需屏幕生成
通用记录MCP         | 通用数据注册和修改              | 不可预测的记录

使用流程示例：

- 用户在聊天中请求"关于人工智能的测试"。
- API触发LLM，识别需要使用"测验生成器"界面MCP。
- LLM访问测验生成MCP，并返回填充了请求主题的页面给前端。
- 用户直接在渲染的界面上回答，界面用自然语言与API通信。
- 答案再次发送给LLM，由其定向到"测验结果记录器"数据MCP。
- 系统在数据库中记录用户的表现。
""",
"""
2.4. 数据库

DomPII使用不同的数据库，结合它们的特定特性，为系统的动态方案提供
所需的灵活性、可扩展性和责任分离。
关系型数据库PostgreSQL用于存储更结构化和稳定的信息，如用户配置文件、
设置、权限和其他管理记录。它确保了引用完整性、事务查询性能和平台
基本操作所依赖的核心数据安全性。
MongoDB用于存储在学习界面中生成和操作的原始知识。其面向文档且无固定
模式的特性允许每个MCP自由定义自己的数据格式，保持工具之间的独立性，
并适应学习体验的多样性。
""",
"""
最后，Neo4j通过智能图谱表示内容、上下文和活动之间的关系。这些图谱在
AI算法的支持下进行调优，使系统能够构建动态学习路径，同时让学习者以
个性化和可视化的方式探索自己的认知联系。
这种数据库组合不仅提供稳健性和速度，还为与知识的新型交互方式开辟了
道路，这将在后续主题中深入探讨。

2.5. 存储和RAG

DomPII整合了文档和媒体存储系统，允许用户上传内容以补充他们的学习旅程，
或者甚至仅从自己的材料构建形成性路径。

所有存储的内容，以及保存在MongoDB中的学习记录和它们在Neo4j中的关系，
都可以通过嵌入技术进行嵌入，为每个知识元素生成唯一的向量表示。这些向量
使系统能够使用检索增强生成（RAG）高效且语义地检索相关信息，以个性化和
语境化的方式响应用户请求。
这种架构将DomPII转变为学习者记忆的真正延伸，一个数字第二大脑，知识
不仅被存储，还可以以创新方式探索。

这些内容的访问可以通过不同的视觉MCP进行，这些MCP从各种角度表示知识，
如思维导图、互动时间记录或其他可以不断开发的动态界面，以丰富导航和
发现的体验。

3. 游戏化

DomPII整合了游戏化元素，以加强用户学习旅程的参与度和连续性。将实施一个
每日连续使用系统，计算用户连续与平台交互的天数，鼓励形成一致的
""",
"""
学习习惯。这种动态可以通过多种方式探索，包括与类似保险箱的奖励系统
集成，在达到特定目标时解锁奖励。

用户可以添加自己的礼品卡或接收来自朋友和家人的贡献，为兑换配置个性化
条件。
释放奖励的目标将是灵活的，可能包括连续使用天数、专注于平台的总时间、
学习内容的进度等指标，随着系统的发展可能会纳入其他指标。
这一机制旨在将学习过程转变为一种实实在在的成就体验，加强动机和个人
进步的循环。

4. 局限和挑战

随着用户在系统内存储的信息量增加，语言模型可能会发现有效处理大量上下文
具有挑战性。然而，LLM的持续发展，特别是标记窗口大小的加速扩大，
结合良好的知识表示和压缩实践，可以显著减轻这一限制。

另一个挑战在于DomPII的模块化和主动性质。习惯于传统学习方法（更被动且
线性结构化）的用户最初可能会对平台提供的自由和动态感到陌生。然而，
基于MCP的模块化架构本身允许创建更有指导性的流程和自适应界面，为那些
偏好更传统学习体验的人提供更线性的导航和学习选项。
这些因素，远非决定性障碍，被视为系统持续发展的机会，无论是在支持学习者
档案的多样性，还是在采用语言处理中最先进的技术方面。

5. 结论

DomPII代表了学习平台的新方法：
""",
"""
更开放、灵活，与人工智能的发展深度集成，并面向无需传统机构的主动和
独立学习。

通过围绕模块化、个性化和学习者自主性构建其核心，系统不仅定位为一个
教育工具，还是思考和知识构建的主动延伸。
通过采用Model Context Protocol、专用数据库的使用和RAG辅助搜索等概念，
DomPII提供了一个能够与用户有机成长并持续跟上AI进步的架构。

虽然存在技术和教育方面的挑战，但它们被视为创新过程的自然部分。系统的
灵活性确保它能够适应新模型、新用户档案和新的知识探索方式。
使用DomPII，学习不再仅仅是积累信息：它成为一种创造性、动态和个人的
行为，每个旅程都是独特的，每个成就也是我们能够知道和构建的内容的
真实扩展。
"""
]

# --- 样式定义 ---
styles = getSampleStyleSheet()

# 按照比特币白皮书风格的页边距
left_margin = 1.5 * inch
right_margin = 1.46 * inch
top_margin = 1.3 * inch
bottom_margin = 1.0 * inch

# 修改现有样式以使用CMU字体
styles['Normal'].fontName = 'CMU-Roman'
styles['Normal'].fontSize = 10
styles['Normal'].leading = 12
styles['Normal'].alignment = TA_JUSTIFY
styles['Normal'].firstLineIndent = 0
styles['Normal'].spaceAfter = 0

# 第一行缩进的段落样式（第一段落之后）
styles.add(ParagraphStyle(
    name='NormalIndented',
    parent=styles['Normal'],
    firstLineIndent=24,  # 向段落第一行添加缩进
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

# 添加自定义样式
# 作者信息样式
styles.add(ParagraphStyle(
    name='Author',
    fontName='CMU-Roman',
    fontSize=10,
    leading=12,
    alignment=TA_CENTER,
    spaceAfter=0
))

# 斜体文本样式
styles.add(ParagraphStyle(
    name='ItalicText',  # 不同名称以避免冲突
    fontName='CMU-Italic',
    fontSize=10,
    leading=12,
    alignment=TA_JUSTIFY
))

# 列表样式
styles.add(ParagraphStyle(
    name='ListItem',
    fontName='CMU-Roman',
    fontSize=10,
    leading=12,
    alignment=TA_JUSTIFY,
    leftIndent=20,
    bulletIndent=10
))


# 摘要样式
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

# --- 添加页码的函数 ---
def add_page_number(canvas, doc):
    """按比特币白皮书风格在页脚添加页码"""
    page_num = canvas.getPageNumber()
    text = "%d" % page_num
    canvas.saveState()
    canvas.setFont('CMU-Roman', 9)
    canvas.drawCentredString(letter[0]/2.0, 0.5 * inch, text)
    canvas.restoreState()

# --- 文档构建 ---
output_filename = "dompii-whitepaper_zh.pdf"

# 定义canvas自定义以添加PDF元数据
class PdfDocTemplate(SimpleDocTemplate):
    def __init__(self, *args, **kwargs):
        SimpleDocTemplate.__init__(self, *args, **kwargs)
        self.title = "DomPII: 一个具有人工智能的自学系统"
        self.author = "Yan Vidal"
        self.subject = "DomPII白皮书"
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

story = [] # 包含PDF元素的列表

# 连续处理所有内容
# 首先添加标题和作者信息
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

# 提取并添加摘要
abstract_text = ""
abstract_found = False
for line in pages_content[0].strip().split('\n'):
    if line.startswith("摘要。"):
        abstract_found = True
        # 保持开头的"摘要。"，就像比特币白皮书那样
        abstract_text = line[3:].strip() + " "
    elif abstract_found and not line.strip():
        break
    elif abstract_found:
        abstract_text += line.strip() + " "

# 创建一个自定义摘要段落，"摘要。"为粗体
bold_abstract = Paragraph("<font face='CMU-Bold'>摘要。</font> " + abstract_text, styles['Abstract'])
story.append(bold_abstract)
story.append(Spacer(1, 0.3*inch))

# 现在连续处理所有内容
current_paragraph = ""
in_abstract = True  # 从跳过摘要开始，因为已经处理了
in_table_header = False
skip_lines = 0
is_first_paragraph_of_section = False  # 变量，用于跟踪我们是否在部分的第一段

# 将所有内容合并为单一行列表
all_lines = []
for page in pages_content:
    lines = page.strip().split('\n')
    all_lines.extend(lines)

i = 0
while i < len(all_lines):
    line = all_lines[i]
    
    # 2.4节的特殊处理
    if line.strip() == '2.4. 数据库':
        # 添加节标题
        if current_paragraph:
            story.append(Paragraph(current_paragraph, styles['Normal']))
            current_paragraph = ""
        story.append(Paragraph(line, styles['Heading2']))
        
        # 跳过空行，直到找到有内容的第一行
        next_i = i + 1
        while next_i < len(all_lines) and not all_lines[next_i].strip():
            next_i += 1
        
        # 检查下一行是否是我们在2.4节中预期的行
        if next_i < len(all_lines) and "使用不同的数据库" in all_lines[next_i]:
            # 构建第一段
            first_para = "DomPII使用不同的数据库，结合它们的特定特性，为系统的动态方案提供所需的灵活性、可扩展性和责任分离。"
            story.append(Paragraph(first_para, styles['Normal']))
            
            # 构建关于"PostgreSQL"的第二段
            second_para = "关系型数据库PostgreSQL用于存储更结构化和稳定的信息，如用户配置文件、设置、权限和其他管理记录。它确保了引用完整性、事务查询性能和平台基本操作所依赖的核心数据安全性。"
            story.append(Paragraph(second_para, styles['NormalIndented']))
            
            # 构建关于"MongoDB"的第三段
            third_para = "MongoDB用于存储在学习界面中生成和操作的原始知识。其面向文档且无固定模式的特性允许每个MCP自由定义自己的数据格式，保持工具之间的独立性，并适应学习体验的多样性。"
            story.append(Paragraph(third_para, styles['NormalIndented']))
            
            # 前进到2.4节之后
            i = next_i + 12  # 大约跳到下一个标题
            continue
    
    # 跳过开头的空行
    if i < 6:  # 跳过标题和作者信息
        i += 1
        continue
    
    # 跳过摘要，因为已经处理过了
    if line.startswith("摘要。"):
        in_abstract = True
        i += 1
        continue
    elif in_abstract:
        if not line.strip():
            in_abstract = False
        i += 1
        continue
    
    # 跳过图表插入标签并插入图表
    if line.startswith("Diagram.jpg"):
        if current_paragraph:
            story.append(Paragraph(current_paragraph, styles['Normal']))
            current_paragraph = ""
        
        # 添加图表
        diagram_path = "Diagram.png"
        if os.path.exists(diagram_path):
            img = Image(diagram_path, width=3.5*inch, height=3.5*inch)
            img.hAlign = 'CENTER'
            story.append(Spacer(1, 0.2*inch))
            story.append(img)
            story.append(Spacer(1, 0.2*inch))
        i += 1
        continue
    
    # 主节标题（例如："3. 游戏化"）
    if line.strip() and line.strip()[0].isdigit() and '. ' in line and '.' in line.strip()[:3]:
        if current_paragraph:
            story.append(Paragraph(current_paragraph, styles['Normal']))
            current_paragraph = ""
        story.append(Paragraph(line, styles['Heading1']))
        is_first_paragraph_of_section = True  # 标记下一段为节的第一段
    
    # 子节标题（例如："2.1. 前端"或"2.4. 数据库"）
    elif line.strip() == "2.4. 数据库" or (line.strip() and '.' in line.strip()[:4] and line.strip()[0].isdigit() and 
          (line.strip()[2].isdigit() or (len(line.strip()) > 3 and '.' in line.strip()[2:4]))):
        # 当找到2.x时打印详细信息
        if line.strip().startswith("2."):
            print(f"调试器: 检查行 '{line.strip()}' 在位置 {i}")
            print(f"调试器: 条件: isdigit[0]={line.strip()[0].isdigit()}, '.' in [:4]={'.' in line.strip()[:4]}")
            if len(line.strip()) > 2:
                print(f"调试器: isdigit[2]={line.strip()[2].isdigit() if len(line.strip()) > 2 else 'N/A'}")
            if len(line.strip()) > 3:
                print(f"调试器: '.' in [2:4]={'.' in line.strip()[2:4] if len(line.strip()) > 3 else 'N/A'}")
        if current_paragraph:
            story.append(Paragraph(current_paragraph, styles['Normal']))
            current_paragraph = ""
        story.append(Paragraph(line, styles['Heading2']))
        is_first_paragraph_of_section = True  # 标记下一段为节的第一段
        print(f"调试器: 找到标题 {line.strip()} 在行 {i}")
    
    # 空行（段落分隔）
    elif not line.strip():
        if current_paragraph:
            # 根据是否是标题后的第一段选择适当的样式
            if is_first_paragraph_of_section:
                story.append(Paragraph(current_paragraph, styles['Normal']))
                is_first_paragraph_of_section = False  # 重置标志
            else:
                story.append(Paragraph(current_paragraph, styles['NormalIndented']))
            current_paragraph = ""
    
    # 星号开头的列表项
    elif line.strip().startswith('*'):
        if current_paragraph:
            # 根据是否是标题后的第一段选择适当的样式
            if is_first_paragraph_of_section:
                story.append(Paragraph(current_paragraph, styles['Normal']))
                is_first_paragraph_of_section = False  # 重置标志
            else:
                story.append(Paragraph(current_paragraph, styles['NormalIndented']))
            current_paragraph = ""
        
        item_text = line.strip()[1:].strip()
        story.append(Paragraph('• ' + item_text, styles['ListItem']))
    
    # 编号列表项（1., 2.等）或连字符（-）开头的项
    elif (line.strip() and line.strip()[0].isdigit() and line.strip()[1:].startswith('. ')) or line.strip().startswith('-'):
        # 结束当前段落
        if current_paragraph:
            # 根据是否是标题后的第一段选择适当的样式
            if is_first_paragraph_of_section:
                story.append(Paragraph(current_paragraph, styles['Normal']))
                is_first_paragraph_of_section = False  # 重置标志
            else:
                story.append(Paragraph(current_paragraph, styles['NormalIndented']))
            current_paragraph = ""
            
        # 格式化为列表项（所有类型相同）
        item_text = line.strip()
        story.append(Paragraph(item_text, styles['ListItem']))
    
    # 表格
    elif line.strip().startswith('MCP类型') and '|' in line:
        if current_paragraph:
            story.append(Paragraph(current_paragraph, styles['Normal']))
            current_paragraph = ""
        
        story.append(Spacer(1, 0.2*inch))
        
        # 表格标题
        table_title = "表 1: DomPII中的MCP工具示例"
        story.append(Paragraph(table_title, styles['ItalicText']))
        story.append(Spacer(1, 0.1*inch))
        
        # 收集表格数据
        table_data = []
        header_line = line.strip()
        headers = [head.strip() for head in header_line.split('|')]
        
        # 使用段落添加标题以便格式化
        table_data.append([Paragraph(f"<b>{h}</b>", styles['Normal']) for h in headers if h])
        
        # 收集包含表格数据的下几行
        data_line_count = 0
        j = i + 1
        while j < len(all_lines) and data_line_count < 5:
            data_line = all_lines[j].strip()
            if '|' in data_line:
                cells = [cell.strip() for cell in data_line.split('|')]
                row_data = []
                for cell in cells:
                    if cell:  # 忽略空单元格
                        row_data.append(Paragraph(cell, styles['Normal']))
                if row_data:
                    table_data.append(row_data)
                data_line_count += 1
            j += 1
        
        # 配置列宽
        available_width = letter[0] - left_margin - right_margin
        col_widths = [available_width * 0.25, available_width * 0.40, available_width * 0.35]
        
        # 创建表格
        table = Table(table_data, colWidths=col_widths)
        
        # 表格样式
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
        
        # 需要跳过表格行 - 现在基于找到的实际行数
        in_table_header = True
        skip_lines = data_line_count + 1  # +1用于标题
    
    # 标题"使用流程示例："
    elif line.strip() == "使用流程示例：":
        if current_paragraph:
            story.append(Paragraph(current_paragraph, styles['Normal']))
            current_paragraph = ""
        
        # 以斜体添加标题
        story.append(Spacer(1, 0.2*inch))
        story.append(Paragraph("使用流程示例：", styles['ItalicText']))
        story.append(Spacer(1, 0.1*inch))
        
        # 将流程项处理为较小字体的段落
        j = i + 1
        while j < len(all_lines) and j < i + 10:  # 向前检查最多10行
            line_text = all_lines[j].strip()
            # 检查是否是连字符（-）开头的项
            if line_text and line_text.startswith('-'):
                # 作为普通文本添加，使用与列表相同的样式
                story.append(Paragraph(line_text, styles['ListItem']))
                j += 1
            else:
                # 如果不是连字符项，退出循环
                break
        
        # 跳过已处理的行
        i = j - 1
    
    # 普通文本 - 积累形成段落
    else:
        if in_table_header:
            # 我们在表格中间，需要跳过一些行
            if skip_lines > 0:
                skip_lines -= 1
                if skip_lines == 0:
                    in_table_header = False
        elif "|" not in line:  # 忽略表格行
            # 检查是否是标题后的第一行
            is_first_after_heading = False
            for j in range(i-1, max(0, i-5), -1):
                if j < len(all_lines):
                    prev_line = all_lines[j].strip()
                    if not prev_line:
                        continue  # 跳过空行
                    if ((prev_line[0].isdigit() and '. ' in prev_line and '.' in prev_line[:3]) or  # 主标题
                        ('.' in prev_line[:4] and prev_line[0].isdigit() and prev_line[2].isdigit())): # 副标题
                        is_first_after_heading = True
                        for k in range(j+1, i):
                            if k < len(all_lines) and all_lines[k].strip() and not all_lines[k].strip().startswith("Diagram"):
                                is_first_after_heading = False
                                break
                        break
                    break
            
            # 如果是标题后的第一行文本且没有积累的文本，标记段落
            if is_first_after_heading and not current_paragraph:
                # 标记为节的第一段
                is_first_paragraph_of_section = True
            
            current_paragraph += line.strip() + " "
    
    i += 1

# 添加最后一个待处理段落
if current_paragraph:
    # 根据是否是标题后的第一段选择适当的样式
    if is_first_paragraph_of_section:
        story.append(Paragraph(current_paragraph, styles['Normal']))
    else:
        story.append(Paragraph(current_paragraph, styles['NormalIndented']))

# 构建PDF
try:
    doc.build(story, onFirstPage=add_page_number, onLaterPages=add_page_number)
    print(f"PDF文档已成功以比特币白皮书风格重新创建为 '{output_filename}'。")
except Exception as e:
    print(f"生成PDF '{output_filename}' 时出错: {e}")