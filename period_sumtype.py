""" Python Algebraic Data Types (ADTs)

    `Period` example from `Stupid Python Ideas`
    Implemented in using SumTypes Pytohn package
"""

# %%
import attr
from datetime import date
from sumtypes import sumtype, constructor, match

@sumtype
class PeriodSumtype(object):
    DurationPeriod = constructor('start_date', 'duration')
    DatePeriod = constructor('end_date', 'start_date')

# type durationPeriod = end_date * duration
# type datePeriod = end_date * start_date
# type Period = durationPeriod | datePeriod

# type printPeriod = Period -> String
@match(PeriodSumtype)
class print_period(object):
    def DurationPeriod(start_date, duration):
        return "start_date: {0}\n  duration: {1}".format(str(start_date), str(duration)), 
    def DatePeriod(start_date, end_date):
        return "start_date: {0}\n  end_date: {1}".format(str(start_date), str(end_date))

start = date(2017, 7, 28)
end = date(2017, 8, 28)
duration = "1M"

# assert get_num(MyType.NamedNum('foo', 1)) == 1
# assert get_num(MyType.AnonymousNum(2)) == 2

print("DurationPeriod:\n{}".format(print_period(PeriodSumtype.DurationPeriod(start, duration))))
print("DatePeriod:\n{}".format(print_period(PeriodSumtype.DatePeriod(start, end))))

print("Finished...")

# %%

@sumtype
class PeriodAttrtype(object):
    DurationPeriod = constructor(
        start_date = attr.ib(validator=attr.validators.instance_of(date)),
        duration = attr.ib(validator=attr.validators.instance_of(str)))
    DatePeriod = constructor(
        start_date = attr.ib(validator=attr.validators.instance_of(date)),
        end_date = attr.ib(validator=attr.validators.instance_of(date)))

@sumtype
class Period(object):
    Sumtype = constructor(
        sum_type = attr.ib(validator=attr.validators.instance_of(PeriodSumtype)))
    Attrtype = constructor(
        attr_type = attr.ib(validator=attr.validators.instance_of(PeriodAttrtype)))
