# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/stats/kickoff.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ...api import player_id_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='api/stats/kickoff.proto',
  package='api.stats',
  serialized_pb=_b('\n\x17\x61pi/stats/kickoff.proto\x12\tapi.stats\x1a\x13\x61pi/player_id.proto\"A\n\x12PlayerPositionData\x12\r\n\x05pos_x\x18\x01 \x01(\x02\x12\r\n\x05pos_y\x18\x02 \x01(\x02\x12\r\n\x05pos_z\x18\x03 \x01(\x02\"\xde\x02\n\rKickoffPlayer\x12\x1d\n\x06player\x18\x01 \x01(\x0b\x32\r.api.PlayerId\x12\x34\n\x10kickoff_position\x18\x02 \x01(\x0e\x32\x1a.api.stats.KickoffPosition\x12\x30\n\x0etouch_position\x18\x03 \x01(\x0e\x32\x18.api.stats.TouchPosition\x12\x36\n\x0fplayer_position\x18\x04 \x01(\x0b\x32\x1d.api.stats.PlayerPositionData\x12\r\n\x05\x62oost\x18\x05 \x01(\x02\x12\r\n\x05jumps\x18\x06 \x03(\x02\x12\x11\n\tball_dist\x18\x07 \x01(\x02\x12\x12\n\nboost_time\x18\x08 \x01(\x02\x12\x12\n\nstart_left\x18\t \x01(\x08\x12\x35\n\x0estart_position\x18\n \x01(\x0b\x32\x1d.api.stats.PlayerPositionData\"\x8d\x01\n\x05Touch\x12)\n\x07players\x18\x01 \x03(\x0b\x32\x18.api.stats.KickoffPlayer\x12\x14\n\x0ckickoff_goal\x18\x02 \x01(\x02\x12\x18\n\x10orange_team_goal\x18\x03 \x01(\x08\x12)\n\x12\x66irst_touch_player\x18\x04 \x01(\x0b\x32\r.api.PlayerId\"\x93\x01\n\x0cKickoffStats\x12\x13\n\x0bstart_frame\x18\x01 \x01(\x05\x12\x13\n\x0btouch_frame\x18\x02 \x01(\x05\x12\x12\n\ntouch_time\x18\x03 \x01(\x02\x12$\n\x04type\x18\x04 \x01(\x0e\x32\x16.api.stats.KickoffType\x12\x1f\n\x05touch\x18\x05 \x01(\x0b\x32\x10.api.stats.Touch*S\n\x0fKickoffPosition\x12\x0c\n\x08\x44IAGONAL\x10\x00\x12\r\n\tOFFCENTER\x10\x01\x12\n\n\x06GOALIE\x10\x02\x12\x17\n\x13UNKNOWN_KICKOFF_POS\x10\x03*\xe0\x02\n\x0bKickoffType\x12\x1c\n\x18THREES_DIAG_DIAG_OFFCENT\x10\x00\x12\x19\n\x15THREES_DIAG_DIAG_GOAL\x10\x01\x12\x1f\n\x1bTHREES_DIAG_OFFCENT_OFFCENT\x10\x02\x12\x1c\n\x18THREES_DIAG_OFFCENT_GOAL\x10\x03\x12\x1f\n\x1bTHREES_OFFCENT_OFFCENT_GOAL\x10\x04\x12\x12\n\x0eTWOS_DIAG_DIAG\x10\x05\x12\x15\n\x11TWOS_DIAG_OFFCENT\x10\x06\x12\x18\n\x14TWOS_OFFCENT_OFFCENT\x10\x07\x12\x15\n\x11TWOS_OFFCENT_GOAL\x10\x08\x12\x12\n\x0eTWOS_DIAG_GOAL\x10\t\x12\r\n\tDUEL_DIAG\x10\n\x12\x10\n\x0c\x44UEL_OFFCENT\x10\x0b\x12\r\n\tDUEL_GOAL\x10\x0c\x12\x18\n\x14UNKNOWN_KICKOFF_TYPE\x10\r*Y\n\rTouchPosition\x12\t\n\x05\x42OOST\x10\x00\x12\x08\n\x04\x42\x41LL\x10\x01\x12\x07\n\x03\x41\x46K\x10\x02\x12\x08\n\x04GOAL\x10\x03\x12\t\n\x05\x43HEAT\x10\x04\x12\x15\n\x11UNKNOWN_TOUCH_POS\x10\x05')
  ,
  dependencies=[player_id_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_KICKOFFPOSITION = _descriptor.EnumDescriptor(
  name='KickoffPosition',
  full_name='api.stats.KickoffPosition',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DIAGONAL', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OFFCENTER', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GOALIE', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_KICKOFF_POS', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=773,
  serialized_end=856,
)
_sym_db.RegisterEnumDescriptor(_KICKOFFPOSITION)

KickoffPosition = enum_type_wrapper.EnumTypeWrapper(_KICKOFFPOSITION)
_KICKOFFTYPE = _descriptor.EnumDescriptor(
  name='KickoffType',
  full_name='api.stats.KickoffType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='THREES_DIAG_DIAG_OFFCENT', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='THREES_DIAG_DIAG_GOAL', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='THREES_DIAG_OFFCENT_OFFCENT', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='THREES_DIAG_OFFCENT_GOAL', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='THREES_OFFCENT_OFFCENT_GOAL', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TWOS_DIAG_DIAG', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TWOS_DIAG_OFFCENT', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TWOS_OFFCENT_OFFCENT', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TWOS_OFFCENT_GOAL', index=8, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TWOS_DIAG_GOAL', index=9, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DUEL_DIAG', index=10, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DUEL_OFFCENT', index=11, number=11,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DUEL_GOAL', index=12, number=12,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_KICKOFF_TYPE', index=13, number=13,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=859,
  serialized_end=1211,
)
_sym_db.RegisterEnumDescriptor(_KICKOFFTYPE)

KickoffType = enum_type_wrapper.EnumTypeWrapper(_KICKOFFTYPE)
_TOUCHPOSITION = _descriptor.EnumDescriptor(
  name='TouchPosition',
  full_name='api.stats.TouchPosition',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='BOOST', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BALL', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AFK', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GOAL', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHEAT', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_TOUCH_POS', index=5, number=5,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1213,
  serialized_end=1302,
)
_sym_db.RegisterEnumDescriptor(_TOUCHPOSITION)

TouchPosition = enum_type_wrapper.EnumTypeWrapper(_TOUCHPOSITION)
DIAGONAL = 0
OFFCENTER = 1
GOALIE = 2
UNKNOWN_KICKOFF_POS = 3
THREES_DIAG_DIAG_OFFCENT = 0
THREES_DIAG_DIAG_GOAL = 1
THREES_DIAG_OFFCENT_OFFCENT = 2
THREES_DIAG_OFFCENT_GOAL = 3
THREES_OFFCENT_OFFCENT_GOAL = 4
TWOS_DIAG_DIAG = 5
TWOS_DIAG_OFFCENT = 6
TWOS_OFFCENT_OFFCENT = 7
TWOS_OFFCENT_GOAL = 8
TWOS_DIAG_GOAL = 9
DUEL_DIAG = 10
DUEL_OFFCENT = 11
DUEL_GOAL = 12
UNKNOWN_KICKOFF_TYPE = 13
BOOST = 0
BALL = 1
AFK = 2
GOAL = 3
CHEAT = 4
UNKNOWN_TOUCH_POS = 5



_PLAYERPOSITIONDATA = _descriptor.Descriptor(
  name='PlayerPositionData',
  full_name='api.stats.PlayerPositionData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pos_x', full_name='api.stats.PlayerPositionData.pos_x', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pos_y', full_name='api.stats.PlayerPositionData.pos_y', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pos_z', full_name='api.stats.PlayerPositionData.pos_z', index=2,
      number=3, type=2, cpp_type=6, label=1,
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
  serialized_start=59,
  serialized_end=124,
)


_KICKOFFPLAYER = _descriptor.Descriptor(
  name='KickoffPlayer',
  full_name='api.stats.KickoffPlayer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='player', full_name='api.stats.KickoffPlayer.player', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='kickoff_position', full_name='api.stats.KickoffPlayer.kickoff_position', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='touch_position', full_name='api.stats.KickoffPlayer.touch_position', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='player_position', full_name='api.stats.KickoffPlayer.player_position', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='boost', full_name='api.stats.KickoffPlayer.boost', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='jumps', full_name='api.stats.KickoffPlayer.jumps', index=5,
      number=6, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ball_dist', full_name='api.stats.KickoffPlayer.ball_dist', index=6,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='boost_time', full_name='api.stats.KickoffPlayer.boost_time', index=7,
      number=8, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='start_left', full_name='api.stats.KickoffPlayer.start_left', index=8,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='start_position', full_name='api.stats.KickoffPlayer.start_position', index=9,
      number=10, type=11, cpp_type=10, label=1,
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
  serialized_start=127,
  serialized_end=477,
)


_TOUCH = _descriptor.Descriptor(
  name='Touch',
  full_name='api.stats.Touch',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='players', full_name='api.stats.Touch.players', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='kickoff_goal', full_name='api.stats.Touch.kickoff_goal', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='orange_team_goal', full_name='api.stats.Touch.orange_team_goal', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='first_touch_player', full_name='api.stats.Touch.first_touch_player', index=3,
      number=4, type=11, cpp_type=10, label=1,
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
  serialized_start=480,
  serialized_end=621,
)


_KICKOFFSTATS = _descriptor.Descriptor(
  name='KickoffStats',
  full_name='api.stats.KickoffStats',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='start_frame', full_name='api.stats.KickoffStats.start_frame', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='touch_frame', full_name='api.stats.KickoffStats.touch_frame', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='touch_time', full_name='api.stats.KickoffStats.touch_time', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='api.stats.KickoffStats.type', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='touch', full_name='api.stats.KickoffStats.touch', index=4,
      number=5, type=11, cpp_type=10, label=1,
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
  serialized_start=624,
  serialized_end=771,
)

_KICKOFFPLAYER.fields_by_name['player'].message_type = player_id_pb2._PLAYERID
_KICKOFFPLAYER.fields_by_name['kickoff_position'].enum_type = _KICKOFFPOSITION
_KICKOFFPLAYER.fields_by_name['touch_position'].enum_type = _TOUCHPOSITION
_KICKOFFPLAYER.fields_by_name['player_position'].message_type = _PLAYERPOSITIONDATA
_KICKOFFPLAYER.fields_by_name['start_position'].message_type = _PLAYERPOSITIONDATA
_TOUCH.fields_by_name['players'].message_type = _KICKOFFPLAYER
_TOUCH.fields_by_name['first_touch_player'].message_type = player_id_pb2._PLAYERID
_KICKOFFSTATS.fields_by_name['type'].enum_type = _KICKOFFTYPE
_KICKOFFSTATS.fields_by_name['touch'].message_type = _TOUCH
DESCRIPTOR.message_types_by_name['PlayerPositionData'] = _PLAYERPOSITIONDATA
DESCRIPTOR.message_types_by_name['KickoffPlayer'] = _KICKOFFPLAYER
DESCRIPTOR.message_types_by_name['Touch'] = _TOUCH
DESCRIPTOR.message_types_by_name['KickoffStats'] = _KICKOFFSTATS
DESCRIPTOR.enum_types_by_name['KickoffPosition'] = _KICKOFFPOSITION
DESCRIPTOR.enum_types_by_name['KickoffType'] = _KICKOFFTYPE
DESCRIPTOR.enum_types_by_name['TouchPosition'] = _TOUCHPOSITION

PlayerPositionData = _reflection.GeneratedProtocolMessageType('PlayerPositionData', (_message.Message,), dict(
  DESCRIPTOR = _PLAYERPOSITIONDATA,
  __module__ = 'api.stats.kickoff_pb2'
  # @@protoc_insertion_point(class_scope:api.stats.PlayerPositionData)
  ))
_sym_db.RegisterMessage(PlayerPositionData)

KickoffPlayer = _reflection.GeneratedProtocolMessageType('KickoffPlayer', (_message.Message,), dict(
  DESCRIPTOR = _KICKOFFPLAYER,
  __module__ = 'api.stats.kickoff_pb2'
  # @@protoc_insertion_point(class_scope:api.stats.KickoffPlayer)
  ))
_sym_db.RegisterMessage(KickoffPlayer)

Touch = _reflection.GeneratedProtocolMessageType('Touch', (_message.Message,), dict(
  DESCRIPTOR = _TOUCH,
  __module__ = 'api.stats.kickoff_pb2'
  # @@protoc_insertion_point(class_scope:api.stats.Touch)
  ))
_sym_db.RegisterMessage(Touch)

KickoffStats = _reflection.GeneratedProtocolMessageType('KickoffStats', (_message.Message,), dict(
  DESCRIPTOR = _KICKOFFSTATS,
  __module__ = 'api.stats.kickoff_pb2'
  # @@protoc_insertion_point(class_scope:api.stats.KickoffStats)
  ))
_sym_db.RegisterMessage(KickoffStats)


# @@protoc_insertion_point(module_scope)
