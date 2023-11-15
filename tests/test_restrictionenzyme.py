from restriction_enzyme.classes import rest_dict, RestrictionEnzyme, Fasta

def test_rest_dict():
    "test whether rest_dict is imported with correct type"
    assert isinstance(rest_dict, dict)

def test_recognition_site():
    "test data type of the recognition_site"
    enzyme = RestrictionEnzyme(rest_dict["AatII"])
    assert isinstance(enzyme.recognition_site, str)

def test_cleavage_position():
    "test data type of the cleavage_position"
    enzyme = RestrictionEnzyme(rest_dict["AatII"])
    assert isinstance(enzyme.cleavage_position, tuple)

def test_over_hanging_sequence():
    "test data type of the over_hanging_sequence"
    enzyme = RestrictionEnzyme(rest_dict["AatII"])
    assert isinstance(enzyme.over_hanging_sequence, str)

def test_is_palindromic():
    "test if the function correctly identifies palindromic sequences"
    enzyme = RestrictionEnzyme(rest_dict["AatII"])
    assert isinstance(enzyme.is_palindromic(), bool)
    assert enzyme.is_palindromic() is True

def test_is_sticky():
    "test if the function correctly identifies sticky ends"
    enzyme = RestrictionEnzyme(rest_dict["AatII"])
    assert isinstance(enzyme.is_sticky(), bool)
    assert enzyme.is_sticky() is True

def test_find_all_occurences():
    "test the output data type of the function and the correctness of the output"
    fasta = Fasta("./data/sequence.fasta")
    dna = fasta.sequences[0]
    sequence = dna.sequence
    enzyme = RestrictionEnzyme(rest_dict["AatII"])
    assert isinstance(enzyme.find_all_occurrences(sequence), list)
    assert len(enzyme.find_all_occurrences(sequence)) == 1

def test_cleave_dna():
    "test the correctness of the output and the output data type"
    fasta = Fasta("./data/sequence.fasta")
    dna = fasta.sequences[0]
    enzyme = RestrictionEnzyme(rest_dict["AatII"])
    output = enzyme.cleave_dna(dna)
    assert isinstance(output, list)
    assert len(output[0]["fragments"]) == 1