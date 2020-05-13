# Letters statistics

Program in Python that makes statistics (max and min occurrence, median and average value) and draws ascii-histogram of letters, based on text from read file.

## Installation

Download files and type in terminal:

```bash
python3 letters_statistics.py <filename.txt>
```
Example:
```bash
python3 letters_statistics.py lorem.txt
```
Result:
```bash
OrderedDict([(97, 195), (98, 23), (99, 105), (100, 77), (101, 300), (102, 28), (103, 38), (104, 19),
(105, 235), (106, 3),(108, 172), (109, 135), (110, 141), (111, 120), (112, 65), (113, 30), (114, 132), 
(115, 231), (116, 196), (117, 235), (118, 46), (120, 7), (122, 1)])
a | ##########################
b | ###
c | ##############
d | ##########
e | ########################################
f | ###
g | #####
h | ##
i | ###############################
j | 
l | ######################
m | ##################
n | ##################
o | ################
p | ########
q | ####
r | #################
s | ##############################
t | ##########################
u | ###############################
v | ######
x | 
z | 
Max value: 300
Min value: 1
Median value: 105
Average value: 110.17391304347827

```
