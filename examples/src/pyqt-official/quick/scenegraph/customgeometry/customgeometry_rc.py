# Resource object code (Python 3)
# Created by: object code
# Created by: The Resource Compiler for Qt version 6.6.2
# WARNING! All changes made in this file will be lost!

from PySide6 import QtCore

qt_resource_data = b"\
\x00\x00\x0a\xac\
/\
****************\
****************\
****************\
****************\
************\x0a**\x0a\
** Copyright (C)\
 2013 Digia Plc \
and/or its subsi\
diary(-ies).\x0a** \
Contact: http://\
www.qt-project.o\
rg/legal\x0a**\x0a** T\
his file is part\
 of the demonstr\
ation applicatio\
ns of the Qt Too\
lkit.\x0a**\x0a** $QT_\
BEGIN_LICENSE:LG\
PL$\x0a** Commercia\
l License Usage\x0a\
** Licensees hol\
ding valid comme\
rcial Qt license\
s may use this f\
ile in\x0a** accord\
ance with the co\
mmercial license\
 agreement provi\
ded with the\x0a** \
Software or, alt\
ernatively, in a\
ccordance with t\
he terms contain\
ed in\x0a** a writt\
en agreement bet\
ween you and Dig\
ia.  For licensi\
ng terms and\x0a** \
conditions see h\
ttp://qt.digia.c\
om/licensing.  F\
or further infor\
mation\x0a** use th\
e contact form a\
t http://qt.digi\
a.com/contact-us\
.\x0a**\x0a** GNU Less\
er General Publi\
c License Usage\x0a\
** Alternatively\
, this file may \
be used under th\
e terms of the G\
NU Lesser\x0a** Gen\
eral Public Lice\
nse version 2.1 \
as published by \
the Free Softwar\
e\x0a** Foundation \
and appearing in\
 the file LICENS\
E.LGPL included \
in the\x0a** packag\
ing of this file\
.  Please review\
 the following i\
nformation to\x0a**\
 ensure the GNU \
Lesser General P\
ublic License ve\
rsion 2.1 requir\
ements\x0a** will b\
e met: http://ww\
w.gnu.org/licens\
es/old-licenses/\
lgpl-2.1.html.\x0a*\
*\x0a** In addition\
, as a special e\
xception, Digia \
gives you certai\
n additional\x0a** \
rights.  These r\
ights are descri\
bed in the Digia\
 Qt LGPL Excepti\
on\x0a** version 1.\
1, included in t\
he file LGPL_EXC\
EPTION.txt in th\
is package.\x0a**\x0a*\
* GNU General Pu\
blic License Usa\
ge\x0a** Alternativ\
ely, this file m\
ay be used under\
 the terms of th\
e GNU\x0a** General\
 Public License \
version 3.0 as p\
ublished by the \
Free Software\x0a**\
 Foundation and \
appearing in the\
 file LICENSE.GP\
L included in th\
e\x0a** packaging o\
f this file.  Pl\
ease review the \
following inform\
ation to\x0a** ensu\
re the GNU Gener\
al Public Licens\
e version 3.0 re\
quirements will \
be\x0a** met: http:\
//www.gnu.org/co\
pyleft/gpl.html.\
\x0a**\x0a**\x0a** $QT_EN\
D_LICENSE$\x0a**\x0a**\
****************\
****************\
****************\
****************\
**********/\x0a\x0aimp\
ort QtQuick 2.0\x0a\
import CustomGeo\
metry 1.0\x0a\x0aItem \
{\x0a    width: 300\
\x0a    height: 200\
\x0a\x0a    BezierCurv\
e {\x0a        id: \
line\x0a        anc\
hors.fill: paren\
t\x0a        anchor\
s.margins: 20\x0a\x0a \
       property \
real t\x0a        S\
equentialAnimati\
on on t {\x0a      \
      NumberAnim\
ation { to: 1; d\
uration: 2000; e\
asing.type: Easi\
ng.InOutQuad }\x0a \
           Numbe\
rAnimation { to:\
 0; duration: 20\
00; easing.type:\
 Easing.InOutQua\
d }\x0a            \
loops: Animation\
.Infinite\x0a      \
  }\x0a\x0a        p2:\
 Qt.point(t, 1 -\
 t)\x0a        p3: \
Qt.point(1 - t, \
t)\x0a    }\x0a\x0a    Te\
xt {\x0a        anc\
hors.bottom: lin\
e.bottom\x0a\x0a      \
  x: 20\x0a        \
width: parent.wi\
dth - 40\x0a       \
 wrapMode: Text.\
WordWrap\x0a\x0a      \
  text: \x22This cu\
rve is a custom \
scene graph item\
, implemented us\
ing GL_LINE_STRI\
P\x22\x0a    }\x0a}\x0a\
"

qt_resource_name = b"\
\x00\x0a\
\x04\xb1\xbb\xe8\
\x00s\
\x00c\x00e\x00n\x00e\x00g\x00r\x00a\x00p\x00h\
\x00\x0e\
\x055\x16\x99\
\x00c\
\x00u\x00s\x00t\x00o\x00m\x00g\x00e\x00o\x00m\x00e\x00t\x00r\x00y\
\x00\x08\
\x08\x01Z\x5c\
\x00m\
\x00a\x00i\x00n\x00.\x00q\x00m\x00l\
"

qt_resource_struct = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x02\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x1a\x00\x02\x00\x00\x00\x01\x00\x00\x00\x03\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00<\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
\x00\x00\x01\x8eh\xfbB\x0c\
"

def qInitResources():
    QtCore.qRegisterResourceData(0x03, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(0x03, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()
