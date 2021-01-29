import datetime
import sys
from msvcrt import getwch

from NewLifeUtils.ColorModule import ACC, MCC, FGC
from NewLifeUtils.FileModule import create_files, get_yaml, file_exist, file_apwrite
from NewLifeUtils.StringUtilModule import screate, remove_csi, parse_args

default_colors = """
indianred:
  - 205
  - 92
  - 92
lightcoral:
  - 240
  - 128
  - 128
salmon:
  - 250
  - 128
  - 114
darksalmon:
  - 233
  - 150
  - 122
lightsalmon:
  - 255
  - 160
  - 122
crimson:
  - 220
  - 20
  - 60
red:
  - 255
  - 0
  - 0
firebrick:
  - 178
  - 34
  - 34
darkred:
  - 139
  - 0
  - 0
pink:
  - 255
  - 192
  - 203
lightpink:
  - 255
  - 182
  - 193
hotpink:
  - 255
  - 105
  - 180
deeppink:
  - 255
  - 20
  - 147
mediumvioletred:
  - 199
  - 21
  - 133
palevioletred:
  - 219
  - 112
  - 147
coral:
  - 255
  - 127
  - 80
tomato:
  - 255
  - 99
  - 71
orangered:
  - 255
  - 69
  - 0
darkorange:
  - 255
  - 140
  - 0
orange:
  - 255
  - 165
  - 0
gold:
  - 255
  - 215
  - 0
yellow:
  - 255
  - 255
  - 0
lightyellow:
  - 255
  - 255
  - 224
lemonchiffon:
  - 255
  - 250
  - 205
lightgoldenrodyellow:
  - 250
  - 250
  - 210
papayawhip:
  - 255
  - 239
  - 213
moccasin:
  - 255
  - 228
  - 181
peachpuff:
  - 255
  - 218
  - 185
palegoldenrod:
  - 238
  - 232
  - 170
khaki:
  - 240
  - 230
  - 140
darkkhaki:
  - 189
  - 183
  - 107
lavender:
  - 230
  - 230
  - 250
thistle:
  - 216
  - 191
  - 216
plum:
  - 221
  - 160
  - 221
violet:
  - 238
  - 130
  - 238
orchid:
  - 218
  - 112
  - 214
fuchsia:
  - 255
  - 0
  - 255
magenta:
  - 255
  - 0
  - 255
mediumorchid:
  - 186
  - 85
  - 211
mediumpurple:
  - 147
  - 112
  - 219
blueviolet:
  - 138
  - 43
  - 226
darkviolet:
  - 148
  - 0
  - 211
darkorchid:
  - 153
  - 50
  - 204
darkmagenta:
  - 139
  - 0
  - 139
purple:
  - 128
  - 0
  - 128
indigo:
  - 75
  - 0
  - 130
slateblue:
  - 106
  - 90
  - 205
darkslateblue:
  - 72
  - 61
  - 139
cornsilk:
  - 255
  - 248
  - 220
blanchedalmond:
  - 255
  - 235
  - 205
bisque:
  - 255
  - 228
  - 196
navajowhite:
  - 255
  - 222
  - 173
wheat:
  - 245
  - 222
  - 179
burlywood:
  - 222
  - 184
  - 135
tan:
  - 210
  - 180
  - 140
rosybrown:
  - 188
  - 143
  - 143
sandybrown:
  - 244
  - 164
  - 96
goldenrod:
  - 218
  - 165
  - 32
darkgoldenrod:
  - 184
  - 134
  - 11
peru:
  - 205
  - 133
  - 63
chocolate:
  - 210
  - 105
  - 30
saddlebrown:
  - 139
  - 69
  - 19
sienna:
  - 160
  - 82
  - 45
brown:
  - 165
  - 42
  - 42
maroon:
  - 128
  - 0
  - 0
black:
  - 0
  - 0
  - 0
gray:
  - 128
  - 128
  - 128
silver:
  - 192
  - 192
  - 192
white:
  - 255
  - 255
  - 255
olive:
  - 128
  - 128
  - 0
lime:
  - 0
  - 255
  - 0
green:
  - 0
  - 128
  - 0
aqua:
  - 0
  - 255
  - 255
teal:
  - 0
  - 128
  - 128
blue:
  - 0
  - 0
  - 255
navy:
  - 0
  - 0
  - 128
greenyellow:
  - 173
  - 255
  - 47
chartreuse:
  - 127
  - 255
  - 0
lawngreen:
  - 124
  - 252
  - 0
limegreen:
  - 50
  - 205
  - 50
palegreen:
  - 152
  - 251
  - 152
lightgreen:
  - 144
  - 238
  - 144
mediumspringgreen:
  - 0
  - 250
  - 154
springgreen:
  - 0
  - 255
  - 127
mediumseagreen:
  - 60
  - 179
  - 113
seagreen:
  - 46
  - 139
  - 87
forestgreen:
  - 34
  - 139
  - 34
darkgreen:
  - 0
  - 100
  - 0
yellowgreen:
  - 154
  - 205
  - 50
olivedrab:
  - 107
  - 142
  - 35
darkolivegreen:
  - 85
  - 107
  - 47
mediumaquamarine:
  - 102
  - 205
  - 170
darkseagreen:
  - 143
  - 188
  - 143
lightseagreen:
  - 32
  - 178
  - 170
darkcyan:
  - 0
  - 139
  - 139
cyan:
  - 0
  - 255
  - 255
lightcyan:
  - 224
  - 255
  - 255
paleturquoise:
  - 175
  - 238
  - 238
aquamarine:
  - 127
  - 255
  - 212
turquoise:
  - 64
  - 224
  - 208
mediumturquoise:
  - 72
  - 209
  - 204
darkturquoise:
  - 0
  - 206
  - 209
cadetblue:
  - 95
  - 158
  - 160
steelblue:
  - 70
  - 130
  - 180
lightsteelblue:
  - 176
  - 196
  - 222
powderblue:
  - 176
  - 224
  - 230
lightblue:
  - 173
  - 216
  - 230
skyblue:
  - 135
  - 206
  - 235
lightskyblue:
  - 135
  - 206
  - 250
deepskyblue:
  - 0
  - 191
  - 255
dodgerblue:
  - 30
  - 144
  - 255
cornflowerblue:
  - 100
  - 149
  - 237
mediumslateblue:
  - 123
  - 104
  - 238
royalblue:
  - 65
  - 105
  - 225
mediumblue:
  - 0
  - 0
  - 205
darkblue:
  - 0
  - 0
  - 139
midnightblue:
  - 25
  - 25
  - 112
snow:
  - 255
  - 250
  - 250
honeydew:
  - 240
  - 255
  - 240
mintcream:
  - 245
  - 255
  - 250
azure:
  - 240
  - 255
  - 255
aliceblue:
  - 240
  - 248
  - 255
ghostwhite:
  - 248
  - 248
  - 255
whitesmoke:
  - 245
  - 245
  - 245
seashell:
  - 255
  - 245
  - 238
beige:
  - 245
  - 245
  - 220
oldlace:
  - 253
  - 245
  - 230
floralwhite:
  - 255
  - 250
  - 240
ivory:
  - 255
  - 255
  - 240
antiquewhite:
  - 250
  - 235
  - 215
linen:
  - 250
  - 240
  - 230
lavenderblush:
  - 255
  - 240
  - 245
mistyrose:
  - 255
  - 228
  - 225
gainsboro:
  - 220
  - 220
  - 220
lightgrey:
  - 211
  - 211
  - 211
darkgrey:
  - 169
  - 169
  - 169
grey:
  - 128
  - 128
  - 128
dimgrey:
  - 105
  - 105
  - 105
lightslategrey:
  - 119
  - 136
  - 153
slategrey:
  - 112
  - 128
  - 144
darkslategrey:
  - 47p
  - 79
  - 79
"""

