import xml.dom.minidom 

def main(): 
    doc = xml.dom.minidom.parse("log")
    gets = doc.getElementsByTagName("GET")
    print("%d requests: " % gets.length)