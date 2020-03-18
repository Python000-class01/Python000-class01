个人总结：

* xpath:
    - / : Selects from the root node
    - // : Selects nodes in the document from the current node that match the selection no matter where they are
    - . : Selects the current node
    - .. : Selects the parent of the current node
    - @ : Selects attribute

* xpath examples:
    - tag_name : Selects all nodes with the name "tag_name"
    - /tag_name : Selects the root element "tag_name"
    - tag_name/item : Selects all "item" elements that are children of "tag_name"
    - //tag_name : Selects all "tag_name" elements no matter where they are in the document
    - tag_name//item : Selects all "item" elements that are descendant of the "tag_name" element, no matter where they are under the "tag_name" element
    - //@attribute : Selects all attributes that are named "attribute"
    - /tag_name/item[1] : first item
    - /tag_name/item[last()] : last item
    - //title[@lang] : Selects all the title elements that have an attribute named lang
    - //title[@lang='en'] : Selects all the title elements that have a "lang" attribute with a value of "en"
    - \* : Matches any element node
    - @* : Matches any attribute node
    - //title[@*] : Selects all title elements which have at least one attribute of any kind