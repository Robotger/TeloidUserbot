
# Copyright (C) 2022 RobotgerDev.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
# TeloidUserBot


from userbot import LOGS


def __list_all_modules():
    from os.path import dirname, basename, isfile
    import glob

    mod_paths = glob.glob(dirname(__file__) + "/*.py")
    all_module = [
        basename(f)[:-3] for f in mod_paths
        if isfile(f) and f.endswith(".py") and not f.endswith("__init__.py")
    ]
    return all_module


ALL_MODULE = sorted(__list_all_modules())
LOGS.info("Asistan modülleri yükleniyor: %s", str(ALL_MODULE))
__all__ = ALL_MODULE + ["ALL_MODULE"]
