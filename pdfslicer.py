#! /usr/bin/env python3
from PyPDF2 import PdfFileReader, PdfFileWriter
import sys, os

def newPDFfromList(pageList, name):
    writer = PdfFileWriter()
    # TODO: Need to be the reverse order of pageList
    reversePageList = pageList[::-1]
    for page in reversePageList:
        writer.insertPage(page)

    writer.write(open(name, "wb"))

def doSplitPdf(filename):
    # Get aula05.pdf file srteam
    myPdfFile = open(filename, "rb")
    pdfReader = PdfFileReader(myPdfFile)
    pageListEven = []
    pageListOdd  = []
    for num in range(pdfReader.getNumPages()):
        if num % 2 == 0:
            pageListEven.append(pdfReader.getPage(num))
        else:
            pageListOdd.append(pdfReader.getPage(num))
        # Write the files
        
        newPDFfromList(pageListEven, filename[0:-4] + ".even.pdf")
        newPDFfromList(pageListOdd, filename[0:-4]  + ".odd.pdf")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: pdfslicer filename")
        exit(-1)
    else:
        filename = sys.argv[1]
        #Check if file exists
        if os.path.isfile(filename):
            print("Generating pdfs")
            doSplitPdf(filename)
            print("Complete")
        else:
            print(filename + "file doesn't exists")
            exit(-2)
