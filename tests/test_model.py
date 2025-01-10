import pytest
import pandas as pd
from xgboost import XGBClassifier


def test_dummy_model():
    # A simple test to confirm environment is OK
    model = XGBClassifier()
    assert model is not None


def test_data_shape():
    df = pd.read_csv('data/train.csv')
    # Example: check we have 'target' column
    assert 'target' in df.columns
