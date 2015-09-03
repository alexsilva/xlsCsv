# coding=utf-8
from openpyxl import Workbook
from cStringIO import StringIO
import codecs
import unicodecsv


class Format(object):
    """Supported formats."""
    CSV = "csv"
    XLS = "xls"


class XlsCSV(object):
    """
    :keyword fmt Sets the file format (csv, xls).
    :keyword encoding data encoding.
    """

    def __init__(self, fmt=Format.CSV, *args, **kwargs):
        getattr(self, "_format_" + fmt)(*args, **kwargs)
        self.format = fmt

    def _format_xls(self, *args, **kwargs):
        self.encoding = kwargs.get('encoding', 'utf-8')
        self.wb = Workbook(write_only=True, encoding=self.encoding)
        self.writer = self.wb.create_sheet()

    def _format_csv(self, *args, **kwargs):
        self.buff = kwargs.get("file", StringIO())
        self.encoding = kwargs.get('encoding', 'utf-8')
        self.writer = unicodecsv.writer(self.buff, encoding=self.encoding)

    def writerow(self, data):
        getattr(self, "_write_" + self.format)(data)

    def _write_xls(self, data):
        self.writer.append(data)

    def _write_csv(self, data):
        self.writer.writerow(data)

    def save(self, filename):
        getattr(self, "_save_" + self.format)(filename)

    @property
    def stream(self):
        return getattr(self, "_stream_" + self.format)

    @property
    def _stream_csv(self):
        return self.buff.getvalue()

    @property
    def _stream_xls(self):
        buff = StringIO()
        self.wb.save(buff)
        return buff.getvalue()

    def _save_csv(self, filename):
        if not hasattr(self.buff, 'save') and hasattr(self.buff, 'getvalue'):
            with open(filename, mode='w') as _file:
                _file.write(self.buff.getvalue())

    def _save_xls(self, filename):
        self.wb.save(filename)