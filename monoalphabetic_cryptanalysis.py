from tkinter import *
from tkinter import ttk

letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

root = Tk()
root.title('MonoAlphabetic Cipher Cryptanalysis')
root.resizable(True,True)
root.configure(background='blue')

root.frame_header = ttk.Frame()

ttk.Label(root.frame_header, text='MonoAlphabetic Cipher Cryptanalysis', style = 'Header.TLabel').grid(row = 0, column = 1)
ttk.Label(root.frame_header, text = 'Text:', style = 'Header.TLabel').grid(row = 2, column = 0)
ttk.Label(root.frame_header, text='Decrypted Text:',style='Header.TLabel').grid(row=30, column=0)

dec_text = list()

for i in range(4,31):
    dcc = ttk.Entry(root.frame_header, width=110)
    dcc.grid(row=i,column=1)
    dec_text.append(dcc)





text_entry = ttk.Entry(root.frame_header, width=100)
text_entry.grid(row=2,column=1)




def decrypt_text():
    stringtodecrypt = text_entry.get()
    stringtodecrypt = str(stringtodecrypt)
    stringtodecrypt = stringtodecrypt.upper()
    letters_list = list(letters)
    letters_dict = dict()

    
    for i in range(0,26):
        letters_dict[letters_list[i]] = 0

    str_len = 0

    for i in stringtodecrypt:
        if(i != " "):
            str_len = str_len+1
            letters_dict[i] = letters_dict[i]+1

    alp_count = 0
    letters_dict = sorted(letters_dict.items(), key=lambda x: x[1], reverse=True)
    letters_dict = dict(letters_dict)

    dict_temp = letters_dict.items()
    new_replace_dict = dict()
    replace_string = "ETAOINSRHDLUCMFYWGPBVKXQJZ"

    alp_count2 = 0

    for items in dict_temp:
        new_replace_dict[items[0]] = replace_string[alp_count2]
        alp_count2 = alp_count2+1

    
    print("Replacement Dictionary",new_replace_dict)
    for i in letters_list:
        alp_count = alp_count + 1
        letters_dict[i] = (letters_dict[i]/str_len)*100
        dec_text[alp_count-1].delete(0,END)
        dec_text[alp_count-1].insert(alp_count,"Frequency Analysis of "+i+" is "+str(letters_dict[i])[0:5]+"%, Will be replaced with "+new_replace_dict[i])
    

    # print(letters_dict) 


    new_string = str()

    for i in stringtodecrypt:
        if(i != " "):
            let = new_replace_dict[i]
            new_string = new_string + let

        else:
            new_string = new_string + " "

    dec_text[26].delete(0,END)
    dec_text[26].insert(31,new_string)








               

        
    
    


decrypt_button = ttk.Button(root.frame_header,text='Decrypt',command = lambda: decrypt_text()).grid(row=3,column=1)
root.frame_header.pack()
root.mainloop()