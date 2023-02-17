Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import turtle
tao = turtle.Pen()
tao.shape('turtle')
tao.forwaerd(100)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    tao.forwaerd(100)
AttributeError: 'Turtle' object has no attribute 'forwaerd'. Did you mean: 'forward'?
tao.forward(100)
tao.left(90)
tao.right(180)
tao.backward(200)
tao.right(90)
taoforawrd(100)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    taoforawrd(100)
NameError: name 'taoforawrd' is not defined
tao.forawrd(100)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    tao.forawrd(100)
AttributeError: 'Turtle' object has no attribute 'forawrd'. Did you mean: 'forward'?
tao.forward(100)
tao.left(90)
tao.forawrd(200)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    tao.forawrd(200)
AttributeError: 'Turtle' object has no attribute 'forawrd'. Did you mean: 'forward'?
tao.forward(200)
tao.clear()
for i in range(4):
    tao.forward(100)
    tao.left(90)

    
tao.penup()
tao.goto(200,200)
tao.goto(-200,-200)
tao.goto(200,200)
tao.pendown()
for i in range(4):
    tao.forward(100)
    tao.left(90)

    
tao.clear()
tao.clear()
tao.left(90)
tao.backword(200)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    tao.backword(200)
AttributeError: 'Turtle' object has no attribute 'backword'. Did you mean: 'backward'?
tao.backward(200)
tao.clear()
tao.right(90)
tao.forward(200)
tao.clear()
tao.left(90)
for i in range(4) :
    tao.forard(20)
    tao.left(90)
    tao.goto(40,0)
    for j in range(4) :
        tao.forward(20)
        tao.left(90)

        
Traceback (most recent call last):
  File "<pyshell#44>", line 2, in <module>
    tao.forard(20)
AttributeError: 'Turtle' object has no attribute 'forard'. Did you mean: 'forward'?
for i in range(4) :
    tao.forward(20)
    tao.left(90)
    tao.goto(40,0)
    for j in range(4) :
        tao.forward(20)
        tao.left(90)

        
for i in range(4) :
    tao.forward(20)
    tao.left(90)
    tao.goto(40,0)
    for j in range(4) :
        tao.forward(20)
        tao.left(90)

        
for i in range(4) :
    tao.forward(20)
    tao.left(90)
    tao.goto(40,0)
    for j in range(4) :
        tao.forward(40)
        tao.left(90)

        
tao.clear(
    )

tao.clear()
for i in range(4) :
    tao.forward(20)
    tao.left(90)
    tao.goto(40,0)
    for j in range(4) :
        tao.forward(40)
        tao.left(90)

        
for i in range(4) :
    tao.forward(20)
    tao.left(90)
    tao.goto(40,0)
    for j in range(4) :
        tao.forward(80)
        tao.left(90)

        
tao.clear()
tao.circle()
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    tao.circle()
TypeError: TNavigator.circle() missing 1 required positional argument: 'radius'
tao.circle
<bound method TNavigator.circle of <turtle.Turtle object at 0x000002047DF7FD50>>
tao.circle(20)
tao.goto(50,0)
tao.goto(50,0)

tao.circle(20)
tao.goto(100,0)
tao.circle(20)
tao.goto(150,0)
tao.circle(20)
tao.clear()
tao.goto(0,0)
tao.clear()
fir i in range(4)
SyntaxError: invalid syntax
for i in range(4):
    tao.circle(20)
    tao.goto(0,100)

    
tao.clear()
tao.goto(0,0)
tao.clear()for i in range(4):
    tao.circle(20)
    tao.goto(0,100)
    
SyntaxError: invalid syntax

tao.clear()
for i in range(4):
    tao.circle(20)
    tao.goto(0,100)
    for j in range(4) :
        tao.down(20)
        tao.circle(40)

        
Traceback (most recent call last):
  File "<pyshell#90>", line 5, in <module>
    tao.down(20)
TypeError: TPen.pendown() takes 1 positional argument but 2 were given

