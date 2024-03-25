# Resource object code (Python 3)
# Created by: object code
# Created by: The Resource Compiler for Qt version 6.6.2
# WARNING! All changes made in this file will be lost!

from PySide6 import QtCore

qt_resource_data = b"\
\x00\x00\xdf\xa6\
/\
*\x0a * jQuery Java\
Script Library v\
1.3.2\x0a * http://\
jquery.com/\x0a *\x0a \
* Copyright (c) \
2009 John Resig\x0a\
 * Dual licensed\
 under the MIT a\
nd GPL licenses.\
\x0a * http://docs.\
jquery.com/Licen\
se\x0a *\x0a * Date: 2\
009-02-19 17:34:\
21 -0500 (Thu, 1\
9 Feb 2009)\x0a * R\
evision: 6246\x0a *\
/\x0a(function(){va\
r l=this,g,y=l.j\
Query,p=l.$,o=l.\
jQuery=l.$=funct\
ion(E,F){return \
new o.fn.init(E,\
F)},D=/^[^<]*(<(\
.|\x5cs)+>)[^>]*$|^\
#([\x5cw-]+)$/,f=/^\
.[^:#\x5c[\x5c.,]*$/;o\
.fn=o.prototype=\
{init:function(E\
,H){E=E||documen\
t;if(E.nodeType)\
{this[0]=E;this.\
length=1;this.co\
ntext=E;return t\
his}if(typeof E=\
==\x22string\x22){var \
G=D.exec(E);if(G\
&&(G[1]||!H)){if\
(G[1]){E=o.clean\
([G[1]],H)}else{\
var I=document.g\
etElementById(G[\
3]);if(I&&I.id!=\
G[3]){return o()\
.find(E)}var F=o\
(I||[]);F.contex\
t=document;F.sel\
ector=E;return F\
}}else{return o(\
H).find(E)}}else\
{if(o.isFunction\
(E)){return o(do\
cument).ready(E)\
}}if(E.selector&\
&E.context){this\
.selector=E.sele\
ctor;this.contex\
t=E.context}retu\
rn this.setArray\
(o.isArray(E)?E:\
o.makeArray(E))}\
,selector:\x22\x22,jqu\
ery:\x221.3.2\x22,size\
:function(){retu\
rn this.length},\
get:function(E){\
return E===g?Arr\
ay.prototype.sli\
ce.call(this):th\
is[E]},pushStack\
:function(F,H,E)\
{var G=o(F);G.pr\
evObject=this;G.\
context=this.con\
text;if(H===\x22fin\
d\x22){G.selector=t\
his.selector+(th\
is.selector?\x22 \x22:\
\x22\x22)+E}else{if(H)\
{G.selector=this\
.selector+\x22.\x22+H+\
\x22(\x22+E+\x22)\x22}}retur\
n G},setArray:fu\
nction(E){this.l\
ength=0;Array.pr\
ototype.push.app\
ly(this,E);retur\
n this},each:fun\
ction(F,E){retur\
n o.each(this,F,\
E)},index:functi\
on(E){return o.i\
nArray(E&&E.jque\
ry?E[0]:E,this)}\
,attr:function(F\
,H,G){var E=F;if\
(typeof F===\x22str\
ing\x22){if(H===g){\
return this[0]&&\
o[G||\x22attr\x22](thi\
s[0],F)}else{E={\
};E[F]=H}}return\
 this.each(funct\
ion(I){for(F in \
E){o.attr(G?this\
.style:this,F,o.\
prop(this,E[F],G\
,I,F))}})},css:f\
unction(E,F){if(\
(E==\x22width\x22||E==\
\x22height\x22)&&parse\
Float(F)<0){F=g}\
return this.attr\
(E,F,\x22curCSS\x22)},\
text:function(F)\
{if(typeof F!==\x22\
object\x22&&F!=null\
){return this.em\
pty().append((th\
is[0]&&this[0].o\
wnerDocument||do\
cument).createTe\
xtNode(F))}var E\
=\x22\x22;o.each(F||th\
is,function(){o.\
each(this.childN\
odes,function(){\
if(this.nodeType\
!=8){E+=this.nod\
eType!=1?this.no\
deValue:o.fn.tex\
t([this])}})});r\
eturn E},wrapAll\
:function(E){if(\
this[0]){var F=o\
(E,this[0].owner\
Document).clone(\
);if(this[0].par\
entNode){F.inser\
tBefore(this[0])\
}F.map(function(\
){var G=this;whi\
le(G.firstChild)\
{G=G.firstChild}\
return G}).appen\
d(this)}return t\
his},wrapInner:f\
unction(E){retur\
n this.each(func\
tion(){o(this).c\
ontents().wrapAl\
l(E)})},wrap:fun\
ction(E){return \
this.each(functi\
on(){o(this).wra\
pAll(E)})},appen\
d:function(){ret\
urn this.domMani\
p(arguments,true\
,function(E){if(\
this.nodeType==1\
){this.appendChi\
ld(E)}})},prepen\
d:function(){ret\
urn this.domMani\
p(arguments,true\
,function(E){if(\
this.nodeType==1\
){this.insertBef\
ore(E,this.first\
Child)}})},befor\
e:function(){ret\
urn this.domMani\
p(arguments,fals\
e,function(E){th\
is.parentNode.in\
sertBefore(E,thi\
s)})},after:func\
tion(){return th\
is.domManip(argu\
ments,false,func\
tion(E){this.par\
entNode.insertBe\
fore(E,this.next\
Sibling)})},end:\
function(){retur\
n this.prevObjec\
t||o([])},push:[\
].push,sort:[].s\
ort,splice:[].sp\
lice,find:functi\
on(E){if(this.le\
ngth===1){var F=\
this.pushStack([\
],\x22find\x22,E);F.le\
ngth=0;o.find(E,\
this[0],F);retur\
n F}else{return \
this.pushStack(o\
.unique(o.map(th\
is,function(G){r\
eturn o.find(E,G\
)})),\x22find\x22,E)}}\
,clone:function(\
G){var E=this.ma\
p(function(){if(\
!o.support.noClo\
neEvent&&!o.isXM\
LDoc(this)){var \
I=this.outerHTML\
;if(!I){var J=th\
is.ownerDocument\
.createElement(\x22\
div\x22);J.appendCh\
ild(this.cloneNo\
de(true));I=J.in\
nerHTML}return o\
.clean([I.replac\
e(/ jQuery\x5cd+=\x22(\
?:\x5cd+|null)\x22/g,\x22\
\x22).replace(/^\x5cs*\
/,\x22\x22)])[0]}else{\
return this.clon\
eNode(true)}});i\
f(G===true){var \
H=this.find(\x22*\x22)\
.andSelf(),F=0;E\
.find(\x22*\x22).andSe\
lf().each(functi\
on(){if(this.nod\
eName!==H[F].nod\
eName){return}va\
r I=o.data(H[F],\
\x22events\x22);for(va\
r K in I){for(va\
r J in I[K]){o.e\
vent.add(this,K,\
I[K][J],I[K][J].\
data)}}F++})}ret\
urn E},filter:fu\
nction(E){return\
 this.pushStack(\
o.isFunction(E)&\
&o.grep(this,fun\
ction(G,F){retur\
n E.call(G,F)})|\
|o.multiFilter(E\
,o.grep(this,fun\
ction(F){return \
F.nodeType===1})\
),\x22filter\x22,E)},c\
losest:function(\
E){var G=o.expr.\
match.POS.test(E\
)?o(E):null,F=0;\
return this.map(\
function(){var H\
=this;while(H&&H\
.ownerDocument){\
if(G?G.index(H)>\
-1:o(H).is(E)){o\
.data(H,\x22closest\
\x22,F);return H}H=\
H.parentNode;F++\
}})},not:functio\
n(E){if(typeof E\
===\x22string\x22){if(\
f.test(E)){retur\
n this.pushStack\
(o.multiFilter(E\
,this,true),\x22not\
\x22,E)}else{E=o.mu\
ltiFilter(E,this\
)}}var F=E.lengt\
h&&E[E.length-1]\
!==g&&!E.nodeTyp\
e;return this.fi\
lter(function(){\
return F?o.inArr\
ay(this,E)<0:thi\
s!=E})},add:func\
tion(E){return t\
his.pushStack(o.\
unique(o.merge(t\
his.get(),typeof\
 E===\x22string\x22?o(\
E):o.makeArray(E\
))))},is:functio\
n(E){return !!E&\
&o.multiFilter(E\
,this).length>0}\
,hasClass:functi\
on(E){return !!E\
&&this.is(\x22.\x22+E)\
},val:function(K\
){if(K===g){var \
E=this[0];if(E){\
if(o.nodeName(E,\
\x22option\x22)){retur\
n(E.attributes.v\
alue||{}).specif\
ied?E.value:E.te\
xt}if(o.nodeName\
(E,\x22select\x22)){va\
r I=E.selectedIn\
dex,L=[],M=E.opt\
ions,H=E.type==\x22\
select-one\x22;if(I\
<0){return null}\
for(var F=H?I:0,\
J=H?I+1:M.length\
;F<J;F++){var G=\
M[F];if(G.select\
ed){K=o(G).val()\
;if(H){return K}\
L.push(K)}}retur\
n L}return(E.val\
ue||\x22\x22).replace(\
/\x5cr/g,\x22\x22)}return\
 g}if(typeof K==\
=\x22number\x22){K+=\x22\x22\
}return this.eac\
h(function(){if(\
this.nodeType!=1\
){return}if(o.is\
Array(K)&&/radio\
|checkbox/.test(\
this.type)){this\
.checked=(o.inAr\
ray(this.value,K\
)>=0||o.inArray(\
this.name,K)>=0)\
}else{if(o.nodeN\
ame(this,\x22select\
\x22)){var N=o.make\
Array(K);o(\x22opti\
on\x22,this).each(f\
unction(){this.s\
elected=(o.inArr\
ay(this.value,N)\
>=0||o.inArray(t\
his.text,N)>=0)}\
);if(!N.length){\
this.selectedInd\
ex=-1}}else{this\
.value=K}}})},ht\
ml:function(E){r\
eturn E===g?(thi\
s[0]?this[0].inn\
erHTML.replace(/\
 jQuery\x5cd+=\x22(?:\x5c\
d+|null)\x22/g,\x22\x22):\
null):this.empty\
().append(E)},re\
placeWith:functi\
on(E){return thi\
s.after(E).remov\
e()},eq:function\
(E){return this.\
slice(E,+E+1)},s\
lice:function(){\
return this.push\
Stack(Array.prot\
otype.slice.appl\
y(this,arguments\
),\x22slice\x22,Array.\
prototype.slice.\
call(arguments).\
join(\x22,\x22))},map:\
function(E){retu\
rn this.pushStac\
k(o.map(this,fun\
ction(G,F){retur\
n E.call(G,F,G)}\
))},andSelf:func\
tion(){return th\
is.add(this.prev\
Object)},domMani\
p:function(J,M,L\
){if(this[0]){va\
r I=(this[0].own\
erDocument||this\
[0]).createDocum\
entFragment(),F=\
o.clean(J,(this[\
0].ownerDocument\
||this[0]),I),H=\
I.firstChild;if(\
H){for(var G=0,E\
=this.length;G<E\
;G++){L.call(K(t\
his[G],H),this.l\
ength>1||G>0?I.c\
loneNode(true):I\
)}}if(F){o.each(\
F,z)}}return thi\
s;function K(N,O\
){return M&&o.no\
deName(N,\x22table\x22\
)&&o.nodeName(O,\
\x22tr\x22)?(N.getElem\
entsByTagName(\x22t\
body\x22)[0]||N.app\
endChild(N.owner\
Document.createE\
lement(\x22tbody\x22))\
):N}}};o.fn.init\
.prototype=o.fn;\
function z(E,F){\
if(F.src){o.ajax\
({url:F.src,asyn\
c:false,dataType\
:\x22script\x22})}else\
{o.globalEval(F.\
text||F.textCont\
ent||F.innerHTML\
||\x22\x22)}if(F.paren\
tNode){F.parentN\
ode.removeChild(\
F)}}function e()\
{return +new Dat\
e}o.extend=o.fn.\
extend=function(\
){var J=argument\
s[0]||{},H=1,I=a\
rguments.length,\
E=false,G;if(typ\
eof J===\x22boolean\
\x22){E=J;J=argumen\
ts[1]||{};H=2}if\
(typeof J!==\x22obj\
ect\x22&&!o.isFunct\
ion(J)){J={}}if(\
I==H){J=this;--H\
}for(;H<I;H++){i\
f((G=arguments[H\
])!=null){for(va\
r F in G){var K=\
J[F],L=G[F];if(J\
===L){continue}i\
f(E&&L&&typeof L\
===\x22object\x22&&!L.\
nodeType){J[F]=o\
.extend(E,K||(L.\
length!=null?[]:\
{}),L)}else{if(L\
!==g){J[F]=L}}}}\
}return J};var b\
=/z-?index|font-\
?weight|opacity|\
zoom|line-?heigh\
t/i,q=document.d\
efaultView||{},s\
=Object.prototyp\
e.toString;o.ext\
end({noConflict:\
function(E){l.$=\
p;if(E){l.jQuery\
=y}return o},isF\
unction:function\
(E){return s.cal\
l(E)===\x22[object \
Function]\x22},isAr\
ray:function(E){\
return s.call(E)\
===\x22[object Arra\
y]\x22},isXMLDoc:fu\
nction(E){return\
 E.nodeType===9&\
&E.documentEleme\
nt.nodeName!==\x22H\
TML\x22||!!E.ownerD\
ocument&&o.isXML\
Doc(E.ownerDocum\
ent)},globalEval\
:function(G){if(\
G&&/\x5cS/.test(G))\
{var F=document.\
getElementsByTag\
Name(\x22head\x22)[0]|\
|document.docume\
ntElement,E=docu\
ment.createEleme\
nt(\x22script\x22);E.t\
ype=\x22text/javasc\
ript\x22;if(o.suppo\
rt.scriptEval){E\
.appendChild(doc\
ument.createText\
Node(G))}else{E.\
text=G}F.insertB\
efore(E,F.firstC\
hild);F.removeCh\
ild(E)}},nodeNam\
e:function(F,E){\
return F.nodeNam\
e&&F.nodeName.to\
UpperCase()==E.t\
oUpperCase()},ea\
ch:function(G,K,\
F){var E,H=0,I=G\
.length;if(F){if\
(I===g){for(E in\
 G){if(K.apply(G\
[E],F)===false){\
break}}}else{for\
(;H<I;){if(K.app\
ly(G[H++],F)===f\
alse){break}}}}e\
lse{if(I===g){fo\
r(E in G){if(K.c\
all(G[E],E,G[E])\
===false){break}\
}}else{for(var J\
=G[0];H<I&&K.cal\
l(J,H,J)!==false\
;J=G[++H]){}}}re\
turn G},prop:fun\
ction(H,I,G,F,E)\
{if(o.isFunction\
(I)){I=I.call(H,\
F)}return typeof\
 I===\x22number\x22&&G\
==\x22curCSS\x22&&!b.t\
est(E)?I+\x22px\x22:I}\
,className:{add:\
function(E,F){o.\
each((F||\x22\x22).spl\
it(/\x5cs+/),functi\
on(G,H){if(E.nod\
eType==1&&!o.cla\
ssName.has(E.cla\
ssName,H)){E.cla\
ssName+=(E.class\
Name?\x22 \x22:\x22\x22)+H}}\
)},remove:functi\
on(E,F){if(E.nod\
eType==1){E.clas\
sName=F!==g?o.gr\
ep(E.className.s\
plit(/\x5cs+/),func\
tion(G){return !\
o.className.has(\
F,G)}).join(\x22 \x22)\
:\x22\x22}},has:functi\
on(F,E){return F\
&&o.inArray(E,(F\
.className||F).t\
oString().split(\
/\x5cs+/))>-1}},swa\
p:function(H,G,I\
){var E={};for(v\
ar F in G){E[F]=\
H.style[F];H.sty\
le[F]=G[F]}I.cal\
l(H);for(var F i\
n G){H.style[F]=\
E[F]}},css:funct\
ion(H,F,J,E){if(\
F==\x22width\x22||F==\x22\
height\x22){var L,G\
={position:\x22abso\
lute\x22,visibility\
:\x22hidden\x22,displa\
y:\x22block\x22},K=F==\
\x22width\x22?[\x22Left\x22,\
\x22Right\x22]:[\x22Top\x22,\
\x22Bottom\x22];functi\
on I(){L=F==\x22wid\
th\x22?H.offsetWidt\
h:H.offsetHeight\
;if(E===\x22border\x22\
){return}o.each(\
K,function(){if(\
!E){L-=parseFloa\
t(o.curCSS(H,\x22pa\
dding\x22+this,true\
))||0}if(E===\x22ma\
rgin\x22){L+=parseF\
loat(o.curCSS(H,\
\x22margin\x22+this,tr\
ue))||0}else{L-=\
parseFloat(o.cur\
CSS(H,\x22border\x22+t\
his+\x22Width\x22,true\
))||0}})}if(H.of\
fsetWidth!==0){I\
()}else{o.swap(H\
,G,I)}return Mat\
h.max(0,Math.rou\
nd(L))}return o.\
curCSS(H,F,J)},c\
urCSS:function(I\
,F,G){var L,E=I.\
style;if(F==\x22opa\
city\x22&&!o.suppor\
t.opacity){L=o.a\
ttr(E,\x22opacity\x22)\
;return L==\x22\x22?\x221\
\x22:L}if(F.match(/\
float/i)){F=w}if\
(!G&&E&&E[F]){L=\
E[F]}else{if(q.g\
etComputedStyle)\
{if(F.match(/flo\
at/i)){F=\x22float\x22\
}F=F.replace(/([\
A-Z])/g,\x22-$1\x22).t\
oLowerCase();var\
 M=q.getComputed\
Style(I,null);if\
(M){L=M.getPrope\
rtyValue(F)}if(F\
==\x22opacity\x22&&L==\
\x22\x22){L=\x221\x22}}else{\
if(I.currentStyl\
e){var J=F.repla\
ce(/\x5c-(\x5cw)/g,fun\
ction(N,O){retur\
n O.toUpperCase(\
)});L=I.currentS\
tyle[F]||I.curre\
ntStyle[J];if(!/\
^\x5cd+(px)?$/i.tes\
t(L)&&/^\x5cd/.test\
(L)){var H=E.lef\
t,K=I.runtimeSty\
le.left;I.runtim\
eStyle.left=I.cu\
rrentStyle.left;\
E.left=L||0;L=E.\
pixelLeft+\x22px\x22;E\
.left=H;I.runtim\
eStyle.left=K}}}\
}return L},clean\
:function(F,K,I)\
{K=K||document;i\
f(typeof K.creat\
eElement===\x22unde\
fined\x22){K=K.owne\
rDocument||K[0]&\
&K[0].ownerDocum\
ent||document}if\
(!I&&F.length===\
1&&typeof F[0]==\
=\x22string\x22){var H\
=/^<(\x5cw+)\x5cs*\x5c/?>\
$/.exec(F[0]);if\
(H){return[K.cre\
ateElement(H[1])\
]}}var G=[],E=[]\
,L=K.createEleme\
nt(\x22div\x22);o.each\
(F,function(P,S)\
{if(typeof S===\x22\
number\x22){S+=\x22\x22}i\
f(!S){return}if(\
typeof S===\x22stri\
ng\x22){S=S.replace\
(/(<(\x5cw+)[^>]*?)\
\x5c/>/g,function(U\
,V,T){return T.m\
atch(/^(abbr|br|\
col|img|input|li\
nk|meta|param|hr\
|area|embed)$/i)\
?U:V+\x22></\x22+T+\x22>\x22\
});var O=S.repla\
ce(/^\x5cs+/,\x22\x22).su\
bstring(0,10).to\
LowerCase();var \
Q=!O.indexOf(\x22<o\
pt\x22)&&[1,\x22<selec\
t multiple='mult\
iple'>\x22,\x22</selec\
t>\x22]||!O.indexOf\
(\x22<leg\x22)&&[1,\x22<f\
ieldset>\x22,\x22</fie\
ldset>\x22]||O.matc\
h(/^<(thead|tbod\
y|tfoot|colg|cap\
)/)&&[1,\x22<table>\
\x22,\x22</table>\x22]||!\
O.indexOf(\x22<tr\x22)\
&&[2,\x22<table><tb\
ody>\x22,\x22</tbody><\
/table>\x22]||(!O.i\
ndexOf(\x22<td\x22)||!\
O.indexOf(\x22<th\x22)\
)&&[3,\x22<table><t\
body><tr>\x22,\x22</tr\
></tbody></table\
>\x22]||!O.indexOf(\
\x22<col\x22)&&[2,\x22<ta\
ble><tbody></tbo\
dy><colgroup>\x22,\x22\
</colgroup></tab\
le>\x22]||!o.suppor\
t.htmlSerialize&\
&[1,\x22div<div>\x22,\x22\
</div>\x22]||[0,\x22\x22,\
\x22\x22];L.innerHTML=\
Q[1]+S+Q[2];whil\
e(Q[0]--){L=L.la\
stChild}if(!o.su\
pport.tbody){var\
 R=/<tbody/i.tes\
t(S),N=!O.indexO\
f(\x22<table\x22)&&!R?\
L.firstChild&&L.\
firstChild.child\
Nodes:Q[1]==\x22<ta\
ble>\x22&&!R?L.chil\
dNodes:[];for(va\
r M=N.length-1;M\
>=0;--M){if(o.no\
deName(N[M],\x22tbo\
dy\x22)&&!N[M].chil\
dNodes.length){N\
[M].parentNode.r\
emoveChild(N[M])\
}}}if(!o.support\
.leadingWhitespa\
ce&&/^\x5cs/.test(S\
)){L.insertBefor\
e(K.createTextNo\
de(S.match(/^\x5cs*\
/)[0]),L.firstCh\
ild)}S=o.makeArr\
ay(L.childNodes)\
}if(S.nodeType){\
G.push(S)}else{G\
=o.merge(G,S)}})\
;if(I){for(var J\
=0;G[J];J++){if(\
o.nodeName(G[J],\
\x22script\x22)&&(!G[J\
].type||G[J].typ\
e.toLowerCase()=\
==\x22text/javascri\
pt\x22)){E.push(G[J\
].parentNode?G[J\
].parentNode.rem\
oveChild(G[J]):G\
[J])}else{if(G[J\
].nodeType===1){\
G.splice.apply(G\
,[J+1,0].concat(\
o.makeArray(G[J]\
.getElementsByTa\
gName(\x22script\x22))\
))}I.appendChild\
(G[J])}}return E\
}return G},attr:\
function(J,G,K){\
if(!J||J.nodeTyp\
e==3||J.nodeType\
==8){return g}va\
r H=!o.isXMLDoc(\
J),L=K!==g;G=H&&\
o.props[G]||G;if\
(J.tagName){var \
F=/href|src|styl\
e/.test(G);if(G=\
=\x22selected\x22&&J.p\
arentNode){J.par\
entNode.selected\
Index}if(G in J&\
&H&&!F){if(L){if\
(G==\x22type\x22&&o.no\
deName(J,\x22input\x22\
)&&J.parentNode)\
{throw\x22type prop\
erty can't be ch\
anged\x22}J[G]=K}if\
(o.nodeName(J,\x22f\
orm\x22)&&J.getAttr\
ibuteNode(G)){re\
turn J.getAttrib\
uteNode(G).nodeV\
alue}if(G==\x22tabI\
ndex\x22){var I=J.g\
etAttributeNode(\
\x22tabIndex\x22);retu\
rn I&&I.specifie\
d?I.value:J.node\
Name.match(/(but\
ton|input|object\
|select|textarea\
)/i)?0:J.nodeNam\
e.match(/^(a|are\
a)$/i)&&J.href?0\
:g}return J[G]}i\
f(!o.support.sty\
le&&H&&G==\x22style\
\x22){return o.attr\
(J.style,\x22cssTex\
t\x22,K)}if(L){J.se\
tAttribute(G,\x22\x22+\
K)}var E=!o.supp\
ort.hrefNormaliz\
ed&&H&&F?J.getAt\
tribute(G,2):J.g\
etAttribute(G);r\
eturn E===null?g\
:E}if(!o.support\
.opacity&&G==\x22op\
acity\x22){if(L){J.\
zoom=1;J.filter=\
(J.filter||\x22\x22).r\
eplace(/alpha\x5c([\
^)]*\x5c)/,\x22\x22)+(par\
seInt(K)+\x22\x22==\x22Na\
N\x22?\x22\x22:\x22alpha(opa\
city=\x22+K*100+\x22)\x22\
)}return J.filte\
r&&J.filter.inde\
xOf(\x22opacity=\x22)>\
=0?(parseFloat(J\
.filter.match(/o\
pacity=([^)]*)/)\
[1])/100)+\x22\x22:\x22\x22}\
G=G.replace(/-([\
a-z])/ig,functio\
n(M,N){return N.\
toUpperCase()});\
if(L){J[G]=K}ret\
urn J[G]},trim:f\
unction(E){retur\
n(E||\x22\x22).replace\
(/^\x5cs+|\x5cs+$/g,\x22\x22\
)},makeArray:fun\
ction(G){var E=[\
];if(G!=null){va\
r F=G.length;if(\
F==null||typeof \
G===\x22string\x22||o.\
isFunction(G)||G\
.setInterval){E[\
0]=G}else{while(\
F){E[--F]=G[F]}}\
}return E},inArr\
ay:function(G,H)\
{for(var E=0,F=H\
.length;E<F;E++)\
{if(H[E]===G){re\
turn E}}return -\
1},merge:functio\
n(H,E){var F=0,G\
,I=H.length;if(!\
o.support.getAll\
){while((G=E[F++\
])!=null){if(G.n\
odeType!=8){H[I+\
+]=G}}}else{whil\
e((G=E[F++])!=nu\
ll){H[I++]=G}}re\
turn H},unique:f\
unction(K){var F\
=[],E={};try{for\
(var G=0,H=K.len\
gth;G<H;G++){var\
 J=o.data(K[G]);\
if(!E[J]){E[J]=t\
rue;F.push(K[G])\
}}}catch(I){F=K}\
return F},grep:f\
unction(F,J,E){v\
ar G=[];for(var \
H=0,I=F.length;H\
<I;H++){if(!E!=!\
J(F[H],H)){G.pus\
h(F[H])}}return \
G},map:function(\
E,J){var F=[];fo\
r(var G=0,H=E.le\
ngth;G<H;G++){va\
r I=J(E[G],G);if\
(I!=null){F[F.le\
ngth]=I}}return \
F.concat.apply([\
],F)}});var C=na\
vigator.userAgen\
t.toLowerCase();\
o.browser={versi\
on:(C.match(/.+(\
?:rv|it|ra|ie)[\x5c\
/: ]([\x5cd.]+)/)||\
[0,\x220\x22])[1],safa\
ri:/webkit/.test\
(C),opera:/opera\
/.test(C),msie:/\
msie/.test(C)&&!\
/opera/.test(C),\
mozilla:/mozilla\
/.test(C)&&!/(co\
mpatible|webkit)\
/.test(C)};o.eac\
h({parent:functi\
on(E){return E.p\
arentNode},paren\
ts:function(E){r\
eturn o.dir(E,\x22p\
arentNode\x22)},nex\
t:function(E){re\
turn o.nth(E,2,\x22\
nextSibling\x22)},p\
rev:function(E){\
return o.nth(E,2\
,\x22previousSiblin\
g\x22)},nextAll:fun\
ction(E){return \
o.dir(E,\x22nextSib\
ling\x22)},prevAll:\
function(E){retu\
rn o.dir(E,\x22prev\
iousSibling\x22)},s\
iblings:function\
(E){return o.sib\
ling(E.parentNod\
e.firstChild,E)}\
,children:functi\
on(E){return o.s\
ibling(E.firstCh\
ild)},contents:f\
unction(E){retur\
n o.nodeName(E,\x22\
iframe\x22)?E.conte\
ntDocument||E.co\
ntentWindow.docu\
ment:o.makeArray\
(E.childNodes)}}\
,function(E,F){o\
.fn[E]=function(\
G){var H=o.map(t\
his,F);if(G&&typ\
eof G==\x22string\x22)\
{H=o.multiFilter\
(G,H)}return thi\
s.pushStack(o.un\
ique(H),E,G)}});\
o.each({appendTo\
:\x22append\x22,prepen\
dTo:\x22prepend\x22,in\
sertBefore:\x22befo\
re\x22,insertAfter:\
\x22after\x22,replaceA\
ll:\x22replaceWith\x22\
},function(E,F){\
o.fn[E]=function\
(G){var J=[],L=o\
(G);for(var K=0,\
H=L.length;K<H;K\
++){var I=(K>0?t\
his.clone(true):\
this).get();o.fn\
[F].apply(o(L[K]\
),I);J=J.concat(\
I)}return this.p\
ushStack(J,E,G)}\
});o.each({remov\
eAttr:function(E\
){o.attr(this,E,\
\x22\x22);if(this.node\
Type==1){this.re\
moveAttribute(E)\
}},addClass:func\
tion(E){o.classN\
ame.add(this,E)}\
,removeClass:fun\
ction(E){o.class\
Name.remove(this\
,E)},toggleClass\
:function(F,E){i\
f(typeof E!==\x22bo\
olean\x22){E=!o.cla\
ssName.has(this,\
F)}o.className[E\
?\x22add\x22:\x22remove\x22]\
(this,F)},remove\
:function(E){if(\
!E||o.filter(E,[\
this]).length){o\
(\x22*\x22,this).add([\
this]).each(func\
tion(){o.event.r\
emove(this);o.re\
moveData(this)})\
;if(this.parentN\
ode){this.parent\
Node.removeChild\
(this)}}},empty:\
function(){o(thi\
s).children().re\
move();while(thi\
s.firstChild){th\
is.removeChild(t\
his.firstChild)}\
}},function(E,F)\
{o.fn[E]=functio\
n(){return this.\
each(F,arguments\
)}});function j(\
E,F){return E[0]\
&&parseInt(o.cur\
CSS(E[0],F,true)\
,10)||0}var h=\x22j\
Query\x22+e(),v=0,A\
={};o.extend({ca\
che:{},data:func\
tion(F,E,G){F=F=\
=l?A:F;var H=F[h\
];if(!H){H=F[h]=\
++v}if(E&&!o.cac\
he[H]){o.cache[H\
]={}}if(G!==g){o\
.cache[H][E]=G}r\
eturn E?o.cache[\
H][E]:H},removeD\
ata:function(F,E\
){F=F==l?A:F;var\
 H=F[h];if(E){if\
(o.cache[H]){del\
ete o.cache[H][E\
];E=\x22\x22;for(E in \
o.cache[H]){brea\
k}if(!E){o.remov\
eData(F)}}}else{\
try{delete F[h]}\
catch(G){if(F.re\
moveAttribute){F\
.removeAttribute\
(h)}}delete o.ca\
che[H]}},queue:f\
unction(F,E,H){i\
f(F){E=(E||\x22fx\x22)\
+\x22queue\x22;var G=o\
.data(F,E);if(!G\
||o.isArray(H)){\
G=o.data(F,E,o.m\
akeArray(H))}els\
e{if(H){G.push(H\
)}}}return G},de\
queue:function(H\
,G){var E=o.queu\
e(H,G),F=E.shift\
();if(!G||G===\x22f\
x\x22){F=E[0]}if(F!\
==g){F.call(H)}}\
});o.fn.extend({\
data:function(E,\
G){var H=E.split\
(\x22.\x22);H[1]=H[1]?\
\x22.\x22+H[1]:\x22\x22;if(G\
===g){var F=this\
.triggerHandler(\
\x22getData\x22+H[1]+\x22\
!\x22,[H[0]]);if(F=\
==g&&this.length\
){F=o.data(this[\
0],E)}return F==\
=g&&H[1]?this.da\
ta(H[0]):F}else{\
return this.trig\
ger(\x22setData\x22+H[\
1]+\x22!\x22,[H[0],G])\
.each(function()\
{o.data(this,E,G\
)})}},removeData\
:function(E){ret\
urn this.each(fu\
nction(){o.remov\
eData(this,E)})}\
,queue:function(\
E,F){if(typeof E\
!==\x22string\x22){F=E\
;E=\x22fx\x22}if(F===g\
){return o.queue\
(this[0],E)}retu\
rn this.each(fun\
ction(){var G=o.\
queue(this,E,F);\
if(E==\x22fx\x22&&G.le\
ngth==1){G[0].ca\
ll(this)}})},deq\
ueue:function(E)\
{return this.eac\
h(function(){o.d\
equeue(this,E)})\
}});\x0a/*\x0a * Sizzl\
e CSS Selector E\
ngine - v0.9.3\x0a \
*  Copyright 200\
9, The Dojo Foun\
dation\x0a *  Relea\
sed under the MI\
T, BSD, and GPL \
Licenses.\x0a *  Mo\
re information: \
http://sizzlejs.\
com/\x0a */\x0a(functi\
on(){var R=/((?:\
\x5c((?:\x5c([^()]+\x5c)|\
[^()]+)+\x5c)|\x5c[(?:\
\x5c[[^[\x5c]]*\x5c]|['\x22]\
[^'\x22]*['\x22]|[^[\x5c]\
'\x22]+)+\x5c]|\x5c\x5c.|[^ \
>+~,(\x5c[\x5c\x5c]+)+|[>\
+~])(\x5cs*,\x5cs*)?/g\
,L=0,H=Object.pr\
ototype.toString\
;var F=function(\
Y,U,ab,ac){ab=ab\
||[];U=U||docume\
nt;if(U.nodeType\
!==1&&U.nodeType\
!==9){return[]}i\
f(!Y||typeof Y!=\
=\x22string\x22){retur\
n ab}var Z=[],W,\
af,ai,T,ad,V,X=t\
rue;R.lastIndex=\
0;while((W=R.exe\
c(Y))!==null){Z.\
push(W[1]);if(W[\
2]){V=RegExp.rig\
htContext;break}\
}if(Z.length>1&&\
M.exec(Y)){if(Z.\
length===2&&I.re\
lative[Z[0]]){af\
=J(Z[0]+Z[1],U)}\
else{af=I.relati\
ve[Z[0]]?[U]:F(Z\
.shift(),U);whil\
e(Z.length){Y=Z.\
shift();if(I.rel\
ative[Y]){Y+=Z.s\
hift()}af=J(Y,af\
)}}}else{var ae=\
ac?{expr:Z.pop()\
,set:E(ac)}:F.fi\
nd(Z.pop(),Z.len\
gth===1&&U.paren\
tNode?U.parentNo\
de:U,Q(U));af=F.\
filter(ae.expr,a\
e.set);if(Z.leng\
th>0){ai=E(af)}e\
lse{X=false}whil\
e(Z.length){var \
ah=Z.pop(),ag=ah\
;if(!I.relative[\
ah]){ah=\x22\x22}else{\
ag=Z.pop()}if(ag\
==null){ag=U}I.r\
elative[ah](ai,a\
g,Q(U))}}if(!ai)\
{ai=af}if(!ai){t\
hrow\x22Syntax erro\
r, unrecognized \
expression: \x22+(a\
h||Y)}if(H.call(\
ai)===\x22[object A\
rray]\x22){if(!X){a\
b.push.apply(ab,\
ai)}else{if(U.no\
deType===1){for(\
var aa=0;ai[aa]!\
=null;aa++){if(a\
i[aa]&&(ai[aa]==\
=true||ai[aa].no\
deType===1&&K(U,\
ai[aa]))){ab.pus\
h(af[aa])}}}else\
{for(var aa=0;ai\
[aa]!=null;aa++)\
{if(ai[aa]&&ai[a\
a].nodeType===1)\
{ab.push(af[aa])\
}}}}}else{E(ai,a\
b)}if(V){F(V,U,a\
b,ac);if(G){hasD\
uplicate=false;a\
b.sort(G);if(has\
Duplicate){for(v\
ar aa=1;aa<ab.le\
ngth;aa++){if(ab\
[aa]===ab[aa-1])\
{ab.splice(aa--,\
1)}}}}}return ab\
};F.matches=func\
tion(T,U){return\
 F(T,null,null,U\
)};F.find=functi\
on(aa,T,ab){var \
Z,X;if(!aa){retu\
rn[]}for(var W=0\
,V=I.order.lengt\
h;W<V;W++){var Y\
=I.order[W],X;if\
((X=I.match[Y].e\
xec(aa))){var U=\
RegExp.leftConte\
xt;if(U.substr(U\
.length-1)!==\x22\x5c\x5c\
\x22){X[1]=(X[1]||\x22\
\x22).replace(/\x5c\x5c/g\
,\x22\x22);Z=I.find[Y]\
(X,T,ab);if(Z!=n\
ull){aa=aa.repla\
ce(I.match[Y],\x22\x22\
);break}}}}if(!Z\
){Z=T.getElement\
sByTagName(\x22*\x22)}\
return{set:Z,exp\
r:aa}};F.filter=\
function(ad,ac,a\
g,W){var V=ad,ai\
=[],aa=ac,Y,T,Z=\
ac&&ac[0]&&Q(ac[\
0]);while(ad&&ac\
.length){for(var\
 ab in I.filter)\
{if((Y=I.match[a\
b].exec(ad))!=nu\
ll){var U=I.filt\
er[ab],ah,af;T=f\
alse;if(aa==ai){\
ai=[]}if(I.preFi\
lter[ab]){Y=I.pr\
eFilter[ab](Y,aa\
,ag,ai,W,Z);if(!\
Y){T=ah=true}els\
e{if(Y===true){c\
ontinue}}}if(Y){\
for(var X=0;(af=\
aa[X])!=null;X++\
){if(af){ah=U(af\
,Y,X,aa);var ae=\
W^!!ah;if(ag&&ah\
!=null){if(ae){T\
=true}else{aa[X]\
=false}}else{if(\
ae){ai.push(af);\
T=true}}}}}if(ah\
!==g){if(!ag){aa\
=ai}ad=ad.replac\
e(I.match[ab],\x22\x22\
);if(!T){return[\
]}break}}}if(ad=\
=V){if(T==null){\
throw\x22Syntax err\
or, unrecognized\
 expression: \x22+a\
d}else{break}}V=\
ad}return aa};va\
r I=F.selectors=\
{order:[\x22ID\x22,\x22NA\
ME\x22,\x22TAG\x22],match\
:{ID:/#((?:[\x5cw\x5cu\
00c0-\x5cuFFFF_-]|\x5c\
\x5c.)+)/,CLASS:/\x5c.\
((?:[\x5cw\x5cu00c0-\x5cu\
FFFF_-]|\x5c\x5c.)+)/,\
NAME:/\x5c[name=['\x22\
]*((?:[\x5cw\x5cu00c0-\
\x5cuFFFF_-]|\x5c\x5c.)+)\
['\x22]*\x5c]/,ATTR:/\x5c\
[\x5cs*((?:[\x5cw\x5cu00c\
0-\x5cuFFFF_-]|\x5c\x5c.)\
+)\x5cs*(?:(\x5cS?=)\x5cs\
*(['\x22]*)(.*?)\x5c3|\
)\x5cs*\x5c]/,TAG:/^((\
?:[\x5cw\x5cu00c0-\x5cuFF\
FF\x5c*_-]|\x5c\x5c.)+)/,\
CHILD:/:(only|nt\
h|last|first)-ch\
ild(?:\x5c((even|od\
d|[\x5cdn+-]*)\x5c))?/\
,POS:/:(nth|eq|g\
t|lt|first|last|\
even|odd)(?:\x5c((\x5c\
d*)\x5c))?(?=[^-]|$\
)/,PSEUDO:/:((?:\
[\x5cw\x5cu00c0-\x5cuFFFF\
_-]|\x5c\x5c.)+)(?:\x5c((\
['\x22]*)((?:\x5c([^\x5c)\
]+\x5c)|[^\x5c2\x5c(\x5c)]*)\
+)\x5c2\x5c))?/},attrM\
ap:{\x22class\x22:\x22cla\
ssName\x22,\x22for\x22:\x22h\
tmlFor\x22},attrHan\
dle:{href:functi\
on(T){return T.g\
etAttribute(\x22hre\
f\x22)}},relative:{\
\x22+\x22:function(aa,\
T,Z){var X=typeo\
f T===\x22string\x22,a\
b=X&&!/\x5cW/.test(\
T),Y=X&&!ab;if(a\
b&&!Z){T=T.toUpp\
erCase()}for(var\
 W=0,V=aa.length\
,U;W<V;W++){if((\
U=aa[W])){while(\
(U=U.previousSib\
ling)&&U.nodeTyp\
e!==1){}aa[W]=Y|\
|U&&U.nodeName==\
=T?U||false:U===\
T}}if(Y){F.filte\
r(T,aa,true)}},\x22\
>\x22:function(Z,U,\
aa){var X=typeof\
 U===\x22string\x22;if\
(X&&!/\x5cW/.test(U\
)){U=aa?U:U.toUp\
perCase();for(va\
r V=0,T=Z.length\
;V<T;V++){var Y=\
Z[V];if(Y){var W\
=Y.parentNode;Z[\
V]=W.nodeName===\
U?W:false}}}else\
{for(var V=0,T=Z\
.length;V<T;V++)\
{var Y=Z[V];if(Y\
){Z[V]=X?Y.paren\
tNode:Y.parentNo\
de===U}}if(X){F.\
filter(U,Z,true)\
}}},\x22\x22:function(\
W,U,Y){var V=L++\
,T=S;if(!U.match\
(/\x5cW/)){var X=U=\
Y?U:U.toUpperCas\
e();T=P}T(\x22paren\
tNode\x22,U,V,W,X,Y\
)},\x22~\x22:function(\
W,U,Y){var V=L++\
,T=S;if(typeof U\
===\x22string\x22&&!U.\
match(/\x5cW/)){var\
 X=U=Y?U:U.toUpp\
erCase();T=P}T(\x22\
previousSibling\x22\
,U,V,W,X,Y)}},fi\
nd:{ID:function(\
U,V,W){if(typeof\
 V.getElementByI\
d!==\x22undefined\x22&\
&!W){var T=V.get\
ElementById(U[1]\
);return T?[T]:[\
]}},NAME:functio\
n(V,Y,Z){if(type\
of Y.getElements\
ByName!==\x22undefi\
ned\x22){var U=[],X\
=Y.getElementsBy\
Name(V[1]);for(v\
ar W=0,T=X.lengt\
h;W<T;W++){if(X[\
W].getAttribute(\
\x22name\x22)===V[1]){\
U.push(X[W])}}re\
turn U.length===\
0?null:U}},TAG:f\
unction(T,U){ret\
urn U.getElement\
sByTagName(T[1])\
}},preFilter:{CL\
ASS:function(W,U\
,V,T,Z,aa){W=\x22 \x22\
+W[1].replace(/\x5c\
\x5c/g,\x22\x22)+\x22 \x22;if(a\
a){return W}for(\
var X=0,Y;(Y=U[X\
])!=null;X++){if\
(Y){if(Z^(Y.clas\
sName&&(\x22 \x22+Y.cl\
assName+\x22 \x22).ind\
exOf(W)>=0)){if(\
!V){T.push(Y)}}e\
lse{if(V){U[X]=f\
alse}}}}return f\
alse},ID:functio\
n(T){return T[1]\
.replace(/\x5c\x5c/g,\x22\
\x22)},TAG:function\
(U,T){for(var V=\
0;T[V]===false;V\
++){}return T[V]\
&&Q(T[V])?U[1]:U\
[1].toUpperCase(\
)},CHILD:functio\
n(T){if(T[1]==\x22n\
th\x22){var U=/(-?)\
(\x5cd*)n((?:\x5c+|-)?\
\x5cd*)/.exec(T[2]=\
=\x22even\x22&&\x222n\x22||T\
[2]==\x22odd\x22&&\x222n+\
1\x22||!/\x5cD/.test(T\
[2])&&\x220n+\x22+T[2]\
||T[2]);T[2]=(U[\
1]+(U[2]||1))-0;\
T[3]=U[3]-0}T[0]\
=L++;return T},A\
TTR:function(X,U\
,V,T,Y,Z){var W=\
X[1].replace(/\x5c\x5c\
/g,\x22\x22);if(!Z&&I.\
attrMap[W]){X[1]\
=I.attrMap[W]}if\
(X[2]===\x22~=\x22){X[\
4]=\x22 \x22+X[4]+\x22 \x22}\
return X},PSEUDO\
:function(X,U,V,\
T,Y){if(X[1]===\x22\
not\x22){if(X[3].ma\
tch(R).length>1|\
|/^\x5cw/.test(X[3]\
)){X[3]=F(X[3],n\
ull,null,U)}else\
{var W=F.filter(\
X[3],U,V,true^Y)\
;if(!V){T.push.a\
pply(T,W)}return\
 false}}else{if(\
I.match.POS.test\
(X[0])||I.match.\
CHILD.test(X[0])\
){return true}}r\
eturn X},POS:fun\
ction(T){T.unshi\
ft(true);return \
T}},filters:{ena\
bled:function(T)\
{return T.disabl\
ed===false&&T.ty\
pe!==\x22hidden\x22},d\
isabled:function\
(T){return T.dis\
abled===true},ch\
ecked:function(T\
){return T.check\
ed===true},selec\
ted:function(T){\
T.parentNode.sel\
ectedIndex;retur\
n T.selected===t\
rue},parent:func\
tion(T){return !\
!T.firstChild},e\
mpty:function(T)\
{return !T.first\
Child},has:funct\
ion(V,U,T){retur\
n !!F(T[3],V).le\
ngth},header:fun\
ction(T){return/\
h\x5cd/i.test(T.nod\
eName)},text:fun\
ction(T){return\x22\
text\x22===T.type},\
radio:function(T\
){return\x22radio\x22=\
==T.type},checkb\
ox:function(T){r\
eturn\x22checkbox\x22=\
==T.type},file:f\
unction(T){retur\
n\x22file\x22===T.type\
},password:funct\
ion(T){return\x22pa\
ssword\x22===T.type\
},submit:functio\
n(T){return\x22subm\
it\x22===T.type},im\
age:function(T){\
return\x22image\x22===\
T.type},reset:fu\
nction(T){return\
\x22reset\x22===T.type\
},button:functio\
n(T){return\x22butt\
on\x22===T.type||T.\
nodeName.toUpper\
Case()===\x22BUTTON\
\x22},input:functio\
n(T){return/inpu\
t|select|textare\
a|button/i.test(\
T.nodeName)}},se\
tFilters:{first:\
function(U,T){re\
turn T===0},last\
:function(V,U,T,\
W){return U===W.\
length-1},even:f\
unction(U,T){ret\
urn T%2===0},odd\
:function(U,T){r\
eturn T%2===1},l\
t:function(V,U,T\
){return U<T[3]-\
0},gt:function(V\
,U,T){return U>T\
[3]-0},nth:funct\
ion(V,U,T){retur\
n T[3]-0==U},eq:\
function(V,U,T){\
return T[3]-0==U\
}},filter:{PSEUD\
O:function(Z,V,W\
,aa){var U=V[1],\
X=I.filters[U];i\
f(X){return X(Z,\
W,V,aa)}else{if(\
U===\x22contains\x22){\
return(Z.textCon\
tent||Z.innerTex\
t||\x22\x22).indexOf(V\
[3])>=0}else{if(\
U===\x22not\x22){var Y\
=V[3];for(var W=\
0,T=Y.length;W<T\
;W++){if(Y[W]===\
Z){return false}\
}return true}}}}\
,CHILD:function(\
T,W){var Z=W[1],\
U=T;switch(Z){ca\
se\x22only\x22:case\x22fi\
rst\x22:while(U=U.p\
reviousSibling){\
if(U.nodeType===\
1){return false}\
}if(Z==\x22first\x22){\
return true}U=T;\
case\x22last\x22:while\
(U=U.nextSibling\
){if(U.nodeType=\
==1){return fals\
e}}return true;c\
ase\x22nth\x22:var V=W\
[2],ac=W[3];if(V\
==1&&ac==0){retu\
rn true}var Y=W[\
0],ab=T.parentNo\
de;if(ab&&(ab.si\
zcache!==Y||!T.n\
odeIndex)){var X\
=0;for(U=ab.firs\
tChild;U;U=U.nex\
tSibling){if(U.n\
odeType===1){U.n\
odeIndex=++X}}ab\
.sizcache=Y}var \
aa=T.nodeIndex-a\
c;if(V==0){retur\
n aa==0}else{ret\
urn(aa%V==0&&aa/\
V>=0)}}},ID:func\
tion(U,T){return\
 U.nodeType===1&\
&U.getAttribute(\
\x22id\x22)===T},TAG:f\
unction(U,T){ret\
urn(T===\x22*\x22&&U.n\
odeType===1)||U.\
nodeName===T},CL\
ASS:function(U,T\
){return(\x22 \x22+(U.\
className||U.get\
Attribute(\x22class\
\x22))+\x22 \x22).indexOf\
(T)>-1},ATTR:fun\
ction(Y,W){var V\
=W[1],T=I.attrHa\
ndle[V]?I.attrHa\
ndle[V](Y):Y[V]!\
=null?Y[V]:Y.get\
Attribute(V),Z=T\
+\x22\x22,X=W[2],U=W[4\
];return T==null\
?X===\x22!=\x22:X===\x22=\
\x22?Z===U:X===\x22*=\x22\
?Z.indexOf(U)>=0\
:X===\x22~=\x22?(\x22 \x22+Z\
+\x22 \x22).indexOf(U)\
>=0:!U?Z&&T!==fa\
lse:X===\x22!=\x22?Z!=\
U:X===\x22^=\x22?Z.ind\
exOf(U)===0:X===\
\x22$=\x22?Z.substr(Z.\
length-U.length)\
===U:X===\x22|=\x22?Z=\
==U||Z.substr(0,\
U.length+1)===U+\
\x22-\x22:false},POS:f\
unction(X,U,V,Y)\
{var T=U[2],W=I.\
setFilters[T];if\
(W){return W(X,V\
,U,Y)}}}};var M=\
I.match.POS;for(\
var O in I.match\
){I.match[O]=Reg\
Exp(I.match[O].s\
ource+/(?![^\x5c[]*\
\x5c])(?![^\x5c(]*\x5c))/\
.source)}var E=f\
unction(U,T){U=A\
rray.prototype.s\
lice.call(U);if(\
T){T.push.apply(\
T,U);return T}re\
turn U};try{Arra\
y.prototype.slic\
e.call(document.\
documentElement.\
childNodes)}catc\
h(N){E=function(\
X,W){var U=W||[]\
;if(H.call(X)===\
\x22[object Array]\x22\
){Array.prototyp\
e.push.apply(U,X\
)}else{if(typeof\
 X.length===\x22num\
ber\x22){for(var V=\
0,T=X.length;V<T\
;V++){U.push(X[V\
])}}else{for(var\
 V=0;X[V];V++){U\
.push(X[V])}}}re\
turn U}}var G;if\
(document.docume\
ntElement.compar\
eDocumentPositio\
n){G=function(U,\
T){var V=U.compa\
reDocumentPositi\
on(T)&4?-1:U===T\
?0:1;if(V===0){h\
asDuplicate=true\
}return V}}else{\
if(\x22sourceIndex\x22\
 in document.doc\
umentElement){G=\
function(U,T){va\
r V=U.sourceInde\
x-T.sourceIndex;\
if(V===0){hasDup\
licate=true}retu\
rn V}}else{if(do\
cument.createRan\
ge){G=function(W\
,U){var V=W.owne\
rDocument.create\
Range(),T=U.owne\
rDocument.create\
Range();V.select\
Node(W);V.collap\
se(true);T.selec\
tNode(U);T.colla\
pse(true);var X=\
V.compareBoundar\
yPoints(Range.ST\
ART_TO_END,T);if\
(X===0){hasDupli\
cate=true}return\
 X}}}}(function(\
){var U=document\
.createElement(\x22\
form\x22),V=\x22script\
\x22+(new Date).get\
Time();U.innerHT\
ML=\x22<input name=\
'\x22+V+\x22'/>\x22;var T\
=document.docume\
ntElement;T.inse\
rtBefore(U,T.fir\
stChild);if(!!do\
cument.getElemen\
tById(V)){I.find\
.ID=function(X,Y\
,Z){if(typeof Y.\
getElementById!=\
=\x22undefined\x22&&!Z\
){var W=Y.getEle\
mentById(X[1]);r\
eturn W?W.id===X\
[1]||typeof W.ge\
tAttributeNode!=\
=\x22undefined\x22&&W.\
getAttributeNode\
(\x22id\x22).nodeValue\
===X[1]?[W]:g:[]\
}};I.filter.ID=f\
unction(Y,W){var\
 X=typeof Y.getA\
ttributeNode!==\x22\
undefined\x22&&Y.ge\
tAttributeNode(\x22\
id\x22);return Y.no\
deType===1&&X&&X\
.nodeValue===W}}\
T.removeChild(U)\
})();(function()\
{var T=document.\
createElement(\x22d\
iv\x22);T.appendChi\
ld(document.crea\
teComment(\x22\x22));i\
f(T.getElementsB\
yTagName(\x22*\x22).le\
ngth>0){I.find.T\
AG=function(U,Y)\
{var X=Y.getElem\
entsByTagName(U[\
1]);if(U[1]===\x22*\
\x22){var W=[];for(\
var V=0;X[V];V++\
){if(X[V].nodeTy\
pe===1){W.push(X\
[V])}}X=W}return\
 X}}T.innerHTML=\
\x22<a href='#'></a\
>\x22;if(T.firstChi\
ld&&typeof T.fir\
stChild.getAttri\
bute!==\x22undefine\
d\x22&&T.firstChild\
.getAttribute(\x22h\
ref\x22)!==\x22#\x22){I.a\
ttrHandle.href=f\
unction(U){retur\
n U.getAttribute\
(\x22href\x22,2)}}})()\
;if(document.que\
rySelectorAll){(\
function(){var T\
=F,U=document.cr\
eateElement(\x22div\
\x22);U.innerHTML=\x22\
<p class='TEST'>\
</p>\x22;if(U.query\
SelectorAll&&U.q\
uerySelectorAll(\
\x22.TEST\x22).length=\
==0){return}F=fu\
nction(Y,X,V,W){\
X=X||document;if\
(!W&&X.nodeType=\
==9&&!Q(X)){try{\
return E(X.query\
SelectorAll(Y),V\
)}catch(Z){}}ret\
urn T(Y,X,V,W)};\
F.find=T.find;F.\
filter=T.filter;\
F.selectors=T.se\
lectors;F.matche\
s=T.matches})()}\
if(document.getE\
lementsByClassNa\
me&&document.doc\
umentElement.get\
ElementsByClassN\
ame){(function()\
{var T=document.\
createElement(\x22d\
iv\x22);T.innerHTML\
=\x22<div class='te\
st e'></div><div\
 class='test'></\
div>\x22;if(T.getEl\
ementsByClassNam\
e(\x22e\x22).length===\
0){return}T.last\
Child.className=\
\x22e\x22;if(T.getElem\
entsByClassName(\
\x22e\x22).length===1)\
{return}I.order.\
splice(1,0,\x22CLAS\
S\x22);I.find.CLASS\
=function(U,V,W)\
{if(typeof V.get\
ElementsByClassN\
ame!==\x22undefined\
\x22&&!W){return V.\
getElementsByCla\
ssName(U[1])}}})\
()}function P(U,\
Z,Y,ad,aa,ac){va\
r ab=U==\x22previou\
sSibling\x22&&!ac;f\
or(var W=0,V=ad.\
length;W<V;W++){\
var T=ad[W];if(T\
){if(ab&&T.nodeT\
ype===1){T.sizca\
che=Y;T.sizset=W\
}T=T[U];var X=fa\
lse;while(T){if(\
T.sizcache===Y){\
X=ad[T.sizset];b\
reak}if(T.nodeTy\
pe===1&&!ac){T.s\
izcache=Y;T.sizs\
et=W}if(T.nodeNa\
me===Z){X=T;brea\
k}T=T[U]}ad[W]=X\
}}}function S(U,\
Z,Y,ad,aa,ac){va\
r ab=U==\x22previou\
sSibling\x22&&!ac;f\
or(var W=0,V=ad.\
length;W<V;W++){\
var T=ad[W];if(T\
){if(ab&&T.nodeT\
ype===1){T.sizca\
che=Y;T.sizset=W\
}T=T[U];var X=fa\
lse;while(T){if(\
T.sizcache===Y){\
X=ad[T.sizset];b\
reak}if(T.nodeTy\
pe===1){if(!ac){\
T.sizcache=Y;T.s\
izset=W}if(typeo\
f Z!==\x22string\x22){\
if(T===Z){X=true\
;break}}else{if(\
F.filter(Z,[T]).\
length>0){X=T;br\
eak}}}T=T[U]}ad[\
W]=X}}}var K=doc\
ument.compareDoc\
umentPosition?fu\
nction(U,T){retu\
rn U.compareDocu\
mentPosition(T)&\
16}:function(U,T\
){return U!==T&&\
(U.contains?U.co\
ntains(T):true)}\
;var Q=function(\
T){return T.node\
Type===9&&T.docu\
mentElement.node\
Name!==\x22HTML\x22||!\
!T.ownerDocument\
&&Q(T.ownerDocum\
ent)};var J=func\
tion(T,aa){var W\
=[],X=\x22\x22,Y,V=aa.\
nodeType?[aa]:aa\
;while((Y=I.matc\
h.PSEUDO.exec(T)\
)){X+=Y[0];T=T.r\
eplace(I.match.P\
SEUDO,\x22\x22)}T=I.re\
lative[T]?T+\x22*\x22:\
T;for(var Z=0,U=\
V.length;Z<U;Z++\
){F(T,V[Z],W)}re\
turn F.filter(X,\
W)};o.find=F;o.f\
ilter=F.filter;o\
.expr=F.selector\
s;o.expr[\x22:\x22]=o.\
expr.filters;F.s\
electors.filters\
.hidden=function\
(T){return T.off\
setWidth===0||T.\
offsetHeight===0\
};F.selectors.fi\
lters.visible=fu\
nction(T){return\
 T.offsetWidth>0\
||T.offsetHeight\
>0};F.selectors.\
filters.animated\
=function(T){ret\
urn o.grep(o.tim\
ers,function(U){\
return T===U.ele\
m}).length};o.mu\
ltiFilter=functi\
on(V,T,U){if(U){\
V=\x22:not(\x22+V+\x22)\x22}\
return F.matches\
(V,T)};o.dir=fun\
ction(V,U){var T\
=[],W=V[U];while\
(W&&W!=document)\
{if(W.nodeType==\
1){T.push(W)}W=W\
[U]}return T};o.\
nth=function(X,T\
,V,W){T=T||1;var\
 U=0;for(;X;X=X[\
V]){if(X.nodeTyp\
e==1&&++U==T){br\
eak}}return X};o\
.sibling=functio\
n(V,U){var T=[];\
for(;V;V=V.nextS\
ibling){if(V.nod\
eType==1&&V!=U){\
T.push(V)}}retur\
n T};return;l.Si\
zzle=F})();o.eve\
nt={add:function\
(I,F,H,K){if(I.n\
odeType==3||I.no\
deType==8){retur\
n}if(I.setInterv\
al&&I!=l){I=l}if\
(!H.guid){H.guid\
=this.guid++}if(\
K!==g){var G=H;H\
=this.proxy(G);H\
.data=K}var E=o.\
data(I,\x22events\x22)\
||o.data(I,\x22even\
ts\x22,{}),J=o.data\
(I,\x22handle\x22)||o.\
data(I,\x22handle\x22,\
function(){retur\
n typeof o!==\x22un\
defined\x22&&!o.eve\
nt.triggered?o.e\
vent.handle.appl\
y(arguments.call\
ee.elem,argument\
s):g});J.elem=I;\
o.each(F.split(/\
\x5cs+/),function(M\
,N){var O=N.spli\
t(\x22.\x22);N=O.shift\
();H.type=O.slic\
e().sort().join(\
\x22.\x22);var L=E[N];\
if(o.event.speci\
alAll[N]){o.even\
t.specialAll[N].\
setup.call(I,K,O\
)}if(!L){L=E[N]=\
{};if(!o.event.s\
pecial[N]||o.eve\
nt.special[N].se\
tup.call(I,K,O)=\
==false){if(I.ad\
dEventListener){\
I.addEventListen\
er(N,J,false)}el\
se{if(I.attachEv\
ent){I.attachEve\
nt(\x22on\x22+N,J)}}}}\
L[H.guid]=H;o.ev\
ent.global[N]=tr\
ue});I=null},gui\
d:1,global:{},re\
move:function(K,\
H,J){if(K.nodeTy\
pe==3||K.nodeTyp\
e==8){return}var\
 G=o.data(K,\x22eve\
nts\x22),F,E;if(G){\
if(H===g||(typeo\
f H===\x22string\x22&&\
H.charAt(0)==\x22.\x22\
)){for(var I in \
G){this.remove(K\
,I+(H||\x22\x22))}}els\
e{if(H.type){J=H\
.handler;H=H.typ\
e}o.each(H.split\
(/\x5cs+/),function\
(M,O){var Q=O.sp\
lit(\x22.\x22);O=Q.shi\
ft();var N=RegEx\
p(\x22(^|\x5c\x5c.)\x22+Q.sl\
ice().sort().joi\
n(\x22.*\x5c\x5c.\x22)+\x22(\x5c\x5c.\
|$)\x22);if(G[O]){i\
f(J){delete G[O]\
[J.guid]}else{fo\
r(var P in G[O])\
{if(N.test(G[O][\
P].type)){delete\
 G[O][P]}}}if(o.\
event.specialAll\
[O]){o.event.spe\
cialAll[O].teard\
own.call(K,Q)}fo\
r(F in G[O]){bre\
ak}if(!F){if(!o.\
event.special[O]\
||o.event.specia\
l[O].teardown.ca\
ll(K,Q)===false)\
{if(K.removeEven\
tListener){K.rem\
oveEventListener\
(O,o.data(K,\x22han\
dle\x22),false)}els\
e{if(K.detachEve\
nt){K.detachEven\
t(\x22on\x22+O,o.data(\
K,\x22handle\x22))}}}F\
=null;delete G[O\
]}}})}for(F in G\
){break}if(!F){v\
ar L=o.data(K,\x22h\
andle\x22);if(L){L.\
elem=null}o.remo\
veData(K,\x22events\
\x22);o.removeData(\
K,\x22handle\x22)}}},t\
rigger:function(\
I,K,H,E){var G=I\
.type||I;if(!E){\
I=typeof I===\x22ob\
ject\x22?I[h]?I:o.e\
xtend(o.Event(G)\
,I):o.Event(G);i\
f(G.indexOf(\x22!\x22)\
>=0){I.type=G=G.\
slice(0,-1);I.ex\
clusive=true}if(\
!H){I.stopPropag\
ation();if(this.\
global[G]){o.eac\
h(o.cache,functi\
on(){if(this.eve\
nts&&this.events\
[G]){o.event.tri\
gger(I,K,this.ha\
ndle.elem)}})}}i\
f(!H||H.nodeType\
==3||H.nodeType=\
=8){return g}I.r\
esult=g;I.target\
=H;K=o.makeArray\
(K);K.unshift(I)\
}I.currentTarget\
=H;var J=o.data(\
H,\x22handle\x22);if(J\
){J.apply(H,K)}i\
f((!H[G]||(o.nod\
eName(H,\x22a\x22)&&G=\
=\x22click\x22))&&H[\x22o\
n\x22+G]&&H[\x22on\x22+G]\
.apply(H,K)===fa\
lse){I.result=fa\
lse}if(!E&&H[G]&\
&!I.isDefaultPre\
vented()&&!(o.no\
deName(H,\x22a\x22)&&G\
==\x22click\x22)){this\
.triggered=true;\
try{H[G]()}catch\
(L){}}this.trigg\
ered=false;if(!I\
.isPropagationSt\
opped()){var F=H\
.parentNode||H.o\
wnerDocument;if(\
F){o.event.trigg\
er(I,K,F,true)}}\
},handle:functio\
n(K){var J,E;K=a\
rguments[0]=o.ev\
ent.fix(K||l.eve\
nt);K.currentTar\
get=this;var L=K\
.type.split(\x22.\x22)\
;K.type=L.shift(\
);J=!L.length&&!\
K.exclusive;var \
I=RegExp(\x22(^|\x5c\x5c.\
)\x22+L.slice().sor\
t().join(\x22.*\x5c\x5c.\x22\
)+\x22(\x5c\x5c.|$)\x22);E=(\
o.data(this,\x22eve\
nts\x22)||{})[K.typ\
e];for(var G in \
E){var H=E[G];if\
(J||I.test(H.typ\
e)){K.handler=H;\
K.data=H.data;va\
r F=H.apply(this\
,arguments);if(F\
!==g){K.result=F\
;if(F===false){K\
.preventDefault(\
);K.stopPropagat\
ion()}}if(K.isIm\
mediatePropagati\
onStopped()){bre\
ak}}}},props:\x22al\
tKey attrChange \
attrName bubbles\
 button cancelab\
le charCode clie\
ntX clientY ctrl\
Key currentTarge\
t data detail ev\
entPhase fromEle\
ment handler key\
Code metaKey new\
Value originalTa\
rget pageX pageY\
 prevValue relat\
edNode relatedTa\
rget screenX scr\
eenY shiftKey sr\
cElement target \
toElement view w\
heelDelta which\x22\
.split(\x22 \x22),fix:\
function(H){if(H\
[h]){return H}va\
r F=H;H=o.Event(\
F);for(var G=thi\
s.props.length,J\
;G;){J=this.prop\
s[--G];H[J]=F[J]\
}if(!H.target){H\
.target=H.srcEle\
ment||document}i\
f(H.target.nodeT\
ype==3){H.target\
=H.target.parent\
Node}if(!H.relat\
edTarget&&H.from\
Element){H.relat\
edTarget=H.fromE\
lement==H.target\
?H.toElement:H.f\
romElement}if(H.\
pageX==null&&H.c\
lientX!=null){va\
r I=document.doc\
umentElement,E=d\
ocument.body;H.p\
ageX=H.clientX+(\
I&&I.scrollLeft|\
|E&&E.scrollLeft\
||0)-(I.clientLe\
ft||0);H.pageY=H\
.clientY+(I&&I.s\
crollTop||E&&E.s\
crollTop||0)-(I.\
clientTop||0)}if\
(!H.which&&((H.c\
harCode||H.charC\
ode===0)?H.charC\
ode:H.keyCode)){\
H.which=H.charCo\
de||H.keyCode}if\
(!H.metaKey&&H.c\
trlKey){H.metaKe\
y=H.ctrlKey}if(!\
H.which&&H.butto\
n){H.which=(H.bu\
tton&1?1:(H.butt\
on&2?3:(H.button\
&4?2:0)))}return\
 H},proxy:functi\
on(F,E){E=E||fun\
ction(){return F\
.apply(this,argu\
ments)};E.guid=F\
.guid=F.guid||E.\
guid||this.guid+\
+;return E},spec\
ial:{ready:{setu\
p:B,teardown:fun\
ction(){}}},spec\
ialAll:{live:{se\
tup:function(E,F\
){o.event.add(th\
is,F[0],c)},tear\
down:function(G)\
{if(G.length){va\
r E=0,F=RegExp(\x22\
(^|\x5c\x5c.)\x22+G[0]+\x22(\
\x5c\x5c.|$)\x22);o.each(\
(o.data(this,\x22ev\
ents\x22).live||{})\
,function(){if(F\
.test(this.type)\
){E++}});if(E<1)\
{o.event.remove(\
this,G[0],c)}}}}\
}};o.Event=funct\
ion(E){if(!this.\
preventDefault){\
return new o.Eve\
nt(E)}if(E&&E.ty\
pe){this.origina\
lEvent=E;this.ty\
pe=E.type}else{t\
his.type=E}this.\
timeStamp=e();th\
is[h]=true};func\
tion k(){return \
false}function u\
(){return true}o\
.Event.prototype\
={preventDefault\
:function(){this\
.isDefaultPreven\
ted=u;var E=this\
.originalEvent;i\
f(!E){return}if(\
E.preventDefault\
){E.preventDefau\
lt()}E.returnVal\
ue=false},stopPr\
opagation:functi\
on(){this.isProp\
agationStopped=u\
;var E=this.orig\
inalEvent;if(!E)\
{return}if(E.sto\
pPropagation){E.\
stopPropagation(\
)}E.cancelBubble\
=true},stopImmed\
iatePropagation:\
function(){this.\
isImmediatePropa\
gationStopped=u;\
this.stopPropaga\
tion()},isDefaul\
tPrevented:k,isP\
ropagationStoppe\
d:k,isImmediateP\
ropagationStoppe\
d:k};var a=funct\
ion(F){var E=F.r\
elatedTarget;whi\
le(E&&E!=this){t\
ry{E=E.parentNod\
e}catch(G){E=thi\
s}}if(E!=this){F\
.type=F.data;o.e\
vent.handle.appl\
y(this,arguments\
)}};o.each({mous\
eover:\x22mouseente\
r\x22,mouseout:\x22mou\
seleave\x22},functi\
on(F,E){o.event.\
special[E]={setu\
p:function(){o.e\
vent.add(this,F,\
a,E)},teardown:f\
unction(){o.even\
t.remove(this,F,\
a)}}});o.fn.exte\
nd({bind:functio\
n(F,G,E){return \
F==\x22unload\x22?this\
.one(F,G,E):this\
.each(function()\
{o.event.add(thi\
s,F,E||G,E&&G)})\
},one:function(G\
,H,F){var E=o.ev\
ent.proxy(F||H,f\
unction(I){o(thi\
s).unbind(I,E);r\
eturn(F||H).appl\
y(this,arguments\
)});return this.\
each(function(){\
o.event.add(this\
,G,E,F&&H)})},un\
bind:function(F,\
E){return this.e\
ach(function(){o\
.event.remove(th\
is,F,E)})},trigg\
er:function(E,F)\
{return this.eac\
h(function(){o.e\
vent.trigger(E,F\
,this)})},trigge\
rHandler:functio\
n(E,G){if(this[0\
]){var F=o.Event\
(E);F.preventDef\
ault();F.stopPro\
pagation();o.eve\
nt.trigger(F,G,t\
his[0]);return F\
.result}},toggle\
:function(G){var\
 E=arguments,F=1\
;while(F<E.lengt\
h){o.event.proxy\
(G,E[F++])}retur\
n this.click(o.e\
vent.proxy(G,fun\
ction(H){this.la\
stToggle=(this.l\
astToggle||0)%F;\
H.preventDefault\
();return E[this\
.lastToggle++].a\
pply(this,argume\
nts)||false}))},\
hover:function(E\
,F){return this.\
mouseenter(E).mo\
useleave(F)},rea\
dy:function(E){B\
();if(o.isReady)\
{E.call(document\
,o)}else{o.ready\
List.push(E)}ret\
urn this},live:f\
unction(G,F){var\
 E=o.event.proxy\
(F);E.guid+=this\
.selector+G;o(do\
cument).bind(i(G\
,this.selector),\
this.selector,E)\
;return this},di\
e:function(F,E){\
o(document).unbi\
nd(i(F,this.sele\
ctor),E?{guid:E.\
guid+this.select\
or+F}:null);retu\
rn this}});funct\
ion c(H){var E=R\
egExp(\x22(^|\x5c\x5c.)\x22+\
H.type+\x22(\x5c\x5c.|$)\x22\
),G=true,F=[];o.\
each(o.data(this\
,\x22events\x22).live|\
|[],function(I,J\
){if(E.test(J.ty\
pe)){var K=o(H.t\
arget).closest(J\
.data)[0];if(K){\
F.push({elem:K,f\
n:J})}}});F.sort\
(function(J,I){r\
eturn o.data(J.e\
lem,\x22closest\x22)-o\
.data(I.elem,\x22cl\
osest\x22)});o.each\
(F,function(){if\
(this.fn.call(th\
is.elem,H,this.f\
n.data)===false)\
{return(G=false)\
}});return G}fun\
ction i(F,E){ret\
urn[\x22live\x22,F,E.r\
eplace(/\x5c./g,\x22`\x22\
).replace(/ /g,\x22\
|\x22)].join(\x22.\x22)}o\
.extend({isReady\
:false,readyList\
:[],ready:functi\
on(){if(!o.isRea\
dy){o.isReady=tr\
ue;if(o.readyLis\
t){o.each(o.read\
yList,function()\
{this.call(docum\
ent,o)});o.ready\
List=null}o(docu\
ment).triggerHan\
dler(\x22ready\x22)}}}\
);var x=false;fu\
nction B(){if(x)\
{return}x=true;i\
f(document.addEv\
entListener){doc\
ument.addEventLi\
stener(\x22DOMConte\
ntLoaded\x22,functi\
on(){document.re\
moveEventListene\
r(\x22DOMContentLoa\
ded\x22,arguments.c\
allee,false);o.r\
eady()},false)}e\
lse{if(document.\
attachEvent){doc\
ument.attachEven\
t(\x22onreadystatec\
hange\x22,function(\
){if(document.re\
adyState===\x22comp\
lete\x22){document.\
detachEvent(\x22onr\
eadystatechange\x22\
,arguments.calle\
e);o.ready()}});\
if(document.docu\
mentElement.doSc\
roll&&l==l.top){\
(function(){if(o\
.isReady){return\
}try{document.do\
cumentElement.do\
Scroll(\x22left\x22)}c\
atch(E){setTimeo\
ut(arguments.cal\
lee,0);return}o.\
ready()})()}}}o.\
event.add(l,\x22loa\
d\x22,o.ready)}o.ea\
ch((\x22blur,focus,\
load,resize,scro\
ll,unload,click,\
dblclick,mousedo\
wn,mouseup,mouse\
move,mouseover,m\
ouseout,mouseent\
er,mouseleave,ch\
ange,select,subm\
it,keydown,keypr\
ess,keyup,error\x22\
).split(\x22,\x22),fun\
ction(F,E){o.fn[\
E]=function(G){r\
eturn G?this.bin\
d(E,G):this.trig\
ger(E)}});o(l).b\
ind(\x22unload\x22,fun\
ction(){for(var \
E in o.cache){if\
(E!=1&&o.cache[E\
].handle){o.even\
t.remove(o.cache\
[E].handle.elem)\
}}});(function()\
{o.support={};va\
r F=document.doc\
umentElement,G=d\
ocument.createEl\
ement(\x22script\x22),\
K=document.creat\
eElement(\x22div\x22),\
J=\x22script\x22+(new \
Date).getTime();\
K.style.display=\
\x22none\x22;K.innerHT\
ML='   <link/><t\
able></table><a \
href=\x22/a\x22 style=\
\x22color:red;float\
:left;opacity:.5\
;\x22>a</a><select>\
<option>text</op\
tion></select><o\
bject><param/></\
object>';var H=K\
.getElementsByTa\
gName(\x22*\x22),E=K.g\
etElementsByTagN\
ame(\x22a\x22)[0];if(!\
H||!H.length||!E\
){return}o.suppo\
rt={leadingWhite\
space:K.firstChi\
ld.nodeType==3,t\
body:!K.getEleme\
ntsByTagName(\x22tb\
ody\x22).length,obj\
ectAll:!!K.getEl\
ementsByTagName(\
\x22object\x22)[0].get\
ElementsByTagNam\
e(\x22*\x22).length,ht\
mlSerialize:!!K.\
getElementsByTag\
Name(\x22link\x22).len\
gth,style:/red/.\
test(E.getAttrib\
ute(\x22style\x22)),hr\
efNormalized:E.g\
etAttribute(\x22hre\
f\x22)===\x22/a\x22,opaci\
ty:E.style.opaci\
ty===\x220.5\x22,cssFl\
oat:!!E.style.cs\
sFloat,scriptEva\
l:false,noCloneE\
vent:true,boxMod\
el:null};G.type=\
\x22text/javascript\
\x22;try{G.appendCh\
ild(document.cre\
ateTextNode(\x22win\
dow.\x22+J+\x22=1;\x22))}\
catch(I){}F.inse\
rtBefore(G,F.fir\
stChild);if(l[J]\
){o.support.scri\
ptEval=true;dele\
te l[J]}F.remove\
Child(G);if(K.at\
tachEvent&&K.fir\
eEvent){K.attach\
Event(\x22onclick\x22,\
function(){o.sup\
port.noCloneEven\
t=false;K.detach\
Event(\x22onclick\x22,\
arguments.callee\
)});K.cloneNode(\
true).fireEvent(\
\x22onclick\x22)}o(fun\
ction(){var L=do\
cument.createEle\
ment(\x22div\x22);L.st\
yle.width=L.styl\
e.paddingLeft=\x221\
px\x22;document.bod\
y.appendChild(L)\
;o.boxModel=o.su\
pport.boxModel=L\
.offsetWidth===2\
;document.body.r\
emoveChild(L).st\
yle.display=\x22non\
e\x22})})();var w=o\
.support.cssFloa\
t?\x22cssFloat\x22:\x22st\
yleFloat\x22;o.prop\
s={\x22for\x22:\x22htmlFo\
r\x22,\x22class\x22:\x22clas\
sName\x22,\x22float\x22:w\
,cssFloat:w,styl\
eFloat:w,readonl\
y:\x22readOnly\x22,max\
length:\x22maxLengt\
h\x22,cellspacing:\x22\
cellSpacing\x22,row\
span:\x22rowSpan\x22,t\
abindex:\x22tabInde\
x\x22};o.fn.extend(\
{_load:o.fn.load\
,load:function(G\
,J,K){if(typeof \
G!==\x22string\x22){re\
turn this._load(\
G)}var I=G.index\
Of(\x22 \x22);if(I>=0)\
{var E=G.slice(I\
,G.length);G=G.s\
lice(0,I)}var H=\
\x22GET\x22;if(J){if(o\
.isFunction(J)){\
K=J;J=null}else{\
if(typeof J===\x22o\
bject\x22){J=o.para\
m(J);H=\x22POST\x22}}}\
var F=this;o.aja\
x({url:G,type:H,\
dataType:\x22html\x22,\
data:J,complete:\
function(M,L){if\
(L==\x22success\x22||L\
==\x22notmodified\x22)\
{F.html(E?o(\x22<di\
v/>\x22).append(M.r\
esponseText.repl\
ace(/<script(.|\x5c\
s)*?\x5c/script>/g,\
\x22\x22)).find(E):M.r\
esponseText)}if(\
K){F.each(K,[M.r\
esponseText,L,M]\
)}}});return thi\
s},serialize:fun\
ction(){return o\
.param(this.seri\
alizeArray())},s\
erializeArray:fu\
nction(){return \
this.map(functio\
n(){return this.\
elements?o.makeA\
rray(this.elemen\
ts):this}).filte\
r(function(){ret\
urn this.name&&!\
this.disabled&&(\
this.checked||/s\
elect|textarea/i\
.test(this.nodeN\
ame)||/text|hidd\
en|password|sear\
ch/i.test(this.t\
ype))}).map(func\
tion(E,F){var G=\
o(this).val();re\
turn G==null?nul\
l:o.isArray(G)?o\
.map(G,function(\
I,H){return{name\
:F.name,value:I}\
}):{name:F.name,\
value:G}}).get()\
}});o.each(\x22ajax\
Start,ajaxStop,a\
jaxComplete,ajax\
Error,ajaxSucces\
s,ajaxSend\x22.spli\
t(\x22,\x22),function(\
E,F){o.fn[F]=fun\
ction(G){return \
this.bind(F,G)}}\
);var r=e();o.ex\
tend({get:functi\
on(E,G,H,F){if(o\
.isFunction(G)){\
H=G;G=null}retur\
n o.ajax({type:\x22\
GET\x22,url:E,data:\
G,success:H,data\
Type:F})},getScr\
ipt:function(E,F\
){return o.get(E\
,null,F,\x22script\x22\
)},getJSON:funct\
ion(E,F,G){retur\
n o.get(E,F,G,\x22j\
son\x22)},post:func\
tion(E,G,H,F){if\
(o.isFunction(G)\
){H=G;G={}}retur\
n o.ajax({type:\x22\
POST\x22,url:E,data\
:G,success:H,dat\
aType:F})},ajaxS\
etup:function(E)\
{o.extend(o.ajax\
Settings,E)},aja\
xSettings:{url:l\
ocation.href,glo\
bal:true,type:\x22G\
ET\x22,contentType:\
\x22application/x-w\
ww-form-urlencod\
ed\x22,processData:\
true,async:true,\
xhr:function(){r\
eturn l.ActiveXO\
bject?new Active\
XObject(\x22Microso\
ft.XMLHTTP\x22):new\
 XMLHttpRequest(\
)},accepts:{xml:\
\x22application/xml\
, text/xml\x22,html\
:\x22text/html\x22,scr\
ipt:\x22text/javasc\
ript, applicatio\
n/javascript\x22,js\
on:\x22application/\
json, text/javas\
cript\x22,text:\x22tex\
t/plain\x22,_defaul\
t:\x22*/*\x22}},lastMo\
dified:{},ajax:f\
unction(M){M=o.e\
xtend(true,M,o.e\
xtend(true,{},o.\
ajaxSettings,M))\
;var W,F=/=\x5c?(&|\
$)/g,R,V,G=M.typ\
e.toUpperCase();\
if(M.data&&M.pro\
cessData&&typeof\
 M.data!==\x22strin\
g\x22){M.data=o.par\
am(M.data)}if(M.\
dataType==\x22jsonp\
\x22){if(G==\x22GET\x22){\
if(!M.url.match(\
F)){M.url+=(M.ur\
l.match(/\x5c?/)?\x22&\
\x22:\x22?\x22)+(M.jsonp|\
|\x22callback\x22)+\x22=?\
\x22}}else{if(!M.da\
ta||!M.data.matc\
h(F)){M.data=(M.\
data?M.data+\x22&\x22:\
\x22\x22)+(M.jsonp||\x22c\
allback\x22)+\x22=?\x22}}\
M.dataType=\x22json\
\x22}if(M.dataType=\
=\x22json\x22&&(M.data\
&&M.data.match(F\
)||M.url.match(F\
))){W=\x22jsonp\x22+r+\
+;if(M.data){M.d\
ata=(M.data+\x22\x22).\
replace(F,\x22=\x22+W+\
\x22$1\x22)}M.url=M.ur\
l.replace(F,\x22=\x22+\
W+\x22$1\x22);M.dataTy\
pe=\x22script\x22;l[W]\
=function(X){V=X\
;I();L();l[W]=g;\
try{delete l[W]}\
catch(Y){}if(H){\
H.removeChild(T)\
}}}if(M.dataType\
==\x22script\x22&&M.ca\
che==null){M.cac\
he=false}if(M.ca\
che===false&&G==\
\x22GET\x22){var E=e()\
;var U=M.url.rep\
lace(/(\x5c?|&)_=.*\
?(&|$)/,\x22$1_=\x22+E\
+\x22$2\x22);M.url=U+(\
(U==M.url)?(M.ur\
l.match(/\x5c?/)?\x22&\
\x22:\x22?\x22)+\x22_=\x22+E:\x22\x22\
)}if(M.data&&G==\
\x22GET\x22){M.url+=(M\
.url.match(/\x5c?/)\
?\x22&\x22:\x22?\x22)+M.data\
;M.data=null}if(\
M.global&&!o.act\
ive++){o.event.t\
rigger(\x22ajaxStar\
t\x22)}var Q=/^(\x5cw+\
:)?\x5c/\x5c/([^\x5c/?#]+\
)/.exec(M.url);i\
f(M.dataType==\x22s\
cript\x22&&G==\x22GET\x22\
&&Q&&(Q[1]&&Q[1]\
!=location.proto\
col||Q[2]!=locat\
ion.host)){var H\
=document.getEle\
mentsByTagName(\x22\
head\x22)[0];var T=\
document.createE\
lement(\x22script\x22)\
;T.src=M.url;if(\
M.scriptCharset)\
{T.charset=M.scr\
iptCharset}if(!W\
){var O=false;T.\
onload=T.onready\
statechange=func\
tion(){if(!O&&(!\
this.readyState|\
|this.readyState\
==\x22loaded\x22||this\
.readyState==\x22co\
mplete\x22)){O=true\
;I();L();T.onloa\
d=T.onreadystate\
change=null;H.re\
moveChild(T)}}}H\
.appendChild(T);\
return g}var K=f\
alse;var J=M.xhr\
();if(M.username\
){J.open(G,M.url\
,M.async,M.usern\
ame,M.password)}\
else{J.open(G,M.\
url,M.async)}try\
{if(M.data){J.se\
tRequestHeader(\x22\
Content-Type\x22,M.\
contentType)}if(\
M.ifModified){J.\
setRequestHeader\
(\x22If-Modified-Si\
nce\x22,o.lastModif\
ied[M.url]||\x22Thu\
, 01 Jan 1970 00\
:00:00 GMT\x22)}J.s\
etRequestHeader(\
\x22X-Requested-Wit\
h\x22,\x22XMLHttpReque\
st\x22);J.setReques\
tHeader(\x22Accept\x22\
,M.dataType&&M.a\
ccepts[M.dataTyp\
e]?M.accepts[M.d\
ataType]+\x22, */*\x22\
:M.accepts._defa\
ult)}catch(S){}i\
f(M.beforeSend&&\
M.beforeSend(J,M\
)===false){if(M.\
global&&!--o.act\
ive){o.event.tri\
gger(\x22ajaxStop\x22)\
}J.abort();retur\
n false}if(M.glo\
bal){o.event.tri\
gger(\x22ajaxSend\x22,\
[J,M])}var N=fun\
ction(X){if(J.re\
adyState==0){if(\
P){clearInterval\
(P);P=null;if(M.\
global&&!--o.act\
ive){o.event.tri\
gger(\x22ajaxStop\x22)\
}}}else{if(!K&&J\
&&(J.readyState=\
=4||X==\x22timeout\x22\
)){K=true;if(P){\
clearInterval(P)\
;P=null}R=X==\x22ti\
meout\x22?\x22timeout\x22\
:!o.httpSuccess(\
J)?\x22error\x22:M.ifM\
odified&&o.httpN\
otModified(J,M.u\
rl)?\x22notmodified\
\x22:\x22success\x22;if(R\
==\x22success\x22){try\
{V=o.httpData(J,\
M.dataType,M)}ca\
tch(Z){R=\x22parser\
error\x22}}if(R==\x22s\
uccess\x22){var Y;t\
ry{Y=J.getRespon\
seHeader(\x22Last-M\
odified\x22)}catch(\
Z){}if(M.ifModif\
ied&&Y){o.lastMo\
dified[M.url]=Y}\
if(!W){I()}}else\
{o.handleError(M\
,J,R)}L();if(X){\
J.abort()}if(M.a\
sync){J=null}}}}\
;if(M.async){var\
 P=setInterval(N\
,13);if(M.timeou\
t>0){setTimeout(\
function(){if(J&\
&!K){N(\x22timeout\x22\
)}},M.timeout)}}\
try{J.send(M.dat\
a)}catch(S){o.ha\
ndleError(M,J,nu\
ll,S)}if(!M.asyn\
c){N()}function \
I(){if(M.success\
){M.success(V,R)\
}if(M.global){o.\
event.trigger(\x22a\
jaxSuccess\x22,[J,M\
])}}function L()\
{if(M.complete){\
M.complete(J,R)}\
if(M.global){o.e\
vent.trigger(\x22aj\
axComplete\x22,[J,M\
])}if(M.global&&\
!--o.active){o.e\
vent.trigger(\x22aj\
axStop\x22)}}return\
 J},handleError:\
function(F,H,E,G\
){if(F.error){F.\
error(H,E,G)}if(\
F.global){o.even\
t.trigger(\x22ajaxE\
rror\x22,[H,F,G])}}\
,active:0,httpSu\
ccess:function(F\
){try{return !F.\
status&&location\
.protocol==\x22file\
:\x22||(F.status>=2\
00&&F.status<300\
)||F.status==304\
||F.status==1223\
}catch(E){}retur\
n false},httpNot\
Modified:functio\
n(G,E){try{var H\
=G.getResponseHe\
ader(\x22Last-Modif\
ied\x22);return G.s\
tatus==304||H==o\
.lastModified[E]\
}catch(F){}retur\
n false},httpDat\
a:function(J,H,G\
){var F=J.getRes\
ponseHeader(\x22con\
tent-type\x22),E=H=\
=\x22xml\x22||!H&&F&&F\
.indexOf(\x22xml\x22)>\
=0,I=E?J.respons\
eXML:J.responseT\
ext;if(E&&I.docu\
mentElement.tagN\
ame==\x22parsererro\
r\x22){throw\x22parser\
error\x22}if(G&&G.d\
ataFilter){I=G.d\
ataFilter(I,H)}i\
f(typeof I===\x22st\
ring\x22){if(H==\x22sc\
ript\x22){o.globalE\
val(I)}if(H==\x22js\
on\x22){I=l[\x22eval\x22]\
(\x22(\x22+I+\x22)\x22)}}ret\
urn I},param:fun\
ction(E){var G=[\
];function H(I,J\
){G[G.length]=en\
codeURIComponent\
(I)+\x22=\x22+encodeUR\
IComponent(J)}if\
(o.isArray(E)||E\
.jquery){o.each(\
E,function(){H(t\
his.name,this.va\
lue)})}else{for(\
var F in E){if(o\
.isArray(E[F])){\
o.each(E[F],func\
tion(){H(F,this)\
})}else{H(F,o.is\
Function(E[F])?E\
[F]():E[F])}}}re\
turn G.join(\x22&\x22)\
.replace(/%20/g,\
\x22+\x22)}});var m={}\
,n,d=[[\x22height\x22,\
\x22marginTop\x22,\x22mar\
ginBottom\x22,\x22padd\
ingTop\x22,\x22padding\
Bottom\x22],[\x22width\
\x22,\x22marginLeft\x22,\x22\
marginRight\x22,\x22pa\
ddingLeft\x22,\x22padd\
ingRight\x22],[\x22opa\
city\x22]];function\
 t(F,E){var G={}\
;o.each(d.concat\
.apply([],d.slic\
e(0,E)),function\
(){G[this]=F});r\
eturn G}o.fn.ext\
end({show:functi\
on(J,L){if(J){re\
turn this.animat\
e(t(\x22show\x22,3),J,\
L)}else{for(var \
H=0,F=this.lengt\
h;H<F;H++){var E\
=o.data(this[H],\
\x22olddisplay\x22);th\
is[H].style.disp\
lay=E||\x22\x22;if(o.c\
ss(this[H],\x22disp\
lay\x22)===\x22none\x22){\
var G=this[H].ta\
gName,K;if(m[G])\
{K=m[G]}else{var\
 I=o(\x22<\x22+G+\x22 />\x22\
).appendTo(\x22body\
\x22);K=I.css(\x22disp\
lay\x22);if(K===\x22no\
ne\x22){K=\x22block\x22}I\
.remove();m[G]=K\
}o.data(this[H],\
\x22olddisplay\x22,K)}\
}for(var H=0,F=t\
his.length;H<F;H\
++){this[H].styl\
e.display=o.data\
(this[H],\x22olddis\
play\x22)||\x22\x22}retur\
n this}},hide:fu\
nction(H,I){if(H\
){return this.an\
imate(t(\x22hide\x22,3\
),H,I)}else{for(\
var G=0,F=this.l\
ength;G<F;G++){v\
ar E=o.data(this\
[G],\x22olddisplay\x22\
);if(!E&&E!==\x22no\
ne\x22){o.data(this\
[G],\x22olddisplay\x22\
,o.css(this[G],\x22\
display\x22))}}for(\
var G=0,F=this.l\
ength;G<F;G++){t\
his[G].style.dis\
play=\x22none\x22}retu\
rn this}},_toggl\
e:o.fn.toggle,to\
ggle:function(G,\
F){var E=typeof \
G===\x22boolean\x22;re\
turn o.isFunctio\
n(G)&&o.isFuncti\
on(F)?this._togg\
le.apply(this,ar\
guments):G==null\
||E?this.each(fu\
nction(){var H=E\
?G:o(this).is(\x22:\
hidden\x22);o(this)\
[H?\x22show\x22:\x22hide\x22\
]()}):this.anima\
te(t(\x22toggle\x22,3)\
,G,F)},fadeTo:fu\
nction(E,G,F){re\
turn this.animat\
e({opacity:G},E,\
F)},animate:func\
tion(I,F,H,G){va\
r E=o.speed(F,H,\
G);return this[E\
.queue===false?\x22\
each\x22:\x22queue\x22](f\
unction(){var K=\
o.extend({},E),M\
,L=this.nodeType\
==1&&o(this).is(\
\x22:hidden\x22),J=thi\
s;for(M in I){if\
(I[M]==\x22hide\x22&&L\
||I[M]==\x22show\x22&&\
!L){return K.com\
plete.call(this)\
}if((M==\x22height\x22\
||M==\x22width\x22)&&t\
his.style){K.dis\
play=o.css(this,\
\x22display\x22);K.ove\
rflow=this.style\
.overflow}}if(K.\
overflow!=null){\
this.style.overf\
low=\x22hidden\x22}K.c\
urAnim=o.extend(\
{},I);o.each(I,f\
unction(O,S){var\
 R=new o.fx(J,K,\
O);if(/toggle|sh\
ow|hide/.test(S)\
){R[S==\x22toggle\x22?\
L?\x22show\x22:\x22hide\x22:\
S](I)}else{var Q\
=S.toString().ma\
tch(/^([+-]=)?([\
\x5cd+-.]+)(.*)$/),\
T=R.cur(true)||0\
;if(Q){var N=par\
seFloat(Q[2]),P=\
Q[3]||\x22px\x22;if(P!\
=\x22px\x22){J.style[O\
]=(N||1)+P;T=((N\
||1)/R.cur(true)\
)*T;J.style[O]=T\
+P}if(Q[1]){N=((\
Q[1]==\x22-=\x22?-1:1)\
*N)+T}R.custom(T\
,N,P)}else{R.cus\
tom(T,S,\x22\x22)}}});\
return true})},s\
top:function(F,E\
){var G=o.timers\
;if(F){this.queu\
e([])}this.each(\
function(){for(v\
ar H=G.length-1;\
H>=0;H--){if(G[H\
].elem==this){if\
(E){G[H](true)}G\
.splice(H,1)}}})\
;if(!E){this.deq\
ueue()}return th\
is}});o.each({sl\
ideDown:t(\x22show\x22\
,1),slideUp:t(\x22h\
ide\x22,1),slideTog\
gle:t(\x22toggle\x22,1\
),fadeIn:{opacit\
y:\x22show\x22},fadeOu\
t:{opacity:\x22hide\
\x22}},function(E,F\
){o.fn[E]=functi\
on(G,H){return t\
his.animate(F,G,\
H)}});o.extend({\
speed:function(G\
,H,F){var E=type\
of G===\x22object\x22?\
G:{complete:F||!\
F&&H||o.isFuncti\
on(G)&&G,duratio\
n:G,easing:F&&H|\
|H&&!o.isFunctio\
n(H)&&H};E.durat\
ion=o.fx.off?0:t\
ypeof E.duration\
===\x22number\x22?E.du\
ration:o.fx.spee\
ds[E.duration]||\
o.fx.speeds._def\
ault;E.old=E.com\
plete;E.complete\
=function(){if(E\
.queue!==false){\
o(this).dequeue(\
)}if(o.isFunctio\
n(E.old)){E.old.\
call(this)}};ret\
urn E},easing:{l\
inear:function(G\
,H,E,F){return E\
+F*G},swing:func\
tion(G,H,E,F){re\
turn((-Math.cos(\
G*Math.PI)/2)+0.\
5)*F+E}},timers:\
[],fx:function(F\
,E,G){this.optio\
ns=E;this.elem=F\
;this.prop=G;if(\
!E.orig){E.orig=\
{}}}});o.fx.prot\
otype={update:fu\
nction(){if(this\
.options.step){t\
his.options.step\
.call(this.elem,\
this.now,this)}(\
o.fx.step[this.p\
rop]||o.fx.step.\
_default)(this);\
if((this.prop==\x22\
height\x22||this.pr\
op==\x22width\x22)&&th\
is.elem.style){t\
his.elem.style.d\
isplay=\x22block\x22}}\
,cur:function(F)\
{if(this.elem[th\
is.prop]!=null&&\
(!this.elem.styl\
e||this.elem.sty\
le[this.prop]==n\
ull)){return thi\
s.elem[this.prop\
]}var E=parseFlo\
at(o.css(this.el\
em,this.prop,F))\
;return E&&E>-10\
000?E:parseFloat\
(o.curCSS(this.e\
lem,this.prop))|\
|0},custom:funct\
ion(I,H,G){this.\
startTime=e();th\
is.start=I;this.\
end=H;this.unit=\
G||this.unit||\x22p\
x\x22;this.now=this\
.start;this.pos=\
this.state=0;var\
 E=this;function\
 F(J){return E.s\
tep(J)}F.elem=th\
is.elem;if(F()&&\
o.timers.push(F)\
&&!n){n=setInter\
val(function(){v\
ar K=o.timers;fo\
r(var J=0;J<K.le\
ngth;J++){if(!K[\
J]()){K.splice(J\
--,1)}}if(!K.len\
gth){clearInterv\
al(n);n=g}},13)}\
},show:function(\
){this.options.o\
rig[this.prop]=o\
.attr(this.elem.\
style,this.prop)\
;this.options.sh\
ow=true;this.cus\
tom(this.prop==\x22\
width\x22||this.pro\
p==\x22height\x22?1:0,\
this.cur());o(th\
is.elem).show()}\
,hide:function()\
{this.options.or\
ig[this.prop]=o.\
attr(this.elem.s\
tyle,this.prop);\
this.options.hid\
e=true;this.cust\
om(this.cur(),0)\
},step:function(\
H){var G=e();if(\
H||G>=this.optio\
ns.duration+this\
.startTime){this\
.now=this.end;th\
is.pos=this.stat\
e=1;this.update(\
);this.options.c\
urAnim[this.prop\
]=true;var E=tru\
e;for(var F in t\
his.options.curA\
nim){if(this.opt\
ions.curAnim[F]!\
==true){E=false}\
}if(E){if(this.o\
ptions.display!=\
null){this.elem.\
style.overflow=t\
his.options.over\
flow;this.elem.s\
tyle.display=thi\
s.options.displa\
y;if(o.css(this.\
elem,\x22display\x22)=\
=\x22none\x22){this.el\
em.style.display\
=\x22block\x22}}if(thi\
s.options.hide){\
o(this.elem).hid\
e()}if(this.opti\
ons.hide||this.o\
ptions.show){for\
(var I in this.o\
ptions.curAnim){\
o.attr(this.elem\
.style,I,this.op\
tions.orig[I])}}\
this.options.com\
plete.call(this.\
elem)}return fal\
se}else{var J=G-\
this.startTime;t\
his.state=J/this\
.options.duratio\
n;this.pos=o.eas\
ing[this.options\
.easing||(o.easi\
ng.swing?\x22swing\x22\
:\x22linear\x22)](this\
.state,J,0,1,thi\
s.options.durati\
on);this.now=thi\
s.start+((this.e\
nd-this.start)*t\
his.pos);this.up\
date()}return tr\
ue}};o.extend(o.\
fx,{speeds:{slow\
:600,fast:200,_d\
efault:400},step\
:{opacity:functi\
on(E){o.attr(E.e\
lem.style,\x22opaci\
ty\x22,E.now)},_def\
ault:function(E)\
{if(E.elem.style\
&&E.elem.style[E\
.prop]!=null){E.\
elem.style[E.pro\
p]=E.now+E.unit}\
else{E.elem[E.pr\
op]=E.now}}}});i\
f(document.docum\
entElement.getBo\
undingClientRect\
){o.fn.offset=fu\
nction(){if(!thi\
s[0]){return{top\
:0,left:0}}if(th\
is[0]===this[0].\
ownerDocument.bo\
dy){return o.off\
set.bodyOffset(t\
his[0])}var G=th\
is[0].getBoundin\
gClientRect(),J=\
this[0].ownerDoc\
ument,F=J.body,E\
=J.documentEleme\
nt,L=E.clientTop\
||F.clientTop||0\
,K=E.clientLeft|\
|F.clientLeft||0\
,I=G.top+(self.p\
ageYOffset||o.bo\
xModel&&E.scroll\
Top||F.scrollTop\
)-L,H=G.left+(se\
lf.pageXOffset||\
o.boxModel&&E.sc\
rollLeft||F.scro\
llLeft)-K;return\
{top:I,left:H}}}\
else{o.fn.offset\
=function(){if(!\
this[0]){return{\
top:0,left:0}}if\
(this[0]===this[\
0].ownerDocument\
.body){return o.\
offset.bodyOffse\
t(this[0])}o.off\
set.initialized|\
|o.offset.initia\
lize();var J=thi\
s[0],G=J.offsetP\
arent,F=J,O=J.ow\
nerDocument,M,H=\
O.documentElemen\
t,K=O.body,L=O.d\
efaultView,E=L.g\
etComputedStyle(\
J,null),N=J.offs\
etTop,I=J.offset\
Left;while((J=J.\
parentNode)&&J!=\
=K&&J!==H){M=L.g\
etComputedStyle(\
J,null);N-=J.scr\
ollTop,I-=J.scro\
llLeft;if(J===G)\
{N+=J.offsetTop,\
I+=J.offsetLeft;\
if(o.offset.does\
NotAddBorder&&!(\
o.offset.doesAdd\
BorderForTableAn\
dCells&&/^t(able\
|d|h)$/i.test(J.\
tagName))){N+=pa\
rseInt(M.borderT\
opWidth,10)||0,I\
+=parseInt(M.bor\
derLeftWidth,10)\
||0}F=G,G=J.offs\
etParent}if(o.of\
fset.subtractsBo\
rderForOverflowN\
otVisible&&M.ove\
rflow!==\x22visible\
\x22){N+=parseInt(M\
.borderTopWidth,\
10)||0,I+=parseI\
nt(M.borderLeftW\
idth,10)||0}E=M}\
if(E.position===\
\x22relative\x22||E.po\
sition===\x22static\
\x22){N+=K.offsetTo\
p,I+=K.offsetLef\
t}if(E.position=\
==\x22fixed\x22){N+=Ma\
th.max(H.scrollT\
op,K.scrollTop),\
I+=Math.max(H.sc\
rollLeft,K.scrol\
lLeft)}return{to\
p:N,left:I}}}o.o\
ffset={initializ\
e:function(){if(\
this.initialized\
){return}var L=d\
ocument.body,F=d\
ocument.createEl\
ement(\x22div\x22),H,G\
,N,I,M,E,J=L.sty\
le.marginTop,K='\
<div style=\x22posi\
tion:absolute;to\
p:0;left:0;margi\
n:0;border:5px s\
olid #000;paddin\
g:0;width:1px;he\
ight:1px;\x22><div>\
</div></div><tab\
le style=\x22positi\
on:absolute;top:\
0;left:0;margin:\
0;border:5px sol\
id #000;padding:\
0;width:1px;heig\
ht:1px;\x22 cellpad\
ding=\x220\x22 cellspa\
cing=\x220\x22><tr><td\
></td></tr></tab\
le>';M={position\
:\x22absolute\x22,top:\
0,left:0,margin:\
0,border:0,width\
:\x221px\x22,height:\x221\
px\x22,visibility:\x22\
hidden\x22};for(E i\
n M){F.style[E]=\
M[E]}F.innerHTML\
=K;L.insertBefor\
e(F,L.firstChild\
);H=F.firstChild\
,G=H.firstChild,\
I=H.nextSibling.\
firstChild.first\
Child;this.doesN\
otAddBorder=(G.o\
ffsetTop!==5);th\
is.doesAddBorder\
ForTableAndCells\
=(I.offsetTop===\
5);H.style.overf\
low=\x22hidden\x22,H.s\
tyle.position=\x22r\
elative\x22;this.su\
btractsBorderFor\
OverflowNotVisib\
le=(G.offsetTop=\
==-5);L.style.ma\
rginTop=\x221px\x22;th\
is.doesNotInclud\
eMarginInBodyOff\
set=(L.offsetTop\
===0);L.style.ma\
rginTop=J;L.remo\
veChild(F);this.\
initialized=true\
},bodyOffset:fun\
ction(E){o.offse\
t.initialized||o\
.offset.initiali\
ze();var G=E.off\
setTop,F=E.offse\
tLeft;if(o.offse\
t.doesNotInclude\
MarginInBodyOffs\
et){G+=parseInt(\
o.curCSS(E,\x22marg\
inTop\x22,true),10)\
||0,F+=parseInt(\
o.curCSS(E,\x22marg\
inLeft\x22,true),10\
)||0}return{top:\
G,left:F}}};o.fn\
.extend({positio\
n:function(){var\
 I=0,H=0,F;if(th\
is[0]){var G=thi\
s.offsetParent()\
,J=this.offset()\
,E=/^body|html$/\
i.test(G[0].tagN\
ame)?{top:0,left\
:0}:G.offset();J\
.top-=j(this,\x22ma\
rginTop\x22);J.left\
-=j(this,\x22margin\
Left\x22);E.top+=j(\
G,\x22borderTopWidt\
h\x22);E.left+=j(G,\
\x22borderLeftWidth\
\x22);F={top:J.top-\
E.top,left:J.lef\
t-E.left}}return\
 F},offsetParent\
:function(){var \
E=this[0].offset\
Parent||document\
.body;while(E&&(\
!/^body|html$/i.\
test(E.tagName)&\
&o.css(E,\x22positi\
on\x22)==\x22static\x22))\
{E=E.offsetParen\
t}return o(E)}})\
;o.each([\x22Left\x22,\
\x22Top\x22],function(\
F,E){var G=\x22scro\
ll\x22+E;o.fn[G]=fu\
nction(H){if(!th\
is[0]){return nu\
ll}return H!==g?\
this.each(functi\
on(){this==l||th\
is==document?l.s\
crollTo(!F?H:o(l\
).scrollLeft(),F\
?H:o(l).scrollTo\
p()):this[G]=H})\
:this[0]==l||thi\
s[0]==document?s\
elf[F?\x22pageYOffs\
et\x22:\x22pageXOffset\
\x22]||o.boxModel&&\
document.documen\
tElement[G]||doc\
ument.body[G]:th\
is[0][G]}});o.ea\
ch([\x22Height\x22,\x22Wi\
dth\x22],function(I\
,G){var E=I?\x22Lef\
t\x22:\x22Top\x22,H=I?\x22Ri\
ght\x22:\x22Bottom\x22,F=\
G.toLowerCase();\
o.fn[\x22inner\x22+G]=\
function(){retur\
n this[0]?o.css(\
this[0],F,false,\
\x22padding\x22):null}\
;o.fn[\x22outer\x22+G]\
=function(K){ret\
urn this[0]?o.cs\
s(this[0],F,fals\
e,K?\x22margin\x22:\x22bo\
rder\x22):null};var\
 J=G.toLowerCase\
();o.fn[J]=funct\
ion(K){return th\
is[0]==l?documen\
t.compatMode==\x22C\
SS1Compat\x22&&docu\
ment.documentEle\
ment[\x22client\x22+G]\
||document.body[\
\x22client\x22+G]:this\
[0]==document?Ma\
th.max(document.\
documentElement[\
\x22client\x22+G],docu\
ment.body[\x22scrol\
l\x22+G],document.d\
ocumentElement[\x22\
scroll\x22+G],docum\
ent.body[\x22offset\
\x22+G],document.do\
cumentElement[\x22o\
ffset\x22+G]):K===g\
?(this.length?o.\
css(this[0],J):n\
ull):this.css(J,\
typeof K===\x22stri\
ng\x22?K:K+\x22px\x22)}})\
})();\
"

qt_resource_name = b"\
\x00\x0d\
\x06+\x87\xd3\
\x00j\
\x00q\x00u\x00e\x00r\x00y\x00.\x00m\x00i\x00n\x00.\x00j\x00s\
"

qt_resource_struct = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
\x00\x00\x01\x8eh\xfbB\x18\
"

def qInitResources():
    QtCore.qRegisterResourceData(0x03, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(0x03, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()
