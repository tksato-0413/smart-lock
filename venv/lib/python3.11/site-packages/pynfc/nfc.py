# -*- coding: utf-8 -*-
#
# TARGET arch is: ('-I/usr/include/clang/5.0/include/',)
# WORD_SIZE is: 8
# POINTER_SIZE is: 8
# LONGDOUBLE_SIZE is: 16
#
import ctypes


_libraries = {}
_libraries['libfreefare.so'] = ctypes.CDLL('libfreefare.so')
c_int128 = ctypes.c_ubyte*16
c_uint128 = c_int128
void = None
if ctypes.sizeof(ctypes.c_longdouble) == 16:
    c_long_double_t = ctypes.c_longdouble
else:
    c_long_double_t = ctypes.c_ubyte*16



size_t = ctypes.c_size_t
class struct_mifare_desfire_key(ctypes.Structure):
    pass

MifareDESFireKey = ctypes.POINTER(struct_mifare_desfire_key)
MifareUltralightPageNumber = ctypes.c_ubyte
MifareUltralightPage = ctypes.c_ubyte * 4
class struct_mifare_tag(ctypes.Structure):
    pass

class struct_nfc_device(ctypes.Structure):
    pass

freefare_get_tags = _libraries['libfreefare.so'].freefare_get_tags
freefare_get_tags.restype = ctypes.POINTER(ctypes.POINTER(struct_mifare_tag))
freefare_get_tags.argtypes = [ctypes.POINTER(struct_nfc_device)]
MifareTag = ctypes.POINTER(struct_mifare_tag)
class struct_c__SA_nfc_iso14443a_info(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('abtAtqa', ctypes.c_ubyte * 2),
    ('btSak', ctypes.c_ubyte),
    ('szUidLen', ctypes.c_uint64),
    ('abtUid', ctypes.c_ubyte * 10),
    ('szAtsLen', ctypes.c_uint64),
    ('abtAts', ctypes.c_ubyte * 254),
     ]

nfc_iso14443a_info = struct_c__SA_nfc_iso14443a_info
freefare_tag_new = _libraries['libfreefare.so'].freefare_tag_new
freefare_tag_new.restype = MifareTag
freefare_tag_new.argtypes = [ctypes.POINTER(struct_nfc_device), nfc_iso14443a_info]
freefare_get_tag_friendly_name = _libraries['libfreefare.so'].freefare_get_tag_friendly_name
freefare_get_tag_friendly_name.restype = ctypes.POINTER(ctypes.c_char)
freefare_get_tag_friendly_name.argtypes = [MifareTag]
freefare_get_tag_uid = _libraries['libfreefare.so'].freefare_get_tag_uid
freefare_get_tag_uid.restype = ctypes.POINTER(ctypes.c_char)
freefare_get_tag_uid.argtypes = [MifareTag]
freefare_free_tag = _libraries['libfreefare.so'].freefare_free_tag
freefare_free_tag.restype = None
freefare_free_tag.argtypes = [MifareTag]
freefare_free_tags = _libraries['libfreefare.so'].freefare_free_tags
freefare_free_tags.restype = None
freefare_free_tags.argtypes = [ctypes.POINTER(ctypes.POINTER(struct_mifare_tag))]
freefare_strerror = _libraries['libfreefare.so'].freefare_strerror
freefare_strerror.restype = ctypes.POINTER(ctypes.c_char)
freefare_strerror.argtypes = [MifareTag]
freefare_strerror_r = _libraries['libfreefare.so'].freefare_strerror_r
freefare_strerror_r.restype = ctypes.c_int32
freefare_strerror_r.argtypes = [MifareTag, ctypes.POINTER(ctypes.c_char), size_t]
freefare_perror = _libraries['libfreefare.so'].freefare_perror
freefare_perror.restype = None
freefare_perror.argtypes = [MifareTag, ctypes.POINTER(ctypes.c_char)]
mifare_ultralight_connect = _libraries['libfreefare.so'].mifare_ultralight_connect
mifare_ultralight_connect.restype = ctypes.c_int32
mifare_ultralight_connect.argtypes = [MifareTag]
mifare_ultralight_disconnect = _libraries['libfreefare.so'].mifare_ultralight_disconnect
mifare_ultralight_disconnect.restype = ctypes.c_int32
mifare_ultralight_disconnect.argtypes = [MifareTag]
mifare_ultralight_read = _libraries['libfreefare.so'].mifare_ultralight_read
mifare_ultralight_read.restype = ctypes.c_int32
mifare_ultralight_read.argtypes = [MifareTag, MifareUltralightPageNumber, ctypes.POINTER(ctypes.c_ubyte * 4)]
mifare_ultralight_write = _libraries['libfreefare.so'].mifare_ultralight_write
mifare_ultralight_write.restype = ctypes.c_int32
mifare_ultralight_write.argtypes = [MifareTag, MifareUltralightPageNumber, MifareUltralightPage]
mifare_ultralightc_authenticate = _libraries['libfreefare.so'].mifare_ultralightc_authenticate
mifare_ultralightc_authenticate.restype = ctypes.c_int32
mifare_ultralightc_authenticate.argtypes = [MifareTag, MifareDESFireKey]
is_mifare_ultralightc_on_reader = _libraries['libfreefare.so'].is_mifare_ultralightc_on_reader
is_mifare_ultralightc_on_reader.restype = ctypes.c_bool
is_mifare_ultralightc_on_reader.argtypes = [ctypes.POINTER(struct_nfc_device), nfc_iso14443a_info]
MifareClassicBlock = ctypes.c_ubyte * 16
MifareClassicSectorNumber = ctypes.c_ubyte
MifareClassicBlockNumber = ctypes.c_ubyte

# values for enumeration 'c__EA_MifareClassicKeyType'
c__EA_MifareClassicKeyType__enumvalues = {
    0: 'MFC_KEY_A',
    1: 'MFC_KEY_B',
}
MFC_KEY_A = 0
MFC_KEY_B = 1
c__EA_MifareClassicKeyType = ctypes.c_int # enum
MifareClassicKeyType = c__EA_MifareClassicKeyType
MifareClassicKeyType__enumvalues = c__EA_MifareClassicKeyType__enumvalues
MifareClassicKey = ctypes.c_ubyte * 6
mifare_classic_connect = _libraries['libfreefare.so'].mifare_classic_connect
mifare_classic_connect.restype = ctypes.c_int32
mifare_classic_connect.argtypes = [MifareTag]
mifare_classic_disconnect = _libraries['libfreefare.so'].mifare_classic_disconnect
mifare_classic_disconnect.restype = ctypes.c_int32
mifare_classic_disconnect.argtypes = [MifareTag]
mifare_classic_authenticate = _libraries['libfreefare.so'].mifare_classic_authenticate
mifare_classic_authenticate.restype = ctypes.c_int32
mifare_classic_authenticate.argtypes = [MifareTag, MifareClassicBlockNumber, MifareClassicKey, MifareClassicKeyType]
mifare_classic_read = _libraries['libfreefare.so'].mifare_classic_read
mifare_classic_read.restype = ctypes.c_int32
mifare_classic_read.argtypes = [MifareTag, MifareClassicBlockNumber, ctypes.POINTER(ctypes.c_ubyte * 16)]
int32_t = ctypes.c_int32
mifare_classic_init_value = _libraries['libfreefare.so'].mifare_classic_init_value
mifare_classic_init_value.restype = ctypes.c_int32
mifare_classic_init_value.argtypes = [MifareTag, MifareClassicBlockNumber, int32_t, MifareClassicBlockNumber]
mifare_classic_read_value = _libraries['libfreefare.so'].mifare_classic_read_value
mifare_classic_read_value.restype = ctypes.c_int32
mifare_classic_read_value.argtypes = [MifareTag, MifareClassicBlockNumber, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_ubyte)]
mifare_classic_write = _libraries['libfreefare.so'].mifare_classic_write
mifare_classic_write.restype = ctypes.c_int32
mifare_classic_write.argtypes = [MifareTag, MifareClassicBlockNumber, MifareClassicBlock]
uint32_t = ctypes.c_uint32
mifare_classic_increment = _libraries['libfreefare.so'].mifare_classic_increment
mifare_classic_increment.restype = ctypes.c_int32
mifare_classic_increment.argtypes = [MifareTag, MifareClassicBlockNumber, uint32_t]
mifare_classic_decrement = _libraries['libfreefare.so'].mifare_classic_decrement
mifare_classic_decrement.restype = ctypes.c_int32
mifare_classic_decrement.argtypes = [MifareTag, MifareClassicBlockNumber, uint32_t]
mifare_classic_restore = _libraries['libfreefare.so'].mifare_classic_restore
mifare_classic_restore.restype = ctypes.c_int32
mifare_classic_restore.argtypes = [MifareTag, MifareClassicBlockNumber]
mifare_classic_transfer = _libraries['libfreefare.so'].mifare_classic_transfer
mifare_classic_transfer.restype = ctypes.c_int32
mifare_classic_transfer.argtypes = [MifareTag, MifareClassicBlockNumber]
uint16_t = ctypes.c_uint16
mifare_classic_get_trailer_block_permission = _libraries['libfreefare.so'].mifare_classic_get_trailer_block_permission
mifare_classic_get_trailer_block_permission.restype = ctypes.c_int32
mifare_classic_get_trailer_block_permission.argtypes = [MifareTag, MifareClassicBlockNumber, uint16_t, MifareClassicKeyType]
mifare_classic_get_data_block_permission = _libraries['libfreefare.so'].mifare_classic_get_data_block_permission
mifare_classic_get_data_block_permission.restype = ctypes.c_int32
mifare_classic_get_data_block_permission.argtypes = [MifareTag, MifareClassicBlockNumber, ctypes.c_ubyte, MifareClassicKeyType]
mifare_classic_format_sector = _libraries['libfreefare.so'].mifare_classic_format_sector
mifare_classic_format_sector.restype = ctypes.c_int32
mifare_classic_format_sector.argtypes = [MifareTag, MifareClassicSectorNumber]
uint8_t = ctypes.c_uint8
mifare_classic_trailer_block = _libraries['libfreefare.so'].mifare_classic_trailer_block
mifare_classic_trailer_block.restype = None
mifare_classic_trailer_block.argtypes = [ctypes.POINTER(ctypes.c_ubyte * 16), MifareClassicKey, uint8_t, uint8_t, uint8_t, uint8_t, uint8_t, MifareClassicKey]
mifare_classic_block_sector = _libraries['libfreefare.so'].mifare_classic_block_sector
mifare_classic_block_sector.restype = MifareClassicSectorNumber
mifare_classic_block_sector.argtypes = [MifareClassicBlockNumber]
mifare_classic_sector_first_block = _libraries['libfreefare.so'].mifare_classic_sector_first_block
mifare_classic_sector_first_block.restype = MifareClassicBlockNumber
mifare_classic_sector_first_block.argtypes = [MifareClassicSectorNumber]
mifare_classic_sector_block_count = _libraries['libfreefare.so'].mifare_classic_sector_block_count
mifare_classic_sector_block_count.restype = size_t
mifare_classic_sector_block_count.argtypes = [MifareClassicSectorNumber]
mifare_classic_sector_last_block = _libraries['libfreefare.so'].mifare_classic_sector_last_block
mifare_classic_sector_last_block.restype = MifareClassicBlockNumber
mifare_classic_sector_last_block.argtypes = [MifareClassicSectorNumber]
class struct_mad_aid(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('application_code', ctypes.c_ubyte),
    ('function_cluster_code', ctypes.c_ubyte),
     ]