tao.clear()
for i in range(4):
    tao.circle(20)
    tao.penup()
    tao.down(20)
    for j in range(4) :
        tao.pendown()
        tao.down(20)
        tao.circle(40)

        
Traceback (most recent call last):
  File "<pyshell#93>", line 4, in <module>
    tao.down(20)
TypeError: TPen.pendown() takes 1 positional argument but 2 were given
for i in range(4):
    tao.circle(20)
    tao.penup()
    tao.forward(20)
    for j in range(4) :
        tao.pendown()
        tao.forward(20)
        tao.circle(40)

        
tao.clear()
tao.goto(0,0)
tao.clear()
for i in range(4):
    tao.penup()
    tao.forward(20)
    for j in range(4) :
        tao.pendown()
        tao.forward(20)
        tao.circle(40+i*j)

        
tao.clear()
tao.penup(), tao.goto(0,0)
(None, None)
for i in range(4):
    tao.pendown()
    tao.clrcle(5*i)
    tao.penup()
    tao.goto(0,0)

    
Traceback (most recent call last):
  File "<pyshell#104>", line 3, in <module>
    tao.clrcle(5*i)
AttributeError: 'Turtle' object has no attribute 'clrcle'. Did you mean: 'circle'?
for i in range(4):
    tao.pendown()
    tao.clrcle(5 * i)
    tao.penup()
    tao.goto(0,0)

    
Traceback (most recent call last):
  File "<pyshell#106>", line 3, in <module>
    tao.clrcle(5 * i)
AttributeError: 'Turtle' object has no attribute 'clrcle'. Did you mean: 'circle'?
for i in range(4):
    tao.pendown()
    tao.circle(5 * i)
    tao.penup()
    tao.goto(0,0)

    

for i in range(4):
    tao.pendown()
    tao.circle(10 * i)
    tao.penup()
    tao.goto(0,0)

    
tao.clear()
tao.goto(0,0)
for i in range(5):
    tao.pendown()
    tao.circle(10 * i)
    tao.penup()
    tao.goto(i,0)

    
for i in range(5):
    tao.pendown()
    tao.circle(10 * i)
    tao.penup()
    tao.goto(i*i,0)

    
tao.clear()
tao.goto(0,0)
for i in range(5):
    tao.pendown()
    tao.circle(10 * i)
    tao.penup()
    tao.goto(i*i,i*i)

    
tao.clear()
tao.goto(0,0)
for i in range(5):
    for i in range (4):
    tao.pendown()
    tao.circle(10 * i * j)
    tao.penup()
    tao.goto(i*j,0)
    
SyntaxError: expected an indented block after 'for' statement on line 2

for i in range(5):
    for i in range (4):
        tao.pendown()
        tao.circle(10 * i * j)
        tao.penup()
        tao.goto(i*j,0)

        
for i in range(3):
    for i in range (4):
        tao.pendown()
        tao.circle(10 * i * j)
        tao.penup()
        tao.goto(i*j,0)

        
for i in range(3):
    tao.goto(5*i*j, 5* i * j)
        for i in range (4):
        tao.pendown()
        tao.circle(10 * i * j)
        tao.penup()
        tao.goto(i*j,0)
        
SyntaxError: unexpected indent

tao.clear()
for i in range(3):
    tao.goto(5*i*j, 5* i * j)
        for i in range (4):
            tao.pendown()
            tao.circle(10 * i * j)
            tao.penup()
            tao.goto(i*j,0)
            
SyntaxError: unexpected indent
for i in range(3):
    tao.goto(5*i*j, 5*i*j)
        for i in range (4):
            tao.pendown()
            tao.circle(10*i*j)
            tao.penup()
            tao.goto(i*j,0)
            
SyntaxError: unexpected indent

for i in range(3):
       for i in range (4):
            tao.pendown()
            tao.circle(10*i*j)
            tao.penup()
            tao.goto(i*j,0)

            
for i in range(3):
    tao.penup()
    tao.forward(20)
       for i in range (4):
            tao.pendown()
            tao.circle(10*i*j)
            tao.penup()
            tao.goto(i*j,0)
            
