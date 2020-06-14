# Baldir-Markdown

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


    &lt;sourceListingStart source="./src/main/MyJavaFile.java" from="5" to="5" lang="java"/&gt;
    ```java
            System.out.writeln("Hello world");
    ```
    &lt;sourceListingEnd/&gt;

```

&lt;sourceListingStart source="./src/main/MyJavaFile.java" from="5" to="5" lang="java"/&gt;

```java
        System.out.writeln("Hello world");
```

&lt;sourceListingEnd/&gt;
