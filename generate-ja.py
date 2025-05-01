# -*- coding: utf-8 -*-

# reportlab ライブラリから必要なクラスをインポート
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

# CMU Serif フォント（Computer Modern）を登録
pdfmetrics.registerFont(TTFont('CMU-Roman', 'assets/NotoSansJP-Regular.ttf'))
pdfmetrics.registerFont(TTFont('CMU-Bold', 'assets/NotoSansJP-Bold.ttf'))
pdfmetrics.registerFont(TTFont('CMU-Italic', 'assets/NotoSansJP-Light.ttf'))

# --- PDFから抽出されたコンテンツ ---
pages_content = [
"""
DomPII: AIを活用した自己学習システム

Yan Vidal
contact@dompii.com
www.dompii.com

要約。DomPIIは、あらゆる知識分野の独学者をエンパワーするために設計された
人工知能ベースのオープンソース教育プラットフォームです。LLM、RAG、
ナレッジグラフ、動的インターフェース生成（MCP経由）などの最先端技術を
組み合わせ、パーソナライズされたインタラクティブでマルチモーダルな
学習の旅を提供します。DomPIIは学習環境としてだけでなく、思考の拡張として
機能し、インテリジェントな検索、タイムライン、学際的な可視化を通じて
ユーザー自身の記録、コンテンツ、認知的つながりをナビゲートできるように
します。柔軟な学習モード（エキスパートまたはポリマス）、インテリジェントな
ゲーミフィケーション、実際の報酬システムを備えたDomPIIは、学習行為を
創造的で自由、そして刺激的な経験に変え、ユーザーは知識を吸収するだけでなく
それを変容させることができます。

1. はじめに

DomPIIは人工知能をベースにした自己学習プラットフォームで、知識を探索、
構築、適用する新しい方法を提供するために作られました。硬直した教育経路に
従うのではなく、DomPIIは各学習者の独自性を尊重し、教育プロセスの柔軟性、
自律性、深いパーソナライゼーションを提供します。プラットフォームの中核には、
大規模言語モデル（LLM）の革新的な使用があり、これらは説明、質問、評価が
できるインテリジェントなチューターとしてだけでなく、完全な学習インターフェースと
経験を生成するエンジンとしても機能します。

MCP（Model Context Protocol）と呼ばれるモジュラーシステムを通じて、AI
モデル自体がアプリケーションのフロントエンドを動的に構築し、インタラクティブで
マルチモーダル、レスポンシブなページを直接HTMLでキャンバスにレンダリングするために
生成することで、教育的インタラクションのデザインと構造に前例のない自由を
可能にします。

DomPIIは学習環境を生きた拡張可能な空間に変え、学生はドキュメント、ビデオ、
オーディオをアップロードでき、それらは処理されて個人的な知識ベースに
組み込まれます。この知識ベースはRAG（Retrieval-Augmented Generation）、
関係グラフ、またはインタラクティブなタイムラインを通じて自然に
相談することができ、アクティブな学習だけでなく、まるでシステムが心の
デジタル拡張であるかのように、自分自身の知的履歴に継続的にアクセスすることを
可能にします。
さらに、DomPIIはデイリーストリークシステムや実際の報酬（ギフトカード、
設定可能な目標、友人や家族からのインセンティブ）などのゲーミフィケーション
メカニズムを統合し、認知的深さを犠牲にすることなくエンゲージメントを
促進します。最初から、ユーザーは2つのモードのいずれかを選択します：
特定の分野を深めることに焦点を当てたエキスパートモード、または複数の
知識の横断的で相互接続された探索を奨励するポリマスモードです。

2. システムアーキテクチャ

Diagram.jpg
""",
"""
2.1. フロントエンド

DomPIIのフロントエンドは意図的にミニマリストで、メインチャット、設定メニュー、
そしてHTMLレンダリング用のキャンバスエリアのみで構成されています。
インタラクティブインターフェースの複雑さはすべて言語モデル自体に委任され、
MCPツールを通じて視覚的および機能的なコンテンツを動的に生成します。
このアプローチにより、従来のインターフェースの手動開発の必要性が
大幅に削減され、AIがユーザーのコンテキストと目的に応じて完全なページを
構成できるようになります。また、AIによって動的に埋められる
事前定義されたレイアウトを使用することも可能です。この動的生成プロセスの
詳細はトピック2.3で説明されており、MCPの機能について説明しています。

2.2. API

DomPIIのAPIはRESTアーキテクチャに基づいており、ユーザーのカスタマイズと
システム設定向けのCRUD操作のためのエンドポイントを提供しています。
システムロジックと言語モデルの間の仲介者として機能するMCPプロトコル
（Model Context Protocol）と統合されており、AIをメインの操作エンジンとして
使用しています。この構造は市場で利用可能な異なるLLMと互換性があり、
MCPプロトコルのサポートを実装している限り、ローカルで実行されるオープン
モデルも含まれます。フロントエンドとバックエンドの間の通信の大部分は
ストリーミングエンドポイントを通じて行われ、ユーザーインターフェースを
MCPツールに継続的、応答的、マルチモーダルな方法で接続しています。

2.3. MCPサーバー

Model Context Protocol（MCP）はAnthropicによって作成された標準で、
統一された通信インターフェースを通じて言語モデルを外部ツールに接続し、
LLMと実行環境の間の「USBポート」のように機能します。DomPIIでは、
MCPはAIがシステムのコンポーネント（メディアジェネレーター、HTMLレンダラー、
ビジュアルインターフェース、またはデータベースハンドラーなど）に直接
操作できるようにする基本的なレイヤーとして採用されています。MCPを通じて、
期待される入力と出力の形式、および各ツールの動作の簡単な説明を定義することが
可能です。これにより、インタラクティブインターフェースや再利用可能な
機能ブロックを表すMCPツールを作成することができます。

これらのツールは事前定義されているか、AIによってオンデマンドで生成され、
AIはそのパラメータを理解し、通常はキャンバスでレンダリングする準備ができて
いるHTMLでコンテンツの完全な表現を返します。インターフェースがデータ操作
（進捗状況の保存やユーザーアクションの記録など）を必要とする場合、2番目の
MCPを最初のものに連鎖させ、論理的なペアとして機能させることができます。
最初のMCPはインターフェースとアクションプロンプトを生成し、2番目のMCPは
コンテキストに埋め込まれたコマンドに従ってデータベースで操作を実行します。
さらに、MCPは印刷可能なエクササイズPDF、説明ビデオ、オーディオ、または
学習プロセスを豊かにするために動的に作成された画像などの物理的および
デジタルコンテンツの生成にも使用されます。

最初、これらのMCPツールは手動で定義する必要がありますが、DomPIIは2つの
主要な機能の開発を予想しています：AIから埋め込むデータだけでなく
インターフェースの説明も受け入れることができる拡張可能なMCP、およびデータの
普遍的な登録と修正のために設計された汎用MCP。後者は動的インターフェースMCPが
必要とするあらゆる種類のデータの操作に使用できます。

これらの機能により、新しいインターフェースを手動で開発する必要性が排除され、
形式的およびセキュリティの原則が尊重される限り、視覚的および操作的な
機能のデザイナー、実装者、実行者としての役割をAIに委任することが
可能になります。
このアーキテクチャモデルはDomPIIをモジュラー、柔軟、そして高度に
分離されたシステムに変えます。各機能は自律的なMCPであり、自由に追加、
削除、または他のものと組み合わせることができます。これにより保守と開発の
複雑さが劇的に削減され、同時に新しいタイプの教育システムのための
スペースが作られます：相互接続され、流動的で、おそらく画面が硬直した
階層に従わないカオス的なもので、各ユーザーの旅に応じて動的に接続される
インタラクティブな環境として現れます。
この構造はまた、非常に高度なカスタマイズを可能にし、各ユーザー、または
各コミュニティが、自分のスタイル、目的、好みのテーマに合わせたMCPツールの
セットで独自のDomPIIを構築できるようにし、それを使用する人から学ぶにつれて
適応し再構成される生きた教育システムのようになります。
""",
"""
MCPの例：

MCP タイプ           | 主な機能                        | DomPIIでの例
インターフェース MCP    | HTMLインターフェースの生成と入力   | クイズ、マインドマップ、タイムライン
データ MCP            | データベースレコードの操作         | 回答の保存、進捗状況の更新
メディア生成 MCP       | コンテキストベースのデジタルコンテンツ制作 | エクササイズPDF、レビュー画像
拡張インターフェース MCP | AI経由の新しいインターフェースの動的作成 | オンデマンドスクリーン生成
汎用レコード MCP       | 普遍的なデータ登録と修正         | 予測不可能なレコード

使用フロー例：

- ユーザーがチャットで「人工知能についてのテスト」をリクエストします。
- APIがLLMをトリガーし、「クイズジェネレーター」インターフェースMCPを使用する必要性を識別します。
- LLMはクイズ生成MCPにアクセスし、リクエストされたテーマで埋められたページをフロントエンドに返します。
- ユーザーはレンダリングされたインターフェースで直接回答し、APIと自然言語で通信します。
- 回答は再びLLMに送信され、「クイズ結果レコーダー」データMCPに転送されます。
- システムはユーザーのパフォーマンスをデータベースに登録します。
""",
"""
2.4. データベース

DomPIIは異なるデータベースを使用し、システムの動的な提案に必要な柔軟性、
スケーラビリティ、および責任の分離を提供するためにそれらの特定の特性を
組み合わせています。
リレーショナルデータベースであるPostgreSQLは、ユーザープロファイル、
設定、権限、その他の管理記録など、より構造化された安定した情報を保存するために
使用されています。それはリファレンシャルインテグリティ、トランザクション
クエリでのパフォーマンス、およびプラットフォームの基本操作を支える
コアデータのセキュリティを保証します。
MongoDBは学習インターフェースで生成および操作される生の知識を保存するために
使用されています。そのドキュメント指向の性質と固定スキーマの欠如により、
各MCPは自由に独自のデータ形式を定義でき、ツール間の独立性を維持し、
""",
"""
学習体験の多様性に適応します。

最後に、Neo4jはインテリジェントグラフを通じてコンテンツ、コンテキスト、
活動間の関係を表現するために使用されています。これらのグラフはAIアルゴリズムの
サポートでチューニングされ、システムが動的な学習パスを構築できるようにすると
同時に、学習者が自分の認知的つながりをパーソナライズされた視覚的な方法で
探索できるようにします。
このデータベースの組み合わせは堅牢性とスピードだけでなく、知識との
新しい形の相互作用への道も開き、これは以下のトピックでより詳細に
探求されます。

2.5. ストレージとRAG

DomPIIはドキュメントとメディアのストレージシステムを組み込み、ユーザーが
自分の学習の旅を補完するためのコンテンツをアップロードすることを可能にし、
あるいは自分自身の素材からのみ形成的なパスを構築することも可能にします。

MongoDBに保存された学習記録とNeo4jでのそれらの関係と同様に保存された
すべてのコンテンツは、埋め込み技術を通じて埋め込まれ、各知識要素の
ユニークなベクトル表現を生成することができます。これらのベクターにより、
システムはRetrieval-Augmented Generation（RAG）を使用して、効率的で意味的に
関連情報を取得し、パーソナライズされたコンテキスト化された方法で
ユーザーのリクエストに応答することができます。
このアーキテクチャはDomPIIを学習者のメモリの真の拡張、知識が単に
保存されるだけでなく、革新的な方法で探索することもできるデジタルの
セカンドブレインに変えます。

このコンテンツへのアクセスは、マインドマップ、インタラクティブな年代記録録、
またはナビゲーションと発見の経験を豊かにするために継続的に開発される
可能性のある他の動的インターフェースなど、異なる視覚的MCPを通じて行われ、
知識をさまざまな視点から表現します。

3. ゲーミフィケーション

DomPIIはユーザーの学習の旅の参加と継続性を強化するためのゲーミフィケーション
要素を組み込んでいます。ユーザーがプラットフォームと相互作用する連続した
日数をカウントするデイリーストリークシステムが実装され、一貫した
""",
"""
学習習慣の作成を奨励します。この動的な仕組みは、特定の目標に達した
時に解除される報酬が保存される金庫のような報酬システムとの統合など、
さまざまな方法で探索することができます。

ユーザーは自分自身のギフトカードを追加したり、友人や家族からの寄付を
受け取ったりして、交換のためのパーソナライズされた条件を設定することが
できます。
報酬を解放するための目標は柔軟で、連続使用日数、プラットフォームに
専念した総時間、学習したコンテンツの進歩など、システムの進化に応じて
組み込まれる可能性のある他のメトリックを含むことができます。
このメカニズムは学習プロセスを達成の具体的な経験に変え、モチベーション
と個人的な進歩のサイクルを強化することを目指しています。

4. 制限と課題

システム内でユーザーによって保存される情報の量が増えるにつれて、
言語モデルが広範囲なコンテキストを効率的に処理することは困難になる
可能性があります。しかし、LLMの継続的な進化、特にトークンウィンドウサイズの
加速的な増加は、知識表現と圧縮の優れた実践と組み合わさり、この制限を
大幅に軽減することができます。

もう一つの課題はDomPIIのモジュラーでアクティブな性質にあります。
より受動的で線形に構造化された伝統的な学習方法に慣れたユーザーは、
最初はプラットフォームが提供する自由とダイナミクスに違和感を
覚えるかもしれません。しかし、MCPに基づいたモジュラーアーキテクチャ
自体がより方向付けられたフローと適応的なインターフェースの作成を可能にし、
より従来の学習体験を好む人々のためのより線形なナビゲーションと学習の
オプションを提供します。
これらの要因は、決定的な障壁というよりも、学習者プロファイルの多様性の
サポートと言語処理における最先端技術の採用の両方において、システムの
継続的な進化の機会と考えられています。

5. 結論

DomPIIは学習プラットフォームに対する新しいアプローチを表しています：
""",
"""
より開放的で柔軟、人工知能の進化と深く統合され、伝統的な機関の必要なしに
アクティブで独立した学習に向けられています。

モジュラリティ、パーソナライゼーション、学習者の自律性を中心に
核を構造化することにより、システムは単なる教育ツールではなく、
思考と知識構築のアクティブな拡張として位置づけられています。
Model Context Protocol、専門データベースの使用、RAGによる支援検索
などの概念を採用することにより、DomPIIはユーザーと有機的に成長し、
AIの進歩に継続的に追いつくことができるアーキテクチャを提供します。

技術的かつ教育的な課題が存在していますが、それらはイノベーション
プロセスの自然な一部として扱われています。システムの柔軟性により、
新しいモデル、新しいユーザープロファイル、知識を探索する新しい方法に
適応できることが保証されています。
DomPIIを使用すると、学ぶことは単に情報を蓄積することだけではなく、
各旅が一意であり、各達成も私たちが知り、構築できることの実際の
拡張でもある創造的で動的、個人的な行為になります。
"""
]

