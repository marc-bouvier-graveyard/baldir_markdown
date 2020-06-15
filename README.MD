# Baldir-Markdown

[![Sonarcloud Status](https://sonarcloud.io/api/project_badges/measure?project=marc-bouvier_baldir_markdown&metric=alert_status)](https://sonarcloud.io/dashboard?id=marc-bouvier_baldir_markdown)
[![Github Action CI Status](https://github.com/marc-bouvier/baldir_markdown/workflows/Python%20package/badge.svg)](https://github.com/marc-bouvier/baldir_markdown/actions?query=workflow%3A%22Python+package%22)

Aim : a markdown preprocessor to import content of sources files from markdown file in place.

This can be a building block for making [Living documentation](
https://github.com/LivingDocumentation/awesome-living-documentation/blob/master/README.adoc) on platforms. that does not support asciidoc.

Usages examples:

* (re)-generate doc with snippets included in azure devops pipeline.
* check is doc is up to date against current code

`./src/main/MyJavaFile.java`

```java
public class MyJavaFile {

    public static void main(String[] args){

        System.out.writeln("Hello world");

    }

}
```

`./markdown.md`

````markdown
    This is a markwdown file.


    <sourceListingStart source="./src/main/MyJavaFile.java" from="5" to="5" lang="java"/>
    ```java
            System.out.writeln("Hello world");
    ```
    <sourceListingEnd/>
````

<sourceListingStart source="./src/main/MyJavaFile.java" from="5" to="5" lang="java"/>

```java
        System.out.writeln("Hello world");
```

<sourceListingEnd/>
