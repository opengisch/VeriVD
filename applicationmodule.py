# -*- coding: utf-8 -*-

from __future__ import absolute_import, print_function
import os

from veriso.modules.applicationmodule_base import ApplicationModuleBase


class ApplicationModule(ApplicationModuleBase):
    """
    This is the minimum required implementation to have your own module
    """
    def __init__(self, veriso):
        super(ApplicationModule, self).__init__(veriso)
