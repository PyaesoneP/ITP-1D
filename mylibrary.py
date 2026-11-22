## Business Logic ---------------------------------------------------------------------
## This file stores functions that implement the business logic.
## 1) calculate_total: Takes in the number of adults and children and returns the total price. 
## Currently, it returns 0,0. Modify the code so that it returns the total price of the tickets. 
##
## 2) audio_guides: Takes in the number of items and return the total price.
## Currently, it returns 0. Modify the code so that it returns the total price according to the number of items. 
## ------------------------------------------------------------------------------------

def calculate_total( adults, children ):
    Adults_Price = 10
    Children_Price =  5
    return adults * Adults_Price, children * Children_Price


def audio_guides(items): 
    Audio_Guide_Price = 3
    return Audio_Guide_Price * items
    
def get_peak_prices(adults, children):
    PEAK_SURCHARGE_RATE = 0.30
    adults_total, children_total = calculate_total(adults, children)

    adults_peak_total = adults_total * (1 + PEAK_SURCHARGE_RATE)
    children_peak_total = children_total * (1 + PEAK_SURCHARGE_RATE)

    return adults_peak_total, children_peak_total

## Make It Yours ---------------------------------------------------------------------
## You are now ready to design your own ticketing scheme 
## And modify the code so that the web application works according to your design. 
## ------------------------------------------------------------------------------------
