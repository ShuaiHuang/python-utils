#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from opt import opt

LOG_FORMAT = '[%(asctime)s] [%(filename)s@%(lineno)d] [%(levelname)s] %(message)s'
logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT, filename=opt.log)