MadAid = struct_mad_aid
class struct_mad(ctypes.Structure):
    pass

Mad = ctypes.POINTER(struct_mad)
mad_new = _libraries['libfreefare.so'].mad_new
mad_new.restype = Mad
mad_new.argtypes = [uint8_t]
mad_read = _libraries['libfreefare.so'].mad_read
mad_read.restype = Mad
mad_read.argtypes = [MifareTag]
mad_write = _libraries['libfreefare.so'].mad_write
mad_write.restype = ctypes.c_int32
mad_write.argtypes = [MifareTag, Mad, MifareClassicKey, MifareClassicKey]
mad_get_version = _libraries['libfreefare.so'].mad_get_version
mad_get_version.restype = ctypes.c_int32
mad_get_version.argtypes = [Mad]
mad_set_version = _libraries['libfreefare.so'].mad_set_version
mad_set_version.restype = None
mad_set_version.argtypes = [Mad, uint8_t]
mad_get_card_publisher_sector = _libraries['libfreefare.so'].mad_get_card_publisher_sector
mad_get_card_publisher_sector.restype = MifareClassicSectorNumber
mad_get_card_publisher_sector.argtypes = [Mad]
mad_set_card_publisher_sector = _libraries['libfreefare.so'].mad_set_card_publisher_sector
mad_set_card_publisher_sector.restype = ctypes.c_int32
mad_set_card_publisher_sector.argtypes = [Mad, MifareClassicSectorNumber]
mad_get_aid = _libraries['libfreefare.so'].mad_get_aid
mad_get_aid.restype = ctypes.c_int32
mad_get_aid.argtypes = [Mad, MifareClassicSectorNumber, ctypes.POINTER(struct_mad_aid)]
mad_set_aid = _libraries['libfreefare.so'].mad_set_aid
mad_set_aid.restype = ctypes.c_int32
mad_set_aid.argtypes = [Mad, MifareClassicSectorNumber, MadAid]
mad_sector_reserved = _libraries['libfreefare.so'].mad_sector_reserved
mad_sector_reserved.restype = ctypes.c_bool
mad_sector_reserved.argtypes = [MifareClassicSectorNumber]
mad_free = _libraries['libfreefare.so'].mad_free
mad_free.restype = None
mad_free.argtypes = [Mad]
mifare_application_alloc = _libraries['libfreefare.so'].mifare_application_alloc
mifare_application_alloc.restype = ctypes.POINTER(ctypes.c_ubyte)
mifare_application_alloc.argtypes = [Mad, MadAid, size_t]
ssize_t = ctypes.c_size_t
mifare_application_read = _libraries['libfreefare.so'].mifare_application_read
mifare_application_read.restype = ssize_t
mifare_application_read.argtypes = [MifareTag, Mad, MadAid, ctypes.POINTER(None), size_t, MifareClassicKey, MifareClassicKeyType]
mifare_application_write = _libraries['libfreefare.so'].mifare_application_write
mifare_application_write.restype = ssize_t
mifare_application_write.argtypes = [MifareTag, Mad, MadAid, ctypes.POINTER(None), size_t, MifareClassicKey, MifareClassicKeyType]
mifare_application_free = _libraries['libfreefare.so'].mifare_application_free
mifare_application_free.restype = None
mifare_application_free.argtypes = [Mad, MadAid]
mifare_application_find = _libraries['libfreefare.so'].mifare_application_find
mifare_application_find.restype = ctypes.POINTER(ctypes.c_ubyte)
mifare_application_find.argtypes = [Mad, MadAid]
class struct_mifare_desfire_aid(ctypes.Structure):
    pass

MifareDESFireAID = ctypes.POINTER(struct_mifare_desfire_aid)
class struct_mifare_desfire_df(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('aid', ctypes.c_uint32),
    ('fid', ctypes.c_uint16),
    ('df_name', ctypes.c_ubyte * 16),
    ('PADDING_0', ctypes.c_ubyte * 2),
    ('df_name_len', ctypes.c_uint64),
     ]

MifareDESFireDF = struct_mifare_desfire_df
mifare_desfire_aid_new = _libraries['libfreefare.so'].mifare_desfire_aid_new
mifare_desfire_aid_new.restype = MifareDESFireAID
mifare_desfire_aid_new.argtypes = [uint32_t]
mifare_desfire_aid_new_with_mad_aid = _libraries['libfreefare.so'].mifare_desfire_aid_new_with_mad_aid
mifare_desfire_aid_new_with_mad_aid.restype = MifareDESFireAID
mifare_desfire_aid_new_with_mad_aid.argtypes = [MadAid, uint8_t]
mifare_desfire_aid_get_aid = _libraries['libfreefare.so'].mifare_desfire_aid_get_aid
mifare_desfire_aid_get_aid.restype = uint32_t
mifare_desfire_aid_get_aid.argtypes = [MifareDESFireAID]
mifare_desfire_last_pcd_error = _libraries['libfreefare.so'].mifare_desfire_last_pcd_error
mifare_desfire_last_pcd_error.restype = uint8_t
mifare_desfire_last_pcd_error.argtypes = [MifareTag]
mifare_desfire_last_picc_error = _libraries['libfreefare.so'].mifare_desfire_last_picc_error
mifare_desfire_last_picc_error.restype = uint8_t
mifare_desfire_last_picc_error.argtypes = [MifareTag]
mifare_desfire_connect = _libraries['libfreefare.so'].mifare_desfire_connect
mifare_desfire_connect.restype = ctypes.c_int32
mifare_desfire_connect.argtypes = [MifareTag]
mifare_desfire_disconnect = _libraries['libfreefare.so'].mifare_desfire_disconnect
mifare_desfire_disconnect.restype = ctypes.c_int32
mifare_desfire_disconnect.argtypes = [MifareTag]
mifare_desfire_authenticate = _libraries['libfreefare.so'].mifare_desfire_authenticate
mifare_desfire_authenticate.restype = ctypes.c_int32
mifare_desfire_authenticate.argtypes = [MifareTag, uint8_t, MifareDESFireKey]
mifare_desfire_authenticate_iso = _libraries['libfreefare.so'].mifare_desfire_authenticate_iso
mifare_desfire_authenticate_iso.restype = ctypes.c_int32
mifare_desfire_authenticate_iso.argtypes = [MifareTag, uint8_t, MifareDESFireKey]
mifare_desfire_authenticate_aes = _libraries['libfreefare.so'].mifare_desfire_authenticate_aes
mifare_desfire_authenticate_aes.restype = ctypes.c_int32
mifare_desfire_authenticate_aes.argtypes = [MifareTag, uint8_t, MifareDESFireKey]
mifare_desfire_change_key_settings = _libraries['libfreefare.so'].mifare_desfire_change_key_settings
mifare_desfire_change_key_settings.restype = ctypes.c_int32
mifare_desfire_change_key_settings.argtypes = [MifareTag, uint8_t]
mifare_desfire_get_key_settings = _libraries['libfreefare.so'].mifare_desfire_get_key_settings
mifare_desfire_get_key_settings.restype = ctypes.c_int32
mifare_desfire_get_key_settings.argtypes = [MifareTag, ctypes.POINTER(ctypes.c_ubyte), ctypes.POINTER(ctypes.c_ubyte)]
mifare_desfire_change_key = _libraries['libfreefare.so'].mifare_desfire_change_key
mifare_desfire_change_key.restype = ctypes.c_int32
mifare_desfire_change_key.argtypes = [MifareTag, uint8_t, MifareDESFireKey, MifareDESFireKey]
mifare_desfire_get_key_version = _libraries['libfreefare.so'].mifare_desfire_get_key_version
mifare_desfire_get_key_version.restype = ctypes.c_int32
mifare_desfire_get_key_version.argtypes = [MifareTag, uint8_t, ctypes.POINTER(ctypes.c_ubyte)]
mifare_desfire_create_application = _libraries['libfreefare.so'].mifare_desfire_create_application
mifare_desfire_create_application.restype = ctypes.c_int32
mifare_desfire_create_application.argtypes = [MifareTag, MifareDESFireAID, uint8_t, uint8_t]
mifare_desfire_create_application_3k3des = _libraries['libfreefare.so'].mifare_desfire_create_application_3k3des
mifare_desfire_create_application_3k3des.restype = ctypes.c_int32
mifare_desfire_create_application_3k3des.argtypes = [MifareTag, MifareDESFireAID, uint8_t, uint8_t]
mifare_desfire_create_application_aes = _libraries['libfreefare.so'].mifare_desfire_create_application_aes
mifare_desfire_create_application_aes.restype = ctypes.c_int32
mifare_desfire_create_application_aes.argtypes = [MifareTag, MifareDESFireAID, uint8_t, uint8_t]
mifare_desfire_create_application_iso = _libraries['libfreefare.so'].mifare_desfire_create_application_iso
mifare_desfire_create_application_iso.restype = ctypes.c_int32
mifare_desfire_create_application_iso.argtypes = [MifareTag, MifareDESFireAID, uint8_t, uint8_t, ctypes.c_int32, uint16_t, ctypes.POINTER(ctypes.c_ubyte), size_t]
mifare_desfire_create_application_3k3des_iso = _libraries['libfreefare.so'].mifare_desfire_create_application_3k3des_iso
mifare_desfire_create_application_3k3des_iso.restype = ctypes.c_int32
mifare_desfire_create_application_3k3des_iso.argtypes = [MifareTag, MifareDESFireAID, uint8_t, uint8_t, ctypes.c_int32, uint16_t, ctypes.POINTER(ctypes.c_ubyte), size_t]
mifare_desfire_create_application_aes_iso = _libraries['libfreefare.so'].mifare_desfire_create_application_aes_iso
mifare_desfire_create_application_aes_iso.restype = ctypes.c_int32
mifare_desfire_create_application_aes_iso.argtypes = [MifareTag, MifareDESFireAID, uint8_t, uint8_t, ctypes.c_int32, uint16_t, ctypes.POINTER(ctypes.c_ubyte), size_t]
mifare_desfire_delete_application = _libraries['libfreefare.so'].mifare_desfire_delete_application
mifare_desfire_delete_application.restype = ctypes.c_int32
mifare_desfire_delete_application.argtypes = [MifareTag, MifareDESFireAID]
mifare_desfire_get_application_ids = _libraries['libfreefare.so'].mifare_desfire_get_application_ids
mifare_desfire_get_application_ids.restype = ctypes.c_int32
mifare_desfire_get_application_ids.argtypes = [MifareTag, ctypes.POINTER(ctypes.POINTER(struct_mifare_desfire_aid)) * 0, ctypes.POINTER(ctypes.c_uint64)]
mifare_desfire_get_df_names = _libraries['libfreefare.so'].mifare_desfire_get_df_names
mifare_desfire_get_df_names.restype = ctypes.c_int32
mifare_desfire_get_df_names.argtypes = [MifareTag, ctypes.POINTER(struct_mifare_desfire_df) * 0, ctypes.POINTER(ctypes.c_uint64)]
mifare_desfire_free_application_ids = _libraries['libfreefare.so'].mifare_desfire_free_application_ids
mifare_desfire_free_application_ids.restype = None
mifare_desfire_free_application_ids.argtypes = [ctypes.POINTER(struct_mifare_desfire_aid) * 0]
mifare_desfire_select_application = _libraries['libfreefare.so'].mifare_desfire_select_application
mifare_desfire_select_application.restype = ctypes.c_int32
mifare_desfire_select_application.argtypes = [MifareTag, MifareDESFireAID]
mifare_desfire_format_picc = _libraries['libfreefare.so'].mifare_desfire_format_picc
mifare_desfire_format_picc.restype = ctypes.c_int32
mifare_desfire_format_picc.argtypes = [MifareTag]
class struct_mifare_desfire_version_info(ctypes.Structure):
    pass

