from Bio import SeqIO 

record=SeqIO.read("ACCA protein.fasta","fasta")
print(record.id)
print(record.description)
print("Sequence is shown here:",record.seq)
Total_length=len(record)
print("The length of the aminoacid is",Total_length)
sequence=str(record.seq)

#Quality Control Check
stop_count=sequence.count("*")     #For STOP CODON Count 
Unknown_Aminoacid=sequence.count("X")  #For Unknown Aminoacid

print("There are",stop_count,"stop codons")
print("There are",Unknown_Aminoacid,"Unknown Aminoacid")
if stop_count==0:
    print("It is biologically reasonbale")
else:
    print("Error detected")


aminoacid_counts={}
for a in record:
    if a in aminoacid_counts:
        aminoacid_counts[a] +=1
    else:
        aminoacid_counts[a] =1

print("Aminoacid composition is shown below:")

for a, count in aminoacid_counts.items():
    percentage=(count/ Total_length) * 100
    print(a, ":", count, "(", round(percentage, 2) ,"%)")