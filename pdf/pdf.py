import PyPDF2
import sys


def watermark(inputFiles, wmFile, outputDir):
    for inputFile in inputFiles:
        with open(inputFile, 'rb') as inputFileOpened:
            pdf = PyPDF2.PdfFileReader(inputFileOpened)

            with open(wmFile, 'rb') as watermarkOpened:
                wm = PyPDF2.PdfFileReader(watermarkOpened).getPage(0)
                pdfWriter = PyPDF2.PdfFileWriter()

                for page in pdf.pages:
                    page.mergePage(wm)
                    pdfWriter.addPage(page)

                with open(f'{outputDir}/{inputFile}', 'wb') as outputFileOpened:
                    pdfWriter.write(outputFileOpened)


if __name__ == '__main__':
    inputFiles = sys.argv[1:]
    watermark(inputFiles, wmFile='draft.pdf', outputDir='output')