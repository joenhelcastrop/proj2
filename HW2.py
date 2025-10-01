def str(text):
    freq = {}
    for ch in text:
        if ch != " ":
            freq[ch] = freq.get(ch, 0) + 1
    return freq

string = input("Enter string: ")
result = str(string)

for ch, count in result.items():
    print(f"{ch}={count}", end=", ")
