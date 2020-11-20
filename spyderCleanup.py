import sqlite3
import html
from bs4 import BeautifulSoup
from requests import req
import webbrowser

fileHandle = None

class cleanup(req):

    def __init__ (self, fileHandle):
        self.htmlHandle = fileHandle

    def scrape (self, htmlTree):

        conn = sqlite3.connect('cleanup.sqlite')
        cur = conn.cursor()

        cur.execute('''DROP TABLE IF EXISTS Spyder''')
        cur.execute('''CREATE TABLE IF NOT EXISTS Spyder (id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, links TEXT UNIQUE)''')

        soup = BeautifulSoup(htmlTree, features="html5lib")
        #print(f"Retrieving all tags from html handle\n Kindly wait... \n Loading...\n All Done!")

        #look for anchor tags in doc.
        
        anchorTags = soup('a')
        #print(f"Retrieving all anchor tags from html handle\n Kindly wait... \n Loading...\n All Done!")

        print("Generating links...")
        num = 1
        link = list()


        for links in anchorTags:
            links = links.get("href", None)
            if ( links is None ) : continue
            
            #print(f"{num} Getting Link... {links}")
            links = str(links)
            cur.execute('INSERT OR IGNORE INTO Spyder (links) VALUES (? )', (links, ) )
            conn.commit()
            num = num + 1
            link.append(links)
            #webbrowser.open_new_tab(links)

        
        cur.close()
        return link
