# n = 5
# while n > 0:
#     print (n)
#     n -= 1
# print('blastoff')
# print(n)

# Breaking out of a loop
# while True:
#     line = input('> ')
#     if line == 'done':
#         break
#     print(line)
# print('Done!')

# Continue statement
# while True:
#     line = raw_input('> ')
#     if line[0] == '#' :
#         continue
#     if line == 'done' :
#         break
#     print(line)
# print('Done!') 

# For Loop
# for i in [5,4,3,2,1] :
#     print(i)
# print('Blastoff')

#Find the largest number
maxNum = 0
for i in [3, 41, 12, 89, 74, 15]:
    if i > maxNum:
        maxNum = i
print("The largest number is",maxNum)


