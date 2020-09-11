from tkinter import *
from tkinter import ttk

letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

root = Tk()
root.title(' Caesar cipher brute')
root.resizable(True,True)
root.configure(background='blue')

root.frame_header = ttk.Frame()

ttk.Label(root.frame_header, text='Caesar Cipher', style = 'Header.TLabel').grid(row = 0, column = 1)
ttk.Label(root.frame_header, text = 'Text:', style = 'Header.TLabel').grid(row = 2, column = 0)
ttk.Label(root.frame_header, text='Decrypted Text:',style='Header.TLabel').grid(row=4, column=0)

dec_text = list()

for i in range(4,29):
    dcc = ttk.Entry(root.frame_header, width=110)
    dcc.grid(row=i,column=1)
    dec_text.append(dcc)





text_entry = ttk.Entry(root.frame_header, width=100)
text_entry.grid(row=2,column=1)

def decrypt_text():
    stringtodecrypt = text_entry.get()
    stringtodecrypt = str(stringtodecrypt)
    stringtodecrypt = stringtodecrypt.upper()
    for key in range(1,len(letters)):
        decryptedstring = ''
        for symbol in stringtodecrypt:
            if symbol in letters:
                num = letters.find(symbol)
                num = num - key

                if (num<0):
                    num = num + len(letters)

                decryptedstring = decryptedstring + letters[num]
            else:
                decryptedstring = decryptedstring + symbol

        dec_text[key-1].delete(0,END)
        dec_text[key-1].insert(key,decryptedstring+" #Key = "+str(key))
        # print(key,decryptedstring)


               

        
    
    


decrypt_button = ttk.Button(root.frame_header,text='Decrypt',command = lambda: decrypt_text()).grid(row=3,column=1)
root.frame_header.pack()
root.mainloop()