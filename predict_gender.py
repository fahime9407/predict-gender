import csv
from sklearn import tree
from tkinter import *
from tkinter import ttk

def predictor():
    try :
        # This code collects user input includes height, weight, and shoe size
        height, weight, shoe_size = float(e1.get()), float(e2.get()), float(e3.get())
        # This code uses a classifier (clf) to predict the gender based on the provided information
        answer = clf.predict([[height, weight, shoe_size]])
        lable_result.config(text= f" result : {answer[0]}")

    except ValueError : # if invalid input
        lable_result.config(text= "invalid input!")

x, y = [], []

'''
This code reads data from a CSV file named 'info.csv', extracts the first three columns as features (x) 
and the fourth column as labels (y), and appends them to respective lists for further processing.
'''
with open('info.csv', 'r') as fin :
    data = csv.reader(fin)
    for line in data :
        info = list(map(float, line[0:3]))
        x.append(info)
        y.append(line[3])

# This code initializes a Decision Tree Classifier and fits it to the provided training data (x, y).
clf = tree.DecisionTreeClassifier()
clf = clf.fit(x, y)

# create a window
root =Tk()
root.title("predictor")
root.geometry("250x200")
# receive height
lable1 = Label(root, text= "height : ").place(x= 0, y= 5)
e1 = Entry(root)
e1.place(x= 65, y= 7)
# receive weight
lable2 = Label(root, text= "weight : ").place(x= 0, y= 35)
e2 = Entry(root)
e2.place(x= 65, y= 35)
# receive shoe size
lable3 = Label(root, text= "shoe size : ").place(x= 0, y= 70)
e3 = Entry(root)
e3.place(x= 65, y= 70)
# predict button
button1 = Button(root, text= "predict", width= 30, command= predictor, activebackground= "green", activeforeground= "red")
button1.place(x= 15, y= 110)
# show result
lable_result = Label(root, text= "result .....", bg= "lightgray")
lable_result.place(x= 0, y= 145)
# close button
button2 = Button(root, text= "Done", command= root.destroy, width= 30, activebackground= "black", activeforeground= "white").place(x= 15, y= 170)

root.mainloop()