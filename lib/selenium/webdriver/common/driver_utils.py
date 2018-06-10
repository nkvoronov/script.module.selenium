# Licensed to the Software Freedom Conservancy (SFC) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The SFC licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

"""
Web Driver Utils
"""
import os
import xbmc
import xbmcaddon
import platform
import subprocess

def run_selenium_doker():
    run_script = get_driver_path('docker')
    try:
        process = subprocess.Popen(run_script)
        code = process.wait()
    except Exception, e:
        if e.errno != errno.ECONNRESET:
            raise
        pass
    return code

def get_driver_path(dname):
    rpath = xbmcaddon.Addon('script.module.selenium').getAddonInfo('path') + os.path.sep + 'bin' + os.path.sep + dname + os.path.sep
    if platform.system() == 'Windows':
        result = rpath + 'win32' + os.path.sep + dname
    if platform.system() == 'Linux':
        if xbmc.getCondVisibility('System.HasAddon(service.libreelec.settings)'):
            result = rpath + 'libreelec' + os.path.sep + dname
        else:
            result = rpath + 'linux64' + os.path.sep + dname
        if dname == 'docker':
            result = result + '.start'
        os.system('chmod +x ' + result)
    return result
