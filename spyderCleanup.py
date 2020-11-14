import sqlite3
import html
from bs4 import BeautifulSoup
from requests import req

#soup = BeautifulSoup("<p>Some<b>bad<i>HTML", features="html.parser")
#print(soup.prettify())

fileHandle = None

class cleanup:

    def __init__ (self, fileHandle):
        self.htmlHandle = fileHandle

    def scrape (self):

        conn = sqlite3.connect('cleanup.sqlite')
        cur = conn.cursor()

        cur.execute('''DROP TABLE IF EXISTS Spyder''')
        cur.execute('''CREATE TABLE IF NOT EXISTS Spyder (id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, links TEXT UNIQUE)''')


        htmlHandle = open("htmlHandle.html")
        htmlTree = htmlHandle.read()

        soup = BeautifulSoup(htmlTree, features="html5lib")
        print(f"Retrieving all tags from html handle\n Kindly wait... \n Loading...\n All Done!")

        #look for anchor tags in doc.
        
        anchorTags = soup('a')
        print(f"Retrieving all anchor tags from html handle\n Kindly wait... \n Loading...\n All Done!")

        print("Generating link...")
        num = 1
        for links in anchorTags:
            links = links.get("href", None)
            if ( links is None ) : continue
            
            print(f"{num} Getting Link... {links}")
            links = str(links)
            cur.execute('INSERT OR IGNORE INTO Spyder (links) VALUES (? )', (links, ) )
            conn.commit()
            num = num + 1
        
        cur.close()
        return True




