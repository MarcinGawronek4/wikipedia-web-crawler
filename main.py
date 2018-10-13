import requests
from bs4 import BeautifulSoup


def wikipediaCrawler(page, count):
        pages = []
        url = "https://en.wikipedia.org" + page
        sourceCode = requests.get(url)
        print(sourceCode)
        plainText = sourceCode.text
        soup = BeautifulSoup(plainText, "html.parser")
        see_also = soup.select("h2 > #See_also")[0]
        ul = see_also.parent.find_next_sibling("ul")
        print(url)
        try:
            for link in ul.findAll('a'):
                pages.append(str(link.get('href')))
            for a in pages:
                if "/wiki/" not in a:
                    errors = True
                    break
                else:
                    errors = False
            if errors is True:
                del pages[:]
                div = see_also.parent.find_next_sibling("div")
                for li in div.findAll("li"):
                    print('li: ', li.get_text())
                for link in div.findAll('a'):
                    pages.append(str(link.get('href')))
                print(pages)
            else:
                for li in ul.findAll("li"):
                    print('li: ', li.get_text())
                print(pages)


        except AttributeError:
            print("No links found")
        if count > 0:
            for href in pages:
                try:
                    try:
                        wikipediaCrawler(href, count-1)

                    except IndexError:
                        continue
                except requests.exceptions.ConnectionError:
                    continue




wikipediaCrawler("/wiki/Online_chat", 2)