default_colors2 = """
red: '#FF0000'
white: '#FFFFFF'
cyan: '#00FFFF'
silver: '#C0C0C0'
blue: '#0000FF'
gray: '#736F6E'
darkblue: '#0000A0'
black: '#000000'
lightblue: '#ADD8E6'
orange: '#FFA500'
purple: '#8E35EF'
brown: '#A52A2A'
maroon: '#810541'
green: '#00FF00'
yellow: '#FFFF00'
lime: '#00FF00'
magenta: '#FF00FF'
olive: '#FF00FF'
night: '#0C090A'
gunmetal: '#2C3539'
midnight: '#2B1B17'
charcoal: '#34282C'
dark_slate_grey: '#25383C'
oil: '#3B3131'
black_cat: '#413839'
iridium: '#3D3C3A'
black_eel: '#463E3F'
black_cow: '#4C4646'
gray_wolf: '#504A4B'
vampire_gray: '#565051'
gray_dolphin: '#5C5858'
carbon_gray: '#625D5D'
ash_gray: '#666362'
cloudy_gray: '#6D6968'
smokey_gray: '#726E6D'
granite: '#837E7C'
battleship_gray: '#848482'
gray_cloud: '#B6B6B4'
gray_goose: '#D1D0CE'
platinum: '#E5E4E2'
metallic_silver: '#BCC6CC'
blue_gray: '#98AFC7'
light_slate_gray: '#6D7B8D'
slate_gray: '#657383'
jet_gray: '#616D7E'
mist_blue: '#646D7E'
marble_blue: '#566D7E'
slate_blue: '#737CA1'
steel_blue: '#4863A0'
blue_jay: '#2B547E'
dark_slate_blue: '#2B3856'
midnight_blue: '#151B54'
navy_blue: '#000080'
blue_whale: '#342D7E'
lapis_blue: '#15317E'
denim_dark_blue: '#151B8D'
earth_blue: '#0000A0'
cobalt_blue: '#0020C2'
blueberry_blue: '#0041C2'
sapphire_blue: '#2554C7'
blue_eyes: '#1569C7'
royal_blue: '#2B60DE'
blue_orchid: '#1F45FC'
blue_lotus: '#6960EC'
light_slate_blue: '#736AFF'
windows_blue: '#357EC7'
glacial_blue_ice: '#368BC1'
silk_blue: '#488AC7'
blue_ivy: '#3090C7'
blue_koi: '#659EC7'
columbia_blue: '#87AFC7'
baby_blue: '#95B9C7'
light_steel_blue: '#728FCE'
ocean_blue: '#2B65EC'
blue_ribbon: '#306EFF'
blue_dress: '#157DEC'
dodger_blue: '#1589FF'
cornflower_blue: '#6495ED'
sky_blue: '#6698FF'
butterfly_blue: '#38ACEC'
iceberg: '#56A5EC'
crystal_blue: '#5CB3FF'
deep_sky_blue: '#3BB9FF'
denim_blue: '#79BAEC'
light_sky_blue: '#82CAFA'
day_sky_blue: '#82CAFF'
jeans_blue: '#A0CFEC'
blue_angel: '#B7CEEC'
pastel_blue: '#B4CFEC'
sea_blue: '#C2DFFF'
powder_blue: '#C6DEFF'
coral_blue: '#AFDCEC'
light_blue: '#ADDFFF'
robin_egg_blue: '#BDEDFF'
pale_blue_lily: '#CFECEC'
light_cyan: '#E0FFFF'
water: '#EBF4FA'
aliceblue: '#F0F8FF'
azure: '#F0FFFF'
light_slate: '#CCFFFF'
light_aquamarine: '#93FFE8'
electric_blue: '#9AFEFF'
aquamarine: '#7FFFD4'
cyan_or_aqua: '#00FFFF'
tron_blue: '#7DFDFE'
blue_zircon: '#57FEFF'
blue_lagoon: '#8EEBEC'
celeste: '#50EBEC'
blue_diamond: '#4EE2EC'
tiffany_blue: '#81D8D0'
cyan_opaque: '#92C7C7'
blue_hosta: '#77BFC7'
northern_lights_blue: '#78C7C7'
medium_turquoise: '#48CCCD'
turquoise: '#43C6DB'
jellyfish: '#46C7C7'
blue_green: '#7BCCB5'
macaw_blue_green: '#43BFC7'
light_sea_green: '#3EA99F'
dark_turquoise: '#3B9C9C'
sea_turtle_green: '#438D80'
medium_aquamarine: '#348781'
greenish_blue: '#307D7E'
grayish_turquoise: '#5E7D7E'
beetle_green: '#4C787E'
teal: '#008080'
sea_green: '#4E8975'
camouflage_green: '#78866B'
sage_green: '#848b79'
hazel_green: '#617C58'
venom_green: '#728C00'
fern_green: '#667C26'
dark_forest_green: '#254117'
medium_sea_green: '#306754'
medium_forest_green: '#347235'
seaweed_green: '#437C17'
pine_green: '#387C44'
jungle_green: '#347C2C'
shamrock_green: '#347C17'
medium_spring_green: '#348017'
forest_green: '#4E9258'
green_onion: '#6AA121'
spring_green: '#4AA02C'
lime_green: '#41A317'
clover_green: '#3EA055'
green_snake: '#6CBB3C'
alien_green: '#6CC417'
green_apple: '#4CC417'
yellow_green: '#52D017'
kelly_green: '#4CC552'
zombie_green: '#54C571'
frog_green: '#99C68E'
green_peas: '#89C35C'
dollar_bill_green: '#85BB65'
dark_sea_green: '#8BB381'
iguana_green: '#9CB071'
avocado_green: '#B2C248'
pistachio_green: '#9DC209'
salad_green: '#A1C935'
hummingbird_green: '#7FE817'
nebula_green: '#59E817'
stoplight_go_green: '#57E964'
algae_green: '#64E986'
jade_green: '#5EFB6E'
emerald_green: '#5FFB17'
lawn_green: '#87F717'
chartreuse: '#8AFB17'
dragon_green: '#6AFB92'
mint_green: '#98FF98'
green_thumb: '#B5EAAA'
light_jade: '#C3FDB8'
tea_green: '#CCFB5D'
green_yellow: '#B1FB17'
slime_green: '#BCE954'
goldenrod: '#EDDA74'
harvest_gold: '#EDE275'
sun_yellow: '#FFE87C'
corn_yellow: '#FFF380'
parchment: '#FFFFC2'
cream: '#FFFFCC'
lemon_chiffon: '#FFF8C6'
cornsilk: '#FFF8DC'
beige: '#F5F5DC'
blonde: '#FBF6D9'
antiquewhite: '#FAEBD7'
champagne: '#F7E7CE'
blanchedalmond: '#FFEBCD'
vanilla: '#F3E5AB'
tan_brown: '#ECE5B6'
peach: '#FFE5B4'
mustard: '#FFDB58'
rubber_ducky_yellow: '#FFD801'
bright_gold: '#FDD017'
golden_brown: '#EAC117'
macaroni_and_cheese: '#F2BB66'
saffron: '#FBB917'
beer: '#FBB117'
cantaloupe: '#FFA62F'
bee_yellow: '#E9AB17'
brown_sugar: '#E2A76F'
burlywood: '#DEB887'
deep_peach: '#FFCBA4'
ginger_brown: '#C9BE62'
school_bus_yellow: '#E8A317'
sandy_brown: '#EE9A4D'
fall_leaf_brown: '#C8B560'
orange_gold: '#D4A017'
sand: '#C2B280'
cookie_brown: '#C7A317'
caramel: '#C68E17'
brass: '#B5A642'
khaki: '#ADA96E'
camel_brown: '#C19A6B'
bronze: '#CD7F32'
tiger_orange: '#C88141'
cinnamon: '#C58917'
bullet_shell: '#AF9B60'
dark_goldenrod: '#AF7817'
copper: '#B87333'
wood: '#966F33'
oak_brown: '#806517'
moccasin: '#827839'
army_brown: '#827B60'
sandstone: '#786D5F'
mocha: '#493D26'
taupe: '#483C32'
coffee: '#6F4E37'
brown_bear: '#835C3B'
red_dirt: '#7F5217'
sepia: '#7F462C'
orange_salmon: '#C47451'
rust: '#C36241'
red_fox: '#C35817'
chocolate: '#C85A17'
sedona: '#CC6600'
papaya_orange: '#E56717'
halloween_orange: '#E66C2C'
pumpkin_orange: '#F87217'
construction_cone_ora: '#F87431'
sunrise_orange: '#E67451'
mango_orange: '#FF8040'
dark_orange: '#F88017'
coral: '#FF7F50'
basket_ball_orange: '#F88158'
light_salmon: '#F9966B'
tangerine: '#E78A61'
dark_salmon: '#E18B6B'
light_coral: '#E77471'
bean_red: '#F75D59'
valentine_red: '#E55451'
shocking_orange: '#E55B3C'
scarlet: '#FF2400'
ruby_red: '#F62217'
ferrari_red: '#F70D1A'
fire_engine_red: '#F62817'
lava_red: '#E42217'
love_red: '#E41B17'
grapefruit: '#DC381F'
chestnut_red: '#C34A2C'
cherry_red: '#C24641'
mahogany: '#C04000'
chilli_pepper: '#C11B17'
cranberry: '#9F000F'
red_wine: '#990012'
burgundy: '#8C001A'
chestnut: '#954535'
blood_red: '#7E3517'
sienna: '#8A4117'
sangria: '#7E3817'
firebrick: '#800517'
plum_pie: '#7D0541'
velvet_maroon: '#7E354D'
plum_velvet: '#7D0552'
rosy_finch: '#7F4E52'
puce: '#7F5A58'
dull_purple: '#7F525D'
rosy_brown: '#B38481'
khaki_rose: '#C5908E'
pink_bow: '#C48189'
lipstick_pink: '#C48793'
rose: '#E8ADAA'
rose_gold: '#ECC5C0'
desert_sand: '#EDC9AF'
pig_pink: '#FDD7E4'
cotton_candy: '#FCDFFF'
pink_bubble_gum: '#FFDFDD'
misty_rose: '#FBBBB9'
pink: '#FAAFBE'
light_pink: '#FAAFBA'
flamingo_pink: '#F9A7B0'
pink_rose: '#E7A1B0'
pink_daisy: '#E799A3'
cadillac_pink: '#E38AAE'
carnation_pink: '#F778A1'
blush_red: '#E56E94'
hot_pink: '#F660AB'
watermelon_pink: '#FC6C85'
violet_red: '#F6358A'
deep_pink: '#F52887'
pink_cupcake: '#E45E9D'
pink_lemonade: '#E4287C'
neon_pink: '#F535AA'
dimorphotheca_magenta: '#E3319D'
bright_neon_pink: '#F433FF'
pale_violet_red: '#D16587'
tulip_pink: '#C25A7C'
medium_violet_red: '#CA226B'
rogue_pink: '#C12869'
burnt_pink: '#C12267'
bashful_pink: '#C25283'
dark_carnation_pink: '#C12283'
plum: '#B93B8F'
viola_purple: '#7E587E'
purple_iris: '#571B7E'
plum_purple: '#583759'
indigo: '#4B0082'
purple_monster: '#461B7E'
purple_haze: '#4E387E'
eggplant: '#614051'
grape: '#5E5A80'
purple_jam: '#6A287E'
dark_orchid: '#7D1B7E'
purple_flower: '#A74AC7'
medium_orchid: '#B048B5'
purple_amethyst: '#6C2DC7'
dark_violet: '#842DCE'
violet: '#8D38C9'
purple_sage_bush: '#7A5DC7'
lovely_purple: '#7F38EC'
aztech_purple: '#893BFF'
medium_purple: '#8467D7'
jasmine_purple: '#A23BEC'
purple_daffodil: '#B041FF'
tyrian_purple: '#C45AEC'
crocus_purple: '#9172EC'
purple_mimosa: '#9E7BFF'
heliotrope_purple: '#D462FF'
crimson: '#E238EC'
purple_dragon: '#C38EC7'
lilac: '#C8A2C8'
blush_pink: '#E6A9EC'
mauve: '#E0B0FF'
wisteria_purple: '#C6AEC7'
blossom_pink: '#F9B7FF'
thistle: '#D2B9D3'
periwinkle: '#E9CFEC'
lavender_pinocchio: '#EBDDE2'
lavender_blue: '#E3E4FA'
pearl: '#FDEEF4'
seashell: '#FFF5EE'
milk_white: '#FEFCFF'
"""

