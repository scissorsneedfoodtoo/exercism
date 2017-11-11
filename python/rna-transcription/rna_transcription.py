def to_rna(dna_strand):
    rna = ''
    conversion = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}

    for n in dna_strand:
        if n not in conversion:
            raise ValueError('That\'s not a valid nucleotide!')
        else:
            rna += conversion[n]

    return rna
