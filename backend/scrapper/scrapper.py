import requests
from bs4 import BeautifulSoup
import time
import json

def praskaj_tus_hranilne_vrednosti(url_kataloga):
    # Dodamo Header, da se predstavimo kot običajen brskalnik (prepreči blokade)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    
    print(f"1. Prenašam seznam izdelkov z zbirne strani...")
    odgovor = requests.get(url_kataloga, headers=headers)
    
    if odgovor.status_code != 200:
        print(f"Napaka pri dostopu do strani. Koda: {odgovor.status_code}")
        return []

    soup = BeautifulSoup(odgovor.text, 'html.parser')
    
    # Poiščemo vse povezave do posameznih izdelkov
    # Uporabimo set(), da se znebimo podvojenih povezav (npr. slika in naslov pogosto vodita na isti link)
    povezave_izdelkov = set()
    for a_znacka in soup.find_all('a', href=True):
        href = a_znacka['href']
        if 'https://www.tus.si/aktualno/akcijska-ponudba/aktualno-iz-kataloga/page/2/?swoof=1&product_cat_m=zamrznjeno%2Csladko-in-slano%2Calkoholne-pijace%2Cbrezalkoholne-pijace%2Chlajeni-in-mlecni-izdelki%2Ckruh-in-pekovski-izdelki%2Cmednarodna-hrana%2Cmeso-delikatesa-in-ribe%2Csadje-in-zelenjava%2Cshramba' in href:
            povezave_izdelkov.add(href)
            
    povezave_izdelkov = list(povezave_izdelkov)
    print(f"Najdenih {len(povezave_izdelkov)} unikatnih izdelkov. Začenjam iskanje podrobnosti...\n")
    
    vsi_podatki = []
