# -*- coding: utf-8 -*-

import random

#################################################################

# open reference chart, important encoding to read japanese char.
with open('subset', encoding='utf-8') as file:
    # TODO: open any file, not only this      
    # create a list of lists reading the lines (deleting '\n')
    #lines = [[line[0],line[2:-1]] for line in file]
    
    #separate L1 and L2 using where '\t' is 
    lines = [line.split('\t') for line in file]
    #delete \n at each L2 (last element)
    for line in lines:
        line[-1] = line[-1].strip()
    
    # create a dict with key=number from 1 and value=[L1, L2(meaning)] 
    klc_dict = {k+1:v for k, v in enumerate(lines)}


##############################################################



# Select two numbers, and take from the dictionary
# show randomly and eliminate from the list (to a new list?)
class Review():

    def __init__(self, n, e):
        self.n = n
        self.e = e+1 #to 

        self.rev_list = []
    
    def selection(self):
        
        for i in range(self.n, self.e):
            
            self.rev_list.append(klc_dict[i])
        
        return self.rev_list
    
    def shuffle(self, rev_list):
        a_word = random.choice(self.rev_list)
        
        self.rev_list.remove(a_word)
        
        return a_word