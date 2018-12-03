#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 1999-2017 Alibaba Group Holding Ltd.
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#      http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from odps.models import Table


class MockProject(object):
    def __init__(self):
        self.name = 'mocked_project'


class SeahawksTable(Table):
    def __init__(self, **kwargs):
        super(SeahawksTable, self).__init__(**kwargs)

        self._loaded = True

    @property
    def project(self):
        return MockProject()

    def reload(self):
        return