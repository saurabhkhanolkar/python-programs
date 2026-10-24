import os 
directory_path = r'C:\Users\saura\Desktop\Resumes'
contents = os.listdir(directory_path)

for item in contents: 
    print(item)