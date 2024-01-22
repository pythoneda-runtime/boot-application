# vim: set fileencoding=utf-8
"""
pythoneda/runtime/boot/application/boot_app.py

This file can be used to run pythoneda-runtime/boot

Copyright (C) 2024-today boot's pythoneda-runtime/boot-application

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
import asyncio
from pythoneda.shared.application import PythonEDA
from pythoneda.shared.runtime.events.lifecycle.infrastructure.cli import DefUrlCli
from pythoneda.shared.runtime.events.lifecycle.infrastructure.dbus import (
    BootDbusSignalEmitter,
)
from pythoneda.shared.runtime.events.lifecycle.infrastructure.dbus import (
    BootDbusSignalListener,
)


@enable(BootDbusSignalEmitter)
@enable(BootDbusSignalListener)
@enable(DefUrlCli)
class BootApp(PythonEDA):
    """
    Runs PythonEDA Boot.

    Class name: BootApp

    Responsibilities:
        - Runs PythonEDA Boot.

    Collaborators:
        - Command-line handlers from pythoneda-runtime/boot-infrastructure
    """

    def __init__(self):
        """
        Creates a new BootApp instance.
        """
        # boot_banner is automatically generated by pythoneda-runtime-def/boot-application
        try:
            from pythoneda.runtime.boot.application.boot_banner import BootBanner

            banner = BootBanner()
        except ImportError:
            banner = None
        super().__init__(banner, __file__)

    async def accept_definition_url(self, url: str):
        """
        Annotates the url of the definition repository and generates
        a BootRequested event.
        :param url: Such url.
        :type url: str
        """
        booted = Boot.listen_BootRequested(BootRequested(url))
        if booted:
            self.emit(booted)


if __name__ == "__main__":
    asyncio.run(BootApp.main("pythoneda.runtime.boot.Boot"))

# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
