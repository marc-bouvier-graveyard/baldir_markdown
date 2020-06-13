import os
import xml.dom.minidom

current_working_directory = os.getcwd()

markdown_file_name = './markdown-sample.md'
def import_code_snippet(source_listing_infos):
    from_line = int(source_listing_infos["from"])
    to_line = int(source_listing_infos["to"])
    file_content = read_source_file(source_listing_infos["source"],)
    return cut_lines(file_content,from_line,to_line)

def cut_lines(file_as_string,from_line,to_line):
    line_array = file_as_string.split('\n')
    line_array = line_array[:(to_line)]
    line_array = line_array[(from_line-1):]
    
    
    result ='\n'.join(line_array)
    return result

def format_markdown_snippet(source_listing_infos):
   md_snippet = "```" + source_listing_infos['lang']+"\n"
   md_snippet += import_code_snippet(source_listing_infos)
   md_snippet += '\n```'
   print(md_snippet)
   return md_snippet

# reads file as string
def read_source_file(markdown_file_name):
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

