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
    _debug = False

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
        data = [{
            'MetricName': instance_id + '_Memory_Total',
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
            'Value': getattr(self._virtual_memory, 'total'),
            'Unit': 'Bytes'
        },
            {
                'MetricName': instance_id + '_Memory_Available',
                'Dimensions': [
                    {
                        'Name': 'TeaLeafModule',
                        'Value': 'Memory'
                    },
                    {
                        'Name': 'InstanceId',
                        'Value': instance_id
                    }
                ],
                'Value': getattr(self._virtual_memory, 'available'),
                'Unit': 'Bytes'
            },
            {
                'MetricName': instance_id + '_Memory_Used',
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
                'Value': getattr(self._virtual_memory, 'used'),
                'Unit': 'Bytes'
            },
            {
                'MetricName': instance_id + '_Memory_Free',
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
                'Value': getattr(self._virtual_memory, 'free'),
                'Unit': 'Bytes'
            },
            {
                'MetricName': instance_id + '_Memory_Active',
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
                'Value': getattr(self._virtual_memory, 'active'),
                'Unit': 'Bytes'
            },
            {
                'MetricName': instance_id + '_Memory_Inactive',
                'Dimensions': [
                    {
                        'Name': 'TeaLeafModule',
                        'Value': 'Memory'
                    },                {
                        'Name': 'InstanceId',
                        'Value': instance_id
                    },
                ],
                'Value': getattr(self._virtual_memory, 'inactive'),
                'Unit': 'Bytes'
            },
            {
                'MetricName': instance_id + '_Memory_Wired',
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
                'Value': getattr(self._virtual_memory, 'wired'),
                'Unit': 'Bytes'
            },
            {
                'MetricName': instance_id + '_Memory_Percentage_Used',
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
                'Value': getattr(self._virtual_memory, 'percent'),
                'Unit': 'Percent'
            },
            {
                'MetricName': instance_id + '_Swap_Total',
                'Dimensions': [
                    {
                        'Name': 'TeaLeafModule',
                        'Value': 'Memory'
                    },                {
                        'Name': 'InstanceId',
                        'Value': instance_id
                    },
                ],
                'Value': getattr(self._swap_memory, 'total'),
                'Unit': 'Bytes'
            },
            {
                'MetricName': instance_id + '_Swap_Used',
                'Dimensions': [
                    {
                        'Name': 'TeaLeafModule',
                        'Value': 'Memory'
                    },                {
                        'Name': 'InstanceId',
                        'Value': instance_id
                    },
                ],
                'Value': getattr(self._swap_memory, 'used'),
                'Unit': 'Bytes'
            },
            {
                'MetricName': instance_id + '_Swap_Free',
                'Dimensions': [
                    {
                        'Name': 'TeaLeafModule',
                        'Value': 'Memory'
                    },                {
                        'Name': 'InstanceId',
                        'Value': instance_id
                    },
                ],
                'Value': getattr(self._swap_memory, 'free'),
                'Unit': 'Bytes'
            },
            {
                'MetricName': instance_id + '_Swap_Percentage_Used',
                'Dimensions': [
                    {
                        'Name': 'TeaLeafModule',
                        'Value': 'Memory'
                    },                {
                        'Name': 'InstanceId',
                        'Value': instance_id
                    },
                ],
                'Value': getattr(self._swap_memory, 'percent'),
                'Unit': 'Percent'
            },
            {
                'MetricName': instance_id + '_Swap_SIN',
                'Dimensions': [
                    {
                        'Name': 'TeaLeafModule',
                        'Value': 'Memory'
                    },                {
                        'Name': 'InstanceId',
                        'Value': instance_id
                    },
                ],
                'Value': getattr(self._swap_memory, 'sin'),
                'Unit': 'Bytes'
            },
            {
                'MetricName': instance_id + '_Swap_SOUT',
                'Dimensions': [
                    {
                        'Name': 'TeaLeafModule',
                        'Value': 'Memory'
                    },                {
                        'Name': 'InstanceId',
                        'Value': instance_id
                    },
                ],
                'Value': getattr(self._swap_memory, 'sout'),
                'Unit': 'Bytes'
            }]
        if self._debug:
            pprint(data)
        return data

    def linux_data(self, instance_id):
        data = [{
            'MetricName': instance_id + '_Memory_Total',
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
            'Value': getattr(self._virtual_memory, 'total'),
            'Unit': 'Bytes'
        },
            {
                'MetricName': instance_id + '_Memory_Available',
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
                'Value': getattr(self._virtual_memory, 'available'),
                'Unit': 'Bytes'
            },
            {
                'MetricName': instance_id + '_Memory_Used',
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
                'Value': getattr(self._virtual_memory, 'used'),
                'Unit': 'Bytes'
            },
            {
                'MetricName': instance_id + '_Memory_Free',
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
                'Value': getattr(self._virtual_memory, 'free'),
                'Unit': 'Bytes'
            },
            {
                'MetricName': instance_id + '_Memory_Active',
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
                'Value': getattr(self._virtual_memory, 'active'),
                'Unit': 'Bytes'
            },
            {
                'MetricName': instance_id + '_Memory_Inactive',
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
                'Value': getattr(self._virtual_memory, 'inactive'),
                'Unit': 'Bytes'
            },
            {
                'MetricName': instance_id + '_Memory_Buffers',
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
                'Value': getattr(self._virtual_memory, 'buffers'),
                'Unit': 'Bytes'
            },
            {
                   'MetricName': instance_id + '_Memory_Cached',
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
                   'Value': getattr(self._virtual_memory, 'cached'),
                   'Unit': 'Bytes'
               },
            {
                'MetricName': instance_id + '_Memory_Percentage_Used',
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
                'Value': getattr(self._virtual_memory, 'percent'),
                'Unit': 'Percent'
            },
            {
                'MetricName': instance_id + '_Swap_Total',
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
                'Value': getattr(self._swap_memory, 'total'),
                'Unit': 'Bytes'
            },
            {
                'MetricName': instance_id + '_Swap_Used',
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
                'Value': getattr(self._swap_memory, 'used'),
                'Unit': 'Bytes'
            },
            {
                'MetricName': instance_id + '_Swap_Free',
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
                'Value': getattr(self._swap_memory, 'free'),
                'Unit': 'Bytes'
            },
            {
                'MetricName': instance_id + '_Swap_Percentage_Used',
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
                'Value': getattr(self._swap_memory, 'percent'),
                'Unit': 'Percent'
            },
            {
                'MetricName': instance_id + '_Swap_SIN',
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
                'Value': getattr(self._swap_memory, 'sin'),
                'Unit': 'Bytes'
            },
            {
                'MetricName': instance_id + '_Swap_SOUT',
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
                'Value': getattr(self._swap_memory, 'sout'),
                'Unit': 'Bytes'
            }]
        if self._debug:
            pprint(data)
        return data


if __name__ == "__main__":
    mem = Memory()
    mem.data('i-afaffaf')