# --- スタイル定義 ---
styles = getSampleStyleSheet()

# Bitcoinホワイトペーパースタイルに従った余白
left_margin = 1.5 * inch
right_margin = 1.46 * inch
top_margin = 1.3 * inch
bottom_margin = 1.0 * inch

# CMUフォントを使用するために既存のスタイルを変更
styles['Normal'].fontName = 'CMU-Roman'
styles['Normal'].fontSize = 10
styles['Normal'].leading = 12
styles['Normal'].alignment = TA_JUSTIFY
styles['Normal'].firstLineIndent = 0
styles['Normal'].spaceAfter = 0

# 段落の最初の行にインデントを付けるスタイル（最初の段落の後）
styles.add(ParagraphStyle(
    name='NormalIndented',
    parent=styles['Normal'],
    firstLineIndent=24,  # 段落の最初の行にインデントを追加
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

# カスタムスタイルを追加
# 著者情報のスタイル
styles.add(ParagraphStyle(
    name='Author',
    fontName='CMU-Roman',
    fontSize=10,
    leading=12,
    alignment=TA_CENTER,
    spaceAfter=0
))

# イタリック体テキストのスタイル
styles.add(ParagraphStyle(
    name='ItalicText',  # 競合を避けるために異なる名前
    fontName='CMU-Italic',
    fontSize=10,
    leading=12,
    alignment=TA_JUSTIFY
))

# リストのスタイル
styles.add(ParagraphStyle(
    name='ListItem',
    fontName='CMU-Roman',
    fontSize=10,
    leading=12,
    alignment=TA_JUSTIFY,
    leftIndent=20,
    bulletIndent=10
))


# 要約のスタイル
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

# --- ページ番号を追加する関数 ---
def add_page_number(canvas, doc):
    """Bitcoinホワイトペーパースタイルでフッターにページ番号を追加する"""
    page_num = canvas.getPageNumber()
    text = "%d" % page_num
    canvas.saveState()
    canvas.setFont('CMU-Roman', 9)
    canvas.drawCentredString(letter[0]/2.0, 0.5 * inch, text)
    canvas.restoreState()

# --- ドキュメント構築 ---
output_filename = "docs/dompii-whitepaper_ja.pdf"

# PDFにメタデータを追加するためのキャンバスカスタマイズを定義
class PdfDocTemplate(SimpleDocTemplate):
    def __init__(self, *args, **kwargs):
        SimpleDocTemplate.__init__(self, *args, **kwargs)
        self.title = "DomPII: AIを活用した自己学習システム"
        self.author = "Yan Vidal"
        self.subject = "DomPII ホワイトペーパー"
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

story = [] # PDFの要素を含むリスト

# すべてのコンテンツを連続的に処理
# まずタイトルと著者情報を追加
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

# 要約を抽出して追加
abstract_text = ""
abstract_found = False
for line in pages_content[0].strip().split('\n'):
    if line.startswith("要約。"):
        abstract_found = True
        # Bitcoinホワイトペーパーのように「要約。」という単語を冒頭に保持
        abstract_text = line[3:].strip() + " "
    elif abstract_found and not line.strip():
        break
    elif abstract_found:
        abstract_text += line.strip() + " "

# 「要約。」を太字にしたカスタム要約段落を作成
bold_abstract = Paragraph("<font face='CMU-Bold'>要約。</font> " + abstract_text, styles['Abstract'])
story.append(bold_abstract)
story.append(Spacer(1, 0.3*inch))

# すべてのコンテンツを連続的に処理
current_paragraph = ""
in_abstract = True  # 要約は既に処理されているため、スキップから始める
in_table_header = False
skip_lines = 0
is_first_paragraph_of_section = False  # セクションの最初の段落かどうかを追跡する変数

# すべてのコンテンツを単一の行リストに結合
all_lines = []
for page in pages_content:
    lines = page.strip().split('\n')
    all_lines.extend(lines)

i = 0
while i < len(all_lines):
    line = all_lines[i]
    
    # セクション2.4の特別な扱い
    if line.strip() == '2.4. データベース':
        # セクションタイトルを追加
        if current_paragraph:
            story.append(Paragraph(current_paragraph, styles['Normal']))
            current_paragraph = ""
        story.append(Paragraph(line, styles['Heading2']))
        
        # 内容のある最初の行が見つかるまで空行をスキップ
        next_i = i + 1
        while next_i < len(all_lines) and not all_lines[next_i].strip():
            next_i += 1
        
        # 次の行がセクション2.4で期待する行かどうか確認
        if next_i < len(all_lines) and "異なるデータベースを使用" in all_lines[next_i]:
            # 最初の段落を構築
            first_para = "DomPIIは異なるデータベースを使用し、システムの動的な提案に必要な柔軟性、スケーラビリティ、および責任の分離を提供するためにそれらの特定の特性を組み合わせています。"
            story.append(Paragraph(first_para, styles['Normal']))
            
            # "PostgreSQL"についての2番目の段落を構築
            second_para = "リレーショナルデータベースであるPostgreSQLは、ユーザープロファイル、設定、権限、その他の管理記録など、より構造化された安定した情報を保存するために使用されています。それはリファレンシャルインテグリティ、トランザクションクエリでのパフォーマンス、およびプラットフォームの基本操作を支えるコアデータのセキュリティを保証します。"
            story.append(Paragraph(second_para, styles['NormalIndented']))
            
            # "MongoDB"についての3番目の段落を構築
            third_para = "MongoDBは学習インターフェースで生成および操作される生の知識を保存するために使用されています。そのドキュメント指向の性質と固定スキーマの欠如により、各MCPは自由に独自のデータ形式を定義でき、ツール間の独立性を維持し、学習体験の多様性に適応します。"
            story.append(Paragraph(third_para, styles['NormalIndented']))
            
            # セクション2.4の後に進む
            i = next_i + 12  # おおよそ次の見出しまでスキップ
            continue
    
    # 冒頭の空行をスキップ
    if i < 6:  # タイトルと著者情報をスキップ
        i += 1
        continue
    
    # 要約は既に処理されているためスキップ
    if line.startswith("要約。"):
        in_abstract = True
        i += 1
        continue
    elif in_abstract:
        if not line.strip():
            in_abstract = False
        i += 1
        continue
    
    # 図表挿入タグをスキップして図表を挿入
    if line.startswith("Diagram.jpg"):
        if current_paragraph:
            story.append(Paragraph(current_paragraph, styles['Normal']))
            current_paragraph = ""
        
        # 図表を追加
        diagram_path = "Diagram.png"
        if os.path.exists(diagram_path):
            img = Image(diagram_path, width=3.5*inch, height=3.5*inch)
            img.hAlign = 'CENTER'
            story.append(Spacer(1, 0.2*inch))
            story.append(img)
            story.append(Spacer(1, 0.2*inch))
        i += 1
        continue
    
    # メインセクションのタイトル（例：「3. ゲーミフィケーション」）
    if line.strip() and line.strip()[0].isdigit() and '. ' in line and '.' in line.strip()[:3]:
        if current_paragraph:
            story.append(Paragraph(current_paragraph, styles['Normal']))
            current_paragraph = ""
        story.append(Paragraph(line, styles['Heading1']))
        is_first_paragraph_of_section = True  # 次の段落をセクションの最初の段落としてマーク
    
    # サブセクションのタイトル（例：「2.1. フロントエンド」または「2.4. データベース」）
    elif line.strip() == "2.4. データベース" or (line.strip() and '.' in line.strip()[:4] and line.strip()[0].isdigit() and 
          (line.strip()[2].isdigit() or (len(line.strip()) > 3 and '.' in line.strip()[2:4]))):
        # 2.xを見つけたときの詳細を出力
        if line.strip().startswith("2."):
            print(f"デバッガー: 行 '{line.strip()}' を位置 {i} で確認中")
            print(f"デバッガー: 条件: isdigit[0]={line.strip()[0].isdigit()}, '.' in [:4]={'.' in line.strip()[:4]}")
            if len(line.strip()) > 2:
                print(f"デバッガー: isdigit[2]={line.strip()[2].isdigit() if len(line.strip()) > 2 else 'N/A'}")
            if len(line.strip()) > 3:
                print(f"デバッガー: '.' in [2:4]={'.' in line.strip()[2:4] if len(line.strip()) > 3 else 'N/A'}")
        if current_paragraph:
            story.append(Paragraph(current_paragraph, styles['Normal']))
            current_paragraph = ""
        story.append(Paragraph(line, styles['Heading2']))
        is_first_paragraph_of_section = True  # 次の段落をセクションの最初の段落としてマーク
        print(f"デバッガー: タイトル {line.strip()} を行 {i} で見つけました")
    
    # 空行（段落の区切り）
    elif not line.strip():
        if current_paragraph:
            # タイトルの後の最初の段落かどうかに基づいて適切なスタイルを選択
            if is_first_paragraph_of_section:
                story.append(Paragraph(current_paragraph, styles['Normal']))
                is_first_paragraph_of_section = False  # フラグをリセット
            else:
                story.append(Paragraph(current_paragraph, styles['NormalIndented']))
            current_paragraph = ""
    
    # アスタリスクで始まるリストアイテム
    elif line.strip().startswith('*'):
        if current_paragraph:
            # タイトルの後の最初の段落かどうかに基づいて適切なスタイルを選択
            if is_first_paragraph_of_section:
                story.append(Paragraph(current_paragraph, styles['Normal']))
                is_first_paragraph_of_section = False  # フラグをリセット
            else:
                story.append(Paragraph(current_paragraph, styles['NormalIndented']))
            current_paragraph = ""
        
        item_text = line.strip()[1:].strip()
        story.append(Paragraph('• ' + item_text, styles['ListItem']))
    
    # 番号付きリストアイテム（1., 2.など）またはハイフン（-）で始まるアイテム
    elif (line.strip() and line.strip()[0].isdigit() and line.strip()[1:].startswith('. ')) or line.strip().startswith('-'):
        # 現在の段落を終了
        if current_paragraph:
            # タイトルの後の最初の段落かどうかに基づいて適切なスタイルを選択
            if is_first_paragraph_of_section:
                story.append(Paragraph(current_paragraph, styles['Normal']))
                is_first_paragraph_of_section = False  # フラグをリセット
            else:
                story.append(Paragraph(current_paragraph, styles['NormalIndented']))
            current_paragraph = ""
            
        # すべて同じスタイルでリストアイテムとしてフォーマット
        item_text = line.strip()
        story.append(Paragraph(item_text, styles['ListItem']))
    
    # テーブル
    elif line.strip().startswith('MCP タイプ') and '|' in line:
        if current_paragraph:
            story.append(Paragraph(current_paragraph, styles['Normal']))
            current_paragraph = ""
        
        story.append(Spacer(1, 0.2*inch))
        
        # テーブルのタイトル
        table_title = "表 1: DomPIIにおけるMCPツールの例"
        story.append(Paragraph(table_title, styles['ItalicText']))
        story.append(Spacer(1, 0.1*inch))
        
        # テーブルデータを収集
        table_data = []
        header_line = line.strip()
        headers = [head.strip() for head in header_line.split('|')]
        
        # フォーマット用のParagraphsでヘッダーを追加
        table_data.append([Paragraph(f"<b>{h}</b>", styles['Normal']) for h in headers if h])
        
        # テーブルデータを含む次の行を収集
        data_line_count = 0
        j = i + 1
        while j < len(all_lines) and data_line_count < 5:
            data_line = all_lines[j].strip()
            if '|' in data_line:
                cells = [cell.strip() for cell in data_line.split('|')]
                row_data = []
                for cell in cells:
                    if cell:  # 空のセルを無視
                        row_data.append(Paragraph(cell, styles['Normal']))
                if row_data:
                    table_data.append(row_data)
                data_line_count += 1
            j += 1
        
        # 列の幅を設定
        available_width = letter[0] - left_margin - right_margin
        col_widths = [available_width * 0.25, available_width * 0.40, available_width * 0.35]
        
        # テーブルを作成
        table = Table(table_data, colWidths=col_widths)
        
        # テーブルスタイル
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
        
        # テーブルの行をスキップする必要がある - 見つかった実際の行数に基づく
        in_table_header = True
        skip_lines = data_line_count + 1  # ヘッダーの+1
    
    # タイトル「使用フロー例：」
    elif line.strip() == "使用フロー例：":
        if current_paragraph:
            story.append(Paragraph(current_paragraph, styles['Normal']))
            current_paragraph = ""
        
        # タイトルをイタリック体で追加
        story.append(Spacer(1, 0.2*inch))
        story.append(Paragraph("使用フロー例：", styles['ItalicText']))
        story.append(Spacer(1, 0.1*inch))
        
        # フローのアイテムを小さいフォントの段落として処理
        j = i + 1
        while j < len(all_lines) and j < i + 10:  # 10行先まで確認
            line_text = all_lines[j].strip()
            # ハイフンで始まるアイテムかどうか確認
            if line_text and line_text.startswith('-'):
                # リストと同じスタイルで通常のテキストとして追加
                story.append(Paragraph(line_text, styles['ListItem']))
                j += 1
            else:
                # ハイフンで始まるアイテムでなければループを抜ける
                break
        
        # 既に処理した行をスキップ
        i = j - 1
    
    # 通常のテキスト - 段落を形成するために蓄積
    else:
        if in_table_header:
            # テーブルの途中なので数行スキップする必要がある
            if skip_lines > 0:
                skip_lines -= 1
                if skip_lines == 0:
                    in_table_header = False
        elif "|" not in line:  # テーブルの行を無視
            # タイトルの後の最初の行かどうか確認
            is_first_after_heading = False
            for j in range(i-1, max(0, i-5), -1):
                if j < len(all_lines):
                    prev_line = all_lines[j].strip()
                    if not prev_line:
                        continue  # 空行をスキップ
                    if ((prev_line[0].isdigit() and '. ' in prev_line and '.' in prev_line[:3]) or  # メインタイトル
                        ('.' in prev_line[:4] and prev_line[0].isdigit() and prev_line[2].isdigit())): # サブタイトル
                        is_first_after_heading = True
                        for k in range(j+1, i):
                            if k < len(all_lines) and all_lines[k].strip() and not all_lines[k].strip().startswith("Diagram"):
                                is_first_after_heading = False
                                break
                        break
                    break
            
            # タイトルの後の最初のテキスト行で、蓄積されたテキストがない場合、段落をマーク
            if is_first_after_heading and not current_paragraph:
                # セクションの最初の段落としてマーク
                is_first_paragraph_of_section = True
            
            current_paragraph += line.strip() + " "
    
    i += 1

# 最後の保留中の段落を追加
if current_paragraph:
    # タイトルの後の最初の段落かどうかに基づいて適切なスタイルを選択
    if is_first_paragraph_of_section:
        story.append(Paragraph(current_paragraph, styles['Normal']))
    else:
        story.append(Paragraph(current_paragraph, styles['NormalIndented']))

# PDFを構築
try:
    doc.build(story, onFirstPage=add_page_number, onLaterPages=add_page_number)
    print(f"PDFドキュメントがBitcoinホワイトペーパースタイルで '{output_filename}' として正常に再作成されました。")
except Exception as e:
    print(f"PDF '{output_filename}' の生成中にエラーが発生しました: {e}")