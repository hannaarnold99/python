# --------  Reads a CSV file and returns an array of each row --------- #
def csv_file_reader(file):
    arr = []
    f = open(file, 'r')
    reader = csv.reader(f)
    headers = next(reader, None)
    for row in reader:
        values = []
        for value in row:
            values.append(value)
        arr.append(values)
    return arr, headers
