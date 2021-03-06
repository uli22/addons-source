#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Gramps - a GTK+/GNOME based genealogy program
#
# Copyright (C) 2017 Sam Manzi
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#

'''
Import from an Whollygenes - The Master Genealogist (TMG) Project backup file
(*.SQZ)
'''

#-------------------------------------------------------------------------
#
# Standard python modules
#
#-------------------------------------------------------------------------


#------------------------------------------------------------------------
#
# Set up logging
#
#------------------------------------------------------------------------
import logging
LOG = logging.getLogger(".TMGImport")

#-------------------------------------------------------------------------
#
# TMG library
#
#-------------------------------------------------------------------------

from lib import libtmg

#-------------------------------------------------------------------------
#
# importData (based on importgpkg.py)
#
#-------------------------------------------------------------------------
def importSqzData(database, filename, user):
    """
    Function called by Gramps to import TMG project dataset(s).
    Uses TMG library to process .SQZ Backup file
    """
    importer = libtmg.importData
    info = importer(database, filename, user)

    return info
