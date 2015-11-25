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
Request Syntax

response = client.put_metric_data(
    Namespace='string',
    MetricData=[
        {
            'MetricName': 'string',
            'Dimensions': [
                {
                    'Name': 'string',
                    'Value': 'string'
                },
            ],
            'Timestamp': datetime(2015, 1, 1),
            'Value': 123.0,
            'StatisticValues': {
                'SampleCount': 123.0,
                'Sum': 123.0,
                'Minimum': 123.0,
                'Maximum': 123.0
            },
            'Unit': 'Seconds'|'Microseconds'|'Milliseconds'|'Bytes'|'Kilobytes'|'Megabytes'|'Gigabytes'|'Terabytes'|'Bits'|'Kilobits'|'Megabits'|'Gigabits'|'Terabits'|'Percent'|'Count'|'Bytes/Second'|'Kilobytes/Second'|'Megabytes/Second'|'Gigabytes/Second'|'Terabytes/Second'|'Bits/Second'|'Kilobits/Second'|'Megabits/Second'|'Gigabits/Second'|'Terabits/Second'|'Count/Second'|'None'
        },
    ]
)
Parameters
Namespace (string) --
[REQUIRED]

The namespace for the metric data.

MetricData (list) --
[REQUIRED]

A list of data describing the metric.

(dict) --
The MetricDatum data type encapsulates the information sent with PutMetricData to either create a new metric or add new values to be aggregated into an existing metric.

MetricName (string) -- [REQUIRED]
The name of the metric.

Dimensions (list) --
A list of dimensions associated with the metric. Note, when using the Dimensions value in a query, you need to append .member.N to it (e.g., Dimensions.member.N).

(dict) --
The Dimension data type further expands on the identity of a metric using a Name, Value pair.

For examples that use one or more dimensions, see PutMetricData .

Name (string) -- [REQUIRED]
The name of the dimension.

Value (string) -- [REQUIRED]
The value representing the dimension measurement

Timestamp (datetime) --
The time stamp used for the metric. If not specified, the default value is set to the time the metric data was received. Amazon CloudWatch uses Coordinated Universal Time (UTC) when returning time stamps, which do not accommodate seasonal adjustments such as daylight savings time. For more information, see Time stamps in the Amazon CloudWatch Developer Guide .

Value (float) --
The value for the metric.

Warning
Although the Value parameter accepts numbers of type Double , Amazon CloudWatch truncates values with very large exponents. Values with base-10 exponents greater than 126 (1 x 10^126) are truncated. Likewise, values with base-10 exponents less than -130 (1 x 10^-130) are also truncated.
StatisticValues (dict) --
A set of statistical values describing the metric.

SampleCount (float) -- [REQUIRED]
The number of samples used for the statistic set.

Sum (float) -- [REQUIRED]
The sum of values for the sample set.

Minimum (float) -- [REQUIRED]
The minimum value of the sample set.

Maximum (float) -- [REQUIRED]
The maximum value of the sample set.

Unit (string) --
The unit of the metric.

Returns
None
"""
import time


class ExampleModule:
    _timestamp = time.strftime("%d/%m/%Y %H:%M:%S")


def __init__(self): pass


def data(self, instance_id):
    data = [{
        'MetricName': instance_id + 'ExampleModule',
        'MetricName': 'string',
        'Dimensions': [
            {
                'Name': 'string',
                'Value': 'string'
            },
        ],
        'Timestamp': self._timestamp,
        'Value': 123.0,
        'StatisticValues': {
            'SampleCount': 123.0,
            'Sum': 123.0,
            'Minimum': 123.0,
            'Maximum': 123.0
        },
        'Unit': 'Seconds' | 'Microseconds' | 'Milliseconds' | 'Bytes' | 'Kilobytes' | 'Megabytes' | 'Gigabytes' | 'Terabytes' | 'Bits' | 'Kilobits' | 'Megabits' | 'Gigabits' | 'Terabits' | 'Percent' | 'Count' | 'Bytes/Second' | 'Kilobytes/Second' | 'Megabytes/Second' | 'Gigabytes/Second' | 'Terabytes/Second' | 'Bits/Second' | 'Kilobits/Second' | 'Megabits/Second' | 'Gigabits/Second' | 'Terabits/Second' | 'Count/Second' | 'None'
    }]

    return data