SyntaxError: unexpected indent
for i in range(3):
    tao.penup()
    tao.forward(20)
    for i in range (4):
            tao.pendown()
            tao.circle(10*i*j)
            tao.penup()
            tao.goto(i*j,0)

            
for i in range(3):
    tao.penup()
    tao.forward(50)
    for i in range (4):
            tao.pendown()
            tao.circle(10*i*j)
            tao.penup()

            
tao.clear()
tao.goto(0,0)
for i in range(3):
    tao.penup()
    tao.forward(50)
    tao.color(5*i)
        for i in range (4):
            tao.pendown()
            tao.circle(10*i*j)



            
            tao.penup()tao.goto(0,0)
            
SyntaxError: unexpected indent
for i in range(3):
    tao.penup()
    tao.forward(50)
    tao.color(5*i)
        for i in range (4):
            tao.pendown()
            tao.circle(10*i*j)
            
SyntaxError: unexpected indent
tao.color
<bound method TPen.color of <turtle.Turtle object at 0x000002047DF7FD50>>
tao.color(yellow)
Traceback (most recent call last):
  File "<pyshell#147>", line 1, in <module>
    tao.color(yellow)
NameError: name 'yellow' is not defined
tao.clear()
color
Traceback (most recent call last):
  File "<pyshell#149>", line 1, in <module>
    color
NameError: name 'color' is not defined
help color
SyntaxError: incomplete input
tao.pencolor(red)
Traceback (most recent call last):
  File "<pyshell#151>", line 1, in <module>
    tao.pencolor(red)
NameError: name 'red' is not defined
tao.color(red)
Traceback (most recent call last):
  File "<pyshell#152>", line 1, in <module>
    tao.color(red)
NameError: name 'red' is not defined
tao.color()
('black', 'black')
tao.color('blie')
Traceback (most recent call last):
  File "<pyshell#154>", line 1, in <module>
    tao.color('blie')
  File "C:\Python311\Lib\turtle.py", line 2217, in color
    pcolor = self._colorstr(pcolor)
  File "C:\Python311\Lib\turtle.py", line 2697, in _colorstr
    return self.screen._colorstr(args)
  File "C:\Python311\Lib\turtle.py", line 1159, in _colorstr
    raise TurtleGraphicsError("bad color string: %s" % str(color))
turtle.TurtleGraphicsError: bad color string: blie
tao.color('blue')
for i in range(3):
    tao.penup()
    tao.forward(50)
    tao.color(blue)
        for i in range (4):
            tao.pendown()
            tao.circle(10*i*j)
            
SyntaxError: unexpected indent

for i in range(3):
    tao.penup()
    tao.forward(50)
    tao.color('blue')
        for i in range (4):
            tao.pendown()
            tao.circle(10*i*j)
            
SyntaxError: unexpected indent
for i in range(3):
    tao.penup()
    tao.forward(50)
        for i in range (4):
            tao.pendown()
            tao.circle(10*i*j)
            
SyntaxError: unexpected indent

for i in range (3):
    tao.penup()
    tao.forward(50*i)
    for j in range(4):
        tao.pendown()
        tao.circle(10*i*j)

        

tao.clear()
tao.goto(0,0)
tao.clear()
for i in range (3):
    tao.penup()
    tao.forward(50*i*j)
    for j in range(4):
        tao.pendown()
        tao.circle(10*i*j)

        
tao.goto(0,0)
tao.clear()
for i in range (3):
    tao.penup()
    tao.forward(20*i)
    for j in range(4):
        tao.pendown()
        tao.circle(15*i*j)

        

for i in range (3):
    tao.forward(20*i)
    for j in range(4):
        tao.pendown()
        tao.circle(10*i*j)
        tao.forward(5*i*j)

        
tao.goto(0,0)tao.clear()
SyntaxError: invalid syntax
tao.clear()
tao.goto(0,0)
tao.clear()
for i in range (3):
    tao.forward(20*i)
     tao.circle(10*i*j)
    for j in range(4):
        tao.pendown()
        tao.forward(5*i*j)
        tao.left(90)
        
