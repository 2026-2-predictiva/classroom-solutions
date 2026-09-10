import os

FOLDER = "PRE_14_reduccion_dimensionalidad"


def test_01():

    assert os.path.exists(f"{FOLDER}/data/output/digits_pca.png")
    assert os.path.exists(f"{FOLDER}/data/output/digits_tsne.png")
    assert os.path.exists(f"{FOLDER}/data/output/digits_umap.png")
