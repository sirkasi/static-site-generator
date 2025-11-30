import unittest
from htmlnode import HtmlNode


class TestHtmlNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HtmlNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )

    def test_to_html_no_children(self):
        node = HtmlNode("p", "Hello, world!")
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "Hello, world!")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)

    def test_to_html_with_children(self):
        child_node = HtmlNode("span", "child")
        parent_node = HtmlNode("div", "parent", [child_node])
        self.assertEqual(parent_node.tag, "div")
        self.assertEqual(parent_node.value, "parent")
        self.assertEqual(parent_node.children, [child_node])
        self.assertEqual(parent_node.props, None)
