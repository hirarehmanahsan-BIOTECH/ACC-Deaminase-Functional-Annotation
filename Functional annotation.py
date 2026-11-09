annotation_content = """============================================================
FUNCTIONAL ANNOTATION REPORT: ACC DEAMINASE (AcdS)
============================================================
Bases on blast analysis, the query protein showws a strong homology with 1-aminocyclopropane-1-carboxylate deaminase (ACC deaminase / AcdS)
Function:
Catalyzes a cyclopropane ring-opening reaction, the irreversible conversion of 1-aminocyclopropane-1-carboxylate (ACC) to ammonia and alpha-ketobutyrate. Allows growth on ACC as a nitrogen source.
============================================================"""
with open("Functional annotation content.txt","w") as f:
    f.write(annotation_content)

print("File successfully created")