default_config = """
log_pattern: "{greenyellow}[{time}] {lightgreen}{tag}{snow} : {mediumspringgreen}{message}"
wrn_pattern: "{darkorange}[{time}] {orange}{tag}{snow} : {gold}{message}"
err_pattern: "{crimson}[{time}] {red}{tag}{snow} : {firebrick}{message}"
tip_pattern: "{fuchsia}[{time}] {magenta}{tag}{snow} : {mediumorchid}{message}"
rea_pattern: "{cyan}[{time}] {lightcyan}{tag}{snow} : {paleturquoise}{message} > {mediumslateblue}[{readed}]"

log_default_tag: "Log"
wrn_default_tag: "Warn"
err_default_tag: "Error"
tip_default_tag: "Tip"
rea_default_tag: "Read"

date_format: "%d-%m-%Y"
time_format: "%H:%M:%S"

tag_length: 10

colormap: 1

file_log: true
logtime: "%d-%m-%Y_%H-%M-%S"
logname: "log_{time}"
"""

create_files("logger_colors", "color_schema.yml", "logger", default_colors)
create_files("logger_colors2", "color_schema_2.yml", "logger", default_colors2)
create_files("logger_lang", "config.yml", "logger", default_config)
settings_config = get_yaml("logger_lang", default_config)

