import PyPDF2, os

print(os.getcwd())
fileName1 = os.getcwd() + "/" + "meetingminutes1.pdf"
fileName2 = os.getcwd() + "/" + "meetingminutes2.pdf"
pdfFile1 = open(fileName1, "rb")
pdfFile2 = open(fileName2, "rb")
reader1 = PyPDF2.PdfFileReader(pdfFile1)
reader2 = PyPDF2.PdfFileReader(pdfFile2)

print(reader1.numPages)

for i in range(reader1.numPages):
    print(reader1.getPage(i).extractText())

writer = PyPDF2.PdfFileWriter()
for i in range(reader1.numPages):
    page = reader1.getPage(i)
    writer.addPage(page)

for i in range(reader2.numPages):
    page = reader2.getPage(i)
    writer.addPage(page)

outputFileName = os.getcwd() + "/" + "outputFile.pdf"
outputFileStream = open(outputFileName, "wb")
writer.write(outputFileStream)
outputFileStream.close()
pdfFile1.close() 
pdfFile2.close()