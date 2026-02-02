''' Given a list of documents (strings) and a keyword (string), return a list of indices of the documents that contain the keyword as a whole word, case insensitive. 
example:
Input: documents = ["The cat sat on the mat.", "Dogs are great pets.", "The dog chased the cat."], keyword = "cat"
Output: [0, 2] '''

doc_list = []

n = int(input()) # Number of documents

for i in range(n):
    doc = input() # Enter document text
    doc_list.append(doc)

Keyword = input() # Enter keyword

indices = []
key = Keyword.lower()

# Check each document for the keyword
for i in range(len(doc_list)):
    doc = doc_list[i].replace('.', '').replace(',', '').lower()
    words = doc.split()
    if key in words:
        indices.append(i)

print(indices)
