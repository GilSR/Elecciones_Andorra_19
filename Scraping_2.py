#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 01:15:05 2019

@author: Gil
File: Scraping_2.py
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import csv

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

llista=list()
PS_count=0
Li_count=0
DA_count=0
TV_count=0


url = 'https://forum.ad/category/politica/page/2'
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

tags = soup('h2')

for tag in tags:
    llista.append(tag.string)

    
for x in llista:
    PS=x.find('PS')
    PS_1=x.find('López')
    PS_2=x.find("d’Acord")
    PS_3=x.find("socialdemòcrates")
    if PS != -1 or PS_1 !=-1 or PS_2 !=-1:
        PS_count=PS_count+1
        PS=-1
        PS_1=-1
        PS_3=-1
    
    Li=x.find('Liberals')
    Li_1=x.find('Gallardo')
    Li_2=x.find("L'A")
    
    if Li != -1 or Li_1 !=-1 or PS_2 !=-1 or Li_2 !=-1:
        Li_count=Li_count+1
        Li =-1
        Li_1 =-1
        PS_2=-1
        Li_2 =-1
    
    DA=x.find('DA')
    DA_1=x.find('Demòcrates')
    DA_2=x.find('Espot')
    
    if DA !=-1 or DA_1 !=-1 or DA_2 !=-1:
        DA_count = DA_count+1
        DA=-1
        DA_1=-1
        DA_2=-1
    
    TV=x.find('TERCERAVIA')
    TV_1=x.find('Pintat')
    TV_2=x.find('Terceravia')    
    
    if TV !=-1 or TV_1 !=-1 or TV_2 !=-1 :
        TV_count=TV_count+1
        TV=-1
        TV_1=-1
        TV_2=-1

row1 = ["Forum.ad", "Partit Socialdemòcrata", PS_count]
row2= ["Forum.ad", "Liberals d'Andorra", Li_count]
row3= ["Forum.ad", "Demòcrates", DA_count]
row4= ["Forum.ad", "TERCERAVIA", TV_count]

with open('DATA.csv', 'a') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(row1)
    writer.writerow(row2)
    writer.writerow(row3)
    writer.writerow(row4)

csvFile.close()


