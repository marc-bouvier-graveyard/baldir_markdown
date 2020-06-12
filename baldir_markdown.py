import os
import xml.dom.minidom

current_working_directory = os.getcwd()

markdown_file_name = './markdown-sample.md'
def import_code_snippet(source_listing_infos):
    return

# reads file as string
def read_markdown_file(markdown_file_name):
    markdown_sample = open(markdown_file_name)

    file_as_string = markdown_sample.read()

    markdown_sample.close()

    return file_as_string
# end reads file as string

# match both <sourceListingStart source="./MyJavaFile.java" from="5" to="5" lang="java"/>
# and <sourceListingEnd/>

# parse xml tag and extract attributes
#source_listing_start_tag = '<sourceListingStart source="./MyJavaFile.java" from="5" to="5" lang="java"/>'
def parse_source_listing_start(xml_tag):
    tag_dom = xml.dom.minidom.parseString(xml_tag)
    tag = tag_dom.childNodes.item(0)
    tag.attributes.items()
    source_listing_infos = {}
    for attrName, attrValue in tag.attributes.items():
        source_listing_infos[attrName] = attrValue
    return source_listing_infos

# get lines from range
# construct markdown snippet between xml tags

# write file

