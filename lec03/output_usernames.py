csv_file = "cp1111.csv"


def main():
    try:
        infile = open(csv_file, 'r')
        for line in infile:
            temp_list = line.strip().split(',')
            print(temp_list[2])
        infile.close()
        print("{} items loaded from {}".format(len(temp_list), csv_file))
    except IOError as err:
        print("I/O error: {0}".format(err))


# Start the program
main()