log_pattern = settings_config["log_pattern"]
wrn_pattern = settings_config["wrn_pattern"]
err_pattern = settings_config["err_pattern"]
tip_pattern = settings_config["tip_pattern"]
rea_pattern = settings_config["rea_pattern"]
log_default_tag = settings_config["log_default_tag"]
wrn_default_tag = settings_config["wrn_default_tag"]
err_default_tag = settings_config["err_default_tag"]
tip_default_tag = settings_config["tip_default_tag"]
rea_default_tag = settings_config["rea_default_tag"]
date_format = settings_config["date_format"]
time_format = settings_config["time_format"]
tag_length = settings_config["tag_length"]
enable_file_fog = settings_config["file_log"]
logtime = settings_config["logtime"]
logname = settings_config["logname"]
colormap_type = settings_config["colormap"]
colormap = {}


def set_settings(
    new_log_pattern=log_pattern,
    new_wrn_pattern=wrn_pattern,
    new_err_pattern=err_pattern,
    new_tip_pattern=tip_pattern,
    new_rea_pattern=rea_pattern,
    new_log_default_tag=log_default_tag,
    new_wrn_default_tag=wrn_default_tag,
    new_err_default_tag=err_default_tag,
    new_tip_default_tag=tip_default_tag,
    new_rea_default_tag=rea_default_tag,
    new_date_format=date_format,
    new_time_format=time_format,
    new_tag_length=tag_length,
    new_enable_file_fog=enable_file_fog,
    new_logtime=logtime,
    new_logname=logname,
):
    global log_pattern
    global wrn_pattern
    global err_pattern
    global tip_pattern
    global rea_pattern
    global log_default_tag
    global wrn_default_tag
    global err_default_tag
    global tip_default_tag
    global rea_default_tag
    global date_format
    global time_format
    global tag_length
    global enable_file_fog
    global logtime
    global logname

    log_pattern = new_log_pattern
    wrn_pattern = new_wrn_pattern
    err_pattern = new_err_pattern
    tip_pattern = new_tip_pattern
    rea_pattern = new_rea_pattern
    log_default_tag = new_log_default_tag
    wrn_default_tag = new_wrn_default_tag
    err_default_tag = new_err_default_tag
    tip_default_tag = new_tip_default_tag
    rea_default_tag = new_rea_default_tag
    date_format = new_date_format
    time_format = new_time_format
    tag_length = new_tag_length
    enable_file_fog = new_enable_file_fog
    logtime = new_logtime
    logname = new_logname


