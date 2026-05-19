import csv
import os
import requests
import re

###############################################################################
# Najprej definirajmo nekaj pomožnih orodij za pridobivanje podatkov s spleta.
###############################################################################

# definirajte URL glavne strani bolhe za oglase z mačkami
cats_frontpage_url = 'http://www.bolha.com/zivali/male-zivali/macke/'
# mapa, v katero bomo shranili podatke
cat_directory = 'podatki'
# ime datoteke v katero bomo shranili glavno stran
frontpage_filename = 'macke.html'
# ime CSV datoteke v katero bomo shranili podatke
csv_filename = 'macke.csv'

# KOMENTARJI:
# na spletni strani daš desni klik in view page source in shraniš v novo datoteko celotno html kodo strani - samo da preveriš, če ti je isto shranilo 
# try, except uporabimo, če je mogoče, da pride do napake - izvede se try, če je napaka pa except
# če se modul(knjižnica) ne obarva, to pomeni, da ni naložena in jo naložiš v terminalu: python -m pip install ___
# ko enkrat imaš podatke, jih shrani v datoteko in jih potem jih od tam obdeluj
# opazimo, da je posamezen oglas znotraj značke article
# ' na tipki za ?
 

def download_url_to_string(url):
    """Funkcija kot argument sprejme niz in poskusi vrniti vsebino te spletne
    strani kot niz. V primeru, da med izvajanje pride do napake vrne None.
    """
    try:
        # del kode, ki morda sproži napako
        headers = {"User-agent": "Chrome/147.0.7727.138"}  # (chrome: tri pikice -> help -> about google chrome - izpišeš številko)
        page_content = requests.get(url, headers=headers) # (če noče, program pretentaš s headers, da dostopaš iz brskalnika in ne iz programa)
    except requests.exceptions.RequestException:  # (ime razreda napake, ki jo pričakujemo)
        # koda, ki se izvede pri napaki
        # dovolj je če izpišemo opozorilo in prekinemo izvajanje funkcije
        print("Spletna stran ni dosegljiva")
        return None
    # nadaljujemo s kodo če ni prišlo do napake
    return page_content.text  # (brez .text je samo objekt)


def save_string_to_file(text, directory, filename):
    """Funkcija zapiše vrednost parametra "text" v novo ustvarjeno datoteko
    locirano v "directory"/"filename", ali povozi obstoječo. V primeru, da je
    niz "directory" prazen datoteko ustvari v trenutni mapi.
    """
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, filename)
    with open(path, 'w', encoding='utf-8') as file_out:
        file_out.write(text)
    return None


# Definirajte funkcijo, ki prenese glavno stran in jo shrani v datoteko.


def save_frontpage(page, directory, filename):
    """Funkcija shrani vsebino spletne strani na naslovu "page" v datoteko
    "directory"/"filename"."""
    page_content = download_url_to_string(page)
    save_string_to_file(page_content, directory, filename)


###############################################################################
# Po pridobitvi podatkov jih želimo obdelati.
###############################################################################


def read_file_to_string(directory, filename):
    """Funkcija vrne celotno vsebino datoteke "directory"/"filename" kot niz."""
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, filename)
    with open(path, 'r', encoding='utf-8') as file_in:
        text = file_in.read()
    return text


# Definirajte funkcijo, ki sprejme niz, ki predstavlja vsebino spletne strani,
# in ga razdeli na dele, kjer vsak del predstavlja en oglas. To storite s
# pomočjo regularnih izrazov, ki označujejo začetek in konec posameznega
# oglasa. Funkcija naj vrne seznam nizov.


def page_to_ads(page_content):
    """Funkcija poišče posamezne oglase, ki se nahajajo v spletni strani in
    vrne seznam oglasov."""
    return re.findall(r'<article class="entity-body cf">(.*?)</article>', page_content, flags=re.DOTALL)  # (flags=re.DOTALL omogoči iskanje findall čez več vrstic (. je lahko tudi znak za novo vrstico \n), .? naredi * nepožrešno, torej da ne poišče največje možne pojavitve, torej se ustavi pri prvem </article>)


# Definirajte funkcijo, ki sprejme niz, ki predstavlja oglas, in izlušči
# podatke o imenu, lokaciji, datumu objave in ceni v oglasu.


