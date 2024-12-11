import unittest
from unittest.mock import patch
from io import StringIO
import sys

from packets_visualizer import get_dependencies, generate_plantuml


class TestDependencyVisualizer(unittest.TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def test_get_dependencies(self, mock_stdout):
        dependencies = get_dependencies('requests')
        self.assertIn('urllib3', dependencies)

    def test_generate_plantuml(self):
        dependencies = {'urllib3', 'chardet'}
        plantuml_code = generate_plantuml('requests', dependencies)
        self.assertIn('package "requests"', plantuml_code)
        self.assertIn('[ urllib3 ]', plantuml_code)
        self.assertIn('[ requests ] --> [ urllib3 ]', plantuml_code)

if __name__ == '__main__':
    unittest.main()