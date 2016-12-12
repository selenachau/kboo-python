import csv

MY_SAMPLE_FILE = "search_results_metadata_import.csv"
MY_OUTPUT_FILE = "aapb-test-data-export.csv"

NEW_COL_NAME = ['Unique Identifier', 'Identifier Source', 'Physical Format', 'Digital Format', 'Generations',
                'Duration', 'Location', 'Date', 'Date Type', 'Title', 'Title Type']


NAME_TRANSFORMATION = {'assetIdentifier':           'Unique Identifier',
                       'physicalFormat':            'Physical Format',
                       'generations':               'Generations',
                       'date':                      'Date',
                       'dateType':                  'Date Type',
                       'durationPhysical':          "Duration",
                       "originalCarrierLocation":   'Location',
                       'itemTitle':                 'Title',
                       'intellectualAssetType':      'Title Type'
                       }


def get_metadata(filename):
    """ Get the metadata from the filename and yields them one at a time.
    :param filename: path to the filename
    :yields: new record
    """

    with open(filename, "r") as data_file:
        for record in csv.DictReader(data_file):
            yield record


def transform_record(record):
    """
    Performs transformation on the a record and returns a brand new one
    :param record: original record to be transformed
    :return: newly transformed rec ord
    """

    # create a new empty record
    new_record = dict()

    # go though every field in the record, split into a field name and a field value
    for old_field_name, value in record.items():

        # if the field name is in the NAME_TRANSFORMATION dictionary, look up the new name for it
        if old_field_name in NAME_TRANSFORMATION:
            new_field_name = NAME_TRANSFORMATION[old_field_name]

            # add that field to that new record
            new_record[new_field_name] = value

    # return new record after it's been transformed
    return new_record


def main():

    # Read the file to iterate over them
    src_csv = MY_SAMPLE_FILE
    metadata = get_metadata(src_csv)

    dst_csv = MY_OUTPUT_FILE

    # Create a new file to save the transformed data

    print("Transforming file from {} to {}".format(src_csv, dst_csv))
    with open(dst_csv, "w", encoding="utf8") as new_csv_file:

        # The DictWriter from the CSV module will make writing this easier to write.
        # Here we used that new file, and assign it to have the new columns.
        # It's also using the excel csv. if you need something else (handling quotes or commas in fields differently),
        # you'll have to define that.  # See https://docs.python.org/3/library/csv.html#csv-fmt-params to define a
        # different dialect of csv.
        csv_writer = csv.DictWriter(f=new_csv_file, fieldnames=NEW_COL_NAME, dialect="excel")
        for original_record in metadata:

            # Transform your record in a way you want into a new record
            new_record = transform_record(original_record)

            # write that newly transformed record into the new file
            csv_writer.writerow(new_record)

        print("All Done!")
if __name__ == '__main__':
    main()