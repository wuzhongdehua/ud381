# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# https://github.com/apache/storm/blob/master/examples/storm-starter/multilang/resources/splitsentence.py

import storm
import urllib2
import traceback
from bs4 import BeautifulSoup

class URLBolt(storm.BasicBolt):
    def process(self, tup):
        #TO DO: Add check for empty values
        url = tup.values[0]
        try:
            r = urllib2.urlopen(url).read()

            soup = BeautifulSoup(r)
            urlText = soup.findAll({'title' : True, 'p' : True})
            if urlText:
                [storm.emit([t.string]) for t in urlText]
        except:
            #print traceback.format_exc()
            pass

URLBolt().run()
