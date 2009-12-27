#
# Copyright (c) 2009 Testrepository Contributors
# 
# Licensed under either the Apache License, Version 2.0 or the BSD 3-clause
# license at the users choice. A copy of both licenses are available in the
# project source as Apache-2.0 and BSD. You may not use this file except in
# compliance with one of these two licences.
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under these licenses is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  See the
# license you chose for the specific language governing permissions and
# limitations under that license.

"""Load data into a repository."""

import subunit

from testrepository.commands import Command

class load(Command):
    """Load a subunit stream into a repository."""

    input_streams = ['subunit+']

    def run(self):
        path = self.ui.here
        repo = self.repository_factory.open(path)
        for stream in self.ui.iter_streams('subunit'):
            inserter = repo.get_inserter()
            case = subunit.ProtocolTestCase(stream)
            inserter.startTestRun()
            try:
                case.run(inserter)
            finally:
                inserter.stopTestRun()
