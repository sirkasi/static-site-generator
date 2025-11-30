from htmlnode import HtmlNode

class ParentNode(HtmlNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.children is None:
            raise ValueError("Children cannot be None")
        
        if self.tag is None:
            raise ValueError("Tag cannot be None")
        
        text = f"<{self.tag}{self.props_to_html()}>"
        for child in self.children:
            text += child.to_html()
        text += f"</{self.tag}>"
        return text