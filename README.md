# Veotos transform
Obfuscate text replacing each consonant with next consonant in the ASCII consonants and vowel with next vowel in the ASCII vowels,
plus some diacritical marks over vowels. 

Upper and lower case letters are both supported.

# Example
As there are 5 vowels and 21 consonants 105 different obfuscations exist with this algorithm. Check the iteration parameter.

Notice that each 5 multiple will have the same vowels, and each 21 multiple will have the same consonants (they usually can be read and
sound funny).

Enjoy!

```python
from veotos_transform import find_new_text
crazy_on_you = 'My love is the evening breeze touching your skin'
for iteration in range(0, 106):
    print(find_new_text(crazy_on_you, iteration))
```

|iteration|  Transformed text                                    |
|:------- |  :------------------------------------------------:  |
|000      |**_My love is the evening breeze touching your skin_**|
|001      |   Nz muwi ot vji iwipoph csiibi vuadjoph zuas tlop   |
|002      |   Pb naxo uv wko oxoquqj dtooco waefkuqj baet vmuq   |
|003      |   Qc peyu aw xlu uyurark fvuudu xeiglark ceiv wnar   |
|004      |   Rd qiza ex yma azasesl gwaafa yiohmesl diow xpes   |
|005      |  _Sf robe iy zne ebetitm hxeege zoujnitm foux yqit_  |
|006      |   Tg suci oz bpi icivovn jyiihi buakpovn guay zrov   |
|007      |   Vh tado ub cqo odowuwp kzoojo caelquwp haez bsuw   |
|008      |   Wj vefu ac dru ufuxaxq lbuuku deimraxq jeib ctax   |
|009      |   Xk wiga ed fsa agayeyr mcaala fionseyr kioc dvey   |
|010      |  _Yl xohe if gte ehezizs ndeeme gouptizs loud fwiz_  |
|011      |   Zm yuji og hvi ijibobt pfiini huaqvobt muaf gxob   |
|012      |   Bn zako uh jwo okocucv qgoopo jaerwucv naeg hyuc   |
|013      |   Cp belu aj kxu uludadw rhuuqu keisxadw peih jzad   |
|014      |   Dq cima ek lya amafefx sjaara liotyefx qioj kbef   |
|015      |  _Fr done il mze enegigy tkeese mouvzigy rouk lcig_  |
|016      |   Gs fupi om nbi ipihohz vliiti nuawbohz sual mdoh   |
|017      |   Ht gaqo un pco oqojujb wmoovo paexcujb taem nfuj   |
|018      |   Jv heru ap qdu urukakc xnuuwu qeiydakc vein pgak   |
|019      |   Kw jisa eq rfa asaleld ypaaxa riozfeld wiop qhel   |
|020      |  _Lx kote ir sge etemimf zqeeye soubgimf xouq rjim_  |
|021      | **My luvi os thi ivinong briizi tuachong yuar skon** |
|022      |   Nz mawo ut vjo owopuph csoobo vaedjuph zaes tlup   |
|023      |   Pb nexu av wku uxuqaqj dtuucu weifkaqj beit vmaq   |
|024      |   Qc piya ew xla ayarerk fvaada xioglerk ciov wner   |
|025      |  _Rd qoze ix yme ezesisl gweefe youhmisl douw xpis_  |
|026      |   Sf rubi oy zni ibitotm hxiigi zuajnotm fuax yqot   |
|027      |   Tg saco uz bpo ocovuvn jyooho baekpuvn gaey zruv   |
|028      |   Vh tedu ab cqu uduwawp kzuuju ceilqawp heiz bsaw   |
|029      |   Wj vifa ec dra afaxexq lbaaka diomrexq jiob ctex   |
|030      |  _Xk woge id fse egeyiyr mceele founsiyr kouc dviy_  |
|031      |   Yl xuhi of gti ihizozs ndiimi guaptozs luad fwoz   |
|032      |   Zm yajo ug hvo ojobubt pfoono haeqvubt maef gxub   |
|033      |   Bn zeku ah jwu ukucacv qguupu jeirwacv neig hyac   |
|034      |   Cp bila ej kxa aladedw rhaaqa kiosxedw pioh jzed   |
|035      |  _Dq come ik lye emefifx sjeere loutyifx qouj kbif_  |
|036      |   Fr duni ol mzi inigogy tkiisi muavzogy ruak lcog   |
|037      |   Gs fapo um nbo opohuhz vlooto naewbuhz sael mduh   |
|038      |   Ht gequ an pcu uqujajb wmuuvu peixcajb teim nfaj   |
|039      |   Jv hira ep qda arakekc xnaawa qioydekc vion pgek   |
|040      |  _Kw jose iq rfe eselild ypeexe rouzfild woup qhil_  |
|041      |   Lx kuti or sgi itimomf zqiiyi suabgomf xuaq rjom   |
|042      | **My lavo us tho ovonung broozo taechung yaer skun** |
|043      |   Nz mewu at vju uwupaph csuubu veidjaph zeis tlap   |
|044      |   Pb nixa ev wka axaqeqj dtaaca wiofkeqj biot vmeq   |
|045      |  _Qc poye iw xle eyerirk fveede xouglirk couv wnir_  |
|046      |   Rd quzi ox ymi izisosl gwiifi yuahmosl duaw xpos   |
|047      |   Sf rabo uy zno obotutm hxoogo zaejnutm faex yqut   |
|048      |   Tg secu az bpu ucuvavn jyuuhu beikpavn geiy zrav   |
|049      |   Vh tida eb cqa adawewp kzaaja ciolqewp hioz bsew   |
|050      |  _Wj vofe ic dre efexixq lbeeke doumrixq joub ctix_  |
|051      |   Xk wugi od fsi igiyoyr mciili fuansoyr kuac dvoy   |
|052      |   Yl xaho uf gto ohozuzs ndoomo gaeptuzs laed fwuz   |
|053      |   Zm yeju ag hvu ujubabt pfuunu heiqvabt meif gxab   |
|054      |   Bn zika eh jwa akacecv qgaapa jiorwecv niog hyec   |
|055      |  _Cp bole ij kxe eledidw rheeqe kousxidw pouh jzid_  |
|056      |   Dq cumi ok lyi imifofx sjiiri luatyofx quaj kbof   |
|057      |   Fr dano ul mzo onogugy tkooso maevzugy raek lcug   |
|058      |   Gs fepu am nbu upuhahz vluutu neiwbahz seil mdah   |
|059      |   Ht giqa en pca aqajejb wmaava pioxcejb tiom nfej   |
|060      |  _Jv hore ip qde erekikc xneewe qouydikc voun pgik_  |
|061      |   Kw jusi oq rfi isilold ypiixi ruazfold wuap qhol   |
|062      |   Lx kato ur sgo otomumf zqooyo saebgumf xaeq rjum   |
|063      | **My levu as thu uvunang bruuzu teichang yeir skan** |
|064      |   Nz miwa et vja awapeph csaaba viodjeph zios tlep   |
|065      |  _Pb noxe iv wke exeqiqj dteece woufkiqj bout vmiq_  |
|066      |   Qc puyi ow xli iyirork fviidi xuaglork cuav wnor   |
|067      |   Rd qazo ux ymo ozosusl gwoofo yaehmusl daew xpus   |
|068      |   Sf rebu ay znu ubutatm hxuugu zeijnatm feix yqat   |
|069      |   Tg sica ez bpa acavevn jyaaha biokpevn gioy zrev   |
|070      |  _Vh tode ib cqe edewiwp kzeeje coulqiwp houz bsiw_  |
|071      |   Wj vufi oc dri ifixoxq lbiiki duamroxq juab ctox   |
|072      |   Xk wago ud fso ogoyuyr mcoolo faensuyr kaec dvuy   |
|073      |   Yl xehu af gtu uhuzazs nduumu geiptazs leid fwaz   |
|074      |   Zm yija eg hva ajabebt pfaana hioqvebt miof gxeb   |
|075      |  _Bn zoke ih jwe ekecicv qgeepe jourwicv noug hyic_  |
|076      |   Cp buli oj kxi ilidodw rhiiqi kuasxodw puah jzod   |
|077      |   Dq camo uk lyo omofufx sjooro laetyufx qaej kbuf   |
|078      |   Fr denu al mzu unugagy tkuusu meivzagy reik lcag   |
|079      |   Gs fipa em nba apahehz vlaata niowbehz siol mdeh   |
|080      |  _Ht goqe in pce eqejijb wmeeve pouxcijb toum nfij_  |
|081      |   Jv huri op qdi irikokc xniiwi quaydokc vuan pgok   |
|082      |   Kw jaso uq rfo osoluld ypooxo raezfuld waep qhul   |
|083      |   Lx ketu ar sgu utumamf zquuyu seibgamf xeiq rjam   |
|084      | **My liva es tha avaneng braaza tiocheng yior sken** |
|085      |   _Nz mowe it vje ewepiph cseebe voudjiph zous tlip_   |
|086      |   Pb nuxi ov wki ixiqoqj dtiici wuafkoqj buat vmoq   |
|087      |   Qc payo uw xlo oyorurk fvoodo xaeglurk caev wnur   |
|088      |   Rd qezu ax ymu uzusasl gwuufu yeihmasl deiw xpas   |
|089      |   Sf riba ey zna abatetm hxaaga ziojnetm fiox yqet   |
|090      |  _Tg soce iz bpe ecevivn jyeehe boukpivn gouy zriv_  |
|091      |   Vh tudi ob cqi idiwowp kziiji cualqowp huaz bsow   |
|092      |   Wj vafo uc dro ofoxuxq lbooko daemruxq jaeb ctux   |
|093      |   Xk wegu ad fsu uguyayr mcuulu feinsayr keic dvay   |
|094      |   Yl xiha ef gta ahazezs ndaama gioptezs liod fwez   |
|095      |  _Zm yoje ig hve ejebibt pfeene houqvibt mouf gxib_  |
|096      |   Bn zuki oh jwi ikicocv qgiipi juarwocv nuag hyoc   |
|097      |   Cp balo uj kxo olodudw rhooqo kaesxudw paeh jzud   |
|098      |   Dq cemu ak lyu umufafx sjuuru leityafx qeij kbaf   |
|099      |   Fr dina el mza anagegy tkaasa miovzegy riok lceg   |
|100      |  _Gs fope im nbe epehihz vleete nouwbihz soul mdih_  |
|101      |   Ht guqi on pci iqijojb wmiivi puaxcojb tuam nfoj   |
|102      |   Jv haro up qdo orokukc xnoowo qaeydukc vaen pguk   |
|103      |   Kw jesu aq rfu usulald ypuuxu reizfald weip qhal   |
|104      |   Lx kita er sga atamemf zqaaya siobgemf xioq rjem   |
|105      |**_My love is the evening breeze touching your skin_**|
