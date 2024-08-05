from typing import List, Optional
from ROOT import RDataFrame
import pandas as pd


def get_column_names(rdf: RDataFrame) -> List[str]:
    """
    Get the column names of a RDataFrame.

    Parameters
    ----------
    rdf : RDataFrame
        The RDataFrame object.

    Returns
    -------
    List[str]
        The column names of the RDataFrame.
    """
    return [str(col) for col in rdf.GetColumnNames()]


def rdf_to_pandas(rdf: RDataFrame, columns: Optional[List[str]] = None) -> pd.DataFrame:
    """
    Convert a RDataFrame to a pandas DataFrame.

    Parameters
    ----------
    rdf : RDataFrame
        The RDataFrame object.
    columns: Optional[List[str]]
        The columns to convert. By default, all columns are converted.

    Returns
    -------
    pd.DataFrame
        The pandas DataFrame.
    """
    if columns is None:
        pdf_dict = rdf.AsNumpy()
    else:
        pdf_dict = rdf.AsNumpy(columns)
    keys = list(pdf_dict.keys())
    for key in keys:
        # this is necessary because the keys are of type std::string (cppyy.gbl.std.string)
        # and pandas don't know how to deal with it
        pdf_dict[str(key)] = pdf_dict.pop(key)
    return pd.DataFrame.from_dict(pdf_dict)