mifare_desfire_get_version = _libraries['libfreefare.so'].mifare_desfire_get_version
mifare_desfire_get_version.restype = ctypes.c_int32
mifare_desfire_get_version.argtypes = [MifareTag, ctypes.POINTER(struct_mifare_desfire_version_info)]
mifare_desfire_free_mem = _libraries['libfreefare.so'].mifare_desfire_free_mem
mifare_desfire_free_mem.restype = ctypes.c_int32
mifare_desfire_free_mem.argtypes = [MifareTag, ctypes.POINTER(ctypes.c_uint32)]
mifare_desfire_set_configuration = _libraries['libfreefare.so'].mifare_desfire_set_configuration
mifare_desfire_set_configuration.restype = ctypes.c_int32
mifare_desfire_set_configuration.argtypes = [MifareTag, ctypes.c_bool, ctypes.c_bool]
mifare_desfire_set_default_key = _libraries['libfreefare.so'].mifare_desfire_set_default_key
mifare_desfire_set_default_key.restype = ctypes.c_int32
mifare_desfire_set_default_key.argtypes = [MifareTag, MifareDESFireKey]
mifare_desfire_set_ats = _libraries['libfreefare.so'].mifare_desfire_set_ats
mifare_desfire_set_ats.restype = ctypes.c_int32
mifare_desfire_set_ats.argtypes = [MifareTag, ctypes.POINTER(ctypes.c_ubyte)]
mifare_desfire_get_card_uid = _libraries['libfreefare.so'].mifare_desfire_get_card_uid
mifare_desfire_get_card_uid.restype = ctypes.c_int32
mifare_desfire_get_card_uid.argtypes = [MifareTag, ctypes.POINTER(ctypes.POINTER(ctypes.c_char))]
mifare_desfire_get_file_ids = _libraries['libfreefare.so'].mifare_desfire_get_file_ids
mifare_desfire_get_file_ids.restype = ctypes.c_int32
mifare_desfire_get_file_ids.argtypes = [MifareTag, ctypes.POINTER(ctypes.c_ubyte) * 0, ctypes.POINTER(ctypes.c_uint64)]
mifare_desfire_get_iso_file_ids = _libraries['libfreefare.so'].mifare_desfire_get_iso_file_ids
mifare_desfire_get_iso_file_ids.restype = ctypes.c_int32
mifare_desfire_get_iso_file_ids.argtypes = [MifareTag, ctypes.POINTER(ctypes.c_uint16) * 0, ctypes.POINTER(ctypes.c_uint64)]
class struct_mifare_desfire_file_settings(ctypes.Structure):
    pass

