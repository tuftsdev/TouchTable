import pytuio, pygame, sys

# Set hold time to variable and think about system calls
# add comments!

def iround(x):
  y = round(x) - .5
  return int(y) + (y > 0)


class Touch(object):
    def __init__(self, xpos, ypos, origin, sessionid):
        self.xpos = xpos
        self.ypos = ypos
        self.origin = origin
        self.sessionid = sessionid
        self.status = "clicked"
        self.time_held = 0
        self.clickEventFired = False

    def __str__(self):
        return "xpos: " + str(self.xpos) + ", ypos: " + str(self.ypos) + ", origin: " + self.origin + ", sessionid: " + str(self.sessionid) + ", status: " + self.status + ", time: " + str(self.time_held)

class TouchTracker(object):
    def __init__(self, window_width, window_height):
        self.tuioTracker = pytuio.Tracking()
        self.curSessionId = 0
        self.window_width = window_width
        self.window_height = window_height
        self.mouseSessionTracker = 0
        self.curClick = None


    def update(self):
        self.tuioTracker.update()
        for obj in self.tuioTracker.cursors():
            if obj.sessionid != self.curSessionId:
                self.curSessionId = obj.sessionid
                x = iround(obj.xpos * self.window_width)
                y = iround(obj.ypos * self.window_height)
                self.curClick = Touch(x,y, "Tuio", obj.sessionid)
                return self.curClick
            else:
                if self.curClick.xpos != iround(obj.xpos * self.window_width) or self.curClick.ypos != iround(obj.ypos * self.window_height):
                    self.curClick.xpos = iround(obj.xpos * self.window_width)
                    self.curClick.ypos = iround(obj.ypos * self.window_height)
                    self.curClick.time_held = 0
                    self.curClick.status = "dragging"
                else:
                    self.curClick.time_held += 1
                    if self.curClick.time_held == 20:
                        self.curClick.status = "holding"
                    elif self.curClick.time_held > 20:
                        self.curClick.status = "held"
                return self.curClick
        b = pygame.mouse.get_pressed()
        event = pygame.event.poll()
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            self.mouseSessionTracker -= 1
            self.curClick = Touch(event.pos[0], event.pos[1], "Mouse", self.mouseSessionTracker)
            return self.curClick
        elif b[0] == 1 and self.curClick is not None: # Mouse is held down
            x,y = pygame.mouse.get_pos()
            if self.curClick.xpos != x or self.curClick.ypos != y:
                self.curClick.xpos = x
                self.curClick.ypos = y
                self.curClick.time_held = 0
                self.curClick.status = "dragging"
            else:
                self.curClick.time_held += 1
                if(self.curClick.time_held == 20):
                    self.curClick.status = "holding"
                elif self.curClick.time_held > 20:
                    self.curClick.status = "held"
            return self.curClick
        else:
            if self.curClick is not None:
                self.curClick.status = "released"
                retVal = self.curClick
                self.curClick = None
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
