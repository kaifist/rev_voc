import tkinter as tk
from tkinter import ttk, messagebox
import random
import reviewing as rev

root = tk.Tk()
root.title("Rev_Voc")
root.config(padx=5,pady=5)

#-----------entry numbers frame, label, entry and reverse option -------------#

frame_options = tk.Frame(root, padx=5, )

fromL = tk.Label(frame_options,text='From')
fromL.grid(row=0, column=0, padx=5, pady=5 )
fromE = tk.Entry(frame_options, width='5')
fromE.grid(row=0, column=1)

toL = tk.Label(frame_options, text='To')
toL.grid(row=0, column=2)
toE = tk.Entry(frame_options, width='5')
toE.grid(row=0, column=3)

isreverse = tk.BooleanVar() 

reverse = tk.Checkbutton(frame_options, text='Reverse', pady=5, variable=isreverse)
reverse.grid(row=0, column=5)

#--------- Go button and Review functions ----------#

L1 = tk.StringVar()
L2 = tk.StringVar()

review_list = [] # store all the elements for the review (global)

def rev_start():

    global review_list
    
    f = fromE.get()
    to = toE.get()

    try:
        # check reverse review, switch L1-L2
        change = isreverse.get()

        if change == True:
            L1Label.config(textvariable=L2, font=("Verdana", 20))
            L2Label.config(textvariable=L1, font=("MsMincho", 30))
        # instantiation
        repaso = rev.Review(int(f), int(to)) 

        review_list = repaso.selection()
    
        a_word = repaso.shuffle(review_list)
        L1_sel = a_word
        L1.set(L1_sel[0])

        L2Label.config(fg='white')

        L2.set(L1_sel[1])

        showB.config(state='normal')    
        goBut.config(state='disabled')
        reverse.config(state='disabled')
        return review_list 

    except:

        if f == "" or to == "": 

            emerge = messagebox.showinfo("Error", "one or both fields are empty")

        elif int(f) > int(to) or int(f) == 0:
        
            emerge = messagebox.showinfo(
                "Error", "'To' has to be greater than 'From', and 'From' greater than 0"
                )   

def show_L1():

    global review_list

    try:

        a_word = random.choice(review_list)

        review_list.remove(a_word)
    
        L1_sel = a_word
        L1.set(L1_sel[0])

        L2Label.config(fg='white')

        L2.set(L1_sel[1])

        showB.config(state='normal')

        return review_list

    except:

        L1.set('')
        L2.set('')

        goBut.config(state='normal')
        reverse.config(state='normal')
        showB.config(state='disabled')
        nextB.config(state='disabled')
        hideB.config(state='disabled')
        emerge = messagebox.showinfo("End", "Review finished!")

def show_L2():
    
    L2Label.config(fg='black')

    showB.config(state='disabled')
    
    nextB.config(state='normal')

    hideB.config(state='normal')


def hideL2(): 

    L2Label.config(fg='white')

    showB.config(state='normal')

goBut = tk.Button(frame_options, text='Go!', command=rev_start)
goBut.grid(row=0, column=4, padx=10)

frame_options.grid(row=0, column=0, padx=10, pady=10,sticky='w')

#------------ show, next and hide button frame -------------#

frame_middle = tk.Frame(root, height=100, width=100)#,  bg="black")

showB = tk.Button(frame_middle, text='Show', state='disabled', command=show_L2)
showB.grid(row=0, column=0, sticky='n')

nextB = tk.Button(frame_middle, text='Next ', state='disabled', command=show_L1)
nextB.grid()

hideB = tk.Button(frame_middle, text='Hide ', state='disabled', command=hideL2)
hideB.grid()



frame_middle.grid(column=1, row=1, ipadx=15)

#------------frame for L1 and L2 ---------------------#

L1_frame = tk.Frame(root, bg='red', bd = 1, relief='solid', padx=5, pady=5)
L1_frame.grid(column=0, row=1)
L1Label = tk.Label(L1_frame,
 bg='white', padx=100, bd = 1, relief='solid', 
 textvariable=L1, font=("KanjiStrokeOrders", 100)
                  )

L1Label.grid()

L2_frame = tk.Frame(root, bg='red',bd = 1, relief='solid')
L2_frame.grid(column=2,row=1)

L2Label = tk.Label(L2_frame, 
    bg='white', padx=100, pady=25, bd = 1, 
    relief='solid', textvariable=L2, font=("Verdana", 20)
                  )
L2Label.grid()


root.mainloop()