from pdf2docx import Converter

cv = Converter("sample.pdf")
cv.convert("output.docx", start=0, end=None)
cv.close()
