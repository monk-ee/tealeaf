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


Example:



Changelog:


Attributes:

put_metric_data(**kwargs)
Publishes metric data points to Amazon CloudWatch. Amazon Cloudwatch associates the data points with the specified metric. If the specified metric does not exist, Amazon CloudWatch creates the metric. It can take up to fifteen minutes for a new metric to appear in calls to the ListMetrics action.

The size of a PutMetricDatarequest is limited to 8 KB for HTTP GET requests and 40 KB for HTTP POST requests.

Warning
Although the Value parameter accepts numbers of type Double , Amazon CloudWatch truncates values with very large exponents. Values with base-10 exponents greater than 126 (1 x 10^126) are truncated. Likewise, values with base-10 exponents less than -130 (1 x 10^-130) are also truncated.
Data that is timestamped 24 hours or more in the past may take in excess of 48 hours to become available from submission time using GetMetricStatistics .



"""
import boto3
import logging
import yaml
import sys, os, time
import imp
from requests import get

class TeaLeafException(Exception): pass


class TeaLeaf:
    _config = None
    _cloudwatch = None
    _instance_id = None
    _debug = False
    _timestamp = time.strftime("%d/%m/%Y %H:%M:%S")
    _modules = {}

    def __init__(self):
        self.load()
        self.instance_id()
        self.connect()
        self.modules()

    def load(self):
        try:
            config_str = open('config.yml', 'r')
            self._config = yaml.load(config_str)
            #set some helpers
            self._debug = self._config['general']['debug']
            if self._debug:
                logfile = self._config['general']['logfile']
                logging.basicConfig(filename=logfile, level=logging.INFO)
        except IOError as error:
            exit("Could not load config.yml: " + str(error))
        except:
            exit("Unexpected error:", sys.exc_info()[0])

    def instance_id(self):
        try:
            #@todo check these are sensible
            self._instance_id = get('http://169.254.169.254/latest/meta-data/instance-id', timeout=1, allow_redirects=False).content
            if self._debug:
                print(self._instance_id)
        except (BaseException) as emsg:
            if self._debug:
                logging.warning(self._timestamp + ': Cannot determine instance id - ' + str(emsg))
                self._instance_id = 'i-xxxxxxxx'
            else:
                exit("Cannot determine instance id.")


    def connect(self):
        try:
            self.cloudwatch = boto3.setup_default_session(region_name=self._config['general']['region'])
            self.cloudwatch = boto3.client('cloudwatch')
        except (BaseException) as emsg:
            if self._debug:
                logging.warning(self._timestamp + ': Cannot connect to Region for CloudWatch - ' + str(emsg))
            exit("Cannot connect to Region for CloudWatch")

    def modules(self):
        for module in self._config['modules']:
            self._modules[module] = self.load_module(module)
            self.post_metric(self._modules[module].data(self._instance_id), module)
        if self._debug:
            print(self._modules)

    def load_module(self, module_name):
        class_inst = None
        python_module = None
        #@todo need to check for pyc here of course in case file is compiled
        try:
            python_module = imp.load_source(module_name, os.path.dirname(os.path.abspath(__file__)) + '/' + str.lower(module_name) + '.py')
        except (BaseException) as emsg:
            if self._debug:
                logging.warning(self._timestamp + ': Cannot load module - ' + str(emsg) + ' - ' + str(module_name))

        if hasattr(python_module, module_name):
            class_inst = getattr(python_module, module_name)()

        return class_inst

    def post_metric(self, module_name, data):
        response = None
        try:
            response = self.cloudwatch.put_metric_data(
                Namespace=self._config['general']['namespace_prefix'] + module_name,
                MetricData=data
            )
        except (BaseException) as emsg:
            if self._debug:
                logging.warning(self._timestamp + ': Cannot post data - ' + str(emsg) + ' - ' + str(data))

        if self._debug:
            logging.info(self._timestamp + ': Metric Post Response ' + str(module_name) + ' - ' + str(data) + ' - ' + str(response))