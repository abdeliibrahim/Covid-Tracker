#built in 2022
from bs4 import BeautifulSoup
import datetime
import bs4
import requests
import tkinter as tk
def findCov():
    
    html_text = requests.get(f'https://www.nytimes.com/interactive/2021/us/covid-cases.html').text
    soup = BeautifulSoup(html_text, 'lxml')
    states = soup.find('td', class_= "num cases svelte-19jsh0p").text
    #state = states.find('a')

    return states

def stateCov():
    stateog = textfield.get()
    state = (stateog.replace(' ', '-')).lower()
    stateog = stateog.title()
    print(state)
    html_text = requests.get(f'https://www.nytimes.com/interactive/2023/us/{state}-covid-cases.html').text
    soup = BeautifulSoup(html_text, 'lxml')
    states = "Data not available. Try again"
    try:
        states = soup.find('td', class_= "num cases svelte-19jsh0p").text
    except AttributeError:
        mainlabel['text']= "Enter a valid state."
    #state = states.find('a')

    mainlabel['text']= f'COVID Cases in {stateog} today: ' + states
    
def getData(url):
    data = requests.get(url)
    return data


def covData():
    url = "https://www.worldometers.info/coronavirus/"
    html_data = getData(url)
    bs = bs4.BeautifulSoup(html_data.text, 'html.parser')
    infoDiv = bs.find("div", class_= "content-inner").findAll("div", id = "maincounter-wrap")
    allData = ""

    for i in infoDiv:
        text = i.find("h1", class_=None).get_text()
        count = i.find("span", class_=None).get_text()

        allData = allData + text + " " + count + "\n"
    return allData

covData()
def reload():
    new_data = findCov()
    mainlabel['text'] = "COVID Cases in the US today: " + new_data

findCov()

root = tk.Tk()
root.geometry("900x700")
root.title("The Best COVID Tracker")
f = ("arial", 25, "bold")
s = ("arial", 25, "normal")
corner = ("arial", 20, "normal")

mainlabel = tk.Label(root, text="ENTER A STATE BELOW ", font = s)
mainlabel.pack()

textfield = tk.Entry(root, width_=50)
textfield.pack()

mainlabel = tk.Label(root, text="Worldwide Data: \n" + covData(), font = corner)
mainlabel.pack(side="bottom")

gbtn = tk.Button(root, text = "Get Data", font = f, relief = 'solid', command = stateCov)
gbtn.pack()

ubtn = tk.Button(root, text = "Total Cases", font = f, relief = 'solid', command = reload)
ubtn.pack()

mainlabel = tk.Label(root, text="COVID Cases in the US today: " + findCov(), font = f)
mainlabel.pack()




root.mainloop()