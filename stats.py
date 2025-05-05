def count_words(content):
    words = content.split()
    return (len(words))

def count_characters(content):
    content = content.lower()

    counter = {}

    for c in content:
        if c in counter:
            counter[c] += 1
        else:
            counter[c] = 1
            
    
    return counter

def sort_letters(lettercount):
    sorted_list = []

    def sorter(dict):
        return dict["num"]

    for key in lettercount:
        if key.isalpha():
            sorted_list.append({"char": key, "num": lettercount[key]})
            
    
    sorted_list.sort(key=sorter, reverse=True)
    
    return sorted_list