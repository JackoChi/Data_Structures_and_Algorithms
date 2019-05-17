"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records?
Print a message:
"There are <count> different telephone numbers in the records."
"""
text_count = []
for text in texts:
    if text[0] not in text_count:
        text_count.append(text[0])
        if text[1] not in text_count:
            text_count.append(text[1])
print ("There are {} different telephone numbers in the texts records.".format(len(text_count)))

call_count = []
for call in calls:
    if call[0] not in call_count:
        call_count.append(call[0])
        if text[1] not in call_count:
            call_count.append(call[1])
print ("There are {} different telephone numbers in the calls records.".format(len(call_count)))
