global countss, mess, sender_id, activity_id, activity_list, acitivty_idd, temp, socket_in_use, socket_1, socket_2, socket_3, socket_4, socket_5, socket_6, socket_7, socket_8, socket_9, socket_10, socket_11, socket_12, socket_13, socket_14, socket_15, socket_16, socket_17, socket_18, socket_19, socket_20, socket_21, socket_22, socket_23, socket_24, socket_25, socket_26,  socket_list, socket_in_use_list, CONVERSATION_REFERENCES
activity_list = []
activity_id = []
temp = []
countss = 0
mess = ''
sender_id = []
sid = ''
socket_in_use = {}
socket_in_use_list = []
socket_1 = {}
socket_2 = {}
socket_3 = {}
socket_4 = {}
socket_5 = {}
socket_6 = {}
socket_7 = {}
socket_8 = {}
socket_9 = {}
socket_10 = {}
socket_11 = {}
socket_12 = {}
socket_13 = {}
socket_14 = {}
socket_15 = {}
socket_16 = {}
socket_17 = {}
socket_18 = {}
socket_19 = {}
socket_20 = {}
socket_21 = {}
socket_22 = {}
socket_23 = {}
socket_24 = {}
socket_25 = {}
socket_26 = {}
socket_27 = {}
socket_28= {}
socket_29 = {}
socket_30 = {}
socket_31 = {}
socket_32 = {}
socket_33 = {}
socket_34 = {}
socket_35 = {}
socket_36 = {}
socket_37 = {}
socket_38 = {}
socket_39 = {}
socket_40 = {}
socket_41 = {}
socket_42 = {}
socket_43 = {}
socket_44 = {}
socket_45 = {}
socket_46 = {}
socket_47 = {}
socket_48 = {}
socket_49 = {}
socket_50 = {}
socket_51 = {}
socket_52 = {}
socket_53 = {}
socket_54 = {}
socket_55 = {}
socket_56 = {}
socket_57= {}
socket_58 = {}
socket_59 = {}
socket_60 = {}
socket_61 = {}
socket_62 = {}
socket_63 = {}
socket_64 = {}
socket_65 = {}
socket_66 = {}
socket_67 = {}
socket_68 = {}
socket_69 = {}
socket_70 = {}
socket_71 = {}
socket_72 = {}
socket_73 = {}
socket_74 = {}
socket_75 = {}
socket_76 = {}
socket_77 = {}
socket_78 = {}
socket_79 = {}
socket_80= {}
socket_81 = {}
socket_82 = {}
socket_83 = {}
socket_84 = {}
socket_85 = {}
socket_86 = {}
socket_87 = {}
socket_88 = {}
socket_89 = {}
socket_90 = {}
socket_91 = {}
socket_92 = {}
socket_93 = {}
socket_94 = {}
socket_95 = {}
socket_96 = {}
socket_97 = {}
socket_98 = {}
socket_99 = {}
socket_100 = {}
socket_101 = {}
socket_102 = {}
socket_103 = {}
socket_104 = {}
socket_105 = {}
socket_106 = {}
socket_107 = {}
socket_108 = {}
socket_109 = {}
socket_110 = {}
socket_111 = {}
socket_112 = {}
socket_113 = {}
socket_114 = {}
socket_115 = {}
socket_116 = {}
socket_117 = {}
socket_118 = {}
socket_119 = {}
socket_120 = {}
socket_121 = {}
socket_122 = {}
socket_123 = {}
socket_124 = {}
socket_125 = {}
socket_126 = {}
socket_127 = {}
socket_128 = {}
socket_129 = {}
socket_130 = {}
socket_131 = {}
socket_132 = {}
socket_133 = {}
socket_134 = {}
socket_135 = {}
socket_136 = {}
socket_137 = {}
socket_138 = {}
socket_139 = {}
socket_140 = {}
socket_141 = {}
socket_142 = {}
socket_143 = {}
socket_144 = {}
socket_145 = {}
socket_146 = {}
socket_147 = {}
socket_148 = {}
socket_149 = {}
socket_150 = {}
socket_151 = {}
socket_152 = {}
socket_153 = {}
socket_154 = {}
socket_155 = {}
socket_156 = {}
socket_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156]
CONVERSATION_REFERENCES = dict()