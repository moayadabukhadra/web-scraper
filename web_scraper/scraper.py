import requests
from bs4 import BeautifulSoup

def get_citations_needed_count(url):
    if 'wikipedia.org' in url:
        site=requests.get(url)
        soup=BeautifulSoup(site.content,'html.parser')
        citaions=[]
        
        for p in soup.find("div",class_="mw-parser-output").find_all("p"):
            for a in p.find_all('a', title="Wikipedia:Citation needed"):
                citaions.append(a)


        print(f'citaions needed = {len(citaions)}')
        return len(citaions)
    else :
        raise(Exception("This is not a Wikipedia page "))

def  get_citations_needed_report(url):
    if 'wikipedia.org' in url:
        text=[]
        site=requests.get(url)
        soup=BeautifulSoup(site.content,'html.parser')
        
        for p in soup.find("div",class_="mw-parser-output").find_all("p"):
            for a in p.find_all('a', title="Wikipedia:Citation needed"):
                text.append(p.text)
                
        output=''
        for string in text :
            output +=f'{string} \n'
        if output=='':
            output= "No citation needed"
            print(output)
            return output
        print(output)
        return output
    else :
        raise(Exception("This is not a Wikipedia page "))

if __name__ == "__main__":
    url="https://en.wikipedia.org/wiki/History_of_Mexico"
    get_citations_needed_count(url)
    get_citations_needed_report(url)