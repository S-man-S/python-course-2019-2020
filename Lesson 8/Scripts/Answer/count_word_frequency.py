input_filename = "../Data/War & peace.txt"
output_filename = "../Data/out.txt"

word_frequency = {}

in_file = open(input_filename, "r", encoding='utf-8')
for line in in_file:
    line = line.strip().lower()
    line = "".join(c for c in line if c not in ('!', ',', ':', '.', '–', '?'))
    for word in line.split():
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency.update({word: 1})
in_file.close()

sorted_by_frequency = sorted(word_frequency.items(), key = lambda x: x[1], reverse = True)

out_file = open(output_filename, "w")

for item in sorted_by_frequency:
    out_file.write(f"{item[0]} : {item[1]}\n")

out_file.close()
