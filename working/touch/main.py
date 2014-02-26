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
                print obj.mot_accel
    except KeyboardInterrupt:
        tracking.stop()