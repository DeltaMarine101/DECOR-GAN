import tkinter as tk

class ImgCanvas(object):
  def __init__(self, canvas, img):
    self.canvas = canvas
    self.show_dot = False
    self.dot_size = 10
    self.image = img
    self.moved = False
    
    self.dot_loc = (500,500)
    self.mouse_down = False

    canvas.bind('<Enter>',  self.showDot)
    canvas.bind('<Leave>',  self.hideDot)
    # canvas.bind('<Motion>', self.onMouseMove)
    # canvas.bind("<ButtonPress-1>", self.onMouseDown)
    # canvas.bind("<ButtonRelease-1>", self.onMouseUp)
    
    self.canvas.create_image(0, 0, anchor=tk.NW, image=self.image)
    self.drawDot()

  def showDot(self, event):
    self.show_dot = True

  def hideDot(self, event):
    self.show_dot = False
  
  def onMouseMove(self, event):
    if self.mouse_down:
      self.canvas.delete('all')
      x, y = event.x, event.y
      self.dot_loc = (x, y)
      self.canvas.create_image(0, 0, anchor=tk.NW, image=self.image)
      self.drawDot()
      self.moved = True
  
  def onMouseDown(self, event):
    if self.show_dot:
      self.mouse_down = True
      self.onMouseMove(event)
    
  def onMouseUp(self, event):
    self.mouse_down = False
    
  def drawDot(self):
    self.poly_roundrect(self.dot_loc[0] - self.dot_size//2, self.dot_loc[1] - self.dot_size//2, self.dot_size, self.dot_size, self.dot_size*2, 64)
    # self.canvas.create_oval(self.dot_loc[0] - self.dot_size, self.dot_loc[1] - self.dot_size, self.dot_loc[0] + self.dot_size, self.dot_loc[1] + self.dot_size, fill="RoyalBlue3", outline="")
    
  def poly_roundrect(self, x, y, width, height, radius, resolution=32):

    radius = min(min(width, height), radius*2)
    points = [x, y,
              x+radius, y,
              x+(width-radius), y,
              x+width, y,
              x+width, y+radius,
              x+width, y+(height-radius),
              x+width, y+height,
              x+(width-radius), y+height,
              x+radius, y+height,
              x, y+height,
              x, y+(height-radius),
              x, y+radius,
              x, y]
    
    rect = self.canvas.create_polygon(points, fill='SeaGreen2', smooth=True, splinesteps=resolution) 

              
    return rect