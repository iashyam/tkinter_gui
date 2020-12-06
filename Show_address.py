#Showing the data in the address app

from tkinter import *
# from adress import *
import sqlite3 as sql

rohit = Tk()

rahul = LabelFrame(rohit, padx=20, pady=20)
rahul.pack()

dev = Toplevel()

rahu = LabelFrame(dev, padx=20, pady=20)
rahu.pack()


#The Edit Function
def edit():
    hardik = Tk()

    pandya= LabelFrame(hardik, padx=20, pady=20)
    pandya.pack()

    def save():
        # crearing a sql database
        db = sql.connect("Address")

        # creating a cursor
        c = db.cursor()
        record_id = del_entry.get()
        c.execute("""UPDATE adresses SET
        		first_name = :first,
        		last_name = :last,
        		address = :address,
        		city = :city,
        		zipcode = :zipcode 
        		WHERE oid = :oid""",
                  {
                      'first': f_name.get(),
                      'last': l_name.get(),
                      'address': address.get(),
                      'city': city.get(),
                      'zipcode': zipcode.get(),
                      'oid': record_id
                  })

        # commiting the changes
        db.commit()

        # closing the connection
        db.close()
        print("Data Uploaded Sucessfully")

        hardik.quit()

    db = sql.connect("Address")
    c = db.cursor()
    record_id = del_entry.get()
    # Query the database
    c.execute("SELECT * FROM adresses WHERE oid = " + del_entry.get())

    records = c.fetchall()


    db.commit()
    db.close()
    f_name = Entry(pandya, width=35)
    f_name.grid(column=1, row=0, padx=5, pady=10)
    l_name = Entry(pandya, width=35)
    l_name.grid(column=1, row=1, padx=5, pady=10)
    address = Entry(pandya, width=35)
    address.grid(column=1, row=2, padx=5, pady=10)
    city = Entry(pandya, width=35)
    city.grid(column=1, row=3, padx=5, pady=10)
    zipcode = Entry(pandya, width=35)
    zipcode.grid(column=1, row=4, padx=5, pady=10)
    phne = Entry(pandya, width=35)
    phne.grid(column=1, row=5, padx=5, pady=10)


    f_name_label = Label(pandya, text="First Name: ")
    f_name_label.grid(column=0, row=0, padx=5, pady=10)
    l_name_label = Label(pandya, text="Last Name: ")
    l_name_label.grid(column=0, row=1, padx=5, pady=10)
    address_label = Label(pandya, text="Address: ")
    address_label.grid(column=0, row=2, padx=5, pady=10)
    city_label = Label(pandya, text="City: ")
    city_label.grid(column=0, row=3, padx=5, pady=10)
    zipcode_label = Label(pandya, text="Zipcode: ")
    zipcode_label.grid(column=0, row=4, padx=5, pady=10)
    Phone_label = Label(pandya, text="Phone: ")
    Phone_label.grid(column=0, row=5, padx=5, pady=10)

    save = Button(pandya, text='save', command= save)
    save.grid(column=0,row=6,columnspan=2)

    for i in records:
        f_name.insert(0,i[0])
        l_name.insert(0,i[1])
        address.insert(0,i[2])
        city.insert(0,i[3])
        zipcode.insert(0,i[4])


    hardik.mainloop()

#define a delete function
def delete():
    db = sql.connect("Address")
    c = db.cursor()

    c.execute("DELETE FROM adresses WHERE oid = " + del_entry.get())

    del_entry.delete(0,END)

    db.commit()
    db.close()

#creating a see function
def see():

    db = sql.connect("Address")
    c = db.cursor()

    c.execute("SELECT *, oid FROM adresses")
    records = c.fetchall()
    text = ''
    for i in records:
        text += str(i)  + '\n'
    lbl = Label(rahu, text=text)
    lbl.pack()

    db.commit()
    db.close()

#cearing a see Button
btn = Button(rahul, text = "See the data", command=see)
btn.grid(row=0,column=0,ipadx=120, pady=20,columnspan=2)

#creating a delete button
del_lbl = Label(rahul, text = "Select ID No.")
del_lbl.grid(row=1,column=0)
del_entry = Entry(rahul,width=35)
del_entry.grid(row=1,column=1)
del_btn = Button(rahul, text="Delete",command=delete)
del_btn.grid(row=2,column=0,ipadx=135, pady=20,columnspan=2)
edit_btn = Button(rahul, text="Edit",command=edit)
edit_btn.grid(row=4,column=0,ipadx=139, pady=20,columnspan=2)


rohit.mainloop()
