# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from gymnasium.utils.seeding import np_random
import numpy as np


# Used to randomly permute lists in a deterministic manner.
_NP_RANDOM, _ = np_random(seed=0)

OBJECT_BODY_NAME = 'obj'

# Table info, defined in:
#   metaworld/envs/assets_v2/scene/basic_scene.xml
#   <body name='tablelink ... > ... </body>
DEFAULT_TABLE_POS = np.array([0, 0.6, 0])
DEFAULT_TABLE_SIZE = np.array([.7, .4, .46])
TABLE_BODY_NAMES = (
    'tablelink',
    'RetainingWall',
    # metaworld/envs/assets_v2/sawyer_xyz/sawyer_bin_picking.xml
    'bin_start',
    'bin_goal',
    # metaworld/envs/assets_v2/sawyer_xyz/sawyer_button_press_topdown_wall.xml
    'wall',
    # metaworld/envs/assets_v2/sawyer_xyz/sawyer_coffee.xml
    'coffee_machine',
    'coffeemachine',
    'cm_link',
    'cmbutton',
    # metaworld/envs/assets_v2/sawyer_xyz/sawyer_dial.xml
    'dial',
    # metaworld/envs/assets_v2/sawyer_xyz/sawyer_door.xml
    'cabinet',
    # metaworld/envs/assets_v2/sawyer_xyz/sawyer_door_lock.xml
    'door',
    # metaworld/envs/assets_v2/sawyer_xyz/sawyer_hammer.xml, sawyer_peg_insertion_side.xml
    'box',
    # metaworld/envs/assets_v2/sawyer_xyz/sawyer_lever.xml
    'lever',
    # metaworld/envs/assets_v2/sawyer_xyz/sawyer_plate_slide.xml, sawyer_plate_slide_sideway
    'puck_goal',
    # metaworld/envs/assets_v2/sawyer_xyz/sawyer_soccer.xml
    'goal_whole',
    'soccer_goal',
    # metaworld/envs/assets_v2/sawyer_xyz/sawyer_window.xml
    'window',
)

