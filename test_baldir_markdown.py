import pytest
from baldir_markdown import read_source_file, parse_source_listing_start, import_code_snippet, format_markdown_snippet, split_against_source_listing_tags


def test_read_source_file():
    result = read_source_file('./markdown-sample.md')
    assert result == 'Markdown preprocessor should replace code snippet between `sourceListingStart` and `sourceListingEnd` with code from the source file.\n\n<sourceListingStart source="./MyJavaFile.java" from="5" to="5" lang="java"/>\n\n```java\n        System.out.print("Hello world");\n```\n\n<sourceListingEnd/>\n\nend'


def test_parse_source_listing_start():
    result = parse_source_listing_start(
        '<sourceListingStart source="./MyJavaFile.java" from="5" to="5" lang="java"/>')
    assert result == {'from': '5', 'lang': 'java',
                      'source': './MyJavaFile.java', 'to': '5'}


def test_import_code_snippet_one_line():
    code_snippet = import_code_snippet(
        {'from': '5', 'lang': 'java', 'source': './MyJavaFile.java', 'to': '5'})
    assert code_snippet == '        System.out.println("Hello world");'


def test_import_code_snippet_range():
    code_snippet = import_code_snippet(
        {'from': '4', 'lang': 'java', 'source': './MyJavaFile.java', 'to': '5'})
    assert code_snippet == '\n        System.out.println("Hello world");'


def test_import_code_snippet_whole_file():
    code_snippet = import_code_snippet(
        {'from': '1', 'lang': 'java', 'source': './MyJavaFile.java', 'to': '9'})
    assert code_snippet == """public class MyJavaFile {

    public static void main(String[] args){

        System.out.println("Hello world");

    }

}"""


def test_format_markdown_snippet():
    formatted_snippet = format_markdown_snippet(
        {'from': '1', 'lang': 'java', 'source': './MyJavaFile.java', 'to': '9'})
    assert formatted_snippet == """```java
public class MyJavaFile {

    public static void main(String[] args){

        System.out.println("Hello world");

    }

}
```"""


def test_split_against_source_listing_tags():
    md_text = """Markdown preprocessor should replace code snippet between `sourceListingStart` and `sourceListingEnd` with code from the source file.

<sourceListingStart source="./MyJavaFile.java" from="5" to="5" lang="java"/>

```java
        System.out.print("Hello world");
```

<sourceListingEnd/>

end"""
    splitted_text = split_against_source_listing_tags(md_text)
    assert splitted_text['text_before_start_tag'] == """Markdown preprocessor should replace code snippet between `sourceListingStart` and `sourceListingEnd` with code from the source file.

"""
    assert splitted_text['start_tag'] == '<sourceListingStart source="./MyJavaFile.java" from="5" to="5" lang="java"/>'
    assert splitted_text['text_between_start_and_end_tags'] == """

```java
        System.out.print("Hello world");
```

"""
    assert splitted_text['text_after_end_tag'] == """

end"""
