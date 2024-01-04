#!/usr/bin/env python

import os
import re
import requests
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

# EasyData_key_setup("C10D3D29160CE5693F56AA9846ABB2C438D8B230")


def sessions_has_key() -> bool:
    """
    Check if EasyData API key has been verified for the current session.

    Returns
    -------
    bool
        True if EasyData API key is already verified for the current session, False otherwise.
    """
    return "easy_data_key" in globals()


def get_easy_data_key() -> None:
    """
    Print the EasyData API key if entered for the current session.

    Returns
    -------
    None
        If EasyData API key is entered, print the key.
    ValueError
        If no EasyData API key has been entered for the current session.
    """
    if "easy_data_key" in globals():
        print(f"EasyData API key for the current session: {easy_data_key}")
    else:
        raise ValueError("No EasyData API key entered for the current session.")


# Example usage

# get_easydata_key()


def download_series(series_id, start_date, end_date, format="csv"):
    """
    Download time-series data from the EasyData platform of the State Bank of Pakistan and save as CSV.

    Parameters
    ----------
    Series_ID : str
        The ID of the series.
    Start_date : str
        The start date for the series in the format "YYYY-MM-DD".
    End_date : str
        The end date for the series in the format "YYYY-MM-DD".
    format : str, optional
        The format of the downloaded data, either "json" or "csv" (default is "csv").

    Returns
    -------
    pandas.DataFrame
        DataFrame containing the data from the CSV file.

    Raises
    ------
    ValueError
        If the format is not "json" or "csv" or if the request is unsuccessful.
    """
    # Check if the format is valid
    if format not in ["json", "csv"]:
        raise ValueError("Invalid format. Supported formats are 'json' and 'csv'.")

    # Construct the URL for the HTTP GET request
    url = f"https://easydata.sbp.org.pk/api/v1/series/{series_id}/data?api_key={easy_data_key}&start_date={start_date}&end_date={end_date}&format={format}"

    try:
        # Make the HTTP GET request
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        response.raise_for_status()

        # Get the current working directory
        current_directory = os.getcwd()

        # Construct the file path for the CSV file in the current directory
        csv_file_path = os.path.join(
            current_directory, f"{series_id}_{start_date}_{end_date}.{format}"
        )

        # Write the downloaded content to the CSV file
        with open(csv_file_path, "w", encoding="utf-8") as csv_file:
            csv_file.write(response.text)

        print(f"CSV data saved to {csv_file_path}")

        # Load CSV as DataFrame
        data_frame = pd.read_csv(csv_file_path)

        return data_frame

    except requests.exceptions.HTTPError as errh:
        raise ValueError(f"HTTP Error: {errh}")
    except requests.exceptions.RequestException as err:
        raise ValueError(f"Request Error: {err}")


# Example usage

# data_frame = download_series("series_id", "start_date" ,"end_date", format)
