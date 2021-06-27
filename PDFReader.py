import pyttsx3 
import pyPDF2
book = open('C:\\Users\\SAI KIRAN\\Documents\\3-2\\netwoking programing','rb')
pdfReader = pyPDF2.pdfFileReader(book)
pages = pdfReader.numpages
print(pages)
speaker = pyttsx3.init()
page = pdfReader.getpage(9)
text = page.extractText()
speaker.say(text)
speaker.runAndWait()
