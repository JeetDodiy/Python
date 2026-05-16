#set
# s = {-12,1,2,3,5,2,1,4,8,7}
# print(s)
# print(type(s))

# for i in s:
#     print(i)

# s.add(6)
# print(s)

# s.remove(6)
# print(s)

# s.discard(7)
# print(s)

# print(s)
# pop_eli = s.pop()

# print(pop_eli)

# s.clear()
# print(s)


#sume set oprection
#murge two set 
# a = {1,2,3,4,5}
# b = {4,5,6,7,8,9}

# c =a.union(b)
# print(c)

# c = a|b
# print(c)

#murge two set and check coman value

# c = a.intersection(b)
# print(c)

# c = a&b
# print(c)


# check two set and get difrence beetwin

# c = a.difference(b)
# print(c)

# c = b.difference(a)
# print(c)

# c = a-b
# print(c)

# c = b-a
# print(c)


#remove same value show only non repited value

# c = a.symmetric_difference(b)
# print(c)

# c = a^b
# print(c)

# most IMP you can use also compaund oprection also
# a |= b
# a &=b
# a -= b
# a ^= b

# print(a)

#dictionary in python
#In dictionary thw kay or 

# a = {}
# a = {"key":"Value","key":"Value","key":"Value"}
# print(type(a))

# a = {1:10,"hii":20}
# print(a)


# a = {12:10,20:15,30:"jeet","jeet":True}

# print(a[35]) #print value using key
# a[30] = 35 #update value using key
# a.update({39:"jeet"}) #Inset new value using update function
# del a[35] delet the value using del function
# print(a)

# for i in a:
#     print(a[i])


# -------------------------------------------------------IPM----------------------------------------------------------------------
# In python two type of copy function is avelable                                                                                 |
# 1 = hard copy ex. a = b                                                                                                         |
# the hard copy copy the all the value and adress. were we change the value of b the automaticaliy chang a variable value also    |
#                                                                                                                                 |
# 2 = shallow copy ex. a.copy                                                                                                     |
# the shallow copy was only  copy one time that was not chang value of perant copy variyble                                       |
# --------------------------------------------------------------------------------------------------------------------------------

# a.clear()
# print(a)

# b = a.copy()
# print(b)
# thats it