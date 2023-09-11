#! python3
import clr

import Autodesk 
from Autodesk.Revit.DB import *
from Autodesk.Revit.UI import *

uiapp = __revit__
app = uiapp.Application
uidoc = uiapp.ActiveUIDocument
doc = uiapp.ActiveUIDocument.Document


# CODE BELOW HERE #

__author__ = "Dolan Klock"

def test():
    xyz = XYZ(x=0.123, y=2.6, z=4)
    print(xyz)
test()

