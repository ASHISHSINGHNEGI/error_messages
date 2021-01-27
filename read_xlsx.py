#program to read a xlsx format file in python .i am using jupyter notebook
import pandas as pd
import numpy as np

path = "IBM-313 Marks.xlsx"
table =pd.read_excel('IBM-313 Marks.xlsx')

'''error

---------------------------------------------------------------------------
XLRDError                                 Traceback (most recent call last)
<ipython-input-18-e887b49d2d64> in <module>
      1 path = "IBM-313 Marks.xlsx"
----> 2 table =pd.read_excel('IBM-313 Marks.xlsx')

~/.local/lib/python3.9/site-packages/pandas/util/_decorators.py in wrapper(*args, **kwargs)
    294                 )
    295                 warnings.warn(msg, FutureWarning, stacklevel=stacklevel)
--> 296             return func(*args, **kwargs)
    297 
    298         return wrapper

~/.local/lib/python3.9/site-packages/pandas/io/excel/_base.py in read_excel(io, sheet_name, header, names, index_col, usecols, squeeze, dtype, engine, converters, true_values, false_values, skiprows, nrows, na_values, keep_default_na, na_filter, verbose, parse_dates, date_parser, thousands, comment, skipfooter, convert_float, mangle_dupe_cols)
    302 
    303     if not isinstance(io, ExcelFile):
--> 304         io = ExcelFile(io, engine=engine)
    305     elif engine and engine != io.engine:
    306         raise ValueError(

~/.local/lib/python3.9/site-packages/pandas/io/excel/_base.py in __init__(self, path_or_buffer, engine)
    865         self._io = stringify_path(path_or_buffer)
    866 
--> 867         self._reader = self._engines[engine](self._io)
    868 
    869     def __fspath__(self):

~/.local/lib/python3.9/site-packages/pandas/io/excel/_xlrd.py in __init__(self, filepath_or_buffer)
     20         err_msg = "Install xlrd >= 1.0.0 for Excel support"
     21         import_optional_dependency("xlrd", extra=err_msg)
---> 22         super().__init__(filepath_or_buffer)
     23 
     24     @property

~/.local/lib/python3.9/site-packages/pandas/io/excel/_base.py in __init__(self, filepath_or_buffer)
    351             self.book = self.load_workbook(filepath_or_buffer)
    352         elif isinstance(filepath_or_buffer, str):
--> 353             self.book = self.load_workbook(filepath_or_buffer)
    354         elif isinstance(filepath_or_buffer, bytes):
    355             self.book = self.load_workbook(BytesIO(filepath_or_buffer))

~/.local/lib/python3.9/site-packages/pandas/io/excel/_xlrd.py in load_workbook(self, filepath_or_buffer)
     35             return open_workbook(file_contents=data)
     36         else:
---> 37             return open_workbook(filepath_or_buffer)
     38 
     39     @property

~/.local/lib/python3.9/site-packages/xlrd/__init__.py in open_workbook(filename, logfile, verbosity, use_mmap, file_contents, encoding_override, formatting_info, on_demand, ragged_rows, ignore_workbook_corruption)
    168     # files that xlrd can parse don't start with the expected signature.
    169     if file_format and file_format != 'xls':
--> 170         raise XLRDError(FILE_FORMAT_DESCRIPTIONS[file_format]+'; not supported')
    171 
    172     bk = open_workbook_xls(

XLRDError: Excel xlsx file; not supported

'''
