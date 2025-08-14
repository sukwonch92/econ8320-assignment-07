import unittest
import json
import pandas as pd

with open("Lesson.ipynb", "r") as file:
    f_str = file.read()

doc = json.loads(f_str)

code = [i for i in doc['cells'] if i['cell_type']=='code']
si = {}
for i in code:
    for j in i['source']:
        if "#si-exercise" in j:
            source = "".join(i['source'])
            compile(source, '<string>', 'exec')

class testCases(unittest.TestCase):

    def testFunction(self):

      self.assertTrue(re.search(r"bags[ ]*=[ ]*poshmark(", source), 
                      "The `poshmark` function is not used in your code to create the bags variable.")