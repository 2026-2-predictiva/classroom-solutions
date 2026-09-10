import os

FOLDER = "PRE_16_tokenizacion"


def test_01():

    assert os.path.exists(f"{FOLDER}/data/output/file1.txt")
    assert os.path.exists(f"{FOLDER}/data/output/file2.txt")
    assert os.path.exists(f"{FOLDER}/data/output/file3.txt")
