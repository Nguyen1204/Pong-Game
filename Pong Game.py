
from tkinter import *

class Ball (Frame):
    def __init__ (self):
        Frame.__init__ (self)
        self.master.title ("Pong Game")
        self.grid ()
        canvas_width = 800
        canvas_height = 400
        self.canvas = Canvas(self, width = canvas_width, height = canvas_height , bg = "black")
        self.canvas.grid(row = 1)

        #lives of player
        self.lives = 3

        #creating the ball
        ball_diameter = 20 
        top_x = 2 
        top_y = 2
        ball = self.canvas.create_oval(top_x, top_y, top_x + ball_diameter, top_y + ball_diameter, 
                                       fill = "orange" , tags = "ball")

        horizontal_direction = "east"
        vertical_direction = "south"
        dx = dy = 4 #speed of the ball

        #draw rectangle for paddle
        self.paddleTopx = 360
        self.paddleTopy = 380
        self.paddleWidth = 80
        self.paddleHeight = 20
        self.paddle = self.canvas.create_rectangle (self.paddleTopx, self.paddleTopy, self.paddleTopx + self.paddleWidth, self.paddleTopy + self.paddleHeight, 
                                                    fill = "grey", tags = "rect")

        #bind arrow keys to move paddle
        self.canvas.focus_set()
        self.canvas.bind('<KeyPress-Left>', self.moveLeft)
        self.canvas.bind('<KeyPress-Right>', self.moveRight)   

        #the ball animation
        while True:
            try:
                if horizontal_direction == "east":
                    top_x += dx 
                    if top_x >= (canvas_width - ball_diameter): 
                        horizontal_direction = "west" 
                    self.canvas.move("ball", dx, 0)
                    

                else: 
                    top_x -= dx
                    if top_x <= 0: 
                        horizontal_direction = "east"
                    self.canvas.move("ball", -dx, 0)
                    
                    
                if vertical_direction == "south":
                    top_y += dy
                    if top_y >= (canvas_height - ball_diameter):
                        vertical_direction = "north"
                    self.canvas.move("ball", 0, dy)
                    
                    #collision detection
                    if top_y >= 350:
                        leftPaddle = self.paddleTopx <= top_x <=(self.paddleTopx +80)
                        rightPaddle = self.paddleTopx <= top_x+80 <=(self.paddleTopx +80)
                        if leftPaddle or rightPaddle:
                            vertical_direction = "north"
                            self.canvas.move("ball", 0, dy)

                    #dectect if ball hit floor (also keeps track of lives)
                    if top_y >= 380:
                        self.lives -= 1

                else:
                    top_y -= dy
                    if top_y <= 0:
                        vertical_direction = "south"
                    self.canvas.move("ball", 0, -dy)
                

                
            except:
                break

            self._label = Label(self, text = "Remaining lives: " + str(self.lives), font =("Verdana", 20))
            self._label.grid(row = 0)

            #Ends Game when lives have reached 0
            if self.lives == 0:
                self._label = Label(self, text = "Remaining lives: 0", font =("Verdana", 20))
                self._label.grid(row = 0)
                self.canvas.delete ("ball")
                ball = self.canvas.create_oval(2, 2, 2 + ball_diameter, 2 + ball_diameter, fill = "orange" , tags = "ball")
                break
                            
            self.canvas.after(15) 
            self.canvas.update()
    
    #keyboard controls for right and left
    def moveLeft (self, event):
        if self.paddleTopx >= 5:
            self.canvas.delete ("rect")
            self.paddleTopx -= 15 #speed
        self.canvas.create_rectangle (self.paddleTopx, self.paddleTopy, self.paddleTopx + self.paddleWidth, self.paddleTopy + self.paddleHeight, 
                                      fill = "grey", tags = "rect")
            

    def moveRight (self, event):
        if self.paddleTopx <= 720:
            self.canvas.delete ("rect")
            self.paddleTopx += 15 #speed
        self.canvas.create_rectangle (self.paddleTopx, self.paddleTopy, self.paddleTopx + self.paddleWidth, self.paddleTopy + self.paddleHeight, 
                                      fill = "grey", tags = "rect")
        
                 
def main():
    Ball().mainloop()

main()