#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 13:17:49 2019

suit app

@author: dieudonneouedraogo
"""

# enter height 
#enter weight
# enter waist size
#enter preference fit

#print yor suit size is
# you pants size is 
# your suggested fit is :

def Suit_helper():
    height,waist= eval(input("enter your height and waist with comma separation\n"))
    if height>6:
        suit_type="Long"
    else:
        if height>5.5:
            suit_type="Regular"
        else:
            suit_type="Short"
            
    suit_size=waist+6
    suit=str(suit_size)+suit_type
    url="https://www.macys.com"
    print("Your perfect suit is\n those sites could help\n",suit,url)
    
            