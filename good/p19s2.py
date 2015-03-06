from dateutil.rrule import DAILY,rrule
from dateutil.relativedelta import SU
from datetime import datetime


RR = rrule(DAILY, bymonthday=1, byweekday=(SU), cache=True, dtstart=datetime(1901,1,1), until=datetime(2000,12,31))
print len(list(RR))
