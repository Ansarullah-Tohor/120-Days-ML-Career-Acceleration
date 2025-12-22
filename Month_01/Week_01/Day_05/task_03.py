String= "banana"
frequency = {}
for ch in String:
    if ch in frequency:
        frequency[ch] += 1
    else:
        frequency[ch] = 1

print(f"String : {String}")
print(f"frequency: {frequency}")