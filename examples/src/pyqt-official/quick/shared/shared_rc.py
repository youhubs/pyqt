# Resource object code (Python 3)
# Created by: object code
# Created by: The Resource Compiler for Qt version 6.6.2
# WARNING! All changes made in this file will be lost!

from PySide6 import QtCore

qt_resource_data = b"\
\x00\x00\x0c\xd7\
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
*******/\x0aimport \
QtQuick 2.0\x0a\x0aRec\
tangle {\x0a    id:\
 container\x0a    p\
roperty Item exa\
mpleItem\x0a    wid\
th: ListView.vie\
w.width\x0a    heig\
ht: button.impli\
citHeight + 22\x0a\x0a\
    gradient: Gr\
adient {\x0a       \
 GradientStop {\x0a\
            posi\
tion: 0\x0a        \
    Behavior on \
color {ColorAnim\
ation { duration\
: 100 }}\x0a       \
     color: butt\
on.pressed ? \x22#e\
0e0e0\x22 : \x22#fff\x22\x0a\
        }\x0a      \
  GradientStop {\
\x0a            pos\
ition: 1\x0a       \
     Behavior on\
 color {ColorAni\
mation { duratio\
n: 100 }}\x0a      \
      color: but\
ton.pressed ? \x22#\
e0e0e0\x22 : button\
.containsMouse ?\
 \x22#f5f5f5\x22 : \x22#e\
ee\x22\x0a        }\x0a  \
  }\x0a\x0a    Image {\
\x0a        id: ima\
ge\x0a        opaci\
ty: 0.7\x0a        \
Behavior on opac\
ity {NumberAnima\
tion {duration: \
100}}\x0a        so\
urce: \x22images/ne\
xt.png\x22\x0a        \
anchors.vertical\
Center: parent.v\
erticalCenter\x0a  \
      anchors.ri\
ght: parent.righ\
t\x0a        anchor\
s.rightMargin: 1\
6\x0a    }\x0a\x0a    But\
ton {\x0a        id\
: button\x0a       \
 anchors.top: pa\
rent.top\x0a       \
 anchors.left: p\
arent.left\x0a     \
   anchors.botto\
m: parent.bottom\
\x0a        anchors\
.right:image.lef\
t\x0a        text: \
name\x0a        sub\
Text: descriptio\
n\x0a        onClic\
ked: exampleItem\
.exampleUrl = ur\
l;\x0a    }\x0a\x0a    Re\
ctangle {\x0a      \
  height: 1\x0a    \
    color: \x22#ccc\
\x22\x0a        anchor\
s.bottom: parent\
.bottom\x0a        \
anchors.left: pa\
rent.left\x0a      \
  anchors.right:\
 parent.right\x0a  \
  }\x0a}\x0a\
\x00\x00\x146\
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
*******/\x0aimport \
QtQuick 2.0\x0a\x0aRec\
tangle {\x0a    //m\
odel is a list o\
f {\x22name\x22:\x22somen\
ame\x22, \x22url\x22:\x22fil\
e:///some/url/ma\
infile.qml\x22}\x0a   \
 //function used\
 to add to model\
 A) to enforce s\
cheme B) to allo\
w Qt.resolveUrl \
in url assignmen\
ts\x0a\x0a    color: \x22\
#eee\x22\x0a    functi\
on addExample(na\
me, desc, url)\x0a \
   {\x0a        myM\
odel.append({\x22na\
me\x22:name, \x22descr\
iption\x22:desc, \x22u\
rl\x22:url})\x0a    }\x0a\
    function hid\
