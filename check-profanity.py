import urllib.parse
import urllib.request

def read_text():
    input_file = r"/home/dzshu49/python-foundations/profanity-checker/movie_quotes.txt" # Replace with file path of file to be read
    quotes = open(input_file) 
    contents_of_files = quotes.read()
    # print(contents_of_files)
    quotes.close()
    check_profanity(contents_of_files)

def check_profanity(text_to_check):
    quoted_text = urllib.parse.quote(text_to_check)
    original_url = "http://www.wdylike.appspot.com/?q="
    url_to_check = "%s%s" % (original_url, quoted_text)
    # print(url_to_check)
    # quoted_url = urllib.parse.quote(url_to_check)
    # print(quoted_url)
    connection = urllib.request.urlopen(url_to_check)
    output = connection.read()

    #messages to be printed to console
    if b"true" in output:
        print("Tsk tsk, bad words were found!")
    elif b"false" in output:
        print("Congrats! This is a clean text.")
    # print(output)
    connection.close()


read_text()
# check_profanity("fucking shit")
