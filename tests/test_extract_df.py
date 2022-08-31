import sys, os
import unittest
from extract_dataframe import save_as_csv
os.chdir("D:\\10XAcademy\\Ad-campaign-performance")
path_to_module = os.path.abspath(os.getcwd()+"\\scripts")
if path_to_module not in sys.path:
    sys.path.append(path_to_module)

class TestCases(unittest.TestCase):
    def test_read_csv_file(self,filePath):
        """
        Test that it opens a csv file
        """
        assert os.path.exists(filePath) == False, "Please check whether the file exists or the path is correct"
    
    def test_save_as_csv(self,filePath):
        """
         an assertion level for saving files
        """
        assert os.path.exists(save_as_csv(filePath)) == False, "File has not been created"

if __name__ == '__main__':
    unittest.main()