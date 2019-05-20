import spotipy

import spotipy.oauth2 as oauth2

from tkinter import *


class Application(object):
    def getInfo(self):
        print('\nMade by some teenager in Pennsylvania\n')

    def kill(self):
        exit()

    # all strings
    def createButton(self, text, command, fg='black', width_='5', height_='2', justify='center', column_=1, row_=0, bg_='white'):
        button = Button(self.master, width=width_, height=height_, bg=bg_)
        button['text'] = str(text)
        button['fg'] = str(fg)
        button['command'] = command
        button['justify'] = justify
        button.grid(column=column_, row=row_)

        return button

    def createLabel(self, text, column_=0, row_=0):
        lbl = Label(root, text=str(text))
        lbl.grid(column=column_, row=row_)

        return lbl

    def createInput(win, width_=10, column_=0, row_=0):
        input_ = Entry(root, width=width_)
        input_.grid(column=3, row=0)

        return input_
    
    def clicked(self, givenLabel, text_):
        print(str(text_))
        res = 'You said: ' + text_.get()
        givenLabel.configure(text= res)
        
        
    def build(self):
        button1 = self.createButton('Info', self.getInfo, 'blue', column_=1, row_=0)
        killButton = self.createButton('Quit', self.kill, column_=1, row_=1, bg_='red')


        label1 = self.createLabel(text='Info Button')

        inp1 = self.createInput(column_=3)

        switchButton = self.createButton('Click Me', self.clicked(label1, text_=inp1), column_=1, row_=2, bg_='green')


    def __init__(self, master, **kwargs):
        super(Application, self).__init__()
        self.master = master
        self.build()
        

root = Tk()
root.title('Kryptonica')
root.geometry('700x500')

app = Application(root)

root.mainloop()


credentials = oauth2.SpotifyClientCredentials(
    client_id='08552cdcea3d4275ae111e7fb0138799',
    client_secret='8aa74176d02941638899c475ed7feac5')

token = credentials.get_access_token()

bryanAdams_uri = 'spotify:artist:3Z02hBLubJxuFJfhacLSDc'

spotify = spotipy.Spotify(auth=token)

results = spotify.artist_albums(bryanAdams_uri, album_type='album')
albums = results['items']
while results['next']:
    results = spotify.next(results)
    albums.extend(results['items'])