SyntaxError: unexpected indent

for i in range (3):
    tao.forward(20*i)
    tao.circle(10*i*j)
    for j in range(4):
        tao.pendown()
        tao.forward(5*i*j)
        tao.left(90)

        
for i in range (3):
    tao.circle(10*i*j)
    for j in range(4):
        tao.pendown()
        tao.forward(5*i*j)
        tao.left(90)

        

tao.goto(0,0)
tao.clear()
for i in range (4):
    tao.circle(10*i*j)
    for j in range(4):
        tao.pendown()
        tao.forward(5*i*j)
        tao.left(90)

        
tao.goto(0,0)
tao.clear()
tao.goto(0,0)
for i in range (4):
    tao.circle(10*i*j)
    for j in range(4):
        tao.penup()
        tao.forward(5*i*j)
        tao.left(90)

        
tao.goto(0,0)
for i in range (4):
    tao.pendown()
    tao.circle(10*i*j)
    for j in range(4):
        tao.penup()
        tao.forward(5*i*j)
        tao.left(90)

        
tao.goto(0,0)
tao.clear()
for i in range (4):
    tao.pendown()
    tao.circle(10*i*j)
    for j in range(4):
        tao.penup()
        tao.forward(10*i*j)

        

tao.goto(0,0),tao.clear()
(None, None)
for i in range (4):
    tao.pendown()
    tao.circle(10*i*j)
    tao.penup()
    tao.goto(10*i*j,0)

    
tao.goto(0,0),tao.clear()
(None, None)
for i in range (4):
    tao.pendown()
    tao.circle(10*i*j)
    tao.penup()
    tao.goto(0, 10*i)

    
tao.goto(0,0),tao.clear()
(None, None)
for i in range (8):
    tao.pendown()
    tao.circle(10*i*j)
    tao.penup()
    tao.goto(0, -10*i)

    
tao.goto(0,0),tao.clear()
(None, None)
for i in range (8):
    tao.pendown()
    tao.circle(5*i)
    tao.penup()
    tao.goto(0, -10*i)

    
tao.goto(0,0),tao.clear()
(None, None)
for i in range (20):
    tao.pendown()
    tao.circle(5*i)
    tao.penup()
    tao.goto(0, -10*i)

    
for i in range (20):
    tao.pendown()
    tao.circle(5*i)
    tao.penup()
    tao.goto(0, 10*i)

    
tao.goto(0,0),tao.clear()
(None, None)
for i in range (15):
    tao.pendown()
    tao.circle(5*i)
    tao.penup()
    tao.goto(i, 10*i)

    
for i in range (15):
    tao.pendown()
    tao.circle(5*i)
    tao.penup()
    tao.goto(-i, -10*i)

    
tao.goto(0,0),tao.clear()
(None, None)
for i in range (5):
    tao.pendown()
    tao.circle(5*i)
    tao.penup()
    tao.goto(-i, i*i)

    
tao.goto(0,0),tao.clear()
(None, None)
for i in range (15):
    tao.pendown()
    tao.circle(5*i)
    tao.penup()
    tao.goto(-i, i*i)

    
tao.goto(0,0),tao.clear()
(None, None)
for i in range (5):
    tao.pendown()
    tao.circle(i*i)
    tao.penup()
    tao.goto(0, i*i)

    
tao.goto(0,0),tao.clear()
(None, None)
for i in range (10):
    tao.pendown()
    tao.circle(i*i)
    tao.penup()
    tao.goto(0, -i*i)

    
for i in range (5):
    tao.pendown()
    tao.forward(2*i*i)
    tao.left(90)

    
for i in range (5):
    for j in range(4)
        tao.pendown()
        tao.forward(2*i*i)
        
SyntaxError: expected ':'
for i in range (5):
    for j in range(4):
        tao.pendown()
        tao.forward(2*i*i)

        

