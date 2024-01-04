#!/usr/bin/env python

import re
import pandas as pd
import matplotlib.pyplot as plt

easy_data_key: str

def easy_data_key_setup(api_key: str) -> None:
    """
    Verify and store the EasyData API key.

    Parameters
    ----------
    api_key : str
        The EasyData API key for the State Bank of Pakistan's EasyData database.

    Returns
    -------
    None
        If the key is verified, it is stored in the Easydata_key variable and a success message is printed.

    Raises
    ------
    ValueError
        If the provided key is not 40 characters long or starts with a non-alphabetic character.
    """
    try:
        if len(api_key) != 40:
            raise ValueError("The key should be exactly 40 characters long.")
        if not re.match("^[a-zA-Z]", api_key):
            raise ValueError("The key should start with an alphabet character.")
        # Set the global variable
        global easy_data_key
        easy_data_key = api_key
        print("EasyData API key verified")
    except ValueError as e:
        print(f"Error: {e}")

# Example usage

#EasyData_key_setup("C10D3D29160CE5693F56AA9846ABB2C438D8B230")

def sessions_has_key() -> bool:
    """
    Check if EasyData API key has been verified for the current session.

    Returns
    -------
    bool
        True if EasyData API key is already verified for the current session, False otherwise.
    """
    return 'easy_data_key' in globals()
