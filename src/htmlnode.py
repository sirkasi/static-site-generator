class HtmlNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.children = children   
        self.value = value  
        self.props = props

    def __eq__(self, other):
        return (
            self.tag == other.tag
            and self.children == other.children
            and self.value == other.value
            and self.props == other.props
        )

    def __repr__(self):
        return f"HtmlNode({self.tag}, {self.children}, {self.value}, {self.props})"

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props is None:
            return ""
        
        text = ""
        for key, value in self.props.items():
            text += f' {key}="{value}"'
        return text

    
