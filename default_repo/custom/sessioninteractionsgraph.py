if 'custom' not in globals():
    from mage_ai.data_preparation.decorators import custom
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

import matplotlib.pyplot as plt
import numpy as np

@custom
def transform_custom(*args, **kwargs):
    session, interactions = sessioninteractions.iloc[:, 0],  sessioninteractions.iloc[:, 1]

    plt.plot()



    return True


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