if colormap_type == 2:
    settings_color2 = get_yaml("logger_colors2", default_colors2)
    for color in settings_color2:
        h = settings_color2[color].lstrip("#")
        colormap[color] = tuple(int(h[i : i + 2], 16) for i in (0, 2, 4))
else:
    settings_color1 = get_yaml("logger_colors", default_colors)
    for color in settings_color1:
        colormap[color] = ACC.customrgb(*settings_color1[color])


def tag_check(tag, default):
    if tag == "":
        return screate(default, tag_length)
    else:
        return screate(tag, tag_length)


def to_format(pattern, args):
    now = datetime.datetime.now()

    return (
        pattern.format(
            **args,
            **colormap,
            date=now.strftime(date_format),
            time=now.strftime(time_format),
        )
        + ACC.RESET
    )


def out(text):
    now = datetime.datetime.now()
    if enable_file_fog:
        if not file_exist("log"):
            create_files(
                "log", f"{logname.format(time=now.strftime(logtime))}.log", "logs"
            )

        file_apwrite("log", remove_csi(text))

    print(text)


log = lambda message, tag="": out(
    to_format(
        log_pattern,
        {"message": message, "tag": tag_check(tag, log_default_tag)},
    )
)
wrn = lambda message, tag="": out(
    to_format(
        wrn_pattern,
        {"message": message, "tag": tag_check(tag, wrn_default_tag)},
    )
)
err = lambda message, tag="": out(
    to_format(
        err_pattern,
        {"message": message, "tag": tag_check(tag, err_default_tag)},
    )
)
tip = lambda message, tag="": out(
    to_format(
        tip_pattern,
        {"message": message, "tag": tag_check(tag, tip_default_tag)},
    )
)
cstm = lambda pattern, args: out(to_format(pattern, args))

