def read_text():
    # The open() function returns a file object
    quotes = open("movie_quotes.txt")
    
    # By default the read() method returns the whole text
    content_of_file = quotes.read()
    print(content_of_file)
    
    quotes.close()
    
read_text()
