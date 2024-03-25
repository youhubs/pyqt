# Resource object code (Python 3)
# Created by: object code
# Created by: The Resource Compiler for Qt version 6.6.2
# WARNING! All changes made in this file will be lost!

from PySide6 import QtCore

qt_resource_data = b"\
\x00\x00\x03\xfd\
<\
html><body>\x0a<h1>\
\x0aThe Green Peopl\
e Book Club\x0a</h1\
>\x0a\x0a<p>\x0aWelcome t\
o The Green Peop\
le Book Club. Pl\
ease register to\
 obtain a member\
ship with us.\x0a</\
p>\x0a    <form ons\
ubmit=\x22formExtra\
ctor.submit()\x22>\x0a\
    <table>\x0a    \
<tbody><tr>\x0a    \
    <td>\x0a       \
 First name:\x0a   \
     </td>\x0a     \
   <td>\x0a        \
    <input type=\
\x22text\x22 id=\x22first\
name\x22>\x0a        <\
/td>\x0a    </tr>\x0a \
   <tr>\x0a        \
<td>\x0a        Las\
t name:\x0a        \
</td>\x0a        <t\
d>\x0a            <\
input type=\x22text\
\x22 id=\x22lastname\x22>\
\x0a        </td>\x0a \
   </tr>\x0a    <tr\
>\x0a        <td>\x0a \
       Gender:\x0a \
       </td>\x0a   \
     <td>\x0a      \
  <input type=\x22r\
adio\x22 name=\x22gend\
er\x22 id=\x22genderMa\
le\x22 value=\x22Male\x22\
> Male\x0a        <\
input type=\x22radi\
o\x22 name=\x22gender\x22\
 id=\x22genderFemal\
e\x22 value=\x22Female\
\x22> Female\x0a      \
  </td>\x0a    </tr\
>\x0a    <tr>\x0a     \
   <td colspan=\x22\
2\x22>\x0a        <inp\
ut type=\x22checkbo\
x\x22 id=\x22updates\x22 \
value=\x22receive\x22>\
\x0a        Check h\
ere if you would\
 like to receive\
 regular updates\
 from us:\x0a      \
  </td>\x0a    </tr\
>\x0a    </tbody></\
table>\x0a    <inpu\
t type=\x22submit\x22 \
value=\x22Submit\x22>\x0a\
    </form>\x0a\x0a</b\
ody></html>\x0a\
"

qt_resource_name = b"\
\x00\x09\
\x09\x04!\xfc\
\x00f\
\x00o\x00r\x00m\x00.\x00h\x00t\x00m\x00l\
"

qt_resource_struct = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
\x00\x00\x01\x8eh\xfbB\x19\
"

def qInitResources():
    QtCore.qRegisterResourceData(0x03, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(0x03, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()
