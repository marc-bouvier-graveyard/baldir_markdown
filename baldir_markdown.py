import os
import xml.dom.minidom

current_working_directory = os.getcwd()

markdown_file_name = './markdown-sample.md'

def pre_process_markdown_file_in_place(file_path):
    md_text = read_source_file(file_path)

def pre_process_markdown_text(md_text):
    splitted_md_text = split_against_source_listing_tags(md_text)
    start_tag = splitted_md_text['start_tag']
    source_listing_infos = parse_source_listing_start(start_tag)
    code_snippet = import_code_snippet(source_listing_infos)
    splitted_md_text['text_between_start_and_end_tags'] = generate_markdown_code_listing_from_snippet(source_listing_infos,code_snippet)
    
    return splitted_md_text['text_before_start_tag'] + splitted_md_text['start_tag'] + splitted_md_text['text_between_start_and_end_tags'] + '<sourceListingEnd/>' + splitted_md_text['text_after_end_tag']

def generate_markdown_code_listing_from_snippet(source_listing_infos,code_snippet):
    lang = source_listing_infos['lang']
    return """

```{lang}
{code_snippet}
```

""".format(lang=lang,code_snippet=code_snippet)

def import_code_snippet(source_listing_infos):
    from_line = int(source_listing_infos["from"])
    to_line = int(source_listing_infos["to"])
    file_content = read_source_file(source_listing_infos["source"],)
    return cut_lines(file_content, from_line, to_line)


def cut_lines(file_as_string, from_line, to_line):
    line_array = file_as_string.split('\n')
    line_array = line_array[:(to_line)]
    line_array = line_array[(from_line-1):]

    result = '\n'.join(line_array)
    return result


def format_markdown_snippet(source_listing_infos):
    md_snippet = "```" + source_listing_infos['lang']+"\n"
    md_snippet += import_code_snippet(source_listing_infos)
    md_snippet += '\n```'
    return md_snippet

# reads file as string


def read_source_file(markdown_file_name):
    markdown_sample = open(markdown_file_name)

    file_as_string = markdown_sample.read()

    markdown_sample.close()

    return file_as_string

def parse_source_listing_start(xml_tag):
    tag_dom = xml.dom.minidom.parseString(xml_tag)
    tag = tag_dom.childNodes.item(0)
    tag.attributes.items()
    source_listing_infos = {}
    for attrName, attrValue in tag.attributes.items():
        source_listing_infos[attrName] = attrValue
    return source_listing_infos

def split_against_source_listing_tags(md_text):
    text_before_start_tag = md_text[:md_text.index('<sourceListingStart')]
    text_from_start_tag = md_text[md_text.index('<sourceListingStart'):]
    index_end_start_tag = len(text_before_start_tag) + \
        text_from_start_tag.index('/>') + 2
    start_tag = md_text[len(text_before_start_tag):index_end_start_tag]
    start_tag_length = len(start_tag)
    index_start_tag_to_end_tag = text_from_start_tag.index(
        '<sourceListingEnd/>')
    text_between_start_and_end_tags = text_from_start_tag[
        start_tag_length:index_start_tag_to_end_tag]
    index_md_text_until_end_tag = md_text.index(
        '<sourceListingEnd/>') + len('<sourceListingEnd/>')
    text_after_end_tag = md_text[index_md_text_until_end_tag:]
    return {
        "text_before_start_tag": text_before_start_tag,
        "start_tag": start_tag,
        "text_between_start_and_end_tags": text_between_start_and_end_tags,
        "text_after_end_tag": text_after_end_tag
    }
