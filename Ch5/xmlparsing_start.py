# 
# Example file for parsing and processing XML
#

import xml.dom.minidom

def printSkills(doc):
  skills = doc.getElementsByTagName("skill")
  print("%d skills: " %skills.length)
  for skill in skills:
    print(skill.getAttribute("name"))

def main():
  # use the parse() function to load and parse an XML file
  doc = xml.dom.minidom.parse("./Ch5/samplexml.xml")
  
  # print out the document node and the name of the first child tag
  print(doc.nodeName)
  print(doc.firstChild.tagName)
  
  # get a list of XML tags from the document and print each one
  printSkills(doc)
    
  # create a new XML tag and add it into the document
  newSkill = doc.createElement("skill")
  newSkill.setAttribute("name", "React")
  doc.firstChild.appendChild(newSkill)
  
  printSkills(doc)

if __name__ == "__main__":
  main();
