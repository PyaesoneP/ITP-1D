## Business Logic ---------------------------------------------------------------------
## This file stores functions that implement the business logic.
## 1) calculate_total: Takes in the number of adults and children and returns the total price. 
## Currently, it returns 0,0. Modify the code so that it returns the total price of the tickets. 
##
## 2) audio_guides: Takes in the number of items and return the total price.
## Currently, it returns 0. Modify the code so that it returns the total price according to the number of items. 
## ------------------------------------------------------------------------------------

def calculate_total( adults, children ):
    adults_price = 10
    children_price =  5
    return adults * adults_price, children * children_price
    

def audio_guides(items): 
    audio_guide_price = 3
    return audio_guide_price * items
    

def peak_hours(adults, children):
    PEAK_HOUR_SURCHARGE = 2
    return adults *10*PEAK_HOUR_SURCHARGE , children * 5 * PEAK_HOUR_SURCHARGE



## Make It Yours ---------------------------------------------------------------------
## You are now ready to design your own ticketing scheme 
## And modify the code so that the web application works according to your design. 
## ------------------------------------------------------------------------------------
