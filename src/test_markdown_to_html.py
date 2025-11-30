import unittest
from main import markdown_to_html_node


class TestMarkdownToHTML(unittest.TestCase):
    def test_markdown_to_html_node(self):
        md = """
# This is a heading

This is a paragraph with **bold** and *italic* text.

- This is a list
- with items

1. This is an ordered list
2. with items

> This is a quote
> block

```
This is a code block
```
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>This is a heading</h1><p>This is a paragraph with <b>bold</b> and <i>italic</i> text.</p><ul><li>This is a list</li><li>with items</li></ul><ol><li>This is an ordered list</li><li>with items</li></ol><blockquote>This is a quote block</blockquote><pre><code>This is a code block</code></pre></div>",
        )

    def test_headings(self):
        md = """
# Heading 1

## Heading 2

### Heading 3

#### Heading 4

##### Heading 5

###### Heading 6
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>Heading 1</h1><h2>Heading 2</h2><h3>Heading 3</h3><h4>Heading 4</h4><h5>Heading 5</h5><h6>Heading 6</h6></div>",
        )

    def test_blockquote(self):
        md = """
> This is a
> blockquote
> block
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote block</blockquote></div>",
        )

    def test_code_block(self):
        md = """
```
This is a code block
```
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is a code block</code></pre></div>",
        )
