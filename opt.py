#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse

arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('--log',
                        type=str,
                        dest='log',
                        default=None)

opt, _ = arg_parser.parse_known_args()