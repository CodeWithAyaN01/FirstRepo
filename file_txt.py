import os , os.path
os.makedirs('D:\\1 Python\\test\\Days')
for i in range(5):
    os.makedirs(f"D:\\1 Python\\test\\Days\\day{i+1}")
    for dir in range(5):
        open(f"D:\\1 Python\\test\\Days\\day{i+1}\\ayan{dir+1}.txt","w")