__all__ = ["Clock"]

def get_ticks():
    return pygame.time.get_ticks()

def wait(milliseconds):
    pygame.time.wait(milliseconds)

def delay(milliseconds):
    pygame.time.delay(milliseconds)

def set_timer(eventid, milliseconds):
    pygame.time.set_timer(eventid, milliseconds)