mifare_desfire_get_file_settings = _libraries['libfreefare.so'].mifare_desfire_get_file_settings
mifare_desfire_get_file_settings.restype = ctypes.c_int32
mifare_desfire_get_file_settings.argtypes = [MifareTag, uint8_t, ctypes.POINTER(struct_mifare_desfire_file_settings)]
mifare_desfire_change_file_settings = _libraries['libfreefare.so'].mifare_desfire_change_file_settings
mifare_desfire_change_file_settings.restype = ctypes.c_int32
mifare_desfire_change_file_settings.argtypes = [MifareTag, uint8_t, uint8_t, uint16_t]
mifare_desfire_create_std_data_file = _libraries['libfreefare.so'].mifare_desfire_create_std_data_file
mifare_desfire_create_std_data_file.restype = ctypes.c_int32
mifare_desfire_create_std_data_file.argtypes = [MifareTag, uint8_t, uint8_t, uint16_t, uint32_t]
mifare_desfire_create_std_data_file_iso = _libraries['libfreefare.so'].mifare_desfire_create_std_data_file_iso
mifare_desfire_create_std_data_file_iso.restype = ctypes.c_int32
mifare_desfire_create_std_data_file_iso.argtypes = [MifareTag, uint8_t, uint8_t, uint16_t, uint32_t, uint16_t]
mifare_desfire_create_backup_data_file = _libraries['libfreefare.so'].mifare_desfire_create_backup_data_file
mifare_desfire_create_backup_data_file.restype = ctypes.c_int32
mifare_desfire_create_backup_data_file.argtypes = [MifareTag, uint8_t, uint8_t, uint16_t, uint32_t]
mifare_desfire_create_backup_data_file_iso = _libraries['libfreefare.so'].mifare_desfire_create_backup_data_file_iso
mifare_desfire_create_backup_data_file_iso.restype = ctypes.c_int32
mifare_desfire_create_backup_data_file_iso.argtypes = [MifareTag, uint8_t, uint8_t, uint16_t, uint32_t, uint16_t]
mifare_desfire_create_value_file = _libraries['libfreefare.so'].mifare_desfire_create_value_file
mifare_desfire_create_value_file.restype = ctypes.c_int32
mifare_desfire_create_value_file.argtypes = [MifareTag, uint8_t, uint8_t, uint16_t, int32_t, int32_t, int32_t, uint8_t]
mifare_desfire_create_linear_record_file = _libraries['libfreefare.so'].mifare_desfire_create_linear_record_file
mifare_desfire_create_linear_record_file.restype = ctypes.c_int32
mifare_desfire_create_linear_record_file.argtypes = [MifareTag, uint8_t, uint8_t, uint16_t, uint32_t, uint32_t]
mifare_desfire_create_linear_record_file_iso = _libraries['libfreefare.so'].mifare_desfire_create_linear_record_file_iso
mifare_desfire_create_linear_record_file_iso.restype = ctypes.c_int32
mifare_desfire_create_linear_record_file_iso.argtypes = [MifareTag, uint8_t, uint8_t, uint16_t, uint32_t, uint32_t, uint16_t]
mifare_desfire_create_cyclic_record_file = _libraries['libfreefare.so'].mifare_desfire_create_cyclic_record_file
mifare_desfire_create_cyclic_record_file.restype = ctypes.c_int32
mifare_desfire_create_cyclic_record_file.argtypes = [MifareTag, uint8_t, uint8_t, uint16_t, uint32_t, uint32_t]
mifare_desfire_create_cyclic_record_file_iso = _libraries['libfreefare.so'].mifare_desfire_create_cyclic_record_file_iso
mifare_desfire_create_cyclic_record_file_iso.restype = ctypes.c_int32
mifare_desfire_create_cyclic_record_file_iso.argtypes = [MifareTag, uint8_t, uint8_t, uint16_t, uint32_t, uint32_t, uint16_t]
mifare_desfire_delete_file = _libraries['libfreefare.so'].mifare_desfire_delete_file
mifare_desfire_delete_file.restype = ctypes.c_int32
mifare_desfire_delete_file.argtypes = [MifareTag, uint8_t]
off_t = ctypes.c_int64
mifare_desfire_read_data = _libraries['libfreefare.so'].mifare_desfire_read_data
mifare_desfire_read_data.restype = ssize_t
mifare_desfire_read_data.argtypes = [MifareTag, uint8_t, off_t, size_t, ctypes.POINTER(None)]
mifare_desfire_read_data_ex = _libraries['libfreefare.so'].mifare_desfire_read_data_ex
mifare_desfire_read_data_ex.restype = ssize_t
mifare_desfire_read_data_ex.argtypes = [MifareTag, uint8_t, off_t, size_t, ctypes.POINTER(None), ctypes.c_int32]
mifare_desfire_write_data = _libraries['libfreefare.so'].mifare_desfire_write_data
mifare_desfire_write_data.restype = ssize_t
mifare_desfire_write_data.argtypes = [MifareTag, uint8_t, off_t, size_t, ctypes.POINTER(None)]
mifare_desfire_write_data_ex = _libraries['libfreefare.so'].mifare_desfire_write_data_ex
mifare_desfire_write_data_ex.restype = ssize_t
mifare_desfire_write_data_ex.argtypes = [MifareTag, uint8_t, off_t, size_t, ctypes.POINTER(None), ctypes.c_int32]
mifare_desfire_get_value = _libraries['libfreefare.so'].mifare_desfire_get_value
mifare_desfire_get_value.restype = ctypes.c_int32
mifare_desfire_get_value.argtypes = [MifareTag, uint8_t, ctypes.POINTER(ctypes.c_int32)]
mifare_desfire_get_value_ex = _libraries['libfreefare.so'].mifare_desfire_get_value_ex
mifare_desfire_get_value_ex.restype = ctypes.c_int32
mifare_desfire_get_value_ex.argtypes = [MifareTag, uint8_t, ctypes.POINTER(ctypes.c_int32), ctypes.c_int32]
mifare_desfire_credit = _libraries['libfreefare.so'].mifare_desfire_credit
mifare_desfire_credit.restype = ctypes.c_int32
mifare_desfire_credit.argtypes = [MifareTag, uint8_t, int32_t]
mifare_desfire_credit_ex = _libraries['libfreefare.so'].mifare_desfire_credit_ex
mifare_desfire_credit_ex.restype = ctypes.c_int32
mifare_desfire_credit_ex.argtypes = [MifareTag, uint8_t, int32_t, ctypes.c_int32]
mifare_desfire_debit = _libraries['libfreefare.so'].mifare_desfire_debit
mifare_desfire_debit.restype = ctypes.c_int32
mifare_desfire_debit.argtypes = [MifareTag, uint8_t, int32_t]
mifare_desfire_debit_ex = _libraries['libfreefare.so'].mifare_desfire_debit_ex
mifare_desfire_debit_ex.restype = ctypes.c_int32
mifare_desfire_debit_ex.argtypes = [MifareTag, uint8_t, int32_t, ctypes.c_int32]
mifare_desfire_limited_credit = _libraries['libfreefare.so'].mifare_desfire_limited_credit
mifare_desfire_limited_credit.restype = ctypes.c_int32
mifare_desfire_limited_credit.argtypes = [MifareTag, uint8_t, int32_t]
mifare_desfire_limited_credit_ex = _libraries['libfreefare.so'].mifare_desfire_limited_credit_ex
mifare_desfire_limited_credit_ex.restype = ctypes.c_int32
mifare_desfire_limited_credit_ex.argtypes = [MifareTag, uint8_t, int32_t, ctypes.c_int32]
mifare_desfire_write_record = _libraries['libfreefare.so'].mifare_desfire_write_record
mifare_desfire_write_record.restype = ssize_t
mifare_desfire_write_record.argtypes = [MifareTag, uint8_t, off_t, size_t, ctypes.POINTER(None)]
mifare_desfire_write_record_ex = _libraries['libfreefare.so'].mifare_desfire_write_record_ex
mifare_desfire_write_record_ex.restype = ssize_t
mifare_desfire_write_record_ex.argtypes = [MifareTag, uint8_t, off_t, size_t, ctypes.POINTER(None), ctypes.c_int32]
mifare_desfire_read_records = _libraries['libfreefare.so'].mifare_desfire_read_records
mifare_desfire_read_records.restype = ssize_t
mifare_desfire_read_records.argtypes = [MifareTag, uint8_t, off_t, size_t, ctypes.POINTER(None)]
mifare_desfire_read_records_ex = _libraries['libfreefare.so'].mifare_desfire_read_records_ex
mifare_desfire_read_records_ex.restype = ssize_t
mifare_desfire_read_records_ex.argtypes = [MifareTag, uint8_t, off_t, size_t, ctypes.POINTER(None), ctypes.c_int32]
mifare_desfire_clear_record_file = _libraries['libfreefare.so'].mifare_desfire_clear_record_file
mifare_desfire_clear_record_file.restype = ctypes.c_int32
mifare_desfire_clear_record_file.argtypes = [MifareTag, uint8_t]
mifare_desfire_commit_transaction = _libraries['libfreefare.so'].mifare_desfire_commit_transaction
mifare_desfire_commit_transaction.restype = ctypes.c_int32
mifare_desfire_commit_transaction.argtypes = [MifareTag]
mifare_desfire_abort_transaction = _libraries['libfreefare.so'].mifare_desfire_abort_transaction
mifare_desfire_abort_transaction.restype = ctypes.c_int32
mifare_desfire_abort_transaction.argtypes = [MifareTag]
mifare_desfire_des_key_new = _libraries['libfreefare.so'].mifare_desfire_des_key_new
mifare_desfire_des_key_new.restype = MifareDESFireKey
mifare_desfire_des_key_new.argtypes = [ctypes.c_ubyte * 8]
mifare_desfire_3des_key_new = _libraries['libfreefare.so'].mifare_desfire_3des_key_new
mifare_desfire_3des_key_new.restype = MifareDESFireKey
mifare_desfire_3des_key_new.argtypes = [ctypes.c_ubyte * 16]
mifare_desfire_des_key_new_with_version = _libraries['libfreefare.so'].mifare_desfire_des_key_new_with_version
mifare_desfire_des_key_new_with_version.restype = MifareDESFireKey
mifare_desfire_des_key_new_with_version.argtypes = [ctypes.c_ubyte * 8]
mifare_desfire_3des_key_new_with_version = _libraries['libfreefare.so'].mifare_desfire_3des_key_new_with_version
mifare_desfire_3des_key_new_with_version.restype = MifareDESFireKey
mifare_desfire_3des_key_new_with_version.argtypes = [ctypes.c_ubyte * 16]
mifare_desfire_3k3des_key_new = _libraries['libfreefare.so'].mifare_desfire_3k3des_key_new
mifare_desfire_3k3des_key_new.restype = MifareDESFireKey
mifare_desfire_3k3des_key_new.argtypes = [ctypes.c_ubyte * 24]
mifare_desfire_3k3des_key_new_with_version = _libraries['libfreefare.so'].mifare_desfire_3k3des_key_new_with_version
mifare_desfire_3k3des_key_new_with_version.restype = MifareDESFireKey
mifare_desfire_3k3des_key_new_with_version.argtypes = [ctypes.c_ubyte * 24]
mifare_desfire_aes_key_new = _libraries['libfreefare.so'].mifare_desfire_aes_key_new
mifare_desfire_aes_key_new.restype = MifareDESFireKey
mifare_desfire_aes_key_new.argtypes = [ctypes.c_ubyte * 16]
mifare_desfire_aes_key_new_with_version = _libraries['libfreefare.so'].mifare_desfire_aes_key_new_with_version
mifare_desfire_aes_key_new_with_version.restype = MifareDESFireKey
mifare_desfire_aes_key_new_with_version.argtypes = [ctypes.c_ubyte * 16, uint8_t]
mifare_desfire_key_get_version = _libraries['libfreefare.so'].mifare_desfire_key_get_version
mifare_desfire_key_get_version.restype = uint8_t
mifare_desfire_key_get_version.argtypes = [MifareDESFireKey]
mifare_desfire_key_set_version = _libraries['libfreefare.so'].mifare_desfire_key_set_version
mifare_desfire_key_set_version.restype = None
mifare_desfire_key_set_version.argtypes = [MifareDESFireKey, uint8_t]
mifare_desfire_key_free = _libraries['libfreefare.so'].mifare_desfire_key_free
mifare_desfire_key_free.restype = None
mifare_desfire_key_free.argtypes = [MifareDESFireKey]
tlv_encode = _libraries['libfreefare.so'].tlv_encode
tlv_encode.restype = ctypes.POINTER(ctypes.c_ubyte)
tlv_encode.argtypes = [uint8_t, ctypes.POINTER(ctypes.c_ubyte), uint16_t, ctypes.POINTER(ctypes.c_uint64)]
tlv_decode = _libraries['libfreefare.so'].tlv_decode
tlv_decode.restype = ctypes.POINTER(ctypes.c_ubyte)
tlv_decode.argtypes = [ctypes.POINTER(ctypes.c_ubyte), ctypes.POINTER(ctypes.c_ubyte), ctypes.POINTER(ctypes.c_uint16)]
tlv_record_length = _libraries['libfreefare.so'].tlv_record_length
tlv_record_length.restype = size_t
tlv_record_length.argtypes = [ctypes.POINTER(ctypes.c_ubyte), ctypes.POINTER(ctypes.c_uint64), ctypes.POINTER(ctypes.c_uint64)]
tlv_append = _libraries['libfreefare.so'].tlv_append
tlv_append.restype = ctypes.POINTER(ctypes.c_ubyte)
tlv_append.argtypes = [ctypes.POINTER(ctypes.c_ubyte), ctypes.POINTER(ctypes.c_ubyte)]
class struct_nfc_context(ctypes.Structure):
    pass

class struct_nfc_user_defined_device(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('name', ctypes.c_char * 256),
    ('connstring', ctypes.c_char * 1024),
    ('optional', ctypes.c_bool),
     ]

struct_nfc_context._pack_ = True # source:False
struct_nfc_context._fields_ = [
    ('allow_autoscan', ctypes.c_bool),
    ('allow_intrusive_scan', ctypes.c_bool),
    ('PADDING_0', ctypes.c_ubyte * 2),
    ('log_level', ctypes.c_uint32),
    ('user_defined_devices', struct_nfc_user_defined_device * 4),
    ('user_defined_device_count', ctypes.c_uint32),
]

nfc_context = struct_nfc_context
class struct_nfc_driver(ctypes.Structure):
    pass

struct_nfc_device._pack_ = True # source:False
struct_nfc_device._fields_ = [
    ('context', ctypes.POINTER(struct_nfc_context)),
    ('driver', ctypes.POINTER(struct_nfc_driver)),
    ('driver_data', ctypes.POINTER(None)),
    ('chip_data', ctypes.POINTER(None)),
    ('name', ctypes.c_char * 256),
    ('connstring', ctypes.c_char * 1024),
    ('bCrc', ctypes.c_bool),
    ('bPar', ctypes.c_bool),
    ('bEasyFraming', ctypes.c_bool),
    ('bInfiniteSelect', ctypes.c_bool),
    ('bAutoIso14443_4', ctypes.c_bool),
    ('btSupportByte', ctypes.c_ubyte),
    ('PADDING_0', ctypes.c_ubyte * 2),
    ('last_error', ctypes.c_int32),
    ('PADDING_1', ctypes.c_ubyte * 4),
]

nfc_device = struct_nfc_device
nfc_driver = struct_nfc_driver
nfc_connstring = ctypes.c_char * 1024

# values for enumeration 'c__EA_nfc_property'
c__EA_nfc_property__enumvalues = {
    0: 'NP_TIMEOUT_COMMAND',
    1: 'NP_TIMEOUT_ATR',
    2: 'NP_TIMEOUT_COM',
    3: 'NP_HANDLE_CRC',
    4: 'NP_HANDLE_PARITY',
    5: 'NP_ACTIVATE_FIELD',
    6: 'NP_ACTIVATE_CRYPTO1',
    7: 'NP_INFINITE_SELECT',
    8: 'NP_ACCEPT_INVALID_FRAMES',
    9: 'NP_ACCEPT_MULTIPLE_FRAMES',
    10: 'NP_AUTO_ISO14443_4',
    11: 'NP_EASY_FRAMING',
    12: 'NP_FORCE_ISO14443_A',
    13: 'NP_FORCE_ISO14443_B',
    14: 'NP_FORCE_SPEED_106',
}
NP_TIMEOUT_COMMAND = 0
NP_TIMEOUT_ATR = 1
NP_TIMEOUT_COM = 2
NP_HANDLE_CRC = 3
NP_HANDLE_PARITY = 4
NP_ACTIVATE_FIELD = 5
NP_ACTIVATE_CRYPTO1 = 6
NP_INFINITE_SELECT = 7
NP_ACCEPT_INVALID_FRAMES = 8
NP_ACCEPT_MULTIPLE_FRAMES = 9
NP_AUTO_ISO14443_4 = 10
NP_EASY_FRAMING = 11
NP_FORCE_ISO14443_A = 12
NP_FORCE_ISO14443_B = 13
NP_FORCE_SPEED_106 = 14
c__EA_nfc_property = ctypes.c_int # enum
nfc_property = c__EA_nfc_property
nfc_property__enumvalues = c__EA_nfc_property__enumvalues

