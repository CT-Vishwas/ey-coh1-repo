import pytest
import pandas as pd

from utils import load_data

def test_load_data(mocker):

    expected_df = pd.DataFrame({'id': [1,2],'value' : ['A','B']})
    mock_read = mocker.patch('utils.pd.read_csv', return_value=expected_df)

    result = load_data('myFile.csv')

    mock_read.assert_called_once_with('myFile.csv')

    pd.testing.assert_frame_equal(result, expected_df)