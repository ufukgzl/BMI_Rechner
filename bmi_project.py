from tkinter import *

window = Tk()
window.title("BMI Calculator")
window.geometry("400x300")

label_height = Label(text= "Enter Your Height in cm:")
label_height.grid(row=0, column=0)

entry_height = Entry(width=10)
entry_height.grid(row=0, column=1)

label_weight = Label(text= "Enter Your Weight in kg:")
label_weight.grid(row=1, column=0)

entry_weight = Entry(width=10)
entry_weight.grid(row=1, column=1)



def calculator():
    height = float(entry_height.get())
    weight = float(entry_weight.get())
    bmi = weight / (height/100)**2


    if bmi < 16.0:
        label_bmi_category = Label(text="Your BMI Category is: Severely Underweight")
        label_bmi_category.grid(row=3, column=0)
        label_bmi = Label(text="Your BMI is: " + str(bmi))
        label_bmi.grid(row=2, column=0)
    elif 16.0 <= bmi < 18.5:
        label_bmi_category = Label(text="Your BMI Category is: Underweight")
        label_bmi_category.grid(row=3, column=0)
        label_bmi = Label(text="Your BMI is: " + str(bmi))
        label_bmi.grid(row=2, column=0)
    elif 18.5 <= bmi < 25:
        label_bmi_category = Label(text="Your BMI Category is: Normal")
        label_bmi_category.grid(row=3, column=0)
        label_bmi = Label(text="Your BMI is: " + str(bmi))
        label_bmi.grid(row=2, column=0)

    elif 25 <= bmi < 30:
        label_bmi_category = Label(text="Your BMI Category is: Overweight")
        label_bmi_category.grid(row=3, column=0)
        label_bmi = Label(text="Your BMI is: " + str(bmi))
        label_bmi.grid(row=2, column=0)
    elif 30 <= bmi < 35:
        label_bmi_category = Label(text="Your BMI Category is: Moderately Obese")
        label_bmi_category.grid(row=3, column=0)
        label_bmi = Label(text="Your BMI is: " + str(bmi))
        label_bmi.grid(row=2, column=0)
    elif 35 <= bmi < 40:
        label_bmi_category = Label(text="Your BMI Category is: Severely Obese")
        label_bmi_category.grid(row=3, column=0)
        label_bmi = Label(text="Your BMI is: " + str(bmi))
        label_bmi.grid(row=2, column=0)
    else:
        label_bmi_category = Label(text="Your BMI Category is: Morbidly Obese")
        label_bmi_category.grid(row=3, column=0)
        label_bmi = Label(text="Your BMI is: " + str(bmi))
        label_bmi.grid(row=2, column=0)


label_bmi_button = Button(text= "Calculate BMI", command=calculator)
label_bmi_button.grid(row=5, column=0)






window.mainloop()