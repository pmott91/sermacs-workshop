"""
molssi_math.py
Sample repository for MOLSSI at SERMACS

Misc. math functions
"""

def mean (num_list):
       """

       computes the mean of a list.

       Paramaters

       -------------

       num_list: list
              List to calculate mean of 

       Returns
       -------------

       mean: float
              Mean of list of numbers

       """
       list_mean=sum(num_list)/len(num_list)

       return list_mean

