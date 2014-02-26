import pytuio, pygame







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
