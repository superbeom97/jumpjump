from xml.etree.ElementTree import Element, SubElement, dump, ElementTree, parse

def indent(elem, level=0):
    i = "\n" + level*" "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + " "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level+1)
        if not elem.tail or elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i

blog = Element("blog")
blog.attrib["date"] = "20180108"

subject = Element("subject")
subject.text = "Why python"

author = Element("author")
author.text = "Eric"

blog.append(subject)
blog.append(author)

SubElement(author,"age").text = "58"
SubElement(author,"nation").text = "USA"

Agenda = Element("Agenda")
blog.append(Agenda)
SubElement(Agenda,"1.").text = "Data Type"
SubElement(Agenda,"2.").text = "Control Flow"
SubElement(Agenda,"3.").text = "Function"

indent(blog)
dump(blog)      ## xml 출력
ElementTree(blog).write("blog.xml")     ## blog.xml 생성

tree = parse("note.xml")
note = tree.getroot()

# print("0. key()를 이용하여 blog 모든 속성 출력")
# print(blog.keys())
print("\n", end="")

subject_tag = blog.find("subject")
print("1. find()를 이용하여 subject 출력")
print(subject_tag.text)
print("\n", end="")

author_tag = blog.find("author")
print("2. findall()을 이용하여 author의 자식 노드 출력")
for author_element in author_tag:
    print(author_element.text)
print("\n", end="")
# for author_element in author_tags:
#     for element_au in author_element:
#         print(element_au.text)

Agenda_tags = blog.findall("Agenda")
print("3. getieratior()을 이용하여 Agenda의 자식 노드 출력")
for Agenda_element in blog.getiterator("Agenda"):
    for element_Ag in Agenda_element:
        print(element_Ag.text)

# <blog date="20180108">
#     <subject>Why python</subject>
#     <author>Eric
#         <age>58</age>
#         <nation>USA</nation>
#     </author>
#     <Agenda>
#         <1.>Data Type</1.>
#         <2.>Control Flow</2.>
#         <3.>Function </3.>
#     </Agenda>
# </blog>