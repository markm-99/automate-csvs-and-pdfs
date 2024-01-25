# We can only read from pdf files
import PyPDF2
# rb = read binary
f = open('Working_Business_Proposal.pdf', 'rb') 
# f = open('Mark_Mathew_Resume.pdf', 'rb') 
pdf_reader = PyPDF2.PdfReader(f)

numPages = len(pdf_reader.pages)
print(numPages)

page_one = pdf_reader.pages[0]
page_one_text = page_one.extract_text()
print(page_one_text)

first_page = pdf_reader.pages[0]
pdf_writer = PyPDF2.PdfWriter()
type(first_page)
pdf_writer.add_page(first_page)
pdf_output = open('Some_BrandNew_Doc.pdf', 'wb')

pdf_writer.write(pdf_output)

pdf_text = []
pdf_reader = PyPDF2.PdfReader(f)

for page in pdf_reader.pages:
    pdf_text.append(page.extract_text())
    # print(page)
    print(pdf_text[0])