tao.goto(0,0),tao.clear()
(None, None)
for i in range (5):
    for j in range(4):
       tao.forward(2*i*i)
       tao.left(90)

       

tao.goto(0,0),tao.clear()
(None, None)
for i in range (10):
    for j in range(4):
       tao.forward(2*i*i)
       tao.left(90)

       
for i in range (10):
    for j in range(4):
       tao.forward(2*i*i)
       tao.left(90)
for k in range (10):
    for l in range(4):
       tao.forward(2*k*l)
       tao.right(90)
       
SyntaxError: invalid syntax

tao.goto(0,0),tao.clear()
(None, None)
for i in range (10):
    for j in range(4):
       tao.forward(2*i*i)
       tao.left(90)
       
for k in range (10):
    for l in range(4):
       tao.forward(2*k*l)
       tao.right(90)
       
SyntaxError: invalid syntax
for i in range (5):
    for j in range(4):
       tao.forward(2*i*i)
       tao.left(90)
        for k in range (4):
          tao.forward(2*k*j)
          tao.right(90)
          
SyntaxError: unexpected indent
for i in range (5):
    for j in range(4):
        tao.forward(2*i*i)
        tao.left(90)
            for k in range (4):
              tao.forward(2*k*j)
              tao.right(90)
              
SyntaxError: unexpected indent

for i in range (5):
    for j in range(4):
        tao.forward(2*i*i)
        tao.left(90)

        
tao.goto(0,0),tao.clear()
(None, None)
for i in range (10):
    for j in range(4):
        tao.forward(2*i*i)
        tao.left(90)

        
for i in range (10):
    for j in range(4):
        tao.forward(2*i*i)
        tao.right(90)

        
for i in range (10):
    for j in range(4):
        tao.downward(2*i*i)
        tao.right(90)

        
Traceback (most recent call last):
  File "<pyshell#273>", line 3, in <module>
    tao.downward(2*i*i)
AttributeError: 'Turtle' object has no attribute 'downward'. Did you mean: 'forward'?
for i in range (10):
    for j in range(4):
        tao.backward(2*i*i)
        tao.right(90)

        
for i in range (10):
    for j in range(4):
        tao.backward(2*i*i)
        tao.left(90)

        

tao.goto(0,0),tao.clear()
(None, None)
for i in range (10):
    for j in range(4):
        tao.forward(2*i*i)
        tao.left(90)
        for i in range (10):
            for j in range(4):
                tao.forward(2*i*i)
                tao.right(90)

                
Traceback (most recent call last):
  File "<pyshell#281>", line 7, in <module>
    tao.forward(2*i*i)
  File "C:\Python311\Lib\turtle.py", line 1638, in forward
    self._go(distance)
  File "C:\Python311\Lib\turtle.py", line 1606, in _go
    self._goto(ende)
  File "C:\Python311\Lib\turtle.py", line 3196, in _goto
    self._update()
  File "C:\Python311\Lib\turtle.py", line 2664, in _update
    screen._delay(screen._delayvalue) # TurtleScreenBase
  File "C:\Python311\Lib\turtle.py", line 566, in _delay
    self.cv.after(delay)
  File "C:\Python311\Lib\tkinter\__init__.py", line 856, in after
    self.tk.call('after', ms)
KeyboardInterrupt

tao.goto(0,0),tao.clear()
(None, None)
for i in range (4):
    for j in range(4):
        tao.forward(2*i*i)
        tao.left(90)
        for i in range (10):
            for j in range(4):
                tao.forward(2*i*i)
                tao.right(90)

                
Traceback (most recent call last):
  File "<pyshell#284>", line 8, in <module>
    tao.right(90)
  File "C:\Python311\Lib\turtle.py", line 1679, in right
    self._rotate(-angle)
  File "C:\Python311\Lib\turtle.py", line 3293, in _rotate
    self._update()
  File "C:\Python311\Lib\turtle.py", line 2664, in _update
    screen._delay(screen._delayvalue) # TurtleScreenBase
  File "C:\Python311\Lib\turtle.py", line 566, in _delay
    self.cv.after(delay)
  File "C:\Python311\Lib\tkinter\__init__.py", line 856, in after
    self.tk.call('after', ms)
