__author__ = 'anna'

quant = int(raw_input())
record = {}
for i in range(0, quant):
    string = raw_input()
    new_string = string.split()
    key = new_string[0]
    value = new_string[1:4]
    record[key] = value
name = raw_input()
for i in record.keys():
    if i == name:
        value = record[i]
        average = (float(value[0])  + float(value[1]) + float(value[2]))/3
        print "%.2f" % average
        break









