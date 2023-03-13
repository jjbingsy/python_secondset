#import def1
from bs4 import BeautifulSoup
import requests
import os
import glob
import sqlite3



database1 = 'tinventory.db'

def collect_series():
    update1 = 'update Videos set fullpath = ? where film = ?'
    query1 = "select idol_id from idols where link2 like ?"
    garbage = list()
    only_series = list()
    cn = sqlite3.connect(database1)
    cr = cn.cursor()
    cr.execute("select film, link2, html2 from videos where length(html2) > 20")
    guru_list = cr.fetchall()
    for jl in guru_list:
        #print (jl[0])
        msoup = BeautifulSoup(jl[2], 'lxml')
        s = msoup.find('div', class_='infoleft')
        for r in s.find_all('a', rel='tag'):
            if "guru/series/" in r['href']:
                for e in r.stripped_strings:
                    nameI = e
                    linkI = r['href']
                    nameF = jl[0]
                    linkF = jl[1]
                    rawdesc = linkF.split('/')[-2]
                    description = rawdesc.replace (nameF.lower() + '-', '').replace('-', " ")
                    #print (i)
                    tp1 = nameF, description, linkI.split('/')[-2]
                    garbage.append (tp1)
                    tp2 = linkI.split('/')[-2],
                    only_series.append (tp2)


                    #print (linkI.split('/')[-2], e, nameF)
                    #trq2 = nameF, linkF, nameI, linkI
                    #cr.execute (insert1, trq2)
                    cn.commit()
    cn.close()
    return garbage, only_series


if __name__ == '__main__':
    print ("I start from here.")
    garbage, only_series  = collect_series()

    conn = sqlite3.connect("Series230209.db")    
    cr = conn.cursor()
    LL = list()
    dupli = ['IPX-666', 'JUL-195', 'JUL-252', 'JUL-188', 'JUL-859', 'MIAA-076', 'JUL-863', 'MIAE-281', 'MEYD-582']
    for name, desc, series in garbage:
        i = name, desc, series
        if name not in dupli:
            cr.execute ( "insert into films (film_name, film_description, series_id) VALUES (?, ?, (select series_id from series where series_name = ?))" , i)
    conn.commit()
    conn.close()

    print ("I start from here.")



    #for a in only_series:
    #    print (a)
