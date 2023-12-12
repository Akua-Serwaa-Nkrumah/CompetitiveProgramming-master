import textwrap

def wrap(string, max_width):
    paragraph = []
    line = ""
    for i in string:
        if len(line)<max_width:
            line+= i
        else:
            paragraph.append(line)
            line = i
    paragraph.append(line)
    return '\n'.join(paragraph)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)