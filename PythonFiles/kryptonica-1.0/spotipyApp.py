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

    def createNewArtistWindow(self, text, tab, id_):
        print('Button pressed')
        self.tabControl.add(tab, text=str(text))

        newTab = artistWindow(self.tabControl, str(text), self.music, id_)

        self.allWindows.append(newTab)
            
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
                                    #print(str(z) + ' ' + str(y[0]))
                                    if len(artistInfo) <= 3:
                                        artistInfo.append((str(z), str(y[1])))
                                    else:
                                        continue
                                        
               # artistInfo.append(str(result[obj]))

        artistInfo = list(artistInfo)
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

        if not nameVar == 'Not Found. Try Again?':

            enterArtistButton = self.createButton('Go To ' + str(nameVar), command= lambda: self.createNewArtistWindow(nameVar, artistFrame, artistID), width_=str(len(nameVar) + 2), column_=1, row_=5, bg_='orange')
        
        
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

        self.allWindows = []


class artistWindow(Frame):

    def __init__(self, root, name, music, id_):
        Frame.__init__(self, root)
    
        self.artistID = id_
        self.music = music

        self.musicPlaying = False
        
        newRoot = Tk()
        self.newRoot = newRoot
        newRoot.title(name)
        newRoot.geometry('800x500')

        albums = self.music.artist_albums(self.artistID)
        
        # WORKING -------
        
        self.fiveRelatedArtists = self.fiveRelatedArtists()
        emptyString = ''
        
        for i in range(5):
            emptyString += str(i+1) + '. ' + str(self.fiveRelatedArtists[i] + '     \n')

        self.fiveRelatedArtistText = 'Related Artists: \n' + emptyString 
        
        
        self.topFiveTracks, self.topFiveIDs = self.fiveTopTracks()

        self.topTrackIDRelation = []
        
        emptyString = ''
        
        for i in range(5):
            emptyString += str(i+1) + '. ' + str(self.topFiveTracks[i] + '\n')

        for i in range(5):
            self.topTrackIDRelation.append((self.topFiveTracks[i], i, self.topFiveIDs[i]))

        self.topFiveTracksText = 'Top Tracks: \n' + emptyString

        # ---------------
            
        for i in albums.items():
            if 'items' in i:
# Finish sorting out album data types.
                for x in i[i.index('items')]:
                    pass
        count = 1
        
        #for i in range(len(albums)):
         #   print(str(count) + '. ' + str(i))

        self.buildArtistWindow()

    def buildArtistWindow(self):
        relatedArtistLabel = self.createLabel(self.fiveRelatedArtistText)
        topFiveTracksLabel = self.createLabel(self.topFiveTracksText, 1, 0)

        stopPlaying = self.createButton('Pause Music', lambda: self.pauseMusic(), row_=8, width_=10, column_=1, bg_='red')

        self.createFivePlayButtons()

    def createFivePlayButtons(self):
        labelOne = self.createLabel('Play Top Hits:', 0, 2)
        
        buttonOne = self.createButton('Play: ' + str(self.topTrackIDRelation[0][0]), lambda: self.playTrack(self.topTrackIDRelation[0][2]), width_=len(str(self.topTrackIDRelation[0][0])) + 2, height_='1', column_=0, row_=3)
        buttonTwo = self.createButton('Play: ' + str(self.topTrackIDRelation[1][0]), lambda: self.playTrack(self.topTrackIDRelation[1][2]), width_=len(str(self.topTrackIDRelation[1][0])) + 2, height_='1', column_=0, row_=4)
        buttonThree = self.createButton('Play: ' + str(self.topTrackIDRelation[2][0]), lambda: self.playTrack(self.topTrackIDRelation[2][2]), width_=len(str(self.topTrackIDRelation[2][0])) + 2, height_='1', column_=0, row_=5)
        buttonFour = self.createButton('Play: ' + str(self.topTrackIDRelation[3][0]), lambda: self.playTrack(self.topTrackIDRelation[3][2]), width_=len(str(self.topTrackIDRelation[3][0])) + 2, height_='1', column_=0, row_=6)
        buttonFive = self.createButton('Play: ' + str(self.topTrackIDRelation[4][0]), lambda: self.playTrack(self.topTrackIDRelation[4][2]), width_=len(str(self.topTrackIDRelation[4][0])) + 2, height_='1', column_=0, row_=7)

    def createButton(self, text, command, fg='black', width_='5', height_='2', justify='center', column_=1, row_=0, bg_='white'):
        button = tk.Button(self.newRoot, width=width_, height=height_, bg=bg_)
        button['text'] = str(text)
        button['fg'] = str(fg)
        button['command'] = command
        button['justify'] = justify
        button.grid(column=column_, row=row_)

    def createLabel(self, text, column_=0, row_=0):
        lbl = Label(self.newRoot, text=str(text))
        lbl.grid(column=column_, row=row_)

        return lbl

    def pauseMusic(self):
        if self.musicPlaying:
            self.music.pause_playback()

    def playTrack(self, id_=0):
        list_ = self.music.audio_features(id_)

        self.music.start_playback(uris=list(list_[0]['uri']))
        self.musicPlaying = False
            
    def fiveTopTracks(self):
        topTracks = self.music.artist_top_tracks(self.artistID)

        topTrackList = []
        topTrackIDList = []

        for dict_ in topTracks['tracks']:
            topTrackList.append(dict_['name'])
            topTrackIDList.append(dict_['id'])

        return topTrackList[0:5], topTrackIDList[0:5]

    def fiveRelatedArtists(self):
        import random
                    
        relatedArtists = self.music.artist_related_artists(self.artistID)
        relatedArtistsList = []
        
        for dict_ in relatedArtists['artists']:
            relatedArtistsList.append(dict_['name'])

        # gets five random artists from the list and returns them.
        value = random.sample(relatedArtistsList, len(relatedArtistsList))
        
        return value[0:5]
        
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
