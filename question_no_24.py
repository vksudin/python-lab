# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 20:58:20 2021

@author: sudin jana
"""
import matplotlib.pyplot as plt

x = []
y = []
for i in range(5):
    x.append(i+1)
    y.append(i+2)

plt.plot(x, y, c='blue')
plt.xlabel('Current')
plt.ylabel('Voltage')
plt.grid(True, which='both')
plt.show()

first_bar_values=[1,9,4,6,7]

fig, ax = plt.subplots()
ax.bar(x, first_bar_values, width=0.5, align='center', color='red', edgecolor="blue")
plt.title("Vertical bar chart")
plt.xlabel("X axis values")
plt.ylabel("Y axis values")
plt.show()

second_bar_values=[5,2,8,6,9]

fig, ax = plt.subplots()
ax.barh(y, second_bar_values, align='center', color='blue', edgecolor="red")
plt.title("Horizontal bar chart")
plt.xlabel("X axis values")
plt.ylabel("Y axis values")
plt.show()