#  This file is part of Ryanhtech shOS (SenseHat Operating System)
#  Copyright (c) 2022 Ryanhtech Labs
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

# Sense HAT library
from sense_hat import SenseHat

# UI layouts
from shos.ui.ui_pixels import UI_KE_BOOT_SPLASH_SCREEN


class ShosBootUi:
    def __init__(self, sh: SenseHat):
        """
        This class provides controls for the boot UI.
        """
        super(ShosBootUi, self).__init__()
        self.__sense_hat = sh

    def show_splash_screen_ui(self):
        """
        This shows the splash screen UI. It is a big R that appears in white with a grey background.
        """
        self.__sense_hat.set_pixels(UI_KE_BOOT_SPLASH_SCREEN)