KeyboardInterrupt
tao.goto(0,0),tao.clear()
(None, None)
for i in range (4):
    for j in range(4):
        tao.forward(2*i*i)
        tao.left(90)
        for i in range (4):
            for j in range(4):
                tao.forward(2*i*i)
                tao.right(90)

                
Traceback (most recent call last):
  File "<pyshell#287>", line 8, in <module>
    tao.right(90)
  File "C:\Python311\Lib\turtle.py", line 1679, in right
    self._rotate(-angle)
  File "C:\Python311\Lib\turtle.py", line 3293, in _rotate
    self._update()
  File "C:\Python311\Lib\turtle.py", line 2664, in _update
    screen._delay(screen._delayvalue) # TurtleScreenBase
  File "C:\Python311\Lib\turtle.py", line 566, in _delay
    self.cv.after(delay)
  File "C:\Python311\Lib\tkinter\__init__.py", line 856, in after
    self.tk.call('after', ms)
KeyboardInterrupt
tao.goto(0,0),tao.clear()
(None, None)
for i in range (4):
    tao.goto(0,0)
    for j in range(4):
        tao.forward(2*i*i)
        tao.left(90)
        for i in range (4):
            for j in range(4):
                tao.forward(2*i*i)
                tao.right(90)

                
Traceback (most recent call last):
  File "<pyshell#290>", line 9, in <module>
    tao.right(90)
  File "C:\Python311\Lib\turtle.py", line 1679, in right
    self._rotate(-angle)
  File "C:\Python311\Lib\turtle.py", line 3293, in _rotate
    self._update()
  File "C:\Python311\Lib\turtle.py", line 2664, in _update
    screen._delay(screen._delayvalue) # TurtleScreenBase
  File "C:\Python311\Lib\turtle.py", line 566, in _delay
    self.cv.after(delay)
  File "C:\Python311\Lib\tkinter\__init__.py", line 856, in after
    self.tk.call('after', ms)
KeyboardInterrupt
tao.goto(0,0),tao.clear()
(None, None)
for i in range (4):
    tao.goto(0,0)
    for j in range(4):
        tao.forward(2*i*j)
        tao.left(90)
        for i in range (4):
            for j in range(4):
                tao.forward(2*i*j)
                tao.right(90)

                
Traceback (most recent call last):
  File "<pyshell#293>", line 5, in <module>
    tao.left(90)
  File "C:\Python311\Lib\turtle.py", line 1700, in left
    self._rotate(angle)
  File "C:\Python311\Lib\turtle.py", line 3293, in _rotate
    self._update()
  File "C:\Python311\Lib\turtle.py", line 2664, in _update
    screen._delay(screen._delayvalue) # TurtleScreenBase
  File "C:\Python311\Lib\turtle.py", line 566, in _delay
    self.cv.after(delay)
  File "C:\Python311\Lib\tkinter\__init__.py", line 856, in after
    self.tk.call('after', ms)
KeyboardInterrupt
tao.goto(0,0),tao.clear()
(None, None)
for i in range (4):
    tao.goto(0,0)
    for j in range(4):
        tao.forward(i*i*j)
        tao.left(90)
        for i in range (4):
            for j in range(4):
                tao.forward(i*i*j)
                tao.right(90)

                
Traceback (most recent call last):
  File "<pyshell#296>", line 9, in <module>
    tao.right(90)
  File "C:\Python311\Lib\turtle.py", line 1679, in right
    self._rotate(-angle)
  File "C:\Python311\Lib\turtle.py", line 3295, in _rotate
    self._update()
  File "C:\Python311\Lib\turtle.py", line 2664, in _update
    screen._delay(screen._delayvalue) # TurtleScreenBase
  File "C:\Python311\Lib\turtle.py", line 566, in _delay
    self.cv.after(delay)
  File "C:\Python311\Lib\tkinter\__init__.py", line 856, in after
    self.tk.call('after', ms)
