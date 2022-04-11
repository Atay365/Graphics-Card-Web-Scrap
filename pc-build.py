from unittest import result
from bs4 import BeautifulSoup
import requests

cpu_url = "https://www.newegg.com/amd-ryzen-7-3800x/p/N82E16819113104?Description=Ryzen&cm_re=Ryzen-_-19-113-104-_-Product&quicklink=true"
gpu_url = "https://www.newegg.com/gigabyte-geforce-rtx-3080-ti-gv-n308tvision-oc-12gd/p/N82E16814932437?Item=N82E16814932437"
case_url = "https://www.newegg.com/p/2AM-000Z-00084?quicklink=true"
mb_url = "https://www.newegg.com/asus-rog-strix-x570-i-gaming/p/N82E16813119209?Item=N82E16813119209"
ram_url = "https://www.newegg.com/g-skill-16gb-288-pin-ddr4-sdram/p/N82E16820232476?Item=9SIB9YXHBW2010"

#CPU#
results = requests.get(cpu_url)
doc = BeautifulSoup(results.text, "html.parser")
cpu_title = doc.find('title')
cpu_prices = doc.find_all(text="$")
cpu_parent = cpu_prices[0].parent
cpu_strong = cpu_parent.find("strong")
cpu_price = cpu_strong.string
cpu_title_text = cpu_title.string

#GPU#
gpu_results = requests.get(gpu_url)
gpu_doc = BeautifulSoup(gpu_results.text, "html.parser")
gpu_title = gpu_doc.find('title')
gpu_title_text = gpu_title.string
gpu_prices = gpu_doc.find_all(text="$")
gpu_parent = gpu_prices[0].parent
gpu_strong = gpu_parent.find("strong")
gpu_price = gpu_strong.string

#Case#
case_results = requests.get(case_url)
case_doc = BeautifulSoup(case_results.text, "html.parser")
case_title = case_doc.find('title')
case_title_text = case_title.string
case_prices = case_doc.find_all(text="$")
case_parent = case_prices[0].parent
case_strong = case_parent.find("strong")
case_price = case_strong.string

#motherboard#
mb_results = requests.get(mb_url)
mb_doc = BeautifulSoup(mb_results.text, "html.parser")
mb_title = mb_doc.find('title')
mb_title_text = mb_title.string
mb_prices = mb_doc.find_all(text="$")
mb_parent = mb_prices[0].parent
mb_strong = mb_parent.find("strong")
mb_price = mb_strong.string

#ram#
ram_results = requests.get(ram_url)
ram_doc = BeautifulSoup(ram_results.text, "html.parser")
ram_title = ram_doc.find('title')
ram_title_text = ram_title.string
ram_prices = ram_doc.find_all(text="$")
ram_parent = ram_prices[0].parent
ram_strong = ram_parent.find("strong")
ram_price = int(ram_strong)



#Combine to one dict#
comp_build = {"CPU":[cpu_title_text, cpu_price], "GPU":[gpu_title_text, gpu_price], "Case":[case_title_text,case_price], "Motherboard":[mb_title_text, mb_price], "Ram":[ram_title_text,ram_price]}
