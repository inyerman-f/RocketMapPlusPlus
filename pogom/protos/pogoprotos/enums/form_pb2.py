# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/enums/form.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/enums/form.proto',
  package='pogoprotos.enums',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1bpogoprotos/enums/form.proto\x12\x10pogoprotos.enums*\xde\x10\n\x04\x46orm\x12\x0e\n\nFORM_UNSET\x10\x00\x12\x0b\n\x07UNOWN_A\x10\x01\x12\x0b\n\x07UNOWN_B\x10\x02\x12\x0b\n\x07UNOWN_C\x10\x03\x12\x0b\n\x07UNOWN_D\x10\x04\x12\x0b\n\x07UNOWN_E\x10\x05\x12\x0b\n\x07UNOWN_F\x10\x06\x12\x0b\n\x07UNOWN_G\x10\x07\x12\x0b\n\x07UNOWN_H\x10\x08\x12\x0b\n\x07UNOWN_I\x10\t\x12\x0b\n\x07UNOWN_J\x10\n\x12\x0b\n\x07UNOWN_K\x10\x0b\x12\x0b\n\x07UNOWN_L\x10\x0c\x12\x0b\n\x07UNOWN_M\x10\r\x12\x0b\n\x07UNOWN_N\x10\x0e\x12\x0b\n\x07UNOWN_O\x10\x0f\x12\x0b\n\x07UNOWN_P\x10\x10\x12\x0b\n\x07UNOWN_Q\x10\x11\x12\x0b\n\x07UNOWN_R\x10\x12\x12\x0b\n\x07UNOWN_S\x10\x13\x12\x0b\n\x07UNOWN_T\x10\x14\x12\x0b\n\x07UNOWN_U\x10\x15\x12\x0b\n\x07UNOWN_V\x10\x16\x12\x0b\n\x07UNOWN_W\x10\x17\x12\x0b\n\x07UNOWN_X\x10\x18\x12\x0b\n\x07UNOWN_Y\x10\x19\x12\x0b\n\x07UNOWN_Z\x10\x1a\x12\x1b\n\x17UNOWN_EXCLAMATION_POINT\x10\x1b\x12\x17\n\x13UNOWN_QUESTION_MARK\x10\x1c\x12\x13\n\x0f\x43\x41STFORM_NORMAL\x10\x1d\x12\x12\n\x0e\x43\x41STFORM_SUNNY\x10\x1e\x12\x12\n\x0e\x43\x41STFORM_RAINY\x10\x1f\x12\x12\n\x0e\x43\x41STFORM_SNOWY\x10 \x12\x11\n\rDEOXYS_NORMAL\x10!\x12\x11\n\rDEOXYS_ATTACK\x10\"\x12\x12\n\x0e\x44\x45OXYS_DEFENSE\x10#\x12\x10\n\x0c\x44\x45OXYS_SPEED\x10$\x12\r\n\tSPINDA_00\x10%\x12\r\n\tSPINDA_01\x10&\x12\r\n\tSPINDA_02\x10\'\x12\r\n\tSPINDA_03\x10(\x12\r\n\tSPINDA_04\x10)\x12\r\n\tSPINDA_05\x10*\x12\r\n\tSPINDA_06\x10+\x12\r\n\tSPINDA_07\x10,\x12\x12\n\x0eRATTATA_NORMAL\x10-\x12\x11\n\rRATTATA_ALOLA\x10.\x12\x13\n\x0fRATICATE_NORMAL\x10/\x12\x12\n\x0eRATICATE_ALOLA\x10\x30\x12\x11\n\rRAICHU_NORMAL\x10\x31\x12\x10\n\x0cRAICHU_ALOLA\x10\x32\x12\x14\n\x10SANDSHREW_NORMAL\x10\x33\x12\x13\n\x0fSANDSHREW_ALOLA\x10\x34\x12\x14\n\x10SANDSLASH_NORMAL\x10\x35\x12\x13\n\x0fSANDSLASH_ALOLA\x10\x36\x12\x11\n\rVULPIX_NORMAL\x10\x37\x12\x10\n\x0cVULPIX_ALOLA\x10\x38\x12\x14\n\x10NINETALES_NORMAL\x10\x39\x12\x13\n\x0fNINETALES_ALOLA\x10:\x12\x12\n\x0e\x44IGLETT_NORMAL\x10;\x12\x11\n\rDIGLETT_ALOLA\x10<\x12\x12\n\x0e\x44UGTRIO_NORMAL\x10=\x12\x11\n\rDUGTRIO_ALOLA\x10>\x12\x11\n\rMEOWTH_NORMAL\x10?\x12\x10\n\x0cMEOWTH_ALOLA\x10@\x12\x12\n\x0ePERSIAN_NORMAL\x10\x41\x12\x11\n\rPERSIAN_ALOLA\x10\x42\x12\x12\n\x0eGEODUDE_NORMAL\x10\x43\x12\x11\n\rGEODUDE_ALOLA\x10\x44\x12\x13\n\x0fGRAVELER_NORMAL\x10\x45\x12\x12\n\x0eGRAVELER_ALOLA\x10\x46\x12\x10\n\x0cGOLEM_NORMAL\x10G\x12\x0f\n\x0bGOLEM_ALOLA\x10H\x12\x11\n\rGRIMER_NORMAL\x10I\x12\x10\n\x0cGRIMER_ALOLA\x10J\x12\x0e\n\nMUK_NORMAL\x10K\x12\r\n\tMUK_ALOLA\x10L\x12\x14\n\x10\x45XEGGUTOR_NORMAL\x10M\x12\x13\n\x0f\x45XEGGUTOR_ALOLA\x10N\x12\x12\n\x0eMAROWAK_NORMAL\x10O\x12\x11\n\rMAROWAK_ALOLA\x10P\x12\x10\n\x0cROTOM_NORMAL\x10Q\x12\x0f\n\x0bROTOM_FROST\x10R\x12\r\n\tROTOM_FAN\x10S\x12\r\n\tROTOM_MOW\x10T\x12\x0e\n\nROTOM_WASH\x10U\x12\x0e\n\nROTOM_HEAT\x10V\x12\x12\n\x0eWORMADAM_PLANT\x10W\x12\x12\n\x0eWORMADAM_SANDY\x10X\x12\x12\n\x0eWORMADAM_TRASH\x10Y\x12\x14\n\x10GIRATINA_ALTERED\x10Z\x12\x13\n\x0fGIRATINA_ORIGIN\x10[\x12\x0f\n\x0bSHAYMIN_SKY\x10\\\x12\x10\n\x0cSHAYMIN_LAND\x10]\x12\x14\n\x10\x43HERRIM_OVERCAST\x10^\x12\x11\n\rCHERRIM_SUNNY\x10_\x12\x14\n\x10SHELLOS_WEST_SEA\x10`\x12\x14\n\x10SHELLOS_EAST_SEA\x10\x61\x12\x16\n\x12GASTRODON_WEST_SEA\x10\x62\x12\x16\n\x12GASTRODON_EAST_SEA\x10\x63\x12\x11\n\rARCEUS_NORMAL\x10\x64\x12\x13\n\x0f\x41RCEUS_FIGHTING\x10\x65\x12\x11\n\rARCEUS_FLYING\x10\x66\x12\x11\n\rARCEUS_POISON\x10g\x12\x11\n\rARCEUS_GROUND\x10h\x12\x0f\n\x0b\x41RCEUS_ROCK\x10i\x12\x0e\n\nARCEUS_BUG\x10j\x12\x10\n\x0c\x41RCEUS_GHOST\x10k\x12\x10\n\x0c\x41RCEUS_STEEL\x10l\x12\x0f\n\x0b\x41RCEUS_FIRE\x10m\x12\x10\n\x0c\x41RCEUS_WATER\x10n\x12\x10\n\x0c\x41RCEUS_GRASS\x10o\x12\x13\n\x0f\x41RCEUS_ELECTRIC\x10p\x12\x12\n\x0e\x41RCEUS_PSYCHIC\x10q\x12\x0e\n\nARCEUS_ICE\x10r\x12\x11\n\rARCEUS_DRAGON\x10s\x12\x0f\n\x0b\x41RCEUS_DARK\x10t\x12\x10\n\x0c\x41RCEUS_FAIRY\x10u\x12\x0f\n\x0b\x42URMY_PLANT\x10v\x12\x0f\n\x0b\x42URMY_SANDY\x10w\x12\x0f\n\x0b\x42URMY_TRASH\x10xb\x06proto3')
)

