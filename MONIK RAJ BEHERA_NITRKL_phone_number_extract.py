import os
import re

root_path = raw_input("Enter the Directory path of the text files : ")

for file in os.listdir(root_path):
    if file.endswith(".txt"):
    	print "\n"
    	print file
        with open(root_path+"/"+str(file)) as f:
            for line in f:
                m=re.findall("[789]\d{9}", line)
                if len(m)!=0:
                    for j in range(0,len(m),1):
                        print str(m[j])          
