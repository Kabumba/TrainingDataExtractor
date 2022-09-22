class Interpolator:
    def __init__(self, target_framerate: float):
        self.target_framerate = target_framerate  # in frames per second
        self.controls = ["boost", "throttle", "steer", "pitch", "yaw", "roll", "jump", "handbrake"]
        self.bool_controls = ["boost", "jump", "handbrake"]
        self.float_controls = ["throttle", "steer", "pitch", "yaw", "roll"]

    def interpolate(self, start_frame: dict, end_frame: dict) -> list:
        '''
        Interpolates inputs between start_frame and end_frame to match the target_framerate.
        Ideally, start_frame and end_frame are follow-up frames
        Default: Interpolates with no inputs
        :param start_frame: a frame structured as described in TODO: find final place for that method
        :param end_frame: a frame structured the same way as start_frame
        :return: list of frames to insert between start_frame and end_frame to interpolate between them
        '''
        times = self.missing_frame_times(start_frame["time"], end_frame["time"])
        interpolated_frames = []
        for i in len(times):
            frame = {"time": times[i], "players": []}
            for j in range(len(start_frame["players"])):
                player_data = {"index": start_frame["players"][j]["index"], "inputs": {}}
                for c in self.bool_controls:
                    player_data["inputs"][c] = False
                for c in self.float_controls:
                    player_data["inputs"][c] = 0
                frame["players"].append(player_data)
        return interpolated_frames

    def interpolate_all(self, input_frame_data: list) -> list:
        '''
        Takes structured input data and adds interpolated frames inbetween to raise the framerate to the target_framerate
        :param input_frame_data: frames structured as described in TODO: see above
        :return:
        '''
        interpolated_inputs = []
        for i in len(input_frame_data) - 1:
            interpolated_inputs.append(input_frame_data[i])
            interpolated_inputs.extend(self.interpolate(input_frame_data[i], input_frame_data[i + 1]))
        interpolated_inputs.append(input_frame_data[len(input_frame_data) - 1])
        return interpolated_inputs

    def missing_frame_times(self, start_time: float, end_time: float) -> list:
        '''
        Return the times of frames that need to be inserted between start_time and end_time to get the target_framerate
        :param start_time: time of the first frame
        :param end_time: time of the second frame
        :return:
        '''
        delta_time = end_time - start_time
        delta_frames = round(delta_time * self.target_framerate) - 1
        times = [start_time + (i + 1) / self.target_framerate for i in range(delta_frames)]
        return times


class ConstantSplit(Interpolator):
    def __init__(self, target_framerate, split_ratio):
        '''
        Interpolates between two frames by copying the start or the end frame depending on the split_ratio
        :param target_framerate:
        :param split_ratio: 1 means all start frame, 0 means all end frame, 0.5 means first half start frame, second half end frame
        '''
        super.__init__(target_framerate)
        self.split_ratio = split_ratio

    def interpolate(self, start_frame: dict, end_frame: dict) -> list:
        times = self.missing_frame_times(start_frame["time"], end_frame["time"])
        interpolated_frames = []
        constants = [start_frame, end_frame]
        use = 0
        delta_time = end_frame["time"] - start_frame["time"]
        for i in len(times):
            frame = {"time": times[i], "players": []}
            if times[i] > delta_time * self.split_ratio:
                use = 1
            for j in range(len(start_frame["players"])):
                player_data = {"index": start_frame["players"][j]["index"], "inputs": {}}
                for c in self.controls:
                    player_data["inputs"][c] = constants[use]["players"][j]["inputs"][c]
                frame["players"].append(player_data)
        return interpolated_frames

def interpolateInputs(replayData: dict, targetFramerate: int, interpolator: Interpolator) -> dict:
    pass
