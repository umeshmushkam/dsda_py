# word count from file

def wordcount(fname):
    try:
        fhand = open(fname)
    except:
        print('File cannot be opened')
        exit()
    
    count = dict()
    for line in fhand:
        words = line.split()
        for word in words:
            if word not in count:
                count[word] = 1
            else:
                count[word] += 1
    return(count)

print(wordcount('test-data/wordcount-sample.txt'))
print(wordcount('test-data/sample-2mb-text-file.txt'))

counts = wordcount('test-data/sample-2mb-text-file.txt')

print(counts['magnis'])

filtered = { key:value for key, value in counts.items() if value  < 200 and value > 15 }

print(filtered)