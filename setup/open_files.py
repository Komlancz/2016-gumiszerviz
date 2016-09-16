from csv import *


class OpenFiles:
    @classmethod
    def open_file(cls, file_name):
        open_file_items = []
        with open(file_name, 'r') as file:
            filereader = reader(file, delimiter=';')
            for item in filereader:
                open_file_items.append(item)
        return (open_file_items)


# OpenFiles.open_file('../gumik.csv')