"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".
"""

results = {}
for call in calls:
    if call[0] in results:
        results[call[0]] += int(call[3])
    if call[1] in results:
        results[call[1]] += int(call[3])
    if call[0] not in results:
        results[call[0]] = int(call[3])
    if call[1] not in results:
        results[call[1]] = int(call[3])
max_value = max(results.values())
max_keys = [k for k, v in results.items() if v == max_value]
print ("{} spent the longest time, {} seconds, on the phone during September 2016.".format(max_keys, max_value))
