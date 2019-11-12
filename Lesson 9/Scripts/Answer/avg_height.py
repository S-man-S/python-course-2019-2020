height_in_klass = {}
data = open('children.txt', 'r')

for line in data:
    student_info = (line.split('\t'))
    klass = int(''.join(ch for ch in student_info[0] if ch.isdigit()))
    height = int(student_info[2])
    if (klass in height_in_klass):
        height_in_klass[klass].append(height)
    else:
        height_in_klass[klass] = [height]
data.close()

output = open("out.txt", 'w')
for klass in range(1, 12):
    if (klass in height_in_klass):
        heights = height_in_klass[klass]
        output.write(f"{klass} : {sum(heights) / float(len(heights)):.2f}\n")
    else:
        output.write(f"{klass} : -\n")
output.close()