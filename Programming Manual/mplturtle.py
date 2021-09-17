import pylab as py

class Turtle(object):
    
    def __init__(self):
        self.reset()

    def reset(self,figsize=(10,10)):
        self.x=0
        self.y=0
        self.angle=0
        
        self.color='k'
        self.pensize=1

        self.facecolor='white'

        self.pen='down'
        self._reset=True   
        self.fig=None
        self.ax=None
        self.figsize=figsize
        self.data=[]
        self.texts=[]
        self.limits=[-100,100,-100,100]
        
    def clear(self):
        fig=py.figure(figsize=self.figsize)
        ax=fig.gca()

        self.fig=fig
        self.ax=ax
        ax.set_facecolor(self.facecolor)

        ax.clear()
        ax.axis('equal')
        ax.axis(self.limits)

        self.data=[]
        
    def forward(self,length):
        if self._reset:
            self.clear()
            self._reset=False

        fig=self.fig
        ax=self.ax
        
        
        dx=length*py.cos(py.radians(self.angle))
        dy=length*py.sin(py.radians(self.angle))
        
        if self.pen=='down':
            ax.plot([self.x,self.x+dx],[self.y,self.y+dy],
                         color=self.color,
                         linestyle='-',linewidth=self.pensize)
            self.data.append([
                [self.x,self.x+dx],[self.y,self.y+dy],self.color,self.angle,self.pensize,
            ])
        else:
            self.data.append([
                [self.x,self.x+dx],[self.y,self.y+dy],None,self.angle,self.pensize,
            ])
            
            
        self.x+=dx
        self.y+=dy
        
        self.adjust_axis()

    def adjust_axis(self):

        limits=self.ax.axis()
        if self.x<limits[0] or self.x>limits[1] or self.y<limits[2] or self.y>limits[3]:
            limits=[2*_ for _ in limits]
            self.ax.axis(limits)
            self.limits=limits

    def setx(self,x):
        self.goto(x,self.y)

    def sety(self,x):
        self.goto(self.x,y)

    def goto(self,x,y):
        if self._reset:
            self.clear()
            self._reset=False

        fig=self.fig
        ax=self.ax
        
        if self.pen=='down':
            ax.plot([self.x,x],[self.y,y],
                         color=self.color,
                         linestyle='-',linewidth=self.pensize)
            self.data.append([
                [self.x,x],[self.y,y],self.color,self.angle,self.pensize,
            ])
        else:
            self.data.append([
                [self.x,x],[self.y,y],None,self.angle,self.pensize,
            ])
            
            
        self.x=x
        self.y=y
        self.adjust_axis()
        
    def backward(self,length):
        self.forward(-self.length)
        
    def setheading(self,angle):
        self.angle=angle
        self.angle=self.angle % 360
        self.data.append([
            [self.x,self.x],[self.y,self.y],None,self.angle,self.pensize,
        ])

    def home(self):
        self.goto(0,0)
        self.setheading(0)

    def seth(self,angle):
        self.setheading(angle)

    def right(self,angle):
        self.angle-=angle
        self.angle=self.angle % 360
        self.data.append([
            [self.x,self.x],[self.y,self.y],None,self.angle,self.pensize,
        ])
        
    def left(self,angle):
        self.right(-angle)
        

    def circle(self,radius,extent=None,steps=50):
        R=radius
        n=steps

        b=(n-2)*180/n  # polygon interior angle
        a=180-b  # polygon exterior angle
        L=R*py.cos(py.radians(b/2))  # length of one side

        if not extent is None:  # partial circle
            n=n*extent//360

        for i in range(n):
            self.forward(L)

            if radius>0:
                self.left(a) 
            else:
                self.right(a) 

    def position(self):
        return self.x,self.y


_t=Turtle()


def done():
    pass

def write(txt,**kwargs):
    py.text(_t.x,_t.y,txt,**kwargs)
    _t.texts.append( (_t.x,_t.y,txt,kwargs) )

def bgcolor(color):
    _t.facecolor=color

def isdown():
    return _t.pen=='down'

def isup():
    return not _t.pen=='down'

def pos():
    return _t.position()

def position():
    return _t.position()

def xcor():
    return _t.x

def ycor():
    return _t.y

def heading():
    return _t.angle

def distance(x,y=None):
    if not y is None:
        return py.sqrt((y-_t.y)**2 + (x-_t.x)**2)
    else:
        return py.sqrt((x[1]-_t.y)**2 + (x[0]-_t.x)**2)

def pensize(size=None):
    if not size is None:
        _t.pensize=size
    return _t.pensize

def forward(length):
    global _t
    _t.forward(length)
    
def backward(length):
    forward(-length)
    
def right(angle):
    global _t
    _t.right(angle)
    
def left(angle):
    right(-angle)

def penup():
    global _t
    _t.pen='up'
    

def pendown():
    global _t
    _t.pen='down'    

up = penup
down = pendown




def pencolor(*args):
    global _t

    if len(args)==0:
        return _t.color
    if len(args)==1:
        color=args[0]
    else:
        color=args[:3]

    _t.color=color  
    return _t.color

def reset(*args,**kwargs):
    global _t
    _t.reset(*args,**kwargs)
    
def speed(arg):
    pass

def goto(x,y):
    global _t
    _t.goto(x,y)

def home():
    goto(0,0)

def sety(y):
    goto(_t.x,y)

def setx(x):
    goto(x,_t.y)

def circle(radius,extent=None,steps=50):
    _t.circle(radius,extent,steps)


def animate(delay=0.05,skip=1,figsize=(5,5)):

    # delay will be per 100 units

    global _t
    from IPython.display import clear_output
    import time

    i=0
    interrupt_count=0
    while True:

        try:

            clear_output(wait=True)
            fig=py.figure(figsize=_t.figsize)
            ax = fig.add_subplot(111)
            ax.clear()
            ax.set_facecolor(_t.facecolor)
            ax.axis('equal')
            ax.axis(_t.limits)
            
            for x,y,t,k in _t.texts:
                ax.text(x,y,t,**k)

            for x,y,c,a,ps in _t.data[:i]:
                if c is not None:
                    ax.plot(x,y,color=c,linestyle='-',linewidth=ps)
                
            x,y,c,a,ps = _t.data[i-1]            
            ax.plot([x[1]],[y[1]],'g',marker=(3, 0, a-90),markersize=20,)
            ax.plot([x[1]+2*py.cos(py.radians(a))],[y[1]+2*py.sin(py.radians(a))],'r.')
            py.show() 


            # each step is a delay

            time.sleep(delay)    
        
            if i==len(_t.data):
                break

            i+=skip
            if i>len(_t.data):  # make sure to plot the last one
                i=len(_t.data)

        except KeyboardInterrupt:
            interrupt_count+=1
            if interrupt_count==1:
                delay=0
            else:
                i=len(_t.data)
