
import re
from collections import Counter

def reader(filename):
    with open(filename) as f:

        log = f.read()
        
        regexp = r'\d{1,4}\:\d{1,2}\:\d{1,2}\:\d{1,2}'

        ips_list = re.findall(regexp, log)

        return ips_list




def count(ips_list):
    counter = (Counter(ips_list))
    return counter



if __name__ == '__main__':
    reader('log')