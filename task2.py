# Task 02 - Longest Valid Window
def longest_unique_window(text):
    seen = {}                     # letter -> last position
    start = 0
    best = (0, 0)                 # (start, length)
    for i in range(len(text)):
        if text[i] in seen and seen[text[i]] >= start:
            start = seen[text[i]] + 1
        seen[text[i]] = i
        if i - start + 1 > best[1]:
            best = (start, i - start + 1)
    return text[best[0]:best[0] + best[1]], best[0], best[1]

print(longest_unique_window("abcabcbb"))   # ('abc', 0, 3)
print(longest_unique_window(""))           # ('', 0, 0)
