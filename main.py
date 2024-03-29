from functions import *
from tax_for_each_province import *
from tkinter import * 

#Defining the Board
root=Tk()
root.title("Tax Calculator")
centerwindow(root,400,600)

#Starting the calculation
first_text=Label(root,text="Please select your province")
first_text.pack()

#Adding Provinces

provinces={"Ontario":ON_TAX_RATES,
        "Quebec":QC_TAX_RATES,
        "Nova Scotia":NS_TAX_RATES,
        "New Brunswick":NB_TAX_RATES,
        "Manitoba":MB_TAX_RATES,
        "British Columbia":BC_TAX_RATES,
        "Prince Edward Island":PE_TAX_RATES,
        "Saskatchewan":SK_TAX_RATES,
        "Alberta":AB_TAX_RATES,
        "Newfoundland and Labrador":NL_TAX_RATES,
        "Northwest Territories":NT_TAX_RATES,
        "Nunavut":NU_TAX_RATES,
        "Yukon":YT_TAX_RATES}


selected_province = StringVar()
selected_province.set("Ontario")

var=StringVar()
var.set("Ontario")

province_selection=OptionMenu(root,var,*provinces.keys())
province_selection.pack()

var.trace("w", update_selected_option(var, selected_province))

income_input=Entry(root)
income_input.pack()

root.mainloop()
print("Selected province : "+selected_province.get())