KeyboardInterrupt
tao.goto(0,0),tao.clear()
(None, None)
for i in range (4):
    tao.goto(0,i*j)
    for j in range(4):
        tao.forward(10*i*j)
        tao.left(90)
        for i in range (4):
            for j in range(4):
                tao.forward(10*i*j)
                tao.right(90)

                
tao.goto(0,0),tao.clear()
(None, None)
for i in range (4):
    tao.goto(0,i*j)
    for j in range(4):
        tao.forward(10*i*j)
        tao.left(90)

        
tao.goto(0,0),tao.clear()
(None, None)
tao.left(90)
tao.left(45)
tao.right(90)
tao.right(10)
tao.goto(0,0),tao.clear()
(None, None)
for i in range (4):
      for j in range(4):
        tao.forward(10*i*j)
        tao.left(90)
        for i in range (4):
            for j in range(4):
                tao.forward(10*i*j)
                tao.right(90)

                
tao.goto(0,0),tao.clear()
(None, None)
for i in ragnge(4):
    tao.forward(50*i)
    tao.left(90)
    for j in range(4):
        tao.forward(50*i*j)
        tao.left(90)

        
Traceback (most recent call last):
  File "<pyshell#319>", line 1, in <module>
    for i in ragnge(4):
NameError: name 'ragnge' is not defined. Did you mean: 'range'?
for i in range(4):
    tao.forward(50*i)
    tao.left(90)
    for j in range(4):
        tao.forward(50*i*j)
        tao.left(90)

        
KeyboardInterrupt
tao.goto(0,0),tao.clear()
(None, None)
for i in range(4):
     for j in range(4):
        tao.forward(5*i*j)
        tao.left(90)

        
for i in range(4):
        tao.forward(200)     tao.left(90)
        
SyntaxError: invalid syntax
for i in range(4):
        tao.forward(200)
        tao.left(90)

        
tao.goto(0,0),tao.clear()
(None, None)
for i in range(4):
        tao.forward(200)
        tao.left(90)

        
tao.goto(0,0),tao.clear()
(None, None)
tao.goto(0,0),tao.clear(),for i in range(4):
        tao.forward(200)
        tao.left(90)
        
SyntaxError: invalid syntax
tao.goto(0,0),tao.clear()
for i in range(4):
        tao.forward(200)
        tao.left(90)
        
SyntaxError: multiple statements found while compiling a single statement
tao.goto(0,0),tao.clear()
(None, None)
import turtle()
SyntaxError: invalid syntax
SyntaxError: invalid syntax
SyntaxError: incomplete input
import turtle
tao = turtle.Pen()
tao.shape('turtle')
SyntaxError: multiple statements found while compiling a single statement
import turtle

import turtle
tao = turtle.Pen()
tao.shape('turtle')
SyntaxError: multiple statements found while compiling a single statement
tao = turtle.Pen()
Traceback (most recent call last):
  File "<pyshell#342>", line 1, in <module>
    tao = turtle.Pen()
  File "C:\Python311\Lib\turtle.py", line 3831, in __init__
    RawTurtle.__init__(self, Turtle._screen,
  File "C:\Python311\Lib\turtle.py", line 2558, in __init__
    self._update()
  File "C:\Python311\Lib\turtle.py", line 2661, in _update
    self._update_data()
  File "C:\Python311\Lib\turtle.py", line 2647, in _update_data
    self.screen._incrementudc()
  File "C:\Python311\Lib\turtle.py", line 1293, in _incrementudc
    raise Terminator
turtle.Terminator
tao.shape('turtle')
Traceback (most recent call last):
  File "<pyshell#343>", line 1, in <module>
    tao.shape('turtle')
  File "C:\Python311\Lib\turtle.py", line 2779, in shape
    self._update()
  File "C:\Python311\Lib\turtle.py", line 2662, in _update
    self._drawturtle()
  File "C:\Python311\Lib\turtle.py", line 3027, in _drawturtle
    screen._drawpoly(titem, shape, fill=fc, outline=oc,
  File "C:\Python311\Lib\turtle.py", line 514, in _drawpoly
    self.cv.coords(polyitem, *cl)
  File "<string>", line 1, in coords
  File "C:\Python311\Lib\tkinter\__init__.py", line 2822, in coords
    self.tk.call((self._w, 'coords') + args))]