# Object directories must exist in metaworld/envs/mujoco_scanned_objects
OBJECT_NAMES = _NP_RANDOM.permutation([
    '2_of_Jenga_Classic_Game',
    'Nikon_1_AW1_w11275mm_Lens_Silver',
    '3D_Dollhouse_Happy_Brother',
    'Nintendo_Mario_Action_Figure',
    '3D_Dollhouse_Lamp',
    'Nintendo_Yoshi_Action_Figure',
    '3D_Dollhouse_Refrigerator',
    'Object_REmvBDJStub',
    '3D_Dollhouse_Sink',
    'Ocedar_Snap_On_Dust_Pan_And_Brush_1_ct',
    '3D_Dollhouse_Sofa',
    'Olive_Kids_Game_On_Munch_n_Lunch',
    '3D_Dollhouse_Swing',
    'Ortho_Forward_Facing',
    '3D_Dollhouse_TablePurple',
    'Ortho_Forward_Facing_3Q6J2oKJD92',
    '3M_Vinyl_Tape_Green_1_x_36_yd',
    'Ortho_Forward_Facing_CkAW6rL25xH',
    'adizero_5Tool_25',
    'Ortho_Forward_Facing_QCaor9ImJ2G',
    'adiZero_Slide_2_SC',
    'OXO_Cookie_Spatula',
    'Air_Hogs_Wind_Flyers_Set_Airplane_Red',
    'OXO_Soft_Works_Can_Opener_SnapLock',
    'Animal_Planet_Foam_2Headed_Dragon',
    'Pinwheel_Pencil_Case',
    'Aroma_Stainless_Steel_Milk_Frother_2_Cup',
    'Playmates_nickelodeon_teenage_mutant_ninja_turtles_shredder',
    'ASSORTED_VEGETABLE_SET',
    'Pony_C_Clamp_1440',
    'Baby_Elements_Stacking_Cups',
    'Poppin_File_Sorter_Pink',
    'BALANCING_CACTUS',
    'PUNCH_DROP_TjicLPMqLvz',
    'Big_O_Sponges_Assorted_Cellulose_12_pack',
    'Racoon',
    'Black_and_Decker_TR3500SD_2Slice_Toaster',
    'Razer_Kraken_Pro_headset_Full_size_Black',
    'Black_Decker_CM2035B_12Cup_Thermal_Coffeemaker',
    'Razer_Taipan_White_Ambidextrous_Gaming_Mouse',
    'BREAKFAST_MENU',
    'RedBlack_Nintendo_3DSXL',
    'Breyer_Horse_Of_The_Year_2015',
    'Reebok_FS_HI_INT_R12',
    'BUNNY_RATTLE',
    'Reebok_ZIGSTORM',
    'CASTLE_BLOCKS',
    'REEF_BANTU',
    'CHICKEN_RACER',
    'Reef_Star_Cushion_Flipflops_Size_8_Black',
    'Circo_Fish_Toothbrush_Holder_14995988',
    'Remington_TStudio_Hair_Dryer',
    'Cole_Hardware_Hammer_Black',
    'Remington_TStudio_Silk_Ceramic_Hair_Straightener_2_Inch_Floating_Plates',
    'Cole_Hardware_Mini_Honey_Dipper',
    'Retail_Leadership_Summit_tQFCizMt6g0',
    'Cole_Hardware_School_Bell_Solid_Brass_38',
    'Rubbermaid_Large_Drainer',
    'Crayola_Bonus_64_Crayons',
    'SAMe_200',
    'Crosley_Alarm_Clock_Vintage_Metal',
    'SANDWICH_MEAL',
    'DANCING_ALLIGATOR_zoWBjc0jbTs',
    'SAPPHIRE_R7_260X_OC',
    'Dino_3',
    'Schleich_African_Black_Rhino',
    'Dino_4',
    'Schleich_Allosaurus',
    'Dino_5',
    'Schleich_Bald_Eagle',
    'Dixie_10_ounce_Bowls_35_ct',
    'Schleich_Hereford_Bull',
    'Dog',
    'Schleich_Lion_Action_Figure',
    'Elephant',
    'Schleich_S_Bayala_Unicorn_70432',
    'Embark_Lunch_Cooler_Blue',
    'Schleich_Spinosaurus_Action_Figure',
    'F10_TRX_FG_ssscuo9tGxb',
    'Schleich_Therizinosaurus_ln9cruulPqc',
    'FIRE_ENGINE',
    'SCHOOL_BUS',
    'FIRE_TRUCK',
    'Shark',
    'Focus_8643_Lime_Squeezer_10x35x188_Enamelled_Aluminum_Light',
    'Shaxon_100_Molded_Category_6_RJ45RJ45_Shielded_Patch_Cord_White',
    'GARDEN_SWING',
    'Shurtape_Tape_Purple_CP28',
    'GEOMETRIC_SORTING_BOARD',
    'SIT_N_WALK_PUPPY',
    'GIRLS_DECKHAND',
    'SNAIL_MEASURING_TAPE',
    'GoPro_HERO3_Composite_Cable',
    'Sonny_School_Bus',
    'GRANDMOTHER',
    'Sootheze_Cold_Therapy_Elephant',
    'Granimals_20_Wooden_ABC_Blocks_Wagon_g2TinmUGGHI',
    'Granimals_20_Wooden_ABC_Blocks_Wagon_85VdSftGsLi',
    'Granimals_20_Wooden_ABC_Blocks_Wagon',
    'Sootheze_Toasty_Orca',
    'Granimals_20_Wooden_ABC_Blocks_Wagon_g2TinmUGGHI',
    'Granimals_20_Wooden_ABC_Blocks_Wagon_85VdSftGsLi',
    'Granimals_20_Wooden_ABC_Blocks_Wagon',
    'SORTING_TRAIN',
    'Great_Dinos_Triceratops_Toy',
    'SpiderMan_Titan_Hero_12Inch_Action_Figure_5Hnn4mtkFsP',
    'SpiderMan_Titan_Hero_12Inch_Action_Figure_oo1qph4wwiW',
    'Grreat_Choice_Dog_Double_Dish_Plastic_Blue',
    'Squirrel',
    'Guardians_of_the_Galaxy_Galactic_Battlers_Rocket_Raccoon_Figure',
    'Squirt_Strain_Fruit_Basket',
    'HeavyDuty_Flashlight',
    'STACKING_BEAR',
    'HELICOPTER',
    'STACKING_RING',
    'Hilary',
    'Sterilite_Caddy_Blue_Sky_17_58_x_12_58_x_9_14',
    'Imaginext_Castle_Ogre',
    'Teenage_Mutant_Ninja_Turtles_Rahzar_Action_Figure',
    'In_Green_Company_Surface_Saver_Ring_10_Terra_Cotta',
    'Thomas_Friends_Wooden_Railway_Porter_5JzRhMm3a9o',
    'Inositol',
    'Toysmith_Windem_Up_Flippin_Animals_Dog',
    'JA_Henckels_International_Premio_Cutlery_Block_Set_14Piece',
    'Toys_R_Us_Treat_Dispenser_Smart_Puzzle_Foobler',
    'Jansport_School_Backpack_Blue_Streak',
    'Transformers_Age_of_Extinction_Mega_1Step_Bumblebee_Figure',
    'Transformers_Age_of_Extinction_Stomp_and_Chomp_Grimlock_Figure',
    'Jawbone_UP24_Wireless_Activity_Tracker_Pink_Coral_L',
    'Travel_Mate_P_series_Notebook',
    'JBL_Charge_Speaker_portable_wireless_wired_Green',
    'TURBOPROP_AIRPLANE_WITH_PILOT',
    'Kingston_DT4000MR_G2_Management_Ready_USB_64GB',
    'Ubisoft_RockSmith_Real_Tone_Cable_Xbox_360',
    'KITCHEN_SET_CLASSIC_40HwCHfeG0H',
    'UGG_Classic_Tall_Womens_Boots_Grey_7',
    'UGG_Classic_Tall_Womens_Boots_Chestnut_7',
    'Kong_Puppy_Teething_Rubber_Small_Pink',
    'Vtech_Roll_Learn_Turtle',
    'LACING_SHEEP',
    'Vtech_Stack_Sing_Rings_636_Months',
    'Lovable_Huggable_Cuddly_Boutique_Teddy_Bear_Beige',
    'Weisshai_Great_White_Shark',
    'Magnifying_Glassassrt',
    'Weston_No_33_Signature_Sausage_Tonic_12_fl_oz',
    'Marc_Anthony_True_Professional_Oil_of_Morocco_Argan_Oil_Treatment',
    'Marc_Anthony_True_Professional_Strictly_Curls_Curl_Defining_Lotion',
    'Wilton_Pearlized_Sugar_Sprinkles_525_oz_Gold',
    'Marvel_Avengers_Titan_Hero_Series_Doctor_Doom',
    'Wishbone_Pencil_Case',
    'Mens_Santa_Cruz_Thong_in_Tan_r59C69daRPh',
    'W_Lou_z0dkC78niiZ',
    'MINI_EXCAVATOR',
    'Womens_Betty_Chukka_Boot_in_Grey_Jersey_Sequin',
    'Womens_Betty_Chukka_Boot_in_Navy_aEE8OqvMII4',
    'Womens_Betty_Chukka_Boot_in_Navy_Jersey_Sequin_y0SsHk7dKUX',
    'Womens_Betty_Chukka_Boot_in_Salt_Washed_Red_AL2YrOt9CRy',
    'MINI_FIRE_ENGINE',
    'Womens_Hikerfish_Boot_in_Linen_Leather_Sparkle_Suede_imlP8VkwqIH',
    'Womens_Hikerfish_Boot_in_Linen_Leather_Sparkle_Suede_QktIyAkonrU',
    'MINI_ROLLER',
    'Womens_Multi_13',
    'My_First_Rolling_Lion',
    'Xyli_Pure_Xylitol',
    'My_First_Wiggle_Crocodile',
    'YumYum_D3_Liquid',
    'Nescafe_Tasters_Choice_Instant_Coffee_Decaf_House_Blend_Light_7_oz',
    'ZX700_mf9Pc06uL06',
    'Nickelodeon_Teenage_Mutant_Ninja_Turtles_Leonardo',
    'Nickelodeon_Teenage_Mutant_Ninja_Turtles_Michelangelo',
    'Nickelodeon_Teenage_Mutant_Ninja_Turtles_Raphael',
]).tolist()
