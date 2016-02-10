count = { 'a': 120, 'b': 120, 'c': 100 }

highest = max(count.values())

print [k for k,v in count.items() if v == highest]