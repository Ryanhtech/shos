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

"""shOS startup params

This file contains the KeBootParameters class. This class allows you to start up shOS kernel using the KeBase.boot_ke()
static method.
"""

from sense_hat import SenseHat


class KeBootParameters:
    """Kernel boot parameters

    You should pass this class to the KeBase.boot_ke() method. It will allow you to pass parameters to the kernel at
    startup.

    :param cmdline: The command line that was used to start the Python startup script. You can get it using sys.argv.
    :param sense_hat: The Sense HAT instance corresponding to the Sense HAT you want to use.
    :param force_safe_mode: If you should run in safe mode. This can be overridden later by the user's actions, but
                            setting this to True will force safe mode and ignore these actions.
    """

    def __init__(self, cmdline: list, sense_hat: SenseHat, force_safe_mode=False):
        super(KeBootParameters, self).__init__()

        # Set the class attributes
        self.__cmdline = cmdline
        self.__sense_hat = sense_hat
        self.__force_safemode = force_safe_mode

    def should_force_safemode(self) -> bool:
        """
        Determines if you should force Safe Mode.

        :return: True if you should force Safe Mode, False otherwise.
        """
        return self.__force_safemode

    def get_cmdline(self) -> list:
        """
        Returns the cmdline that was used to create the class.

        :return: the cmdline that was used to create the class.
        """
        return self.__cmdline

    def get_sense_hat(self):
        """
        Returns the Sense HAT instance that you used to create this class.

        :return: ^^^^^^^^
        """
        return self.__sense_hat
