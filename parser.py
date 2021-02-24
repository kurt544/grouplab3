from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_data(self, data):
        print("Encountered data: ", data)

def main():
    
    parser = MyHTMLParser()
    f = open("logs.html")
    if f.mode == 'r': 
        contents = f.read()
        parser.feed(contents)

if __name__ == "__main__":
    main(); 