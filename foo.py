import csv
import argparse

NEW_CSV_LIST = []

def reformat_csv(csv_filename):
    with open(csv_filename, "r") as f:
        readable_csv = csv.reader(f)
        # print('READABLE `{}`'.format(list(readable_csv)))
        header = next(readable_csv)
        print(header)
        beginning_range_index = 9
        ending_range_index = 24
        i = 0
        for row in readable_csv:
            # print('ROW `{}`'.format(row))
            # str_list = list(filter(None, str_list))
            j = 0
            for shoe_size_quantity in row[9:24]:
                try:
                    shoe_size_quantity = int(shoe_size_quantity)
                except:
                    # print('Value `{}` is not an integer. continuing to the next entry...'.format(shoe_size_quantity))
                    continue
                if shoe_size_quantity <= 0:
                    # print('INVALID QUANTITY `{}`'.format(shoe_size_quantity))
                    print()
            # elif type(shoe_size_quantity) != int:
            #     # print('TYPE`{}`'.format(shoe_size_quantity))
            #     raise TypeError("shoe_size_quantity must be an int. instead it is a `{}`".format(type(shoe_size_quantity)))
                else:
                    while shoe_size_quantity > 0:
                        print('MADE IT `{}`'.format(shoe_size_quantity))
                    #     print('ROW `{}`'.format(header[beginning_range_index]))
                        # reformat_row(row, header[beginning_range_index])
                        # shoe_size_quantity -= 1
                        shoe_size_quantity -= 1
                # print('MADE IT `{}`'.format(beginning_range_index))
                # if shoe_size_quantity == None or shoe_size_quantity == '':
                #     print('VALUE IS `{}`, passing...'.format(shoe_size_quantity))
                #     # continue
                #     break
                # shoe_size_quantity = int(shoe_size_quantity)
                j += 1
                beginning_range_index += 1 
                print('JJJJJJJ {} '.format(i)) 
            i += 1
        print(i)


def reformat_row(row, shoe_size):
    print(shoe_size)    
#     new_row = []
#     new_row.append(shoe_size)
#     new_row.append(row[0:j-1]
#     new_row.append(row[w:])
#     NEW_CSV_LIST.append(new_row)


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

