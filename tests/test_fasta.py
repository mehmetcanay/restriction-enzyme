from restriction_enzyme.classes import Fasta, Dna

def test_sequences():
    "test data type of sequences attribute of Fasta class"
    fasta = Fasta("./data/sequence.fasta")
    assert isinstance(fasta.sequences, list)
    assert isinstance(fasta.sequences[0], Dna)

def test_read():
    "test data type of output of read function of Fasta"
    fasta = Fasta("./data/sequence.fasta")
    assert isinstance(fasta.read("./data/sequence.fasta"), list)
    assert isinstance(fasta.read("./data/sequence.fasta")[0], Dna)