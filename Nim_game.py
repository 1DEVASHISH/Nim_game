import pygame

pygame.init()

window_height = 500
window_width = 600
window  = pygame.display.set_mode((window_height,window_width))
"""window_bg = pygame.image.load("PRO.jpg")
window_bg= pygame.transform.scale(window_bg,(500,600))"""

font = pygame.font.Font('freesansbold.ttf', 32)
turn_color = (219,70 ,77)
window_bg = (255, 220, 200)
"""turn_bg= pygame.image.load("PRO.jpg")"""

player1 = font.render("Player_1  Enter The Number :", True, turn_color)
player2 = font.render("Player_2 Enter The Number :", True, turn_color)

 

class button():
    def __init__(self, color, x,y,width,height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.over = False

    def draw(self,window,outline=None):
        #Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(window, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
                    
        pygame.draw.rect(window, self.color, (self.x,self.y,self.width,self.height),0)
                
        if self.text != '':
            font = pygame.font.SysFont('comicsans', 60)
            text = font.render(self.text, 1, (0,0,0))
            window.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False

    """def playSoundIfMouseIsOver(self, pos, sound):
        if self.isOver(pos):            
            if not self.over:
                # beepsound.play()
                self.over = True
        else:
            self.over = False"""
                    
white = (255,255,255)
# the numbers for the calcaltor
s_1s = button((0,255,0),50,350,100,50, '1')
s_2s = button((0,255,0),200,350,100,50, '2')
s_3s = button((0,255,0),350,350,100,50, '3')
s_4s = button((0,255,0),50,410,100,50, '4')
s_5s = button((0,255,0),200,410,100,50, '5')
s_6s = button((0,255,0),350,410,100,50, '6')
s_7s = button((0,255,0),50,470,100,50, '7')
s_8s = button((0,255,0),200,470,100,50, '8')
s_9s = button((0,255,0),350,470,100,50, '9')
s_10s = button((0,255,0),200,530,100,50, '10')

numbers = [s_1s,s_2s,s_3s,s_4s,s_5s,s_6s,s_7s,s_8s,s_9s,s_10s]

d_6s = button((0,255,0),310,220,150,50, 'EXIT')

symbols = [d_6s]


# redraw window
def redraw(inputtap):
    # draw all the numbers
    for button in numbers:
        button.draw(window)

    # the symbols
    for button in symbols:
        button.draw(window)

    inputtap.draw(window)

def Symbols():
    global user_input
    global python_input
    global is_finished

    if event.type == pygame.MOUSEBUTTONDOWN:
        pos = pygame.mouse.get_pos()



        if d_6s.isOver(pos):
            print("C")
            python_input = ""
            user_input = ""
            exit()



def MOUSEOVERnumbers():
    global user_input
    global python_input
    global is_finished

    if event.type == pygame.MOUSEBUTTONDOWN:
        if is_finished:
            user_input = ""
            python_input = ""
            is_finished = False
        pos = pygame.mouse.get_pos()          
        if s_1s.isOver(pos):
            print("1")
            user_input += "1"
            python_input += "1"
            return 1, True
        if s_2s.isOver(pos):
            print("2")
            user_input += "2"
            python_input += "2"
            return 2, True
        if s_3s.isOver(pos):
            print("3")
            user_input += "3"
            python_input += "3"
            return 3, True
        if s_4s.isOver(pos):
            print("4")
            user_input += "4"
            python_input += "4"
            return 4, True
        if s_5s.isOver(pos):
            print("5")
            user_input += "5"
            python_input += "5"
            return 5, True
        if s_6s.isOver(pos):
            print("6")
            user_input += "6"
            python_input += "6"
            return 6, True
        if s_7s.isOver(pos):
            print("7")
            user_input += "7"
            python_input += "7"
            return 7, True
        if s_8s.isOver(pos):
            print("8")
            user_input += "8"
            python_input += "8"
            return 8, True
        if s_9s.isOver(pos):
            print("9")
            user_input += "9"
            python_input += "9"
            return 9, True
        if s_10s.isOver(pos):
            print("10")
            user_input += "10"
            python_input += "10"
            return 10, True
    return 0, False


# the main loop
run = True
user_input = ""
python_input = ""
is_finished = True



def with_user(turn,s,x):  
    # print("Enter the value from 1 to 10:") 
    # while s<100:
    if(turn):
            if 0<x<11:
                turn,s=play (x,turn,s)
                return turn, s
            else:
                print("Invalid!!!")    
    else:
        if 0<x<11:
            turn,s=play (x,turn,s)
            return turn, s
        else:
            print("Invalid!!!")           
    print("Sum=",s)
    if turn ==False:
        print("Player1 won!")
    else:
        print("Player2 won!")




s=0
turn=True
def play(x,turn,s):
    s+=x
    global user_input 
    user_input = f"{s}"
    print("Sum=",s)
    if(turn):
        turn = False
    else:
        turn = True
    return turn,s,


while run:
    # input tap
    if s<100:
        inputtap = button((253,100,32),10,280,450,50,f"{user_input}")
        window.fill(window_bg)
        # window.blit(text, textRect)
        if turn :
            window.blit(player1, (25,25))
        else:
            window.blit(player2, (25,25))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            
            if s<100:    
                x,b=MOUSEOVERnumbers()
                if b:
                    turn, s=with_user(turn, s,x)
    else:
        if turn==False:
            inputtap = button((245,85,5),10,280,450,50,F"PLAYER 1 WIN!")
        else:
            inputtap = button((245,85,5),10,280,450,50,"PLAYER 2 WIN!")           
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    Symbols()
  

    redraw(inputtap)
    pygame.display.update()

pygame.quit()