_tkinter.TclError: invalid command name ".!canvas"

tao.shape('turtle')
Traceback (most recent call last):
  File "<pyshell#345>", line 1, in <module>
    tao.shape('turtle')
  File "C:\Python311\Lib\turtle.py", line 2779, in shape
    self._update()
  File "C:\Python311\Lib\turtle.py", line 2662, in _update
    self._drawturtle()
  File "C:\Python311\Lib\turtle.py", line 3027, in _drawturtle
    screen._drawpoly(titem, shape, fill=fc, outline=oc,
  File "C:\Python311\Lib\turtle.py", line 514, in _drawpoly
    self.cv.coords(polyitem, *cl)
  File "<string>", line 1, in coords
  File "C:\Python311\Lib\tkinter\__init__.py", line 2822, in coords
    self.tk.call((self._w, 'coords') + args))]
_tkinter.TclError: invalid command name ".!canvas"
import turtle
tao = turtle.Pen()
tao.shape('turtle')
for i in range (4):
    tao.forward(50)
    tao.left(90)

    
for i in range (4):
    tao.forward(50)
    for j in range (4)
        tao.forward(50)
        tao.left(90)
        
SyntaxError: expected ':'
tao.goto(0,0),tao.clear()
(None, None)
for i in range (4):
    tao.forward(50)
    for j in range (4):
        tao.forward(50)
        tao.left(90)

        
tao.goto(0,0),tao.clear()
(None, None)
for i in range (4):
    tao.forward(50)
    for j in range (4):
        tao.forward(50*i)
        tao.left(90)

        
tao.goto(0,0),tao.clear()
(None, None)
for i in range (4):
    tao.forward(10)
    for j in range (4):
        tao.forward(50*i)
        tao.left(90)

        
tao.goto(0,0),tao.clear()
(None, None)
for i in range (4):
    tao.goto(0,0)
    for j in range (4):
        tao.forward(50*i)
        tao.left(90)

        
tao.goto(0,0),tao.clear()
(None, None)
for i in range (1):
    tao.goto(0,0)
    for j in range (4):
...         tao.forward(20*i)
...         tao.left(90)
... 
...         
>>> for i in range (10):
...     tao.goto(0,0)
...     for j in range (4):
...         tao.forward(20*i)
...         tao.left(90)
... 
...         
>>> tao.goto(0,0),tao.clear()
(None, None)
>>> for i in range (15):
...     tao.goto(0,0)
...     for j in range (4):
...         tao.forward(15*i)
...         tao.left(90)
... 
...         
>>> for i in range (15):
...     tao.goto(0,0)
...     print(i)
...     for j in range (4):
...         tao.forward(15*i)
...         tao.left(90)
... 
...         
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
tao.goto(0,0),tao.clear()
(None, None)
for i in range (10):
    tao.goto(0,0)
    print(i)
    for j in range (4):
        tao.forward(15*i)
        tao.left(90)

        
0
1
2
3
4
5
6
7
8
9
for i in range (10):
    tao.goto(0,0)
    print(i)
    for j in range (4):
        tao.forward(15*i)
        tao.right(90)

        
0
1
2
3
4
5
6
7
8
9
for i in range (10):
    tao.goto(0,0)
    print(i)
    for j in range (4):
        tao.backward(15*i)
        tao.right(90)

        
0
1
2
3
4
5
6
7
8
9
for i in range (10):
    tao.goto(0,0)
    print(i)
    for j in range (4):
        tao.backward(15*i)
        tao.left(90)

        
0
1
2
3
4
5
6
7
8
9
