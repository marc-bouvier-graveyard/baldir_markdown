# Baldir-Markdown

[![Sonarcloud Status](https://sonarcloud.io/api/project_badges/measure?project=marc-bouvier_baldir_markdown&metric=alert_status)](https://sonarcloud.io/dashboard?id=marc-bouvier_baldir_markdown)

Aim : a markdown preprocessor to import content of sources files from mordown file in place.

`./src/main/MyJavaFile.java`

```java
public class MyJavaFile {

    public static void main(String[] args){

        System.out.writeln("Hello world");

    }

}
```


./markdown.md
```markdown

    This is a markwdown file.


    <sourceListingStart source="./src/main/MyJavaFile.java" from="5" to="5" lang="java"/>
    ```java
            System.out.writeln("Hello world");
    ```
    <sourceListingEnd/>

```

<sourceListingStart source="./src/main/MyJavaFile.java" from="5" to="5" lang="java"/>

```java
        System.out.writeln("Hello world");
```

<sourceListingEnd/>
