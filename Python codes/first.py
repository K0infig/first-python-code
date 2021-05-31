sentence = input("Enter any sentence");

characterCount =0;
wordCount =1;

for i in sentence:
    characterCount = characterCount+1;
    if(i ==' '):
        wordCount=wordCount+1

print("The number of characters are : ")
print(characterCount)
print("The number of words are : ");
print(wordCount);

