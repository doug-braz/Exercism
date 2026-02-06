def to_rna(dna_strand):
    rna_complement = []
    for nucleotide in dna_strand:
        if nucleotide == 'G':
            rna_complement.append('C')
        elif nucleotide == 'C':
            rna_complement.append('G')
        elif nucleotide == 'T':
            rna_complement.append('A')
        elif nucleotide == 'A':
            rna_complement.append('U')
    return "".join(rna_complement)
            
