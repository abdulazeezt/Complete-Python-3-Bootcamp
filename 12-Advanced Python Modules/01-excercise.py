import os
os.getcwd

for dirpath, dirname, filename in os.walk('C:\\Users\\azi\\Documents\\GitHub\\Complete-Python-3-Bootcamp\\'):
    print(f"Current path : {dirpath}  "  )
    print(f"Current dirname : {dirname}")
    print(f"Current filename : {filename} " )