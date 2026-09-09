import os

FOLDER = "PRE_08_series_de_tiempo"


def test_src():

    assert os.path.exists(f"{FOLDER}/data/output/metrics.csv")
    assert os.path.exists(f"{FOLDER}/data/output/forecasts.csv")
