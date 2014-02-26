import pytuio, pygame, sys

class Touch(object):
  def __init__(self, xpos, ypos, origin, sessionid):
    self.xpos = xpos
    self.ypos = ypos
    self.origin = origin
    self.sessionid = sessionid

class TouchTracker(object):
  def __init__(self, window_width, window_height):
    self.tuioTracker = pytuio.Tracking()
    self.curSessionId = 0
    self.window_width = window_width
    self.window_height = window_height
    self.mouseSessionTracker = 0

  def update(self):
    self.tuioTracker.update()
    for obj in self.tuioTracker.cursors():
      if obj.sessionid != self.curSessionId:
        self.curSessionId = obj.sessionid
        # print "Tuio: ", obj.xpos * self.window_width, obj.ypos * self.window_height
        return Touch(obj.xpos * self.window_width, obj.ypos * self.window_height, "Tuio", obj.sessionid)
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
    elif event.type == pygame.MOUSEBUTTONDOWN:
      # print "Mouse: ", event.pos
      self.mouseSessionTracker -= 1
      return Touch(event.pos[0], event.pos[1], "Mouse", self.mouseSessionTracker)

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
