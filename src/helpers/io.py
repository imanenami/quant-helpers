import os
import pathlib


def find_file(symbol: str, data_dir: str | pathlib.Path) -> pathlib.Path:
    """Finds data file related to a symbol in the provided path

    Args:
        symbol (str): symbol name, e.g. EURUSD
        data_dir (str | pathlib.Path, optional): path to search

    Raises:
        FileNotFoundError: If no suitable file is found

    Returns:
        pathlib.Path: found file
    """
    for f in os.listdir(data_dir):
        if symbol in f:
            return pathlib.Path(f)
    raise FileNotFoundError(f"No files related to {symbol} could be found")
