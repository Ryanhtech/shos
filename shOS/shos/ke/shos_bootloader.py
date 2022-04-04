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


try:
    from sense_hat import SenseHat
except ImportError as sh_err:
    # Flag the error
    print("Error: Cannot import SenseHat!")

    # Rethrow the error
    raise sh_err


try:
    from shos.ke.shos_bootparams import KeBootParameters
except ImportError as ke_err:
    # Flag this kernel error
    print("Critical error: cannot import KeBootParameters!!")
    raise ke_err

from shos.ui.boot_ui import ShosBootUi


class KeBootloader:
    """shOS KeBootloader (Kernel Bootloader)

    This class provides the shOS bootloader methods. It boots up the system by initializing the shos, and by checking
    if everything is OK to start it.

    :param shos_cmdline: the command line arguments. You can get them using `sys.argv`.
    """

    def __init__(self, shos_cmdline):
        super(KeBootloader, self).__init__()

        # Save the cmdline contents in the class
        self._kb_cmdline = shos_cmdline

    def shos_start(self) -> int:
        """
        Starts the shOS kernel. This method will never return, except if the kernel leaves.
        This method starts the kernel in three simple steps:

          - Step 1: Initialize the Sense HAT and the kernel startup params.
          - Step 2: Start up the kernel using those params.
          - Step 3: TODO step 3

        :return: The kernel exit code. If the kernel doesn't leave, this method will never return.
        """
        # Step 1.1: Initialize Sense HAT
        try:
            sh = SenseHat()
        except Exception as e:
            # There was an error initializing the Sense HAT.
            print("Sense hat initialization error - Please ensure that your device is plugged in correctly and try "
                  "again.")
            raise e

        # Step 1.2: Initialize startup params
        # TODO force safe mode
        ke_params = KeBootParameters(self._kb_cmdline, sh, False)

        # Step 1.3: Initialize boot UI TODO Remove after debug
        bootui = ShosBootUi(sh)
        bootui.show_splash_screen_ui()

        return 0


    def shos_start_secure(self):
        """
        Like the shos_start() method, but this method runs the kernel in a sandbox. If an error occurs, a
        KeEndInformation instance will be returned. This KeEndInformation contains all the info on the reasons that
        forced the kernel to leave.

        :return: The KeEndInformation instance (read doc). This will never return if the kernel never leaves.
        """
        # Copy the shos_start method in a variable
        start_method_inst = self.shos_start

        # Initialize variables
        has_crashed = False
        kernel_exception = None
        method_return_val = None

        # Start the method under a try/except and get the return value if there is one
        try:
            method_return_val = start_method_inst()
        except Exception as p_kernel_exception:
            has_crashed = True
            kernel_exception = p_kernel_exception

        # TODO KeEndInformation instance initialization
