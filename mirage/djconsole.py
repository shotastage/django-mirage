# -*- coding: utf-8 -*-
"""
Copyright 2017-2018 Shota Shimazu.

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

import sys

from djconsole.djargparse import ArgumentsParser
from djconsole.command import log, raise_error_message

def main():

    parser = ArgumentsParser()

    # Usage & Version
    parser.add_argument("h", "help", None, "UsageShow")
    parser.add_argument("v", "version", None, "VersionShow")

    # Commands
    parser.add_argument("new", "newproject", None, "DjangoStartup")
    parser.add_argument_with_subaction("new", "newproject", "cms", None, "DjangoCMSStartup")

    parser.add_argument("b", "backup", "app", "DjangoBackupApp")

    parser.add_argument("conf", "configure", None, "Configure")

    parser.add_argument("c", "console", None, "DjangoConsole")
    parser.add_argument_with_subaction("c", "console", "db", None, "DjangoDBConsole")

    parser.add_argument("d", "destroy", "app", "DjangoDestroy")

    parser.add_argument_with_subaction("db", "database", "migrate", None, "DjangoMigrate")
    parser.add_argument_with_subaction("db", "database", "reset", None, "DjangoDBReset")

    # parser.add_argument("d", "destroy", None, "DjangoDestroy")

    parser.add_argument("g", "generate", "app", "DjangoAppMake")

    parser.add_argument("ide", "scaffold", None, "Scaffold")
    parser.add_argument("internal_server_launch", "internal_server_launch", None, "ScaffoldServer")

    parser.add_argument("s", "server", None, "DjangoDebugServer")

    # Excute
    parser.parse()