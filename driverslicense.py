from tkinter import *

root= Tk()
root.title("drivers licence")
root.geometry("300x400")

root.configure(bg="white")
canvas = Canvas(root, width=300, height=400)
canvas.create_image(0, 0, anchor=NW)
canvas.create_rectangle(0, 0, 300, 55, fill="#1463B0")
canvas.create_rectangle(0, 345, 300, 400, fill="#1463B0")

label_heading = canvas.create_text(150, 90, font=('Times', '24', 'bold italic'), text="Drivers licence")
label_name_tag = canvas.create_text(40, 165, font=('Times', '16', 'bold'), text="Name :")
label_adress_tag = canvas.create_text(40, 205, font=('Times', '16', 'bold'), text="adress :")
label_pin_tag = canvas.create_text(50, 250, font=('Times', '16', 'bold'), text="Pin no. :")
label_dob_tag = canvas.create_text(50, 250, font=('Times', '16', 'bold'), text="date of birth :")


label_name = Label(root)

label_adress = Label(root)

label_dateofbirth = Label(root)

label_pin = Label(root)


#add function
def myCardDetails():
    name = "Anika Roy"
    print(type(name))
    adress= "bangalore, yelehanka"
    print(type(adress))
    pin = 560064
    print(type(pin))
    dateofbirth = ["21st july 2008"]
    print(type(dateofbirth))
    
    label_name["text"] = name
    label_adress["text"] = adress
    label_pin["text"] = pin
    label_dateofbirth["text"] = dateofbirth
    
    


#add button
button1 = Button(root, text = "show my drivers license", command= myCardDetails)

button1.configure(width=20, activebackground="#9EC6EE", relief=FLAT)
button1_window = canvas.create_window(150, 330, anchor=CENTER, window=button1)
label_name_window = canvas.create_window(120, 165, anchor=CENTER, window=label_name)
label_grade_window = canvas.create_window(90, 205, anchor=CENTER, window=label_grade)
label_subjects_window = canvas.create_window(155, 252, anchor=CENTER, window=label_subjects)
canvas.pack()

#tkinter basic template end statement
root.mainloop()


