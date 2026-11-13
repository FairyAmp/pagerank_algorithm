#!/usr/bin/env python3


input = """Apples, Bananas, Broccoli, Cabbage, Kumquats, Strawberries,
 Oranges, Plums, Coconuts, Kumquats, Blueberries, Cherries, Strawberries,
 Lettuce, Spinach, Bananas, Blackberries, Peas, Strawberries,
 Oranges, Onions, Celery, Kumquats, Corn, Radishes,
 Pineapples, Plums, Corn, Cherries, Broccoli, Peas, Strawberries,
 Lettuce, Onions, Coconuts, Spinach, Peas, Strawberries,
 Apples, Onions, Broccoli, Corn, Cabbage, Peas,
 Plums, Blueberries, Raspberries, Blackberries, Strawberries,
 Apples, Cucumbers, Carrots, Spinach, Corn, BlackBeans, Cabbage,
 Mushrooms, Carrots, Lettuce, Radishes, Peppers, Broccoli, Spinach,
 Carrots, Lettuce, Celery, Onions, Cabbage, Peas,
 Broccoli, Cabbage, Carrots, Spinach, Corn, Peas,"""

ws = input.split()
unique_ws = []

for word in ws:
    if word not in unique_ws:
        unique_ws.append(word)

# Sort the unique words in alphabetical order
unique_ws.sort()

dic = {w: (i + 1) for i, w in enumerate(unique_ws)}
print(dic)

webs = input.split('\n')
print(webs)

out = []
for ws in webs:
    out.append([dic[w] for w in ws.split()])

print(out)
