import xbmc, xbmcaddon, xbmcgui, xbmcplugin
import os
import re

ADDON= xbmcaddon.Addon(id='plugin.video.filmon')
language= ADDON.getLocalizedString

     
        
def RETURN_COUNTRIES(url):
	dialog = xbmcgui.Dialog()
	countries = [language(30061),language(30062),language(30063),language(30064),language(30065),language(30066),language(30067),language(30068),language(30069),language(30070),language(30071),language(30072),language(30073),language(30074),language(30075),language(30076),language(30077),language(30078),language(30079),language(30080),language(30081),language(30082),language(30083),language(30084),language(30085),language(30086),language(30087),language(30088),language(30089),language(30090),language(30091),language(30092),language(30093),language(30094),language(30095),language(30096),language(30097),language(30098),language(30099),language(30100),language(30101),language(30102),language(30103),language(30104),language(30105),language(30106),language(30107),language(30108),language(30109),language(30110),language(30111),language(30112),language(30113),language(30114),language(30115),language(30116),language(30117),language(30118),language(30119),language(30120),language(30121),language(30122),language(30123),language(30124),language(30125),language(30126),language(30127),language(30128),language(30129),language(30130),language(30131),language(30132),language(30133),language(30134),language(30135),language(30136),language(30137),language(30138),language(30139),language(30140),language(30141),language(30142),language(30143),language(30144),language(30145),language(30146),language(30147),language(30148),language(30149),language(30150),language(30151),language(30152),language(30153),language(30154),language(30155),language(30156),language(30157),language(30158),language(30159),language(30160),language(30161),language(30162),language(30163),language(30164),language(30165),language(30166),language(30167),language(30168),language(30169),language(30170),language(30171),language(30172),language(30173),language(30174),language(30175),language(30176),language(30177),language(30178),language(30179),language(30180),language(30181),language(30182),language(30183),language(30184),language(30185),language(30186),language(30187),language(30188),language(30189),language(30190),language(30191),language(30192),language(30193),language(30194),language(30195),language(30196),language(30197),language(30198),language(30199),language(30200),language(30201),language(30202),language(30203),language(30204),language(30205),language(30206),language(30207),language(30208),language(30209),language(30210),language(30211),language(30212),language(30213),language(30214),language(30215),language(30216),language(30217),language(30218),language(30219),language(30220),language(30221),language(30222),language(30223),language(30224),language(30225),language(30226),language(30227),language(30228),language(30229),language(30230),language(30231),language(30232),language(30233),language(30234),language(30235),language(30236),language(30237),language(30238),language(30239),language(30240),language(30241),language(30242),language(30243),language(30244),language(30245),language(30246),language(30247),language(30248),language(30249),language(30250),language(30251),language(30252),language(30253),language(30254),language(30255),language(30256),language(30257),language(30258),language(30259),language(30260),language(30261),language(30262),language(30263),language(30264),language(30265),language(30266),language(30267),language(30268),language(30269),language(30270),language(30271),language(30272),language(30273),language(30274),language(30275),language(30276),language(30277),language(30278),language(30279),language(30280),language(30281),language(30282),language(30283),language(30284),language(30285),language(30286),language(30287),language(30288),language(30289),language(30290),language(30291),language(30292),language(30293),language(30294),language(30295),language(30296),language(30297),language(30298),language(30299),language(30300),language(30301),language(30302),language(30303),language(30304),language(30305)]
	countriesAbbr=['AF','AL','DZ','AS','AD','AO','AI','AQ','AG','AR','AM','AW','AU','AT','AZ','AX','BS','BH','BD','BB','BY','BE','BZ','BJ','BM','BT','BO','BA','BW','BV','BR','IO','BN','BG','BF','BI','KH','CM','CA','CV','CW','KY','CF','TD','CL','CN','CX','CC','CO','KM','CG','CD','CK','CR','CI','HR','CU','CY','CZ','DK','DJ','DM','DO','EU','EC','EG','SV','GQ','ER','EE','ET','FK','FO','FJ','FI','FR','GF','PF','TF','GA','GM','GE','DE','GH','GI','GR','GL','GD','GP','GU','GT','GN','GW','GY','HT','HM','VA','HN','HK','HU','IS','IN','ID','IR','IQ','IE','IL','IT','JM','JP','JO','KZ','KE','KI','KP','KR','KW','KG','LA','LV','LB','LS','LR','LY','LI','LT','LU','MO','MK','MG','MW','MY','MV','ML','MT','MH','MQ','MR','MU','YT','MX','FM','MD','ME','MC','MN','MS','MA','MZ','MM','NA','NR','NP','NL','AN','NC','NZ','NI','NE','NG','NU','NF','MP','NO','OM','PK','PW','PS','PA','PG','PY','PE','PH','PN','PL','PT','PR','QA','RE','RO','RS','RU','RW','SH','KN','LC','PM','VC','WS','SM','ST','SA','SN','CS','SC','SL','SG','SK','SI','SB','SO','ZA','GS','ES','LK','SD','SR','SJ','SZ','SE','CH','SY','TW','TJ','TZ','TH','TL','TG','TK','TO','TT','TN','TR','TM','TC','TV','UG','UA','AE','GB','UK','US','UM','UY','UZ','VU','VE','VN','VG','VI','WF','EH','YE','ZM','ZW']
	return countriesAbbr[xbmcgui.Dialog().select(language(30306), countries)]
	
	
