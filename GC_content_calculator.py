# Replace BRCA1.txt with any DNA seq (as txt)
gene = open("BRCA1.txt", "r")

# Set nucleotide values to 0
g = 0
c = 0
t = 0
a = 0
gc = 0
number_of_bases = 0

# Skip first line of header
gene.readline()

for line in gene:
    # turn every letter lowercase
    line = line.lower()
    for base in line:
        number_of_bases += 1
        if base == "g":
            g+=1
        if base == "c":
            c+=1
        if base == "t":
            t+=1
        if base == "a":
            a+=1
        if base == 'g' or base == 'c':
            gc += 1

print("Number of g's " + str(g))
print("Number of c's " + str(c))
print("Number of t's " + str(t))
print("Number of a's " + str(a))

content = float(gc)/float(number_of_bases)
print("GC Content: ", content)



