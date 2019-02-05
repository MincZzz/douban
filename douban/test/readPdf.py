from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal, LAParams
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed

from urllib.request import urlopen
from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
import ssl

context = ssl._create_unverified_context()

# 获取文档对象
# fb = open("http://www.tencent.com/zh-cn/content/ir/an/2016/attachments/20160321.pdf","rb")
fb = urlopen("https://www.tencent.com/zh-cn/articles/8003521534381984.pdf", context=context)
# 创建一个与文档关联解析器
parser = PDFParser(fb)

doc = PDFDocument()
# 链接解析器和文档对象
parser.set_document(doc)
doc.set_parser(parser)

# 参数是密码
doc.initialize("")

# 创建PDF资源管理器
resource = PDFResourceManager()
# 参数分析器
params = LAParams()
# 聚合器
device = PDFPageAggregator(resource, laparams=params)
# 创建PDF页面解析器
interpreter = PDFPageInterpreter(resource, device)

# 使用文档对象得到页面的集合
for page in doc.get_pages():
    interpreter.process_page(page)
    layout = device.get_result()

    for out in layout:
        if hasattr(out, "get_text"):
            print(out.get_text())
