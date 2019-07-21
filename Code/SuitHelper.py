#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 13:17:49 2019

If you have some suggestions email me 

suit app
I worked in retail for over 15 years In fine clothing for men.
I sat in every angle of the business, sales, management, products development,
planning and forecasting, strategies, clientele building.
I consider myself an expert on this field and I am hoping that 
this app could reflect that as well; it could be used to find your size and fit on a garment and 
recommend hand pick  sites that reflect my expertise in this industry
; regularly new features will be added
If you have some suggestions email me at ondieudo@gmail.com


@author: dieudonne ouedraogo
"""

# enter height 
#enter weight
# enter waist size
#enter preference fit

#print yor suit size is
# you pants size is 
# your suggested fit is :


def suit_helper():
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
    print("Your perfect suit is\n",suit)
    print("Check this Site",url)
    
            