eExample()\x0a    {\
\x0a        ei.visi\
ble = false;\x0a   \
 }\x0a\x0a    ListView\
 {\x0a        clip:\
 true\x0a        de\
legate: SimpleLa\
uncherDelegate{e\
xampleItem: ei}\x0a\
        model: L\
istModel {id:myM\
odel}\x0a        an\
chors.fill: pare\
nt\x0a    }\x0a\x0a    It\
em {\x0a        id:\
 ei\x0a        visi\
ble: false\x0a     \
   clip: true\x0a  \
      property u\
rl exampleUrl\x0a  \
      onExampleU\
rlChanged: visib\
le = (exampleUrl\
 == '' ? false :\
 true); //Settin\
g exampleUrl aut\
omatically shows\
 example\x0a       \
 anchors.fill: p\
arent\x0a        an\
chors.bottomMarg\
in: 40\x0a        R\
ectangle {\x0a     \
       id: bg\x0a  \
          anchor\
s.fill: parent\x0a \
           color\
: \x22white\x22\x0a      \
  }\x0a        Mous\
eArea{\x0a         \
   anchors.fill:\
 parent\x0a        \
    enabled: ei.\
visible\x0a        \
    //Eats mouse\
 events\x0a        \
}\x0a        Loader\
{\x0a            fo\
cus: true\x0a      \
      source: ei\
.exampleUrl\x0a    \
        anchors.\
fill: parent\x0a   \
     }\x0a    }\x0a   \
 Rectangle {\x0a   \
     id: bar\x0a   \
     visible: ei\
.visible\x0a       \
 anchors.bottom:\
 parent.bottom\x0a \
       width: pa\
rent.width\x0a     \
   height: 40\x0a\x0a \
       Rectangle\
 {\x0a            h\
eight: 1\x0a       \
     color: \x22#cc\
c\x22\x0a            a\
nchors.top: pare\
nt.top\x0a         \
   anchors.left:\
 parent.left\x0a   \
         anchors\
.right: parent.r\
ight\x0a        }\x0a\x0a\
        Rectangl\
e {\x0a            \
height: 1\x0a      \
      color: \x22#f\
ff\x22\x0a            \
anchors.top: par\
ent.top\x0a        \
    anchors.topM\
argin: 1\x0a       \
     anchors.lef\
t: parent.left\x0a \
           ancho\
rs.right: parent\
.right\x0a        }\
\x0a\x0a        gradie\
nt: Gradient {\x0a \
           Gradi\
entStop { positi\
on: 0 ; color: \x22\
#eee\x22 }\x0a        \
    GradientStop\
 { position: 1 ;\
 color: \x22#ccc\x22 }\
\x0a        }\x0a\x0a    \
    MouseArea{\x0a \
           ancho\
rs.fill: parent\x0a\
            enab\
led: ei.visible\x0a\
            //Ea\
ts mouse events\x0a\
        }\x0a\x0a     \
   Image {\x0a     \
       id: back\x0a\
            sour\
ce: \x22images/back\
.png\x22\x0a          \
  anchors.vertic\
alCenter: parent\
.verticalCenter\x0a\
            anch\
ors.verticalCent\
erOffset: 2\x0a    \
        anchors.\
left: parent.lef\
t\x0a            an\
chors.leftMargin\
: 16\x0a\x0a          \
  MouseArea {\x0a  \
              id\
: mouse\x0a        \
        hoverEna\
bled: true\x0a     \
           ancho\
rs.centerIn: par\
ent\x0a            \
    width: 38\x0a  \
              he\
ight: 31\x0a       \
         anchors\
.verticalCenterO\
ffset: -1\x0a      \
          onClic\
ked: ei.exampleU\
rl = \x22\x22\x0a        \
        Rectangl\
e {\x0a            \
        anchors.\
fill: parent\x0a   \
                \
 opacity: mouse.\
pressed ? 1 : 0\x0a\
                \
    Behavior on \
opacity { Number\
Animation{ durat\
ion: 100 }}\x0a    \
                \
gradient: Gradie\
nt {\x0a           \
             Gra\
dientStop { posi\
tion: 0 ; color:\
 \x22#22000000\x22 }\x0a \
                \
       GradientS\
top { position: \
0.2 ; color: \x22#1\
1000000\x22 }\x0a     \
               }\
\x0a               \
     border.colo\
r: \x22darkgray\x22\x0a  \
                \
  antialiasing: \
true\x0a           \
         radius:\
 4\x0a             \
   }\x0a           \
 }\x0a        }\x0a   \
 }\x0a}\x0a\
\x00\x00\x0c\xdb\
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
 QtQuick 2.0\x0a\x0aIt\
em {\x0a    id: con\
tainer\x0a\x0a    prop\
erty string text\
: \x22Button\x22\x0a    p\
roperty string s\
ubText: \x22\x22\x0a    s\
ignal clicked\x0a  \
  property alias\
 containsMouse: \
mouseArea.contai\
nsMouse\x0a    prop\
erty alias press\
ed: mouseArea.pr\
essed\x0a    implic\
itHeight: col.he\
ight\x0a    height:\
 implicitHeight\x0a\
    width: butto\
nLabel.width + 2\
0\x0a\x0a    MouseArea\
 {\x0a        id: m\
ouseArea\x0a       \
 anchors.fill: p\
arent\x0a        on\
Clicked: contain\
er.clicked()\x0a   \
     hoverEnable\
d: true\x0a    }\x0a\x0a \
   Column {\x0a    \
    spacing: 2\x0a \
       id: col\x0a \
       anchors.v\
erticalCenter: p\
arent.verticalCe\
nter\x0a        wid\
th: parent.width\
\x0a        Text {\x0a\
            id: \
buttonLabel\x0a    \
        anchors.\
left: parent.lef\
t\x0a            an\
chors.leftMargin\
: 10\x0a           \
 anchors.right: \
parent.right\x0a   \
         anchors\
.rightMargin: 10\
\x0a            tex\
t: container.tex\
t\x0a            co\
lor: \x22black\x22\x0a   \
         font.pi\
xelSize: 22\x0a    \
        wrapMode\
: Text.WrapAtWor\
dBoundaryOrAnywh\
ere\x0a            \
styleColor: \x22whi\
te\x22\x0a            \
style: Text.Rais\
ed\x0a\x0a        }\x0a  \
      Text {\x0a   \
         id: but\
tonLabel2\x0a      \
      anchors.le\
ft: parent.left\x0a\
            anch\
ors.leftMargin: \
10\x0a            t\
ext: container.s\
ubText\x0a         \
   wrapMode: Tex\
t.WrapAtWordBoun\
daryOrAnywhere\x0a \
           color\
: \x22#666\x22\x0a       \
     font.pixelS\
ize: 12\x0a        \
}\x0a    }\x0a}\x0a\
\x00\x00\x066\
\x89\
PNG\x0d\x0a\x1a\x0a\x00\x00\x00\x0dIHDR\x00\
\x00\x00\x0d\x00\x00\x00\x17\x08\x06\x00\x00\x00\xd0\xa6\xc5\x81\
\x00\x00\x00\x19tEXtSoftware\
\x00Adobe ImageRead\
yq\xc9e<\x00\x00\x03$iTXtXML\
:com.adobe.xmp\x00\x00\
\x00\x00\x00<?xpacket beg\
in=\x22\xef\xbb\xbf\x22 id=\x22W5M\
0MpCehiHzreSzNTc\
zkc9d\x22?> <x:xmpm\
eta xmlns:x=\x22ado\
be:ns:meta/\x22 x:x\
mptk=\x22Adobe XMP \
Core 5.3-c011 66\
.145661, 2012/02\
/06-14:56:27    \
    \x22> <rdf:RDF \
xmlns:rdf=\x22http:\
//www.w3.org/199\
9/02/22-rdf-synt\
ax-ns#\x22> <rdf:De\
scription rdf:ab\
out=\x22\x22 xmlns:xmp\
=\x22http://ns.adob\
e.com/xap/1.0/\x22 \
xmlns:xmpMM=\x22htt\
p://ns.adobe.com\
/xap/1.0/mm/\x22 xm\
lns:stRef=\x22http:\
//ns.adobe.com/x\
ap/1.0/sType/Res\
ourceRef#\x22 xmp:C\
reatorTool=\x22Adob\
e Photoshop CS6 \
(Macintosh)\x22 xmp\
MM:InstanceID=\x22x\
mp.iid:DCE827695\
74811E2B0EE92BEE\
27047DB\x22 xmpMM:D\
ocumentID=\x22xmp.d\
id:DCE8276A57481\
1E2B0EE92BEE2704\
7DB\x22> <xmpMM:Der\
ivedFrom stRef:i\
nstanceID=\x22xmp.i\
id:DCE8276757481\
1E2B0EE92BEE2704\
7DB\x22 stRef:docum\
entID=\x22xmp.did:D\
CE82768574811E2B\
0EE92BEE27047DB\x22\
/> </rdf:Descrip\
tion> </rdf:RDF>\
 </x:xmpmeta> <?\
xpacket end=\x22r\x22?\
>\x97\xa0=\xd8\x00\x00\x02\xa8IDATx\xda\x8c\
\x94_HSQ\x1c\xc7\xcf\xbd\xbb\xd7;\xb7\xdd\xddQ\
\x90\xbe\x0cb\x9b\x93\xd4\xf5\x10\xc1\x0a\xf4\xc5)\xd8\x1f\
)Fd\xd4C\xeaK\xe4CB\xf6\x98\xb4\xb5\xad=\
\xc8\xe8\xc9\xf5\x1e\xf4\x92\xd2\x96E\xeb!Y\x96\xc5\x94\
\xc2\x94\x05\xb2\xf9\x10H\xed\xa1\x8767\xc1\xfd\xf3\xf6\
=\xd7ML\x97z\xe0\xcb\xdd\xef\xdc}8\xbf\xf3\xfd\
\x9es\x19Y\x96\xc9A\xc3j\xb5\x0ep\x1c\xf7\x98\xc8\
r\xa1P,\xde`\x0e\x82\xdaZ[\xefiu\xba1\
\xb5 \x90r\xb9Lr\xeb\xeb1n?\xc0f\xb3\xb9\
\x0c\x06\xc3\x03Q\xaf'u<O\x0a\x85\x02\x11Eq\
\xb5&d6\x99\x18\xadV;\x06`D\x02\xa0\xd1h\
\x94\xf9c\x0d\x0d?\xfc~\xff\xcc\x1e\xc8l6\xabt\
:\xdd\xb8$I\xb7 R__O\x18\x86!\x8d\x8d\
\x8d\x09\xaf\xcf7\xb1g%\xcb\x16\xf0\xd4 I\xd7\xf5\
U\x00\xf3F\xa3\xf1\xbb\xc7\xeb\x0d\xa1^A\xf9v\x1b\
\xb2X,u:Q\x9c\x04\xd0\xabGK\xea\x0a`2\
\x99\xbe=\xf4x\xa6x\x9e_F9\x09\x15\xb9\x0a\xa0\
\xc1\xb2/\x01t)\x80ZM\xa8\xa7\xd6\xe6\xe6y\xb7\
\xdb\x1daY6\x8e2\x04\x95\xe9\xff\x19\xb4$\x01x\
-\x19\x0c\xedzQ\xdc\x06N\xdal\xb3\xf7GG\xa7\
\xf1s\x01z\x05mV\xbb\xe2\x90\xc1sl\xb8]\xaa\
\xae\x80\xdc\xce\xd8\xed\xd3wGFf\xf1~\x1e\x8a@\
\xff\x84\xc9\xc1\xdaN\xecE\xb1\x95\xba\x84\xf6V\xef\x0c\
\x0f\x7f\xc2;\x0a\xbd\xab\x15\x09\xdb\xda\xd2\xf2\x91\xe78\
\x82\xbe\x95\x89T*e\xbc\xd6\xd7w\x16'\xe1\xfd\xff\
Bg\xc7\x83\xc1\x0f8[\x0b\xa5RI\x99P\xa9T\
$\x9dNw\xd7\x09\xc2\x0b\xeahM\x08V~y\xe4\
\xf7O\xc1\xa99\x0a\xa2&h\x99`\x8f\xbd0(\xd2\
\x04gwC\xf4\xc0\xd2\xbe.B\xa7|^o\xe7\xe2\
\xd2R\x07\xcd'\x9f\xcf\x93\xcc\xda\x1a\xc9\xa4\xd3\x9f\xb3\
\xb9\xdc\xf9d2\x99\xd9\x09)O\xa8\x07\xb2\x07\x02\x81\
\xf6\xb9X\xccA\xf7\xb8\xb1\xb1A\xd6\x00\xa63\x99\xaf\
\xb9\x5c\xee\x5c\x22\x91\xf8\xbd\x13\xaa\x0e\x07\xd4\xf1$\x18\
<\x1d\x8dF/( V\xccf\xb3t\x9fq<{\
\x00\xfe\xdc}`i\x98\xf9\xdbCC4\xb3\xe2\x9bH\
\xe4\x12\xee\x11\xc3l\xb5\xd2\x06\xcd\xc04G\xad\xabA\
\xf3\xc9\x0f\x0c\x0eR\xb0\x10\x0e\x87\xaf\x08\x82\xc0\xd2\x0c\
\xd1\x93yS\x96C*\x97\xcbU\xcb\xd5_\xd0\x1f\x5c\
\xc2\xa3\x88 \x15\x8f\xc7O\xe0\xc9\x22}\xb2Y.\x1f\
a\xf7\xb9\xb8\x8b\xd0\x84\xd3\xe9\x5c\xbe\xd9\xdf\xff\x0c\xdf\
\x88\x0c\x96+uuw\x87\x99C|X\x9a\xa0\xab\x10\
_\xa9K\x87\x81\xe88\x0e]\x86\xb4\xf4<\xfe\x15`\
\x00\x07\x7f\xeb\x18\x9af\x83_\x00\x00\x00\x00IEN\
D\xaeB`\x82\
\x00\x00\x05[\
\x89\
PNG\x0d\x0a\x1a\x0a\x00\x00\x00\x0dIHDR\x00\
\x00\x00\x12\x00\x00\x00\x1f\x08\x06\x00\x00\x00\xeaP\x9d\x89\
\x00\x00\x00\x19tEXtSoftware\
\x00Adobe ImageRead\
yq\xc9e<\x00\x00\x03$iTXtXML\
:com.adobe.xmp\x00\x00\
\x00\x00\x00<?xpacket beg\
in=\x22\xef\xbb\xbf\x22 id=\x22W5M\
0MpCehiHzreSzNTc\
zkc9d\x22?> <x:xmpm\
eta xmlns:x=\x22ado\
be:ns:meta/\x22 x:x\
mptk=\x22Adobe XMP \
Core 5.3-c011 66\
.145661, 2012/02\
/06-14:56:27    \
    \x22> <rdf:RDF \
xmlns:rdf=\x22http:\
//www.w3.org/199\
9/02/22-rdf-synt\
ax-ns#\x22> <rdf:De\
scription rdf:ab\
out=\x22\x22 xmlns:xmp\
=\x22http://ns.adob\
e.com/xap/1.0/\x22 \
xmlns:xmpMM=\x22htt\
p://ns.adobe.com\
/xap/1.0/mm/\x22 xm\
lns:stRef=\x22http:\
//ns.adobe.com/x\
ap/1.0/sType/Res\
ourceRef#\x22 xmp:C\
reatorTool=\x22Adob\
e Photoshop CS6 \
(Macintosh)\x22 xmp\
MM:InstanceID=\x22x\
mp.iid:DCE827655\
74811E2B0EE92BEE\
27047DB\x22 xmpMM:D\
ocumentID=\x22xmp.d\
id:DCE8276657481\
1E2B0EE92BEE2704\
7DB\x22> <xmpMM:Der\
ivedFrom stRef:i\
nstanceID=\x22xmp.i\
id:DCE8276357481\
1E2B0EE92BEE2704\
7DB\x22 stRef:docum\
entID=\x22xmp.did:D\
CE82764574811E2B\
0EE92BEE27047DB\x22\
/> </rdf:Descrip\
tion> </rdf:RDF>\
 </x:xmpmeta> <?\
xpacket end=\x22r\x22?\
>\xd9\x0c\xdf\xc0\x00\x00\x01\xcdIDATx\xda\xac\
\x95;K\x03A\x14\x857\x994\xdaF1>@\xc5\
\x88A\x8c,*\x16b#XZ\x08\x06\x04\x0b\xa3\xad\
\x85\x9d`\x13\x0b\x1bm,5\x8d\x88\x89\xd8(B4\
>@B\x88\x16\x16\x22b:\xff\x86 X\x04]\xcf\
\x95+\x84e\xe6\xee\xaef\xe0\xec\xcc\xee\x1c\xbey\xec\
\xbd3\x91\xa5t\xba\xd9\xb2\xac\x03h\x0ez\x832\x87\
\xb9\x5c\xd6\x0aX\xc2\xd0\x064\x0fE\xa0(\xb4\x07\xf8\
\xfa_@\xe3\x9a\xef[\x80e\x82\x82\x1e\x0d}\x9b\x80\
m\xfb\x05)\xdb\xb6\x1fPO@\xbd\x9a\xfeI\xf47\
\xbdT\xab%/P\x88\x1e\xbc\xe1\x97\xd0\x94\xc1\xb7\x03\
\xad\xe1'8\xc6\x19\xd1\x03#\xd60\xf2\xa903\xfa\
\xde\x06\xcf5\xbcf\x90\x0b6\x0c\x0dh\xbcc\x12L\
\xd5\xbf0\xec\x0cM[\x80\xb5\xc3s\x03\xafc\x041\
\xec\xd3\x036\x0a\xc5\xe19\xaf\x87)\xddz\xeb`q\
(\xa9\xb1$\xdd0e\xfa\x0b\x0c+x\xc0\xfa\xe1)\
\x927\xe4\x15\x1f\x08\x0d\x1a,\x0f-\x18,E(\xa5\
\xbc@4uZ\x02\x9a1\xde\x1fw\xa1}\x8c)?\
\xe1\xcf\xb0+4;\xa1\x11\xdd2\xc3\x01\xf22\xca1\
\xa6+\xef!?\x04\xecS+\xaa24d\xb0\xac\xa8\
\x06@V\x91\x83\xbb\xca\x03\xd2\x81\xaa$\xcd\x84 b\
\x1c\x01\xd2\x85\xea\x0eJ\x08\x90\xac\x18\xd9\x0c\xa9@}\
\x9a\xee/h\x19\x90}1\xd7\x00\xe9\xe1=1A\x16\
\x019\x12\xb3\x1f\x10J\x87{\xa8[\x80\x1c\x8b\xe7\x11\
C*\x1ct\xeeR\xa3\x9b\x06\x90\x13\xf1\x84\x04$\xc1\
\xcb1AR\x80\x14\xc4\xc3\x1f\x90A^NL\x80\x5c\
x\xc5\x1b]\x8a\xb4q-\x9a\xbe\x0fh\x16\x90[?\
\xd1\x1f1$!Af\x00)\x07\xb9 \x9f\xff\x0b\xf9\
\x05\xd1\x81\xf5\xc4\xef\xaf\xd0tP\xc8\xcf\x05\xe98\x8e\
\xd5\x88\xf2-\xc0\x00\xaa\xfa\xae\x1fG|9m\x00\x00\
\x00\x00IEND\xaeB`\x82\
"

qt_resource_name = b"\
\x00\x06\
\x07\x9e\x88\xb4\
\x00s\
\x00h\x00a\x00r\x00e\x00d\
\x00\x1a\
\x04'S\xdc\
\x00S\
\x00i\x00m\x00p\x00l\x00e\x00L\x00a\x00u\x00n\x00c\x00h\x00e\x00r\x00D\x00e\x00l\
\x00e\x00g\x00a\x00t\x00e\x00.\x00q\x00m\x00l\
\x00\x10\
\x09\x8e}\x5c\
\x00L\
\x00a\x00u\x00n\x00c\x00h\x00e\x00r\x00L\x00i\x00s\x00t\x00.\x00q\x00m\x00l\
\x00\x06\
\x07\x03}\xc3\
\x00i\
\x00m\x00a\x00g\x00e\x00s\
\x00\x0a\
\x0bhq\x5c\
\x00B\
\x00u\x00t\x00t\x00o\x00n\x00.\x00q\x00m\x00l\
\x00\x08\
\x07\x9eZG\
\x00b\
\x00a\x00c\x00k\x00.\x00p\x00n\x00g\
\x00\x08\
\x0c\xf7Y\xc7\
\x00n\
\x00e\x00x\x00t\x00.\x00p\x00n\x00g\
"

qt_resource_struct = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x04\x00\x00\x00\x02\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x12\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
\x00\x00\x01\x8eh\xfbB\x0c\
\x00\x00\x00r\x00\x02\x00\x00\x00\x02\x00\x00\x00\x06\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00L\x00\x00\x00\x00\x00\x01\x00\x00\x0c\xdb\
\x00\x00\x01\x8eh\xfbB\x0c\
\x00\x00\x00\x84\x00\x00\x00\x00\x00\x01\x00\x00!\x15\
\x00\x00\x01\x8eh\xfbB\x0c\
\x00\x00\x00\x9e\x00\x00\x00\x00\x00\x01\x00\x00-\xf4\
\x00\x00\x01\x8eh\xfbB\x0c\
\x00\x00\x00\xb4\x00\x00\x00\x00\x00\x01\x00\x004.\
\x00\x00\x01\x8eh\xfbB\x0c\
"

def qInitResources():
    QtCore.qRegisterResourceData(0x03, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(0x03, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()
