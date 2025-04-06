import csv
from sklearn import tree

x, y = [], []

'''
This code reads data from a CSV file named 'info.csv', extracts the first three columns as features (x) 
and the fourth column as labels (y), and appends them to respective lists for further processing.
'''
with open('info.csv', 'r') as fin :
    data = csv.reader(fin)
    for line in data :
        x.append(line[0:3])
        y.append(line[3])

# This code initializes a Decision Tree Classifier and fits it to the provided training data (x, y).
clf = tree.DecisionTreeClassifier()
clf = clf.fit(x, y)

'''
This code collects user input for height, weight, and shoe size for two individuals, 
splits the input into separate values, and stores them in a list called new_data.
'''
new_data = []
for i in range(2):
    info = input("please enter the information in this order \"height(meter) weight(kg) shoe-size\" : ")
    info = info.strip().split()
    new_data.append(info)  

# This code uses a classifier (clf) to predict the gender based on the provided new data (new_data).
answer = clf.predict(new_data)

print(answer[0], answer[1])