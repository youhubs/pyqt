# Resource object code (Python 3)
# Created by: object code
# Created by: The Resource Compiler for Qt version 6.6.2
# WARNING! All changes made in this file will be lost!

from PySide6 import QtCore

qt_resource_data = b"\
\x00\x00\x08\xb1\
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
 of the examples\
 of the Qt Toolk\
it.\x0a**\x0a** $QT_BE\
GIN_LICENSE:BSD$\
\x0a** You may use \
this file under \
the terms of the\
 BSD license as \
follows:\x0a**\x0a** \x22\
Redistribution a\
nd use in source\
 and binary form\
s, with or witho\
ut\x0a** modificati\
on, are permitte\
d provided that \
the following co\
nditions are\x0a** \
met:\x0a**   * Redi\
stributions of s\
ource code must \
retain the above\
 copyright\x0a**   \
  notice, this l\
ist of condition\
s and the follow\
ing disclaimer.\x0a\
**   * Redistrib\
utions in binary\
 form must repro\
duce the above c\
opyright\x0a**     \
notice, this lis\
t of conditions \
and the followin\
g disclaimer in\x0a\
**     the docum\
entation and/or \
other materials \
provided with th\
e\x0a**     distrib\
ution.\x0a**   * Ne\
ither the name o\
f Digia Plc and \
its Subsidiary(-\
ies) nor the nam\
es\x0a**     of its\
 contributors ma\
y be used to end\
orse or promote \
products derived\
\x0a**     from thi\
s software witho\
ut specific prio\
r written permis\
sion.\x0a**\x0a**\x0a** T\
HIS SOFTWARE IS \
PROVIDED BY THE \
COPYRIGHT HOLDER\
S AND CONTRIBUTO\
RS\x0a** \x22AS IS\x22 AN\
D ANY EXPRESS OR\
 IMPLIED WARRANT\
IES, INCLUDING, \
BUT NOT\x0a** LIMIT\
ED TO, THE IMPLI\
ED WARRANTIES OF\
 MERCHANTABILITY\
 AND FITNESS FOR\
\x0a** A PARTICULAR\
 PURPOSE ARE DIS\
CLAIMED. IN NO E\
VENT SHALL THE C\
OPYRIGHT\x0a** OWNE\
R OR CONTRIBUTOR\
S BE LIABLE FOR \
ANY DIRECT, INDI\
RECT, INCIDENTAL\
,\x0a** SPECIAL, EX\
EMPLARY, OR CONS\
EQUENTIAL DAMAGE\
S (INCLUDING, BU\
T NOT\x0a** LIMITED\
 TO, PROCUREMENT\
 OF SUBSTITUTE G\
OODS OR SERVICES\
; LOSS OF USE,\x0a*\
* DATA, OR PROFI\
TS; OR BUSINESS \
INTERRUPTION) HO\
WEVER CAUSED AND\
 ON ANY\x0a** THEOR\
Y OF LIABILITY, \
WHETHER IN CONTR\
ACT, STRICT LIAB\
ILITY, OR TORT\x0a*\
* (INCLUDING NEG\
LIGENCE OR OTHER\
WISE) ARISING IN\
 ANY WAY OUT OF \
THE USE\x0a** OF TH\
IS SOFTWARE, EVE\
N IF ADVISED OF \
THE POSSIBILITY \
OF SUCH DAMAGE.\x22\
\x0a**\x0a** $QT_END_L\
ICENSE$\x0a**\x0a*****\
****************\
****************\
****************\
****************\
*******/\x0a\x0aimport\
 QtQuick 2.0\x0a\x0a//\
![0]\x0aListView {\x0a\
    width: 100; \
height: 100\x0a\x0a   \
 model: myModel\x0a\
    delegate: Re\
ctangle {\x0a      \
  height: 25\x0a   \
     width: 100\x0a\
        color: m\
odel.modelData.c\
olor\x0a        Tex\
t { text: name }\
\x0a    }\x0a}\x0a//![0]\x0a\
\
"

qt_resource_name = b"\
\x00\x08\
\x0f\xca[\xbc\
\x00v\
\x00i\x00e\x00w\x00.\x00q\x00m\x00l\
"

qt_resource_struct = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
\x00\x00\x01\x8eh\xfbB\x0c\
"

def qInitResources():
    QtCore.qRegisterResourceData(0x03, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(0x03, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()
