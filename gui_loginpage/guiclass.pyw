from tkinter import *
class gui():
    def __init__(self,height:int,width:int,title:str) -> None:
        '''initial root window startup'''
        self.root = Tk()
        self.height = height
        self.width = width
        self.title = title
        self.root.geometry(f'{self.height}x{self.width}')
        self.root.title(self.title)
        self.background = NONE

    def set_minsize(self,height:int,width:int):
        '''fix minimum sixe of gui window'''
        self.root.minsize(height,width)

    def set_maxsize(self,height:int,width:int):
        '''fix max size of gui window'''
        self.root.maxsize(height,width)

    def set_background(self,background_color='white'):
        '''Base background'''
        self.background = Canvas(self.root,height=self.height,width=self.width,background=background_color)
        self.background.pack(fill='both',)

    def create_polygon(self,x1,y1,x2,y2,x3,y3,color1 = 'white',color2 = 'black'):
        '''Two triangle with different color'''
        self.background.create_polygon((x1,y1,x2,y2,x3,y3),fill=color1)
        self.background.create_polygon((0,0,1080,0,1080,720),fill=color2)

    def create_frame(self,length:int,breadth:int,background_color = 'white',border_ = 'black',size = 0):
        '''login window frame layout design'''
        frame = Frame(self.root,highlightbackground=border_,highlightthickness=size,background=background_color)
        frame.place(relx=0.5,rely=0.5,anchor='center',height=length,width=breadth)

    def create_label(self):
            pass
    
    def run(self):
        '''runs the whole window in loop'''
        self.root.mainloop()


_gui = gui(1080,720,'eesh')
_gui.set_background()
_gui.create_polygon(0,0,0,720,1080,720,'red','blue')
_gui.set_minsize(1080,720)
_gui.set_maxsize(1080,720)
_gui.run()

        
