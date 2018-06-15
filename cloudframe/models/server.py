#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import logging
import sqlite3
import time

from restframe.common.job import Tasks

LOG = logging.getLogger(__name__)


class Server(object):

    def create(self, tenant, object_id, args):
        LOG.debug('create server...')
        con = sqlite3.connect('/root/data/rf.db')
        con.execute("INSERT INTO server(uuid,tenant,name) \
            values(?,?,?)", (object_id, tenant, args['name']))
        con.commit()
        con.close()
        item = [self.do_server_deploy, object_id]
        Tasks.put_nowait(item)
        data = {'model_name': 'abc'}
        LOG.debug('create server end')
        return data

    @classmethod
    def get(cls, server_id):
        data = {'model_name': 'abc'}
        return data

    def do_server_deploy(self, object_id):
        LOG.debug('do server create bgin.')
        time.sleep(30)
        LOG.debug('do server create end.')
