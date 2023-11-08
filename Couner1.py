
from fileinput import FileInput

with FileInput(["1.txt", "2.txt", "3.txt"]) as input_files:
    with open("All_.txt", 'w') as output_file:
        output_file.writelines(input_files)

with open("All_.txt", 'a') as f:
    f.close()

    with open('1.txt') as a1:
          for count, line in enumerate(a1):
                pass
    s1 = (count + 1)
    
with open('2.txt') as a2:
        for count, line in enumerate(a2):
            pass
        s2 = (count + 1)
        
with open('3.txt') as a3:
            for count, line in enumerate(a3):
                pass
            s3 = (count + 1)
            
Total_lines = {"1.txt": s1, "2.txt": s2, "3.txt": s3}
list_d = list(Total_lines.items())
list_d.sort(key=lambda i: i[1])
for k, v in list_d:
    result = (k + ':', v)
    x = (f'Служебная информация:', result)
    print(x)
    








