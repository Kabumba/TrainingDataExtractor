class Interpolator:
    def __init__(self, targetFramerate):
        self.targetFramerate = targetFramerate
        self.controls = ["throttle", "steer", "pitch", "yaw", "roll", "jump", "handbrake"]

    def interpolate(self, startingFrame : dict, endFrame : dict) -> list:
        return []

class Constant(Interpolator):
    pass

def interpolateInputs(replayData : dict, targetFramerate : int, interpolator : Interpolator) -> dict:
    pass
