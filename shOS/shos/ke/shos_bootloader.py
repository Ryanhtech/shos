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


class KeBootloader:
    """shOS KeBootloader (Kernel Bootloader)

    This class provides the shOS bootloader methods. It boots up the system by initializing the shos, and by checking
    if everything is OK to start it.

    :param shos_cmdline: the command line arguments. You can get them using `sys.argv`.
    """
    def __init__(self, shos_cmdline):
        super(KeBootloader, self).__init__(shos_cmdline)

    def shos_start(self):
        pass
