from tkinter import *
from functools import partial


root = Tk()

root.geometry("800x600")

cart = {}





def main():
    frame_login = Frame(root, width = 800, height = 600, bg ="white")
    frame_login.place(x=0, y=0)

    label_title = Label(frame_login, text = "BlueBox Rentals", font = ("Segoe UI", 32), fg = "SlateBlue")
    label_title.place(x=300,y=10)


    btn_login = Button(frame_login, text = "Login", command = search)
    btn_login.place(x = 350, y = 400)


    label_username = Label(frame_login, text = "Username:")
    label_username.place(x=250, y=300)

    label_password = Label(frame_login, text = "Password:")
    label_password.place(x = 250, y = 340)

    entry_username = Entry(frame_login, justify = RIGHT, width = 20)
    entry_username.place(x = 350, y=300)

    entry_password = Entry(frame_login, justify = RIGHT, width = 20)
    entry_password.place(x = 350, y=340)

def search():
    frame_search_entry = Frame(root, width = 800, height = 600, bg ="white")
    frame_search_entry.place(x=0, y=0)

    label_title = Label(frame_search_entry, text = "BlueBox Rentals", font = ("Segoe UI", 32), fg = "SlateBlue")
    label_title.place(x=300,y=10)


    btn_search = Button(frame_search_entry, text = "Search", command = results)
    btn_search.place(x = 350, y = 400)

    btn_checkout = Button(frame_search_entry, text = "Go to Cart", command = cart_frame)
    btn_checkout.place(x=350, y=500)

    entry_username = Entry(frame_search_entry, justify = RIGHT, width = 20)
    entry_username.place(x = 350, y=300)


    label_movie_title = Label(frame_search_entry, text = "Movie Title:")
    label_movie_title.place(x=250, y=300)

    btn_logout = Button(frame_search_entry, text="Logout", command = main)
    btn_logout.place(x = 700, y = 560)

    btn_account_management = Button(frame_search_entry, text = "Account Management", command = account_management)
    btn_account_management.place(x=50,y=560)

def account_management():
    username = "Username"
    frame_account_management = Frame(root, width = 800, height = 600, bg = "white")
    frame_account_management.place(x = 0,y=0)

    label_title = Label(frame_account_management, text = "BlueBox Rentals", font = ("Segoe UI", 32), fg = "SlateBlue")
    label_title.place(x=300,y=10)

    btn_logout = Button(frame_account_management, text="Logout", command = main)
    btn_logout.place(x = 700, y = 560)

    label_username = Label(frame_account_management, text="Hello, " + username)
    label_username.place(x=350, y=50)

    btn_add_payment = Button(frame_account_management, text = "Add payment option to account", command=add_payment_option)
    btn_add_payment.place(x=350, y=400)

    btn_account_management = Button(frame_account_management, text = "Back to Search", command = search)
    btn_account_management.place(x=50,y=560)

