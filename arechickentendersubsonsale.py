# arechickentendersubsonsale.py
import tkinter as tk
from tkinter import *
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from functools import partial

''' Purpose: The people need to know if Publix chicken tender subs are on sale. I also wanted to mess around with tkinter. '''

def main():
    # Tkinter window
    root = tk.Tk()

    # Website to parse for the sale
    url = 'http://arepublixchickentendersubsonsale.com'

    # gifs
    yes = tk.PhotoImage(file="yes.gif")
    no = tk.PhotoImage(file='no.gif')

    # find_tenders is either going to return True (if the sub is on sale) or False, here I'm storing the results
    tenderBoolean = find_tenders(url)

    # Main label
    TenderButton = Button(root, text="ARE CHICKEN TENDER SUBS ON SALE???", command= lambda : on_sale(tenderBoolean,root, yes, no))
    TenderButton.pack()

    #coloring the GUI bg
    root['background'] = '#44943d'

    # Keep the GUI open
    root.mainloop()

def find_tenders(url):
    # opening up a connection, grabbing the page
    uClient = uReq(url)
    # stores the html file to a variable
    page_html = uClient.read()
    uClient.close()
    # Parsing the html and then converting it into a string
    results = str(soup(page_html, "html.parser"))
    # Splitting that string to find the commented out section through string manipulation because Selenium doesn't
    # support finding html comments
    re = results.split()
    if 'onsale:yes' in re:
        return True
    else:
        return False

# If tenderBoolean is true we print out "Yes!" otherwise "Nope." with the appropriate gifs
def on_sale(tenderBoolean, root,yes, no):
    if tenderBoolean:
        print("Yes!")
        onsale = tk.Label(root, image=yes).pack()
    else:
        print("Nope.")
        notonsale = tk.Label(root, image=no).pack()

if __name__ == '__main__':
    main()



