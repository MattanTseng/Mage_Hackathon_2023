if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

import pandas as pd

@transformer
def transform(*args, **kwargs):
    # at this point, we have 2 dataframes that are the user data and the ecommerce data. 
    # this cell combines both of those data frames into 1 large dataframe. From here we can pull out
    # the specific columns that we need. 

    return pd.merge(randomaugment, ecommercedataloader, left_index=True, right_index=True, how='outer')


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
