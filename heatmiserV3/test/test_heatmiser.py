import unittest
from heatmiserV3 import heatmiser

class TestCRCMethods(unittest.TestCase):
  def test_crc16(self):
    crc = heatmiser.crc16()
    print(crc)
    