def get_dict_from_ad_block(block):
    """Funkcija iz niza za posamezen oglasni blok izlušči podatke o imenu, lokaciji, datumu
    in ceni ter vrne slovar, ki vsebuje ustrezne podatke."""
    ime = re.search(r'<h3 class="entity-title"><a .*?>(.*)</a></h3>', block)
    lokacija = re.search(r'Lokacija: </span>(.*)<br />', block)
    datum = re.search(r'pubdate="pubdate">(.*)\.</time>', block)  # \. ker je dejanska pika v datumu
    cena = re.search(r'<strong class="price price--hrk">(.*)</strong>', block, flags=re.DOTALL)
    if ime == None or lokacija == None or datum == None or cena == None:
        return None
    else:
        if "Cena po dogovoru" in cena.group(1):
            cena = "Cena po dogovoru"
        else:
            cena = re.search(r'(\d+)&nbsp;<span class="currency">(.*)</span>', cena.group(1))
            cena = cena.group(1) + " " + cena.group(2)
        return {"ime": ime.group(1), "lokacija": lokacija.group(1), "datum": datum.group(1), "cena": cena}

# Definirajte funkcijo, ki sprejme ime in lokacijo datoteke, ki vsebuje
# besedilo spletne strani, in vrne seznam slovarjev, ki vsebujejo podatke o
# vseh oglasih strani.


def ads_from_file(filename, directory):
    """Funkcija prebere podatke v datoteki "directory"/"filename" in jih
    pretvori (razčleni) v pripadajoč seznam slovarjev za vsak oglas posebej."""
    page_content = read_file_to_string(directory, filename)
    blocks = page_to_ads(page_content)
    ads = [get_dict_from_ad_block(block) for block in blocks]
    return [ad for ad in ads if ad != None]


###############################################################################
# Obdelane podatke želimo sedaj shraniti.
###############################################################################


def write_csv(fieldnames, rows, directory, filename):
    """
    Funkcija v csv datoteko podano s parametroma "directory"/"filename" zapiše
    vrednosti v parametru "rows" pripadajoče ključem podanim v "fieldnames"
    """
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, filename)
    with open(path, 'w', encoding='utf-8', newline="") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)
    return


# Definirajte funkcijo, ki sprejme neprazen seznam slovarjev, ki predstavljajo
# podatke iz oglasa mačke, in zapiše vse podatke v csv datoteko. Imena za
# stolpce [fieldnames] pridobite iz slovarjev.


def write_cat_ads_to_csv(ads, directory, filename):
    """Funkcija vse podatke iz parametra "ads" zapiše v csv datoteko podano s
    parametroma "directory"/"filename". Funkcija predpostavi, da so ključi vseh
    slovarjev parametra ads enaki in je seznam ads neprazen."""
    # Stavek assert preveri da zahteva velja
    # Če drži se program normalno izvaja, drugače pa sproži napako
    # Prednost je v tem, da ga lahko pod določenimi pogoji izklopimo v
    # produkcijskem okolju
    assert ads and (all(j.keys() == ads[0].keys() for j in ads))  # (assert je prevenjanje - trdimo, da je to izpolnjeno in če ni, bo javilo napako: trdimo, da je seznam definiran in imajo vsi oglasi v tem seznamu enake ključe)
    fieldnames = list(ads[0].keys())  # (imena stolpcev)
    write_csv(fieldnames, ads, directory, filename)


# Celoten program poženemo v glavni funkciji

def main(redownload=True, reparse=True):
    """Funkcija izvede celoten del pridobivanja podatkov:
    1. Oglase prenese iz bolhe
    2. Lokalno html datoteko pretvori v lepšo predstavitev podatkov
    3. Podatke shrani v csv datoteko
    """
    # Najprej v lokalno datoteko shranimo glavno stran
    if redownload:
        save_frontpage(cats_frontpage_url, cat_directory, frontpage_filename)  # (bolha nam javlja, da smo roboti)
    # Iz lokalne (html) datoteke preberemo podatk
    # Podatke preberemo v lepšo obliko (seznam slovarjev)
    # ads = ads_from_file(frontpage_filename, cat_directory)
    # print(ads) - (smo preverjali če pride prav)
    # Podatke shranimo v csv datoteko
    if reparse: # (če želimo ponovno izluščiti podatke iz datoteke)
        ads = ads_from_file(frontpage_filename, cat_directory)
        write_cat_ads_to_csv(ads, cat_directory, csv_filename)
    # Dodatno: S pomočjo parametrov funkcije main omogoči nadzor, ali se
    # celotna spletna stran ob vsakem zagon prenese (četudi že obstaja)
    # in enako za pretvorbo



if __name__ == '__main__':  # (če smo to datoteko pognali kot običajen program, bo poklical funkcijo main - če bi importali nekam, se main ne bi poklical)
    main(False)
