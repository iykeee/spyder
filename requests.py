import urllib.request
#import requests
import ssl
import sys
import os

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

class req:
    def __init__ (self, url):
        self.url = url

    def htmlGenerator (self, url=input("Enter url: ")):
        if (type(url) is not str): 
            print(f"Error, {url} is not a valid input \n Kindly enter valid url")
            sys.exit(1) 

        while True:
            htmlHandle = None
            
            try:                
                try:
                    with urllib.request.urlopen(url) as htmlFile:
                        htmlHandle = htmlFile.read()
                        #os.remove("htmlHandle.html")
                        #fileHandle = open(f"htmlHandle.html", "wb")
                        #fileHandle.write(htmlHandle)
                        #fileHandle.close()
                        break
                except:
                    print(f"{url} access failed!!!")
                    sys.exit(1)
            except KeyboardInterrupt:
                print("Program interrupeted by user \n All Done!")
                break
        return htmlHandle

#animepahe = req.htmlGenerator(req, "https://google.com")

#socket.gaierror