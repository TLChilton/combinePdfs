#! python3
# combinePdfs.py
# Created by Thomas Chilton
import PyPDF2, os, traceback
from colorama import init
init()

pdfFiles = []
for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)
pdfFiles.sort(key = str.lower)
pdfWriter = PyPDF2.PdfFileWriter()

if (pdfFiles):
    for filename in pdfFiles:
        print('Adding pdf file ' + filename)
        try:
            pdfFileObj = open(filename, 'rb')
            pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
            for pageNum in range(0, pdfReader.numPages):
                pageObj = pdfReader.getPage(pageNum)
                pdfWriter.addPage(pageObj)
        except PyPDF2.utils.PdfReadError:
            print ('Error: ' + filename + ' is encrypted')
    print('\u001b[95mPlease enter a name for the combined PDF file: \u001b[0m', end='')
    savedFile = input()
    if savedFile.endswith('.pdf') == False:
        savedFile = savedFile + '.pdf'
    savedFile = os.path.abspath(savedFile)
    while os.path.exists(savedFile):
        print('\u001b[95mERROR: ' + savedFile + ' already exists, \nPlease enter a new name: \u001b[0m', end= '')
        savedFile = input()
        if savedFile.endswith('.pdf') == False:
            savedFile = savedFile + '.pdf'
        savedFile = os.path.abspath(savedFile)
    print('Combined pdf saving as ' + savedFile)
    try:
        pdfOutput = open(savedFile, 'wb')
        pdfWriter.write(pdfOutput)
        pdfOutput.close()
    except:
        errorFile = open('errorInfo.txt', 'w')
        errorFile.write(traceback.format_exc())
        errorFile.close()
        print('\u001b[91mFatal error encountered. Traceback info written to errorInfo.txt.\u001b[0m')
    print('Hit enter to close')
    input()
else:
    print('No pdfs found in ' + os.getcwd())
    print('Hit enter to close')
    input()
