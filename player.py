""""

Name : R.Lokesh

Project : Music Player

Module : Tkinter


"""

################################################ Importing The necessary Module ###############################################################
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import time
import pygame # Can ne installed from command prompt by using ---> pip install pygame

# Initializing the pygame mixer module and Setting some global variable for pause function ###################################################
pygame.mixer.init()

global paused

paused = False

################################################## Creating a class for our Music Player ########################################################

class Player:

    #################################### Defining all the required functions for our Music Player ###############################################
            
    def Import(self):

        # Importing the file using tkinter's askopenfilename method
        Import_file = filedialog.askopenfilename(initialdir='C:/Users/user/Documents/Music Player/Audio',title='Choose a File',filetypes=(('.mp3 Files','*.mp3'),))

        # Declaring the global variable
        global Renamed_file

        # Replacing the path with None
        Renamed_file = Import_file.replace('C:/Users/user/Documents/Music Player/Audio/','')

        # Inserting the song into our list box
        self.list_songs.insert(0,Renamed_file)

    def Import_Multiple(self):
        try:
            # Importing Muliple files wih filedialog askopenfilenames method 
            Import_file = filedialog.askopenfilenames(initialdir='C:/Users/user/Documents/Music Player/Audio',title='Choose a File',filetypes=(('.mp3 Files','*.mp3'),))

            # Looping through our files and importing as well as displaying each files
            for file in Import_file:

                Renamed_file = file.replace('C:/Users/user/Documents/Music Player/Audio/','')

                # Inserting the file inside our listbox
                self.list_songs.insert(0,Renamed_file)
        except:
            print('[!!ERROR!!]')
    def Play(self):

        try:
            # Getting the active song and storing it in a variable called play_music
            play_music = self.list_songs.get(ACTIVE)

            Rename_file = (f'C:/Users/user/Documents/Music Player/Audio/{play_music}')

            # Loading our music using pygame mixer.load() method
            pygame.mixer.music.load(Rename_file)

            # Playing the loaded music using the pygame play() method
            pygame.mixer.music.play()

            self.play_time()
        except:
            print('[!!ERROR!!]')
    def Stop(self):

        # Stopping the plaing music using pygame stop() method
        pygame.mixer.music.stop()

    def Delete_One(self):
        # Active method of list box gets the active song and the delete method deletes the Selected song.
        self.list_songs.delete(ACTIVE)

        # Code to stop the music when the song is deleted
        pygame.mixer.music.stop()
        
    def Delete_Many(self):
        self.list_songs.delete(0,END)
        
        pygame.mixer.music.stop()

        
    def Pause(self,is_paused):

        # Defining a simple code which pauses and unpauses the song
        try:
            global paused
            
            paused = is_paused

            # if the music is paused then this line of code is executed
            if paused:
                pygame.mixer.music.unpause()
                paused = False

            # else if the song is unpaused this line of code is executed to pause the song
            else:
                pygame.mixer.music.pause()
                
                paused = True
        except:
            print('[!!ERROR]')
            
    def Next_Song(self):

        # the curselection() method gets the current selection of listbox 
        current_song_list = self.list_songs.curselection()
        
        # the above recieved file is in the form of tuple so we are going to use the index to get the 1st item
        current_song = current_song_list[0]+1

        # loading the current song
        song = self.list_songs.get(current_song)
                
        Rename_file = (f'C:/Users/user/Documents/Music Player/Audio/{song}')

        # Loading the recieved music
        pygame.mixer.music.load(Rename_file)

        pygame.mixer.music.play()

        # These subsequent lines of code changes the list box selection to the next one 
        self.list_songs.selection_clear(0,END)

        self.list_songs.activate(current_song)

        self.list_songs.selection_set(current_song,last=None)
            
    def Previous_Song(self):
        current_song_list = self.list_songs.curselection()
                
        current_song = current_song_list[0]-1
                
        song = self.list_songs.get(current_song)
                
        Rename_file = (f'C:/Users/user/Documents/Music Player/Audio/{song}')

        pygame.mixer.music.load(Rename_file)

        pygame.mixer.music.play()

        self.list_songs.selection_clear(0,END)

        self.list_songs.activate(current_song)

        self.list_songs.selection_set(current_song,last=None)

    def play_time(self):

        
        current_time = pygame.mixer.music.get_pos()/1000

        current_time_converted = time.strftime('%H:%M:%S',time.gmtime(current_time))

        self.status_bar.config(text=f"Time Elasped : {current_time_converted}")

        self.status_bar.after(1000,self.play_time)

    def Volume(self,x):

        pygame.mixer.music.set_volume(self.Slider_Volume.get())

     
            
    ############################################### Initializing the constructor #############################################################
    
    def __init__(self,master):
        
        # Creating our main Graphical User Interface Window
        self.master = master

        # Adding title to our GUI window
        master.title("Music Player")

        
        # Opening all the reqquired Images and icon files
         
        self.img_play = PhotoImage(file ='C:/Users/user/Documents/Music Player/Images/play.png')
        self.img_pause = PhotoImage(file ='C:/Users/user/Documents/Music Player/Images/pause.png')
        self.img_stop = PhotoImage(file ='C:/Users/user/Documents/Music Player/Images/stop.png')
        self.img_next = PhotoImage(file ='C:/Users/user/Documents/Music Player/Images/next.png')
        self.img_back = PhotoImage(file ='C:/Users/user/Documents/Music Player/Images/back.png')

        #################################### Creating our menubar with sub-menus ############################################################
        self.menubar = Menu(master)

        # Configuring our Menubar
        master.config(menu=self.menubar)

        # Creating our file menu
        self.file_menu = Menu(self.menubar)
        self.file_menu.add_command(label="Import a File",command=self.Import)
        self.file_menu.add_command(label="Import multiple Files",command=self.Import_Multiple)
        self.menubar.add_cascade(menu=self.file_menu,label="Import")

        # Creating our Editing menu
        self.delete_menu = Menu(self.menubar)
        self.delete_menu.add_command(label="Remove a File",command=self.Delete_One)
        self.delete_menu.add_command(label="Remove multiple Files",command=self.Delete_Many)
        self.menubar.add_cascade(menu=self.delete_menu,label="Remove")

        ####################################### Adding our container widgets ################################################################
        
        self.frame_Main = Frame(master)
        self.frame_Top = Frame(self.frame_Main)
        self.frame_Bottom = Frame(self.frame_Main)
        self.frame_Up = Frame(self.frame_Bottom)
        self.frame_Down = Frame(self.frame_Bottom)
        self.frame_Down_down = Frame(self.frame_Down)
        self.frame_Down_up = Frame(self.frame_Down)
        
        
        # Adding GridLayouts to our container Widgets
        
        self.frame_Main.grid(row=0,column=0)
        self.frame_Top.grid(row=0,column=0)
        self.frame_Bottom.grid(row=1,column=0)
        self.frame_Up.grid(row=0,column=0)
        self.frame_Down.grid(row=1,column=0)
        self.frame_Down_up.grid(row=0,column=0)
        self.frame_Down_down.grid(row=1,column=0)

        ############################# Creating a list box to insert all the imported songs ###################################################

        self.list_songs = Listbox(self.frame_Top,width=60,height=20,bg="powder blue",fg="white",font=('arial',12,'bold'))
        self.list_songs.grid(row=0,column=0,padx=10,pady=10)

        ################################################# Adding the buttons ##################################################################
        
        self.Button_next= Button(self.frame_Up,image=self.img_next,borderwidth=0,command=self.Next_Song)
        self.Button_next.grid(row=0,column=2,padx=10,pady=10)

        self.Button_back= Button(self.frame_Up,image=self.img_back,borderwidth=0,command=self.Previous_Song)
        self.Button_back.grid(row=0,column=0,padx=10,pady=10)
        
        self.Slider_Volume = ttk.Scale(self.frame_Up,from_=0,to_=1,value=1,length=350,orient='horizontal',command=self.Volume)
        self.Slider_Volume.grid(row=0,column=1)

        self.Button_play = Button(self.frame_Down_up,image=self.img_play,borderwidth=0,command=self.Play)
        self.Button_play.grid(row=1,column=1,padx=10)

        self.Button_pause = Button(self.frame_Down_up,image=self.img_pause,borderwidth=0,command=lambda:self.Pause(paused))
        self.Button_pause.grid(row=1,column=0,padx=10)

        self.Button_stop = Button(self.frame_Down_up,image=self.img_stop,borderwidth=0,command=self.Stop)
        self.Button_stop.grid(row=1,column=2,padx=10)

        self.status_bar = Label(self.frame_Down_down,width=75,bg="ghost white",bd=2,relief=GROOVE,text="")
        self.status_bar.grid(row=2,column=0,ipady=2,ipadx=2,padx=10,pady=10)
        
       
        
############################################################Class Ends...#########################################################################

        
if __name__ == '__main__':

    root = Tk()

    app = Player(root)

    root.mainloop()

################################################################ END #############################################################################