# values for enumeration 'c__EA_nfc_dep_mode'
c__EA_nfc_dep_mode__enumvalues = {
    0: 'NDM_UNDEFINED',
    1: 'NDM_PASSIVE',
    2: 'NDM_ACTIVE',
}
NDM_UNDEFINED = 0
NDM_PASSIVE = 1
NDM_ACTIVE = 2
c__EA_nfc_dep_mode = ctypes.c_int # enum
nfc_dep_mode = c__EA_nfc_dep_mode
nfc_dep_mode__enumvalues = c__EA_nfc_dep_mode__enumvalues
class struct_c__SA_nfc_dep_info(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('abtNFCID3', ctypes.c_ubyte * 10),
    ('btDID', ctypes.c_ubyte),
    ('btBS', ctypes.c_ubyte),
    ('btBR', ctypes.c_ubyte),
    ('btTO', ctypes.c_ubyte),
    ('btPP', ctypes.c_ubyte),
    ('abtGB', ctypes.c_ubyte * 48),
    ('szGB', ctypes.c_uint64),
    ('ndm', nfc_dep_mode),
     ]

nfc_dep_info = struct_c__SA_nfc_dep_info
class struct_c__SA_nfc_felica_info(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('szLen', ctypes.c_uint64),
    ('btResCode', ctypes.c_ubyte),
    ('abtId', ctypes.c_ubyte * 8),
    ('abtPad', ctypes.c_ubyte * 8),
    ('abtSysCode', ctypes.c_ubyte * 2),
     ]

nfc_felica_info = struct_c__SA_nfc_felica_info
class struct_c__SA_nfc_iso14443b_info(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('abtPupi', ctypes.c_ubyte * 4),
    ('abtApplicationData', ctypes.c_ubyte * 4),
    ('abtProtocolInfo', ctypes.c_ubyte * 3),
    ('ui8CardIdentifier', ctypes.c_ubyte),
     ]

nfc_iso14443b_info = struct_c__SA_nfc_iso14443b_info
class struct_c__SA_nfc_iso14443bi_info(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('abtDIV', ctypes.c_ubyte * 4),
    ('btVerLog', ctypes.c_ubyte),
    ('btConfig', ctypes.c_ubyte),
    ('szAtrLen', ctypes.c_uint64),
    ('abtAtr', ctypes.c_ubyte * 33),
     ]

nfc_iso14443bi_info = struct_c__SA_nfc_iso14443bi_info
class struct_c__SA_nfc_iso14443b2sr_info(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('abtUID', ctypes.c_ubyte * 8),
     ]

nfc_iso14443b2sr_info = struct_c__SA_nfc_iso14443b2sr_info
class struct_c__SA_nfc_iso14443b2ct_info(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('abtUID', ctypes.c_ubyte * 4),
    ('btProdCode', ctypes.c_ubyte),
    ('btFabCode', ctypes.c_ubyte),
     ]

nfc_iso14443b2ct_info = struct_c__SA_nfc_iso14443b2ct_info
class struct_c__SA_nfc_jewel_info(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('btSensRes', ctypes.c_ubyte * 2),
    ('btId', ctypes.c_ubyte * 4),
     ]

nfc_jewel_info = struct_c__SA_nfc_jewel_info
class union_c__UA_nfc_target_info(ctypes.Union):
    _pack_ = True # source:False
    _fields_ = [
    ('nai', nfc_iso14443a_info),
    ('nfi', nfc_felica_info),
    ('nbi', nfc_iso14443b_info),
    ('nii', nfc_iso14443bi_info),
    ('nsi', nfc_iso14443b2sr_info),
    ('nci', nfc_iso14443b2ct_info),
    ('nji', nfc_jewel_info),
    ('ndi', nfc_dep_info),
    ('PADDING_0', ctypes.c_ubyte * 208),
     ]

nfc_target_info = union_c__UA_nfc_target_info

# values for enumeration 'c__EA_nfc_baud_rate'
c__EA_nfc_baud_rate__enumvalues = {
    0: 'NBR_UNDEFINED',
    1: 'NBR_106',
    2: 'NBR_212',
    3: 'NBR_424',
    4: 'NBR_847',
}
NBR_UNDEFINED = 0
NBR_106 = 1
NBR_212 = 2
NBR_424 = 3
NBR_847 = 4
c__EA_nfc_baud_rate = ctypes.c_int # enum
nfc_baud_rate = c__EA_nfc_baud_rate
nfc_baud_rate__enumvalues = c__EA_nfc_baud_rate__enumvalues

# values for enumeration 'c__EA_nfc_modulation_type'
c__EA_nfc_modulation_type__enumvalues = {
    1: 'NMT_ISO14443A',
    2: 'NMT_JEWEL',
    3: 'NMT_ISO14443B',
    4: 'NMT_ISO14443BI',
    5: 'NMT_ISO14443B2SR',
    6: 'NMT_ISO14443B2CT',
    7: 'NMT_FELICA',
    8: 'NMT_DEP',
}
NMT_ISO14443A = 1
NMT_JEWEL = 2
NMT_ISO14443B = 3
NMT_ISO14443BI = 4
NMT_ISO14443B2SR = 5
NMT_ISO14443B2CT = 6
NMT_FELICA = 7
NMT_DEP = 8
c__EA_nfc_modulation_type = ctypes.c_int # enum
nfc_modulation_type = c__EA_nfc_modulation_type
nfc_modulation_type__enumvalues = c__EA_nfc_modulation_type__enumvalues

# values for enumeration 'c__EA_nfc_mode'
c__EA_nfc_mode__enumvalues = {
    0: 'N_TARGET',
    1: 'N_INITIATOR',
}
N_TARGET = 0
N_INITIATOR = 1
c__EA_nfc_mode = ctypes.c_int # enum
nfc_mode = c__EA_nfc_mode
nfc_mode__enumvalues = c__EA_nfc_mode__enumvalues
class struct_c__SA_nfc_modulation(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('nmt', nfc_modulation_type),
    ('nbr', nfc_baud_rate),
     ]

nfc_modulation = struct_c__SA_nfc_modulation
class struct_c__SA_nfc_target(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('nti', nfc_target_info),
    ('nm', nfc_modulation),
     ]

