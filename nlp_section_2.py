import regex as re
text = 'my pattern is 222-333-4444'
pattern = r'\d{3}-\d{3}-\d{4}'
search = re.search(pattern, text)
print(search.group())
