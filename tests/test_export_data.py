import os
import csv
import pytest
from src.export_data import clean_text, real_time, save_csv


class TestCleanText(object):
    def test_clean_text_tail_multispaces(self):
        actual = clean_text('Header 1         ')
        expected = 'Header 1'
        mess = f"clean_text('Header 1    ') returned {actual} instead of  {expected}"
        assert actual == expected, mess

    def test_clean_text_head_multispaces(self):
        actual = clean_text('      Header 1')
        expected = 'Header 1'
        mess = f"clean_text('Header 1') returned {actual} instead of  {expected}"
        assert actual == expected, mess

    def test_clean_text_multispaces(self):
        actual = clean_text('      Header               1')
        expected = 'Header 1'
        mess = f"clean_text('Header 1') returned {actual} instead of  {expected}"
        assert actual == expected, mess

    def test_clean_text_blank_line(self):
        actual = clean_text('\nHeader 1     \n\n')
        expected = 'Header 1'
        mess = f"clean_text('\\nHeader 1     \\n') returned {actual} instead of  {expected}"
        assert actual == expected, mess

    def test_clean_text_complex(self):
        actual = clean_text('\nFree     \n\n   2 \n ')
        expected = 'Free 2'
        mess = f"clean_text('\\nnFree     \\n\\n   2 \\n ') returned {actual} instead of  {expected}"
        assert actual == expected, mess

    def test_clean_text_empty_values(self):
        actual = clean_text('\n     \n\n    \n ')
        expected = ''
        mess = f"clean_text('\\n     \\n\\n    \\n ') returned {actual} instead of  {expected}"
        assert actual == expected, mess


class TestRealTime(object):
    def test_real_time_positive(self):
        expected = '00:25:00.00'
        actual = real_time(1500)
        mess = f"real_time(1500) returned {actual} instead of {expected}"
        assert actual == expected, mess

    def test_real_time_zero(self):
        expected = '00:00:00.00'
        actual = real_time(0)
        mess = f"real_time(0) returned {actual} instead of {expected}"
        assert actual == expected, mess

    def test_real_time_negative(self):
        with pytest.raises(ValueError) as exception_info:
            real_time(-10)
        assert exception_info.match('Elapsed negative')


class TestSaveCSV(object):
    def test_empty_list(self):
        csv_file_path = 'test_csv_save'
        save_csv(list_data=[], save_type=None, header=[
                 'h1', 'h2', 'h3'], file_name=csv_file_path)
        
        full_file_name = f"{csv_file_path}.csv"
        with open(full_file_name, encoding='utf-8') as csvflie:
            lines = csvflie.readlines()
        os.remove(full_file_name)

        first_line = lines[0]
        assert first_line == 'h1,h2,h3\n'

        with pytest.raises(IndexError) as exception_info:
            second_line = lines[1]
        assert exception_info.match('list index out of range')

    def test_empty_over_list(self):
        csv_file_path = 'test_csv_save'
        save_csv(list_data=[(1, "hai", 3, 5)], save_type=None, header=[
                 'h1', 'h2', 'h3'], file_name=csv_file_path)
        
        full_file_name = f"{csv_file_path}.csv"
        with open(full_file_name, encoding='utf-8') as csvflie:
            lines = csvflie.readlines()
        os.remove(full_file_name)

        first_line = lines[0]
        assert first_line == 'h1,h2,h3\n'
        second_line = lines[1]
        assert second_line == '1,hai,3,5\n'

        with pytest.raises(IndexError) as exception_info:
            third_line = lines[2]
        assert exception_info.match('list index out of range')
