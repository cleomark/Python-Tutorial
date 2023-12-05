# Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form: 
# "X-DSPAM-Confidence: 0.8475"
# Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.

fname = input("Enter file name: ")
fh = open(fname)

total_confidence = 0
total_values = 0

for line in fh:
    line = line.rstrip()
    if line.startswith("X-DSPAM-Confidence:"):
        confidence_string = line.split(": ")[1]
        confidence_value = float(confidence_string)

        total_confidence += confidence_value
        total_values += 1

average_confidence = total_confidence / total_values

print("Average spam confidence:", average_confidence)