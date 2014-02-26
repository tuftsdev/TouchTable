import pytuio, pygame, sys

class TouchTracker(object):
  def __init__(self):
    self.tuioTracker = pytuio.Tracking()
    self.curSessionId = 0

  def update(self):
    self.tuioTracker.update()
    for obj in self.tuioTracker.cursors():
      if obj.sessionid != self.curSessionId:
        self.curSessionId = obj.sessionid
        print "Tuio: ", obj.xpos, obj.ypos
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
    elif event.type == pygame.MOUSEBUTTONDOWN:
      print "Mouse: ", event.pos

# Testing Framework
if __name__ == '__main__':
    tracking = pytuio.Tracking()
    print "loaded profiles:", tracking.profiles.keys()
    print "list functions to access tracked objects:", tracking.get_helpers()
    try:
        while 1:
            
            tracking.update()
            for obj in tracking.cursors():
                print 'Sesh: ', obj.sessionid, ' X: ', obj.xpos, ' Y: ', obj.ypos
    except KeyboardInterrupt:
        tracking.stop()
