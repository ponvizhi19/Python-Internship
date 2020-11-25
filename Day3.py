#merge 2 dictionaries
a={"Maharashtra":"Mumbai","Telangana":"Hyderabad","Tamilnadu":"Chennai"}
b={"Karnataka":"Bengaluru","Bihar":"Patna"}
a.update(b)
print(a)

# remove a key from Dictionary
a={"Maharashtra":"Mumbai","Telangana":"Hyderabad","Tamilnadu":"Chennai","Karnataka":"Bengaluru","Bihar":"Patna"}
a.pop('Bihar')
print(a)

#map 2 lists into a dictionary
a=["Maharashtra","Telangana","Tamilnadu","Karnataka","Bihar"]
b=["Mumbai","Hyderabad","Chennai","Bengaluru","Patna"]
Dictionary=dict(zip(a,b))
print(Dictionary)

#find a length of the set in python
a={"Maharashtra","Telangana","Tamilnadu","Karnataka","Bihar"}
print(len(a))

# remove the intersection of a 2nd set from 1st set 
a={"Maharashtra","Telangana","Tamilnadu"}
b={"Tamilnadu","Karnataka","Bihar"}
c=a&b
print(c)
