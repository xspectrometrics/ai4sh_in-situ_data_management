'''
Created 22 Jan 2021
Updated 12 Feb 2021
Updated4 Jan 2024

support
==========================================

Package belonging to Kartturs GeoImagine Framework.

Author
------
Thomas Gumbricht (thomas.gumbricht@karttur.com)

'''

from .version import __version__, VERSION, metadataD

from .karttur_dt import Today, Delta_days

from .setDiskPath import SetDiskPath

from .pretty_print import Pprint_parameter

from .json_read_write import Read_json, Dump_json

from .csv_read_write import Read_csv, Read_csv_excel, Write_txt_L

from .project_pilot import Project_pilot_locate, Root_locate, Project_locate, Get_project_path, Job_pilot_locate, Full_path_locate

from .character_check import Check_white_space, Check_underscore

from .list_files import Glob_get_file_list, Path_lib_get_file_list, Csv_file_list

from .update_dict import Update_dict