nfc_target = struct_c__SA_nfc_target
nfc_init = _libraries['libfreefare.so'].nfc_init
nfc_init.restype = None
nfc_init.argtypes = [ctypes.POINTER(ctypes.POINTER(struct_nfc_context))]
nfc_exit = _libraries['libfreefare.so'].nfc_exit
nfc_exit.restype = None
nfc_exit.argtypes = [ctypes.POINTER(struct_nfc_context)]
nfc_register_driver = _libraries['libfreefare.so'].nfc_register_driver
nfc_register_driver.restype = ctypes.c_int32
nfc_register_driver.argtypes = [ctypes.POINTER(struct_nfc_driver)]
nfc_open = _libraries['libfreefare.so'].nfc_open
nfc_open.restype = ctypes.POINTER(struct_nfc_device)
nfc_open.argtypes = [ctypes.POINTER(struct_nfc_context), nfc_connstring]
nfc_close = _libraries['libfreefare.so'].nfc_close
nfc_close.restype = None
nfc_close.argtypes = [ctypes.POINTER(struct_nfc_device)]
nfc_abort_command = _libraries['libfreefare.so'].nfc_abort_command
nfc_abort_command.restype = ctypes.c_int32
nfc_abort_command.argtypes = [ctypes.POINTER(struct_nfc_device)]
nfc_list_devices = _libraries['libfreefare.so'].nfc_list_devices
nfc_list_devices.restype = size_t
nfc_list_devices.argtypes = [ctypes.POINTER(struct_nfc_context), ctypes.c_char * 1024 * 0, size_t]
nfc_idle = _libraries['libfreefare.so'].nfc_idle
nfc_idle.restype = ctypes.c_int32
nfc_idle.argtypes = [ctypes.POINTER(struct_nfc_device)]
nfc_initiator_init = _libraries['libfreefare.so'].nfc_initiator_init
nfc_initiator_init.restype = ctypes.c_int32
nfc_initiator_init.argtypes = [ctypes.POINTER(struct_nfc_device)]
nfc_initiator_init_secure_element = _libraries['libfreefare.so'].nfc_initiator_init_secure_element
nfc_initiator_init_secure_element.restype = ctypes.c_int32
nfc_initiator_init_secure_element.argtypes = [ctypes.POINTER(struct_nfc_device)]
nfc_initiator_select_passive_target = _libraries['libfreefare.so'].nfc_initiator_select_passive_target
nfc_initiator_select_passive_target.restype = ctypes.c_int32
nfc_initiator_select_passive_target.argtypes = [ctypes.POINTER(struct_nfc_device), nfc_modulation, ctypes.POINTER(ctypes.c_ubyte), size_t, ctypes.POINTER(struct_c__SA_nfc_target)]
nfc_initiator_list_passive_targets = _libraries['libfreefare.so'].nfc_initiator_list_passive_targets
nfc_initiator_list_passive_targets.restype = ctypes.c_int32
nfc_initiator_list_passive_targets.argtypes = [ctypes.POINTER(struct_nfc_device), nfc_modulation, struct_c__SA_nfc_target * 0, size_t]
nfc_initiator_poll_target = _libraries['libfreefare.so'].nfc_initiator_poll_target
nfc_initiator_poll_target.restype = ctypes.c_int32
nfc_initiator_poll_target.argtypes = [ctypes.POINTER(struct_nfc_device), ctypes.POINTER(struct_c__SA_nfc_modulation), size_t, uint8_t, uint8_t, ctypes.POINTER(struct_c__SA_nfc_target)]
nfc_initiator_select_dep_target = _libraries['libfreefare.so'].nfc_initiator_select_dep_target
nfc_initiator_select_dep_target.restype = ctypes.c_int32
nfc_initiator_select_dep_target.argtypes = [ctypes.POINTER(struct_nfc_device), nfc_dep_mode, nfc_baud_rate, ctypes.POINTER(struct_c__SA_nfc_dep_info), ctypes.POINTER(struct_c__SA_nfc_target), ctypes.c_int32]
nfc_initiator_poll_dep_target = _libraries['libfreefare.so'].nfc_initiator_poll_dep_target
nfc_initiator_poll_dep_target.restype = ctypes.c_int32
nfc_initiator_poll_dep_target.argtypes = [ctypes.POINTER(struct_nfc_device), nfc_dep_mode, nfc_baud_rate, ctypes.POINTER(struct_c__SA_nfc_dep_info), ctypes.POINTER(struct_c__SA_nfc_target), ctypes.c_int32]
nfc_initiator_deselect_target = _libraries['libfreefare.so'].nfc_initiator_deselect_target
nfc_initiator_deselect_target.restype = ctypes.c_int32
nfc_initiator_deselect_target.argtypes = [ctypes.POINTER(struct_nfc_device)]
nfc_initiator_transceive_bytes = _libraries['libfreefare.so'].nfc_initiator_transceive_bytes
nfc_initiator_transceive_bytes.restype = ctypes.c_int32
nfc_initiator_transceive_bytes.argtypes = [ctypes.POINTER(struct_nfc_device), ctypes.POINTER(ctypes.c_ubyte), size_t, ctypes.POINTER(ctypes.c_ubyte), size_t, ctypes.c_int32]
nfc_initiator_transceive_bits = _libraries['libfreefare.so'].nfc_initiator_transceive_bits
nfc_initiator_transceive_bits.restype = ctypes.c_int32
nfc_initiator_transceive_bits.argtypes = [ctypes.POINTER(struct_nfc_device), ctypes.POINTER(ctypes.c_ubyte), size_t, ctypes.POINTER(ctypes.c_ubyte), ctypes.POINTER(ctypes.c_ubyte), size_t, ctypes.POINTER(ctypes.c_ubyte)]
nfc_initiator_transceive_bytes_timed = _libraries['libfreefare.so'].nfc_initiator_transceive_bytes_timed
nfc_initiator_transceive_bytes_timed.restype = ctypes.c_int32
nfc_initiator_transceive_bytes_timed.argtypes = [ctypes.POINTER(struct_nfc_device), ctypes.POINTER(ctypes.c_ubyte), size_t, ctypes.POINTER(ctypes.c_ubyte), size_t, ctypes.POINTER(ctypes.c_uint32)]
nfc_initiator_transceive_bits_timed = _libraries['libfreefare.so'].nfc_initiator_transceive_bits_timed
nfc_initiator_transceive_bits_timed.restype = ctypes.c_int32
nfc_initiator_transceive_bits_timed.argtypes = [ctypes.POINTER(struct_nfc_device), ctypes.POINTER(ctypes.c_ubyte), size_t, ctypes.POINTER(ctypes.c_ubyte), ctypes.POINTER(ctypes.c_ubyte), size_t, ctypes.POINTER(ctypes.c_ubyte), ctypes.POINTER(ctypes.c_uint32)]
nfc_initiator_target_is_present = _libraries['libfreefare.so'].nfc_initiator_target_is_present
nfc_initiator_target_is_present.restype = ctypes.c_int32
nfc_initiator_target_is_present.argtypes = [ctypes.POINTER(struct_nfc_device), ctypes.POINTER(struct_c__SA_nfc_target)]
nfc_target_init = _libraries['libfreefare.so'].nfc_target_init
nfc_target_init.restype = ctypes.c_int32
nfc_target_init.argtypes = [ctypes.POINTER(struct_nfc_device), ctypes.POINTER(struct_c__SA_nfc_target), ctypes.POINTER(ctypes.c_ubyte), size_t, ctypes.c_int32]
nfc_target_send_bytes = _libraries['libfreefare.so'].nfc_target_send_bytes
nfc_target_send_bytes.restype = ctypes.c_int32
nfc_target_send_bytes.argtypes = [ctypes.POINTER(struct_nfc_device), ctypes.POINTER(ctypes.c_ubyte), size_t, ctypes.c_int32]
nfc_target_receive_bytes = _libraries['libfreefare.so'].nfc_target_receive_bytes
nfc_target_receive_bytes.restype = ctypes.c_int32
nfc_target_receive_bytes.argtypes = [ctypes.POINTER(struct_nfc_device), ctypes.POINTER(ctypes.c_ubyte), size_t, ctypes.c_int32]
nfc_target_send_bits = _libraries['libfreefare.so'].nfc_target_send_bits
nfc_target_send_bits.restype = ctypes.c_int32
nfc_target_send_bits.argtypes = [ctypes.POINTER(struct_nfc_device), ctypes.POINTER(ctypes.c_ubyte), size_t, ctypes.POINTER(ctypes.c_ubyte)]
nfc_target_receive_bits = _libraries['libfreefare.so'].nfc_target_receive_bits
nfc_target_receive_bits.restype = ctypes.c_int32
nfc_target_receive_bits.argtypes = [ctypes.POINTER(struct_nfc_device), ctypes.POINTER(ctypes.c_ubyte), size_t, ctypes.POINTER(ctypes.c_ubyte)]
nfc_strerror = _libraries['libfreefare.so'].nfc_strerror
nfc_strerror.restype = ctypes.POINTER(ctypes.c_char)
nfc_strerror.argtypes = [ctypes.POINTER(struct_nfc_device)]
nfc_strerror_r = _libraries['libfreefare.so'].nfc_strerror_r
nfc_strerror_r.restype = ctypes.c_int32
nfc_strerror_r.argtypes = [ctypes.POINTER(struct_nfc_device), ctypes.POINTER(ctypes.c_char), size_t]
nfc_perror = _libraries['libfreefare.so'].nfc_perror
nfc_perror.restype = None
nfc_perror.argtypes = [ctypes.POINTER(struct_nfc_device), ctypes.POINTER(ctypes.c_char)]
nfc_device_get_last_error = _libraries['libfreefare.so'].nfc_device_get_last_error
nfc_device_get_last_error.restype = ctypes.c_int32
nfc_device_get_last_error.argtypes = [ctypes.POINTER(struct_nfc_device)]
nfc_device_get_name = _libraries['libfreefare.so'].nfc_device_get_name
nfc_device_get_name.restype = ctypes.POINTER(ctypes.c_char)
nfc_device_get_name.argtypes = [ctypes.POINTER(struct_nfc_device)]
nfc_device_get_connstring = _libraries['libfreefare.so'].nfc_device_get_connstring
nfc_device_get_connstring.restype = ctypes.POINTER(ctypes.c_char)
nfc_device_get_connstring.argtypes = [ctypes.POINTER(struct_nfc_device)]
nfc_device_get_supported_modulation = _libraries['libfreefare.so'].nfc_device_get_supported_modulation
nfc_device_get_supported_modulation.restype = ctypes.c_int32
nfc_device_get_supported_modulation.argtypes = [ctypes.POINTER(struct_nfc_device), nfc_mode, ctypes.POINTER(ctypes.POINTER(c__EA_nfc_modulation_type))]
nfc_device_get_supported_baud_rate = _libraries['libfreefare.so'].nfc_device_get_supported_baud_rate
nfc_device_get_supported_baud_rate.restype = ctypes.c_int32
nfc_device_get_supported_baud_rate.argtypes = [ctypes.POINTER(struct_nfc_device), nfc_modulation_type, ctypes.POINTER(ctypes.POINTER(c__EA_nfc_baud_rate))]
nfc_device_set_property_int = _libraries['libfreefare.so'].nfc_device_set_property_int
nfc_device_set_property_int.restype = ctypes.c_int32
nfc_device_set_property_int.argtypes = [ctypes.POINTER(struct_nfc_device), nfc_property, ctypes.c_int32]
nfc_device_set_property_bool = _libraries['libfreefare.so'].nfc_device_set_property_bool
nfc_device_set_property_bool.restype = ctypes.c_int32
nfc_device_set_property_bool.argtypes = [ctypes.POINTER(struct_nfc_device), nfc_property, ctypes.c_bool]
iso14443a_crc = _libraries['libfreefare.so'].iso14443a_crc
iso14443a_crc.restype = None
iso14443a_crc.argtypes = [ctypes.POINTER(ctypes.c_ubyte), size_t, ctypes.POINTER(ctypes.c_ubyte)]
iso14443a_crc_append = _libraries['libfreefare.so'].iso14443a_crc_append
iso14443a_crc_append.restype = None
iso14443a_crc_append.argtypes = [ctypes.POINTER(ctypes.c_ubyte), size_t]
iso14443a_locate_historical_bytes = _libraries['libfreefare.so'].iso14443a_locate_historical_bytes
iso14443a_locate_historical_bytes.restype = ctypes.POINTER(ctypes.c_ubyte)
iso14443a_locate_historical_bytes.argtypes = [ctypes.POINTER(ctypes.c_ubyte), size_t, ctypes.POINTER(ctypes.c_uint64)]
nfc_free = _libraries['libfreefare.so'].nfc_free
nfc_free.restype = None
nfc_free.argtypes = [ctypes.POINTER(None)]
nfc_version = _libraries['libfreefare.so'].nfc_version
nfc_version.restype = ctypes.POINTER(ctypes.c_char)
nfc_version.argtypes = []
nfc_device_get_information_about = _libraries['libfreefare.so'].nfc_device_get_information_about
nfc_device_get_information_about.restype = ctypes.c_int32
nfc_device_get_information_about.argtypes = [ctypes.POINTER(struct_nfc_device), ctypes.POINTER(ctypes.POINTER(ctypes.c_char))]
str_nfc_modulation_type = _libraries['libfreefare.so'].str_nfc_modulation_type
str_nfc_modulation_type.restype = ctypes.POINTER(ctypes.c_char)
str_nfc_modulation_type.argtypes = [nfc_modulation_type]
str_nfc_baud_rate = _libraries['libfreefare.so'].str_nfc_baud_rate
str_nfc_baud_rate.restype = ctypes.POINTER(ctypes.c_char)
str_nfc_baud_rate.argtypes = [nfc_baud_rate]
str_nfc_target = _libraries['libfreefare.so'].str_nfc_target
str_nfc_target.restype = ctypes.c_int32
str_nfc_target.argtypes = [ctypes.POINTER(ctypes.POINTER(ctypes.c_char)), ctypes.POINTER(struct_c__SA_nfc_target), ctypes.c_bool]
freefare_get_tag_type = _libraries['libfreefare.so'].freefare_get_tag_type
freefare_get_tag_type.restype = ctypes.c_int32
freefare_get_tag_type.argtypes = [MifareTag]
mifare_desfire_session_key_new = _libraries['libfreefare.so'].mifare_desfire_session_key_new
mifare_desfire_session_key_new.restype = MifareDESFireKey
mifare_desfire_session_key_new.argtypes = [ctypes.c_ubyte * 8, ctypes.c_ubyte * 8, MifareDESFireKey]
mifare_desfire_error_lookup = _libraries['libfreefare.so'].mifare_desfire_error_lookup
mifare_desfire_error_lookup.restype = ctypes.POINTER(ctypes.c_char)
mifare_desfire_error_lookup.argtypes = [uint8_t]

