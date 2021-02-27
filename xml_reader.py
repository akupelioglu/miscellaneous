def no_of_argu(*args) -> int:
    # using len() method in args to count
    return len(args)


def xml_reader(file_path, attribute_name):
    """  ------------------------------------------------------------
Inputs:
file_path (string)      : path_to_the_file\_filename.xml
attribute_name (string) : variable to be extracted from the xml

Outputs:
If attribute found:
Variable value

If attribute not found or error:
None

----------------------------------------------------------------"""
    # Checking Inputs

    if no_of_argu(file_path, attribute_name) < 2:  return None
    if len(file_path) <= 0:                        return None
    if len(attribute_name) <= 0:                   return None
    if type(file_path) != str:                     return None
    if type(attribute_name) != str:                return None
    if ".xml" not in file_path:                    file_path += ".xml"

    import xml.etree.ElementTree
    try:

        xml_tree = xml.etree.ElementTree.parse(file_path)
        root = xml_tree.getroot()

        return get_attribute(root, attribute_name)

    except FileNotFoundError:

        print("Please check your data file")


def get_attribute(root, attribute_name):
    for elem in root:

        for attrib_iter in elem.attrib:

            if attrib_iter == attribute_name:

                print(elem.attrib[attrib_iter])

                return elem.attrib[attrib_iter]

            elif elem.attrib[attrib_iter] == attribute_name:

                try:
                    return elem.attrib["value"]

                except:

                    print("Attribute not found in the file")

        get_attribute(elem, attribute_name)
