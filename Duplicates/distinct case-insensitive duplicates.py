def duplicate_count(text):
    l = text
    l = l.lower()
    k = 0
    key = 0
    for i in l:
        ch = i
        k = 0
        l = l.replace(i, '_')
        for j in l:
            if j == '_':
                k += 1
        if k > 1:
            key += 1
        l = l.replace('_', '')

    return key

print(duplicate_count("ssujjooyy"))