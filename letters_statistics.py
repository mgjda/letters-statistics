#!/usr/bin/python
import sys
import statistics
import collections

def printGraph(file):
    f = open(file, "r")
    data_dictionary = {}
    for x in f:
        for ch in x:
            ascii_char = ord(ch.lower())
            if ascii_char in data_dictionary:
                temp = data_dictionary[ascii_char]
                data_dictionary[ascii_char] = temp + 1
            elif ascii_char >=97 and ascii_char<=122:
                data_dictionary[ascii_char] = 1
        
    sorted_dictionary = collections.OrderedDict(sorted(data_dictionary.items()))            
    print(sorted_dictionary)
    
    max_width = 40
    graph_data = {}
    max_value = max(sorted_dictionary.values())
    
    min_value = min(sorted_dictionary.values())
    median_value = statistics.median(sorted_dictionary.values())
    average_value = statistics.mean(sorted_dictionary.values())
    if max_value > max_width:
        for x, y in sorted_dictionary.items():
            graph_data[x] = int((max_width * y)/max_value)
    else:
        graph_data = sorted_dictionary.copy()
        
    fill_sign = '#'
    for x, y in graph_data.items():
        print(chr(x) + ' | ' + fill_sign*y)

    print('Max value:', max_value)
    print('Min value:', min_value)
    print('Median value:', median_value)
    print('Average value:', average_value)
    
    f.close()


printGraph(sys.argv[1])

