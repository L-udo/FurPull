import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
import time
import random
import requests
import os

# CODE WRITTEN AND COMPILED BY LUDO you can find me on instagram at @ludo_the_wusky or on Twitter 

#setup
path = os.getcwd()
print("Checking requirements!")
try:
    open(path + "\img_out/" + "placeholder.txt", "wb")

except:
    print("An Error Occored when trying to open the folder 'img_out'... Are you sure you created the folder within the CWD?")
    exit()

print("Checks PASSED!")


def image_discov():
    #collecting imformation needed to start scraping
    x = 0
    output_file = open("Unfiltered_Output.txt", "a")

    cd = os.getcwd() + "/" + "chromedriver.exe"

    while x < 40:
        x = x + 1
        print("\n")
    x = 0

    print("How many pages deep to scrape(Normally 63. only change number to be higher if furafinity updates/changes it)(Hit Enter for default)")

    Num_of_pages = input("░▒▓█OWO█▓▒░:")

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

    web_delay_load = int(input("░▒▓█OWO█▓▒░:"))

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



    #set default page number value
    if Num_of_pages == "":
        Num_of_pages = 63

    #start Scraping image urls sequentially
    x = 0
    while x < int(Num_of_pages):
        x = x + 1
        wrn_msg()
        print("page", x , "/"+ str(Num_of_pages) )
        try:
            images = driver.find_elements_by_tag_name('img')
        except:
            pass     
        for image in images:
            try:
                imag = image.get_attribute('src')
                output_file.write(imag + "\n")
            except:
                pass
        time.sleep(web_delay_load)

        next_page = driver.find_element_by_name("next_page")
        next_page.click()

    driver.close()

image_discov()


#filtering urls down to just the post urls
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

    #downloading Images
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
