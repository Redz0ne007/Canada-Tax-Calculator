from functions import *
from tax_for_each_province import *
from tkinter import * 
from tkinter import messagebox

#Defining the Board
root=Tk()
root.title("Tax Calculator")
centerwindow(root,400,600)
root.configure(bg="#6e6e6e")
#Starting the calculation
def TaxCalc():
    selected_province = var.get()
    try:
        income = int(income_input.get())
        if income < 0:
            messagebox.showerror("Error", "Please enter a valid income")
            return
    except ValueError:
        messagebox.showerror("Error", "Please enter a numeric income")
        return

    tax_rates = provinces.get(selected_province, {})
    prov_tax = 0
    previous_bracket = 0

    for bracket, rate in sorted(tax_rates.items()):
        if income <= bracket:
            prov_tax += (income - previous_bracket) * rate
            break
        else:
            prov_tax += (bracket - previous_bracket) * rate
            previous_bracket = bracket

    previous_bracket=0
    fed_tax=0
    for bracket in FED_TAX_RATES:
        if income<=bracket:
            fed_tax+= (income-previous_bracket)* FED_TAX_RATES.get(bracket)
            break
        else:
            fed_tax+= (bracket-previous_bracket)* FED_TAX_RATES.get(bracket)
            previous_bracket=bracket
    
    messagebox.showinfo("Tax",f"Income : ${income}\n Federal Tax : ${fed_tax:.2f}\n Provincial Tax : ${prov_tax:.2f}\n Net income : ${income-prov_tax-fed_tax:.2f}")


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

province_selection=OptionMenu(root,var,*provinces.keys()).pack()

var.trace("w", update_selected_option(var, selected_province))

income_input = Entry(root)
income_input.pack()
income_input.insert(0, "0")

calculation_button = Button(root, text="Calculate", command=TaxCalc).pack()


root.mainloop()
print("Selected province : "+selected_province.get())