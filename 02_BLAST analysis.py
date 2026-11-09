from Bio.Blast import NCBIWWW
from Bio import SeqIO
record=SeqIO.read("ACCA protein.fasta","fasta")

Result=NCBIWWW.qblast(program="blastp",database="nr",sequence=record.seq)
with open("blast_result.xml","w") as b:
    b.write(Result.read())

print("Results are shown")