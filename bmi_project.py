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

result_label = Label(text="")
result_label.grid(row=3, column=0)

def calculator():
    if entry_height.get() == "" or entry_weight.get() == "":
        result_label.config(text="Please Enter Valid Number")


    else:
        try:
            height = float(entry_height.get())
            weight = float(entry_weight.get())
            bmi = weight / (height/100)**2

            if bmi < 16.0:
                result_label.config(text = f"Your BMI is: {str(bmi)}\nYour BMI Category is: Severely Underweight")
            elif 16.0 <= bmi < 18.5:
                result_label.config(text = f"Your BMI is: {str(bmi)}\nYour BMI Category is: Underweight")
            elif 18.5 <= bmi < 25:
                result_label.config(text = f"Your BMI is: {str(bmi)}\nYour BMI Category is: Normal")
            elif 25 <= bmi < 30:
                result_label.config(text = f"Your BMI is: {str(bmi)}\nYour BMI Category is: Overweight")
            elif 30 <= bmi < 35:
                result_label.config(text = f"Your BMI is: {str(bmi)}\nYour BMI Category is: Moderately Obese")
            elif 35 <= bmi < 40:
                result_label.config(text = f"Your BMI is: {str(bmi)}\nYour BMI Category is: Severely Obese")
            else:
                result_label.config(text=f"Your BMI is: {str(bmi)}\nYour BMI Category is: Morbidly Obese")


        except ValueError:
                result_label.config(text="Please Enter Valid Number")

label_bmi_button = Button(text= "Calculate BMI", command=calculator)
label_bmi_button.grid(row=5, column=0)






window.mainloop()