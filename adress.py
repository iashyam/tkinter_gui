from tkinter import *
import sqlite3 as sql

root= Tk()
root.title("Shyam Form")
shyam = LabelFrame(root, padx=15, pady=15)
shyam.pack()

res = StringVar()



def submit():
    # crearing a sql database
    db = sql.connect("Address")

    # creating a cursor
    c = db.cursor()

    # c.execute(''' CREATE TABLE adresses(
    #             First_Name  text,
    #             Last_Name text,
    #             Address text,
    #             city text,
    #             zipcode intiger
    # )
    # ''')

    # submitting into the database

    c.execute("INSERT INTO adresses VALUES(:f_name, :l_name, :address, :city, :zipcode)",
              {'f_name': f_name.get(),
               'l_name': l_name.get(),
               'address': address.get(),
               'city': city.get(),
               'zipcode': zipcode.get(),

               })

    # commiting the changes
    db.commit()

    # closing the connection
    db.close()
    print("Data Uploaded Sucessfully")

    root.quit()

f_name = Entry(shyam, width=35)
f_name.grid(column=1,row=0,padx=5,pady=10)
l_name = Entry(shyam, width=35)
l_name.grid(column=1,row=1,padx=5,pady=10)
address = Entry(shyam, width=35)
address.grid(column=1,row=2,padx=5,pady=10)
city = Entry(shyam, width=35)
city.grid(column=1,row=3,padx=5,pady=10)
zipcode = Entry(shyam, width=35)
zipcode.grid(column=1,row=4,padx=5,pady=10)
phne = Entry(shyam, width=35)
phne.grid(column=1,row=5,padx=5,pady=10)

f_name_label = Label(shyam, text="First Name: ")
f_name_label.grid(column=0,row=0,padx=5,pady=10)
l_name_label = Label(shyam, text="Last Name: ")
l_name_label.grid(column=0,row=1,padx=5,pady=10)
address_label = Label(shyam, text="Address: ")
address_label.grid(column=0,row=2,padx=5,pady=10)
city_label = Label(shyam, text="City: ")
city_label.grid(column=0,row=3,padx=5,pady=10)
zipcode_label = Label(shyam, text="Zipcode: ")
zipcode_label.grid(column=0,row=4,padx=5,pady=10)
Phone_label = Label(shyam, text="Phone: ")
Phone_label.grid(column=0,row=5,padx=5,pady=10)


#creating a button to submit to the databse
btn = Button(shyam, text = 'Submit', command= submit)
btn.grid(row=6,column=0,columnspan=2)







root.mainloop()