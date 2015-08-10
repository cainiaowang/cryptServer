import random,re

def getDracText():
    # Get the text from the file and skim out the excess whitespace
    f = open("Books/dracula.txt","r")
    text =  re.sub('\s+',' ',f.read()) 
    f.close()

    # Split it up by sentences
    sentences = text.split(".")

    #Pick a random sentence
    index = random.randint(0,len(sentences)-2)

    # Print out 2 sentences
    return ".".join(sentences[index:index+2]).strip()+"."


