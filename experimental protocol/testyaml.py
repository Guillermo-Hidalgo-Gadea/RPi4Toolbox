#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 10:56:23 2021

@author: guillermo
"""

import yaml

# data = yaml.load(filepath)

filepath = "protocol.yaml"

with open(filepath, "r") as stream:
    data = yaml.full_load(stream)
    for entry in data:
        print(entry)
        print(type(entry))

print(yaml.dump(data))

print(yaml.dump(data["subjects"]))

