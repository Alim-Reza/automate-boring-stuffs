from jasperFileHeader import *
from jasperMasterBean import *
from jasperItemList import *
from jasperFileTitle import *
from jasperTable import *
from jasperEndFooter import *
import sys 

tableOfItems=[
    "stockLotOid",
    "tag",
    "isIssuable",
    "currentValue",
    "bookValue",
    "lifeTime",
    "itemOid"
]
tableOfItemsBn = [
    "lalastockLotOid",
    "lalatag",
    "lalaisIssuable",
    "lalacurrentValue",
    "lalabookValue",
    "lalalifeTime",
    "lalaitemOid"
]

reportItems = [
    "date",
    "refNo",
    "itemCategory",
    "itemGroup",
    "itemName"
]

reportItemsBn = [
    "laladate",
    "lalarefNo",
    "lalaitemCategory",
    "lalaitemGroup",
    "lalaitemName"
]

fileOpen = open(sys.argv[2], "w+")


fieldName = ""
for i in tableOfItems:
    fieldName += '<field name="'+i+'"/>\n'

try:
    if sys.argv[1] == "-port":
        fileOpen.write(jasperFileHeader.format("595", "842"))
        x = "80"
    if sys.argv[1] == "-land":
        fileOpen.write(jasperFileHeader.format("842", "595"))
        x = "201"
except:
    fileOpen.write(jasperFileHeader.format("595", "842"))
    x = "80"

fileOpen.write(jasperItemList.format(fieldName))
fileOpen.write(jasperMasterBean)
fileOpen.write(jasperFileTitle % (x, x))

tableCell = ""
cellWidth = round((555-40)/len(tableOfItems))
for i in range(0,len(tableOfItems)):
    tableCell += variablePart.format(cellWidth, cellWidth, tableOfItemsBn[i], cellWidth, "{"+tableOfItems[i]+"}")

fileOpen.write(startOfTable + tableCell + endOfTable)

fileOpen.write(jasperEndFooter)

fileOpen.close()    