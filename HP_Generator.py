from __future__ import print_function
from random import *

seed()

first_name_filenames=["Greek Seers.txt", "Latin Colors.txt", 
"Greek-Roman Mythological Names.txt", "Roman Cognomina.txt", 
"Woman's Names 1918 and 1928.txt", "Girl Names.txt"]

last_name_filenames=["Town Names.txt","English Dialectical Terms.txt"]

for i in range(0,20):
    first_name_filename=choice(first_name_filenames)
    last_name_filename=choice(last_name_filenames)
    
    first_name_num_lines = sum(1 for line in open(first_name_filename))
    first_name=open(first_name_filename).readlines()[randint(0, first_name_num_lines-1)].splitlines()[0]
    
    last_name_num_lines = sum(1 for line in open(last_name_filename))
    last_name=open(last_name_filename).readlines()[randint(0, last_name_num_lines-1)].splitlines()[0]
    
    print(first_name, last_name)
