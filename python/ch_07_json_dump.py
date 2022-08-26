import json

phone_numbers = {'Simon':'01234 567899', 'Jane':'01234 666666'}

f = open('test.txt', 'w')
json.dump(phone_numbers, f)
f.close()
