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


class Memory:
    _timestamp = time.strftime("%d/%m/%Y %H:%M:%S")
    _virtual_memory = None
    _swap_memory = None
    _debug = True

    def __init__(self):
        self._virtual_memory = psutil.virtual_memory()
        self._swap_memory = psutil.swap_memory()
        if self._debug:
            pprint(self._virtual_memory)
            pprint(self._swap_memory)

    def data(self, instance_id):
        if platform.system() == "Linux":
            return self.linux_data(instance_id)
        elif platform.system() == 'Darwin':
            return self.mac_data(instance_id)
        else:
            return None

    def mac_data(self, instance_id):
        metric = self.set_mac_metric()
        return self.process_metrics(instance_id, metric)

    def linux_data(self, instance_id):
        metric = self.set_linux_metric()
        return self.process_metrics(instance_id, metric)

    def set_mac_metric(self):
        metric = [
                    {
                        "Unit":'Bytes',
                        "Array": self._virtual_memory,
                        'Dimensions': [
                            {'Memory_Total': 'total'},
                            {'Memory_Available': 'available'},
                            {'Memory_Used': 'used'},
                            {'Memory_Free': 'free'},
                            {"Memory_Active": 'active'},
                             {"Memory_Inactive": 'inactive'},
                              {"Memory_Wired": 'wired'}
                        ],
                    },
                    {
                        "Unit":'Percent',
                        "Array": self._virtual_memory,
                        'Dimensions': [
                            {'Memory_Percentage_Used': 'percent'},
                        ],
                    },
                    {
                        "Unit":'Bytes',
                        "Array": self._swap_memory,
                        'Dimensions': [
                            {'Swap_Total': 'total'},
                            {'Swap_Used': 'used'},
                            {'Swap_Free': 'free'},
                            {'Swap_SIN': 'sin'},
                            {"Swap_SOUT": 'sout'}
                        ],
                    },
                    {
                        "Unit":'Percent',
                        "Array": self._swap_memory,
                        'Dimensions': [
                            {'Swap_Percentage_Used': 'percent'},
                        ],
                    },
                ]
        return metric

    def set_linux_metric(self):
        metric = [
            {
                "Unit":'Bytes',
                "Array": self._virtual_memory,
                'Dimensions': [
                    {'Memory_Total': 'total'},
                    {'Memory_Available': 'available'},
                    {'Memory_Used': 'used'},
                    {'Memory_Free': 'free'},
                    {"Memory_Active": 'active'},
                    {"Memory_Inactive": 'inactive'},
                    {"Memory_Buffered": 'buffered'},
                    {"Memory_Cached": 'cached'},
                ],
            },
            {
                "Unit":'Percent',
                "Array": self._virtual_memory,
                'Dimensions': [
                    {'Memory_Pecentage_Used': 'percent'},
                ],
            },
            {
                "Unit":'Bytes',
                "Array": self._swap_memory,
                'Dimensions': [
                    {'Swap_Total': 'total'},
                    {'Swap_Used': 'used'},
                    {'Swap_Free': 'free'},
                    {'Swap_SIN': 'sin'},
                    {"Swap_SOUT": 'sout'}
                ],
            },
            {
                "Unit":'Percent',
                "Array": self._swap_memory,
                'Dimensions': [
                    {'Swap_Percentage_Used': 'percent'},
                ],
            },
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
                                'Value': 'Memory'
                            },
                            {
                                'Name': 'InstanceId',
                                'Value': instance_id
                            },
                        ],
                        'Value': getattr(unit['Array'], datapoints[point]),
                        'Unit': unit['Unit']
                        })
        if self._debug:
            pprint(data)
        return data



if __name__ == "__main__":
    mem = Memory()
    mem.data('i-afaffaf')
