if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

import pandas as pd


@data_loader
def load_data(*args, **kwargs): 

    # read the ecommerce data

    return pd.read_csv("/home/src/default_repo/Mage_Hackathon_2023/Data/ecom-user-churn-data.csv")


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
