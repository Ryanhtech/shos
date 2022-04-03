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

"""shOS boot file

This file loads the shOS bootloader that will load the kernel. It is the main entry point of shOS. You can store it
anywhere, and start it in the shOS virtual environment, and it will start shOS for you.
"""

try:
    # Import sys to get commandline arguments
    import sys
except ImportError as sys_error:
    # Flag the error
    print("ERROR: Cannot import sys. Your Python installation is seriously broken.")

    # Rethrow the exception. It is the only way to stop execution
    raise sys_error


# shOS boot file class
class ShosBootFile:
    def __init__(self):
        super(ShosBootFile, self).__init__()

    @staticmethod
    def is_running_in_venv() -> bool:
        """
        This method determines if the current script is running in a virtual environment (also known as "venv").

        :return: True if you run in a virtual environment, False otherwise.
        """
        return sys.prefix != sys.base_prefix

    @staticmethod
    def handle_shos_kernel_missing():
        """
        Use this method to handle a kernel file lack. For example, call this after trying to import a kernel component
        (e.g. KeBase, KeBootloader), and catching ImportError. This will do the following:
            - If the user is not running in a virtual environment, ask to create one and install the shos package into
              it.
            - If the user is running in a virtual environment, ask the user to check if it is the right virtual
              environment and, if it is the case, to uninstall/reinstall the shos package.
        """

        is_venv = ShosBootFile.is_running_in_venv()

        if is_venv:
            # We are running in a venv. (see doc for more info)
            print("An error occurred. The shOS library cannot be found or is corrupted. This is what you can do :\n"
                  "  - If you have already installed the shOS library in this virtual environment, uninstall it and\n"
                  "    then reinstall it.\n"
                  "  - If you have not installed the shOS library yet, install it in this virtual environment.")

            return

        # We are not in a venv
        print("Please run this in a virtual environment with the shOS library installed.")
        return


try:
    # Try to import shOS bootloader
    from shos.ke.shos_bootloader import KeBootloader
except ImportError:
    # Print the installation prompt message. If the user has not installed the shOS package, it will need to follow
    # these instructions. Read doc for more info
    ShosBootFile.handle_shos_kernel_missing()

    # Exit with return value 1
    sys.exit(1)


# Entry point
if __name__ == "__main__":
    # Get the commandline arguments and store them
    cmdline = sys.argv

    # Initialize a shOS bootloader instance
    shos_bootloader_instance = KeBootloader(cmdline)

    # Start shOS using the instance we created
    shos_bootloader_instance.shos_start()