# values for enumeration 'c__EA_mifare_cmd'
c__EA_mifare_cmd__enumvalues = {
    96: 'MC_AUTH_A',
    97: 'MC_AUTH_B',
    48: 'MC_READ',
    160: 'MC_WRITE',
    176: 'MC_TRANSFER',
    192: 'MC_DECREMENT',
    193: 'MC_INCREMENT',
    194: 'MC_STORE',
}
MC_AUTH_A = 96
MC_AUTH_B = 97
MC_READ = 48
MC_WRITE = 160
MC_TRANSFER = 176
MC_DECREMENT = 192
MC_INCREMENT = 193
MC_STORE = 194
c__EA_mifare_cmd = ctypes.c_int # enum
mifare_cmd = c__EA_mifare_cmd
mifare_cmd__enumvalues = c__EA_mifare_cmd__enumvalues
class union_c__UA_mifare_param(ctypes.Union):
    pass

class struct_mifare_param_auth(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('abtKey', ctypes.c_ubyte * 6),
    ('abtAuthUid', ctypes.c_ubyte * 4),
     ]

class struct_mifare_param_value(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('abtValue', ctypes.c_ubyte * 4),
     ]

class struct_mifare_param_data(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('abtData', ctypes.c_ubyte * 16),
     ]

union_c__UA_mifare_param._pack_ = True # source:False
union_c__UA_mifare_param._fields_ = [
    ('mpa', struct_mifare_param_auth),
    ('mpd', struct_mifare_param_data),
    ('mpv', struct_mifare_param_value),
    ('PADDING_0', ctypes.c_ubyte * 12),
]

mifare_param = union_c__UA_mifare_param
class struct_c__SA_mifare_classic_block_manufacturer(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('abtUID', ctypes.c_ubyte * 4),
    ('btBCC', ctypes.c_ubyte),
    ('btSAK', ctypes.c_ubyte),
    ('abtATQA', ctypes.c_ubyte * 2),
    ('abtManufacturer', ctypes.c_ubyte * 8),
     ]

mifare_classic_block_manufacturer = struct_c__SA_mifare_classic_block_manufacturer
class struct_c__SA_mifare_classic_block_data(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('abtData', ctypes.c_ubyte * 16),
     ]

mifare_classic_block_data = struct_c__SA_mifare_classic_block_data
class struct_c__SA_mifare_classic_block_trailer(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('abtKeyA', ctypes.c_ubyte * 6),
    ('abtAccessBits', ctypes.c_ubyte * 4),
    ('abtKeyB', ctypes.c_ubyte * 6),
     ]

mifare_classic_block_trailer = struct_c__SA_mifare_classic_block_trailer
class union_c__UA_mifare_classic_block(ctypes.Union):
    _pack_ = True # source:False
    _fields_ = [
    ('mbm', mifare_classic_block_manufacturer),
    ('mbd', mifare_classic_block_data),
    ('mbt', mifare_classic_block_trailer),
     ]

mifare_classic_block = union_c__UA_mifare_classic_block
class struct_c__SA_mifare_classic_tag(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('amb', union_c__UA_mifare_classic_block * 256),
     ]

mifare_classic_tag = struct_c__SA_mifare_classic_tag
class struct_c__SA_mifareul_block_manufacturer(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('sn0', ctypes.c_ubyte * 3),
    ('btBCC0', ctypes.c_ubyte),
    ('sn1', ctypes.c_ubyte * 4),
    ('btBCC1', ctypes.c_ubyte),
    ('internal', ctypes.c_ubyte),
    ('lock', ctypes.c_ubyte * 2),
    ('otp', ctypes.c_ubyte * 4),
     ]

mifareul_block_manufacturer = struct_c__SA_mifareul_block_manufacturer
class struct_c__SA_mifareul_block_data(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('abtData', ctypes.c_ubyte * 16),
     ]

mifareul_block_data = struct_c__SA_mifareul_block_data
class union_c__UA_mifareul_block(ctypes.Union):
    _pack_ = True # source:False
    _fields_ = [
    ('mbm', mifareul_block_manufacturer),
    ('mbd', mifareul_block_data),
     ]

mifareul_block = union_c__UA_mifareul_block
class struct_c__SA_mifareul_tag(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('amb', union_c__UA_mifareul_block * 4),
     ]

mifareul_tag = struct_c__SA_mifareul_tag
struct_mifare_desfire_key._pack_ = True # source:False
struct_mifare_desfire_key._fields_ = [
    ('PADDING_0', ctypes.c_ubyte),
]

class struct_supported_tag(ctypes.Structure):
    pass


# values for enumeration 'mifare_tag_type'
mifare_tag_type__enumvalues = {
    0: 'ULTRALIGHT',
    1: 'ULTRALIGHT_C',
    2: 'CLASSIC_1K',
    3: 'CLASSIC_4K',
    4: 'DESFIRE',
}
ULTRALIGHT = 0
ULTRALIGHT_C = 1
CLASSIC_1K = 2
CLASSIC_4K = 3
DESFIRE = 4
mifare_tag_type = ctypes.c_int # enum
struct_supported_tag._pack_ = True # source:False
struct_supported_tag._fields_ = [
    ('type', mifare_tag_type),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('friendly_name', ctypes.POINTER(ctypes.c_char)),
    ('SAK', ctypes.c_ubyte),
    ('ATS_min_length', ctypes.c_ubyte),
    ('ATS_compare_length', ctypes.c_ubyte),
    ('ATS', ctypes.c_ubyte * 5),
    ('check_tag_on_reader', ctypes.POINTER(ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.POINTER(struct_nfc_device), struct_c__SA_nfc_iso14443a_info))),
]

struct_mifare_tag._pack_ = True # source:False
struct_mifare_tag._fields_ = [
    ('device', ctypes.POINTER(struct_nfc_device)),
    ('info', nfc_iso14443a_info),
    ('PADDING_0', ctypes.c_ubyte * 5),
    ('tag_info', ctypes.POINTER(struct_supported_tag)),
    ('active', ctypes.c_int32),
    ('PADDING_1', ctypes.c_ubyte * 4),
]

struct_mifare_desfire_aid._pack_ = True # source:False
struct_mifare_desfire_aid._fields_ = [
    ('data', ctypes.c_ubyte * 3),
]

class struct_mifare_desfire_version_info_0(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('vendor_id', ctypes.c_ubyte),
    ('type', ctypes.c_ubyte),
    ('subtype', ctypes.c_ubyte),
    ('version_major', ctypes.c_ubyte),
    ('version_minor', ctypes.c_ubyte),
    ('storage_size', ctypes.c_ubyte),
    ('protocol', ctypes.c_ubyte),
     ]

class struct_mifare_desfire_version_info_1(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('vendor_id', ctypes.c_ubyte),
    ('type', ctypes.c_ubyte),
    ('subtype', ctypes.c_ubyte),
    ('version_major', ctypes.c_ubyte),
    ('version_minor', ctypes.c_ubyte),
    ('storage_size', ctypes.c_ubyte),
    ('protocol', ctypes.c_ubyte),
     ]

struct_mifare_desfire_version_info._pack_ = True # source:False
struct_mifare_desfire_version_info._fields_ = [
    ('hardware', struct_mifare_desfire_version_info_0),
    ('software', struct_mifare_desfire_version_info_1),
    ('uid', ctypes.c_ubyte * 7),
    ('batch_number', ctypes.c_ubyte * 5),
    ('production_week', ctypes.c_ubyte),
    ('production_year', ctypes.c_ubyte),
]

class union_mifare_desfire_file_settings_0(ctypes.Union):
    pass

class struct_mifare_desfire_file_settings_0_0(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('file_size', ctypes.c_uint32),
     ]

class struct_mifare_desfire_file_settings_0_2(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('record_size', ctypes.c_uint32),
    ('max_number_of_records', ctypes.c_uint32),
    ('current_number_of_records', ctypes.c_uint32),
     ]

class struct_mifare_desfire_file_settings_0_1(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('lower_limit', ctypes.c_int32),
    ('upper_limit', ctypes.c_int32),
    ('limited_credit_value', ctypes.c_int32),
    ('limited_credit_enabled', ctypes.c_ubyte),
    ('PADDING_0', ctypes.c_ubyte * 3),
     ]

union_mifare_desfire_file_settings_0._pack_ = True # source:False
union_mifare_desfire_file_settings_0._fields_ = [
    ('standard_file', struct_mifare_desfire_file_settings_0_0),
    ('value_file', struct_mifare_desfire_file_settings_0_1),
    ('linear_record_file', struct_mifare_desfire_file_settings_0_2),
    ('PADDING_0', ctypes.c_ubyte * 4),
]

struct_mifare_desfire_file_settings._pack_ = True # source:False
struct_mifare_desfire_file_settings._fields_ = [
    ('file_type', ctypes.c_ubyte),
    ('communication_settings', ctypes.c_ubyte),
    ('access_rights', ctypes.c_uint16),
    ('settings', union_mifare_desfire_file_settings_0),
]

