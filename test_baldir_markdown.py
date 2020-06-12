import pytest
from baldir_markdown import read_markdown_file , parse_source_listing_start, import_code_snippet

def test_read_markdown_file():
    result = read_markdown_file('./markdown-sample.md')
    assert result == 'Markdown preprocessor should replace code snippet between `sourceListingStart` and `sourceListingEnd` with code from the source file.\n\n<sourceListingStart source="./MyJavaFile.java" from="5" to="5" lang="java"/>\n\n```java\n        System.out.print("Hello world");\n```\n\n<sourceListingEnd/>'

def test_parse_source_listing_start():
    result = parse_source_listing_start('<sourceListingStart source="./MyJavaFile.java" from="5" to="5" lang="java"/>')
    assert result == {'from': '5', 'lang': 'java', 'source': './MyJavaFile.java', 'to': '5'}

def test_import_code_snippet():
    code_snippet = import_code_snippet({'from': '5', 'lang': 'java', 'source': './MyJavaFile.java', 'to': '5'})
    assert code_snippet == '        System.out.println("Hello world");'