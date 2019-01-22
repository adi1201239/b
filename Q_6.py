str1 = str(input("Enter the first string"))
for i in str1:
    print(i)

b = int((len(str1))/2)
substring = str1[0:b]
print("Get the substring of the given str1",substring)

RepeatStr = 100*str1
print(RepeatStr)

str2 = str(input("Enter the second string"))

concatenate = str1 + str2
print("Show the concatenated string",concatenate)