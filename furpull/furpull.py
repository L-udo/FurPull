import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
import time
import random
import requests
import os

# CODE WRITTEN AND COMPILED BY LUDO you can find me on instagram at @ludo_the_wusky or on Twitter @Ludo_Dash

#image downloading stage


def image_discov():
    #collecting imformation needed to start scraping
    x = 0
    a = open("Unfiltered_Output.txt", "a")
    print("Chrome Driver (may or may not work with Firefox but is untested):")

    cd = input("░▒▓█OWO█▓▒░:")

    while x < 40:
        x = x + 1
        print("\n")
    x = 0

    print("How many pages deep to scrape(Normally 63. only change number to be higher if furafinity updates/changes it)(Hit Enter for default)")

    f = input("░▒▓█OWO█▓▒░:")

    while x < 40:
        x = x + 1
        print("\n")
    x = 0

    print("Search Term(s)")
    fa_url = "https://www.furaffinity.net/search/?q=" + input("░▒▓█OWO█▓▒░:").replace(" ","+")

    while x < 40:
        x = x + 1
        print("\n")
    x = 0

    print("Time delay for loading page(3 seconds for moderate internet speeds, higher if your internet is slower)")

    t = int(input("░▒▓█OWO█▓▒░:"))

    while x < 40:
        x = x + 1
        print("\n")
    x = 0

    login_url = "https://www.furaffinity.net/login"
    driver = webdriver.Chrome(cd)
    driver.get(login_url)


    print(" if you want to allow 🅽 🆂 🅵 🆆 content you need to login then hit enter if not hit enter")
    
    input("░▒▓█OWO█▓▒░")

    while x < 40:
        x = x + 1
        print("\n")
    x = 0


    driver.get(fa_url)

    print("░▒▓█OWO█▓▒░ if you are wanting to set custom filters for the web search please do so now then hit Enter ░▒▓█OWO█▓▒░")

    input("░▒▓█OWO█▓▒░")
    
    while x < 40:
        x = x + 1
        print("\n")
    x = 0

    print("░▒▓█OWO█▓▒░ Please do not scroll or interact with the webpage while Furpull is running thank you ^ ^ ░▒▓█OWO█▓▒░")


    def wrn_msg():
        k = 0
        while k < 40:
            k = k + 1
            print("\n")
        k = 0
        print("░▒▓█OWO█▓▒░ Please do not scroll or interact with the webpage while Furpull is running thank you ^ ^ ░▒▓█OWO█▓▒░")



    #starting search
    x = 0
    g = 0
    if f == "":
        g = 63
    else:
        g = f


    while x < int(g):
        x = x + 1
        wrn_msg()
        print("page", x , "/"+ str(g) )
        try:
            images = driver.find_elements_by_tag_name('img')
        except:
            pass     
        for image in images:
            try:
                imag = image.get_attribute('src')
                a.write(imag + "\n")
            except:
                pass
        time.sleep(t)

        nex_page = driver.find_element_by_name("next_page")
        nex_page.click()

    driver.close()

image_discov()


#filtering urls found, output to file and download images
def filter_and_output():
    print("Filtering Output...")

    open('output.txt','w').writelines(line for line in open('Unfiltered_Output.txt') if "https://t.facdn.net/" in line)

    print("Done!")


    def file_lengthy(fname):
            with open(fname) as f:
                    for i, l in enumerate(f):
                            pass
            return i + 1
    print("Number of Images Found: ",file_lengthy("output.txt"))
    f_len = file_lengthy("output.txt")

    urls = open('output.txt')
    print("downloading images")


    x = 0
    path = os.getcwd()
    for lines in urls:
        x = x + 1
        img = requests.get(lines.strip('\n'))
        img_name = "image" + str(x) + ".png"
        file = open( path + "\img_out/" + img_name, "wb")
        file.write(img.content)
        file.close()
        print("Downloading Image", str(x), "of", f_len )

    print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKc..0MMMMM\
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNd.   .dXMMM\
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNk.      .XMMM\
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWO.        oWMMM\
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMO.        .xMMMM\
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM0.          dWMMM\
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWO.           lWMMM\
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWx.            .XMMM\
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWx...           .0MMM\
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKkl.           .dWMM\
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXx.              .0MM\
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN0o.                .kMM\
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWN0xc..                 .xXMM\
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNKxl...                     .0MMM\
    MMMMMMMMMMMMMMMMMMMMMMMMMMMWX0Okdlc....                          .kMMM\
    MMMMMMMMMMMMMMMMMMMMMWNKkdc...                                   .xMMM\
    MMMMMMMMMMMMMMMWX0kdc...                                         .KMMM\
    MMMMMMMMMNKOkdc...                                               oWMMM\
    MMMMMMNOl..                                                     .lNMMM\
    MMMMWO.                                                        .xXWMMM\
    MMMNx.                                                         .0MMMMM\
    MMNo.                                                          .0MMMMM\
    MWd.                       .cdol.....                         .OWMMMMM\
    MK.                        .kWMMWXK00Oxo..                   cNMMMMMMM\
    MO.                         .KMMMMMMMMMMWKd.....            .xMMMMMMMM\
    MO.                         .oNMMMMMMMMMMMMWXKXk.           .0MMMMMMMM\
    M0.                          .dWMMMMMMMMMMMMMMMK.    ...    cNMMMMMMMM\
    M0.      .                    oWMMMMMMMMMMMMMMMK.   .x0.   .xMMMMMMMMM\
    Mk.     ...       .cOd.      .0MMMMMMMMMMMMMMMM0.   cXk.   .KMMMMMMMMM\
    Wo     .c.      .l0WMW0.     oWMMMMMMMMMMMMMMMWo.  .0Nl    oWMMMMMMMMM\
    Nc      .     .c0WMMMMWd    .OMMMMMMMMMMMMMMMMO.  .xWO.   .0MMMMMMMMMM\
    Wo.         .l0WMMMMMMWo     .kNMMMMMMMMMMMMMK.   lNNc    oWMMMMMMMMMM\
    MNOx.     .dKWMMMMMMMMMNk..    .0WMMMMMMMMMMWd.  .OM0.   .dWMMMMMMMMMM\
    MMMK.  ..ONMMMMMMMMMMMMMMW0c.   .kWMMMMMMMMMMk.  .KMNd.   .NMMMMMMMMMM\
    MMMO. .oNMMMMMMMMMMMMMMMMMMWO.   .ldONMMMMMMW0.  .d0Od.   .cx0NWMMMMMM\
    MMMx. .XMMMMMMMMMMMMMMMMWWMMMXl.     .cox00x..               ...oONMMM\
    MMNl  lWMMMMMMWWWNXKOxo..lKKOkl.         .                       ..lON\
    MM0.  .ONKkoc.......      ..                                        .c\
    MMk.   ... ")

    print("DONE!")

filter_and_output()