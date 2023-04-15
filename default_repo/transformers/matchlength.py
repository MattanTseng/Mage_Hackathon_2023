import pandas as pd


if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(*args, **kwargs):

    empty_rows = pd.DataFrame(index = range(48958), columns = userdataloader.columns)
    # print(data.head())

    return pd.concat([userdataloader, empty_rows])


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