def add_payment_option():
    frame_add_payment = Frame(root, width = 800, height = 600, bg = "white")
    frame_add_payment.place(x = 0,y=0)

    label_title = Label(frame_add_payment, text = "BlueBox Rentals", font = ("Segoe UI", 32), fg = "SlateBlue")
    label_title.place(x=300,y=10)

    label_ask_cardnumber = Label(frame_add_payment, text="Card Number: ")
    label_ask_cardnumber.place(x=100,y=150)

    entry_ask_cardnumber = Entry(frame_add_payment, width=16)
    entry_ask_cardnumber.place(x=200,y=150)

    label_ask_expiry = Label(frame_add_payment, text="Card Expiry: ")
    label_ask_expiry.place(x=400,y=150)

    entry_ask_expiry = Entry(frame_add_payment, width=5)
    entry_ask_expiry.place(x=480,y=150)

    label_ask_address = Label(frame_add_payment, text="Street Address: ")
    label_ask_address.place(x=100,y=360)

    entry_ask_address = Entry(frame_add_payment, width=30)
    entry_ask_address.place(x=200,y=360)

    label_ask_csv = Label(frame_add_payment, text="Card CSV: ")
    label_ask_csv.place(x=100,y=180)

    entry_ask_csv = Entry(frame_add_payment, width=3)
    entry_ask_csv.place(x=200,y=180)

    label_ask_cardtype = Label(frame_add_payment, text="Card Type: ")
    label_ask_cardtype.place(x=300,y=180)

    entry_ask_cardtype = Entry(frame_add_payment, width=15)
    entry_ask_cardtype.place(x=400,y=180)

    label_ask_billingcity = Label(frame_add_payment, text="Billing City: ")
    label_ask_billingcity.place(x=100,y=380)

    entry_ask_billingcity = Entry(frame_add_payment, width=20)
    entry_ask_billingcity.place(x=200,y=380)

    label_ask_zip = Label(frame_add_payment, text="Billing Zip: ")
    label_ask_zip.place(x=100,y=400)

    entry_ask_zip = Entry(frame_add_payment, width=5)
    entry_ask_zip.place(x=200,y=400)

    label_ask_state = Label(frame_add_payment, text="Billing State: ")
    label_ask_state.place(x=100,y=420)

    entry_ask_state = Entry(frame_add_payment, width=2)
    entry_ask_state.place(x=200,y=420)

    btn_logout = Button(frame_add_payment, text="Logout", command = main)
    btn_logout.place(x = 700, y = 560)

    btn_add_payment = Button(frame_add_payment, text="Add payment method to account")
    btn_add_payment.place(x=300,y=560)

    btn_search = Button(frame_add_payment, text = "Search", command = search)
    btn_search.place(x = 600, y = 560)

    btn_checkout = Button(frame_add_payment, text = "Go to Cart", command = cart_frame)
    btn_checkout.place(x=100, y=560)


    

'''    PaymentID 

CardNumber 
ExpirationDate 
BillingAddress 
CSV 
CardType 
BillingCity 
BillingZip 
BillingState 
Order '''


def results():

    dict_returned_titles = {"1":{"Title":"Home Alone 2:Lost in New York","Plot":"Woah he got lost in new york this time!","Year":"1992","Rating":"PG","Runtime":"120","Director":"I Don't Know","Rental_Rate":"1","Language":"English"},"2":{"Title":"Good Will Hunting","Plot":"Poor dude, very smart though","Year":"1997","Rating":"R","Runtime":"120","Director":"Gus Van Sant","Rental_Rate":"1","Language":"English"}}

    frame_search_results = Frame(root, width = 800, height = 600, bg ="white")
    frame_search_results.place(x=0, y=0)

    label_title = Label(frame_search_results, text = "BlueBox Rentals", font = ("Segoe UI", 32), fg = "SlateBlue")
    label_title.place(x=300,y=10)


    btn_return = Button(frame_search_results, text = "Return to Search", command = search)
    btn_return.place(x = 600, y = 20)

    btn_logout = Button(frame_search_results, text="Logout", command = main)
    btn_logout.place(x = 700, y = 560)

    btn_checkout = Button(frame_search_results, text = "Go to Cart", command = cart_frame)
    btn_checkout.place(x=350, y=500)

    btn_account_management = Button(frame_search_results, text = "Account Management", command = account_management)
    btn_account_management.place(x=50,y=560)

    frame_subframe = Frame(frame_search_results, width=600, height = 400, bg="black")
    frame_subframe.place(x=100,y=100)

    canvas_results = Canvas(frame_subframe, height=400, width = 600, bg="white")
    canvas_results.place(x=0,y=0)

    for key in dict_returned_titles:
        key = Button(canvas_results, text = dict_returned_titles[key]["Title"], command=partial(movie_overview,key, dict_returned_titles[key]))
        key.pack()

