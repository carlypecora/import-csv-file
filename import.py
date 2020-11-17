import csv
import argparse

NEW_CSV_LIST = []

def reformat_csv(csv_filename):
    with open(csv_filename, "r") as f:
        readable_csv = csv.reader(f)
        header = next(readable_csv)
        beginning_range_index = 9
        ending_range_index = 24
        i = 0
        for row in readable_csv:
            j = 0
            size_rows = row[9:23]
            for x, shoe_size_quantity in enumerate(size_rows):
                index = row.index(shoe_size_quantity)
                try:
                    shoe_size_quantity = int(shoe_size_quantity)
                except:
                    continue
                if shoe_size_quantity <= 0:
                    print()
                else:
                    while shoe_size_quantity > 0:
                        reformat_row(row, header[x + 9])
                        shoe_size_quantity -= 1
                j += 1
                beginning_range_index += 1 
            i += 1
        print(i)
    write_to_csv()
    tester()


def reformat_row(row, shoe_size):
    new_row = []
    new_row.append(row[0:9])
    new_row.append(row[23:28])
    asdf = [str(item) for sublist in new_row for item in sublist]
    asdf.append(shoe_size[4:])
    asdf = tuple(asdf)
    NEW_CSV_LIST.append(asdf)

def write_to_csv():
    with open("test.csv", "wt") as fp:
        writer = csv.writer(fp, delimiter=",")
        writer.writerows(NEW_CSV_LIST)

def tester():
    with open("test.csv", "r") as fp:
        output_csv = list(csv.reader(fp))
        with open("ItWorks.csv", "r") as rp:
            test_csv = list(csv.reader(rp))
            print('LENGTH')
            print(len(output_csv)) == len(test_csv)
            for i, row in enumerate(output_csv):
                print('ROWS {}'.format(row))
                print('TEST {}'.format(test_csv[i]))
                print(row == test_csv[i])




if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='reformat a csv file')

    subparsers = parser.add_subparsers(dest='action', 
                                       help='the action to be taken')

    parser_reformat = subparsers.add_parser('reformat', help='reformat')

    parser_reformat.add_argument('csv_file', type=str, help='')

    args = parser.parse_args()

    if args.action == 'reformat':
        csv_filename = args.csv_file
        reformat_csv(csv_filename)

    else:
        parser.print_help()

