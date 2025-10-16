def longestWord(word):
    max_length=len(word[0])
    for item in word:
        length=len(item)
        if length>max_length:
            max_length=length
    return max_length
word=input("enter a list of words seperated by spaces:")
word=word.split()
result=longestWord(word)
print(f"the length of the longest word is:{result}")
