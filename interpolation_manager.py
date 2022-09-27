import random

import numpy


class Interpolator:
    '''
    Parent class for all different kinds of Interpolators.
    Creates additional frames to increase the framerate of the input data
    '''
    def __init__(self, target_framerate: float):
        self.target_framerate = target_framerate  # in frames per second
        self.controls = ["throttle", "steer", "pitch", "yaw", "roll", "jump", "boost", "handbrake"]
        self.float_controls = ["throttle", "steer", "pitch", "yaw", "roll"]
        self.bool_controls = ["jump", "boost", "handbrake"]

    def to_string(self):
        return "[" + type(self).__name__ + str(self.target_framerate) + "]"

    def interpolate_two_bools(self, start_value: bool, end_value: bool, frames_between: int, frame_index: int) -> bool:
        '''
        Overrite this to change the way two boolean inputs get interpolated. Default: False
        :param start_value: The Value of the input in the starting frame
        :param end_value: The Value of the input in the end frame
        :param frames_between: The number of frames that will get inserted between start and end frame
        :param frame_index: The index of the frame this methods output belongs to in regard to its position within the
        frames that get inserted inbetween start and end. Min: 0, Max frames_between-1
        :return: The interpolated value
        '''
        return False

    def interpolate_two_floats(self, start_value: float, end_value: float, frames_between: int,
                               frame_index: int) -> float:
        '''
        Overrite this to change the way two float inputs get interpolated. Default: 0
        :param start_value: The Value of the input in the starting frame
        :param end_value: The Value of the input in the end frame
        :param frames_between: The number of frames that will get inserted between start and end frame
        :param frame_index: The index of the frame this methods output belongs to in regard to its position within the
        frames that get inserted inbetween start and end. Min: 0, Max frames_between-1
        :return: The interpolated value
        '''
        return 0

    def interpolate_two_values(self, start_value, end_value, frames_between: int, frame_index: int):
        '''
        Calls interpolate_two_bools or interpolate_two_floats depending on the type of value used.
        Only overwrite this if the interpolating behavior is indifferent to the type of data used
        :param start_value: The Value of the input in the starting frame
        :param end_value: The Value of the input in the end frame
        :param frames_between: The number of frames that will get inserted between start and end frame
        :param frame_index: The index of the frame this methods output belongs to in regard to its position within the
        frames that get inserted inbetween start and end. Min: 0, Max frames_between-1
        :return: The interpolated value
        '''
        if type(start_value) == bool and type(end_value) == bool:
            return self.interpolate_two_bools(start_value, end_value, frames_between, frame_index)
        if type(start_value) == float and type(end_value) == float:
            return self.interpolate_two_floats(start_value, end_value, frames_between, frame_index)
        raise ValueError(
            "The start and end values dont match types or are neither bool nor float! start_value: " + str(start_value) + " end_value: " + str(
                end_value))

    def interpolate_two_frames(self, start_frame: dict, end_frame: dict) -> list:
        '''
        Interpolates all input dimensions between start_frame and end_frame to match the target_framerate.
        Ideally, start_frame and end_frame are follow-up frames
        :param start_frame: a frame structured as described in input_extractor.extract_inputs_from_goal
        :param end_frame: a frame structured the same way as start_frame
        :return: list of frames to insert between start_frame and end_frame to interpolate between them
        '''
        times = self.missing_frame_times(start_frame["time"], end_frame["time"])
        frames_between = len(times)
        interpolated_frames = []
        for frame_index in range(frames_between):
            frame = {"time": times[frame_index], "players": []}
            for player_index in range(len(start_frame["players"])):
                player_start = start_frame["players"][player_index]
                start_inputs = player_start["inputs"]
                end_inputs = end_frame["players"][player_index]["inputs"]
                player_data = {"index": player_start["index"], "inputs": {}}
                for c in self.float_controls:
                    player_data["inputs"][c] = self.interpolate_two_floats(start_inputs[c], end_inputs[c],
                                                                           frames_between, frame_index)
                for c in self.bool_controls:
                    player_data["inputs"][c] = self.interpolate_two_bools(start_inputs[c], end_inputs[c],
                                                                          frames_between, frame_index)
                frame["players"].append(player_data)
            interpolated_frames.append(frame)
        return interpolated_frames

    def interpolate_all_frames(self, input_frame_data: list) -> list:
        '''
        Takes structured input data and adds interpolated frames inbetween to raise the framerate to the
        target_framerate
        :param input_frame_data: frames structured as described in input_extractor.extract_inputs_from_goal
        :return:
        '''
        interpolated_inputs = []
        for i in range(len(input_frame_data) - 1):
            interpolated_inputs.append(input_frame_data[i])
            interpolated_inputs.extend(self.interpolate_two_frames(input_frame_data[i], input_frame_data[i + 1]))
        interpolated_inputs.append(input_frame_data[len(input_frame_data) - 1])
        return interpolated_inputs

    def missing_frame_times(self, start_time: float, end_time: float) -> list:
        '''
        Return the times of frames that need to be inserted between start_time and end_time to get the target_framerate
        :param start_time: time of the first frame
        :param end_time: time of the second frame
        :return:
        '''
        delta_time = float(end_time) - float(start_time)
        delta_frames = round(delta_time * self.target_framerate) - 1
        '''
        print(type(delta_time))
        print(type(delta_frames))
        print(type(self.target_framerate))
        print(start_time + (0 + 1) / self.target_framerate)
        '''
        times = [start_time + (i + 1) / self.target_framerate for i in range(delta_frames)]
        return times


