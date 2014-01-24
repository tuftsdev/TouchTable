__all__ = ['MotionEventProvider']

class MotionEventProvider(object):

    def __init__(self, device, args):
        self.device = device
        if self.__class__ == MotionEventProvider:
            raise NotImplementedError('MotionEventProvider is an abstract class')

    def start(self):
        pass

    def stop(self):
        pass

    def update(self, dispatch):
        pass