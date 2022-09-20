# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/stats/player_stats.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ...api.stats import stats_pb2
from ...api.stats import events_pb2
from ...api.stats import per_possession_stats_pb2
from ...api.stats import rumble_pb2
from ...api.stats import dropshot_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='api/stats/player_stats.proto',
  package='api.stats',
  serialized_pb=_b('\n\x1c\x61pi/stats/player_stats.proto\x12\tapi.stats\x1a\x15\x61pi/stats/stats.proto\x1a\x16\x61pi/stats/events.proto\x1a$api/stats/per_possession_stats.proto\x1a\x16\x61pi/stats/rumble.proto\x1a\x18\x61pi/stats/dropshot.proto\"\xab\x02\n\x05\x42oost\x12\x13\n\x0b\x62oost_usage\x18\x01 \x01(\x01\x12\x18\n\x10num_small_boosts\x18\x02 \x01(\x05\x12\x18\n\x10num_large_boosts\x18\x03 \x01(\x05\x12\x19\n\x11wasted_collection\x18\x04 \x01(\x02\x12\x14\n\x0cwasted_usage\x18\x05 \x01(\x02\x12\x17\n\x0ftime_full_boost\x18\x06 \x01(\x02\x12\x16\n\x0etime_low_boost\x18\x07 \x01(\x02\x12\x15\n\rtime_no_boost\x18\x08 \x01(\x02\x12\x19\n\x11num_stolen_boosts\x18\t \x01(\x05\x12\x1b\n\x13\x61verage_boost_level\x18\n \x01(\x02\x12\x12\n\nwasted_big\x18\x0b \x01(\x02\x12\x14\n\x0cwasted_small\x18\x0c \x01(\x02\"\xe7\x01\n\x08\x44istance\x12\x18\n\x10\x62\x61ll_hit_forward\x18\x01 \x01(\x01\x12\x19\n\x11\x62\x61ll_hit_backward\x18\x02 \x01(\x01\x12\x1c\n\x14time_closest_to_ball\x18\x03 \x01(\x02\x12\x1f\n\x17time_furthest_from_ball\x18\x04 \x01(\x02\x12\x1a\n\x12time_close_to_ball\x18\x05 \x01(\x02\x12#\n\x1btime_closest_to_team_center\x18\x06 \x01(\x02\x12&\n\x1etime_furthest_from_team_center\x18\x07 \x01(\x02\"\xc1\x01\n\x13RelativePositioning\x12\'\n\x1ftime_in_front_of_center_of_mass\x18\x01 \x01(\x02\x12\"\n\x1atime_behind_center_of_mass\x18\x02 \x01(\x02\x12 \n\x18time_most_forward_player\x18\x03 \x01(\x02\x12\x1d\n\x15time_most_back_player\x18\x04 \x01(\x02\x12\x1c\n\x14time_between_players\x18\x05 \x01(\x02\"\xfd\x05\n\x0bPlayerStats\x12\x1f\n\x05\x62oost\x18\x01 \x01(\x0b\x32\x10.api.stats.Boost\x12%\n\x08\x64istance\x18\x02 \x01(\x0b\x32\x13.api.stats.Distance\x12)\n\npossession\x18\x03 \x01(\x0b\x32\x15.api.stats.Possession\x12>\n\x15positional_tendencies\x18\x04 \x01(\x0b\x32\x1f.api.stats.PositionalTendencies\x12%\n\x08\x61verages\x18\x05 \x01(\x0b\x32\x13.api.stats.Averages\x12(\n\nhit_counts\x18\x06 \x01(\x0b\x32\x14.api.stats.HitCounts\x12/\n\x0e\x63\x61mera_changes\x18\x07 \x03(\x0b\x32\x17.api.stats.CameraChange\x12)\n\ncontroller\x18\x08 \x01(\x0b\x32\x15.api.stats.Controller\x12\x1f\n\x05speed\x18\t \x01(\x0b\x32\x10.api.stats.Speed\x12<\n\x14relative_positioning\x18\n \x01(\x0b\x32\x1e.api.stats.RelativePositioning\x12;\n\x14per_possession_stats\x18\x0b \x01(\x0b\x32\x1d.api.stats.PerPossessionStats\x12,\n\x0crumble_stats\x18\x0c \x01(\x0b\x32\x16.api.stats.RumbleStats\x12.\n\x0c\x62\x61ll_carries\x18\r \x01(\x0b\x32\x18.api.stats.CarryDribbles\x12\x38\n\rkickoff_stats\x18\x0e \x01(\x0b\x32!.api.stats.CumulativeKickoffStats\x12\x30\n\x0e\x64ropshot_stats\x18\x0f \x01(\x0b\x32\x18.api.stats.DropshotStats\x12(\n\ndemo_stats\x18\x10 \x01(\x0b\x32\x14.api.stats.DemoStats\"\xa1\x01\n\nController\x12\x13\n\x0bis_keyboard\x18\x01 \x01(\x08\x12\'\n\x1f\x61nalogue_steering_input_percent\x18\x02 \x01(\x02\x12\'\n\x1f\x61nalogue_throttle_input_percent\x18\x03 \x01(\x02\x12\x14\n\x0ctime_ballcam\x18\x04 \x01(\x02\x12\x16\n\x0etime_handbrake\x18\x05 \x01(\x02\"\x90\x02\n\rCarryDribbles\x12\x15\n\rtotal_carries\x18\x01 \x01(\x05\x12\x14\n\x0ctotal_flicks\x18\x02 \x01(\x05\x12\x15\n\rlongest_carry\x18\x03 \x01(\x02\x12\x16\n\x0e\x66urthest_carry\x18\x04 \x01(\x02\x12\x18\n\x10total_carry_time\x18\x05 \x01(\x02\x12\x1a\n\x12\x61verage_carry_time\x18\x06 \x01(\x02\x12\x1b\n\x13\x66\x61stest_carry_speed\x18\x07 \x01(\x02\x12\x1c\n\x14total_carry_distance\x18\x08 \x01(\x02\x12\x32\n\x0b\x63\x61rry_stats\x18\t \x01(\x0b\x32\x1d.api.stats.DetailedCarryStats\"\xe6\x01\n\x16\x43umulativeKickoffStats\x12\x16\n\x0etotal_kickoffs\x18\x01 \x01(\x05\x12\x16\n\x0enum_time_boost\x18\x02 \x01(\x05\x12\x16\n\x0enum_time_cheat\x18\x03 \x01(\x05\x12\x17\n\x0fnum_time_defend\x18\x04 \x01(\x05\x12\x1b\n\x13num_time_go_to_ball\x18\x05 \x01(\x05\x12\x14\n\x0cnum_time_afk\x18\x06 \x01(\x05\x12\x1c\n\x14num_time_first_touch\x18\x07 \x01(\x05\x12\x1a\n\x12\x61verage_boost_used\x18\x08 \x01(\x02\"A\n\tDemoStats\x12\x1b\n\x13num_demos_inflicted\x18\x01 \x01(\x05\x12\x17\n\x0fnum_demos_taken\x18\x02 \x01(\x05')
  ,
  dependencies=[stats_pb2.DESCRIPTOR,events_pb2.DESCRIPTOR,per_possession_stats_pb2.DESCRIPTOR,rumble_pb2.DESCRIPTOR,dropshot_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_BOOST = _descriptor.Descriptor(
  name='Boost',
  full_name='api.stats.Boost',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='boost_usage', full_name='api.stats.Boost.boost_usage', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_small_boosts', full_name='api.stats.Boost.num_small_boosts', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_large_boosts', full_name='api.stats.Boost.num_large_boosts', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='wasted_collection', full_name='api.stats.Boost.wasted_collection', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='wasted_usage', full_name='api.stats.Boost.wasted_usage', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='time_full_boost', full_name='api.stats.Boost.time_full_boost', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='time_low_boost', full_name='api.stats.Boost.time_low_boost', index=6,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='time_no_boost', full_name='api.stats.Boost.time_no_boost', index=7,
      number=8, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_stolen_boosts', full_name='api.stats.Boost.num_stolen_boosts', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='average_boost_level', full_name='api.stats.Boost.average_boost_level', index=9,
      number=10, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='wasted_big', full_name='api.stats.Boost.wasted_big', index=10,
      number=11, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='wasted_small', full_name='api.stats.Boost.wasted_small', index=11,
      number=12, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=179,
  serialized_end=478,
)


_DISTANCE = _descriptor.Descriptor(
  name='Distance',
  full_name='api.stats.Distance',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ball_hit_forward', full_name='api.stats.Distance.ball_hit_forward', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ball_hit_backward', full_name='api.stats.Distance.ball_hit_backward', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='time_closest_to_ball', full_name='api.stats.Distance.time_closest_to_ball', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='time_furthest_from_ball', full_name='api.stats.Distance.time_furthest_from_ball', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='time_close_to_ball', full_name='api.stats.Distance.time_close_to_ball', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='time_closest_to_team_center', full_name='api.stats.Distance.time_closest_to_team_center', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='time_furthest_from_team_center', full_name='api.stats.Distance.time_furthest_from_team_center', index=6,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=481,
  serialized_end=712,
)


_RELATIVEPOSITIONING = _descriptor.Descriptor(
  name='RelativePositioning',
  full_name='api.stats.RelativePositioning',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='time_in_front_of_center_of_mass', full_name='api.stats.RelativePositioning.time_in_front_of_center_of_mass', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='time_behind_center_of_mass', full_name='api.stats.RelativePositioning.time_behind_center_of_mass', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='time_most_forward_player', full_name='api.stats.RelativePositioning.time_most_forward_player', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='time_most_back_player', full_name='api.stats.RelativePositioning.time_most_back_player', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='time_between_players', full_name='api.stats.RelativePositioning.time_between_players', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=715,
  serialized_end=908,
)


_PLAYERSTATS = _descriptor.Descriptor(
  name='PlayerStats',
  full_name='api.stats.PlayerStats',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='boost', full_name='api.stats.PlayerStats.boost', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='distance', full_name='api.stats.PlayerStats.distance', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='possession', full_name='api.stats.PlayerStats.possession', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='positional_tendencies', full_name='api.stats.PlayerStats.positional_tendencies', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='averages', full_name='api.stats.PlayerStats.averages', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hit_counts', full_name='api.stats.PlayerStats.hit_counts', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='camera_changes', full_name='api.stats.PlayerStats.camera_changes', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='controller', full_name='api.stats.PlayerStats.controller', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='speed', full_name='api.stats.PlayerStats.speed', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='relative_positioning', full_name='api.stats.PlayerStats.relative_positioning', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='per_possession_stats', full_name='api.stats.PlayerStats.per_possession_stats', index=10,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rumble_stats', full_name='api.stats.PlayerStats.rumble_stats', index=11,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ball_carries', full_name='api.stats.PlayerStats.ball_carries', index=12,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='kickoff_stats', full_name='api.stats.PlayerStats.kickoff_stats', index=13,
      number=14, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dropshot_stats', full_name='api.stats.PlayerStats.dropshot_stats', index=14,
      number=15, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='demo_stats', full_name='api.stats.PlayerStats.demo_stats', index=15,
      number=16, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=911,
  serialized_end=1676,
)


_CONTROLLER = _descriptor.Descriptor(
  name='Controller',
  full_name='api.stats.Controller',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='is_keyboard', full_name='api.stats.Controller.is_keyboard', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='analogue_steering_input_percent', full_name='api.stats.Controller.analogue_steering_input_percent', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='analogue_throttle_input_percent', full_name='api.stats.Controller.analogue_throttle_input_percent', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='time_ballcam', full_name='api.stats.Controller.time_ballcam', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='time_handbrake', full_name='api.stats.Controller.time_handbrake', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1679,
  serialized_end=1840,
)


_CARRYDRIBBLES = _descriptor.Descriptor(
  name='CarryDribbles',
  full_name='api.stats.CarryDribbles',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='total_carries', full_name='api.stats.CarryDribbles.total_carries', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='total_flicks', full_name='api.stats.CarryDribbles.total_flicks', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='longest_carry', full_name='api.stats.CarryDribbles.longest_carry', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='furthest_carry', full_name='api.stats.CarryDribbles.furthest_carry', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='total_carry_time', full_name='api.stats.CarryDribbles.total_carry_time', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='average_carry_time', full_name='api.stats.CarryDribbles.average_carry_time', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fastest_carry_speed', full_name='api.stats.CarryDribbles.fastest_carry_speed', index=6,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='total_carry_distance', full_name='api.stats.CarryDribbles.total_carry_distance', index=7,
      number=8, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='carry_stats', full_name='api.stats.CarryDribbles.carry_stats', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1843,
  serialized_end=2115,
)


_CUMULATIVEKICKOFFSTATS = _descriptor.Descriptor(
  name='CumulativeKickoffStats',
  full_name='api.stats.CumulativeKickoffStats',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='total_kickoffs', full_name='api.stats.CumulativeKickoffStats.total_kickoffs', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_time_boost', full_name='api.stats.CumulativeKickoffStats.num_time_boost', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_time_cheat', full_name='api.stats.CumulativeKickoffStats.num_time_cheat', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_time_defend', full_name='api.stats.CumulativeKickoffStats.num_time_defend', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_time_go_to_ball', full_name='api.stats.CumulativeKickoffStats.num_time_go_to_ball', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_time_afk', full_name='api.stats.CumulativeKickoffStats.num_time_afk', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_time_first_touch', full_name='api.stats.CumulativeKickoffStats.num_time_first_touch', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='average_boost_used', full_name='api.stats.CumulativeKickoffStats.average_boost_used', index=7,
      number=8, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=2118,
  serialized_end=2348,
)


_DEMOSTATS = _descriptor.Descriptor(
  name='DemoStats',
  full_name='api.stats.DemoStats',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='num_demos_inflicted', full_name='api.stats.DemoStats.num_demos_inflicted', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_demos_taken', full_name='api.stats.DemoStats.num_demos_taken', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=2350,
  serialized_end=2415,
)

_PLAYERSTATS.fields_by_name['boost'].message_type = _BOOST
_PLAYERSTATS.fields_by_name['distance'].message_type = _DISTANCE
_PLAYERSTATS.fields_by_name['possession'].message_type = stats_pb2._POSSESSION
_PLAYERSTATS.fields_by_name['positional_tendencies'].message_type = stats_pb2._POSITIONALTENDENCIES
_PLAYERSTATS.fields_by_name['averages'].message_type = stats_pb2._AVERAGES
_PLAYERSTATS.fields_by_name['hit_counts'].message_type = stats_pb2._HITCOUNTS
_PLAYERSTATS.fields_by_name['camera_changes'].message_type = events_pb2._CAMERACHANGE
_PLAYERSTATS.fields_by_name['controller'].message_type = _CONTROLLER
_PLAYERSTATS.fields_by_name['speed'].message_type = stats_pb2._SPEED
_PLAYERSTATS.fields_by_name['relative_positioning'].message_type = _RELATIVEPOSITIONING
_PLAYERSTATS.fields_by_name['per_possession_stats'].message_type = per_possession_stats_pb2._PERPOSSESSIONSTATS
_PLAYERSTATS.fields_by_name['rumble_stats'].message_type = rumble_pb2._RUMBLESTATS
_PLAYERSTATS.fields_by_name['ball_carries'].message_type = _CARRYDRIBBLES
_PLAYERSTATS.fields_by_name['kickoff_stats'].message_type = _CUMULATIVEKICKOFFSTATS
_PLAYERSTATS.fields_by_name['dropshot_stats'].message_type = dropshot_pb2._DROPSHOTSTATS
_PLAYERSTATS.fields_by_name['demo_stats'].message_type = _DEMOSTATS
_CARRYDRIBBLES.fields_by_name['carry_stats'].message_type = stats_pb2._DETAILEDCARRYSTATS
DESCRIPTOR.message_types_by_name['Boost'] = _BOOST
DESCRIPTOR.message_types_by_name['Distance'] = _DISTANCE
DESCRIPTOR.message_types_by_name['RelativePositioning'] = _RELATIVEPOSITIONING
DESCRIPTOR.message_types_by_name['PlayerStats'] = _PLAYERSTATS
DESCRIPTOR.message_types_by_name['Controller'] = _CONTROLLER
DESCRIPTOR.message_types_by_name['CarryDribbles'] = _CARRYDRIBBLES
DESCRIPTOR.message_types_by_name['CumulativeKickoffStats'] = _CUMULATIVEKICKOFFSTATS
DESCRIPTOR.message_types_by_name['DemoStats'] = _DEMOSTATS

Boost = _reflection.GeneratedProtocolMessageType('Boost', (_message.Message,), dict(
  DESCRIPTOR = _BOOST,
  __module__ = 'api.stats.player_stats_pb2'
  # @@protoc_insertion_point(class_scope:api.stats.Boost)
  ))
_sym_db.RegisterMessage(Boost)

Distance = _reflection.GeneratedProtocolMessageType('Distance', (_message.Message,), dict(
  DESCRIPTOR = _DISTANCE,
  __module__ = 'api.stats.player_stats_pb2'
  # @@protoc_insertion_point(class_scope:api.stats.Distance)
  ))
_sym_db.RegisterMessage(Distance)

RelativePositioning = _reflection.GeneratedProtocolMessageType('RelativePositioning', (_message.Message,), dict(
  DESCRIPTOR = _RELATIVEPOSITIONING,
  __module__ = 'api.stats.player_stats_pb2'
  # @@protoc_insertion_point(class_scope:api.stats.RelativePositioning)
  ))
_sym_db.RegisterMessage(RelativePositioning)

PlayerStats = _reflection.GeneratedProtocolMessageType('PlayerStats', (_message.Message,), dict(
  DESCRIPTOR = _PLAYERSTATS,
  __module__ = 'api.stats.player_stats_pb2'
  # @@protoc_insertion_point(class_scope:api.stats.PlayerStats)
  ))
_sym_db.RegisterMessage(PlayerStats)

Controller = _reflection.GeneratedProtocolMessageType('Controller', (_message.Message,), dict(
  DESCRIPTOR = _CONTROLLER,
  __module__ = 'api.stats.player_stats_pb2'
  # @@protoc_insertion_point(class_scope:api.stats.Controller)
  ))
_sym_db.RegisterMessage(Controller)

CarryDribbles = _reflection.GeneratedProtocolMessageType('CarryDribbles', (_message.Message,), dict(
  DESCRIPTOR = _CARRYDRIBBLES,
  __module__ = 'api.stats.player_stats_pb2'
  # @@protoc_insertion_point(class_scope:api.stats.CarryDribbles)
  ))
_sym_db.RegisterMessage(CarryDribbles)

CumulativeKickoffStats = _reflection.GeneratedProtocolMessageType('CumulativeKickoffStats', (_message.Message,), dict(
  DESCRIPTOR = _CUMULATIVEKICKOFFSTATS,
  __module__ = 'api.stats.player_stats_pb2'
  # @@protoc_insertion_point(class_scope:api.stats.CumulativeKickoffStats)
  ))
_sym_db.RegisterMessage(CumulativeKickoffStats)

DemoStats = _reflection.GeneratedProtocolMessageType('DemoStats', (_message.Message,), dict(
  DESCRIPTOR = _DEMOSTATS,
  __module__ = 'api.stats.player_stats_pb2'
  # @@protoc_insertion_point(class_scope:api.stats.DemoStats)
  ))
_sym_db.RegisterMessage(DemoStats)


# @@protoc_insertion_point(module_scope)
