from Bio.Blast import NCBIXML

with open("Blast_Result.XML.xml") as b:
    blast_result=NCBIXML.read(b)
print(len(blast_result.alignments))
for alignment in blast_result.alignments[0:10]:
    hsp=alignment.hsps[0]
    similarity_percent=(hsp.identities/hsp.align_length) *100  #hsp.identities represents the exact count of identical aminoacids matches betweeen your query sequence and the subject sequence,showing how many positions have the exact same builiding block 
    print("hit:",alignment.title,"Query similarity with subject sequence:",similarity_percent,"E_value is:",hsp.expect)
    print("Query :", hsp.query[:337]) #For the deteremination of conserved regions 
    print("Match :", hsp.match[:337])
    print("Sbjct :", hsp.sbjct[:337])