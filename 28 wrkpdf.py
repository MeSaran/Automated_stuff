#!/usr/bin/python
import PyPDF2
pdfobj=open('MCA 101 MFC.pdf','rb')
pdfReader=PyPDF2.PdfFileReader(pdfobj)
print('No of pages: '+str(pdfReader.numPages))
pageobj=pdfReader.getPage(1)
print('Contents:'+pageobj.extractText())
newfile=open('fil.txt','w')
newfile.write(pageobj.extractText())
newfile.close()

