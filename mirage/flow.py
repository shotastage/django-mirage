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

from abc import ABCMeta, abstractmethod
from djconsole.command import log, raise_error_message


class Workflow():

    def __init__(self, parser):
        self.inherite       = parser
        self._action        = self.inherite[0]
        self._subaction     = self.inherite[1]
        self._option        = self.inherite[2]
        self._option_detail = self.inherite[3]
        self._values        = self.inherite[4]
        self.Stepflows      = []
        self.additional_init_()

    def additional_init_(self): pass
    
    def get_first_arg(self):
        try:
            return self._values[0]
        except:
            raise ValueError

    def register(self, flow):
        self.Stepflows.append(flow)
    
    def main(self):
        # Main flow struct
        pass

    def run(self):
        self.main()

        # Flow
        for flow in self.Stepflows:
            try:
                flow.run()
            except:
                raise Exception
          


class Stepflow():
    def __init__(self, parser):
        self.inherite       = parser
        self._action        = parser._cmd
        self._subaction     = parser._sub_action
        self._option        = parser._option
        self._option_detail = parser._option_detail
        self._values        = parser._values
        self._flows         = []


    def add(self, func):
        self._flows.append(func)

    def run(self):
        for flow in self._flows:
            try:
                flow()
            except:
                log("Something error has occured!", withError = True, errorDetail = raise_error_message(flow))
                raise Exception



class Flow():

    def __init__(self, onInstance = False):
        self._flows = []

        if onInstance:
            self.flow()

    def flow(self):

        for flow in self._flows:
            if "function" in str(type(flow)):
                try:
                    flow()
                except:
                    log("Something error has occured!", withError = True, errorDetail = raise_error_message(flow))
                    raise Exception

    def execute(self):
        self.flow()

    def register(self, *funcs):
        for func in funcs:
            self._flows.append(func)