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

        # TODO connect to a signal sent when a new layer is loaded to call
        # translations

        self.iface = veriso.iface

        #self.legend = self.iface.legendInterface()
        #self.legend.itemAdded.connect(self.translate)

    def translate(self, i):

        from veriso.opengisch_utils.qgis.layers_translator.layers_translator \
            import QgisLayersTranslator, Dictionary

        current_dir = os.path.dirname(os.path.abspath(__file__))
        dictionary_file = os.path.join(current_dir, 'translations_verivd.yml')

        verivd_dictionary = Dictionary(dictionary_file)

        layers_translator = QgisLayersTranslator(
            self.iface, verivd_dictionary)
        layers_translator.run()
