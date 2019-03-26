# -*- coding: utf-8 -*-

import datetime
import time
import pytz
import dateutil.relativedelta as drel
from dateutil import parser
from dateutil.rrule import *

utc_0 = int(time.mktime(datetime.datetime(1970, 01, 01).timetuple()))


def now_time():
    """
    今天时间 年月日时分秒

    :return:
    """
    now = datetime.datetime.now()
    return now
    
   
   def get_utc_millis():
    """
    获取系统从1970-1-1至今的utc毫秒数
    :return: 13位毫秒数
    """
    return datetime_to_utc_ms(datetime.datetime.utcnow())
   
