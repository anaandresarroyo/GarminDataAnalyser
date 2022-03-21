from pathlib import Path
from pyprojroot import here
import pandas as pd
from fitparse import FitFile


def get_records(fitfile):
    """Get the timeseries records from the FitFile object.

    Parameters
    ----------
    fitfile: (fitparse FitFile)
        The object containing the activity data from a Garmin device.
    
    Returns
    -------
    record: (pandas DataFrame)
        The contents of the data in a tabular format.
    """
    # Get timeseries 'record' data from the FitFile object
    records = pd.DataFrame()
    for _, message in enumerate(fitfile.get_messages('record')):
        data = {message_data.name: message_data.value for message_data in message}
        records = records.append(pd.Series(data), ignore_index=True)

    # Set the variable units as column MultiIndex
    # This assumes that all messages will have the same units.
    units = {message_data.name: message_data.units for message_data in message}
    columns = pd.MultiIndex.from_tuples(units.items(), names=['variable', 'units'])
    records.columns = columns

    # Set the timestamp as the row index
    records = records.set_index([('timestamp', None)])
    records.index.name = 'timestamp'
    records = records.sort_index()

    return records


def convert_fit_to_csv(fit_file_path, csv_file_path):
    """Read the activity data from a .fit file and save it as a .csv file.

    Parameters:
    -----------
    fit_file_path: (path or str)
        Should point to a .fit file that already exists.

    csv_file_path: (path or str)
        Should point to a .csv file. 
        If the file does not yet exist, it will be created.
        If the file already exists, it will be overwritten.
    """
    fitfile = FitFile(str(fit_file_path))
    records = get_records(fitfile)
    records.to_csv(csv_file_path)


if __name__ == "__main__":

    # Get the location of the .fit and .csv files.
    project_root = here()
    fit_dir = Path(project_root / 'data' / 'lisbon' / 'fit')
    csv_dir = Path(project_root / 'data' / 'lisbon' / 'csv')

    # All items in fit_dir should be .fit files.
    for fit_file_path in fit_dir.iterdir():
        csv_file_path = csv_dir / fit_file_path.name.replace('.fit', '.csv')
        # Only convert the file if the .csv file does not already exist.
        if not csv_file_path.is_file():
            print('Converting file: %s' % fit_file_path.name)
            convert_fit_to_csv(fit_file_path, csv_file_path)
