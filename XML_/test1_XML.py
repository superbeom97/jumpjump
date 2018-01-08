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

note = Element("note")
note.attrib["date"] = "20180108"
note.attrib["editor"] = "pycharm"

to = Element("to")
to.text = "Tove"
note.append(to)

SubElement(note,"to").text = "김기정"
SubElement(note,"to").text = "김인한"
SubElement(note,"to").text = "김상엽"

SubElement(note, "from").text = "Jani"

SubElement(note, "heading").text = "Reminder"
SubElement(note, "body").text = "Don't forget me this weekend!"

indent(note)
dump(note)
ElementTree(note).write("note.xml")

tree = parse("note.xml")
note = tree.getroot()

# print(note.get("date"))     ## date 호출
# print(note.get("foo", "default"))   ## "foo"가 없으면 "default" 출력
                                    ## print(note.get("foo")) -> "foo"가 없으면 None 출력
print(note.keys())      ## 속성 호출
# print(note.items())     ## (키-값) 쌍 호출

# from_tag = note.find("from")
# print(from_tag)
# from_text = note.findtext("from")
# print(from_text)
# from_tags = note.findall("from")
# print(from_tags)

to_tag = note.find("to")
print(to_tag.text)
to_tags = note.findall("to")

for to_element in to_tags:
    print(to_element.text)
    # print(to_element)      ## to_element 로만 적어주면 주소를 출력하는!!
#
# print("Search from Root")
# for parent in note.getiterator():
#     for child in parent:
#         print(child.text)
#
# print("Search from from")
# for child in note.getiterator("from"):
#         print(child.text)
#
# print("end")