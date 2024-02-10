text = open("file.txt", "r")
final = open("final.txt","w")
l = list()
def find_email(s):
    for line in s:
        words = line.split(' ')
        for word in words:
            if "@" in word:
            
                l.append(word.strip())
find_email(text)

for item in l:
    final.write(item+",\n")
final.close()
text.close()
