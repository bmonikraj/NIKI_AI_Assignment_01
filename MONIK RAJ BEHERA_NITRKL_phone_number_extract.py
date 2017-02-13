import os #For Handling directory and files
import re #For handling regex patterns

root_path = raw_input("Enter the Directory path of the text files : ") #Taking the full path of the Directory to be traversed 

for file in os.listdir(root_path):
    if file.endswith(".txt"): #To handle the text files only
    	print file #To print file name it is traversing
        with open(root_path+"/"+str(file)) as f: #To read each file
            for line in f: #To read each line as string
                m=re.findall(r"(?:\+?\[9]\?[1][ -]?)?[789]\d{9}", line) #Regex matching with pattern and string
                if len(m)!=0: #Print if match is found
                    for j in range(0,len(m),1):
                        print str(m[j])          
