#!/usr/bin/env python

import re
import pandas as pd
import matplotlib.pyplot as plt

def easy_data_key_setup(api_key):
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
