import pymongo
from pymongo import MongoClient
import matplotlib.pyplot as plt
import numpy as np

def numberify(n):
	if n[-1] == "k":
		return float(n[0:-1]) * 1000
	elif n[-1] == "M":
		return float(n[0:-1]) * 1000000
	elif n[-1] == "M":
		return float(n[0:-1]) * 1000000000
	else:
		return n

def numberify_date(s):
	year = int(s[0:4])
	month = int(s[5:7])
	day = int(s[8:10])
	return year*365+month*30+day

def batch_numberify_date(arr):
	output = []
	for date in arr:
		output.append(numberify_date(date))
	return output

client = MongoClient

client = MongoClient('mongodb://127.0.0.1:3001/meteor')
database_name = 'meteor'
db = client[database_name]
cursor = db.recipes.find()

data = []
dates = []
compare = 'students'
companies = ['Udacity', 'Coursera', 'Udemy']
colors = ['b', 'g', 'r', 'c', 'm', 'y', 'b']
for company in companies:
	data.append([])
	dates.append([])

for document in cursor:
	if 'autocomplete' not in document:
		for metric in document['Metrics']:
			if compare in metric['name']:
				for index, company in enumerate(companies):
					if company in document['CompanyName']:
						data[index].append(numberify(metric['value']))
						dates[index].append(document['DataDate'])

for index, company in enumerate(companies):
	dates[index], data[index] = (list(t) for t in zip(*sorted(zip(dates[index], data[index]))))

print dates
print data

x_min = float("inf")
y_min = float("inf")
x_max = float("-inf")
y_max = float("-inf")
for d in dates:
	d = batch_numberify_date(d)
	if min(d) < x_min:
		x_min = min(d)
	if max(d) > x_max:
		x_max = max(d)
for d in data:
	if min(d) < y_min:
		y_min = min(d)
	if max(d) > y_max:
		y_max = max(d)

x_buff = (x_max-x_min)/10
y_buff = (y_max-y_min)/10
print x_buff
print x_min, x_max, y_min, y_max
plt.xlim(x_min-x_buff, x_max+x_buff)
plt.ylim(y_min-y_buff, y_max+y_buff)

for index, company in enumerate(companies):
	x = batch_numberify_date(dates[index])
	y = data[index]
	plt.plot(x, y, colors[index], label=companies[index])
	plt.plot(x, y, colors[index]+'o')
	fit = np.polyfit(x, y, 1)
	fit_fn = np.poly1d(fit)
	plt.plot(x, fit_fn(x), colors[index]+'--')

all_dates = []
for date in dates:
	for d in date:
		all_dates.append(d)
plt.xticks(batch_numberify_date(all_dates), all_dates, rotation=45)
plt.xlabel('Time')
plt.ylabel(compare)
plt.legend(loc='upper center', fancybox=True, shadow=True)
plt.tight_layout()
plt.show()
 
# indices = [0,1,2]
# colors = ['b', 'r', 'y']
# bar_width = 1

# for i in range(3):
#     plt.bar(indices[i], data[i], color=colors[i], label=names[i], width=bar_width)

# plt.xlabel('Company')
# plt.ylabel(compare)
# plt.title(compare)
# plt.legend()
# plt.xticks([0.5,1.5,2.5], names, color='black')

# plt.show()