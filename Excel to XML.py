#import necessary modules
import openpyxl 
import xml.etree.ElementTree as ET 

#open Excel file
wb = openpyxl.Workbook("text.xlsx") 

#open the first sheet
sheet = wb.active 

#create an XML root element
data = ET.Element('data')

#iterate over rows and columns
for i in range(1, sheet.a nrows): 
	row = ET.SubElement(data, 'row') 
	for j in range(sheet.ncols): 
		cell = ET.SubElement(row, 'cell') 
		cell.text = str(sheet.cell_value(i, j)) 

#save XML file
tree = ET.ElementTree(data) 
tree.write("file.xml", xml_declaration=True, encoding='utf-8', method = 'xml')