# coding=utf-8
import os
import unittest
from xlscsv import XlsCSV, Format
import tempfile

__author__ = 'alex'

tempdir = tempfile.gettempdir()
print 'Save files to [%s]' % tempdir


class TestFileTypes(unittest.TestCase):

    def setUp(self):
        self.header = ["fruit", "tree"]
        self.items = (
            [u"Cajá", "Cajazeira"],
            [u"Cambucá", "Cambucazeiro"],
            [u"Guaraná", "Guaranazeiro"],
            [u"Ingá", "Ingazeira "],
            [u"Jatobá", "Jatobazeiro"]
        )

    def test_xls_stream(self):
        filepath = os.path.join(tempdir, 'sample.xlsx')

        xls = XlsCSV(fmt=Format.XLS, encoding='ISO-8859-1')
        xls.writerow(self.header)

        for i in self.items:
            xls.writerow(i)

        with open(filepath, 'wb') as f:
            f.write(xls.stream)

        self.assertTrue(os.path.exists(filepath))

    def test_xls_save(self):
        filepath = os.path.join(tempdir, 'sample2.xlsx')

        xls = XlsCSV(fmt=Format.XLS, encoding='ISO-8859-1')
        xls.writerow(self.header)

        for i in self.items:
            xls.writerow(i)

        xls.save(filepath)

        self.assertTrue(os.path.exists(filepath))

    def test_csv_file(self):
        filepath = os.path.join(tempdir, 'sample.csv')

        with open(filepath, mode='w') as _file:
            csv = XlsCSV(fmt=Format.CSV, file=_file)
            csv.writerow(self.header)

            for i in self.items:
                csv.writerow(i)

        self.assertTrue(os.path.exists(filepath))

    def test_csv_save(self):
        filepath = os.path.join(tempdir, 'sample2.csv')

        csv = XlsCSV(fmt=Format.CSV)
        csv.writerow(self.header)

        for i in self.items:
            csv.writerow(i)

        csv.save(filepath)

        self.assertTrue(os.path.exists(filepath))


if __name__ == '__main__':
    unittest.main()