_FORM = _descriptor.EnumDescriptor(
  name='Form',
  full_name='pogoprotos.enums.Form',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='FORM_UNSET', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNOWN_A', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNOWN_B', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNOWN_C', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNOWN_D', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNOWN_E', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNOWN_F', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNOWN_G', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNOWN_H', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNOWN_I', index=9, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNOWN_J', index=10, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNOWN_K', index=11, number=11,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNOWN_L', index=12, number=12,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNOWN_M', index=13, number=13,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNOWN_N', index=14, number=14,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNOWN_O', index=15, number=15,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNOWN_P', index=16, number=16,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNOWN_Q', index=17, number=17,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNOWN_R', index=18, number=18,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNOWN_S', index=19, number=19,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNOWN_T', index=20, number=20,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNOWN_U', index=21, number=21,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNOWN_V', index=22, number=22,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNOWN_W', index=23, number=23,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNOWN_X', index=24, number=24,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNOWN_Y', index=25, number=25,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNOWN_Z', index=26, number=26,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNOWN_EXCLAMATION_POINT', index=27, number=27,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNOWN_QUESTION_MARK', index=28, number=28,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CASTFORM_NORMAL', index=29, number=29,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CASTFORM_SUNNY', index=30, number=30,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CASTFORM_RAINY', index=31, number=31,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CASTFORM_SNOWY', index=32, number=32,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEOXYS_NORMAL', index=33, number=33,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEOXYS_ATTACK', index=34, number=34,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEOXYS_DEFENSE', index=35, number=35,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEOXYS_SPEED', index=36, number=36,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SPINDA_00', index=37, number=37,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SPINDA_01', index=38, number=38,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SPINDA_02', index=39, number=39,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SPINDA_03', index=40, number=40,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SPINDA_04', index=41, number=41,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SPINDA_05', index=42, number=42,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SPINDA_06', index=43, number=43,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SPINDA_07', index=44, number=44,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RATTATA_NORMAL', index=45, number=45,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RATTATA_ALOLA', index=46, number=46,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RATICATE_NORMAL', index=47, number=47,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RATICATE_ALOLA', index=48, number=48,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RAICHU_NORMAL', index=49, number=49,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RAICHU_ALOLA', index=50, number=50,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SANDSHREW_NORMAL', index=51, number=51,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SANDSHREW_ALOLA', index=52, number=52,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SANDSLASH_NORMAL', index=53, number=53,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SANDSLASH_ALOLA', index=54, number=54,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VULPIX_NORMAL', index=55, number=55,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VULPIX_ALOLA', index=56, number=56,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NINETALES_NORMAL', index=57, number=57,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NINETALES_ALOLA', index=58, number=58,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DIGLETT_NORMAL', index=59, number=59,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DIGLETT_ALOLA', index=60, number=60,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DUGTRIO_NORMAL', index=61, number=61,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DUGTRIO_ALOLA', index=62, number=62,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MEOWTH_NORMAL', index=63, number=63,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MEOWTH_ALOLA', index=64, number=64,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PERSIAN_NORMAL', index=65, number=65,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PERSIAN_ALOLA', index=66, number=66,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GEODUDE_NORMAL', index=67, number=67,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GEODUDE_ALOLA', index=68, number=68,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GRAVELER_NORMAL', index=69, number=69,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GRAVELER_ALOLA', index=70, number=70,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GOLEM_NORMAL', index=71, number=71,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GOLEM_ALOLA', index=72, number=72,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GRIMER_NORMAL', index=73, number=73,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GRIMER_ALOLA', index=74, number=74,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MUK_NORMAL', index=75, number=75,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MUK_ALOLA', index=76, number=76,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EXEGGUTOR_NORMAL', index=77, number=77,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EXEGGUTOR_ALOLA', index=78, number=78,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MAROWAK_NORMAL', index=79, number=79,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MAROWAK_ALOLA', index=80, number=80,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ROTOM_NORMAL', index=81, number=81,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ROTOM_FROST', index=82, number=82,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ROTOM_FAN', index=83, number=83,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ROTOM_MOW', index=84, number=84,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ROTOM_WASH', index=85, number=85,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ROTOM_HEAT', index=86, number=86,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WORMADAM_PLANT', index=87, number=87,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WORMADAM_SANDY', index=88, number=88,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WORMADAM_TRASH', index=89, number=89,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GIRATINA_ALTERED', index=90, number=90,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GIRATINA_ORIGIN', index=91, number=91,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SHAYMIN_SKY', index=92, number=92,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SHAYMIN_LAND', index=93, number=93,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHERRIM_OVERCAST', index=94, number=94,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHERRIM_SUNNY', index=95, number=95,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SHELLOS_WEST_SEA', index=96, number=96,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SHELLOS_EAST_SEA', index=97, number=97,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GASTRODON_WEST_SEA', index=98, number=98,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GASTRODON_EAST_SEA', index=99, number=99,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ARCEUS_NORMAL', index=100, number=100,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ARCEUS_FIGHTING', index=101, number=101,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ARCEUS_FLYING', index=102, number=102,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ARCEUS_POISON', index=103, number=103,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ARCEUS_GROUND', index=104, number=104,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ARCEUS_ROCK', index=105, number=105,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ARCEUS_BUG', index=106, number=106,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ARCEUS_GHOST', index=107, number=107,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ARCEUS_STEEL', index=108, number=108,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ARCEUS_FIRE', index=109, number=109,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ARCEUS_WATER', index=110, number=110,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ARCEUS_GRASS', index=111, number=111,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ARCEUS_ELECTRIC', index=112, number=112,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ARCEUS_PSYCHIC', index=113, number=113,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ARCEUS_ICE', index=114, number=114,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ARCEUS_DRAGON', index=115, number=115,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ARCEUS_DARK', index=116, number=116,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ARCEUS_FAIRY', index=117, number=117,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BURMY_PLANT', index=118, number=118,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BURMY_SANDY', index=119, number=119,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BURMY_TRASH', index=120, number=120,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=50,
  serialized_end=2192,
)
_sym_db.RegisterEnumDescriptor(_FORM)

