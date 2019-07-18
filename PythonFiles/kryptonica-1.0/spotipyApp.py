import spotipy

import tkinter as tk
import spotipy.oauth2 as oauth2

from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk, Image


class Application(object):
    def getInfo(self):
        print('\nMade by some teenager in Pennsylvania\n')

    def kill(self):
        exit()

    # all strings
    def createButton(self, text, command, fg='black', width_='5', height_='2', justify='center', column_=1, row_=0, bg_='white'):
        button = tk.Button(self.master, width=width_, height=height_, bg=bg_)
        button['text'] = str(text)
        button['fg'] = str(fg)
        button['command'] = command
        button['justify'] = justify
        button.grid(column=column_, row=row_)

        return button

    def createLabel(self, text, column_=0, row_=0):
        lbl = Label(self.master, text=str(text))
        lbl.grid(column=column_, row=row_)

        return lbl

    def createInput(self, width_=13, column_=0, row_=0):
        input_ = Entry(self.master, width=width_)
        input_.grid(column=3, row=0)        

        return input_

    def createNewWindow(self, text, tab, id_):
        print('Button pressed')
        self.tabControl.add(tab, text=str(text))

        newTab = artistWindow(self.tabControl, str(text), self.music, id_)

    def returnInput(self, inp):
        return str(inp.get())

    def updateLabel(self, label, txt):
        label.configure(text= txt)
    
    def clickedTextRepeat(self, label, inp):
        res = 'You said: ' + inp.get()
        label.configure(text= res)

    def searchArtists(self, inp, label, welcome):
        search = self.returnInput(inp)
        result = self.music.search(str(search), limit=1, type='artist')
       # print(str(result.values()))

        dict_ = result
        print(dict_.values())

        for i in result.values():
            # i is the three paragraph sections
            if 'items' in i:
                for x in i['items']:
                    for y in list(x.items()):
                        if str(y[0]) == 'id':
                            artistID = str(y[1])

        
        # Gather artist data

        searchList = ['name', 'genres', 'popularity']
        printList = ['Name: ', 'Genres: ', 'Popularity: ']
        artistInfo = []

        string = ''

        for obj in searchList:
            for i in result.values():
                # i is the three paragraph sections
                if 'items' in i:
                    for x in i['items']:
                        for y in list(x.items()):
                            for z in searchList:
                                if str(z) == str(y[0]).strip():
                                    print(str(z) + ' ' + str(y[0]))
                                    if len(artistInfo) <= 3:
                                        artistInfo.append((str(z), str(y[1])))
                                    else:
                                        continue
                                        
               # artistInfo.append(str(result[obj]))

        artistInfo = list(artistInfo)
        print(str(artistInfo))
        artistInfo.sort()

        nameVar = 'Not Found. Try Again?'
        genreVar = 'Not Found. Try Again?'
        popVar = 'Not Found. Try Again?'
        
        for i in artistInfo:
            if i[0] == 'name':
                nameVar = str(i[1])
            elif i[0] == 'genres':
                genreVar = str(i[1])
            elif i[0] == 'popularity':
                popVar = str(i[1])


        #"['album rock', 'canadian pop', 'classic canadian rock', 'heartland rock', 'mellow gold', 'rock', 'soft rock']"
        #Above is the issue. 


        gString = ''
        if not genreVar == 'Not Found. Try Again?':
            for i in list(genreVar):
                if i == ']' or i == '[' or i == '\'':
                    pass
                else:    
                    gString = gString + str(i)              


        gString.replace('\'', '')
        gString.replace('[', '')
        gString.replace(']', '')
        gString.replace(',', '')
                                    
        string = 'Search Results: \n' + 'Name: ' + nameVar + '\nGenres: ' + str(gString) + '\nPopularity: ' + popVar + '\n'

        self.updateLabel(self.result, string)

        artistFrame = Frame(self.tabControl)

        enterArtistButton = self.createButton('Go To ' + str(nameVar), command= lambda: self.createNewWindow(nameVar, artistFrame, artistID), width_=str(len(nameVar) + 2), column_=1, row_=5, bg_='orange')

        
    def build(self):
        button1 = self.createButton('Info', self.getInfo, 'blue', column_=1, row_=0)
        killButton = self.createButton('Quit', self.kill, column_=1, row_=1, bg_='red')

        


        self.label1 = self.createLabel(text='Info Button')
        self.result = self.createLabel(text='Results: ', column_=3, row_=1)


        self.inp1 = self.createInput(column_=3)

        switchButton = self.createButton('Search: ', command= lambda: self.searchArtists(self.inp1, self.result, welcomeTab), column_=1, row_=2, bg_='green')

    def __init__(self, master, music, welcome, tabControl, **kwargs):
        super(Application, self).__init__()
        self.tabControl = tabControl
        self.master = master
        self.music = music
        self.build()

class artistWindow(Frame):

    def __init__(self, root, name, music, id_):
        Frame.__init__(self, root)
    
        self.artistID = id_
        self.music = music
        
        newRoot = Tk()
        newRoot.title(name)
        newRoot.geometry('800x500')

        albums = self.music.artist_albums(self.artistID)

        for i in albums.items():
            if 'items' in i:
                print('\n\n\n\n' + str(i) + '\n\n\n')
# Finish sorting out album data types.
                for x in i[i.index('items')]:
                    pass
        count = 1

        print(albums)
        
        for i in range(len(albums)):
            print(str(count) + '. ' + str(i))  

    def createArtistButton(self, text, command, fg='black', width_='5', height_='2', justify='center', column_=1, row_=0, bg_='white'):
        button = tk.Button(self.master, width=width_, height=height_, bg=bg_)
        button['text'] = str(text)
        button['fg'] = str(fg)
        button['command'] = command
        button['justify'] = justify
        button.grid(column=column_, row=row_)

        return button

        
        

root = Tk()
root.title('Kryptonica')
root.geometry('800x500') # Make 1950x990

tabControl = Notebook(root)
# Use this as tab creation (nb)

welcomeTab = Frame(tabControl)

tabControl.add(welcomeTab, text='Welcome!')

#tabControl.pack(expand=1, fill='both')

# Implements background image (Include Image in package)

filepath = 'tkBackground2.jpg'
imported = Image.open(filepath)
backgroundImage = ImageTk.PhotoImage(imported)

backgroundLabel = tk.Label(root, image=backgroundImage)
backgroundLabel.place(x=0, y=0, relwidth=1, relheight=1)





credentials = oauth2.SpotifyClientCredentials(
    client_id='08552cdcea3d4275ae111e7fb0138799',
    client_secret='8aa74176d02941638899c475ed7feac5')

token = credentials.get_access_token()


spotify = spotipy.Spotify(auth=token)

app = Application(root, spotify, welcomeTab, tabControl)

root.mainloop()

"""
bryanAdams_uri = 'spotify:artist:3Z02hBLubJxuFJfhacLSDc'

results = spotify.artist_albums(bryanAdams_uri, album_type='album')
albums = results['items']
while results['next']:
    results = spotify.next(results)
    albums.extend(results['items'])
"""
