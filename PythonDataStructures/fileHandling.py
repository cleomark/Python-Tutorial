# # File handle as a sequence
# xfile = open('mbox.txt')
# for cheese in xfile:
#     print(cheese)

# # Counting lines in a file
# fhand = open('mbox.txt')
# count = 0
# for line in fhand:
#     count+=1
# print('Line count:', count)

# # Reading the whole file
# fhand = open('mbox.txt')
# inp = fhand.read()
# print(len(inp))
# print(inp)
# print(inp[:7])

# # Searching through a file
# fhand = open('mbox-short.txt')
# for line in fhand:
#     line = line.rstrip()
#     if line.startswith('From:') :
#         print(line)

# # Using 'in' to select lines
# fhand = open('mbox-short.txt')
# for line in fhand:
#     line = line.rstrip()
#     if not '@uct.ac.za' in line :
#         continue
#     print(line)

# Prompt for file name
fname = input("Enter file name: ")
try:
    fhand = open(fname)
except:
    print('File cannot be opened: ', fname)
    quit()
count = 0
for line in fhand:
    if line.startswith('Subject:') :
        count+=1
print('There were', count, 'subject lines in', fname)