def movie_overview(diskID,movie):

    def disk_already_in_cart():
        label_error = Label(frame_movie_overview, text = "Disk already in cart!", fg = "red")
        label_error.place(x=350, y=560)

    def add_to_cart(diskID, movie):

        if diskID in cart.keys():
            disk_already_in_cart()
            print("Already in cart")
        else:
            cart[diskID] = movie
            print("added to cart")
            

    currently_selected_diskID = diskID

    frame_movie_overview = Frame(root, width = 800, height = 600, bg ="white")
    frame_movie_overview.place(x=0, y=0)

    label_title = Label(frame_movie_overview, text = "BlueBox Rentals", font = ("Segoe UI", 32), fg = "SlateBlue")
    label_title.place(x=300,y=10)

    btn_logout = Button(frame_movie_overview, text="Logout", command = main)
    btn_logout.place(x = 700, y = 560)

    btn_return = Button(frame_movie_overview, text = "Return to Search", command = search)
    btn_return.place(x = 600, y = 20)

    btn_add_to_cart = Button(frame_movie_overview, text = "Add to Cart", command=partial(add_to_cart,currently_selected_diskID,movie))
    btn_add_to_cart.place(x=350, y=580)

    frame_subframe = Frame(frame_movie_overview, width=600, height = 400, bg="black")
    frame_subframe.place(x=100,y=100)

    canvas_movie = Canvas(frame_subframe, height=400, width = 600, bg="white")
    canvas_movie.place(x=0,y=0)

    label_movie_title = Label(canvas_movie, text = movie["Title"])
    label_movie_title.pack()
    
    label_movie_plot = Label(canvas_movie, text = movie["Plot"])
    label_movie_plot.pack()

    label_movie_year = Label(canvas_movie, text= movie["Year"])
    label_movie_year.pack()

    label_movie_runtime = Label(canvas_movie, text= movie["Runtime"])
    label_movie_runtime.pack()

    label_movie_director = Label(canvas_movie, text= movie["Director"])
    label_movie_director.pack()

    label_movie_rental_rate = Label(canvas_movie, text= movie["Rental_Rate"])
    label_movie_rental_rate.pack()

    label_movie_rating= Label(canvas_movie, text= movie["Rating"])
    label_movie_rating.pack()

    label_movie_language = Label(canvas_movie, text= movie["Language"])
    label_movie_language.pack()

def cart_frame():

    def remove_from_cart(key):
        del cart[key]
        label_removed = Label(frame_cart, text = "Removed from cart!")
        label_removed.place(x=360, y=540)
    
    frame_cart = Frame(root, width = 800, height = 600, bg ="white")
    frame_cart.place(x=0, y=0)

    label_title = Label(frame_cart, text = "BlueBox Rentals", font = ("Segoe UI", 32), fg = "SlateBlue")
    label_title.place(x=300,y=10)

    btn_account_management = Button(frame_cart, text = "Account Management", command = account_management)
    btn_account_management.place(x=50,y=560)

    btn_logout = Button(frame_cart, text="Logout", command = main)
    btn_logout.place(x = 700, y = 560)

    btn_checkout = Button(frame_cart, text="Checkout", command = checkout)
    btn_checkout.place(x=360, y=560)

    frame_subframe = Frame(frame_cart, width=600, height = 400, bg="black")
    frame_subframe.place(x=100,y=100)

    canvas_results = Canvas(frame_subframe, height=400, width = 600, bg="white")
    canvas_results.place(x=0,y=0)

    btn_return = Button(frame_cart, text = "Return to Search", command = search)
    btn_return.place(x = 600, y = 20)

    for key in cart:
        key = Button(frame_subframe, text=cart[key]["Title"], command=partial(remove_from_cart, key))
        key.pack()

def checkout():
    frame_checkout = Frame(root, width = 800, height = 600)
    frame_checkout.place(x=0,y=0)

    label_title = Label(frame_checkout, text = "BlueBox Rentals", font = ("Segoe UI", 32), fg = "SlateBlue")
    label_title.place(x=300,y=10)

    label_thank_you = Label(frame_checkout, text = "Thank you for using BlueBox!")
    label_thank_you.place(x=350,y=300)

    btn_logout = Button(frame_checkout, text="Logout", command = main)
    btn_logout.place(x = 700, y = 560)

main()
root.mainloop()
