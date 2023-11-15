from restriction_enzyme.classes import Fasta

def test_sequence():
    "test data type of sequences attribute of Fasta class"
    fasta = Fasta("./data/sequence.fasta")
    dna = fasta.sequences[0]
    assert isinstance(dna.sequence, str)
    assert isinstance(dna.identifier, str)

def test_identifier():
    "test data type of sequences attribute of Fasta class"
    fasta = Fasta("./data/sequence.fasta")
    dna = fasta.sequences[0]
    assert isinstance(dna.identifier, str)