__all__ = \
    ['CLASSIC_1K', 'CLASSIC_4K', 'DESFIRE', 'MC_AUTH_A', 'MC_AUTH_B',
    'MC_DECREMENT', 'MC_INCREMENT', 'MC_READ', 'MC_STORE',
    'MC_TRANSFER', 'MC_WRITE', 'MFC_KEY_A', 'MFC_KEY_B', 'Mad',
    'MadAid', 'MifareClassicBlock', 'MifareClassicBlockNumber',
    'MifareClassicKey', 'MifareClassicKeyType',
    'MifareClassicKeyType__enumvalues', 'MifareClassicSectorNumber',
    'MifareDESFireAID', 'MifareDESFireDF', 'MifareDESFireKey',
    'MifareTag', 'MifareUltralightPage', 'MifareUltralightPageNumber',
    'NBR_106', 'NBR_212', 'NBR_424', 'NBR_847', 'NBR_UNDEFINED',
    'NDM_ACTIVE', 'NDM_PASSIVE', 'NDM_UNDEFINED', 'NMT_DEP',
    'NMT_FELICA', 'NMT_ISO14443A', 'NMT_ISO14443B',
    'NMT_ISO14443B2CT', 'NMT_ISO14443B2SR', 'NMT_ISO14443BI',
    'NMT_JEWEL', 'NP_ACCEPT_INVALID_FRAMES',
    'NP_ACCEPT_MULTIPLE_FRAMES', 'NP_ACTIVATE_CRYPTO1',
    'NP_ACTIVATE_FIELD', 'NP_AUTO_ISO14443_4', 'NP_EASY_FRAMING',
    'NP_FORCE_ISO14443_A', 'NP_FORCE_ISO14443_B',
    'NP_FORCE_SPEED_106', 'NP_HANDLE_CRC', 'NP_HANDLE_PARITY',
    'NP_INFINITE_SELECT', 'NP_TIMEOUT_ATR', 'NP_TIMEOUT_COM',
    'NP_TIMEOUT_COMMAND', 'N_INITIATOR', 'N_TARGET', 'ULTRALIGHT',
    'ULTRALIGHT_C', 'c__EA_MifareClassicKeyType', 'c__EA_mifare_cmd',
    'c__EA_nfc_baud_rate', 'c__EA_nfc_dep_mode', 'c__EA_nfc_mode',
    'c__EA_nfc_modulation_type', 'c__EA_nfc_property',
    'freefare_free_tag', 'freefare_free_tags',
    'freefare_get_tag_friendly_name', 'freefare_get_tag_type',
    'freefare_get_tag_uid', 'freefare_get_tags', 'freefare_perror',
    'freefare_strerror', 'freefare_strerror_r', 'freefare_tag_new',
    'int32_t', 'is_mifare_ultralightc_on_reader', 'iso14443a_crc',
    'iso14443a_crc_append', 'iso14443a_locate_historical_bytes',
    'mad_free', 'mad_get_aid', 'mad_get_card_publisher_sector',
    'mad_get_version', 'mad_new', 'mad_read', 'mad_sector_reserved',
    'mad_set_aid', 'mad_set_card_publisher_sector', 'mad_set_version',
    'mad_write', 'mifare_application_alloc',
    'mifare_application_find', 'mifare_application_free',
    'mifare_application_read', 'mifare_application_write',
    'mifare_classic_authenticate', 'mifare_classic_block',
    'mifare_classic_block_data', 'mifare_classic_block_manufacturer',
    'mifare_classic_block_sector', 'mifare_classic_block_trailer',
    'mifare_classic_connect', 'mifare_classic_decrement',
    'mifare_classic_disconnect', 'mifare_classic_format_sector',
    'mifare_classic_get_data_block_permission',
    'mifare_classic_get_trailer_block_permission',
    'mifare_classic_increment', 'mifare_classic_init_value',
    'mifare_classic_read', 'mifare_classic_read_value',
    'mifare_classic_restore', 'mifare_classic_sector_block_count',
    'mifare_classic_sector_first_block',
    'mifare_classic_sector_last_block', 'mifare_classic_tag',
    'mifare_classic_trailer_block', 'mifare_classic_transfer',
    'mifare_classic_write', 'mifare_cmd', 'mifare_cmd__enumvalues',
    'mifare_desfire_3des_key_new',
    'mifare_desfire_3des_key_new_with_version',
    'mifare_desfire_3k3des_key_new',
    'mifare_desfire_3k3des_key_new_with_version',
    'mifare_desfire_abort_transaction', 'mifare_desfire_aes_key_new',
    'mifare_desfire_aes_key_new_with_version',
    'mifare_desfire_aid_get_aid', 'mifare_desfire_aid_new',
    'mifare_desfire_aid_new_with_mad_aid',
    'mifare_desfire_authenticate', 'mifare_desfire_authenticate_aes',
    'mifare_desfire_authenticate_iso',
    'mifare_desfire_change_file_settings',
    'mifare_desfire_change_key', 'mifare_desfire_change_key_settings',
    'mifare_desfire_clear_record_file',
    'mifare_desfire_commit_transaction', 'mifare_desfire_connect',
    'mifare_desfire_create_application',
    'mifare_desfire_create_application_3k3des',
    'mifare_desfire_create_application_3k3des_iso',
    'mifare_desfire_create_application_aes',
    'mifare_desfire_create_application_aes_iso',
    'mifare_desfire_create_application_iso',
    'mifare_desfire_create_backup_data_file',
    'mifare_desfire_create_backup_data_file_iso',
    'mifare_desfire_create_cyclic_record_file',
    'mifare_desfire_create_cyclic_record_file_iso',
    'mifare_desfire_create_linear_record_file',
    'mifare_desfire_create_linear_record_file_iso',
    'mifare_desfire_create_std_data_file',
    'mifare_desfire_create_std_data_file_iso',
    'mifare_desfire_create_value_file', 'mifare_desfire_credit',
    'mifare_desfire_credit_ex', 'mifare_desfire_debit',
    'mifare_desfire_debit_ex', 'mifare_desfire_delete_application',
    'mifare_desfire_delete_file', 'mifare_desfire_des_key_new',
    'mifare_desfire_des_key_new_with_version',
    'mifare_desfire_disconnect', 'mifare_desfire_error_lookup',
    'mifare_desfire_format_picc',
    'mifare_desfire_free_application_ids', 'mifare_desfire_free_mem',
    'mifare_desfire_get_application_ids',
    'mifare_desfire_get_card_uid', 'mifare_desfire_get_df_names',
    'mifare_desfire_get_file_ids', 'mifare_desfire_get_file_settings',
    'mifare_desfire_get_iso_file_ids',
    'mifare_desfire_get_key_settings',
    'mifare_desfire_get_key_version', 'mifare_desfire_get_value',
    'mifare_desfire_get_value_ex', 'mifare_desfire_get_version',
    'mifare_desfire_key_free', 'mifare_desfire_key_get_version',
    'mifare_desfire_key_set_version', 'mifare_desfire_last_pcd_error',
    'mifare_desfire_last_picc_error', 'mifare_desfire_limited_credit',
    'mifare_desfire_limited_credit_ex', 'mifare_desfire_read_data',
    'mifare_desfire_read_data_ex', 'mifare_desfire_read_records',
    'mifare_desfire_read_records_ex',
    'mifare_desfire_select_application',
    'mifare_desfire_session_key_new', 'mifare_desfire_set_ats',
    'mifare_desfire_set_configuration',
    'mifare_desfire_set_default_key', 'mifare_desfire_write_data',
    'mifare_desfire_write_data_ex', 'mifare_desfire_write_record',
    'mifare_desfire_write_record_ex', 'mifare_param',
    'mifare_tag_type', 'mifare_ultralight_connect',
    'mifare_ultralight_disconnect', 'mifare_ultralight_read',
    'mifare_ultralight_write', 'mifare_ultralightc_authenticate',
    'mifareul_block', 'mifareul_block_data',
    'mifareul_block_manufacturer', 'mifareul_tag',
    'nfc_abort_command', 'nfc_baud_rate', 'nfc_baud_rate__enumvalues',
    'nfc_close', 'nfc_connstring', 'nfc_context', 'nfc_dep_info',
    'nfc_dep_mode', 'nfc_dep_mode__enumvalues', 'nfc_device',
    'nfc_device_get_connstring', 'nfc_device_get_information_about',
    'nfc_device_get_last_error', 'nfc_device_get_name',
    'nfc_device_get_supported_baud_rate',
    'nfc_device_get_supported_modulation',
    'nfc_device_set_property_bool', 'nfc_device_set_property_int',
    'nfc_driver', 'nfc_exit', 'nfc_felica_info', 'nfc_free',
    'nfc_idle', 'nfc_init', 'nfc_initiator_deselect_target',
    'nfc_initiator_init', 'nfc_initiator_init_secure_element',
    'nfc_initiator_list_passive_targets',
    'nfc_initiator_poll_dep_target', 'nfc_initiator_poll_target',
    'nfc_initiator_select_dep_target',
    'nfc_initiator_select_passive_target',
    'nfc_initiator_target_is_present',
    'nfc_initiator_transceive_bits',
    'nfc_initiator_transceive_bits_timed',
    'nfc_initiator_transceive_bytes',
    'nfc_initiator_transceive_bytes_timed', 'nfc_iso14443a_info',
    'nfc_iso14443b2ct_info', 'nfc_iso14443b2sr_info',
    'nfc_iso14443b_info', 'nfc_iso14443bi_info', 'nfc_jewel_info',
    'nfc_list_devices', 'nfc_mode', 'nfc_mode__enumvalues',
    'nfc_modulation', 'nfc_modulation_type',
    'nfc_modulation_type__enumvalues', 'nfc_open', 'nfc_perror',
    'nfc_property', 'nfc_property__enumvalues', 'nfc_register_driver',
    'nfc_strerror', 'nfc_strerror_r', 'nfc_target', 'nfc_target_info',
    'nfc_target_init', 'nfc_target_receive_bits',
    'nfc_target_receive_bytes', 'nfc_target_send_bits',
    'nfc_target_send_bytes', 'nfc_version', 'off_t', 'size_t',
    'ssize_t', 'str_nfc_baud_rate', 'str_nfc_modulation_type',
    'str_nfc_target', 'struct_c__SA_mifare_classic_block_data',
    'struct_c__SA_mifare_classic_block_manufacturer',
    'struct_c__SA_mifare_classic_block_trailer',
    'struct_c__SA_mifare_classic_tag',
    'struct_c__SA_mifareul_block_data',
    'struct_c__SA_mifareul_block_manufacturer',
    'struct_c__SA_mifareul_tag', 'struct_c__SA_nfc_dep_info',
    'struct_c__SA_nfc_felica_info', 'struct_c__SA_nfc_iso14443a_info',
    'struct_c__SA_nfc_iso14443b2ct_info',
    'struct_c__SA_nfc_iso14443b2sr_info',
    'struct_c__SA_nfc_iso14443b_info',
    'struct_c__SA_nfc_iso14443bi_info', 'struct_c__SA_nfc_jewel_info',
    'struct_c__SA_nfc_modulation', 'struct_c__SA_nfc_target',
    'struct_mad', 'struct_mad_aid', 'struct_mifare_desfire_aid',
    'struct_mifare_desfire_df', 'struct_mifare_desfire_file_settings',
    'struct_mifare_desfire_file_settings_0_0',
    'struct_mifare_desfire_file_settings_0_1',
    'struct_mifare_desfire_file_settings_0_2',
    'struct_mifare_desfire_key', 'struct_mifare_desfire_version_info',
    'struct_mifare_desfire_version_info_0',
    'struct_mifare_desfire_version_info_1',
    'struct_mifare_param_auth', 'struct_mifare_param_data',
    'struct_mifare_param_value', 'struct_mifare_tag',
    'struct_nfc_context', 'struct_nfc_device', 'struct_nfc_driver',
    'struct_nfc_user_defined_device', 'struct_supported_tag',
    'tlv_append', 'tlv_decode', 'tlv_encode', 'tlv_record_length',
    'uint16_t', 'uint32_t', 'uint8_t',
    'union_c__UA_mifare_classic_block', 'union_c__UA_mifare_param',
    'union_c__UA_mifareul_block', 'union_c__UA_nfc_target_info',
    'union_mifare_desfire_file_settings_0']
