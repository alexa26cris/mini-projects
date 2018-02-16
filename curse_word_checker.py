import urllib

def read_text():
    quotes = open("path for the text file")   #path of the txt file to be read.
    file_content = quotes.read()
    print(file_content)
    quotes.close()  #always close any file you open in the code
    check_profanity(file_content)

def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check) #a google webpage for checking profanity in a text document
    output = connection.read()
    #print(output)
    connection.close()
    if "true" in output:
        print("Profanity Alert!")
    elif "false" in output:
        print("No curse words found! :)")
    else:
        print("Document couldn't be scanned properly.")
        
read_text()
