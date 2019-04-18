# -*- coding: utf-8 -*-
"""
 This script initializes the plugin, making it known to QGIS.
"""
from __future__ import absolute_import

def classFactory(iface):
    from .SuperLabeling import SuperLabeling
    return SuperLabeling(iface)
