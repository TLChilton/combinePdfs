#! python3
# combinePdfs.py - combines all pdf files in a directory into a single pdf
# Created by Thomas Chilton
import PyPDF2, os, traceback
from colorama import init
init()

# Collects all pdf file names into a list
pdfFiles = []
for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)
pdfFiles.sort(key = str.lower)
pdfWriter = PyPDF2.PdfFileWriter()


if (pdfFiles): # if pdfs exist
    # Add each pdf to pdfWriter
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

    # Combined PDF file creation
    print('\u001b[95mPlease enter a name for the combined PDF file: \u001b[0m', end='')
    savedFile = input()
    # If the user didn't include a .pdf extension add it at the end
    if savedFile.endswith('.pdf') == False:
        savedFile = savedFile + '.pdf'
    savedFile = os.path.abspath(savedFile)
    # If the file name already exists ask the user for a new one
    while os.path.exists(savedFile):
        print('\u001b[95mERROR: \u001b[93m' + savedFile + ' already exists, \n\u001b[95mPlease enter a new name: \u001b[0m', end= '')
        savedFile = input()
        if savedFile.endswith('.pdf') == False:
            savedFile = savedFile + '.pdf'
        savedFile = os.path.abspath(savedFile)
    print('Combined pdf saving as ' + savedFile)
    try:
        pdfOutput = open(savedFile, 'wb')
        pdfWriter.write(pdfOutput)
        pdfOutput.close()
    except: # If the combined pdf fails to save then save the error report as a .txt
        errorFile = open('errorInfo.txt', 'w')
        errorFile.write(traceback.format_exc())
        errorFile.close()
        print('\u001b[91mFatal error encountered. Traceback info written to errorInfo.txt.\u001b[0m')
    print('Hit enter to close')
    input()
else: # If no pdfs are found tell the user then end the program
    print('No pdfs found in ' + os.getcwd())
    print('Hit enter to close')
    input()
