import pandas as pd


def get_records(fitfile):
    """
    Get the timeseries records from the FitFile object.

    :param fitfile: (fitparse FitFile)
    :return: record: (pandas DataFrame)
    """
    # Get timeseries 'record' data from the FitFile object
    records = pd.DataFrame()
    for im, message in enumerate(fitfile.get_messages('record')):
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
