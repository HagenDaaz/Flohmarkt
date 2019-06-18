from openpyxl import load_workbook
from os.path import join
import datetime

class XlsxReader:
    def __init__(self, filename, path, sheet_name="Anzeigen"):
        self.lines = []
        self.book = load_workbook(filename=join(path, filename), read_only=False)
        self.data = self.book[sheet_name]
        self.header = None
        self.header_index = 0

    def find_header(self, header_names=['reference', 'name', 'quantity', 'price']):
        """
        find the header and index
        """
        first_row = list(self.data.rows)[0]

        self.header = [cell.value for cell in first_row]
        # header, header_index = None, None
        # for header_index, header in enumerate(self.data):
        #
        #     if header:
        #         if header[0].value in header_names:
        #             print(header[0].value)
        #             header = [cell.value for cell in header]
        #             break
        #         else:
        #             header = None
        #
        # if not header:
        #     header = [cell.value for cell in self.data]
        #     if not header_index:
        #         header_index = self.header_index
        #
        # self.header, self.header_index = header, header_index

    def build_lines(self, itemFactory):
        for row in self.data[self.header_index+1:]:
            self.lines.append(itemFactory(zip(self.header, row)))
        self.book.close()
        return self.lines

    
