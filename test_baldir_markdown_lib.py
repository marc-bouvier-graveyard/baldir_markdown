import pytest
import tempfile
import shutil
from baldir_markdown_lib import read_source_file, parse_source_listing_start, import_code_snippet, format_markdown_snippet, split_against_source_listing_tags, pre_process_markdown_file_in_place, pre_process_markdown_text, pre_process_markdown_file_to_string, verify


def test_verify_mismatch_after_pre_processing():
    assert verify('markdown-sample-without-snippet.md') == False


def test_verify_match_after_pre_processing():
    assert verify('markdown-sample.md') == True


def test_pre_process_markdown_file_in_place():
    md_temp_file_path = shutil.copy(
        'markdown-sample-without-snippet.md', tempfile.mkdtemp()+'/markdown-sample.md')
    pre_process_markdown_file_in_place(md_temp_file_path)
    file_pre_processed = open(md_temp_file_path)
    text_pre_processed = file_pre_processed.read()
    file_pre_processed.close()
    assert text_pre_processed == """Markdown preprocessor should replace code snippet between `sourceListingStart` and `sourceListingEnd` with code from the source file.

<sourceListingStart source="./MyJavaFile.java" from="5" to="5" lang="java"/>
```java
        System.out.println("Hello world");
```
<sourceListingEnd/>

end"""


def test_pre_process_markdown_file_to_string():
    md_temp_file_path = shutil.copy(
        'markdown-sample-without-snippet.md', tempfile.mkdtemp()+'/markdown-sample.md')
    assert pre_process_markdown_file_to_string(md_temp_file_path) == """Markdown preprocessor should replace code snippet between `sourceListingStart` and `sourceListingEnd` with code from the source file.

<sourceListingStart source="./MyJavaFile.java" from="5" to="5" lang="java"/>
```java
        System.out.println("Hello world");
```
<sourceListingEnd/>

end"""


def test_pre_process_markdown_text():
    markdown_text = """Markdown preprocessor should replace code snippet between `sourceListingStart` and `sourceListingEnd` with code from the source file.

<sourceListingStart source="./MyJavaFile.java" from="5" to="5" lang="java"/>


<sourceListingEnd/>

end"""
    result_as_string = pre_process_markdown_text(markdown_text)
    print(result_as_string)
    assert result_as_string == """Markdown preprocessor should replace code snippet between `sourceListingStart` and `sourceListingEnd` with code from the source file.

<sourceListingStart source="./MyJavaFile.java" from="5" to="5" lang="java"/>
```java
        System.out.println("Hello world");
```
<sourceListingEnd/>

end"""


def test_read_source_file():
    result = read_source_file('./markdown-sample.md')
    assert result == 'Markdown preprocessor should replace code snippet between `sourceListingStart` and `sourceListingEnd` with code from the source file.\n\n<sourceListingStart source="./MyJavaFile.java" from="5" to="5" lang="java"/>\n```java\n        System.out.println("Hello world");\n```\n<sourceListingEnd/>\n\nend'


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
        System.out.println("Hello world");
```

<sourceListingEnd/>

end"""
    splitted_text = split_against_source_listing_tags(md_text)
    assert splitted_text['text_before_start_tag'] == """Markdown preprocessor should replace code snippet between `sourceListingStart` and `sourceListingEnd` with code from the source file.

"""
    assert splitted_text['start_tag'] == '<sourceListingStart source="./MyJavaFile.java" from="5" to="5" lang="java"/>'
    assert splitted_text['text_between_start_and_end_tags'] == """

```java
        System.out.println("Hello world");
```

"""
    assert splitted_text['text_after_end_tag'] == """

end"""
