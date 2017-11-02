#
# Transform
#

import attr
from sumtypes import constructor, sumtype, match

print("Start...")

@sumtype
class Transform(object):
    Int_To_String = constructor(
        i=attr.ib(validator=attr.validators.instance_of(int)),
        s=attr.ib(validator=attr.validators.instance_of(str)))
    String_To_Int = constructor(
        s=attr.ib(validator=attr.validators.instance_of(str)),
        i=attr.ib(validator=attr.validators.instance_of(int)))

@match
class transform(object):
    def Int_To_String(i, s):
        return str(i)
    def String_To_Int(s, i):
        return int(s)

i_to_s = Transform.Int_To_String(1, "")

s = transform(i_to_s)

s_to_i = Transform.String_To_Int("2", 0)

i = transform(s_to_i)

print("Finished...")
