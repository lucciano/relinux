'''
Localization Utilities
@author: MiJyn
'''

import gettext
import os
import re
from relinux import config, configutils


class Localize():
    def __init__(self):
        self.languages = {}
        patt = re.compile(config.productunix + "_(.*?)")
        for i in os.listdir(config.localedir):
            m = patt.match(i)
            if configutils.checkMatched(m):
                lang = m.group(1)
                self.languages[lang] = gettext.translation(
                    config.productunix, config.localedir, languages=[lang])

    def useLanguage(self, language):
        self.languages[language].install()
        config._ = self.languages[language].ugettext