Form = enum_type_wrapper.EnumTypeWrapper(_FORM)
FORM_UNSET = 0
UNOWN_A = 1
UNOWN_B = 2
UNOWN_C = 3
UNOWN_D = 4
UNOWN_E = 5
UNOWN_F = 6
UNOWN_G = 7
UNOWN_H = 8
UNOWN_I = 9
UNOWN_J = 10
UNOWN_K = 11
UNOWN_L = 12
UNOWN_M = 13
UNOWN_N = 14
UNOWN_O = 15
UNOWN_P = 16
UNOWN_Q = 17
UNOWN_R = 18
UNOWN_S = 19
UNOWN_T = 20
UNOWN_U = 21
UNOWN_V = 22
UNOWN_W = 23
UNOWN_X = 24
UNOWN_Y = 25
UNOWN_Z = 26
UNOWN_EXCLAMATION_POINT = 27
UNOWN_QUESTION_MARK = 28
CASTFORM_NORMAL = 29
CASTFORM_SUNNY = 30
CASTFORM_RAINY = 31
CASTFORM_SNOWY = 32
DEOXYS_NORMAL = 33
DEOXYS_ATTACK = 34
DEOXYS_DEFENSE = 35
DEOXYS_SPEED = 36
SPINDA_00 = 37
SPINDA_01 = 38
SPINDA_02 = 39
SPINDA_03 = 40
SPINDA_04 = 41
SPINDA_05 = 42
SPINDA_06 = 43
SPINDA_07 = 44
RATTATA_NORMAL = 45
RATTATA_ALOLA = 46
RATICATE_NORMAL = 47
RATICATE_ALOLA = 48
RAICHU_NORMAL = 49
RAICHU_ALOLA = 50
SANDSHREW_NORMAL = 51
SANDSHREW_ALOLA = 52
SANDSLASH_NORMAL = 53
SANDSLASH_ALOLA = 54
VULPIX_NORMAL = 55
VULPIX_ALOLA = 56
NINETALES_NORMAL = 57
NINETALES_ALOLA = 58
DIGLETT_NORMAL = 59
DIGLETT_ALOLA = 60
DUGTRIO_NORMAL = 61
DUGTRIO_ALOLA = 62
MEOWTH_NORMAL = 63
MEOWTH_ALOLA = 64
PERSIAN_NORMAL = 65
PERSIAN_ALOLA = 66
GEODUDE_NORMAL = 67
GEODUDE_ALOLA = 68
GRAVELER_NORMAL = 69
GRAVELER_ALOLA = 70
GOLEM_NORMAL = 71
GOLEM_ALOLA = 72
GRIMER_NORMAL = 73
GRIMER_ALOLA = 74
MUK_NORMAL = 75
MUK_ALOLA = 76
EXEGGUTOR_NORMAL = 77
EXEGGUTOR_ALOLA = 78
MAROWAK_NORMAL = 79
MAROWAK_ALOLA = 80
ROTOM_NORMAL = 81
ROTOM_FROST = 82
ROTOM_FAN = 83
ROTOM_MOW = 84
ROTOM_WASH = 85
ROTOM_HEAT = 86
WORMADAM_PLANT = 87
WORMADAM_SANDY = 88
WORMADAM_TRASH = 89
GIRATINA_ALTERED = 90
GIRATINA_ORIGIN = 91
SHAYMIN_SKY = 92
SHAYMIN_LAND = 93
CHERRIM_OVERCAST = 94
CHERRIM_SUNNY = 95
SHELLOS_WEST_SEA = 96
SHELLOS_EAST_SEA = 97
GASTRODON_WEST_SEA = 98
GASTRODON_EAST_SEA = 99
ARCEUS_NORMAL = 100
ARCEUS_FIGHTING = 101
ARCEUS_FLYING = 102
ARCEUS_POISON = 103
ARCEUS_GROUND = 104
ARCEUS_ROCK = 105
ARCEUS_BUG = 106
ARCEUS_GHOST = 107
ARCEUS_STEEL = 108
ARCEUS_FIRE = 109
ARCEUS_WATER = 110
ARCEUS_GRASS = 111
ARCEUS_ELECTRIC = 112
ARCEUS_PSYCHIC = 113
ARCEUS_ICE = 114
ARCEUS_DRAGON = 115
ARCEUS_DARK = 116
ARCEUS_FAIRY = 117
BURMY_PLANT = 118
BURMY_SANDY = 119
BURMY_TRASH = 120


DESCRIPTOR.enum_types_by_name['Form'] = _FORM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


# @@protoc_insertion_point(module_scope)
