import os

FOLDER = "PRE_05_clustering_demanda/data/output"


def test_homework():

    assert os.path.exists(f"{FOLDER}/demanda-comercial-patrones-ejemplo.png")
    assert os.path.exists(f"{FOLDER}/demanda-comercial-perfiles.png")
    assert os.path.exists(f"{FOLDER}/demanda-comercial.png")
