# EasyData

An unofficial Python library/package to read in data from EasyData platform of the State Bank of Pakistan

## How to install and use

Inside the Python you just need to type `pip install EasyDataPy`

## How to use the functions inside this library/package

Verifying EasyData API Key

e.g. API key is C10D3D29160CE5693F56AA9846ABB2C423D8B123 <- type in/paste your EasyData API Key!
```
EasyData_key_setup("C10D3D29160CE5693F56AA9846ABB2C423D8B123")
```

## Finding if the EasyData API Key has been verified

```py
session_has_key()
```

## Getting the entered key for further use

```py
get_Easydata_key()
```

## Downloads Weighted-average Overnight Repo Rate series as a Pandas dataframe

```py
data_frame = download_series("TS_GP_IR_REPOMR_D.ORR", "2015-05-25" ,"2023-12-20", "csv")
```

## Tranforming output of download_series function, that is object called data_frame into a usable time-series

```py
build_time_series(data_frame)
```

## Plot Time-Series Graph for the downloaded time-series

```py
plot_time_series(data_frame)
```
