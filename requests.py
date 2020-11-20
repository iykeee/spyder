import urllib.request
import ssl
import sys
import os


class req:
    def __init__ (self, url):
        self.url = url

    def htmlGenerator (self, url):
        if (type(url) is not str): 
            print(f"Error, {url} is not a valid input \n Kindly enter valid url")
            sys.exit(1) 

        # Ignore SSL certificate errors
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        while True:
            htmlHandle = None
            
            try:                
                try:
                    with urllib.request.urlopen(url) as htmlFile:
                        htmlHandle = htmlFile.read()
                        break
                except:
                    print(f"{url} access failed!!!")
                    sys.exit(1)
            except KeyboardInterrupt:
                print("Program interrupeted by user \n All Done!")
                break
        return htmlHandle

