# In-Silico Functional Annotation of Bacterial ACC Deaminase (*acdS*)

## Project Overview
This repository contains an end-to-end computational pipeline developed in Python for sequence quality control, homology searching, and functional domain annotation of **1-aminocyclopropane-1-carboxylate (ACC) deaminase** (*acdS*). 

ACC deaminase is an essential enzyme produced by Plant Growth-Promoting Rhizobacteria (PGPR) that degrades plant stress ethylene precursors, facilitating root elongation and abiotic stress mitigation.

---

## Repository Contents
* `01_sequence retrieval.py`: Performs sequence quality control (checking stop codons, unknown amino acids) and computes amino acid percentage composition.
* `02_BLAST analysis.py`: Submits automated BLASTp queries to the NCBI remote non-redundant (`nr`) protein database using Biopython.
* `Read_blast result.py`: Parses BLAST XML output, calculates percentage identity, filters top rhizobial homologs, and extracts conserved regions.
* `ACCA protein.fasta`: Raw query protein sequence file.
* `hitdata (1).txt`: Complete NCBI Conserved Domain Database (CDD) output search results.
* `functional_annotation.txt`: Summary of enzymatic activity, reaction mechanism, and Gene Ontology (GO) terms.

---

## Key Results & Functional Characterization
* **Homology Screening:** BLASTp identified top significant hits ($E\text{-value} = 0.0$, Identity $87.8\% - 96.4\%$) matching functional rhizobial strains (*Pararhizobium*, *Bradyrhizobium*, *Mesorhizobium*, *Ensifer*).
* **Conserved Domain:** NCBI CDD mapped the full-length sequence (residues 2–337, Bitscore > 540) to the **Trp-synth-beta_II superfamily (cl00342)**.
* **Functional Roles (UniProtKB Q51813):**
  * **Molecular Function:** 1-aminocyclopropane-1-carboxylate deaminase activity (`GO:0016847`), Pyridoxal phosphate (PLP) binding (`GO:0030170`).
  * **Biological Process:** Amine catabolic process, Plant stress ethylene regulation.

---

## Requirements & Usage
To run the analysis scripts locally:

```bash
pip install biopython
python "01_sequence retrieval.py"
python "Read_blast result.py"
