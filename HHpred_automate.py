#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 10:07:57 2018

@author: vassiliadisdane
"""

# This is a python script for shivani to automate hhpred analysis for multiple legionella proteins using the HHPred web tool.
# Pretty basic at the moment. Uses system wait of 4mins per sample to wait for results to be generated. before downloading them to a text file

# tutorial
# http://www.techbeamers.com/selenium-webdriver-python-tutorial/

import sys
from selenium import webdriver
import time
import os
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

#startTime = datetime.now()

# for testing only
sequence = "MPGKRGIRVVHHDIYKGKPHVEKLKKTGGRNNQGRITVRHIGGGQRQKYRIIDFKRNKDGILGRVERLEYDPNRTALIALITYKDGEKRYIIAPSNLEVGATIQSGADSPISVGNCLPLKNIPVGTTIHCVEMKPGKGAQMLRSAGCSGQLVAKEGVYATLRLRSGEMRKIHVLCRAVIGEVSNSEHNLRALGKAGAKRWRGIRPTVRGVAMNPVDHPHGGGEGRTSGGRHPVSPWGLPTKGYKTRSNKRTDTFIVRGRKKK"

# create a new Firefox session in private mode
print("loading Firefox session")
firefox_profile = webdriver.FirefoxProfile()
firefox_profile.set_preference("browser.privatebrowsing.autostart", True)
firefox_profile.set_preference("browser.download.folderList",2)
firefox_profile.set_preference("browser.download.manager.showWhenStarting",False)
firefox_profile.set_preference("browser.download.dir", os.getcwd())
firefox_profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/css")

driver = webdriver.Firefox(firefox_profile=firefox_profile)
driver.maximize_window()

# get input sample
infile = sys.argv[1]
fasta_parser = SeqIO.parse(infile, "fasta")
for record in fasta_parser:
    print(record.id)
    sample_name = str(record.id)
    print(record.seq)
    sequence = str(record.seq)
    outfile_name = os.getcwd() + sample_name + '.txt'
    print(outfile_name)
    outfile = open(outfile_name, "w")

    # navigate to the application home page
    print("Navigating to HHPred")
    driver.get("https://toolkit.tuebingen.mpg.de/#/tools/hhpred")
    driver.implicitly_wait(30)

    # get the search textbox
    search_field = driver.find_element_by_id("alignment")
    search_field.clear()

    # enter search keyword and submit
    search_field.send_keys(sequence)
    driver.execute_script("window.scrollTo(0, 1080)") 
    submit=driver.find_element_by_class_name("success.button.small.submitJob")
    submit.click()

    # get the results textbox
    print("Producing alignment")
    time.sleep(240)

    try:
        driver.find_element_by_id("ui-id-19")
    except:
        print("results not ready, waiting 120s")
        time.sleep(120)

    if driver.find_element_by_id("ui-id-19"):
        print("results ready")
        driver.find_element_by_id("ui-id-19").click()
    else:
        driver.quit()
        print("results not found. exiting")

    # download results
    time.sleep(8)
    resultsText = driver.find_element_by_id("fileview_hhpred")
    #print(resultsText.text)

    outfile.write(resultsText.text)
    outfile.close()
    print("%s HHpred complete" % (outfile_name,))

    
# close the browser window
driver.quit()           
