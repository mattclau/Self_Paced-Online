class Element:
    tag = 'html'
    indent = '    '

    def __init__(self, content=None):
        if content is None:
            self.content = []
        else:
            self.content = [content]

    def append(self, added_content):
        self.content.append(added_content)

    def render(self, file_out, cur_ind=''):
        file_out.write(cur_ind + '<{}>\n'.format(self.tag))
        for item in self.content:
            file_out.write(item + '\n')
        file_out.write('</{}>\n'.format(self.tag))

class Html(Element):
    tag = 'html'

class Body(Element):
    tag = 'body'

class P(Element):
    tag = 'p'
