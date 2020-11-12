import sqlite3
import html
from bs4 import BeautifulSoup
#soup = BeautifulSoup("<p>Some<b>bad<i>HTML", features="html.parser")
#print(soup.prettify())

fileHandle = None

class cleanup:
    def __init__ (self, fileHandle):
        self.htmlHandle = fileHandle

    def scrape (self, htmlHandle):
        while True:
            if (type(htmlHandle) is not str):
                print(f"{htmlHandle} is not a valid file name \n Kindly enter correct file name in .html format")
                continue
            else:
                print(f"{htmlHandle} is OK!")
                break
        
        htmlTree = open(htmlHandle)
        print(htmlTree)

        soup = BeautifulSoup(htmlTree, features="html.parser")
        anchorTags = None
        print(f"Retrieving all tags from {htmlHandle}\n Kindly wait... \n Loading...\n All Done!")

        #look for anchor tags in doc.
        anchorTags = soup('a')
        print(f"Retrieving all anchor tags from {htmlHandle}\n Kindly wait... \n Loading...{anchorTags}\n All Done!")

        print("Generating link...")
        num = 1
        for links in anchorTags:
            print(f"{num} Getting Link... {links}")
            num = num + 1
        
        return True




