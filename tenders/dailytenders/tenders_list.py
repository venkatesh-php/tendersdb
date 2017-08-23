from bs4 import BeautifulSoup
import urllib.request
import lxml

website_list = ['https://arunachaltenders.gov.in/nicgep/app',
                'https://assamtenders.gov.in/nicgep/app',
                'https://etenders.kerala.gov.in/nicgep/app',
                'https://etenders.hry.nic.in/nicgep/app',
                'https://hptenders.gov.in/nicgep/app',
                'https://jharkhandtenders.gov.in/nicgep/app',
                'https://jktenders.gov.in/nicgep/app',
                'https://mahatenders.gov.in/nicgep/app',
                'https://manipurtenders.gov.in/nicgep/app',
                'https://meghalayatenders.gov.in/nicgep/app',
                'https://nagalandtenders.gov.in/nicgep/app',
                'https://tendersodisha.gov.in/nicgep/app',
                'https://eproc.rajasthan.gov.in/nicgep/app',
                'https://sikkimtender.gov.in/nicgep/app',
                'https://tripuratenders.gov.in/nicgep/app',
                'http://uktenders.gov.in/nicgep/app',
                'https://etender.up.nic.in/nicgep/app',
                'https://wbtenders.gov.in/nicgep/app']

for list in website_list:
    html = urllib.request.urlopen(list)
    bsObj = BeautifulSoup(html, 'html.parser')
    nameList = bsObj.find('table', {'id' : 'activeTenders'})
    print(nameList.get_text())
    saveFile = open('model.txt', 'a')
    saveFile.write(str(nameList.get_text()))
saveFile.close()
