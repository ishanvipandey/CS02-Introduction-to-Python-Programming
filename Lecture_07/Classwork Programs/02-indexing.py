string1 = "CAMBRIDGE"
print("The string is: " + string1)
# print("First character: " + string1[0])
# print("Second character: " + string1[1])
# print("Third character: " + string1[2])
# print("Fourth character: " + string1[3])
# print("Fifth character: " + string1[4])
# print("Sixth character: " + string1[5])
# print("Seventh character: " + string1[6])
# print("Eight character: " + string1[7])
# print("Ninth character: " + string1[8])
# print("Tenth character: " + string1[9])

try:
    print("First character: " + string1[0])
    print("Second character: " + string1[1])
    print("Third character: " + string1[2])
    print("Fourth character: " + string1[3])
    print("Fifth character: " + string1[4])
    print("Sixth character: " + string1[5])
    print("Seventh character: " + string1[6])
    print("Eight character: " + string1[7])
    print("Ninth character: " + string1[8])
    print("Tenth character: " + string1[9])
except IndexError:
    print("Invalid Index")