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
            compile("".join(i['source']), '<string>', 'exec')

bags = pd.read_csv("bags.csv")

class testCases(unittest.TestCase):

    def testColnames(self):
        colnames = list(bags.columns)
        brand = "brand" in colnames
        datatype = bags['brand'].dtype=="object"
        # price = "price" in colnames
        # brand = "brand" in colnames
        # size = "size" in colnames

        self.assertTrue((brand & datatype), "Your dataset does not contain all of the required columns.")
