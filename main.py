import tkinter

FONT = ("Sans Serif", 16)
MILES_TO_KM_FACTOR = 1.609

def miles_to_km():
    result.config(text=str(float(input_miles.get()) * MILES_TO_KM_FACTOR))

#Window
window = tkinter.Tk()
window.title("Miles to km converter")
window.config(padx=20, pady=20)

###Labels
miles = tkinter.Label(text="Miles", font=FONT)
is_equal_to = tkinter.Label(text="is equal to", font=FONT)
result = tkinter.Label(text="0", font=FONT)
km = tkinter.Label(text="km", font=FONT)

###Entry
input_miles = tkinter.Entry(width=7)

###Button

button = tkinter.Button(text="Calculate", command=miles_to_km)

###Grid
input_miles.grid(row=0, column=1)
miles.grid(row=0, column=2)
is_equal_to.grid(row=1, column=0)
result.grid(row=1, column=1)
km.grid(row=1, column=2)
button.grid(row=2, column=1)

window.mainloop()
