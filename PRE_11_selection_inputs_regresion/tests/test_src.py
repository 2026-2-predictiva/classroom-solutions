import os

FOLDER = "PRE_11_selection_inputs_regresion"
OUTPUT_FOLDER = f"{FOLDER}/data/output"
ESTIMATOR = f"{OUTPUT_FOLDER}/estimator.pkl"


def test_01():

    assert os.path.exists(ESTIMATOR)
