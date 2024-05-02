
# for pdf based
import PyPDF3
import pyttsx3
import pdfplumber
# for GUI
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter.filedialog import askopenfile
# for Images
from PIL import ImageTk, Image
# for creating the thresh
from threading import Thread


def convert():

    def converttoaudio():
        success.config(text='Extracting the text.....')
        try:
            pdf = open(pdf_file, 'rb')
            pdfreader = PyPDF3.PdfFileReader(pdf)

            pages = pdfreader.numPages
            finaltext = ''

            with pdfplumber.open(pdf_file) as pdf:
                for i in range(0, pages):
                    page = pdf.pages[i]
                    text = page.extract_text()
                    finaltext += text
        except:
            location.config(text='Problem Opening the file')

        success.config(text='Converting Please Wait.....')
        engine = pyttsx3.init()
        engine.save_to_file(finaltext, 'audio/audiobook.mp3')

        success.config(text='Successfully Converted...  :)')

        engine.runAndWait()

    thread = Thread(target=converttoaudio)
    thread.start()


def music():
    global pdf_file
    file = askopenfile(mode='r', filetypes=[('pdf files', '*.pdf')])
    pdf_file = file.name

    location.config(text=pdf_file)

    convert_btn = ttk.Button(text='Convert', command=convert)
    convert_btn.place(x=200, y=300)


root = tk.Tk()
root.geometry('500x600')
root.resizable(False, False)
root.title('PDF TO AUDIO')
root.config(bg='#f8c8dc')

image = ImageTk.PhotoImage(Image.open('images/pdftoaudio.jpeg'))
panel = tk.Label(root, image=image)
panel.place(x=100, y=20)

text1 = tk.Label(text='Please Select the pdf file to convert', font=('Arial', 13, 'bold'), bg='#f8c8dc')
text1.place(x=100, y=200)

btn1 = ttk.Button(text='Select', takefocus=True, command=music)
btn1.place(x=200, y=230)

location = tk.Label(text='', font=('Tahoma', 8), bg='#f8c8dc')
location.place(x=10, y=260)

success = Label(text='', font=('Tahoma', 10), bg='#f8c8db')
success.place(x=200, y=320 )




root.mainloop()