rea = lambda message, tag="", completion=None: read(message, tag, completion)


def read(message, tag="", completion=None):
    if completion is None:
        completion = {}
    selector = 0

    current_text = ""

    def complete(readed, completes):
        nonlocal selector
        nonlocal current_text
        # print(f'{ACC.CLEARSCREEN}')
        if current_text == "":
            current_text = readed
        work_parsed = parse_args(readed)["split"]
        if readed != "":
            if readed[-1] == " ":
                work_parsed.append("")

        keys = completes.keys()

        # print(readed)
        # print(current_text)
        aval = []
        if readed == "":
            aval = list(completes.keys())
        else:
            for argnum, arg in enumerate(work_parsed, start=1):
                aval = []
                next_sel = False
                for key in keys:
                    # print(f'{FGC.GREEN}arg: {arg}, key: {key}, result: {key.startswith(arg)}')
                    sys.stdout.flush()
                    if key.startswith(arg):
                        aval.append(key)
                        next_sel = True
                        try:
                            completes[key]
                        except KeyError:
                            pass  # no completion next
                            keys = {}
                        else:
                            sys.stdout.flush()
                            keys = completes[key]
                            next_sel = True

                if next_sel:
                    selector += 1
                    selector %= len(aval)
                if len(aval) == 1:
                    work_parsed[argnum - 1] = aval[0]
                elif len(aval) > 0:
                    work_parsed[argnum - 1] = aval[selector]
                    # print(f'{FGC.MAGENTA}com: {aval}, next: {keys}, CURRENT: {selector} - {aval[selector]}')

        # print(ACC.RESET)

        return " ".join(work_parsed), aval

    def smart_input(text="", completes=None, end="\n"):
        readed = ""
        print(text + MCC.save_cursor, end="")
        sys.stdout.flush()
        while True:
            key = getwch()
            if ord(key) == 224:
                pass
            elif ord(key) == 0:
                pass
            else:
                if ord(key) == 8:
                    readed = readed[:-1]
                    print(MCC.load_cursor + MCC.erase_nxt_line + readed, end="")

                elif ord(key) == 13:
                    break
                elif ord(key) == 9:
                    readed, aval = complete(readed, completes)
                    if len(aval) > 0:
                        avalr = ", ".join(aval)
                    else:
                        avalr = "no suggestion"
                    avaltext = f"{FGC.GRAY} ({avalr}) {ACC.RESET}"
                    print(
                        MCC.load_cursor
                        + MCC.erase_nxt_line
                        + readed
                        + avaltext
                        + MCC.left(len(remove_csi(avaltext))),
                        end="",
                    )
                else:
                    readed += key
                    print(MCC.load_cursor + MCC.erase_nxt_line + readed, end="")
            sys.stdout.flush()
        print(end)
        return readed

    if message[-1] not in [" ", ">", ":"]:
        message += ": "
    print(
        f"{ACC.bcustomrgb(0, 43, 112)}{ACC.customrgb(235, 54, 30)}{message}",
        end="",
    )
    readed = input()

    out(
        MCC.up()
        + ACC.RESET
        + MCC.ERASE_ALL_LINE
        + to_format(
            rea_pattern,
            {
                "message": message,
                "tag": tag_check(tag, rea_default_tag),
                "readed": readed,
            },
        )
    )
    return readed
