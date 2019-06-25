class Cas():
    def __init__(self):
        pass

    def createOpening(self, title='Hello!'):
        string = '''Content-type: text/html\r\n\r\n
        <html>
            <title>''' + str(title) + '''</title> 
            <body>
                hello World
            </body>
            '''

        return string
            
