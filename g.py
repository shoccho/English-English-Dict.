import tkinter as tk
import pyperclip
# Import the modules required
import json

# Loading data from json file
# in python dictionary
data = json.load(open("dictionary.json"))

def translate(w):
    # converts to lower case
    w = w.lower()

    if w in data:
        return data[w]

    else:
        return "The word doesn't exist. Please double check it"



window = tk.Tk()

greeting = tk.Label(text="E2E Dictionary")
greeting.pack()
entry = tk.Entry(fg="gray",width=50)
entry.pack()


text_box = tk.Text()

text_box.pack(expand=True)

pasted=""
while True:
    pword=""
    word=entry.get().strip()
    if word=="" and len(pyperclip.paste().strip().split(' '))==1:
        word=pyperclip.paste().strip()
    if word!=pword:
        text_box.delete("1.0",tk.END)
        pword=word
        res=""
        try:
            meaning=translate(word)
            if type(meaning)==list:
                res=" ".join(meaning)
            else :
                res=meaning
        except:
            pass
        res=word+"\n"+res
        text_box.insert("1.0",res)
    window.update()
window.mainloop()