class ConstantSplit(Interpolator):
    def __init__(self, target_framerate, split_ratio):
        '''
        Interpolates between two frames by copying the start or the end frame depending on the split_ratio
        :param target_framerate:
        :param split_ratio: 1 means all start frame, 0 means all end frame, 0.5 means first half start frame,
        second half end frame
        '''
        super().__init__(target_framerate)
        self.split_ratio = split_ratio

    def to_string(self):
        return "[" + type(self).__name__ + str(self.target_framerate) + "," + str(self.split_ratio) + "]"

    def interpolate_two_values(self, start_value, end_value, frames_between, frame_index):
        if frame_index + 1 > frames_between * self.split_ratio:
            return end_value
        else:
            return start_value


class SmoothSteps(Interpolator):
    '''
    Interpolates by gradually increasing or decreasing the start value to the end value
    '''
    def interpolate_two_floats(self, start_value: float, end_value: float, frames_between: int,
                               frame_index: int) -> float:
        return start_value + (end_value - start_value) * (frame_index + 1) / (frames_between + 1)

    def interpolate_two_bools(self, start_value: bool, end_value: bool, frames_between: int, frame_index: int) -> bool:
        itp = ConstantSplit(self.target_framerate, 0.5)
        return itp.interpolate_two_values(start_value, end_value, frames_between, frame_index)


class Randomizer(Interpolator):
    '''
    Interpolates with (uniformly) random inputs
    '''

    def interpolate_two_bools(self, start_value: bool, end_value: bool, frames_between: int, frame_index: int) -> bool:
        return random.Random().uniform(0, 1) < 0.5

    def interpolate_two_floats(self, start_value: float, end_value: float, frames_between: int,
                               frame_index: int) -> float:
        return random.Random().uniform(0, 1)


class GaussSteps(Interpolator):
    '''
    Interpolates by gradually increasing or decreasing the start value to the end value and adding gaussian noise.
    Bools get gradually increasing or decreasing probabilities.
    '''

    def interpolate_two_bools(self, start_value: bool, end_value: bool, frames_between: int, frame_index: int) -> bool:
        s = float(start_value)
        e = float(end_value)
        itp = SmoothSteps(self.target_framerate)
        return random.Random().uniform(0, 1) < itp.interpolate_two_floats(s, e, frames_between, frame_index)

    def interpolate_two_floats(self, start_value: float, end_value: float, frames_between: int,
                               frame_index: int) -> float:
        itp = SmoothSteps(self.target_framerate)
        step = itp.interpolate_two_floats(start_value, end_value, frames_between, frame_index)
        next_step = itp.interpolate_two_floats(start_value, end_value, frames_between, frame_index + 1)
        sdv_width = 1.28155  # how many standard deviations to the half-way point to the next step? 1.28155 means only
        # 10% chance for the value to be closer to the next steps mean than to the current steps mean
        return min(max(step + random.Random().gauss(0, abs(next_step - step) / (2 * sdv_width)), 0.0), 1.0)
