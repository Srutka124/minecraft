class Hero():
    def __init__(self,pos,land):
        self.land = land
        self.hero = loader.loadModel('smiley')
        self.hero.setColor(1, 0.5, 0)
        self.hero.setScale(0.3)
        self.hero.setPos(pos)
        self.hero.reparentTo(render)
        self.mode = True
        self.cameraBind()
        self.accept_events()

    def cameraBind(self):
        base.camera.reparentTo(self.hero)
        base.camera.setPos(0, 0, 1)
        base.disableMouse()
        base.camera.setH(180)
        self.cameraOn = True

    def cameraUp(self):
        base.camera.reparentTo(render)
        base.enableMouse()
        base.mouseInterfaceNode.setPos(self.hero.getPos())
        self.cameraOn = False

    def turn_left(self):
        self.hero.setH((self.hero.getH()+5)%360)

    def turn_right(self):
        self.hero.setH((self.hero.getH()-5)%360)
    def checkdir(self, angle):
        if angle >= 0 and angle <= 20:
            return (0, -1)
        elif angle <= 65:
            return (-1, -1)
        elif angle <= 110:
            return (1, 0)
        elif angle <= 155:
            return (1, 1)
        elif angle <= 200:
            return (0, 1)
        elif angle <= 245:
            return (-1, 1)
        elif angle <= 290:
            return (-1, 0)
        elif angle <= 335:
            return (1, 1)
        else:
            return(0,-1)
    def look_at(self,angle):
        x = round(self.hero.getX())
        y = round(self.hero.getY())
        z = round(self.hero.getZ())

        dx, dy = self.checkdir(angle)

        return x+dx, y+dy, z
    
    def Just_move(self,angle):

        pos = self.look_at(angle)
        self.hero.setPos(pos)

    def try_move(self,ange):
        pos = self.look_at(angle)
        if self.map.isEmpy(pos):
            pos = self.land.findHightestEmpty(pos)
            self.hero.setPos(pos)
        else:
            pos  = pos[0] ,pos[1] , pos[2] + 1 
            if  self.map.isEmpty(pos):
                self.hero.setPos(pos)

    def move_to(self,angel):
        if self.mode  == True:
            self.Just_move(angel)
        else:
            self.try_move(angel)
        
    def forward(self):
        angle = self.hero.getH() % 360
        pos = self.look_at(angle)
        self.hero.setPos(pos)
    def back (self):
        angle = (self.hero.getH()+180)  %360
        self.move_to(angle)
    def left (self):
        angle = (self.hero.getH()+90)   %360
        self.move_to(angle)
    def right(self):
        angle = (self.hero.getH()+90)   %360
        self.move_to(angle)
    def up(self):
        
        self.hero.setZ(self.heroZ()+1)
    def down(self):
        if self.hero.getZ() > 1 and self.mode:
            self.hero.setZ(self.heroZ()+1)

    def changeMode(self):
        self.mode = not self.mode
    def accept_events(self):
        base.accept('n', self.turn_left)
        base.accept('n-repeat', self.turn_left)
        base.accept('m', self.turn_right)
        base.accept('m-repeat', self.turn_right)
        base.accept('w', self.forward)
        base.accept('w-repeat', self.forward)
        base.accept('s', self.back)
        base.accept('s-repeat', self.back)
        base.accept('a', self.left)
        base.accept('a-repeat', self.left)
        base.accept('d', self.right)
        base.accept('d-repeat', self.right)
        base.accept('e', self.up)
        base.accept('e-repeat', self.up)
        base.accept('q', self.down)
        base.accept('q-repeat', self.down)
        base.accept('z', self.down)
        base.accept('z-repeat', self.down)
