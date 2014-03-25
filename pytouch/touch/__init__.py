import pytuio, pygame, sys

# Set hold time to variable and think about system calls
# add comments!


class Touch(object):
    def __init__(self, xpos, ypos, origin, sessionid):
        self.xpos = xpos
        self.ypos = ypos
        self.origin = origin
        self.sessionid = sessionid
        self.status = "clicked"
        self.time_held = 0

    def __str__(self):
        return "xpos: " + str(self.xpos) + ", ypos: " + str(self.ypos) + ", origin: " + self.origin + ", sessionid: " + str(self.sessionid) + ", status: " + self.status + ", time: " + str(self.time_held)

class TouchTracker(object):
    def __init__(self, window_width, window_height):
        self.tuioTracker = pytuio.Tracking()
        self.curSessionId = 0
        self.window_width = window_width
        self.window_height = window_height
        self.mouseSessionTracker = 0
        self.curMouseClick = None
        self.curTuioClick = None

    def update(self):
        self.tuioTracker.update()
        for obj in self.tuioTracker.cursors():
            if obj.sessionid != self.curSessionId:
                self.curSessionId = obj.sessionid
                self.curTuioClick = Touch(obj.xpos * self.window_width, obj.ypos * self.window_height, "Tuio", obj.sessionid)
                return self.curTuioClick
            else:
                if self.curTuioClick.xpos != obj.xpos or self.curTuioClick.ypos != obj.ypos:
                    self.curTuioClick.xpos = obj.xpos
                    self.curTuioClick.ypos = obj.ypos
                    self.curTuioClick.time_held = 0
                    self.curTuioClick.status = "dragging"
                else:
                    self.curTuioClick.time_held += 1
                    if self.curTuioClick.time_held == 20:
                        self.curTuioClick.status = "holding"
                    elif self.curTuioClick.time_held > 20:
                        self.curTuioClick.status = "held"
                return self.curTuioClick
        b = pygame.mouse.get_pressed()
        event = pygame.event.poll()
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            self.mouseSessionTracker -= 1
            self.curMouseClick = Touch(event.pos[0], event.pos[1], "Mouse", self.mouseSessionTracker)
            return self.curMouseClick
        elif b[0] == 1 and self.curMouseClick is not None: # Mouse is held down
            x,y = pygame.mouse.get_pos()
            if self.curMouseClick.xpos != x or self.curMouseClick.ypos != y:
                self.curMouseClick.xpos = x
                self.curMouseClick.ypos = y
                self.curMouseClick.time_held = 0
                self.curMouseClick.status = "dragging"
            else:
                self.curMouseClick.time_held += 1
                if(self.curMouseClick.time_held == 20):
                    self.curMouseClick.status = "holding"
                elif self.curMouseClick.time_held > 20:
                    self.curMouseClick.status = "held"
            return self.curMouseClick
        else:
            if self.curMouseClick is not None:
                self.curMouseClick.status = "released"
                retVal = self.curMouseClick
                self.curMouseClick = None
                return retVal

# testing framework
if __name__ == '__main__':
    tracking = pytuio.tracking()
    print "loaded profiles:", tracking.profiles.keys()
    print "list functions to access tracked objects:", tracking.get_helpers()
    try:
        while 1:
            tracking.update()
            for obj in tracking.cursors():
                print 'sesh: ', obj.sessionid, ' x: ', obj.xpos, ' y: ', obj.ypos
    except keyboardinterrupt:
        tracking.stop()
