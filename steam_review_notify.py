#!/usr/bin/python3

from requests import get
import tkinter as tk
from tkinter import ttk

bad_review_num = 2
bad_review_url = 'https://steamcommunity.com/app/2102770/negativereviews/?browsefilter=toprated&snr=1_5_100010_'

def get_steam_page():
    response = get(bad_review_url)
    return response.text

def find_all(string, substring):
    return [i for i in range(len(string)) if string.startswith(substring, i)]

def count_bad_reviews(url_text):
    bad_review = '<div class="title">Not Recommended</div>'
    return len(find_all(url_text, bad_review))

def popupmsg(msg):
    popup = tk.Tk()
    popup.wm_title("Bad Steam review!")
    label = ttk.Label(popup, text=msg)
    label.pack(side="top", fill="x", padx=10, pady=10)
    B1 = ttk.Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    popup.mainloop()

current_bad_review_num = count_bad_reviews(get_steam_page())

if (current_bad_review_num != bad_review_num):
    msg = ''
    msg += f'Expecting {bad_review_num} bad Steam reviews, got {current_bad_review_num}\n'
    msg += f'Executing file: {__file__}'
    popupmsg(msg)



