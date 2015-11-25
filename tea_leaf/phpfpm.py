# -*- coding: utf-8 -*-
__author__ = 'Monkee Magic <magic.monkee.magic@gmail.com>'
__version__ = '1.0.0'

# Copyright (c) 2015 Lyndon Swan.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

"""
>>> psutil.virtual_memory()
svmem(total=8374149120, available=2081050624, percent=75.1, used=8074080256, free=300068864, active=3294920704, inactive=1361616896, buffers=529895424, cached=1251086336)
>>> psutil.swap_memory()
sswap(total=2097147904, used=296128512, free=1801019392, percent=14.1, sin=304193536, sout=677842944)
>>>

"""
import time
import psutil
from pprint import pprint
import platform


class PHPFPM:
    _timestamp = time.strftime("%d/%m/%Y %H:%M:%S")
    _pids = None
    _phpfpm = None
    _swap_memory = None
    _debug = False

    def __init__(self):
        self._pids = self.pidof('php-fpm')
        self.calculate()


    def calculate(self):
        self._phpfpm = {
                           'total': len(self._pids),
                            'percent': 50.0
        }

    def memory(self):
        p = psutil.Process(pid)
        pinfo = p.as_dict(ad_value=ACCESS_DENIED)

    def data(self, instance_id):
        if platform.system() == "Linux":
            pass
        elif platform.system() == 'Darwin':
            pass
        else:
            pass
        return self.universal_data(instance_id)

    def universal_data(self, instance_id):
        metric = self.set_metric()
        return self.process_metrics(instance_id, metric)


    def pidof(self, pgname):
        pids = []
        for proc in psutil.process_iter():
            # search for matches in the process name and cmdline
            try:
                name = proc.name()
            except psutil.Error:
                pass
            else:
                if name == pgname:
                    pids.append(str(proc.pid))
                    continue

            try:
                cmdline = proc.cmdline()
            except psutil.Error:
                pass
            else:
                if cmdline and cmdline[0] == pgname:
                    pids.append(str(proc.pid))

        return pids

    def set_metric(self):
        metric = [
            {
                "Unit": 'Count',
                "Array": self._phpfpm,
                'Dimensions': [
                    {'PHPFPM_Count': 'total'},
                ],
            },
            {
                "Unit": 'Percent',
                "Array": self._phpfpm,
                'Dimensions': [
                    {'Memory_Pecentage_Used': 'percent'},
                ],
            }
        ]
        return metric

    def process_metrics(self, instance_id, metric):
        data = []
        for unit in metric:
            for datapoints in unit['Dimensions']:
                for point in datapoints:
                    data.append({
                        'MetricName': instance_id + "_" + point,
                        'Dimensions': [
                            {
                                'Name': 'TeaLeafModule',
                                'Value': 'PHPFPM'
                            },
                            {
                                'Name': 'InstanceId',
                                'Value': instance_id
                            },
                        ],

                        'Value': unit['Array'][datapoints[point]],
                        'Unit': unit['Unit']
                    })
        if self._debug:
            pprint(data)
        return data



if __name__ == "__main__":
    phpfpm = PHPFPM()
    phpfpm.data('i-afaffaf')
