# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/settings/master/lucky_pokemon_settings.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/settings/master/lucky_pokemon_settings.proto',
  package='pogoprotos.settings.master',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n7pogoprotos/settings/master/lucky_pokemon_settings.proto\x12\x1apogoprotos.settings.master\"B\n\x14LuckyPokemonSettings\x12*\n\"power_up_stardust_discount_percent\x18\x01 \x01(\x02\x62\x06proto3')
)




_LUCKYPOKEMONSETTINGS = _descriptor.Descriptor(
  name='LuckyPokemonSettings',
  full_name='pogoprotos.settings.master.LuckyPokemonSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='power_up_stardust_discount_percent', full_name='pogoprotos.settings.master.LuckyPokemonSettings.power_up_stardust_discount_percent', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=87,
  serialized_end=153,
)

DESCRIPTOR.message_types_by_name['LuckyPokemonSettings'] = _LUCKYPOKEMONSETTINGS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LuckyPokemonSettings = _reflection.GeneratedProtocolMessageType('LuckyPokemonSettings', (_message.Message,), dict(
  DESCRIPTOR = _LUCKYPOKEMONSETTINGS,
  __module__ = 'pogoprotos.settings.master.lucky_pokemon_settings_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.settings.master.LuckyPokemonSettings)
  ))
_sym_db.RegisterMessage(LuckyPokemonSettings)


# @@protoc_insertion_point(module_scope)