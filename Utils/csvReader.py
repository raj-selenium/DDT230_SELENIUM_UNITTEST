import csv

def get_data(filename):
    data = []

    with open(filename) as csvfile:
        obj = csv.reader(csvfile)
        #skipping the header section
        next(obj)

        for datum in obj:
            data.append(datum)

    return data


if __name__ == "__main__":
    print(get_data("C:\\Users\\rajka\\PycharmProjects\\DDT230FrameworkUnittest\\TestData\\login_fail_data.csv"))

# import csv
# open the file using filepath
# pass the file object to the csv.reader() - > reader_object
# to skip the header line give next(reader_object)
# do for loop and add the lines to the data
