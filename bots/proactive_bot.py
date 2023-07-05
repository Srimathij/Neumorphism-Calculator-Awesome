# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from itertools import count
from socket import SocketIO
from typing import Dict
from typing import Dict
import os

from pygame import USEREVENT_DROPFILE
# from app import CONVERSATION_REFERENCES
import config
import socketio
import requests
import json
import time
from botbuilder.core import ActivityHandler, TurnContext, MessageFactory, CardFactory
from botbuilder.schema import ChannelAccount, ConversationReference, Activity, ActivityTypes, Attachment
from sockio import *
import asyncio
from botbuilder.core import ActivityHandler, TurnContext
from botbuilder.schema import ChannelAccount, ConversationReference, Activity
from settings import *
import botbuilder.core.teams as Teams
global user_id, user_flag_5005,user_flag_5004, sock_flag
# user_id = []
user_flag_5005 = {}
user_flag_5004 = {}
sock_flag = {}
# global sio,tsio,usio,vsio,wsio 
from settings import *
CARDS = [
    "resources/RestaurantCard.json",
]

class ProactiveBot(ActivityHandler):
    def __init__(self, conversation_references: Dict[str, ConversationReference]):
        self.conversation_references = conversation_references
        print("THIS IS LOADED CONVERSATION REFERENCES ", self.conversation_references)
        # self.activity_id = activity_id

    async def on_conversation_update_activity(self, turn_context: TurnContext):
        self._add_conversation_reference(turn_context.activity)
        return await super().on_conversation_update_activity(turn_context)

    async def on_members_added_activity(
        self, members_added: [ChannelAccount], turn_context: TurnContext
    ):
        for member in members_added:
            print("THIS IS THE LIST OF MEMBERS ", member)
            print("THIS IS RECIPIENT ID ", turn_context.activity.recipient.id)
            if member.id != turn_context.activity.recipient.id:
                await turn_context.send_activity(
                    "Diva is your new virtual colleague. Designed to support and engage on a real-time basis to answer your queries and even provide solutions related to HR policies instantly round the clock. These apart, eDiva can also support you to raise a service request, go to important links, facilitate transactions with TalentX etc., Go ahead and experience it yourself!"
                )
    async def on_message_activity(self, turn_context: TurnContext):
        global user_flag_5004, sock_flag, user_flag_5005, socket_1, socket_2, socket_3, socket_4, socket_5, socket_6, socket_7, socket_8, socket_9, socket_10, socket_11, socket_12, socket_13, socket_14, socket_15, socket_16, socket_17, socket_18, socket_19, socket_20, socket_21, socket_22, socket_23, socket_24, socket_25, socket_26,socket_27, socket_28, socket_29, socket_30, socket_31, socket_32, socket_33, socket_34, socket_35, socket_36, socket_37, socket_38, socket_39, socket_40, socket_41, socket_42, socket_43, socket_44, socket_45, socket_46, socket_47, socket_48, socket_49, socket_50, socket_51, socket_52,socket_53, socket_54, socket_55, socket_56, socket_57, socket_58, socket_59, socket_60, socket_61, socket_62, socket_63, socket_64, socket_65, socket_66, socket_67, socket_68, socket_69, socket_70, socket_71, socket_72, socket_73, socket_74, socket_75, socket_76, socket_77, socket_78,socket_79, socket_80, socket_81, socket_82, socket_83, socket_84, socket_85, socket_86, socket_87, socket_88, socket_89, socket_90, socket_91, socket_92, socket_93, socket_94, socket_95, socket_96, socket_97, socket_98, socket_99, socket_100, socket_101, socket_102, socket_103, socket_104, socket_105, socket_106, socket_107, socket_108, socket_109, socket_110, socket_111, socket_112, socket_113, socket_114, socket_115, socket_116, socket_117, socket_118, socket_119, socket_120, socket_121, socket_122, socket_123, socket_124, socket_125, socket_126, socket_127, socket_128, socket_129, socket_130,socket_131, socket_132, socket_133, socket_134, socket_135, socket_136, socket_137, socket_138, socket_139, socket_140, socket_141, socket_142, socket_143, socket_144, socket_145, socket_146, socket_147, socket_148, socket_149, socket_150, socket_151, socket_152, socket_153, socket_154, socket_155, socket_156
        await turn_context.send_activities([
            Activity(
                type=ActivityTypes.typing
            ),
            Activity(
                type="delay",
                value=2000
            )
        ])
        
        user_id = str(turn_context.get_conversation_reference(turn_context.activity).user.id)
        idss = user_id.replace('-','')
        print("THIS IS THE CURRENT ID,", user_id)
        print("THIS IS THE SOCKET_IN_USE LIST   :::: ", socket_in_use.keys())
        await self.left_over_sock()
        await self.empty_sock_check(user_id)
        print("THIS IS SOCKET_1 ", socket_1)
        print("THIS IS SOCKET_2 ", socket_2)
        print("THIS IS SOCKET_3 ", socket_3)
        print("THIS IS SOCKET_4 ", socket_4)
        print("THIS IS SOCKET_5 ", socket_5)
        print("THIS IS SOCKET_6 ", socket_6)
        print("THIS IS SOCKET_7 ", socket_7)
        print("THIS IS SOCKET_8 ", socket_8)
        print("THIS IS SOCKET_9 ", socket_9)
        print("THIS IS SOCKET_10 ", socket_10)
        print("THIS IS SOCKET_11 ", socket_11)
        print("THIS IS SOCKET_12 ", socket_12)
        print("THIS IS SOCKET_13 ", socket_13)
        print("THIS IS SOCKET_14 ", socket_14)
        print("THIS IS SOCKET_15 ", socket_15)
        print("THIS IS SOCKET_16 ", socket_16)
        print("THIS IS SOCKET_17 ", socket_17)
        print("THIS IS SOCKET_18 ", socket_18)
        print("THIS IS SOCKET_19 ", socket_19)
        print("THIS IS SOCKET_20 ", socket_20)
        print("THIS IS SOCKET_21 ", socket_21)
        print("THIS IS SOCKET_22 ", socket_22)
        print("THIS IS SOCKET_23 ", socket_23)
        print("THIS IS SOCKET_24 ", socket_24)
        print("THIS IS SOCKET_25 ", socket_25)
        print("THIS IS SOCKET_26 ", socket_26)
        print("THIS IS SOCKET_27 ", socket_27)
        print("THIS IS SOCKET_28 ", socket_28)
        print("THIS IS SOCKET_29 ", socket_29)
        print("THIS IS SOCKET_30 ", socket_30)
        print("THIS IS SOCKET_31 ", socket_31)
        print("THIS IS SOCKET_32 ", socket_32)
        print("THIS IS SOCKET_33 ", socket_33)
        print("THIS IS SOCKET_34 ", socket_34)
        print("THIS IS SOCKET_35 ", socket_35)
        print("THIS IS SOCKET_36 ", socket_36)
        print("THIS IS SOCKET_37 ", socket_37)
        print("THIS IS SOCKET_38 ", socket_38)
        print("THIS IS SOCKET_39 ", socket_39)
        print("THIS IS SOCKET_40 ", socket_40)
        print("THIS IS SOCKET_41 ", socket_41)
        print("THIS IS SOCKET_42 ", socket_42)
        print("THIS IS SOCKET_43 ", socket_43)
        print("THIS IS SOCKET_44 ", socket_44)
        print("THIS IS SOCKET_45 ", socket_45)
        print("THIS IS SOCKET_46 ", socket_46)
        print("THIS IS SOCKET_47 ", socket_47)
        print("THIS IS SOCKET_48 ", socket_48)
        print("THIS IS SOCKET_49 ", socket_49)
        print("THIS IS SOCKET_50 ", socket_50)
        print("THIS IS SOCKET_51 ", socket_51)
        print("THIS IS SOCKET_52 ", socket_52)
        print("THIS IS SOCKET_53 ", socket_53)
        print("THIS IS SOCKET_54 ", socket_54)
        print("THIS IS SOCKET_55 ", socket_55)
        print("THIS IS SOCKET_56 ", socket_56)
        print("THIS IS SOCKET_57 ", socket_57)
        print("THIS IS SOCKET_58 ", socket_58)
        print("THIS IS SOCKET_59 ", socket_59)
        print("THIS IS SOCKET_60 ", socket_60)
        print("THIS IS SOCKET_61 ", socket_61)
        print("THIS IS SOCKET_62 ", socket_62)
        print("THIS IS SOCKET_63 ", socket_63)
        print("THIS IS SOCKET_64 ", socket_64)
        print("THIS IS SOCKET_65 ", socket_65)
        print("THIS IS SOCKET_66 ", socket_66)
        print("THIS IS SOCKET_67 ", socket_67)
        print("THIS IS SOCKET_68 ", socket_68)
        print("THIS IS SOCKET_69 ", socket_69)
        print("THIS IS SOCKET_70 ", socket_70)
        print("THIS IS SOCKET_71 ", socket_71)
        print("THIS IS SOCKET_72 ", socket_72)
        print("THIS IS SOCKET_73 ", socket_73)
        print("THIS IS SOCKET_74 ", socket_74)
        print("THIS IS SOCKET_75 ", socket_75)
        print("THIS IS SOCKET_76 ", socket_76)
        print("THIS IS SOCKET_77 ", socket_77)
        print("THIS IS SOCKET_78 ", socket_78)
        print("THIS IS SOCKET_79 ", socket_79)
        print("THIS IS SOCKET_80 ", socket_80)
        print("THIS IS SOCKET_81 ", socket_81)
        print("THIS IS SOCKET_82 ", socket_82)
        print("THIS IS SOCKET_83 ", socket_83)
        print("THIS IS SOCKET_84 ", socket_84)
        print("THIS IS SOCKET_85 ", socket_85)
        print("THIS IS SOCKET_86 ", socket_86)
        print("THIS IS SOCKET_87 ", socket_87)
        print("THIS IS SOCKET_88 ", socket_88)
        print("THIS IS SOCKET_89 ", socket_89)
        print("THIS IS SOCKET_90 ", socket_90)
        print("THIS IS SOCKET_91 ", socket_91)
        print("THIS IS SOCKET_92 ", socket_92)
        print("THIS IS SOCKET_93 ", socket_93)
        print("THIS IS SOCKET_94 ", socket_94)
        print("THIS IS SOCKET_95 ", socket_95)
        print("THIS IS SOCKET_96 ", socket_96)
        print("THIS IS SOCKET_97 ", socket_97)
        print("THIS IS SOCKET_98 ", socket_98)
        print("THIS IS SOCKET_99 ", socket_99)
        print("THIS IS SOCKET_100 ", socket_100)
        print("THIS IS SOCKET_101 ", socket_101)
        print("THIS IS SOCKET_102 ", socket_102)
        print("THIS IS SOCKET_103 ", socket_103)
        print("THIS IS SOCKET_104 ", socket_104)
        print("THIS IS SOCKET_105 ", socket_105)
        print("THIS IS SOCKET_106 ", socket_106)
        print("THIS IS SOCKET_107 ", socket_107)
        print("THIS IS SOCKET_108 ", socket_108)
        print("THIS IS SOCKET_109 ", socket_109)
        print("THIS IS SOCKET_110 ", socket_110)
        print("THIS IS SOCKET_111 ", socket_111)
        print("THIS IS SOCKET_112 ", socket_112)
        print("THIS IS SOCKET_113 ", socket_113)
        print("THIS IS SOCKET_114 ", socket_114)
        print("THIS IS SOCKET_115 ", socket_115)
        print("THIS IS SOCKET_116 ", socket_116)
        print("THIS IS SOCKET_117 ", socket_117)
        print("THIS IS SOCKET_118 ", socket_118)
        print("THIS IS SOCKET_119 ", socket_119)
        print("THIS IS SOCKET_120 ", socket_120)
        print("THIS IS SOCKET_121 ", socket_121)
        print("THIS IS SOCKET_122 ", socket_122)
        print("THIS IS SOCKET_123 ", socket_123)
        print("THIS IS SOCKET_124 ", socket_124)
        print("THIS IS SOCKET_125 ", socket_125)
        print("THIS IS SOCKET_126 ", socket_126)
        print("THIS IS SOCKET_127 ", socket_127)
        print("THIS IS SOCKET_128 ", socket_128)
        print("THIS IS SOCKET_129 ", socket_129)
        print("THIS IS SOCKET_130 ", socket_130)
        print("THIS IS SOCKET_131 ", socket_131)
        print("THIS IS SOCKET_132 ", socket_132)
        print("THIS IS SOCKET_133 ", socket_133)
        print("THIS IS SOCKET_134 ", socket_134)
        print("THIS IS SOCKET_135 ", socket_135)
        print("THIS IS SOCKET_136 ", socket_136)
        print("THIS IS SOCKET_137 ", socket_137)
        print("THIS IS SOCKET_138 ", socket_138)
        print("THIS IS SOCKET_139 ", socket_139)
        print("THIS IS SOCKET_140 ", socket_140)
        print("THIS IS SOCKET_141 ", socket_141)
        print("THIS IS SOCKET_142 ", socket_142)
        print("THIS IS SOCKET_143 ", socket_143)
        print("THIS IS SOCKET_144 ", socket_144)
        print("THIS IS SOCKET_145 ", socket_145)
        print("THIS IS SOCKET_146 ", socket_146)
        print("THIS IS SOCKET_147 ", socket_147)
        print("THIS IS SOCKET_148 ", socket_148)
        print("THIS IS SOCKET_149 ", socket_149)
        print("THIS IS SOCKET_150 ", socket_150)
        print("THIS IS SOCKET_151 ", socket_151)
        print("THIS IS SOCKET_152 ", socket_152)
        print("THIS IS SOCKET_153 ", socket_153)
        print("THIS IS SOCKET_154 ", socket_154)
        print("THIS IS SOCKET_155 ", socket_155)
        print("THIS IS SOCKET_156 ", socket_156)
        print("THIS IS CURRENT TIME ",time.time())
        print("I AM SENDING THIS MESSAGE ", turn_context.activity.text, "AND THIS IS THE SENDER ID ", id)
        text = str(turn_context.activity.text)
        a = await Teams.TeamsInfo.get_members(turn_context)
        # act_id = turn_context.activity.id
        for i in a:
            unique_email = i.email
            print("THIS IS TEAMS INFRO:::",i.email)
        unique_email = str(unique_email)
        print("THIS IS UNIQUE NAME ", unique_email)
        # q = turn_context.get_mentions
        text = turn_context.activity.text.lower()
        # if 'hey' in text:
        #     tt = self.activity_id[-1]
        #     self.activity_id.append(tt)
        # id = str(turn_context.get_conversation_reference(turn_context.activity).user.id)
        # id = id.replace('-','')
        print("THIS IS THE SENDER ID ", user_id)
        if id not in sock_flag.keys():
            print("THIS IS INITIATING SOCK TO 5005")
            sock_flag[user_id] = '5005'
        # user_flag_5005[id] = time.time()
        # print("THIS IS SOCKET_IN_USE ", socket_in_use, " and this is the act_id ", act_id)
        # else:
        #     exec('self.socket_use_'+socket_in_use[user_id]+'('+user_id+')')

        try:
            if socket_in_use[user_id] == '1':
                print("THIS IS INSIDE SOCKET 1")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        print("THIS IS INSIDE IF")
                        if time.time() - user_flag_5005[user_id] >1000:
                            user_flag_5005[user_id] = time.time()
                            # await sio.sleep(10)
                            await aio.emit('session_request', {'session_id':idss})
                            await aio.emit('user_uttered',{'session_id':idss,
                                'message' : text,
                                'metadata' : {'unique_name': unique_email}
                            })
                        else: 
                            user_flag_5005[user_id] = time.time()
                            # await sio.sleep(10)
                            await aio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email}
                            })
                        print('THIS IS END OF IF')
                    else:
                        print("THIS IS INSIDE ELSE")
                        # await sio.sleep(10)
                        await aio.emit('session_request', {'session_id':idss})
                        await aio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email}
                        })
                        print("THIS IS END OF ELSE")
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared. 
                        user_flag_5005[user_id] = time.time()
              
            elif socket_in_use[user_id] == '2':
                print("THIS IS INSIDE SOCKET 2")
               
                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': #and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): # To check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >1000:
                            user_flag_5005[user_id] = time.time()
                            await bio.emit('session_request', {'session_id':idss})
                            await bio.emit('user_uttered',{'session_id':idss,
                                'message' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else: 
                            user_flag_5005[user_id] = time.time()
                            await bio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        await bio.emit('session_request', {'session_id':idss})
                        await bio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared. 
                        user_flag_5005[user_id] = time.time()
               
            elif socket_in_use[user_id] == '3':
                print("THIS IS INSIDE SOCKET 3")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': #and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            # await sio.sleep(10)
                            await cio.emit('session_request', {'session_id':idss})
                            await cio.emit('user_uttered',{'session_id':idss,
                                'message' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else: 
                            user_flag_5005[user_id] = time.time()
                            # await sio.sleep(10)
                            await cio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        # await sio.sleep(10)
                        await cio.emit('session_request', {'session_id':idss})
                        await cio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared. 
                        user_flag_5005[user_id] = time.time()
        
            elif socket_in_use[user_id] == '4':
                print("THIS IS INSIDE SOCKET 4")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id]  >300:
                            user_flag_5005[user_id] = time.time()
                            # await sio.sleep(10)
                            await dio.emit('session_request', {'session_id':idss})
                            await dio.emit('user_uttered',{'session_id':idss,
                                'message' : text, 
                                'metadata' : {'unique_name': unique_email},
                            })
                        else: 
                            user_flag_5005[user_id] = time.time()
                            # await sio.sleep(10)
                            await dio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        # await sio.sleep(10)
                        await dio.emit('session_request', {'session_id':idss})
                        await dio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared. 
                        user_flag_5005[user_id] = time.time()
               
            elif socket_in_use[user_id] == '5':
                print("THIS IS INSIDE SOCKET 5")
                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            # await sio.sleep(10)
                            await eio.emit('session_request', {'session_id':idss})
                            await eio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else: 
                            user_flag_5005[user_id] = time.time()
                            # await sio.sleep(10)
                            await eio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        # await sio.sleep(10)
                        await eio.emit('session_request', {'session_id':idss})
                        await eio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared. 
                        user_flag_5005[user_id] = time.time()
               
            elif socket_in_use[user_id] == '6':
                print("THIS IS INSIDE SOCKET 6")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            # await sio.sleep(10)
                            await fio.emit('session_request', {'session_id':idss})
                            await fio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else: 
                            user_flag_5005[user_id] = time.time()
                            # await sio.sleep(10)
                            await fio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        # await sio.sleep(10)
                        await fio.emit('session_request', {'session_id':idss})
                        await fio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared. 
                        user_flag_5005[user_id] = time.time()
            elif socket_in_use[user_id] == '7':
                print("THIS IS INSIDE SOCKET 7")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            # await sio.sleep(10)
                            await gio.emit('session_request', {'session_id':idss})
                            await gio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else: 
                            user_flag_5005[user_id] = time.time()
                            # await sio.sleep(10)
                            await gio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        # await sio.sleep(10)
                        await gio.emit('session_request', {'session_id':idss})
                        await gio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared. 
                        user_flag_5005[user_id] = time.time()
            elif socket_in_use[user_id] == '8':
                print("THIS IS INSIDE SOCKET 8")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            # await sio.sleep(10)
                            await hio.emit('session_request', {'session_id':idss})
                            await hio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else: 
                            user_flag_5005[user_id] = time.time()
                            # await sio.sleep(10)
                            await hio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        # await sio.sleep(10)
                        await hio.emit('session_request', {'session_id':idss})
                        await hio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared. 
                        user_flag_5005[user_id] = time.time()
            elif socket_in_use[user_id] == '9':
                print("THIS IS INSIDE SOCKET 9")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            # await sio.sleep(10)
                            await iio.emit('session_request', {'session_id':idss})
                            await iio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else: 
                            user_flag_5005[user_id] = time.time()
                            # await sio.sleep(10)
                            await iio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        # await sio.sleep(10)
                        await iio.emit('session_request', {'session_id':idss})
                        await iio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared. 
                        user_flag_5005[user_id] = time.time()
            elif socket_in_use[user_id] == '10':
                print("THIS IS INSIDE SOCKET 10")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            # await sio.sleep(10)
                            await jio.emit('session_request', {'session_id':idss})
                            await jio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else: 
                            user_flag_5005[user_id] = time.time()
                            # await sio.sleep(10)
                            await jio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        # await sio.sleep(10)
                        await jio.emit('session_request', {'session_id':idss})
                        await jio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared. 
                        user_flag_5005[user_id] = time.time()
            elif socket_in_use[user_id] == '11':
                print("THIS IS INSIDE SOCKET 11")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            # await sio.sleep(10)
                            await kio.emit('session_request', {'session_id':idss})
                            await kio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else: 
                            user_flag_5005[user_id] = time.time()
                            # await sio.sleep(10)
                            await kio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        # await sio.sleep(10)
                        await kio.emit('session_request', {'session_id':idss})
                        await kio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared. 
                        user_flag_5005[user_id] = time.time()
            elif socket_in_use[user_id] == '12':
                print("THIS IS INSIDE SOCKET 12")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            # await sio.sleep(10)
                            await lio.emit('session_request', {'session_id':idss})
                            await lio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else: 
                            user_flag_5005[user_id] = time.time()
                            # await sio.sleep(10)
                            await lio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        # await sio.sleep(10)
                        await lio.emit('session_request', {'session_id':idss})
                        await lio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared. 
                        user_flag_5005[user_id] = time.time()
            elif socket_in_use[user_id] == '13':
                print("THIS IS INSIDE SOCKET 13")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            # await sio.sleep(10)
                            await mio.emit('session_request', {'session_id':idss})
                            await mio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else: 
                            user_flag_5005[user_id] = time.time()
                            # await sio.sleep(10)
                            await mio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        # await sio.sleep(10)
                        await mio.emit('session_request', {'session_id':idss})
                        await mio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared. 
                        user_flag_5005[user_id] = time.time()
            elif socket_in_use[user_id] == '14':
                print("THIS IS INSIDE SOCKET 14")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            # await sio.sleep(10)
                            await nio.emit('session_request', {'session_id':idss})
                            await nio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else: 
                            user_flag_5005[user_id] = time.time()
                            # await sio.sleep(10)
                            await nio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        # await sio.sleep(10)
                        await nio.emit('session_request', {'session_id':idss})
                        await nio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared. 
                        user_flag_5005[user_id] = time.time()
            elif socket_in_use[user_id] == '15':
                print("THIS IS INSIDE SOCKET 15")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            # await sio.sleep(10)
                            await oio.emit('session_request', {'session_id':idss})
                            await oio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else: 
                            user_flag_5005[user_id] = time.time()
                            # await sio.sleep(10)
                            await oio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        # await sio.sleep(10)
                        await oio.emit('session_request', {'session_id':idss})
                        await oio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared. 
                        user_flag_5005[user_id] = time.time()
            elif socket_in_use[user_id] == '16':
                print("THIS IS INSIDE SOCKET 16")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            # await sio.sleep(10)
                            await pio.emit('session_request', {'session_id':idss})
                            await pio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else: 
                            user_flag_5005[user_id] = time.time()
                            # await sio.sleep(10)
                            await pio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        # await sio.sleep(10)
                        await pio.emit('session_request', {'session_id':idss})
                        await pio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared. 
                        user_flag_5005[user_id] = time.time()
            elif socket_in_use[user_id] == '17':
                print("THIS IS INSIDE SOCKET 17")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            # await sio.sleep(10)
                            await qio.emit('session_request', {'session_id':idss})
                            await qio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else: 
                            user_flag_5005[user_id] = time.time()
                            # await sio.sleep(10)
                            await qio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        # await sio.sleep(10)
                        await qio.emit('session_request', {'session_id':idss})
                        await qio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared. 
                        user_flag_5005[user_id] = time.time()
            elif socket_in_use[user_id] == '18':
                print("THIS IS INSIDE SOCKET 18")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            # await sio.sleep(10)
                            await rio.emit('session_request', {'session_id':idss})
                            await rio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else: 
                            user_flag_5005[user_id] = time.time()
                            # await sio.sleep(10)
                            await rio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        # await sio.sleep(10)
                        await rio.emit('session_request', {'session_id':idss})
                        await rio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared. 
                        user_flag_5005[user_id] = time.time()
            elif socket_in_use[user_id] == '19':
                print("THIS IS INSIDE SOCKET 19")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            # await sio.sleep(10)
                            await sio.emit('session_request', {'session_id':idss})
                            await sio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else: 
                            user_flag_5005[user_id] = time.time()
                            # await sio.sleep(10)
                            await sio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        # await sio.sleep(10)
                        await sio.emit('session_request', {'session_id':idss})
                        await sio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared. 
                        user_flag_5005[user_id] = time.time()
            elif socket_in_use[user_id] == '20':
                print("THIS IS INSIDE SOCKET 20")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            # await sio.sleep(10)
                            await tsio.emit('session_request', {'session_id':idss})
                            await tsio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else: 
                            user_flag_5005[user_id] = time.time()
                            # await sio.sleep(10)
                            await tsio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        # await sio.sleep(10)
                        await tsio.emit('session_request', {'session_id':idss})
                        await tsio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared. 
                        user_flag_5005[user_id] = time.time()
            elif socket_in_use[user_id] == '21':
                print("THIS IS INSIDE SOCKET 21")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            # await sio.sleep(10)
                            await usio.emit('session_request', {'session_id':idss})
                            await usio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else: 
                            user_flag_5005[user_id] = time.time()
                            # await sio.sleep(10)
                            await usio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        # await sio.sleep(10)
                        await usio.emit('session_request', {'session_id':idss})
                        await usio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared. 
                        user_flag_5005[user_id] = time.time()
            elif socket_in_use[user_id] == '22':
                print("THIS IS INSIDE SOCKET 22")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            # await sio.sleep(10)
                            await vsio.emit('session_request', {'session_id':idss})
                            await vsio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else: 
                            user_flag_5005[user_id] = time.time()
                            # await sio.sleep(10)
                            await vsio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        # await sio.sleep(10)
                        await vsio.emit('session_request', {'session_id':idss})
                        await vsio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared. 
                        user_flag_5005[user_id] = time.time()
            elif socket_in_use[user_id] == '23':
                print("THIS IS INSIDE SOCKET 23")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            # await sio.sleep(10)
                            await wsio.emit('session_request', {'session_id':idss})
                            await wsio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else: 
                            user_flag_5005[user_id] = time.time()
                            # await sio.sleep(10)
                            await wsio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        # await sio.sleep(10)
                        await wsio.emit('session_request', {'session_id':idss})
                        await wsio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared. 
                        user_flag_5005[user_id] = time.time()
            elif socket_in_use[user_id] == '24':
                print("THIS IS INSIDE SOCKET 24")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            # await sio.sleep(10)
                            await xio.emit('session_request', {'session_id':idss})
                            await xio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else: 
                            user_flag_5005[user_id] = time.time()
                            # await sio.sleep(10)
                            await xio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        # await sio.sleep(10)
                        await xio.emit('session_request', {'session_id':idss})
                        await xio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared. 
                        user_flag_5005[user_id] = time.time()
            elif socket_in_use[user_id] == '25':
                print("THIS IS INSIDE SOCKET 25")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            # await sio.sleep(10)
                            await yio.emit('session_request', {'session_id':idss})
                            await yio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else: 
                            user_flag_5005[user_id] = time.time()
                            # await sio.sleep(10)
                            await yio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        # await sio.sleep(10)
                        await yio.emit('session_request', {'session_id':idss})
                        await yio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared. 
                        user_flag_5005[user_id] = time.time()
            elif socket_in_use[user_id] == '26':
                print("THIS IS INSIDE SOCKET 26")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            # await sio.sleep(10)
                            await zio.emit('session_request', {'session_id':idss})
                            await zio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else: 
                            user_flag_5005[user_id] = time.time()
                            # await sio.sleep(10)
                            await zio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        # await sio.sleep(10)
                        await zio.emit('session_request', {'session_id':idss})
                        await zio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared. 
                        user_flag_5005[user_id] = time.time()
            ####-----
            if socket_in_use[user_id] == '27':
                print("THIS IS INSIDE SOCKET 27")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        print("THIS IS INSIDE IF")
                        if time.time() - user_flag_5005[user_id] >1000:
                            user_flag_5005[user_id] = time.time()
                            # await sio.sleep(10)
                            await aaio.emit('session_request', {'session_id':idss})
                            await aaio.emit('user_uttered',{'session_id':idss,
                                'message' : text,
                                'metadata' : {'unique_name': unique_email}
                            })
                        else: 
                            user_flag_5005[user_id] = time.time()
                            # await sio.sleep(10)
                            await aaio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email}
                            })
                        print('THIS IS END OF IF')
                    else:
                        print("THIS IS INSIDE ELSE")
                        # await sio.sleep(10)
                        await aaio.emit('session_request', {'session_id':idss})
                        await aaio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email}
                        })
                        print("THIS IS END OF ELSE")
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared. 
                        user_flag_5005[user_id] = time.time()
              
            elif socket_in_use[user_id] == '28':
                print("THIS IS INSIDE SOCKET 28")
               
                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': #and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): # To check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >1000:
                            user_flag_5005[user_id] = time.time()
                            await abio.emit('session_request', {'session_id':idss})
                            await abio.emit('user_uttered',{'session_id':idss,
                                'message' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else: 
                            user_flag_5005[user_id] = time.time()
                            await abio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        await abio.emit('session_request', {'session_id':idss})
                        await abio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared. 
                        user_flag_5005[user_id] = time.time()
               
            elif socket_in_use[user_id] == '29':
                print("THIS IS INSIDE SOCKET 29")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': #and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            # await sio.sleep(10)
                            await acio.emit('session_request', {'session_id':idss})
                            await acio.emit('user_uttered',{'session_id':idss,
                                'message' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else: 
                            user_flag_5005[user_id] = time.time()
                            # await sio.sleep(10)
                            await acio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        # await sio.sleep(10)
                        await acio.emit('session_request', {'session_id':idss})
                        await acio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared. 
                        user_flag_5005[user_id] = time.time()
        
            elif socket_in_use[user_id] == '30':
                print("THIS IS INSIDE SOCKET 30")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id]  >300:
                            user_flag_5005[user_id] = time.time()
                            # await sio.sleep(10)
                            await adio.emit('session_request', {'session_id':idss})
                            await adio.emit('user_uttered',{'session_id':idss,
                                'message' : text, 
                                'metadata' : {'unique_name': unique_email},
                            })
                        else: 
                            user_flag_5005[user_id] = time.time()
                            # await sio.sleep(10)
                            await adio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        # await sio.sleep(10)
                        await adio.emit('session_request', {'session_id':idss})
                        await adio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared. 
                        user_flag_5005[user_id] = time.time()
               
            elif socket_in_use[user_id] == '31':
                print("THIS IS INSIDE SOCKET 31")
                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            # await sio.sleep(10)
                            await aeio.emit('session_request', {'session_id':idss})
                            await aeio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else: 
                            user_flag_5005[user_id] = time.time()
                            # await sio.sleep(10)
                            await aeio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        # await sio.sleep(10)
                        await aeio.emit('session_request', {'session_id':idss})
                        await aeio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared. 
                        user_flag_5005[user_id] = time.time()
               
            elif socket_in_use[user_id] == '32':
                print("THIS IS INSIDE SOCKET 32")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            # await sio.sleep(10)
                            await afio.emit('session_request', {'session_id':idss})
                            await afio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else: 
                            user_flag_5005[user_id] = time.time()
                            # await sio.sleep(10)
                            await afio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        # await sio.sleep(10)
                        await afio.emit('session_request', {'session_id':idss})
                        await afio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared. 
                        user_flag_5005[user_id] = time.time()
            elif socket_in_use[user_id] == '33':
                print("THIS IS INSIDE SOCKET 33")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            # await sio.sleep(10)
                            await agio.emit('session_request', {'session_id':idss})
                            await agio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else: 
                            user_flag_5005[user_id] = time.time()
                            # await sio.sleep(10)
                            await agio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        # await sio.sleep(10)
                        await agio.emit('session_request', {'session_id':idss})
                        await agio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared. 
                        user_flag_5005[user_id] = time.time()
            elif socket_in_use[user_id] == '34':
                print("THIS IS INSIDE SOCKET 34")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            # await sio.sleep(10)
                            await ahio.emit('session_request', {'session_id':idss})
                            await ahio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else: 
                            user_flag_5005[user_id] = time.time()
                            # await sio.sleep(10)
                            await ahio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        # await sio.sleep(10)
                        await ahio.emit('session_request', {'session_id':idss})
                        await ahio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared. 
                        user_flag_5005[user_id] = time.time()
            elif socket_in_use[user_id] == '35':
                print("THIS IS INSIDE SOCKET 35")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            # await sio.sleep(10)
                            await aiio.emit('session_request', {'session_id':idss})
                            await aiio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else: 
                            user_flag_5005[user_id] = time.time()
                            # await sio.sleep(10)
                            await aiio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        # await sio.sleep(10)
                        await aiio.emit('session_request', {'session_id':idss})
                        await aiio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared. 
                        user_flag_5005[user_id] = time.time()
            elif socket_in_use[user_id] == '36':
                print("THIS IS INSIDE SOCKET 36")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            # await sio.sleep(10)
                            await ajio.emit('session_request', {'session_id':idss})
                            await ajio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else: 
                            user_flag_5005[user_id] = time.time()
                            # await sio.sleep(10)
                            await ajio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        # await sio.sleep(10)
                        await ajio.emit('session_request', {'session_id':idss})
                        await ajio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared. 
                        user_flag_5005[user_id] = time.time()
            elif socket_in_use[user_id] == '37':
                print("THIS IS INSIDE SOCKET 37")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            # await sio.sleep(10)
                            await akio.emit('session_request', {'session_id':idss})
                            await akio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else: 
                            user_flag_5005[user_id] = time.time()
                            # await sio.sleep(10)
                            await akio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        # await sio.sleep(10)
                        await akio.emit('session_request', {'session_id':idss})
                        await akio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared. 
                        user_flag_5005[user_id] = time.time()
            elif socket_in_use[user_id] == '38':
                print("THIS IS INSIDE SOCKET 38")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            # await sio.sleep(10)
                            await alio.emit('session_request', {'session_id':idss})
                            await alio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else: 
                            user_flag_5005[user_id] = time.time()
                            # await sio.sleep(10)
                            await alio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        # await sio.sleep(10)
                        await alio.emit('session_request', {'session_id':idss})
                        await alio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared. 
                        user_flag_5005[user_id] = time.time()
            elif socket_in_use[user_id] == '39':
                print("THIS IS INSIDE SOCKET 39")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            # await sio.sleep(10)
                            await amio.emit('session_request', {'session_id':idss})
                            await amio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else: 
                            user_flag_5005[user_id] = time.time()
                            # await sio.sleep(10)
                            await amio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        # await sio.sleep(10)
                        await amio.emit('session_request', {'session_id':idss})
                        await amio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared. 
                        user_flag_5005[user_id] = time.time()
            elif socket_in_use[user_id] == '40':
                print("THIS IS INSIDE SOCKET 40")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            # await sio.sleep(10)
                            await anio.emit('session_request', {'session_id':idss})
                            await anio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else: 
                            user_flag_5005[user_id] = time.time()
                            # await sio.sleep(10)
                            await anio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        # await sio.sleep(10)
                        await anio.emit('session_request', {'session_id':idss})
                        await anio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared. 
                        user_flag_5005[user_id] = time.time()
            elif socket_in_use[user_id] == '41':
                print("THIS IS INSIDE SOCKET 41")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            # await sio.sleep(10)
                            await aoio.emit('session_request', {'session_id':idss})
                            await aoio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else: 
                            user_flag_5005[user_id] = time.time()
                            # await sio.sleep(10)
                            await aoio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        # await sio.sleep(10)
                        await aoio.emit('session_request', {'session_id':idss})
                        await aoio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared. 
                        user_flag_5005[user_id] = time.time()
            elif socket_in_use[user_id] == '42':
                print("THIS IS INSIDE SOCKET 42")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            # await sio.sleep(10)
                            await apio.emit('session_request', {'session_id':idss})
                            await apio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else: 
                            user_flag_5005[user_id] = time.time()
                            # await sio.sleep(10)
                            await apio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        # await sio.sleep(10)
                        await apio.emit('session_request', {'session_id':idss})
                        await apio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared. 
                        user_flag_5005[user_id] = time.time()
            elif socket_in_use[user_id] == '43':
                print("THIS IS INSIDE SOCKET 43")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            # await sio.sleep(10)
                            await aqio.emit('session_request', {'session_id':idss})
                            await aqio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else: 
                            user_flag_5005[user_id] = time.time()
                            # await sio.sleep(10)
                            await aqio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        # await sio.sleep(10)
                        await aqio.emit('session_request', {'session_id':idss})
                        await aqio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared. 
                        user_flag_5005[user_id] = time.time()
            elif socket_in_use[user_id] == '44':
                print("THIS IS INSIDE SOCKET 44")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            # await sio.sleep(10)
                            await ario.emit('session_request', {'session_id':idss})
                            await ario.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else: 
                            user_flag_5005[user_id] = time.time()
                            # await sio.sleep(10)
                            await ario.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        # await sio.sleep(10)
                        await ario.emit('session_request', {'session_id':idss})
                        await ario.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared. 
                        user_flag_5005[user_id] = time.time()
            elif socket_in_use[user_id] == '45':
                print("THIS IS INSIDE SOCKET 45")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            # await sio.sleep(10)
                            await asio.emit('session_request', {'session_id':idss})
                            await asio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else: 
                            user_flag_5005[user_id] = time.time()
                            # await sio.sleep(10)
                            await asio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        # await sio.sleep(10)
                        await asio.emit('session_request', {'session_id':idss})
                        await asio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared. 
                        user_flag_5005[user_id] = time.time()
            elif socket_in_use[user_id] == '46':
                print("THIS IS INSIDE SOCKET 46")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            # await sio.sleep(10)
                            await atio.emit('session_request', {'session_id':idss})
                            await atio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else: 
                            user_flag_5005[user_id] = time.time()
                            # await sio.sleep(10)
                            await atio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        # await sio.sleep(10)
                        await atio.emit('session_request', {'session_id':idss})
                        await atio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared. 
                        user_flag_5005[user_id] = time.time()
            elif socket_in_use[user_id] == '47':
                print("THIS IS INSIDE SOCKET 47")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            # await sio.sleep(10)
                            await auio.emit('session_request', {'session_id':idss})
                            await asio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else: 
                            user_flag_5005[user_id] = time.time()
                            # await sio.sleep(10)
                            await auio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        # await sio.sleep(10)
                        await auio.emit('session_request', {'session_id':idss})
                        await auio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared. 
                        user_flag_5005[user_id] = time.time()
            elif socket_in_use[user_id] == '48':
                print("THIS IS INSIDE SOCKET 48")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            # await sio.sleep(10)
                            await avio.emit('session_request', {'session_id':idss})
                            await avio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else: 
                            user_flag_5005[user_id] = time.time()
                            # await sio.sleep(10)
                            await avio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        # await sio.sleep(10)
                        await avio.emit('session_request', {'session_id':idss})
                        await avio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared. 
                        user_flag_5005[user_id] = time.time()
            elif socket_in_use[user_id] == '49':
                print("THIS IS INSIDE SOCKET 49")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            # await sio.sleep(10)
                            await awio.emit('session_request', {'session_id':idss})
                            await awio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else: 
                            user_flag_5005[user_id] = time.time()
                            # await sio.sleep(10)
                            await awio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        # await sio.sleep(10)
                        await awio.emit('session_request', {'session_id':idss})
                        await awio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared. 
                        user_flag_5005[user_id] = time.time()
            elif socket_in_use[user_id] == '50':
                print("THIS IS INSIDE SOCKET 50")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            # await sio.sleep(10)
                            await axio.emit('session_request', {'session_id':idss})
                            await axio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else: 
                            user_flag_5005[user_id] = time.time()
                            # await sio.sleep(10)
                            await axio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        # await sio.sleep(10)
                        await axio.emit('session_request', {'session_id':idss})
                        await axio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared. 
                        user_flag_5005[user_id] = time.time()
            elif socket_in_use[user_id] == '51':
                print("THIS IS INSIDE SOCKET 51")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            # await sio.sleep(10)
                            await ayio.emit('session_request', {'session_id':idss})
                            await ayio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else: 
                            user_flag_5005[user_id] = time.time()
                            # await sio.sleep(10)
                            await ayio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        # await sio.sleep(10)
                        await ayio.emit('session_request', {'session_id':idss})
                        await ayio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared. 
                        user_flag_5005[user_id] = time.time()
            elif socket_in_use[user_id] == '52':
                print("THIS IS INSIDE SOCKET 52")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            # await sio.sleep(10)
                            await azio.emit('session_request', {'session_id':idss})
                            await azio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else: 
                            user_flag_5005[user_id] = time.time()
                            # await sio.sleep(10)
                            await azio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        # await sio.sleep(10)
                        await azio.emit('session_request', {'session_id':idss})
                        await azio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared. 
                        user_flag_5005[user_id] = time.time()

            #------b
            
            elif socket_in_use[user_id] == '53':
                print("THIS IS INSIDE SOCKET 53")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            await baio.emit('session_request', {'session_id':idss})
                            await baio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else: 
                            user_flag_5005[user_id] = time.time()
                            await baio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        await baio.emit('session_request', {'session_id':idss})
                        await baio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared.
                        user_flag_5005[user_id] = time.time()



            elif socket_in_use[user_id] == '54':
                print("THIS IS INSIDE SOCKET 54")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            await bbio.emit('session_request', {'session_id':idss})
                            await bbio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else:
                            user_flag_5005[user_id] = time.time()
                            await bbio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        await bbio.emit('session_request', {'session_id':idss})
                        await bbio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared.
                        user_flag_5005[user_id] = time.time()



            elif socket_in_use[user_id] == '55':
                print("THIS IS INSIDE SOCKET 55")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            await bcio.emit('session_request', {'session_id':idss})
                            await bcio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else:
                            user_flag_5005[user_id] = time.time()
                            await bcio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        await bcio.emit('session_request', {'session_id':idss})
                        await bcio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared.
                        user_flag_5005[user_id] = time.time()



            elif socket_in_use[user_id] == '56':
                print("THIS IS INSIDE SOCKET 56")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            await bdio.emit('session_request', {'session_id':idss})
                            await bdio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else:
                            user_flag_5005[user_id] = time.time()
                            await bdio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        await bdio.emit('session_request', {'session_id':idss})
                        await bdio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared.
                        user_flag_5005[user_id] = time.time()



            elif socket_in_use[user_id] == '57':
                print("THIS IS INSIDE SOCKET 57")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            await beio.emit('session_request', {'session_id':idss})
                            await beio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else:
                            user_flag_5005[user_id] = time.time()
                            await beio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        await beio.emit('session_request', {'session_id':idss})
                        await beio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared.
                        user_flag_5005[user_id] = time.time()



            elif socket_in_use[user_id] == '58':
                print("THIS IS INSIDE SOCKET 58")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            await bfio.emit('session_request', {'session_id':idss})
                            await bfio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else:
                            user_flag_5005[user_id] = time.time()
                            await bfio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        await bfio.emit('session_request', {'session_id':idss})
                        await bfio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared.
                        user_flag_5005[user_id] = time.time()



            elif socket_in_use[user_id] == '59':
                print("THIS IS INSIDE SOCKET 59")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            await bgio.emit('session_request', {'session_id':idss})
                            await bgio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else:
                            user_flag_5005[user_id] = time.time()
                            await bgio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        await bgio.emit('session_request', {'session_id':idss})
                        await bgio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared.
                        user_flag_5005[user_id] = time.time()



            elif socket_in_use[user_id] == '60':
                print("THIS IS INSIDE SOCKET 60")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            await bhio.emit('session_request', {'session_id':idss})
                            await bhio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else:
                            user_flag_5005[user_id] = time.time()
                            await bhio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        await bhio.emit('session_request', {'session_id':idss})
                        await bhio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared.
                        user_flag_5005[user_id] = time.time()



            elif socket_in_use[user_id] == '61':
                print("THIS IS INSIDE SOCKET 61")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            await biio.emit('session_request', {'session_id':idss})
                            await biio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else:
                            user_flag_5005[user_id] = time.time()
                            await biio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        await biio.emit('session_request', {'session_id':idss})
                        await biio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared.
                        user_flag_5005[user_id] = time.time()



            elif socket_in_use[user_id] == '62':
                print("THIS IS INSIDE SOCKET 62")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            await bjio.emit('session_request', {'session_id':idss})
                            await bjio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else:
                            user_flag_5005[user_id] = time.time()
                            await bjio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        await bjio.emit('session_request', {'session_id':idss})
                        await bjio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared.
                        user_flag_5005[user_id] = time.time()



            elif socket_in_use[user_id] == '63':
                print("THIS IS INSIDE SOCKET 63")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            await bkio.emit('session_request', {'session_id':idss})
                            await bkio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else:
                            user_flag_5005[user_id] = time.time()
                            await bkio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        await bkio.emit('session_request', {'session_id':idss})
                        await bkio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared.
                        user_flag_5005[user_id] = time.time()



            elif socket_in_use[user_id] == '64':
                print("THIS IS INSIDE SOCKET 64")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            await blio.emit('session_request', {'session_id':idss})
                            await blio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else:
                            user_flag_5005[user_id] = time.time()
                            await blio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        await blio.emit('session_request', {'session_id':idss})
                        await blio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared.
                        user_flag_5005[user_id] = time.time()



            elif socket_in_use[user_id] == '65':
                print("THIS IS INSIDE SOCKET 65")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            await bmio.emit('session_request', {'session_id':idss})
                            await bmio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else:
                            user_flag_5005[user_id] = time.time()
                            await bmio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        await bmio.emit('session_request', {'session_id':idss})
                        await bmio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared.
                        user_flag_5005[user_id] = time.time()



            elif socket_in_use[user_id] == '66':
                print("THIS IS INSIDE SOCKET 66")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            await bnio.emit('session_request', {'session_id':idss})
                            await bnio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else:
                            user_flag_5005[user_id] = time.time()
                            await bnio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        await bnio.emit('session_request', {'session_id':idss})
                        await bnio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared.
                        user_flag_5005[user_id] = time.time()



            elif socket_in_use[user_id] == '67':
                print("THIS IS INSIDE SOCKET 67")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            await boio.emit('session_request', {'session_id':idss})
                            await boio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else:
                            user_flag_5005[user_id] = time.time()
                            await boio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        await boio.emit('session_request', {'session_id':idss})
                        await boio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared.
                        user_flag_5005[user_id] = time.time()



            elif socket_in_use[user_id] == '68':
                print("THIS IS INSIDE SOCKET 68")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            await bpio.emit('session_request', {'session_id':idss})
                            await bpio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else:
                            user_flag_5005[user_id] = time.time()
                            await bpio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        await bpio.emit('session_request', {'session_id':idss})
                        await bpio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared.
                        user_flag_5005[user_id] = time.time()



            elif socket_in_use[user_id] == '69':
                print("THIS IS INSIDE SOCKET 69")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            await bqio.emit('session_request', {'session_id':idss})
                            await bqio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else:
                            user_flag_5005[user_id] = time.time()
                            await bqio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        await bqio.emit('session_request', {'session_id':idss})
                        await bqio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared.
                        user_flag_5005[user_id] = time.time()



            elif socket_in_use[user_id] == '70':
                print("THIS IS INSIDE SOCKET 70")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            await brio.emit('session_request', {'session_id':idss})
                            await brio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else:
                            user_flag_5005[user_id] = time.time()
                            await brio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        await brio.emit('session_request', {'session_id':idss})
                        await brio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared.
                        user_flag_5005[user_id] = time.time()



            elif socket_in_use[user_id] == '71':
                print("THIS IS INSIDE SOCKET 71")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            await bsio.emit('session_request', {'session_id':idss})
                            await bsio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else:
                            user_flag_5005[user_id] = time.time()
                            await bsio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        await bsio.emit('session_request', {'session_id':idss})
                        await bsio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared.
                        user_flag_5005[user_id] = time.time()



            elif socket_in_use[user_id] == '72':
                print("THIS IS INSIDE SOCKET 72")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            await btio.emit('session_request', {'session_id':idss})
                            await btio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else:
                            user_flag_5005[user_id] = time.time()
                            await btio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        await btio.emit('session_request', {'session_id':idss})
                        await btio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared.
                        user_flag_5005[user_id] = time.time()



            elif socket_in_use[user_id] == '73':
                print("THIS IS INSIDE SOCKET 73")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            await buio.emit('session_request', {'session_id':idss})
                            await buio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else:
                            user_flag_5005[user_id] = time.time()
                            await buio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        await buio.emit('session_request', {'session_id':idss})
                        await buio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared.
                        user_flag_5005[user_id] = time.time()



            elif socket_in_use[user_id] == '74':
                print("THIS IS INSIDE SOCKET 74")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            await bvio.emit('session_request', {'session_id':idss})
                            await bvio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else:
                            user_flag_5005[user_id] = time.time()
                            await bvio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        await bvio.emit('session_request', {'session_id':idss})
                        await bvio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared.
                        user_flag_5005[user_id] = time.time()



            elif socket_in_use[user_id] == '75':
                print("THIS IS INSIDE SOCKET 75")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            await bwio.emit('session_request', {'session_id':idss})
                            await bwio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else:
                            user_flag_5005[user_id] = time.time()
                            await bwio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        await bwio.emit('session_request', {'session_id':idss})
                        await bwio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared.
                        user_flag_5005[user_id] = time.time()



            elif socket_in_use[user_id] == '76':
                print("THIS IS INSIDE SOCKET 76")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            await bxio.emit('session_request', {'session_id':idss})
                            await bxio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else:
                            user_flag_5005[user_id] = time.time()
                            await bxio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        await bxio.emit('session_request', {'session_id':idss})
                        await bxio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared.
                        user_flag_5005[user_id] = time.time()



            elif socket_in_use[user_id] == '77':
                print("THIS IS INSIDE SOCKET 77")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            await byio.emit('session_request', {'session_id':idss})
                            await byio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else:
                            user_flag_5005[user_id] = time.time()
                            await byio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        await byio.emit('session_request', {'session_id':idss})
                        await byio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared.
                        user_flag_5005[user_id] = time.time()



            elif socket_in_use[user_id] == '78':
                print("THIS IS INSIDE SOCKET 78")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            await bzio.emit('session_request', {'session_id':idss})
                            await bzio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else:
                            user_flag_5005[user_id] = time.time()
                            await bzio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        await bzio.emit('session_request', {'session_id':idss})
                        await bzio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared.
                        user_flag_5005[user_id] = time.time()

            #----c

            elif socket_in_use[user_id] == '79':
                print("THIS IS INSIDE SOCKET 79")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            await caio.emit('session_request', {'session_id':idss})
                            await caio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else: 
                            user_flag_5005[user_id] = time.time()
                            await caio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        await caio.emit('session_request', {'session_id':idss})
                        await caio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared.      
                        user_flag_5005[user_id] = time.time()
    

            elif socket_in_use[user_id] == '80':
                print("THIS IS INSIDE SOCKET 80")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            await cbio.emit('session_request', {'session_id':idss})
                            await cbio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else:
                            user_flag_5005[user_id] = time.time()
                            await cbio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        await cbio.emit('session_request', {'session_id':idss})
                        await cbio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared.
                        user_flag_5005[user_id] = time.time()


            elif socket_in_use[user_id] == '81':
                print("THIS IS INSIDE SOCKET 81")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            await ccio.emit('session_request', {'session_id':idss})
                            await ccio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else:
                            user_flag_5005[user_id] = time.time()
                            await ccio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        await ccio.emit('session_request', {'session_id':idss})
                        await ccio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared.
                        user_flag_5005[user_id] = time.time()


            elif socket_in_use[user_id] == '82':
                print("THIS IS INSIDE SOCKET 82")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            await cdio.emit('session_request', {'session_id':idss})
                            await cdio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else:
                            user_flag_5005[user_id] = time.time()
                            await cdio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        await cdio.emit('session_request', {'session_id':idss})
                        await cdio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared.
                        user_flag_5005[user_id] = time.time()


            elif socket_in_use[user_id] == '83':
                print("THIS IS INSIDE SOCKET 83")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            await ceio.emit('session_request', {'session_id':idss})
                            await ceio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else:
                            user_flag_5005[user_id] = time.time()
                            await ceio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        await ceio.emit('session_request', {'session_id':idss})
                        await ceio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared.
                        user_flag_5005[user_id] = time.time()


            elif socket_in_use[user_id] == '84':
                print("THIS IS INSIDE SOCKET 84")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            await cfio.emit('session_request', {'session_id':idss})
                            await cfio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else:
                            user_flag_5005[user_id] = time.time()
                            await cfio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        await cfio.emit('session_request', {'session_id':idss})
                        await cfio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared.
                        user_flag_5005[user_id] = time.time()


            elif socket_in_use[user_id] == '85':
                print("THIS IS INSIDE SOCKET 85")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            await cgio.emit('session_request', {'session_id':idss})
                            await cgio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else:
                            user_flag_5005[user_id] = time.time()
                            await cgio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        await cgio.emit('session_request', {'session_id':idss})
                        await cgio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared.
                        user_flag_5005[user_id] = time.time()


            elif socket_in_use[user_id] == '86':
                print("THIS IS INSIDE SOCKET 86")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            await chio.emit('session_request', {'session_id':idss})
                            await chio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else:
                            user_flag_5005[user_id] = time.time()
                            await chio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        await chio.emit('session_request', {'session_id':idss})
                        await chio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared.
                        user_flag_5005[user_id] = time.time()


            elif socket_in_use[user_id] == '87':
                print("THIS IS INSIDE SOCKET 87")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            await ciio.emit('session_request', {'session_id':idss})
                            await ciio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else:
                            user_flag_5005[user_id] = time.time()
                            await ciio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        await ciio.emit('session_request', {'session_id':idss})
                        await ciio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared.
                        user_flag_5005[user_id] = time.time()


            elif socket_in_use[user_id] == '88':
                print("THIS IS INSIDE SOCKET 88")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            await cjio.emit('session_request', {'session_id':idss})
                            await cjio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else:
                            user_flag_5005[user_id] = time.time()
                            await cjio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        await cjio.emit('session_request', {'session_id':idss})
                        await cjio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared.
                        user_flag_5005[user_id] = time.time()


            elif socket_in_use[user_id] == '89':
                print("THIS IS INSIDE SOCKET 89")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            await ckio.emit('session_request', {'session_id':idss})
                            await ckio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else:
                            user_flag_5005[user_id] = time.time()
                            await ckio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        await ckio.emit('session_request', {'session_id':idss})
                        await ckio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared.
                        user_flag_5005[user_id] = time.time()


            elif socket_in_use[user_id] == '90':
                print("THIS IS INSIDE SOCKET 90")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            await clio.emit('session_request', {'session_id':idss})
                            await clio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else:
                            user_flag_5005[user_id] = time.time()
                            await clio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        await clio.emit('session_request', {'session_id':idss})
                        await clio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared.
                        user_flag_5005[user_id] = time.time()


            elif socket_in_use[user_id] == '91':
                print("THIS IS INSIDE SOCKET 91")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            await cmio.emit('session_request', {'session_id':idss})
                            await cmio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else:
                            user_flag_5005[user_id] = time.time()
                            await cmio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        await cmio.emit('session_request', {'session_id':idss})
                        await cmio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared.
                        user_flag_5005[user_id] = time.time()


            elif socket_in_use[user_id] == '92':
                print("THIS IS INSIDE SOCKET 92")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            await cnio.emit('session_request', {'session_id':idss})
                            await cnio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else:
                            user_flag_5005[user_id] = time.time()
                            await cnio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        await cnio.emit('session_request', {'session_id':idss})
                        await cnio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared.
                        user_flag_5005[user_id] = time.time()


            elif socket_in_use[user_id] == '93':
                print("THIS IS INSIDE SOCKET 93")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            await coio.emit('session_request', {'session_id':idss})
                            await coio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else:
                            user_flag_5005[user_id] = time.time()
                            await coio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        await coio.emit('session_request', {'session_id':idss})
                        await coio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared.
                        user_flag_5005[user_id] = time.time()


            elif socket_in_use[user_id] == '94':
                print("THIS IS INSIDE SOCKET 94")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            await cpio.emit('session_request', {'session_id':idss})
                            await cpio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else:
                            user_flag_5005[user_id] = time.time()
                            await cpio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        await cpio.emit('session_request', {'session_id':idss})
                        await cpio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared.
                        user_flag_5005[user_id] = time.time()


            elif socket_in_use[user_id] == '95':
                print("THIS IS INSIDE SOCKET 95")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            await cqio.emit('session_request', {'session_id':idss})
                            await cqio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else:
                            user_flag_5005[user_id] = time.time()
                            await cqio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        await cqio.emit('session_request', {'session_id':idss})
                        await cqio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared.
                        user_flag_5005[user_id] = time.time()


            elif socket_in_use[user_id] == '96':
                print("THIS IS INSIDE SOCKET 96")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            await crio.emit('session_request', {'session_id':idss})
                            await crio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else:
                            user_flag_5005[user_id] = time.time()
                            await crio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        await crio.emit('session_request', {'session_id':idss})
                        await crio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared.
                        user_flag_5005[user_id] = time.time()


            elif socket_in_use[user_id] == '97':
                print("THIS IS INSIDE SOCKET 97")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            await csio.emit('session_request', {'session_id':idss})
                            await csio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else:
                            user_flag_5005[user_id] = time.time()
                            await csio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        await csio.emit('session_request', {'session_id':idss})
                        await csio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared.
                        user_flag_5005[user_id] = time.time()


            elif socket_in_use[user_id] == '98':
                print("THIS IS INSIDE SOCKET 98")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            await ctio.emit('session_request', {'session_id':idss})
                            await ctio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else:
                            user_flag_5005[user_id] = time.time()
                            await ctio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        await ctio.emit('session_request', {'session_id':idss})
                        await ctio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared.
                        user_flag_5005[user_id] = time.time()


            elif socket_in_use[user_id] == '99':
                print("THIS IS INSIDE SOCKET 99")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            await cuio.emit('session_request', {'session_id':idss})
                            await cuio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else:
                            user_flag_5005[user_id] = time.time()
                            await cuio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        await cuio.emit('session_request', {'session_id':idss})
                        await cuio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared.
                        user_flag_5005[user_id] = time.time()


            elif socket_in_use[user_id] == '100':
                print("THIS IS INSIDE SOCKET 100")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            await cvio.emit('session_request', {'session_id':idss})
                            await cvio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else:
                            user_flag_5005[user_id] = time.time()
                            await cvio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        await cvio.emit('session_request', {'session_id':idss})
                        await cvio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared.
                        user_flag_5005[user_id] = time.time()


            elif socket_in_use[user_id] == '101':
                print("THIS IS INSIDE SOCKET 101")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            await cwio.emit('session_request', {'session_id':idss})
                            await cwio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else:
                            user_flag_5005[user_id] = time.time()
                            await cwio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        await cwio.emit('session_request', {'session_id':idss})
                        await cwio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared.
                        user_flag_5005[user_id] = time.time()


            elif socket_in_use[user_id] == '102':
                print("THIS IS INSIDE SOCKET 102")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            await cxio.emit('session_request', {'session_id':idss})
                            await cxio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else:
                            user_flag_5005[user_id] = time.time()
                            await cxio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        await cxio.emit('session_request', {'session_id':idss})
                        await cxio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared.
                        user_flag_5005[user_id] = time.time()


            elif socket_in_use[user_id] == '103':
                print("THIS IS INSIDE SOCKET 103")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            await cyio.emit('session_request', {'session_id':idss})
                            await cyio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else:
                            user_flag_5005[user_id] = time.time()
                            await cyio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        await cyio.emit('session_request', {'session_id':idss})
                        await cyio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared.
                        user_flag_5005[user_id] = time.time()


            elif socket_in_use[user_id] == '104':
                print("THIS IS INSIDE SOCKET 104")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            await czio.emit('session_request', {'session_id':idss})
                            await czio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else:
                            user_flag_5005[user_id] = time.time()
                            await czio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        await czio.emit('session_request', {'session_id':idss})
                        await czio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared.
                        user_flag_5005[user_id] = time.time()

            #----d

            elif socket_in_use[user_id] == '105':
                print("THIS IS INSIDE SOCKET 105")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            await daio.emit('session_request', {'session_id':idss})
                            await daio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else:
                            user_flag_5005[user_id] = time.time()
                            await daio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        await daio.emit('session_request', {'session_id':idss})
                        await daio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared.
                        user_flag_5005[user_id] = time.time()


            elif socket_in_use[user_id] == '106':
                print("THIS IS INSIDE SOCKET 106")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            await dbio.emit('session_request', {'session_id':idss})
                            await dbio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else:
                            user_flag_5005[user_id] = time.time()
                            await dbio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        await dbio.emit('session_request', {'session_id':idss})
                        await dbio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared.
                        user_flag_5005[user_id] = time.time()


            elif socket_in_use[user_id] == '107':
                print("THIS IS INSIDE SOCKET 107")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            await dcio.emit('session_request', {'session_id':idss})
                            await dcio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else:
                            user_flag_5005[user_id] = time.time()
                            await dcio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        await dcio.emit('session_request', {'session_id':idss})
                        await dcio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared.
                        user_flag_5005[user_id] = time.time()


            elif socket_in_use[user_id] == '108':
                print("THIS IS INSIDE SOCKET 108")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            await ddio.emit('session_request', {'session_id':idss})
                            await ddio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else:
                            user_flag_5005[user_id] = time.time()
                            await ddio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        await ddio.emit('session_request', {'session_id':idss})
                        await ddio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared.
                        user_flag_5005[user_id] = time.time()


            elif socket_in_use[user_id] == '109':
                print("THIS IS INSIDE SOCKET 109")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            await deio.emit('session_request', {'session_id':idss})
                            await deio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else:
                            user_flag_5005[user_id] = time.time()
                            await deio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        await deio.emit('session_request', {'session_id':idss})
                        await deio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared.
                        user_flag_5005[user_id] = time.time()


            elif socket_in_use[user_id] == '110':
                print("THIS IS INSIDE SOCKET 110")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            await dfio.emit('session_request', {'session_id':idss})
                            await dfio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else:
                            user_flag_5005[user_id] = time.time()
                            await dfio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        await dfio.emit('session_request', {'session_id':idss})
                        await dfio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared.
                        user_flag_5005[user_id] = time.time()


            elif socket_in_use[user_id] == '111':
                print("THIS IS INSIDE SOCKET 111")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            await dgio.emit('session_request', {'session_id':idss})
                            await dgio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else:
                            user_flag_5005[user_id] = time.time()
                            await dgio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        await dgio.emit('session_request', {'session_id':idss})
                        await dgio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared.
                        user_flag_5005[user_id] = time.time()


            elif socket_in_use[user_id] == '112':
                print("THIS IS INSIDE SOCKET 112")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            await dhio.emit('session_request', {'session_id':idss})
                            await dhio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else:
                            user_flag_5005[user_id] = time.time()
                            await dhio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        await dhio.emit('session_request', {'session_id':idss})
                        await dhio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared.
                        user_flag_5005[user_id] = time.time()


            elif socket_in_use[user_id] == '113':
                print("THIS IS INSIDE SOCKET 113")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            await diio.emit('session_request', {'session_id':idss})
                            await diio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else:
                            user_flag_5005[user_id] = time.time()
                            await diio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        await diio.emit('session_request', {'session_id':idss})
                        await diio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared.
                        user_flag_5005[user_id] = time.time()


            elif socket_in_use[user_id] == '114':
                print("THIS IS INSIDE SOCKET 114")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            await djio.emit('session_request', {'session_id':idss})
                            await djio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else:
                            user_flag_5005[user_id] = time.time()
                            await djio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        await djio.emit('session_request', {'session_id':idss})
                        await djio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared.
                        user_flag_5005[user_id] = time.time()


            elif socket_in_use[user_id] == '115':
                print("THIS IS INSIDE SOCKET 115")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            await dkio.emit('session_request', {'session_id':idss})
                            await dkio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else:
                            user_flag_5005[user_id] = time.time()
                            await dkio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        await dkio.emit('session_request', {'session_id':idss})
                        await dkio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared.
                        user_flag_5005[user_id] = time.time()


            elif socket_in_use[user_id] == '116':
                print("THIS IS INSIDE SOCKET 116")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            await dlio.emit('session_request', {'session_id':idss})
                            await dlio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else:
                            user_flag_5005[user_id] = time.time()
                            await dlio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        await dlio.emit('session_request', {'session_id':idss})
                        await dlio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared.
                        user_flag_5005[user_id] = time.time()


            elif socket_in_use[user_id] == '117':
                print("THIS IS INSIDE SOCKET 117")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            await dmio.emit('session_request', {'session_id':idss})
                            await dmio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else:
                            user_flag_5005[user_id] = time.time()
                            await dmio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        await dmio.emit('session_request', {'session_id':idss})
                        await dmio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared.
                        user_flag_5005[user_id] = time.time()


            elif socket_in_use[user_id] == '118':
                print("THIS IS INSIDE SOCKET 118")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            await dnio.emit('session_request', {'session_id':idss})
                            await dnio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else:
                            user_flag_5005[user_id] = time.time()
                            await dnio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        await dnio.emit('session_request', {'session_id':idss})
                        await dnio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared.
                        user_flag_5005[user_id] = time.time()


            elif socket_in_use[user_id] == '119':
                print("THIS IS INSIDE SOCKET 119")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            await doio.emit('session_request', {'session_id':idss})
                            await doio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else:
                            user_flag_5005[user_id] = time.time()
                            await doio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        await doio.emit('session_request', {'session_id':idss})
                        await doio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared.
                        user_flag_5005[user_id] = time.time()


            elif socket_in_use[user_id] == '120':
                print("THIS IS INSIDE SOCKET 120")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            await dpio.emit('session_request', {'session_id':idss})
                            await dpio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else:
                            user_flag_5005[user_id] = time.time()
                            await dpio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        await dpio.emit('session_request', {'session_id':idss})
                        await dpio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared.
                        user_flag_5005[user_id] = time.time()


            elif socket_in_use[user_id] == '121':
                print("THIS IS INSIDE SOCKET 121")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            await dqio.emit('session_request', {'session_id':idss})
                            await dqio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else:
                            user_flag_5005[user_id] = time.time()
                            await dqio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        await dqio.emit('session_request', {'session_id':idss})
                        await dqio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared.
                        user_flag_5005[user_id] = time.time()


            elif socket_in_use[user_id] == '122':
                print("THIS IS INSIDE SOCKET 122")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            await drio.emit('session_request', {'session_id':idss})
                            await drio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else:
                            user_flag_5005[user_id] = time.time()
                            await drio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        await drio.emit('session_request', {'session_id':idss})
                        await drio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared.
                        user_flag_5005[user_id] = time.time()


            elif socket_in_use[user_id] == '123':
                print("THIS IS INSIDE SOCKET 123")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            await dsio.emit('session_request', {'session_id':idss})
                            await dsio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else:
                            user_flag_5005[user_id] = time.time()
                            await dsio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        await dsio.emit('session_request', {'session_id':idss})
                        await dsio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared.
                        user_flag_5005[user_id] = time.time()


            elif socket_in_use[user_id] == '124':
                print("THIS IS INSIDE SOCKET 124")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            await dtio.emit('session_request', {'session_id':idss})
                            await dtio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else:
                            user_flag_5005[user_id] = time.time()
                            await dtio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        await dtio.emit('session_request', {'session_id':idss})
                        await dtio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared.
                        user_flag_5005[user_id] = time.time()


            elif socket_in_use[user_id] == '125':
                print("THIS IS INSIDE SOCKET 125")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            await duio.emit('session_request', {'session_id':idss})
                            await duio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else:
                            user_flag_5005[user_id] = time.time()
                            await duio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        await duio.emit('session_request', {'session_id':idss})
                        await duio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared.
                        user_flag_5005[user_id] = time.time()


            elif socket_in_use[user_id] == '126':
                print("THIS IS INSIDE SOCKET 126")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            await dvio.emit('session_request', {'session_id':idss})
                            await dvio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else:
                            user_flag_5005[user_id] = time.time()
                            await dvio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        await dvio.emit('session_request', {'session_id':idss})
                        await dvio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared.
                        user_flag_5005[user_id] = time.time()


            elif socket_in_use[user_id] == '127':
                print("THIS IS INSIDE SOCKET 127")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            await dwio.emit('session_request', {'session_id':idss})
                            await dwio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else:
                            user_flag_5005[user_id] = time.time()
                            await dwio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        await dwio.emit('session_request', {'session_id':idss})
                        await dwio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared.
                        user_flag_5005[user_id] = time.time()


            elif socket_in_use[user_id] == '128':
                print("THIS IS INSIDE SOCKET 128")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            await dxio.emit('session_request', {'session_id':idss})
                            await dxio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else:
                            user_flag_5005[user_id] = time.time()
                            await dxio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        await dxio.emit('session_request', {'session_id':idss})
                        await dxio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared.
                        user_flag_5005[user_id] = time.time()


            elif socket_in_use[user_id] == '129':
                print("THIS IS INSIDE SOCKET 129")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            await dyio.emit('session_request', {'session_id':idss})
                            await dyio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else:
                            user_flag_5005[user_id] = time.time()
                            await dyio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        await dyio.emit('session_request', {'session_id':idss})
                        await dyio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared.
                        user_flag_5005[user_id] = time.time()


            elif socket_in_use[user_id] == '130':
                print("THIS IS INSIDE SOCKET 130")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            await dzio.emit('session_request', {'session_id':idss})
                            await dzio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else:
                            user_flag_5005[user_id] = time.time()
                            await dzio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        await dzio.emit('session_request', {'session_id':idss})
                        await dzio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared.
                        user_flag_5005[user_id] = time.time()

            #----e

            elif socket_in_use[user_id] == '131': 
                print("THIS IS INSIDE SOCKET 131")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            await eaio.emit('session_request', {'session_id':idss})
                            await eaio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else:
                            user_flag_5005[user_id] = time.time()
                            await eaio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        await eaio.emit('session_request', {'session_id':idss})
                        await eaio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared.
                        user_flag_5005[user_id] = time.time()


            elif socket_in_use[user_id] == '132':
                print("THIS IS INSIDE SOCKET 132")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            await ebio.emit('session_request', {'session_id':idss})
                            await ebio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else:
                            user_flag_5005[user_id] = time.time()
                            await ebio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        await ebio.emit('session_request', {'session_id':idss})
                        await ebio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared.
                        user_flag_5005[user_id] = time.time()


            elif socket_in_use[user_id] == '133':
                print("THIS IS INSIDE SOCKET 133")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            await ecio.emit('session_request', {'session_id':idss})
                            await ecio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else:
                            user_flag_5005[user_id] = time.time()
                            await ecio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        await ecio.emit('session_request', {'session_id':idss})
                        await ecio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared.
                        user_flag_5005[user_id] = time.time()


            elif socket_in_use[user_id] == '134':
                print("THIS IS INSIDE SOCKET 134")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            await edio.emit('session_request', {'session_id':idss})
                            await edio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else:
                            user_flag_5005[user_id] = time.time()
                            await edio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        await edio.emit('session_request', {'session_id':idss})
                        await edio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared.
                        user_flag_5005[user_id] = time.time()


            elif socket_in_use[user_id] == '135':
                print("THIS IS INSIDE SOCKET 135")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            await eeio.emit('session_request', {'session_id':idss})
                            await eeio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else:
                            user_flag_5005[user_id] = time.time()
                            await eeio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        await eeio.emit('session_request', {'session_id':idss})
                        await eeio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared.
                        user_flag_5005[user_id] = time.time()


            elif socket_in_use[user_id] == '136':
                print("THIS IS INSIDE SOCKET 136")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            await efio.emit('session_request', {'session_id':idss})
                            await efio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else:
                            user_flag_5005[user_id] = time.time()
                            await efio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        await efio.emit('session_request', {'session_id':idss})
                        await efio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared.
                        user_flag_5005[user_id] = time.time()


            elif socket_in_use[user_id] == '137':
                print("THIS IS INSIDE SOCKET 137")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            await egio.emit('session_request', {'session_id':idss})
                            await egio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else:
                            user_flag_5005[user_id] = time.time()
                            await egio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        await egio.emit('session_request', {'session_id':idss})
                        await egio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared.
                        user_flag_5005[user_id] = time.time()


            elif socket_in_use[user_id] == '138':
                print("THIS IS INSIDE SOCKET 138")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            await ehio.emit('session_request', {'session_id':idss})
                            await ehio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else:
                            user_flag_5005[user_id] = time.time()
                            await ehio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        await ehio.emit('session_request', {'session_id':idss})
                        await ehio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared.
                        user_flag_5005[user_id] = time.time()


            elif socket_in_use[user_id] == '139':
                print("THIS IS INSIDE SOCKET 139")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            await eiio.emit('session_request', {'session_id':idss})
                            await eiio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else:
                            user_flag_5005[user_id] = time.time()
                            await eiio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        await eiio.emit('session_request', {'session_id':idss})
                        await eiio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared.
                        user_flag_5005[user_id] = time.time()


            elif socket_in_use[user_id] == '140':
                print("THIS IS INSIDE SOCKET 140")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            await ejio.emit('session_request', {'session_id':idss})
                            await ejio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else:
                            user_flag_5005[user_id] = time.time()
                            await ejio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        await ejio.emit('session_request', {'session_id':idss})
                        await ejio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared.
                        user_flag_5005[user_id] = time.time()


            elif socket_in_use[user_id] == '141':
                print("THIS IS INSIDE SOCKET 141")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            await ekio.emit('session_request', {'session_id':idss})
                            await ekio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else:
                            user_flag_5005[user_id] = time.time()
                            await ekio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        await ekio.emit('session_request', {'session_id':idss})
                        await ekio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared.
                        user_flag_5005[user_id] = time.time()


            elif socket_in_use[user_id] == '142':
                print("THIS IS INSIDE SOCKET 142")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            await elio.emit('session_request', {'session_id':idss})
                            await elio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else:
                            user_flag_5005[user_id] = time.time()
                            await elio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        await elio.emit('session_request', {'session_id':idss})
                        await elio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared.
                        user_flag_5005[user_id] = time.time()


            elif socket_in_use[user_id] == '143':
                print("THIS IS INSIDE SOCKET 143")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            await emio.emit('session_request', {'session_id':idss})
                            await emio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else:
                            user_flag_5005[user_id] = time.time()
                            await emio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        await emio.emit('session_request', {'session_id':idss})
                        await emio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared.
                        user_flag_5005[user_id] = time.time()


            elif socket_in_use[user_id] == '144':
                print("THIS IS INSIDE SOCKET 144")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            await enio.emit('session_request', {'session_id':idss})
                            await enio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else:
                            user_flag_5005[user_id] = time.time()
                            await enio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        await enio.emit('session_request', {'session_id':idss})
                        await enio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared.
                        user_flag_5005[user_id] = time.time()


            elif socket_in_use[user_id] == '145':
                print("THIS IS INSIDE SOCKET 145")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            await eoio.emit('session_request', {'session_id':idss})
                            await eoio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else:
                            user_flag_5005[user_id] = time.time()
                            await eoio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        await eoio.emit('session_request', {'session_id':idss})
                        await eoio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared.
                        user_flag_5005[user_id] = time.time()


            elif socket_in_use[user_id] == '146':
                print("THIS IS INSIDE SOCKET 146")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            await epio.emit('session_request', {'session_id':idss})
                            await epio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else:
                            user_flag_5005[user_id] = time.time()
                            await epio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        await epio.emit('session_request', {'session_id':idss})
                        await epio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared.
                        user_flag_5005[user_id] = time.time()


            elif socket_in_use[user_id] == '147':
                print("THIS IS INSIDE SOCKET 147")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            await eqio.emit('session_request', {'session_id':idss})
                            await eqio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else:
                            user_flag_5005[user_id] = time.time()
                            await eqio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        await eqio.emit('session_request', {'session_id':idss})
                        await eqio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared.
                        user_flag_5005[user_id] = time.time()


            elif socket_in_use[user_id] == '148':
                print("THIS IS INSIDE SOCKET 148")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            await erio.emit('session_request', {'session_id':idss})
                            await erio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else:
                            user_flag_5005[user_id] = time.time()
                            await erio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        await erio.emit('session_request', {'session_id':idss})
                        await erio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared.
                        user_flag_5005[user_id] = time.time()


            elif socket_in_use[user_id] == '149':
                print("THIS IS INSIDE SOCKET 149")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            await esio.emit('session_request', {'session_id':idss})
                            await esio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else:
                            user_flag_5005[user_id] = time.time()
                            await esio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        await esio.emit('session_request', {'session_id':idss})
                        await esio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared.
                        user_flag_5005[user_id] = time.time()


            elif socket_in_use[user_id] == '150':
                print("THIS IS INSIDE SOCKET 150")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            await etio.emit('session_request', {'session_id':idss})
                            await etio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else:
                            user_flag_5005[user_id] = time.time()
                            await etio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        await etio.emit('session_request', {'session_id':idss})
                        await etio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared.
                        user_flag_5005[user_id] = time.time()


            elif socket_in_use[user_id] == '151':
                print("THIS IS INSIDE SOCKET 151")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            await euio.emit('session_request', {'session_id':idss})
                            await euio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else:
                            user_flag_5005[user_id] = time.time()
                            await euio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        await euio.emit('session_request', {'session_id':idss})
                        await euio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared.
                        user_flag_5005[user_id] = time.time()


            elif socket_in_use[user_id] == '152':
                print("THIS IS INSIDE SOCKET 152")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            await evio.emit('session_request', {'session_id':idss})
                            await evio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else:
                            user_flag_5005[user_id] = time.time()
                            await evio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        await evio.emit('session_request', {'session_id':idss})
                        await evio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared.
                        user_flag_5005[user_id] = time.time()


            elif socket_in_use[user_id] == '153':
                print("THIS IS INSIDE SOCKET 153")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            await ewio.emit('session_request', {'session_id':idss})
                            await ewio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else:
                            user_flag_5005[user_id] = time.time()
                            await ewio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        await ewio.emit('session_request', {'session_id':idss})
                        await ewio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared.
                        user_flag_5005[user_id] = time.time()


            elif socket_in_use[user_id] == '154':
                print("THIS IS INSIDE SOCKET 154")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            await exio.emit('session_request', {'session_id':idss})
                            await exio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else:
                            user_flag_5005[user_id] = time.time()
                            await exio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        await exio.emit('session_request', {'session_id':idss})
                        await exio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared.
                        user_flag_5005[user_id] = time.time()


            elif socket_in_use[user_id] == '155':
                print("THIS IS INSIDE SOCKET 155")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            await eyio.emit('session_request', {'session_id':idss})
                            await eyio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else:
                            user_flag_5005[user_id] = time.time()
                            await eyio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        await eyio.emit('session_request', {'session_id':idss})
                        await eyio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared.
                        user_flag_5005[user_id] = time.time()


            elif socket_in_use[user_id] == '156':
                print("THIS IS INSIDE SOCKET 156")

                print("THIS IS SOCK_FLAG ", sock_flag, 'and this is sock items ', sock_flag.items())
                sock_flag[user_id] = '5005'

                if sock_flag[user_id] == '5005': # and 'menu' not in text and 'raise ticket' not in text:
                    #print("THIS IS INSIDE 5005")
                    if user_id in user_flag_5005.items(): #to check if ongoing conneciton has exceeded 5 mins. IF yes, then issue a new session.
                        if time.time() - user_flag_5005[user_id] >300:
                            user_flag_5005[user_id] = time.time()
                            await ezio.emit('session_request', {'session_id':idss})
                            await ezio.emit('user_uttered',{'session_id':idss,
                                'meessage' : text,
                                'metadata' : {'unique_name': unique_email},
                            })
                        else:
                            user_flag_5005[user_id] = time.time()
                            await ezio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                            })
                    else:
                        await ezio.emit('session_request', {'session_id':idss})
                        await ezio.emit('user_uttered',{'session_id':idss,
                            'message' : text,
                            'metadata' : {'unique_name': unique_email},
                        })
                        # user_id.append(id)  # this list will grow indefinetly unless records are taken into DB and this list is cleared.
                        user_flag_5005[user_id] = time.time()

        except AssertionError as error:
            print(error)
            print("BIG ERROR ")


        # 9abc8def7ghi6klmAAD
        # await sio.sleep(5)
        # @sio.on('bot_uttered')
        # async def message(data):
        #     print("THis is the reponse ", data['text'])
        #     return await turn_context.send_activity(data['text'])
        self._add_conversation_reference(turn_context.activity)
        return None 
        # await turn_context.send_activity(
        #     f""
        # )

    async def left_over_sock(self):

        try:
            if time.time() - list(socket_1.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 1 ", socket_1 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(1)
                del socket_in_use[list(socket_1.keys())[0]]
                socket_1.clear()
                await aio.disconnect()
                # sio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await aio.connect('http://localhost:5005/socket.io')
                print("TIME IS SOCKET 1 NOW ", socket_1)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
        except:
            print("SOCKET 1 clear")
        
        try:
            if time.time() - list(socket_2.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 2 ", socket_2 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(2)
                del socket_in_use[list(socket_2.keys())[0]]
                socket_2.clear()
                await bio.disconnect()
                # sio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await bio.connect('http://localhost:5005/socket.io')
                print("TIME IS SOCKET 2 NOW ", socket_2)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
        except:
            print("SOCKET 1 clear")

        try:
            if time.time() - list(socket_3.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 3 ", socket_3 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(3)
                del socket_in_use[list(socket_3.keys())[0]]
                socket_3.clear()
                await cio.disconnect()
                # sio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await cio.connect('http://localhost:5005/socket.io')
                print("TIME IS SOCKET 3 NOW ", socket_3)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
        except:
            print("SOCKET 3 clear")

        try:
            if time.time() - list(socket_4.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 4 ", socket_4 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(4)
                del socket_in_use[list(socket_4.keys())[0]]
                socket_4.clear()
                await dio.disconnect()
                # sio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await dio.connect('http://localhost:5005/socket.io')
                print("TIME IS SOCKET 4 NOW ", socket_4)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
        except:
            print("SOCKET 4 clear")

        try:
            if time.time() - list(socket_5.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 5 ", socket_5 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(5)
                del socket_in_use[list(socket_5.keys())[0]]
                socket_5.clear()
                await eio.disconnect()
                # sio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await eio.connect('http://localhost:5005/socket.io')
                print("TIME IS SOCKET 5 NOW ", socket_5)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
        except:
            print("SOCKET 5 clear")


        try:
            if time.time() - list(socket_6.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 6 ", socket_6 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(6)
                del socket_in_use[list(socket_6.keys())[0]]
                socket_6.clear()
                await fio.disconnect()
                # sio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await fio.connect('http://localhost:5005/socket.io')
                print("TIME IS SOCKET 6 NOW ", socket_6)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
        except:
            print("SOCKET 6 clear")
        try:
            if time.time() - list(socket_7.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 7 ", socket_7 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(7)
                del socket_in_use[list(socket_7.keys())[0]]
                socket_7.clear()
                print("TIME IS SOCKET 7 NOW ", socket_7)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await gio.disconnect()
                await asyncio.sleep(0.1)
                await gio.connect('http://localhost:5005/socket.io')
        except: 
            print("SOCKET 7 clear")
        try:
            if time.time() - list(socket_8.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 8 ", socket_8 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(8)
                del socket_in_use[list(socket_8.keys())[0]]
                socket_8.clear()
                print("TIME IS SOCKET 8 NOW ", socket_8)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await hio.disconnect()
                # usio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await hio.connect('http://localhost:5005/socket.io')
        except: 
            print("SOCKET 8 clear")
        try:
            if time.time() - list(socket_9.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 9 ", socket_9 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(9)
                del socket_in_use[list(socket_9.keys())[0]]
                socket_9.clear()
                print("TIME IS SOCKET 9 NOW ", socket_9)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await iio.disconnect()
            # vsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await iio.connect('http://localhost:5005/socket.io')
        except: 
            print("SOCKET 9 clear")
        try:
            if time.time() - list(socket_10.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 10 ", socket_10 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(10)
                del socket_in_use[list(socket_10.keys())[0]]
                socket_10.clear()
                print("TIME IS SOCKET 10 NOW ", socket_10)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await jio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await jio.connect('http://localhost:5005/socket.io')
        except: 
            print("SOCKET 10 clear")

        try:
            if time.time() - list(socket_11.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 11 ", socket_11 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(11)
                del socket_in_use[list(socket_11.keys())[0]]
                socket_11.clear()
                print("TIME IS SOCKET 11 NOW ", socket_11)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await kio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await kio.connect('http://localhost:5005/socket.io')
        except: 
            print("SOCKET 11 clear")

        try:
            if time.time() - list(socket_12.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 12 ", socket_12 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(12)
                del socket_in_use[list(socket_12.keys())[0]]
                socket_12.clear()
                print("TIME IS SOCKET 12 NOW ", socket_12)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await lio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await lio.connect('http://localhost:5005/socket.io')
        except: 
            print("SOCKET 12 clear")

        try:
            if time.time() - list(socket_13.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 13 ", socket_13 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(13)
                del socket_in_use[list(socket_13.keys())[0]]
                socket_13.clear()
                print("TIME IS SOCKET 13 NOW ", socket_13)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await mio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await mio.connect('http://localhost:5005/socket.io')
        except: 
            print("SOCKET 13 clear")

        try:
            if time.time() - list(socket_14.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 14 ", socket_14 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(14)
                del socket_in_use[list(socket_14.keys())[0]]
                socket_14.clear()
                print("TIME IS SOCKET 14 NOW ", socket_14)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await nio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await nio.connect('http://localhost:5005/socket.io')
        except: 
            print("SOCKET 14 clear")

        try:
            if time.time() - list(socket_15.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 15 ", socket_15 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(15)
                del socket_in_use[list(socket_15.keys())[0]]
                socket_15.clear()
                print("TIME IS SOCKET 15 NOW ", socket_15)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await oio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await oio.connect('http://localhost:5005/socket.io')
        except: 
            print("SOCKET 15 clear")

        try:
            if time.time() - list(socket_16.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 16 ", socket_16 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(16)
                del socket_in_use[list(socket_16.keys())[0]]
                socket_16.clear()
                print("TIME IS SOCKET 16 NOW ", socket_16)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await pio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await pio.connect('http://localhost:5005/socket.io')
        except: 
            print("SOCKET 16 clear")

        try:
            if time.time() - list(socket_17.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 17 ", socket_17 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(17)
                del socket_in_use[list(socket_17.keys())[0]]
                socket_17.clear()
                print("TIME IS SOCKET 17 NOW ", socket_17)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await qio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await qio.connect('http://localhost:5005/socket.io')
        except: 
            print("SOCKET 17 clear")

        try:
            if time.time() - list(socket_18.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 18 ", socket_18 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(18)
                del socket_in_use[list(socket_18.keys())[0]]
                socket_18.clear()
                print("TIME IS SOCKET 18 NOW ", socket_18)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await rio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await rio.connect('http://localhost:5005/socket.io')
        except: 
            print("SOCKET 18 clear")

        try:
            if time.time() - list(socket_19.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 19 ", socket_19 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(19)
                del socket_in_use[list(socket_19.keys())[0]]
                socket_19.clear()
                print("TIME IS SOCKET 19 NOW ", socket_19)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await sio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await sio.connect('http://localhost:5005/socket.io')
        except: 
            print("SOCKET 19 clear")

        try:
            if time.time() - list(socket_20.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 20 ", socket_20 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(20)
                del socket_in_use[list(socket_20.keys())[0]]
                socket_20.clear()
                print("TIME IS SOCKET 20 NOW ", socket_20)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await tsio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await tsio.connect('http://localhost:5005/socket.io')
        except: 
            print("SOCKET 20 clear")

        try:
            if time.time() - list(socket_21.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 21 ", socket_21 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(21)
                del socket_in_use[list(socket_21.keys())[0]]
                socket_21.clear()
                print("TIME IS SOCKET 21 NOW ", socket_21)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await usio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await usio.connect('http://localhost:5005/socket.io')
        except: 
            print("SOCKET 21 clear")

        try:
            if time.time() - list(socket_22.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 22 ", socket_22 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(22)
                del socket_in_use[list(socket_22.keys())[0]]
                socket_22.clear()
                print("TIME IS SOCKET 22 NOW ", socket_22)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await vsio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await vsio.connect('http://localhost:5005/socket.io')
        except: 
            print("SOCKET 22 clear")

        try:
            if time.time() - list(socket_23.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 23 ", socket_23 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(23)
                del socket_in_use[list(socket_23.keys())[0]]
                socket_23.clear()
                print("TIME IS SOCKET 23 NOW ", socket_23)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await wsio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await wsio.connect('http://localhost:5005/socket.io')
        except: 
            print("SOCKET 23 clear")

        try:
            if time.time() - list(socket_24.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 24 ", socket_24 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(24)
                del socket_in_use[list(socket_24.keys())[0]]
                socket_24.clear()
                print("TIME IS SOCKET 24 NOW ", socket_24)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await xio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await xio.connect('http://localhost:5005/socket.io')
        except: 
            print("SOCKET 24 clear")

        try:
            if time.time() - list(socket_25.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 25 ", socket_25 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(25)
                del socket_in_use[list(socket_25.keys())[0]]
                socket_25.clear()
                print("TIME IS SOCKET 25 NOW ", socket_25)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await yio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await yio.connect('http://localhost:5005/socket.io')
        except: 
            print("SOCKET 25 clear")

        try:
            if time.time() - list(socket_26.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 26 ", socket_26 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(26)
                del socket_in_use[list(socket_26.keys())[0]]
                socket_26.clear()
                print("TIME IS SOCKET 26 NOW ", socket_26)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await zio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await zio.connect('http://localhost:5005/socket.io')
        except: 
            print("SOCKET 26 clear")

        #----
        try:
            if time.time() - list(socket_27.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 27 ", socket_27 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(27)
                del socket_in_use[list(socket_27.keys())[0]]
                socket_27.clear()
                await aaio.disconnect()
                # sio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await aaio.connect('http://localhost:5005/socket.io')
                print("TIME IS SOCKET 27 NOW ", socket_27)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
        except:
            print("SOCKET 27 clear")
        
        try:
            if time.time() - list(socket_28.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 28 ", socket_28 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(28)
                del socket_in_use[list(socket_28.keys())[0]]
                socket_28.clear()
                await abio.disconnect()
                # sio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await abio.connect('http://localhost:5005/socket.io')
                print("TIME IS SOCKET 28 NOW ", socket_28)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
        except:
            print("SOCKET 28 clear")

        try:
            if time.time() - list(socket_29.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 29 ", socket_29 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(29)
                del socket_in_use[list(socket_29.keys())[0]]
                socket_29.clear()
                await acio.disconnect()
                # sio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await acio.connect('http://localhost:5005/socket.io')
                print("TIME IS SOCKET 29 NOW ", socket_29)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
        except:
            print("SOCKET 29 clear")

        try:
            if time.time() - list(socket_30.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 30 ", socket_30 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(30)
                del socket_in_use[list(socket_30.keys())[0]]
                socket_30.clear()
                await adio.disconnect()
                # sio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await adio.connect('http://localhost:5005/socket.io')
                print("TIME IS SOCKET 30 NOW ", socket_30)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
        except:
            print("SOCKET 30 clear")

        try:
            if time.time() - list(socket_31.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 31 ", socket_31 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(31)
                del socket_in_use[list(socket_31.keys())[0]]
                socket_31.clear()
                await aeio.disconnect()
                # sio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await aeio.connect('http://localhost:5005/socket.io')
                print("TIME IS SOCKET 31 NOW ", socket_31)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
        except:
            print("SOCKET 31 clear")


        try:
            if time.time() - list(socket_32.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 32 ", socket_32 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(32)
                del socket_in_use[list(socket_32.keys())[0]]
                socket_32.clear()
                await afio.disconnect()
                # sio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await afio.connect('http://localhost:5005/socket.io')
                print("TIME IS SOCKET 32 NOW ", socket_32)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
        except:
            print("SOCKET 32 clear")
        try:
            if time.time() - list(socket_33.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 33 ", socket_33 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(33)
                del socket_in_use[list(socket_33.keys())[0]]
                socket_33.clear()
                print("TIME IS SOCKET 33 NOW ", socket_33)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await gio.disconnect()
                await asyncio.sleep(0.1)
                await gio.connect('http://localhost:5005/socket.io')
        except: 
            print("SOCKET 33 clear")
        try:
            if time.time() - list(socket_34.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 34 ", socket_34 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(34)
                del socket_in_use[list(socket_34.keys())[0]]
                socket_34.clear()
                print("TIME IS SOCKET 34 NOW ", socket_34)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await ahio.disconnect()
                # usio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await ahio.connect('http://localhost:5005/socket.io')
        except: 
            print("SOCKET 34 clear")
        try:
            if time.time() - list(socket_35.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 35 ", socket_35 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(35)
                del socket_in_use[list(socket_35.keys())[0]]
                socket_35.clear()
                print("TIME IS SOCKET 35 NOW ", socket_35)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await aiio.disconnect()
            # vsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await aiio.connect('http://localhost:5005/socket.io')
        except: 
            print("SOCKET 35 clear")
        try:
            if time.time() - list(socket_36.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 36 ", socket_36 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(36)
                del socket_in_use[list(socket_36.keys())[0]]
                socket_36.clear()
                print("TIME IS SOCKET 36 NOW ", socket_36)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await ajio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await ajio.connect('http://localhost:5005/socket.io')
        except: 
            print("SOCKET 36 clear")

        try:
            if time.time() - list(socket_37.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 11 ", socket_37 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(37)
                del socket_in_use[list(socket_37.keys())[0]]
                socket_37.clear()
                print("TIME IS SOCKET 37 NOW ", socket_11)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await akio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await akio.connect('http://localhost:5005/socket.io')
        except: 
            print("SOCKET 37 clear")

        try:
            if time.time() - list(socket_38.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 38 ", socket_38 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(38)
                del socket_in_use[list(socket_38.keys())[0]]
                socket_38.clear()
                print("TIME IS SOCKET 38 NOW ", socket_38)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await alio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await alio.connect('http://localhost:5005/socket.io')
        except: 
            print("SOCKET 38 clear")

        try:
            if time.time() - list(socket_39.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 39 ", socket_39 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(39)
                del socket_in_use[list(socket_39.keys())[0]]
                socket_39.clear()
                print("TIME IS SOCKET 39 NOW ", socket_39)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await amio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await amio.connect('http://localhost:5005/socket.io')
        except: 
            print("SOCKET 39 clear")

        try:
            if time.time() - list(socket_40.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 40 ", socket_40 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(40)
                del socket_in_use[list(socket_40.keys())[0]]
                socket_40.clear()
                print("TIME IS SOCKET 40 NOW ", socket_40)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await anio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await anio.connect('http://localhost:5005/socket.io')
        except: 
            print("SOCKET 40 clear")

        try:
            if time.time() - list(socket_41.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 41 ", socket_41 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(41)
                del socket_in_use[list(socket_41.keys())[0]]
                socket_41.clear()
                print("TIME IS SOCKET 41 NOW ", socket_41)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await aoio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await aoio.connect('http://localhost:5005/socket.io')
        except: 
            print("SOCKET 41 clear")

        try:
            if time.time() - list(socket_42.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 42 ", socket_42 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(42)
                del socket_in_use[list(socket_42.keys())[0]]
                socket_42.clear()
                print("TIME IS SOCKET 42 NOW ", socket_42)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await apio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await apio.connect('http://localhost:5005/socket.io')
        except: 
            print("SOCKET 42 clear")

        try:
            if time.time() - list(socket_43.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 43 ", socket_43 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(43)
                del socket_in_use[list(socket_43.keys())[0]]
                socket_43.clear()
                print("TIME IS SOCKET 17 NOW ", socket_43)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await aqio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await aqio.connect('http://localhost:5005/socket.io')
        except: 
            print("SOCKET 43 clear")

        try:
            if time.time() - list(socket_44.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 44 ", socket_44 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(44)
                del socket_in_use[list(socket_44.keys())[0]]
                socket_44.clear()
                print("TIME IS SOCKET 4 NOW ", socket_44)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await ario.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await ario.connect('http://localhost:5005/socket.io')
        except: 
            print("SOCKET 4 clear")

        try:
            if time.time() - list(socket_45.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 45 ", socket_45 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(45)
                del socket_in_use[list(socket_45.keys())[0]]
                socket_45.clear()
                print("TIME IS SOCKET 45 NOW ", socket_45)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await asio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await asio.connect('http://localhost:5005/socket.io')
        except: 
            print("SOCKET 45 clear")

        try:
            if time.time() - list(socket_46.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 46 ", socket_46 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(46)
                del socket_in_use[list(socket_46.keys())[0]]
                socket_46.clear()
                print("TIME IS SOCKET 46 NOW ", socket_46)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await atio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await atio.connect('http://localhost:5005/socket.io')
        except: 
            print("SOCKET 46 clear")

        try:
            if time.time() - list(socket_47.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 47 ", socket_47 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(47)
                del socket_in_use[list(socket_47.keys())[0]]
                socket_47.clear()
                print("TIME IS SOCKET 21 NOW ", socket_21)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await auio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await auio.connect('http://localhost:5005/socket.io')
        except: 
            print("SOCKET 47 clear")

        try:
            if time.time() - list(socket_48.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 48 ", socket_48 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(48)
                del socket_in_use[list(socket_48.keys())[0]]
                socket_48.clear()
                print("TIME IS SOCKET 48 NOW ", socket_48)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await avio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await avio.connect('http://localhost:5005/socket.io')
        except: 
            print("SOCKET 22 clear")

        try:
            if time.time() - list(socket_49.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 49 ", socket_49 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(49)
                del socket_in_use[list(socket_49.keys())[0]]
                socket_49.clear()
                print("TIME IS SOCKET 49 NOW ", socket_49)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await awio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await awio.connect('http://localhost:5005/socket.io')
        except: 
            print("SOCKET 49 clear")

        try:
            if time.time() - list(socket_50.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 50 ", socket_50 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(50)
                del socket_in_use[list(socket_50.keys())[0]]
                socket_50.clear()
                print("TIME IS SOCKET 50 NOW ", socket_50)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await axio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await axio.connect('http://localhost:5005/socket.io')
        except: 
            print("SOCKET 50 clear")

        try:
            if time.time() - list(socket_51.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 51 ", socket_51 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(51)
                del socket_in_use[list(socket_51.keys())[0]]
                socket_51.clear()
                print("TIME IS SOCKET 51 NOW ", socket_51)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await ayio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await ayio.connect('http://localhost:5005/socket.io')
        except: 
            print("SOCKET 51 clear")

        try:
            if time.time() - list(socket_52.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 52 ", socket_52 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(52)
                del socket_in_use[list(socket_52.keys())[0]]
                socket_52.clear()
                print("TIME IS SOCKET 52 NOW ", socket_52)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await azio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await azio.connect('http://localhost:5005/socket.io')
        except: 
            print("SOCKET 52 clear")

        #----b

        try:
            if time.time() - list(socket_53.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 53 ", socket_53 , time.time())    
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)       
                socket_in_use_list.remove(53)
                del socket_in_use[list(socket_53.keys())[0]]
                socket_53.clear()
                print("TIME IS SOCKET 53 NOW ", socket_53)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list) 
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)        
                await baio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await baio.connect('http://localhost:5005/socket.io')
        except:
            print("SOCKET socket_53 clear")


        try:
            if time.time() - list(socket_54.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 54 ", socket_54 , time.time())    
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)       
                socket_in_use_list.remove(54)
                del socket_in_use[list(socket_54.keys())[0]]
                socket_54.clear()
                print("TIME IS SOCKET 54 NOW ", socket_54)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await bbio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await bbio.connect('http://localhost:5005/socket.io')
        except:
            print("SOCKET socket_54 clear")


        try:
            if time.time() - list(socket_55.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 55 ", socket_55 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(55)
                del socket_in_use[list(socket_55.keys())[0]]
                socket_55.clear()
                print("TIME IS SOCKET 55 NOW ", socket_55)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await bcio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await bcio.connect('http://localhost:5005/socket.io')
        except:
            print("SOCKET socket_55 clear")


        try:
            if time.time() - list(socket_56.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 56 ", socket_56 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(56)
                del socket_in_use[list(socket_56.keys())[0]]
                socket_56.clear()
                print("TIME IS SOCKET 56 NOW ", socket_56)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await bdio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await bdio.connect('http://localhost:5005/socket.io')
        except:
            print("SOCKET socket_56 clear")


        try:
            if time.time() - list(socket_57.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 57 ", socket_57 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(57)
                del socket_in_use[list(socket_57.keys())[0]]
                socket_57.clear()
                print("TIME IS SOCKET 57 NOW ", socket_57)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await beio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await beio.connect('http://localhost:5005/socket.io')
        except:
            print("SOCKET socket_57 clear")


        try:
            if time.time() - list(socket_58.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 58 ", socket_58 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(58)
                del socket_in_use[list(socket_58.keys())[0]]
                socket_58.clear()
                print("TIME IS SOCKET 58 NOW ", socket_58)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await bfio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await bfio.connect('http://localhost:5005/socket.io')
        except:
            print("SOCKET socket_58 clear")


        try:
            if time.time() - list(socket_59.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 59 ", socket_59 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(59)
                del socket_in_use[list(socket_59.keys())[0]]
                socket_59.clear()
                print("TIME IS SOCKET 59 NOW ", socket_59)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await bgio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await bgio.connect('http://localhost:5005/socket.io')
        except:
            print("SOCKET socket_59 clear")


        try:
            if time.time() - list(socket_60.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 60 ", socket_60 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(60)
                del socket_in_use[list(socket_60.keys())[0]]
                socket_60.clear()
                print("TIME IS SOCKET 60 NOW ", socket_60)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await bhio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await bhio.connect('http://localhost:5005/socket.io')
        except:
            print("SOCKET socket_60 clear")


        try:
            if time.time() - list(socket_61.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 61 ", socket_61 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(61)
                del socket_in_use[list(socket_61.keys())[0]]
                socket_61.clear()
                print("TIME IS SOCKET 61 NOW ", socket_61)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await biio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await biio.connect('http://localhost:5005/socket.io')
        except:
            print("SOCKET socket_61 clear")


        try:
            if time.time() - list(socket_62.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 62 ", socket_62 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(62)
                del socket_in_use[list(socket_62.keys())[0]]
                socket_62.clear()
                print("TIME IS SOCKET 62 NOW ", socket_62)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await bjio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await bjio.connect('http://localhost:5005/socket.io')
        except:
            print("SOCKET socket_62 clear")


        try:
            if time.time() - list(socket_63.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 63 ", socket_63 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(63)
                del socket_in_use[list(socket_63.keys())[0]]
                socket_63.clear()
                print("TIME IS SOCKET 63 NOW ", socket_63)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await bkio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await bkio.connect('http://localhost:5005/socket.io')
        except:
            print("SOCKET socket_63 clear")


        try:
            if time.time() - list(socket_64.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 64 ", socket_64 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(64)
                del socket_in_use[list(socket_64.keys())[0]]
                socket_64.clear()
                print("TIME IS SOCKET 64 NOW ", socket_64)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await blio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await blio.connect('http://localhost:5005/socket.io')
        except:
            print("SOCKET socket_64 clear")


        try:
            if time.time() - list(socket_65.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 65 ", socket_65 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(65)
                del socket_in_use[list(socket_65.keys())[0]]
                socket_65.clear()
                print("TIME IS SOCKET 65 NOW ", socket_65)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await bmio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await bmio.connect('http://localhost:5005/socket.io')
        except:
            print("SOCKET socket_65 clear")


        try:
            if time.time() - list(socket_66.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 66 ", socket_66 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(66)
                del socket_in_use[list(socket_66.keys())[0]]
                socket_66.clear()
                print("TIME IS SOCKET 66 NOW ", socket_66)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await bnio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await bnio.connect('http://localhost:5005/socket.io')
        except:
            print("SOCKET socket_66 clear")


        try:
            if time.time() - list(socket_67.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 67 ", socket_67 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(67)
                del socket_in_use[list(socket_67.keys())[0]]
                socket_67.clear()
                print("TIME IS SOCKET 67 NOW ", socket_67)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await boio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await boio.connect('http://localhost:5005/socket.io')
        except:
            print("SOCKET socket_67 clear")


        try:
            if time.time() - list(socket_68.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 68 ", socket_68 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(68)
                del socket_in_use[list(socket_68.keys())[0]]
                socket_68.clear()
                print("TIME IS SOCKET 68 NOW ", socket_68)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await bpio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await bpio.connect('http://localhost:5005/socket.io')
        except:
            print("SOCKET socket_68 clear")


        try:
            if time.time() - list(socket_69.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 69 ", socket_69 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(69)
                del socket_in_use[list(socket_69.keys())[0]]
                socket_69.clear()
                print("TIME IS SOCKET 69 NOW ", socket_69)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await bqio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await bqio.connect('http://localhost:5005/socket.io')
        except:
            print("SOCKET socket_69 clear")


        try:
            if time.time() - list(socket_70.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 70 ", socket_70 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(70)
                del socket_in_use[list(socket_70.keys())[0]]
                socket_70.clear()
                print("TIME IS SOCKET 70 NOW ", socket_70)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await brio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await brio.connect('http://localhost:5005/socket.io')
        except:
            print("SOCKET socket_70 clear")


        try:
            if time.time() - list(socket_71.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 71 ", socket_71 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(71)
                del socket_in_use[list(socket_71.keys())[0]]
                socket_71.clear()
                print("TIME IS SOCKET 71 NOW ", socket_71)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await bsio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await bsio.connect('http://localhost:5005/socket.io')
        except:
            print("SOCKET socket_71 clear")


        try:
            if time.time() - list(socket_72.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 72 ", socket_72 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(72)
                del socket_in_use[list(socket_72.keys())[0]]
                socket_72.clear()
                print("TIME IS SOCKET 72 NOW ", socket_72)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await btio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await btio.connect('http://localhost:5005/socket.io')
        except:
            print("SOCKET socket_72 clear")


        try:
            if time.time() - list(socket_73.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 73 ", socket_73 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(73)
                del socket_in_use[list(socket_73.keys())[0]]
                socket_73.clear()
                print("TIME IS SOCKET 73 NOW ", socket_73)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await buio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await buio.connect('http://localhost:5005/socket.io')
        except:
            print("SOCKET socket_73 clear")


        try:
            if time.time() - list(socket_74.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 74 ", socket_74 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(74)
                del socket_in_use[list(socket_74.keys())[0]]
                socket_74.clear()
                print("TIME IS SOCKET 74 NOW ", socket_74)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await bvio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await bvio.connect('http://localhost:5005/socket.io')
        except:
            print("SOCKET socket_74 clear")


        try:
            if time.time() - list(socket_75.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 75 ", socket_75 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(75)
                del socket_in_use[list(socket_75.keys())[0]]
                socket_75.clear()
                print("TIME IS SOCKET 75 NOW ", socket_75)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await bwio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await bwio.connect('http://localhost:5005/socket.io')
        except:
            print("SOCKET socket_75 clear")


        try:
            if time.time() - list(socket_76.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 76 ", socket_76 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(76)
                del socket_in_use[list(socket_76.keys())[0]]
                socket_76.clear()
                print("TIME IS SOCKET 76 NOW ", socket_76)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await bxio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await bxio.connect('http://localhost:5005/socket.io')
        except:
            print("SOCKET socket_76 clear")


        try:
            if time.time() - list(socket_77.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 77 ", socket_77 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(77)
                del socket_in_use[list(socket_77.keys())[0]]
                socket_77.clear()
                print("TIME IS SOCKET 77 NOW ", socket_77)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await byio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await byio.connect('http://localhost:5005/socket.io')
        except:
            print("SOCKET socket_77 clear")


        try:
            if time.time() - list(socket_78.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 78 ", socket_78 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(78)
                del socket_in_use[list(socket_78.keys())[0]]
                socket_78.clear()
                print("TIME IS SOCKET 78 NOW ", socket_78)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await bzio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await bzio.connect('http://localhost:5005/socket.io')
        except:
            print("SOCKET socket_78 clear")

        #-----c
        try:
            if time.time() - list(socket_79.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 79 ", socket_79 , time.time())    
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)       
                socket_in_use_list.remove(79)
                del socket_in_use[list(socket_79.keys())[0]]
                socket_79.clear()
                print("TIME IS SOCKET 79 NOW ", socket_79)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await caio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await caio.connect('http://localhost:5005/socket.io')
        except:
            print("SOCKET socket_79 clear")


        try:
            if time.time() - list(socket_80.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 80 ", socket_80 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(80)
                del socket_in_use[list(socket_80.keys())[0]]
                socket_80.clear()
                print("TIME IS SOCKET 80 NOW ", socket_80)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await cbio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await cbio.connect('http://localhost:5005/socket.io')
        except:
            print("SOCKET socket_80 clear")


        try:
            if time.time() - list(socket_81.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 81 ", socket_81 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(81)
                del socket_in_use[list(socket_81.keys())[0]]
                socket_81.clear()
                print("TIME IS SOCKET 81 NOW ", socket_81)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await ccio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await ccio.connect('http://localhost:5005/socket.io')
        except:
            print("SOCKET socket_81 clear")


        try:
            if time.time() - list(socket_82.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 82 ", socket_82 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(82)
                del socket_in_use[list(socket_82.keys())[0]]
                socket_82.clear()
                print("TIME IS SOCKET 82 NOW ", socket_82)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await cdio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await cdio.connect('http://localhost:5005/socket.io')
        except:
            print("SOCKET socket_82 clear")


        try:
            if time.time() - list(socket_83.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 83 ", socket_83 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(83)
                del socket_in_use[list(socket_83.keys())[0]]
                socket_83.clear()
                print("TIME IS SOCKET 83 NOW ", socket_83)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await ceio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await ceio.connect('http://localhost:5005/socket.io')
        except:
            print("SOCKET socket_83 clear")


        try:
            if time.time() - list(socket_84.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 84 ", socket_84 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(84)
                del socket_in_use[list(socket_84.keys())[0]]
                socket_84.clear()
                print("TIME IS SOCKET 84 NOW ", socket_84)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await cfio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await cfio.connect('http://localhost:5005/socket.io')
        except:
            print("SOCKET socket_84 clear")


        try:
            if time.time() - list(socket_85.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 85 ", socket_85 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(85)
                del socket_in_use[list(socket_85.keys())[0]]
                socket_85.clear()
                print("TIME IS SOCKET 85 NOW ", socket_85)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await cgio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await cgio.connect('http://localhost:5005/socket.io')
        except:
            print("SOCKET socket_85 clear")


        try:
            if time.time() - list(socket_86.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 86 ", socket_86 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(86)
                del socket_in_use[list(socket_86.keys())[0]]
                socket_86.clear()
                print("TIME IS SOCKET 86 NOW ", socket_86)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await chio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await chio.connect('http://localhost:5005/socket.io')
        except:
            print("SOCKET socket_86 clear")


        try:
            if time.time() - list(socket_87.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 87 ", socket_87 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(87)
                del socket_in_use[list(socket_87.keys())[0]]
                socket_87.clear()
                print("TIME IS SOCKET 87 NOW ", socket_87)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await ciio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await ciio.connect('http://localhost:5005/socket.io')
        except:
            print("SOCKET socket_87 clear")


        try:
            if time.time() - list(socket_88.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 88 ", socket_88 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(88)
                del socket_in_use[list(socket_88.keys())[0]]
                socket_88.clear()
                print("TIME IS SOCKET 88 NOW ", socket_88)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await cjio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await cjio.connect('http://localhost:5005/socket.io')
        except:
            print("SOCKET socket_88 clear")


        try:
            if time.time() - list(socket_89.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 89 ", socket_89 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(89)
                del socket_in_use[list(socket_89.keys())[0]]
                socket_89.clear()
                print("TIME IS SOCKET 89 NOW ", socket_89)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await ckio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await ckio.connect('http://localhost:5005/socket.io')
        except:
            print("SOCKET socket_89 clear")


        try:
            if time.time() - list(socket_90.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 90 ", socket_90 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(90)
                del socket_in_use[list(socket_90.keys())[0]]
                socket_90.clear()
                print("TIME IS SOCKET 90 NOW ", socket_90)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await clio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await clio.connect('http://localhost:5005/socket.io')
        except:
            print("SOCKET socket_90 clear")


        try:
            if time.time() - list(socket_91.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 91 ", socket_91 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(91)
                del socket_in_use[list(socket_91.keys())[0]]
                socket_91.clear()
                print("TIME IS SOCKET 91 NOW ", socket_91)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await cmio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await cmio.connect('http://localhost:5005/socket.io')
        except:
            print("SOCKET socket_91 clear")


        try:
            if time.time() - list(socket_92.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 92 ", socket_92 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(92)
                del socket_in_use[list(socket_92.keys())[0]]
                socket_92.clear()
                print("TIME IS SOCKET 92 NOW ", socket_92)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await cnio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await cnio.connect('http://localhost:5005/socket.io')
        except:
            print("SOCKET socket_92 clear")


        try:
            if time.time() - list(socket_93.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 93 ", socket_93 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(93)
                del socket_in_use[list(socket_93.keys())[0]]
                socket_93.clear()
                print("TIME IS SOCKET 93 NOW ", socket_93)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await coio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await coio.connect('http://localhost:5005/socket.io')
        except:
            print("SOCKET socket_93 clear")


        try:
            if time.time() - list(socket_94.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 94 ", socket_94 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(94)
                del socket_in_use[list(socket_94.keys())[0]]
                socket_94.clear()
                print("TIME IS SOCKET 94 NOW ", socket_94)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await cpio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await cpio.connect('http://localhost:5005/socket.io')
        except:
            print("SOCKET socket_94 clear")


        try:
            if time.time() - list(socket_95.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 95 ", socket_95 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(95)
                del socket_in_use[list(socket_95.keys())[0]]
                socket_95.clear()
                print("TIME IS SOCKET 95 NOW ", socket_95)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await cqio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await cqio.connect('http://localhost:5005/socket.io')
        except:
            print("SOCKET socket_95 clear")


        try:
            if time.time() - list(socket_96.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 96 ", socket_96 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(96)
                del socket_in_use[list(socket_96.keys())[0]]
                socket_96.clear()
                print("TIME IS SOCKET 96 NOW ", socket_96)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await crio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await crio.connect('http://localhost:5005/socket.io')
        except:
            print("SOCKET socket_96 clear")


        try:
            if time.time() - list(socket_97.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 97 ", socket_97 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(97)
                del socket_in_use[list(socket_97.keys())[0]]
                socket_97.clear()
                print("TIME IS SOCKET 97 NOW ", socket_97)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await csio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await csio.connect('http://localhost:5005/socket.io')
        except:
            print("SOCKET socket_97 clear")


        try:
            if time.time() - list(socket_98.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 98 ", socket_98 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(98)
                del socket_in_use[list(socket_98.keys())[0]]
                socket_98.clear()
                print("TIME IS SOCKET 98 NOW ", socket_98)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await ctio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await ctio.connect('http://localhost:5005/socket.io')
        except:
            print("SOCKET socket_98 clear")


        try:
            if time.time() - list(socket_99.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 99 ", socket_99 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(99)
                del socket_in_use[list(socket_99.keys())[0]]
                socket_99.clear()
                print("TIME IS SOCKET 99 NOW ", socket_99)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await cuio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await cuio.connect('http://localhost:5005/socket.io')
        except:
            print("SOCKET socket_99 clear")


        try:
            if time.time() - list(socket_100.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 100 ", socket_100 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(100)
                del socket_in_use[list(socket_100.keys())[0]]
                socket_100.clear()
                print("TIME IS SOCKET 100 NOW ", socket_100)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await cvio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await cvio.connect('http://localhost:5005/socket.io')
        except:
            print("SOCKET socket_100 clear")


        try:
            if time.time() - list(socket_101.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 101 ", socket_101 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(101)
                del socket_in_use[list(socket_101.keys())[0]]
                socket_101.clear()
                print("TIME IS SOCKET 101 NOW ", socket_101)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await cwio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await cwio.connect('http://localhost:5005/socket.io')
        except:
            print("SOCKET socket_101 clear")


        try:
            if time.time() - list(socket_102.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 102 ", socket_102 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(102)
                del socket_in_use[list(socket_102.keys())[0]]
                socket_102.clear()
                print("TIME IS SOCKET 102 NOW ", socket_102)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await cxio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await cxio.connect('http://localhost:5005/socket.io')
        except:
            print("SOCKET socket_102 clear")


        try:
            if time.time() - list(socket_103.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 103 ", socket_103 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(103)
                del socket_in_use[list(socket_103.keys())[0]]
                socket_103.clear()
                print("TIME IS SOCKET 103 NOW ", socket_103)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await cyio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await cyio.connect('http://localhost:5005/socket.io')
        except:
            print("SOCKET socket_103 clear")


        try:
            if time.time() - list(socket_104.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 104 ", socket_104 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(104)
                del socket_in_use[list(socket_104.keys())[0]]
                socket_104.clear()
                print("TIME IS SOCKET 104 NOW ", socket_104)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await czio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await czio.connect('http://localhost:5005/socket.io')
        except:
            print("SOCKET socket_104 clear")

        #----d

        try:
            if time.time() - list(socket_105.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 105 ", socket_105 , time.time())  
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)       
                socket_in_use_list.remove(105)
                del socket_in_use[list(socket_105.keys())[0]]
                socket_105.clear()
                print("TIME IS SOCKET 105 NOW ", socket_105)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await daio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await daio.connect('http://localhost:5005/socket.io')
        except:
            print("SOCKET socket_105 clear")


        try:
            if time.time() - list(socket_106.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 106 ", socket_106 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(106)
                del socket_in_use[list(socket_106.keys())[0]]
                socket_106.clear()
                print("TIME IS SOCKET 106 NOW ", socket_106)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await dbio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await dbio.connect('http://localhost:5005/socket.io')
        except:
            print("SOCKET socket_106 clear")


        try:
            if time.time() - list(socket_107.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 107 ", socket_107 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(107)
                del socket_in_use[list(socket_107.keys())[0]]
                socket_107.clear()
                print("TIME IS SOCKET 107 NOW ", socket_107)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await dcio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await dcio.connect('http://localhost:5005/socket.io')
        except:
            print("SOCKET socket_107 clear")


        try:
            if time.time() - list(socket_108.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 108 ", socket_108 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(108)
                del socket_in_use[list(socket_108.keys())[0]]
                socket_108.clear()
                print("TIME IS SOCKET 108 NOW ", socket_108)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await ddio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await ddio.connect('http://localhost:5005/socket.io')
        except:
            print("SOCKET socket_108 clear")


        try:
            if time.time() - list(socket_109.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 109 ", socket_109 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(109)
                del socket_in_use[list(socket_109.keys())[0]]
                socket_109.clear()
                print("TIME IS SOCKET 109 NOW ", socket_109)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await deio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await deio.connect('http://localhost:5005/socket.io')
        except:
            print("SOCKET socket_109 clear")


        try:
            if time.time() - list(socket_110.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 110 ", socket_110 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(110)
                del socket_in_use[list(socket_110.keys())[0]]
                socket_110.clear()
                print("TIME IS SOCKET 110 NOW ", socket_110)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await dfio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await dfio.connect('http://localhost:5005/socket.io')
        except:
            print("SOCKET socket_110 clear")


        try:
            if time.time() - list(socket_111.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 111 ", socket_111 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(111)
                del socket_in_use[list(socket_111.keys())[0]]
                socket_111.clear()
                print("TIME IS SOCKET 111 NOW ", socket_111)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await dgio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await dgio.connect('http://localhost:5005/socket.io')
        except:
            print("SOCKET socket_111 clear")


        try:
            if time.time() - list(socket_112.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 112 ", socket_112 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(112)
                del socket_in_use[list(socket_112.keys())[0]]
                socket_112.clear()
                print("TIME IS SOCKET 112 NOW ", socket_112)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await dhio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await dhio.connect('http://localhost:5005/socket.io')
        except:
            print("SOCKET socket_112 clear")


        try:
            if time.time() - list(socket_113.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 113 ", socket_113 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(113)
                del socket_in_use[list(socket_113.keys())[0]]
                socket_113.clear()
                print("TIME IS SOCKET 113 NOW ", socket_113)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await diio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await diio.connect('http://localhost:5005/socket.io')
        except:
            print("SOCKET socket_113 clear")


        try:
            if time.time() - list(socket_114.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 114 ", socket_114 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(114)
                del socket_in_use[list(socket_114.keys())[0]]
                socket_114.clear()
                print("TIME IS SOCKET 114 NOW ", socket_114)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await djio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await djio.connect('http://localhost:5005/socket.io')
        except:
            print("SOCKET socket_114 clear")


        try:
            if time.time() - list(socket_115.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 115 ", socket_115 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(115)
                del socket_in_use[list(socket_115.keys())[0]]
                socket_115.clear()
                print("TIME IS SOCKET 115 NOW ", socket_115)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await dkio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await dkio.connect('http://localhost:5005/socket.io')
        except:
            print("SOCKET socket_115 clear")


        try:
            if time.time() - list(socket_116.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 116 ", socket_116 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(116)
                del socket_in_use[list(socket_116.keys())[0]]
                socket_116.clear()
                print("TIME IS SOCKET 116 NOW ", socket_116)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await dlio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await dlio.connect('http://localhost:5005/socket.io')
        except:
            print("SOCKET socket_116 clear")


        try:
            if time.time() - list(socket_117.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 117 ", socket_117 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(117)
                del socket_in_use[list(socket_117.keys())[0]]
                socket_117.clear()
                print("TIME IS SOCKET 117 NOW ", socket_117)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await dmio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await dmio.connect('http://localhost:5005/socket.io')
        except:
            print("SOCKET socket_117 clear")


        try:
            if time.time() - list(socket_118.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 118 ", socket_118 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(118)
                del socket_in_use[list(socket_118.keys())[0]]
                socket_118.clear()
                print("TIME IS SOCKET 118 NOW ", socket_118)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await dnio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await dnio.connect('http://localhost:5005/socket.io')
        except:
            print("SOCKET socket_118 clear")


        try:
            if time.time() - list(socket_119.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 119 ", socket_119 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(119)
                del socket_in_use[list(socket_119.keys())[0]]
                socket_119.clear()
                print("TIME IS SOCKET 119 NOW ", socket_119)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await doio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await doio.connect('http://localhost:5005/socket.io')
        except:
            print("SOCKET socket_119 clear")


        try:
            if time.time() - list(socket_120.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 120 ", socket_120 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(120)
                del socket_in_use[list(socket_120.keys())[0]]
                socket_120.clear()
                print("TIME IS SOCKET 120 NOW ", socket_120)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await dpio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await dpio.connect('http://localhost:5005/socket.io')
        except:
            print("SOCKET socket_120 clear")


        try:
            if time.time() - list(socket_121.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 121 ", socket_121 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(121)
                del socket_in_use[list(socket_121.keys())[0]]
                socket_121.clear()
                print("TIME IS SOCKET 121 NOW ", socket_121)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await dqio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await dqio.connect('http://localhost:5005/socket.io')
        except:
            print("SOCKET socket_121 clear")


        try:
            if time.time() - list(socket_122.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 122 ", socket_122 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(122)
                del socket_in_use[list(socket_122.keys())[0]]
                socket_122.clear()
                print("TIME IS SOCKET 122 NOW ", socket_122)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await drio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await drio.connect('http://localhost:5005/socket.io')
        except:
            print("SOCKET socket_122 clear")


        try:
            if time.time() - list(socket_123.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 123 ", socket_123 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(123)
                del socket_in_use[list(socket_123.keys())[0]]
                socket_123.clear()
                print("TIME IS SOCKET 123 NOW ", socket_123)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await dsio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await dsio.connect('http://localhost:5005/socket.io')
        except:
            print("SOCKET socket_123 clear")


        try:
            if time.time() - list(socket_124.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 124 ", socket_124 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(124)
                del socket_in_use[list(socket_124.keys())[0]]
                socket_124.clear()
                print("TIME IS SOCKET 124 NOW ", socket_124)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await dtio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await dtio.connect('http://localhost:5005/socket.io')
        except:
            print("SOCKET socket_124 clear")


        try:
            if time.time() - list(socket_125.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 125 ", socket_125 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(125)
                del socket_in_use[list(socket_125.keys())[0]]
                socket_125.clear()
                print("TIME IS SOCKET 125 NOW ", socket_125)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await duio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await duio.connect('http://localhost:5005/socket.io')
        except:
            print("SOCKET socket_125 clear")


        try:
            if time.time() - list(socket_126.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 126 ", socket_126 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(126)
                del socket_in_use[list(socket_126.keys())[0]]
                socket_126.clear()
                print("TIME IS SOCKET 126 NOW ", socket_126)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await dvio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await dvio.connect('http://localhost:5005/socket.io')
        except:
            print("SOCKET socket_126 clear")


        try:
            if time.time() - list(socket_127.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 127 ", socket_127 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(127)
                del socket_in_use[list(socket_127.keys())[0]]
                socket_127.clear()
                print("TIME IS SOCKET 127 NOW ", socket_127)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await dwio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await dwio.connect('http://localhost:5005/socket.io')
        except:
            print("SOCKET socket_127 clear")


        try:
            if time.time() - list(socket_128.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 128 ", socket_128 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(128)
                del socket_in_use[list(socket_128.keys())[0]]
                socket_128.clear()
                print("TIME IS SOCKET 128 NOW ", socket_128)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await dxio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await dxio.connect('http://localhost:5005/socket.io')
        except:
            print("SOCKET socket_128 clear")


        try:
            if time.time() - list(socket_129.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 129 ", socket_129 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(129)
                del socket_in_use[list(socket_129.keys())[0]]
                socket_129.clear()
                print("TIME IS SOCKET 129 NOW ", socket_129)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await dyio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await dyio.connect('http://localhost:5005/socket.io')
        except:
            print("SOCKET socket_129 clear")


        try:
            if time.time() - list(socket_130.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 130 ", socket_130 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(130)
                del socket_in_use[list(socket_130.keys())[0]]
                socket_130.clear()
                print("TIME IS SOCKET 130 NOW ", socket_130)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await dzio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await dzio.connect('http://localhost:5005/socket.io')
        except:
            print("SOCKET socket_130 clear")

        #----e

        try:
            if time.time() - list(socket_131.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 131 ", socket_131 , time.time())  
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(131)
                del socket_in_use[list(socket_131.keys())[0]]
                socket_131.clear()
                print("TIME IS SOCKET 131 NOW ", socket_131)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await eaio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await eaio.connect('http://localhost:5005/socket.io')
        except:
            print("SOCKET socket_131 clear")


        try:
            if time.time() - list(socket_132.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 132 ", socket_132 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(132)
                del socket_in_use[list(socket_132.keys())[0]]
                socket_132.clear()
                print("TIME IS SOCKET 132 NOW ", socket_132)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await ebio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await ebio.connect('http://localhost:5005/socket.io')
        except:
            print("SOCKET socket_132 clear")


        try:
            if time.time() - list(socket_133.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 133 ", socket_133 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(133)
                del socket_in_use[list(socket_133.keys())[0]]
                socket_133.clear()
                print("TIME IS SOCKET 133 NOW ", socket_133)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await ecio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await ecio.connect('http://localhost:5005/socket.io')
        except:
            print("SOCKET socket_133 clear")


        try:
            if time.time() - list(socket_134.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 134 ", socket_134 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(134)
                del socket_in_use[list(socket_134.keys())[0]]
                socket_134.clear()
                print("TIME IS SOCKET 134 NOW ", socket_134)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await edio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await edio.connect('http://localhost:5005/socket.io')
        except:
            print("SOCKET socket_134 clear")


        try:
            if time.time() - list(socket_135.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 135 ", socket_135 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(135)
                del socket_in_use[list(socket_135.keys())[0]]
                socket_135.clear()
                print("TIME IS SOCKET 135 NOW ", socket_135)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await eeio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await eeio.connect('http://localhost:5005/socket.io')
        except:
            print("SOCKET socket_135 clear")


        try:
            if time.time() - list(socket_136.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 136 ", socket_136 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(136)
                del socket_in_use[list(socket_136.keys())[0]]
                socket_136.clear()
                print("TIME IS SOCKET 136 NOW ", socket_136)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await efio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await efio.connect('http://localhost:5005/socket.io')
        except:
            print("SOCKET socket_136 clear")


        try:
            if time.time() - list(socket_137.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 137 ", socket_137 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(137)
                del socket_in_use[list(socket_137.keys())[0]]
                socket_137.clear()
                print("TIME IS SOCKET 137 NOW ", socket_137)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await egio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await egio.connect('http://localhost:5005/socket.io')
        except:
            print("SOCKET socket_137 clear")


        try:
            if time.time() - list(socket_138.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 138 ", socket_138 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(138)
                del socket_in_use[list(socket_138.keys())[0]]
                socket_138.clear()
                print("TIME IS SOCKET 138 NOW ", socket_138)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await ehio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await ehio.connect('http://localhost:5005/socket.io')
        except:
            print("SOCKET socket_138 clear")


        try:
            if time.time() - list(socket_139.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 139 ", socket_139 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(139)
                del socket_in_use[list(socket_139.keys())[0]]
                socket_139.clear()
                print("TIME IS SOCKET 139 NOW ", socket_139)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await eiio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await eiio.connect('http://localhost:5005/socket.io')
        except:
            print("SOCKET socket_139 clear")


        try:
            if time.time() - list(socket_140.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 140 ", socket_140 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(140)
                del socket_in_use[list(socket_140.keys())[0]]
                socket_140.clear()
                print("TIME IS SOCKET 140 NOW ", socket_140)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await ejio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await ejio.connect('http://localhost:5005/socket.io')
        except:
            print("SOCKET socket_140 clear")


        try:
            if time.time() - list(socket_141.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 141 ", socket_141 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(141)
                del socket_in_use[list(socket_141.keys())[0]]
                socket_141.clear()
                print("TIME IS SOCKET 141 NOW ", socket_141)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await ekio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await ekio.connect('http://localhost:5005/socket.io')
        except:
            print("SOCKET socket_141 clear")


        try:
            if time.time() - list(socket_142.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 142 ", socket_142 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(142)
                del socket_in_use[list(socket_142.keys())[0]]
                socket_142.clear()
                print("TIME IS SOCKET 142 NOW ", socket_142)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await elio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await elio.connect('http://localhost:5005/socket.io')
        except:
            print("SOCKET socket_142 clear")


        try:
            if time.time() - list(socket_143.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 143 ", socket_143 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(143)
                del socket_in_use[list(socket_143.keys())[0]]
                socket_143.clear()
                print("TIME IS SOCKET 143 NOW ", socket_143)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await emio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await emio.connect('http://localhost:5005/socket.io')
        except:
            print("SOCKET socket_143 clear")


        try:
            if time.time() - list(socket_144.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 144 ", socket_144 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(144)
                del socket_in_use[list(socket_144.keys())[0]]
                socket_144.clear()
                print("TIME IS SOCKET 144 NOW ", socket_144)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await enio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await enio.connect('http://localhost:5005/socket.io')
        except:
            print("SOCKET socket_144 clear")


        try:
            if time.time() - list(socket_145.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 145 ", socket_145 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(145)
                del socket_in_use[list(socket_145.keys())[0]]
                socket_145.clear()
                print("TIME IS SOCKET 145 NOW ", socket_145)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await eoio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await eoio.connect('http://localhost:5005/socket.io')
        except:
            print("SOCKET socket_145 clear")


        try:
            if time.time() - list(socket_146.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 146 ", socket_146 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(146)
                del socket_in_use[list(socket_146.keys())[0]]
                socket_146.clear()
                print("TIME IS SOCKET 146 NOW ", socket_146)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await epio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await epio.connect('http://localhost:5005/socket.io')
        except:
            print("SOCKET socket_146 clear")


        try:
            if time.time() - list(socket_147.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 147 ", socket_147 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(147)
                del socket_in_use[list(socket_147.keys())[0]]
                socket_147.clear()
                print("TIME IS SOCKET 147 NOW ", socket_147)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await eqio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await eqio.connect('http://localhost:5005/socket.io')
        except:
            print("SOCKET socket_147 clear")


        try:
            if time.time() - list(socket_148.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 148 ", socket_148 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(148)
                del socket_in_use[list(socket_148.keys())[0]]
                socket_148.clear()
                print("TIME IS SOCKET 148 NOW ", socket_148)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await erio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await erio.connect('http://localhost:5005/socket.io')
        except:
            print("SOCKET socket_148 clear")


        try:
            if time.time() - list(socket_149.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 149 ", socket_149 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(149)
                del socket_in_use[list(socket_149.keys())[0]]
                socket_149.clear()
                print("TIME IS SOCKET 149 NOW ", socket_149)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await esio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await esio.connect('http://localhost:5005/socket.io')
        except:
            print("SOCKET socket_149 clear")


        try:
            if time.time() - list(socket_150.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 150 ", socket_150 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(150)
                del socket_in_use[list(socket_150.keys())[0]]
                socket_150.clear()
                print("TIME IS SOCKET 150 NOW ", socket_150)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await etio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await etio.connect('http://localhost:5005/socket.io')
        except:
            print("SOCKET socket_150 clear")


        try:
            if time.time() - list(socket_151.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 151 ", socket_151 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(151)
                del socket_in_use[list(socket_151.keys())[0]]
                socket_151.clear()
                print("TIME IS SOCKET 151 NOW ", socket_151)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await euio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await euio.connect('http://localhost:5005/socket.io')
        except:
            print("SOCKET socket_151 clear")


        try:
            if time.time() - list(socket_152.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 152 ", socket_152 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(152)
                del socket_in_use[list(socket_152.keys())[0]]
                socket_152.clear()
                print("TIME IS SOCKET 152 NOW ", socket_152)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await evio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await evio.connect('http://localhost:5005/socket.io')
        except:
            print("SOCKET socket_152 clear")


        try:
            if time.time() - list(socket_153.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 153 ", socket_153 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(153)
                del socket_in_use[list(socket_153.keys())[0]]
                socket_153.clear()
                print("TIME IS SOCKET 153 NOW ", socket_153)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await ewio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await ewio.connect('http://localhost:5005/socket.io')
        except:
            print("SOCKET socket_153 clear")


        try:
            if time.time() - list(socket_154.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 154 ", socket_154 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(154)
                del socket_in_use[list(socket_154.keys())[0]]
                socket_154.clear()
                print("TIME IS SOCKET 154 NOW ", socket_154)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await exio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await exio.connect('http://localhost:5005/socket.io')
        except:
            print("SOCKET socket_154 clear")


        try:
            if time.time() - list(socket_155.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 155 ", socket_155 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(155)
                del socket_in_use[list(socket_155.keys())[0]]
                socket_155.clear()
                print("TIME IS SOCKET 155 NOW ", socket_155)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await eyio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await eyio.connect('http://localhost:5005/socket.io')
        except:
            print("SOCKET socket_155 clear")


        try:
            if time.time() - list(socket_156.values())[0] > 180:
                print("TIME IS UP FOR SOCKET 156 ", socket_156 , time.time())
                print("THIS IS SOCKET IN USE LISE BEFORE ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC BEFORE", socket_in_use)
                socket_in_use_list.remove(156)
                del socket_in_use[list(socket_156.keys())[0]]
                socket_156.clear()
                print("TIME IS SOCKET 156 NOW ", socket_156)
                print("THIS IS SOCKET IN USE LISE AFTER ", socket_in_use_list)
                print("THIS IS SOCKET IN USE DIC AFTER", socket_in_use)
                await ezio.disconnect()
                # wsio = socketio.AsyncClient()
                await asyncio.sleep(0.1)
                await ezio.connect('http://localhost:5005/socket.io')
        except:
            print("SOCKET socket_156 clear")

    
        pass
    async def empty_sock_check(self,user_id):
        if user_id not in list(socket_in_use.keys()): # To check if the current user is a new user or an existing user
            free_sockets = list(sorted(set(socket_list) - set(socket_in_use_list))) # To check if there are any free sockets or not by comparing a list of sockets to list of sockets that are in use currently 
            if free_sockets[0] == 1: # If there are any free sockets
                await self.socket_1(user_id)# To execute calling a funtion without the need to run through if statements.
            elif free_sockets[0] == 2:
                await self.socket_2(user_id)
            elif free_sockets[0] == 3:
                await self.socket_3(user_id)
            elif free_sockets[0] == 4:
                await self.socket_4(user_id)
            elif free_sockets[0] == 5:
                await self.socket_5(user_id)
            elif free_sockets[0] == 6:
                await self.socket_6(user_id)
            elif free_sockets[0] == 7:
                await self.socket_7(user_id)
            elif free_sockets[0] == 8:
                await self.socket_8(user_id)
            elif free_sockets[0] == 9:
                await self.socket_9(user_id)
            elif free_sockets[0] == 10:
                await self.socket_10(user_id)
            elif free_sockets[0] == 11:
                await self.socket_11(user_id)
            elif free_sockets[0] == 12:
                await self.socket_12(user_id)
            elif free_sockets[0] == 13:
                await self.socket_13(user_id)
            elif free_sockets[0] == 14:
                await self.socket_14(user_id)
            elif free_sockets[0] == 15:
                await self.socket_15(user_id)
            elif free_sockets[0] == 16:
                await self.socket_16(user_id)
            elif free_sockets[0] == 17:
                await self.socket_17(user_id)
            elif free_sockets[0] == 18:
                await self.socket_18(user_id)
            elif free_sockets[0] == 19:
                await self.socket_19(user_id)
            elif free_sockets[0] == 20:
                await self.socket_20(user_id)
            elif free_sockets[0] == 21:
                await self.socket_21(user_id)
            elif free_sockets[0] == 22:
                await self.socket_22(user_id)
            elif free_sockets[0] == 23:
                await self.socket_23(user_id)
            elif free_sockets[0] == 24:
                await self.socket_24(user_id)
            elif free_sockets[0] == 25:
                await self.socket_25(user_id) 
            elif free_sockets[0] == 26:
                await self.socket_26(user_id) 
            elif free_sockets[0] == 27: # If there are any free sockets
                await self.socket_27(user_id)# To execute calling a funtion without the need to run through if statements.
            elif free_sockets[0] == 28:
                await self.socket_28(user_id)
            elif free_sockets[0] == 29:
                await self.socket_29(user_id)
            elif free_sockets[0] == 30:
                await self.socket_30(user_id)
            elif free_sockets[0] == 31:
                await self.socket_31(user_id)
            elif free_sockets[0] == 32:
                await self.socket_32(user_id)
            elif free_sockets[0] == 33:
                await self.socket_33(user_id)
            elif free_sockets[0] == 34:
                await self.socket_34(user_id)
            elif free_sockets[0] == 35:
                await self.socket_35(user_id)
            elif free_sockets[0] == 36:
                await self.socket_36(user_id)
            elif free_sockets[0] == 37:
                await self.socket_37(user_id)
            elif free_sockets[0] == 38:
                await self.socket_38(user_id)
            elif free_sockets[0] == 39:
                await self.socket_39(user_id)
            elif free_sockets[0] == 40:
                await self.socket_40(user_id)
            elif free_sockets[0] == 41:
                await self.socket_41(user_id)
            elif free_sockets[0] == 42:
                await self.socket_42(user_id)
            elif free_sockets[0] == 43:
                await self.socket_43(user_id)
            elif free_sockets[0] == 44:
                await self.socket_44(user_id)
            elif free_sockets[0] == 45:
                await self.socket_45(user_id)
            elif free_sockets[0] == 46:
                await self.socket_46(user_id)
            elif free_sockets[0] == 47:
                await self.socket_47(user_id)
            elif free_sockets[0] == 48:
                await self.socket_48(user_id)
            elif free_sockets[0] == 49:
                await self.socket_49(user_id)
            elif free_sockets[0] == 50:
                await self.socket_50(user_id)
            elif free_sockets[0] == 51:
                await self.socket_51(user_id) 
            elif free_sockets[0] == 52:
                await self.socket_52(user_id)
            elif free_sockets[0] == 53:      
                await self.socket_53(user_id)
            elif free_sockets[0] == 54:      
                await self.socket_54(user_id)
            elif free_sockets[0] == 55:      
                await self.socket_55(user_id)
            elif free_sockets[0] == 56:      
                await self.socket_56(user_id)
            elif free_sockets[0] == 57:      
                await self.socket_57(user_id)
            elif free_sockets[0] == 58:      
                await self.socket_58(user_id)
            elif free_sockets[0] == 59:      
                await self.socket_59(user_id)
            elif free_sockets[0] == 60:      
                await self.socket_60(user_id)
            elif free_sockets[0] == 61:      
                await self.socket_61(user_id)
            elif free_sockets[0] == 62:      
                await self.socket_62(user_id)
            elif free_sockets[0] == 63:      
                await self.socket_63(user_id)
            elif free_sockets[0] == 64:      
                await self.socket_64(user_id)
            elif free_sockets[0] == 65:      
                await self.socket_65(user_id)
            elif free_sockets[0] == 66:
                await self.socket_66(user_id)
            elif free_sockets[0] == 67:
                await self.socket_67(user_id)
            elif free_sockets[0] == 68:
                await self.socket_68(user_id)
            elif free_sockets[0] == 69:
                await self.socket_69(user_id)
            elif free_sockets[0] == 70:
                await self.socket_70(user_id)
            elif free_sockets[0] == 71:
                await self.socket_71(user_id)
            elif free_sockets[0] == 72:
                await self.socket_72(user_id)
            elif free_sockets[0] == 73:
                await self.socket_73(user_id)
            elif free_sockets[0] == 74:
                await self.socket_74(user_id)
            elif free_sockets[0] == 75:
                await self.socket_75(user_id)
            elif free_sockets[0] == 76:
                await self.socket_76(user_id)
            elif free_sockets[0] == 77:
                await self.socket_77(user_id)
            elif free_sockets[0] == 78:
                await self.socket_78(user_id)
            elif free_sockets[0] == 79:
                await self.socket_79(user_id)
            elif free_sockets[0] == 80:
                await self.socket_80(user_id)
            elif free_sockets[0] == 81:
                await self.socket_81(user_id)
            elif free_sockets[0] == 82:
                await self.socket_82(user_id)
            elif free_sockets[0] == 83:
                await self.socket_83(user_id)
            elif free_sockets[0] == 84:
                await self.socket_84(user_id)
            elif free_sockets[0] == 85:
                await self.socket_85(user_id)
            elif free_sockets[0] == 86:
                await self.socket_86(user_id)
            elif free_sockets[0] == 87:
                await self.socket_87(user_id)
            elif free_sockets[0] == 88:
                await self.socket_88(user_id)
            elif free_sockets[0] == 89:
                await self.socket_89(user_id)
            elif free_sockets[0] == 90:
                await self.socket_90(user_id)
            elif free_sockets[0] == 91:
                await self.socket_91(user_id)
            elif free_sockets[0] == 92:
                await self.socket_92(user_id)
            elif free_sockets[0] == 93:
                await self.socket_93(user_id)
            elif free_sockets[0] == 94:
                await self.socket_94(user_id)
            elif free_sockets[0] == 95:
                await self.socket_95(user_id)
            elif free_sockets[0] == 96:
                await self.socket_96(user_id)
            elif free_sockets[0] == 97:
                await self.socket_97(user_id)
            elif free_sockets[0] == 98:
                await self.socket_98(user_id)
            elif free_sockets[0] == 99:
                await self.socket_99(user_id)
            elif free_sockets[0] == 100:
                await self.socket_100(user_id)
            elif free_sockets[0] == 101:
                await self.socket_101(user_id)
            elif free_sockets[0] == 102:
                await self.socket_102(user_id)
            elif free_sockets[0] == 103:
                await self.socket_103(user_id)
            elif free_sockets[0] == 104:
                await self.socket_104(user_id)
            elif free_sockets[0] == 105:
                await self.socket_105(user_id)
            elif free_sockets[0] == 106:
                await self.socket_106(user_id)
            elif free_sockets[0] == 107:
                await self.socket_107(user_id)
            elif free_sockets[0] == 108:
                await self.socket_108(user_id)
            elif free_sockets[0] == 109:
                await self.socket_109(user_id)
            elif free_sockets[0] == 110:
                await self.socket_110(user_id)
            elif free_sockets[0] == 111:
                await self.socket_111(user_id)
            elif free_sockets[0] == 112:
                await self.socket_112(user_id)
            elif free_sockets[0] == 113:
                await self.socket_113(user_id)
            elif free_sockets[0] == 114:
                await self.socket_114(user_id)
            elif free_sockets[0] == 115:
                await self.socket_115(user_id)
            elif free_sockets[0] == 116:
                await self.socket_116(user_id)
            elif free_sockets[0] == 117:
                await self.socket_117(user_id)
            elif free_sockets[0] == 118:
                await self.socket_118(user_id)
            elif free_sockets[0] == 119:
                await self.socket_119(user_id)
            elif free_sockets[0] == 120:
                await self.socket_120(user_id)
            elif free_sockets[0] == 121:
                await self.socket_121(user_id)
            elif free_sockets[0] == 122:
                await self.socket_122(user_id)
            elif free_sockets[0] == 123:
                await self.socket_123(user_id)
            elif free_sockets[0] == 124:
                await self.socket_124(user_id)
            elif free_sockets[0] == 125:
                await self.socket_125(user_id)
            elif free_sockets[0] == 126:
                await self.socket_126(user_id)
            elif free_sockets[0] == 127:
                await self.socket_127(user_id)
            elif free_sockets[0] == 128:
                await self.socket_128(user_id)
            elif free_sockets[0] == 129:
                await self.socket_129(user_id)
            elif free_sockets[0] == 130:
                await self.socket_130(user_id)
            elif free_sockets[0] == 131:
                await self.socket_131(user_id)
            elif free_sockets[0] == 132:
                await self.socket_132(user_id)
            elif free_sockets[0] == 133:
                await self.socket_133(user_id)
            elif free_sockets[0] == 134:
                await self.socket_134(user_id)
            elif free_sockets[0] == 135:
                await self.socket_135(user_id)
            elif free_sockets[0] == 136:
                await self.socket_136(user_id)
            elif free_sockets[0] == 137:
                await self.socket_137(user_id)
            elif free_sockets[0] == 138:
                await self.socket_138(user_id)
            elif free_sockets[0] == 139:
                await self.socket_139(user_id)
            elif free_sockets[0] == 140:
                await self.socket_140(user_id)
            elif free_sockets[0] == 141:
                await self.socket_141(user_id)
            elif free_sockets[0] == 142:
                await self.socket_142(user_id)
            elif free_sockets[0] == 143:
                await self.socket_143(user_id)
            elif free_sockets[0] == 144:
                await self.socket_144(user_id)
            elif free_sockets[0] == 145:
                await self.socket_145(user_id)
            elif free_sockets[0] == 146:
                await self.socket_146(user_id)
            elif free_sockets[0] == 147:
                await self.socket_147(user_id)
            elif free_sockets[0] == 148:
                await self.socket_148(user_id)
            elif free_sockets[0] == 149:
                await self.socket_149(user_id)
            elif free_sockets[0] == 150:
                await self.socket_150(user_id)
            elif free_sockets[0] == 151:
                await self.socket_151(user_id)
            elif free_sockets[0] == 152:
                await self.socket_152(user_id)
            elif free_sockets[0] == 153:
                await self.socket_153(user_id)
            elif free_sockets[0] == 154:
                await self.socket_154(user_id)
            elif free_sockets[0] == 155:
                await self.socket_155(user_id)
            elif free_sockets[0] == 156:
                await self.socket_156(user_id)
            else:
                await turn_context.send_activity(
                    f"Something went wrong, please try again in a few minutes")
            
        else:
            if socket_in_use[user_id] == '1':
                await self.socket_use_1(user_id)
            elif socket_in_use[user_id] == '2':
                await self.socket_use_2(user_id)
            elif socket_in_use[user_id] == '3':
                await self.socket_use_3(user_id)
            elif socket_in_use[user_id] == '4':
                await self.socket_use_4(user_id)
            elif socket_in_use[user_id] == '5':
                await self.socket_use_5(user_id)
            elif socket_in_use[user_id] == '6':
                await self.socket_use_6(user_id)
            elif socket_in_use[user_id] == '7':
                await self.socket_use_7(user_id)
            elif socket_in_use[user_id] == '8':
                await self.socket_use_8(user_id)
            elif socket_in_use[user_id] == '9':
                await self.socket_use_9(user_id)
            elif socket_in_use[user_id] == '10':
                await self.socket_use_10(user_id)
            elif socket_in_use[user_id] == '11':
                await self.socket_use_11(user_id)
            elif socket_in_use[user_id] == '12':
                await self.socket_use_12(user_id)
            elif socket_in_use[user_id] == '13':
                await self.socket_use_13(user_id)
            elif socket_in_use[user_id] == '14':
                await self.socket_use_14(user_id)
            elif socket_in_use[user_id] == '15':
                await self.socket_use_15(user_id)
            elif socket_in_use[user_id] == '16':
                await self.socket_use_16(user_id)
            elif socket_in_use[user_id] == '17':
                await self.socket_use_17(user_id)
            elif socket_in_use[user_id] == '18':
                await self.socket_use_18(user_id)
            elif socket_in_use[user_id] == '19':
                await self.socket_use_19(user_id)
            elif socket_in_use[user_id] == '20':
                await self.socket_use_20(user_id)
            elif socket_in_use[user_id] == '21':
                await self.socket_use_21(user_id)
            elif socket_in_use[user_id] == '22':
                await self.socket_use_22(user_id)
            elif socket_in_use[user_id] == '23':
                await self.socket_use_23(user_id)
            elif socket_in_use[user_id] == '24':
                await self.socket_use_24(user_id)
            elif socket_in_use[user_id] == '25':
                await self.socket_use_25(user_id)
            elif socket_in_use[user_id] == '26':
                await self.socket_use_26(user_id)
            elif socket_in_use[user_id] == '27':
                await self.socket_use_27(user_id)
            elif socket_in_use[user_id] == '28':
                await self.socket_use_28(user_id)
            elif socket_in_use[user_id] == '29':
                await self.socket_use_29(user_id)
            elif socket_in_use[user_id] == '30':
                await self.socket_use_30(user_id)
            elif socket_in_use[user_id] == '31':
                await self.socket_use_31(user_id)
            elif socket_in_use[user_id] == '32':
                await self.socket_use_32(user_id)
            elif socket_in_use[user_id] == '33':
                await self.socket_use_33(user_id)
            elif socket_in_use[user_id] == '34':
                await self.socket_use_34(user_id)
            elif socket_in_use[user_id] == '35':
                await self.socket_use_35(user_id)
            elif socket_in_use[user_id] == '36':
                await self.socket_use_36(user_id)
            elif socket_in_use[user_id] == '37':
                await self.socket_use_37(user_id)
            elif socket_in_use[user_id] == '38':
                await self.socket_use_38(user_id)
            elif socket_in_use[user_id] == '39':
                await self.socket_use_39(user_id)
            elif socket_in_use[user_id] == '40':
                await self.socket_use_40(user_id)
            elif socket_in_use[user_id] == '41':
                await self.socket_use_41(user_id)
            elif socket_in_use[user_id] == '42':
                await self.socket_use_42(user_id)
            elif socket_in_use[user_id] == '43':
                await self.socket_use_43(user_id)
            elif socket_in_use[user_id] == '44':
                await self.socket_use_44(user_id)
            elif socket_in_use[user_id] == '45':
                await self.socket_use_45(user_id)
            elif socket_in_use[user_id] == '46':
                await self.socket_use_46(user_id)
            elif socket_in_use[user_id] == '47':
                await self.socket_use_47(user_id)
            elif socket_in_use[user_id] == '48':
                await self.socket_use_48(user_id)
            elif socket_in_use[user_id] == '49':
                await self.socket_use_49(user_id)
            elif socket_in_use[user_id] == '50':
                await self.socket_use_50(user_id)
            elif socket_in_use[user_id] == '51':
                await self.socket_use_51(user_id)
            elif socket_in_use[user_id] == '52':
                await self.socket_use_52(user_id)
            elif socket_in_use[user_id] == '53': 
                await self.socket_use_53(user_id)
            elif socket_in_use[user_id] == '54': 
                await self.socket_use_54(user_id)
            elif socket_in_use[user_id] == '55': 
                await self.socket_use_55(user_id)
            elif socket_in_use[user_id] == '56': 
                await self.socket_use_56(user_id)
            elif socket_in_use[user_id] == '57': 
                await self.socket_use_57(user_id)
            elif socket_in_use[user_id] == '58': 
                await self.socket_use_58(user_id)
            elif socket_in_use[user_id] == '59': 
                await self.socket_use_59(user_id)
            elif socket_in_use[user_id] == '60': 
                await self.socket_use_60(user_id)
            elif socket_in_use[user_id] == '61': 
                await self.socket_use_61(user_id)
            elif socket_in_use[user_id] == '62': 
                await self.socket_use_62(user_id)
            elif socket_in_use[user_id] == '63': 
                await self.socket_use_63(user_id)
            elif socket_in_use[user_id] == '64': 
                await self.socket_use_64(user_id)
            elif socket_in_use[user_id] == '65': 
                await self.socket_use_65(user_id)
            elif socket_in_use[user_id] == '66': 
                await self.socket_use_66(user_id)
            elif socket_in_use[user_id] == '67': 
                await self.socket_use_67(user_id)
            elif socket_in_use[user_id] == '68': 
                await self.socket_use_68(user_id)
            elif socket_in_use[user_id] == '69':
                await self.socket_use_69(user_id)
            elif socket_in_use[user_id] == '70':
                await self.socket_use_70(user_id)
            elif socket_in_use[user_id] == '71':
                await self.socket_use_71(user_id)
            elif socket_in_use[user_id] == '72':
                await self.socket_use_72(user_id)
            elif socket_in_use[user_id] == '73':
                await self.socket_use_73(user_id)
            elif socket_in_use[user_id] == '74':
                await self.socket_use_74(user_id)
            elif socket_in_use[user_id] == '75':
                await self.socket_use_75(user_id)
            elif socket_in_use[user_id] == '76':
                await self.socket_use_76(user_id)
            elif socket_in_use[user_id] == '77':
                await self.socket_use_77(user_id)
            elif socket_in_use[user_id] == '78':
                await self.socket_use_78(user_id)
            elif socket_in_use[user_id] == '79':
                await self.socket_use_79(user_id)
            elif socket_in_use[user_id] == '80':
                await self.socket_use_80(user_id)
            elif socket_in_use[user_id] == '81':
                await self.socket_use_81(user_id)
            elif socket_in_use[user_id] == '82':
                await self.socket_use_82(user_id)
            elif socket_in_use[user_id] == '83':
                await self.socket_use_83(user_id)
            elif socket_in_use[user_id] == '84':
                await self.socket_use_84(user_id)
            elif socket_in_use[user_id] == '85':
                await self.socket_use_85(user_id)
            elif socket_in_use[user_id] == '86':
                await self.socket_use_86(user_id)
            elif socket_in_use[user_id] == '87':
                await self.socket_use_87(user_id)
            elif socket_in_use[user_id] == '88':
                await self.socket_use_88(user_id)
            elif socket_in_use[user_id] == '89':
                await self.socket_use_89(user_id)
            elif socket_in_use[user_id] == '90':
                await self.socket_use_90(user_id)
            elif socket_in_use[user_id] == '91':
                await self.socket_use_91(user_id)
            elif socket_in_use[user_id] == '92':
                await self.socket_use_92(user_id)
            elif socket_in_use[user_id] == '93':
                await self.socket_use_93(user_id)
            elif socket_in_use[user_id] == '94':
                await self.socket_use_94(user_id)
            elif socket_in_use[user_id] == '95':
                await self.socket_use_95(user_id)
            elif socket_in_use[user_id] == '96':
                await self.socket_use_96(user_id)
            elif socket_in_use[user_id] == '97':
                await self.socket_use_97(user_id)
            elif socket_in_use[user_id] == '98':
                await self.socket_use_98(user_id)
            elif socket_in_use[user_id] == '99':
                await self.socket_use_99(user_id)
            elif socket_in_use[user_id] == '100':
                await self.socket_use_100(user_id)
            elif socket_in_use[user_id] == '101':
                await self.socket_use_101(user_id)
            elif socket_in_use[user_id] == '102':
                await self.socket_use_102(user_id)
            elif socket_in_use[user_id] == '103':
                await self.socket_use_103(user_id)
            elif socket_in_use[user_id] == '104':
                await self.socket_use_104(user_id)
            elif socket_in_use[user_id] == '105':
                await self.socket_use_105(user_id)
            elif socket_in_use[user_id] == '106':
                await self.socket_use_106(user_id)
            elif socket_in_use[user_id] == '107':
                await self.socket_use_107(user_id)
            elif socket_in_use[user_id] == '108':
                await self.socket_use_108(user_id)
            elif socket_in_use[user_id] == '109':
                await self.socket_use_109(user_id)
            elif socket_in_use[user_id] == '110':
                await self.socket_use_110(user_id)
            elif socket_in_use[user_id] == '111':
                await self.socket_use_111(user_id)
            elif socket_in_use[user_id] == '112':
                await self.socket_use_112(user_id)
            elif socket_in_use[user_id] == '113':
                await self.socket_use_113(user_id)
            elif socket_in_use[user_id] == '114':
                await self.socket_use_114(user_id)
            elif socket_in_use[user_id] == '115':
                await self.socket_use_115(user_id)
            elif socket_in_use[user_id] == '116':
                await self.socket_use_116(user_id)
            elif socket_in_use[user_id] == '117':
                await self.socket_use_117(user_id)
            elif socket_in_use[user_id] == '118':
                await self.socket_use_118(user_id)
            elif socket_in_use[user_id] == '119':
                await self.socket_use_119(user_id)
            elif socket_in_use[user_id] == '120':
                await self.socket_use_120(user_id)
            elif socket_in_use[user_id] == '121':
                await self.socket_use_121(user_id)
            elif socket_in_use[user_id] == '122':
                await self.socket_use_122(user_id)
            elif socket_in_use[user_id] == '123':
                await self.socket_use_123(user_id)
            elif socket_in_use[user_id] == '124':
                await self.socket_use_124(user_id)
            elif socket_in_use[user_id] == '125':
                await self.socket_use_125(user_id)
            elif socket_in_use[user_id] == '126':
                await self.socket_use_126(user_id)
            elif socket_in_use[user_id] == '127':
                await self.socket_use_127(user_id)
            elif socket_in_use[user_id] == '128':
                await self.socket_use_128(user_id)
            elif socket_in_use[user_id] == '129':
                await self.socket_use_129(user_id)
            elif socket_in_use[user_id] == '130':
                await self.socket_use_130(user_id)
            elif socket_in_use[user_id] == '131':
                await self.socket_use_131(user_id)
            elif socket_in_use[user_id] == '132':
                await self.socket_use_132(user_id)
            elif socket_in_use[user_id] == '133':
                await self.socket_use_133(user_id)
            elif socket_in_use[user_id] == '134':
                await self.socket_use_134(user_id)
            elif socket_in_use[user_id] == '135':
                await self.socket_use_135(user_id)
            elif socket_in_use[user_id] == '136':
                await self.socket_use_136(user_id)
            elif socket_in_use[user_id] == '137':
                await self.socket_use_137(user_id)
            elif socket_in_use[user_id] == '138':
                await self.socket_use_138(user_id)
            elif socket_in_use[user_id] == '139':
                await self.socket_use_139(user_id)
            elif socket_in_use[user_id] == '140':
                await self.socket_use_140(user_id)
            elif socket_in_use[user_id] == '141':
                await self.socket_use_141(user_id)
            elif socket_in_use[user_id] == '142':
                await self.socket_use_142(user_id)
            elif socket_in_use[user_id] == '143':
                await self.socket_use_143(user_id)
            elif socket_in_use[user_id] == '144':
                await self.socket_use_144(user_id)
            elif socket_in_use[user_id] == '145':
                await self.socket_use_145(user_id)
            elif socket_in_use[user_id] == '146':
                await self.socket_use_146(user_id)
            elif socket_in_use[user_id] == '147':
                await self.socket_use_147(user_id)
            elif socket_in_use[user_id] == '148':
                await self.socket_use_148(user_id)
            elif socket_in_use[user_id] == '149':
                await self.socket_use_149(user_id)
            elif socket_in_use[user_id] == '150':
                await self.socket_use_150(user_id)
            elif socket_in_use[user_id] == '151':
                await self.socket_use_151(user_id)
            elif socket_in_use[user_id] == '152':
                await self.socket_use_152(user_id)
            elif socket_in_use[user_id] == '153':
                await self.socket_use_153(user_id)
            elif socket_in_use[user_id] == '154':
                await self.socket_use_154(user_id)
            elif socket_in_use[user_id] == '155':
                await self.socket_use_155(user_id)
            elif socket_in_use[user_id] == '156':
                await self.socket_use_156(user_id)
            else:
                await turn_context.send_activity(
                    f"Something went wrong, please try again in a few minutes")

    async def socket_1(self,user_id):
        global socket_1, socket_in_use, socket_in_use_list
        socket_1[user_id] = time.time()
        socket_in_use[user_id] = '1'
        socket_in_use_list.append(1)
        print("THIS IS SOCKET_1 ", socket_1)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)

    async def socket_2(self,user_id):
        global socket_2, socket_in_use, socket_in_use_list
        socket_2[user_id] = time.time()
        socket_in_use[user_id] = '2'
        socket_in_use_list.append(2)
        print("THIS IS SOCKET_2 ", socket_2)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)

    async def socket_3(self,user_id):
        global socket_3, socket_in_use, socket_in_use_list
        socket_3[user_id] = time.time()
        socket_in_use[user_id] = '3'
        socket_in_use_list.append(3)
        print("THIS IS SOCKET_3 ", socket_3)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)

    async def socket_4(self,user_id):
        global socket_4, socket_in_use, socket_in_use_list
        socket_4[user_id] = time.time()
        socket_in_use[user_id] = '4'
        socket_in_use_list.append(4)
        print("THIS IS SOCKET_4 ", socket_4)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)

    async def socket_5(self,user_id):
        global socket_5, socket_in_use, socket_in_use_list
        socket_5[user_id] = time.time()
        socket_in_use[user_id] = '5'
        socket_in_use_list.append(5)
        print("THIS IS SOCKET_5 ", socket_5)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)
    
    async def socket_6(self,user_id):
        global socket_6, socket_in_use, socket_in_use_list
        socket_6[user_id] = time.time()
        socket_in_use[user_id] = '6'
        socket_in_use_list.append(6)
        print("THIS IS SOCKET_6 ", socket_6)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)

    async def socket_7(self,user_id):
        global socket_7, socket_in_use, socket_in_use_list
        socket_7[user_id] = time.time()
        socket_in_use[user_id] = '7'
        socket_in_use_list.append(7)
        print("THIS IS SOCKET_7 ", socket_7)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)

    async def socket_8(self,user_id):
        global socket_8, socket_in_use, socket_in_use_list
        socket_8[user_id] = time.time()
        socket_in_use[user_id] = '8'
        socket_in_use_list.append(8)
        print("THIS IS SOCKET_8 ", socket_8)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)

    async def socket_9(self,user_id):
        global socket_9, socket_in_use, socket_in_use_list
        socket_9[user_id] = time.time()
        socket_in_use[user_id] = '9'
        socket_in_use_list.append(9)
        print("THIS IS SOCKET_9 ", socket_9)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)

    async def socket_10(self,user_id):
        global socket_10, socket_in_use, socket_in_use_list
        socket_10[user_id] = time.time()
        socket_in_use[user_id] = '10'
        socket_in_use_list.append(10)
        print("THIS IS SOCKET_10 ", socket_10)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)
    
    async def socket_11(self,user_id):
        global socket_11, socket_in_use, socket_in_use_list
        socket_11[user_id] = time.time()
        socket_in_use[user_id] = '11'
        socket_in_use_list.append(11)
        print("THIS IS SOCKET_11 ", socket_11)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)

    async def socket_12(self,user_id):
        global socket_12, socket_in_use, socket_in_use_list
        socket_12[user_id] = time.time()
        socket_in_use[user_id] = '12'
        socket_in_use_list.append(12)
        print("THIS IS SOCKET_12 ", socket_12)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)
    
    async def socket_13(self,user_id):
        global socket_13, socket_in_use, socket_in_use_list
        socket_13[user_id] = time.time()
        socket_in_use[user_id] = '13'
        socket_in_use_list.append(13)
        print("THIS IS SOCKET_13 ", socket_13)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)

    async def socket_14(self,user_id):
        global socket_14, socket_in_use, socket_in_use_list
        socket_14[user_id] = time.time()
        socket_in_use[user_id] = '14'
        socket_in_use_list.append(14)
        print("THIS IS SOCKET_14 ", socket_14)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)
    
    async def socket_15(self,user_id):
        global socket_15, socket_in_use, socket_in_use_list
        socket_15[user_id] = time.time()
        socket_in_use[user_id] = '15'
        socket_in_use_list.append(15)
        print("THIS IS SOCKET_15 ", socket_15)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)

    async def socket_16(self,user_id):
        global socket_16, socket_in_use, socket_in_use_list
        socket_16[user_id] = time.time()
        socket_in_use[user_id] = '16'
        socket_in_use_list.append(16)
        print("THIS IS SOCKET_16 ", socket_16)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)

    async def socket_17(self,user_id):
        global socket_17, socket_in_use, socket_in_use_list
        socket_17[user_id] = time.time()
        socket_in_use[user_id] = '17'
        socket_in_use_list.append(17)
        print("THIS IS SOCKET_17 ", socket_17)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)

    async def socket_18(self,user_id):
        global socket_18, socket_in_use, socket_in_use_list
        socket_18[user_id] = time.time()
        socket_in_use[user_id] = '18'
        socket_in_use_list.append(18)
        print("THIS IS SOCKET_18 ", socket_18)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)

    async def socket_19(self,user_id):
        global socket_19, socket_in_use, socket_in_use_list
        socket_19[user_id] = time.time()
        socket_in_use[user_id] = '19'
        socket_in_use_list.append(19)
        print("THIS IS SOCKET_19 ", socket_19)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)

    async def socket_20(self,user_id):
        global socket_20, socket_in_use, socket_in_use_list
        socket_20[user_id] = time.time()
        socket_in_use[user_id] = '20'
        socket_in_use_list.append(20)
        print("THIS IS SOCKET_20 ", socket_20)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)

    async def socket_21(self,user_id):
        global socket_21, socket_in_use, socket_in_use_list
        socket_21[user_id] = time.time()
        socket_in_use[user_id] = '21'
        socket_in_use_list.append(21)
        print("THIS IS SOCKET_21 ", socket_21)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)

    async def socket_22(self,user_id):
        global socket_22, socket_in_use, socket_in_use_list
        socket_22[user_id] = time.time()
        socket_in_use[user_id] = '22'
        socket_in_use_list.append(22)
        print("THIS IS SOCKET_22 ", socket_22)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)

    async def socket_23(self,user_id):
        global socket_23, socket_in_use, socket_in_use_list
        socket_23[user_id] = time.time()
        socket_in_use[user_id] = '23'
        socket_in_use_list.append(23)
        print("THIS IS SOCKET_23 ", socket_23)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)

    async def socket_24(self,user_id):
        global socket_24, socket_in_use, socket_in_use_list
        socket_24[user_id] = time.time()
        socket_in_use[user_id] = '24'
        socket_in_use_list.append(24)
        print("THIS IS SOCKET_24 ", socket_24)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)

    async def socket_25(self,user_id):
        global socket_25, socket_in_use, socket_in_use_list
        socket_25[user_id] = time.time()
        socket_in_use[user_id] = '25'
        socket_in_use_list.append(25)
        print("THIS IS SOCKET_25 ", socket_25)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)
    
    async def socket_26(self,user_id):
        global socket_26, socket_in_use, socket_in_use_list
        socket_26[user_id] = time.time()
        socket_in_use[user_id] = '26'
        socket_in_use_list.append(26)
        print("THIS IS SOCKET_26 ", socket_26)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)

    #--------
    async def socket_27(self,user_id):
        global socket_27, socket_in_use, socket_in_use_list
        socket_27[user_id] = time.time()
        socket_in_use[user_id] = '27'
        socket_in_use_list.append(27)
        print("THIS IS SOCKET_27 ", socket_27)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)

    async def socket_28(self,user_id):
        global socket_28, socket_in_use, socket_in_use_list
        socket_28[user_id] = time.time()
        socket_in_use[user_id] = '28'
        socket_in_use_list.append(28)
        print("THIS IS SOCKET_28 ", socket_28)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)

    async def socket_29(self,user_id):
        global socket_29, socket_in_use, socket_in_use_list
        socket_29[user_id] = time.time()
        socket_in_use[user_id] = '29'
        socket_in_use_list.append(29)
        print("THIS IS SOCKET_29 ", socket_29)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)

    async def socket_30(self,user_id):
        global socket_30, socket_in_use, socket_in_use_list
        socket_30[user_id] = time.time()
        socket_in_use[user_id] = '30'
        socket_in_use_list.append(30)
        print("THIS IS SOCKET_30 ", socket_30)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)

    async def socket_31(self,user_id):
        global socket_31, socket_in_use, socket_in_use_list
        socket_31[user_id] = time.time()
        socket_in_use[user_id] = '31'
        socket_in_use_list.append(31)
        print("THIS IS SOCKET_31 ", socket_31)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)
    
    async def socket_32(self,user_id):
        global socket_32, socket_in_use, socket_in_use_list
        socket_32[user_id] = time.time()
        socket_in_use[user_id] = '32'
        socket_in_use_list.append(32)
        print("THIS IS SOCKET_32 ", socket_32)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)

    async def socket_33(self,user_id):
        global socket_33, socket_in_use, socket_in_use_list
        socket_33[user_id] = time.time()
        socket_in_use[user_id] = '33'
        socket_in_use_list.append(33)
        print("THIS IS SOCKET_33 ", socket_33)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)

    async def socket_34(self,user_id):
        global socket_34, socket_in_use, socket_in_use_list
        socket_34[user_id] = time.time()
        socket_in_use[user_id] = '34'
        socket_in_use_list.append(34)
        print("THIS IS SOCKET_34 ", socket_34)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)

    async def socket_35(self,user_id):
        global socket_35, socket_in_use, socket_in_use_list
        socket_35[user_id] = time.time()
        socket_in_use[user_id] = '35'
        socket_in_use_list.append(35)
        print("THIS IS SOCKET_35 ", socket_35)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)

    async def socket_36(self,user_id):
        global socket_36, socket_in_use, socket_in_use_list
        socket_36[user_id] = time.time()
        socket_in_use[user_id] = '36'
        socket_in_use_list.append(36)
        print("THIS IS SOCKET_36 ", socket_36)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)
    
    async def socket_37(self,user_id):
        global socket_37, socket_in_use, socket_in_use_list
        socket_37[user_id] = time.time()
        socket_in_use[user_id] = '37'
        socket_in_use_list.append(37)
        print("THIS IS SOCKET_37 ", socket_37)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)

    async def socket_38(self,user_id):
        global socket_38, socket_in_use, socket_in_use_list
        socket_38[user_id] = time.time()
        socket_in_use[user_id] = '38'
        socket_in_use_list.append(38)
        print("THIS IS SOCKET_38 ", socket_38)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)
    
    async def socket_39(self,user_id):
        global socket_39, socket_in_use, socket_in_use_list
        socket_39[user_id] = time.time()
        socket_in_use[user_id] = '39'
        socket_in_use_list.append(39)
        print("THIS IS SOCKET_39 ", socket_39)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)

    async def socket_40(self,user_id):
        global socket_40, socket_in_use, socket_in_use_list
        socket_40[user_id] = time.time()
        socket_in_use[user_id] = '40'
        socket_in_use_list.append(40)
        print("THIS IS SOCKET_40 ", socket_40)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)
    
    async def socket_41(self,user_id):
        global socket_41, socket_in_use, socket_in_use_list
        socket_41[user_id] = time.time()
        socket_in_use[user_id] = '41'
        socket_in_use_list.append(41)
        print("THIS IS SOCKET_41 ", socket_41)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)

    async def socket_42(self,user_id):
        global socket_42, socket_in_use, socket_in_use_list
        socket_42[user_id] = time.time()
        socket_in_use[user_id] = '42'
        socket_in_use_list.append(42)
        print("THIS IS SOCKET_42 ", socket_42)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)

    async def socket_43(self,user_id):
        global socket_43, socket_in_use, socket_in_use_list
        socket_43[user_id] = time.time()
        socket_in_use[user_id] = '43'
        socket_in_use_list.append(43)
        print("THIS IS SOCKET_43 ", socket_43)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)

    async def socket_44(self,user_id):
        global socket_44, socket_in_use, socket_in_use_list
        socket_44[user_id] = time.time()
        socket_in_use[user_id] = '44'
        socket_in_use_list.append(44)
        print("THIS IS SOCKET_44 ", socket_44)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)

    async def socket_45(self,user_id):
        global socket_45, socket_in_use, socket_in_use_list
        socket_45[user_id] = time.time()
        socket_in_use[user_id] = '45'
        socket_in_use_list.append(45)
        print("THIS IS SOCKET_45 ", socket_45)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)

    async def socket_46(self,user_id):
        global socket_46, socket_in_use, socket_in_use_list
        socket_46[user_id] = time.time()
        socket_in_use[user_id] = '46'
        socket_in_use_list.append(46)
        print("THIS IS SOCKET_46 ", socket_46)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)

    async def socket_47(self,user_id):
        global socket_47, socket_in_use, socket_in_use_list
        socket_47[user_id] = time.time()
        socket_in_use[user_id] = '47'
        socket_in_use_list.append(47)
        print("THIS IS SOCKET_47 ", socket_47)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)

    async def socket_48(self,user_id):
        global socket_48, socket_in_use, socket_in_use_list
        socket_48[user_id] = time.time()
        socket_in_use[user_id] = '48'
        socket_in_use_list.append(48)
        print("THIS IS SOCKET_48 ", socket_48)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)

    async def socket_49(self,user_id):
        global socket_49, socket_in_use, socket_in_use_list
        socket_49[user_id] = time.time()
        socket_in_use[user_id] = '49'
        socket_in_use_list.append(49)
        print("THIS IS SOCKET_49 ", socket_49)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)

    async def socket_50(self,user_id):
        global socket_50, socket_in_use, socket_in_use_list
        socket_50[user_id] = time.time()
        socket_in_use[user_id] = '50'
        socket_in_use_list.append(50)
        print("THIS IS SOCKET_50 ", socket_50)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)

    async def socket_51(self,user_id):
        global socket_51, socket_in_use, socket_in_use_list
        socket_51[user_id] = time.time()
        socket_in_use[user_id] = '51'
        socket_in_use_list.append(51)
        print("THIS IS SOCKET_51 ", socket_51)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)
    
    async def socket_52(self,user_id):
        global socket_52, socket_in_use, socket_in_use_list
        socket_52[user_id] = time.time()
        socket_in_use[user_id] = '52'
        socket_in_use_list.append(52)
        print("THIS IS SOCKET_52 ", socket_52)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)

    async def socket_53(self,user_id):
        global socket_53, socket_in_use, socket_in_use_list
        socket_53[user_id] = time.time()
        socket_in_use[user_id] = '53'
        socket_in_use_list.append(53)
        print("THIS IS SOCKET_53 ", socket_53)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)    
    

    async def socket_54(self,user_id):
        global socket_54, socket_in_use, socket_in_use_list
        socket_54[user_id] = time.time()
        socket_in_use[user_id] = '54'
        socket_in_use_list.append(54)
        print("THIS IS SOCKET_54 ", socket_54)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)    
    

    async def socket_55(self,user_id):
        global socket_55, socket_in_use, socket_in_use_list
        socket_55[user_id] = time.time()
        socket_in_use[user_id] = '55'
        socket_in_use_list.append(55)
        print("THIS IS SOCKET_55 ", socket_55)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)


    async def socket_56(self,user_id):
        global socket_56, socket_in_use, socket_in_use_list
        socket_56[user_id] = time.time()
        socket_in_use[user_id] = '56'
        socket_in_use_list.append(56)
        print("THIS IS SOCKET_56 ", socket_56)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)


    async def socket_57(self,user_id):
        global socket_57, socket_in_use, socket_in_use_list
        socket_57[user_id] = time.time()
        socket_in_use[user_id] = '57'
        socket_in_use_list.append(57)
        print("THIS IS SOCKET_57 ", socket_57)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)


    async def socket_58(self,user_id):
        global socket_58, socket_in_use, socket_in_use_list
        socket_58[user_id] = time.time()
        socket_in_use[user_id] = '58'
        socket_in_use_list.append(58)
        print("THIS IS SOCKET_58 ", socket_58)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)


    async def socket_59(self,user_id):
        global socket_59, socket_in_use, socket_in_use_list
        socket_59[user_id] = time.time()
        socket_in_use[user_id] = '59'
        socket_in_use_list.append(59)
        print("THIS IS SOCKET_59 ", socket_59)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)


    async def socket_60(self,user_id):
        global socket_60, socket_in_use, socket_in_use_list
        socket_60[user_id] = time.time()
        socket_in_use[user_id] = '60'
        socket_in_use_list.append(60)
        print("THIS IS SOCKET_60 ", socket_60)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)


    async def socket_61(self,user_id):
        global socket_61, socket_in_use, socket_in_use_list
        socket_61[user_id] = time.time()
        socket_in_use[user_id] = '61'
        socket_in_use_list.append(61)
        print("THIS IS SOCKET_61 ", socket_61)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)


    async def socket_62(self,user_id):
        global socket_62, socket_in_use, socket_in_use_list
        socket_62[user_id] = time.time()
        socket_in_use[user_id] = '62'
        socket_in_use_list.append(62)
        print("THIS IS SOCKET_62 ", socket_62)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)


    async def socket_63(self,user_id):
        global socket_63, socket_in_use, socket_in_use_list
        socket_63[user_id] = time.time()
        socket_in_use[user_id] = '63'
        socket_in_use_list.append(63)
        print("THIS IS SOCKET_63 ", socket_63)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)


    async def socket_64(self,user_id):
        global socket_64, socket_in_use, socket_in_use_list
        socket_64[user_id] = time.time()
        socket_in_use[user_id] = '64'
        socket_in_use_list.append(64)
        print("THIS IS SOCKET_64 ", socket_64)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)


    async def socket_65(self,user_id):
        global socket_65, socket_in_use, socket_in_use_list
        socket_65[user_id] = time.time()
        socket_in_use[user_id] = '65'
        socket_in_use_list.append(65)
        print("THIS IS SOCKET_65 ", socket_65)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)


    async def socket_66(self,user_id):
        global socket_66, socket_in_use, socket_in_use_list
        socket_66[user_id] = time.time()
        socket_in_use[user_id] = '66'
        socket_in_use_list.append(66)
        print("THIS IS SOCKET_66 ", socket_66)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)


    async def socket_67(self,user_id):
        global socket_67, socket_in_use, socket_in_use_list
        socket_67[user_id] = time.time()
        socket_in_use[user_id] = '67'
        socket_in_use_list.append(67)
        print("THIS IS SOCKET_67 ", socket_67)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)


    async def socket_68(self,user_id):
        global socket_68, socket_in_use, socket_in_use_list
        socket_68[user_id] = time.time()
        socket_in_use[user_id] = '68'
        socket_in_use_list.append(68)
        print("THIS IS SOCKET_68 ", socket_68)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)


    async def socket_69(self,user_id):
        global socket_69, socket_in_use, socket_in_use_list
        socket_69[user_id] = time.time()
        socket_in_use[user_id] = '69'
        socket_in_use_list.append(69)
        print("THIS IS SOCKET_69 ", socket_69)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)


    async def socket_70(self,user_id):
        global socket_70, socket_in_use, socket_in_use_list
        socket_70[user_id] = time.time()
        socket_in_use[user_id] = '70'
        socket_in_use_list.append(70)
        print("THIS IS SOCKET_70 ", socket_70)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)


    async def socket_71(self,user_id):
        global socket_71, socket_in_use, socket_in_use_list
        socket_71[user_id] = time.time()
        socket_in_use[user_id] = '71'
        socket_in_use_list.append(71)
        print("THIS IS SOCKET_71 ", socket_71)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)


    async def socket_72(self,user_id):
        global socket_72, socket_in_use, socket_in_use_list
        socket_72[user_id] = time.time()
        socket_in_use[user_id] = '72'
        socket_in_use_list.append(72)
        print("THIS IS SOCKET_72 ", socket_72)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)


    async def socket_73(self,user_id):
        global socket_73, socket_in_use, socket_in_use_list
        socket_73[user_id] = time.time()
        socket_in_use[user_id] = '73'
        socket_in_use_list.append(73)
        print("THIS IS SOCKET_73 ", socket_73)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)


    async def socket_74(self,user_id):
        global socket_74, socket_in_use, socket_in_use_list
        socket_74[user_id] = time.time()
        socket_in_use[user_id] = '74'
        socket_in_use_list.append(74)
        print("THIS IS SOCKET_74 ", socket_74)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)


    async def socket_75(self,user_id):
        global socket_75, socket_in_use, socket_in_use_list
        socket_75[user_id] = time.time()
        socket_in_use[user_id] = '75'
        socket_in_use_list.append(75)
        print("THIS IS SOCKET_75 ", socket_75)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)


    async def socket_76(self,user_id):
        global socket_76, socket_in_use, socket_in_use_list
        socket_76[user_id] = time.time()
        socket_in_use[user_id] = '76'
        socket_in_use_list.append(76)
        print("THIS IS SOCKET_76 ", socket_76)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)


    async def socket_77(self,user_id):
        global socket_77, socket_in_use, socket_in_use_list
        socket_77[user_id] = time.time()
        socket_in_use[user_id] = '77'
        socket_in_use_list.append(77)
        print("THIS IS SOCKET_77 ", socket_77)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)


    async def socket_78(self,user_id):
        global socket_78, socket_in_use, socket_in_use_list
        socket_78[user_id] = time.time()
        socket_in_use[user_id] = '78'
        socket_in_use_list.append(78)
        print("THIS IS SOCKET_78 ", socket_78)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)


    async def socket_79(self,user_id):
        global socket_79, socket_in_use, socket_in_use_list
        socket_79[user_id] = time.time()
        socket_in_use[user_id] = '79'
        socket_in_use_list.append(79)
        print("THIS IS SOCKET_79 ", socket_79)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)


    async def socket_80(self,user_id):
        global socket_80, socket_in_use, socket_in_use_list
        socket_80[user_id] = time.time()
        socket_in_use[user_id] = '80'
        socket_in_use_list.append(80)
        print("THIS IS SOCKET_80 ", socket_80)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)


    async def socket_81(self,user_id):
        global socket_81, socket_in_use, socket_in_use_list
        socket_81[user_id] = time.time()
        socket_in_use[user_id] = '81'
        socket_in_use_list.append(81)
        print("THIS IS SOCKET_81 ", socket_81)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)


    async def socket_82(self,user_id):
        global socket_82, socket_in_use, socket_in_use_list
        socket_82[user_id] = time.time()
        socket_in_use[user_id] = '82'
        socket_in_use_list.append(82)
        print("THIS IS SOCKET_82 ", socket_82)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)


    async def socket_83(self,user_id):
        global socket_83, socket_in_use, socket_in_use_list
        socket_83[user_id] = time.time()
        socket_in_use[user_id] = '83'
        socket_in_use_list.append(83)
        print("THIS IS SOCKET_83 ", socket_83)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)


    async def socket_84(self,user_id):
        global socket_84, socket_in_use, socket_in_use_list
        socket_84[user_id] = time.time()
        socket_in_use[user_id] = '84'
        socket_in_use_list.append(84)
        print("THIS IS SOCKET_84 ", socket_84)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)


    async def socket_85(self,user_id):
        global socket_85, socket_in_use, socket_in_use_list
        socket_85[user_id] = time.time()
        socket_in_use[user_id] = '85'
        socket_in_use_list.append(85)
        print("THIS IS SOCKET_85 ", socket_85)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)


    async def socket_86(self,user_id):
        global socket_86, socket_in_use, socket_in_use_list
        socket_86[user_id] = time.time()
        socket_in_use[user_id] = '86'
        socket_in_use_list.append(86)
        print("THIS IS SOCKET_86 ", socket_86)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)


    async def socket_87(self,user_id):
        global socket_87, socket_in_use, socket_in_use_list
        socket_87[user_id] = time.time()
        socket_in_use[user_id] = '87'
        socket_in_use_list.append(87)
        print("THIS IS SOCKET_87 ", socket_87)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)


    async def socket_88(self,user_id):
        global socket_88, socket_in_use, socket_in_use_list
        socket_88[user_id] = time.time()
        socket_in_use[user_id] = '88'
        socket_in_use_list.append(88)
        print("THIS IS SOCKET_88 ", socket_88)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)


    async def socket_89(self,user_id):
        global socket_89, socket_in_use, socket_in_use_list
        socket_89[user_id] = time.time()
        socket_in_use[user_id] = '89'
        socket_in_use_list.append(89)
        print("THIS IS SOCKET_89 ", socket_89)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)


    async def socket_90(self,user_id):
        global socket_90, socket_in_use, socket_in_use_list
        socket_90[user_id] = time.time()
        socket_in_use[user_id] = '90'
        socket_in_use_list.append(90)
        print("THIS IS SOCKET_90 ", socket_90)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)


    async def socket_91(self,user_id):
        global socket_91, socket_in_use, socket_in_use_list
        socket_91[user_id] = time.time()
        socket_in_use[user_id] = '91'
        socket_in_use_list.append(91)
        print("THIS IS SOCKET_91 ", socket_91)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)


    async def socket_92(self,user_id):
        global socket_92, socket_in_use, socket_in_use_list
        socket_92[user_id] = time.time()
        socket_in_use[user_id] = '92'
        socket_in_use_list.append(92)
        print("THIS IS SOCKET_92 ", socket_92)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)


    async def socket_93(self,user_id):
        global socket_93, socket_in_use, socket_in_use_list
        socket_93[user_id] = time.time()
        socket_in_use[user_id] = '93'
        socket_in_use_list.append(93)
        print("THIS IS SOCKET_93 ", socket_93)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)


    async def socket_94(self,user_id):
        global socket_94, socket_in_use, socket_in_use_list
        socket_94[user_id] = time.time()
        socket_in_use[user_id] = '94'
        socket_in_use_list.append(94)
        print("THIS IS SOCKET_94 ", socket_94)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)


    async def socket_95(self,user_id):
        global socket_95, socket_in_use, socket_in_use_list
        socket_95[user_id] = time.time()
        socket_in_use[user_id] = '95'
        socket_in_use_list.append(95)
        print("THIS IS SOCKET_95 ", socket_95)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)


    async def socket_96(self,user_id):
        global socket_96, socket_in_use, socket_in_use_list
        socket_96[user_id] = time.time()
        socket_in_use[user_id] = '96'
        socket_in_use_list.append(96)
        print("THIS IS SOCKET_96 ", socket_96)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)


    async def socket_97(self,user_id):
        global socket_97, socket_in_use, socket_in_use_list
        socket_97[user_id] = time.time()
        socket_in_use[user_id] = '97'
        socket_in_use_list.append(97)
        print("THIS IS SOCKET_97 ", socket_97)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)


    async def socket_98(self,user_id):
        global socket_98, socket_in_use, socket_in_use_list
        socket_98[user_id] = time.time()
        socket_in_use[user_id] = '98'
        socket_in_use_list.append(98)
        print("THIS IS SOCKET_98 ", socket_98)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)


    async def socket_99(self,user_id):
        global socket_99, socket_in_use, socket_in_use_list
        socket_99[user_id] = time.time()
        socket_in_use[user_id] = '99'
        socket_in_use_list.append(99)
        print("THIS IS SOCKET_99 ", socket_99)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)


    async def socket_100(self,user_id):
        global socket_100, socket_in_use, socket_in_use_list
        socket_100[user_id] = time.time()
        socket_in_use[user_id] = '100'
        socket_in_use_list.append(100)
        print("THIS IS SOCKET_100 ", socket_100)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)
    
    async def socket_101(self,user_id):
        global socket_101, socket_in_use, socket_in_use_list        
        socket_101[user_id] = time.time()
        socket_in_use[user_id] = '101'
        socket_in_use_list.append(101)
        print("THIS IS SOCKET_101 ", socket_101)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)    


    async def socket_102(self,user_id):
        global socket_102, socket_in_use, socket_in_use_list        
        socket_102[user_id] = time.time()
        socket_in_use[user_id] = '102'
        socket_in_use_list.append(102)
        print("THIS IS SOCKET_102 ", socket_102)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)    


    async def socket_103(self,user_id):
        global socket_103, socket_in_use, socket_in_use_list        
        socket_103[user_id] = time.time()
        socket_in_use[user_id] = '103'
        socket_in_use_list.append(103)
        print("THIS IS SOCKET_103 ", socket_103)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)


    async def socket_104(self,user_id):
        global socket_104, socket_in_use, socket_in_use_list
        socket_104[user_id] = time.time()
        socket_in_use[user_id] = '104'
        socket_in_use_list.append(104)
        print("THIS IS SOCKET_104 ", socket_104)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)


    async def socket_105(self,user_id):
        global socket_105, socket_in_use, socket_in_use_list
        socket_105[user_id] = time.time()
        socket_in_use[user_id] = '105'
        socket_in_use_list.append(105)
        print("THIS IS SOCKET_105 ", socket_105)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)


    async def socket_106(self,user_id):
        global socket_106, socket_in_use, socket_in_use_list
        socket_106[user_id] = time.time()
        socket_in_use[user_id] = '106'
        socket_in_use_list.append(106)
        print("THIS IS SOCKET_106 ", socket_106)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)


    async def socket_107(self,user_id):
        global socket_107, socket_in_use, socket_in_use_list
        socket_107[user_id] = time.time()
        socket_in_use[user_id] = '107'
        socket_in_use_list.append(107)
        print("THIS IS SOCKET_107 ", socket_107)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)


    async def socket_108(self,user_id):
        global socket_108, socket_in_use, socket_in_use_list
        socket_108[user_id] = time.time()
        socket_in_use[user_id] = '108'
        socket_in_use_list.append(108)
        print("THIS IS SOCKET_108 ", socket_108)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)


    async def socket_109(self,user_id):
        global socket_109, socket_in_use, socket_in_use_list
        socket_109[user_id] = time.time()
        socket_in_use[user_id] = '109'
        socket_in_use_list.append(109)
        print("THIS IS SOCKET_109 ", socket_109)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)


    async def socket_110(self,user_id):
        global socket_110, socket_in_use, socket_in_use_list
        socket_110[user_id] = time.time()
        socket_in_use[user_id] = '110'
        socket_in_use_list.append(110)
        print("THIS IS SOCKET_110 ", socket_110)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)


    async def socket_111(self,user_id):
        global socket_111, socket_in_use, socket_in_use_list
        socket_111[user_id] = time.time()
        socket_in_use[user_id] = '111'
        socket_in_use_list.append(111)
        print("THIS IS SOCKET_111 ", socket_111)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)


    async def socket_112(self,user_id):
        global socket_112, socket_in_use, socket_in_use_list
        socket_112[user_id] = time.time()
        socket_in_use[user_id] = '112'
        socket_in_use_list.append(112)
        print("THIS IS SOCKET_112 ", socket_112)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)


    async def socket_113(self,user_id):
        global socket_113, socket_in_use, socket_in_use_list
        socket_113[user_id] = time.time()
        socket_in_use[user_id] = '113'
        socket_in_use_list.append(113)
        print("THIS IS SOCKET_113 ", socket_113)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)


    async def socket_114(self,user_id):
        global socket_114, socket_in_use, socket_in_use_list
        socket_114[user_id] = time.time()
        socket_in_use[user_id] = '114'
        socket_in_use_list.append(114)
        print("THIS IS SOCKET_114 ", socket_114)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)


    async def socket_115(self,user_id):
        global socket_115, socket_in_use, socket_in_use_list
        socket_115[user_id] = time.time()
        socket_in_use[user_id] = '115'
        socket_in_use_list.append(115)
        print("THIS IS SOCKET_115 ", socket_115)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)


    async def socket_116(self,user_id):
        global socket_116, socket_in_use, socket_in_use_list
        socket_116[user_id] = time.time()
        socket_in_use[user_id] = '116'
        socket_in_use_list.append(116)
        print("THIS IS SOCKET_116 ", socket_116)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)


    async def socket_117(self,user_id):
        global socket_117, socket_in_use, socket_in_use_list
        socket_117[user_id] = time.time()
        socket_in_use[user_id] = '117'
        socket_in_use_list.append(117)
        print("THIS IS SOCKET_117 ", socket_117)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)


    async def socket_118(self,user_id):
        global socket_118, socket_in_use, socket_in_use_list
        socket_118[user_id] = time.time()
        socket_in_use[user_id] = '118'
        socket_in_use_list.append(118)
        print("THIS IS SOCKET_118 ", socket_118)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)


    async def socket_119(self,user_id):
        global socket_119, socket_in_use, socket_in_use_list
        socket_119[user_id] = time.time()
        socket_in_use[user_id] = '119'
        socket_in_use_list.append(119)
        print("THIS IS SOCKET_119 ", socket_119)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)


    async def socket_120(self,user_id):
        global socket_120, socket_in_use, socket_in_use_list
        socket_120[user_id] = time.time()
        socket_in_use[user_id] = '120'
        socket_in_use_list.append(120)
        print("THIS IS SOCKET_120 ", socket_120)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)


    async def socket_121(self,user_id):
        global socket_121, socket_in_use, socket_in_use_list
        socket_121[user_id] = time.time()
        socket_in_use[user_id] = '121'
        socket_in_use_list.append(121)
        print("THIS IS SOCKET_121 ", socket_121)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)


    async def socket_122(self,user_id):
        global socket_122, socket_in_use, socket_in_use_list
        socket_122[user_id] = time.time()
        socket_in_use[user_id] = '122'
        socket_in_use_list.append(122)
        print("THIS IS SOCKET_122 ", socket_122)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)


    async def socket_123(self,user_id):
        global socket_123, socket_in_use, socket_in_use_list
        socket_123[user_id] = time.time()
        socket_in_use[user_id] = '123'
        socket_in_use_list.append(123)
        print("THIS IS SOCKET_123 ", socket_123)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)


    async def socket_124(self,user_id):
        global socket_124, socket_in_use, socket_in_use_list
        socket_124[user_id] = time.time()
        socket_in_use[user_id] = '124'
        socket_in_use_list.append(124)
        print("THIS IS SOCKET_124 ", socket_124)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)


    async def socket_125(self,user_id):
        global socket_125, socket_in_use, socket_in_use_list
        socket_125[user_id] = time.time()
        socket_in_use[user_id] = '125'
        socket_in_use_list.append(125)
        print("THIS IS SOCKET_125 ", socket_125)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)


    async def socket_126(self,user_id):
        global socket_126, socket_in_use, socket_in_use_list
        socket_126[user_id] = time.time()
        socket_in_use[user_id] = '126'
        socket_in_use_list.append(126)
        print("THIS IS SOCKET_126 ", socket_126)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)


    async def socket_127(self,user_id):
        global socket_127, socket_in_use, socket_in_use_list
        socket_127[user_id] = time.time()
        socket_in_use[user_id] = '127'
        socket_in_use_list.append(127)
        print("THIS IS SOCKET_127 ", socket_127)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)


    async def socket_128(self,user_id):
        global socket_128, socket_in_use, socket_in_use_list
        socket_128[user_id] = time.time()
        socket_in_use[user_id] = '128'
        socket_in_use_list.append(128)
        print("THIS IS SOCKET_128 ", socket_128)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)


    async def socket_129(self,user_id):
        global socket_129, socket_in_use, socket_in_use_list
        socket_129[user_id] = time.time()
        socket_in_use[user_id] = '129'
        socket_in_use_list.append(129)
        print("THIS IS SOCKET_129 ", socket_129)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)


    async def socket_130(self,user_id):
        global socket_130, socket_in_use, socket_in_use_list
        socket_130[user_id] = time.time()
        socket_in_use[user_id] = '130'
        socket_in_use_list.append(130)
        print("THIS IS SOCKET_130 ", socket_130)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)


    async def socket_131(self,user_id):
        global socket_131, socket_in_use, socket_in_use_list
        socket_131[user_id] = time.time()
        socket_in_use[user_id] = '131'
        socket_in_use_list.append(131)
        print("THIS IS SOCKET_131 ", socket_131)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)


    async def socket_132(self,user_id):
        global socket_132, socket_in_use, socket_in_use_list
        socket_132[user_id] = time.time()
        socket_in_use[user_id] = '132'
        socket_in_use_list.append(132)
        print("THIS IS SOCKET_132 ", socket_132)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)


    async def socket_133(self,user_id):
        global socket_133, socket_in_use, socket_in_use_list
        socket_133[user_id] = time.time()
        socket_in_use[user_id] = '133'
        socket_in_use_list.append(133)
        print("THIS IS SOCKET_133 ", socket_133)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)


    async def socket_134(self,user_id):
        global socket_134, socket_in_use, socket_in_use_list
        socket_134[user_id] = time.time()
        socket_in_use[user_id] = '134'
        socket_in_use_list.append(134)
        print("THIS IS SOCKET_134 ", socket_134)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)


    async def socket_135(self,user_id):
        global socket_135, socket_in_use, socket_in_use_list
        socket_135[user_id] = time.time()
        socket_in_use[user_id] = '135'
        socket_in_use_list.append(135)
        print("THIS IS SOCKET_135 ", socket_135)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)


    async def socket_136(self,user_id):
        global socket_136, socket_in_use, socket_in_use_list
        socket_136[user_id] = time.time()
        socket_in_use[user_id] = '136'
        socket_in_use_list.append(136)
        print("THIS IS SOCKET_136 ", socket_136)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)


    async def socket_137(self,user_id):
        global socket_137, socket_in_use, socket_in_use_list
        socket_137[user_id] = time.time()
        socket_in_use[user_id] = '137'
        socket_in_use_list.append(137)
        print("THIS IS SOCKET_137 ", socket_137)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)


    async def socket_138(self,user_id):
        global socket_138, socket_in_use, socket_in_use_list
        socket_138[user_id] = time.time()
        socket_in_use[user_id] = '138'
        socket_in_use_list.append(138)
        print("THIS IS SOCKET_138 ", socket_138)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)


    async def socket_139(self,user_id):
        global socket_139, socket_in_use, socket_in_use_list
        socket_139[user_id] = time.time()
        socket_in_use[user_id] = '139'
        socket_in_use_list.append(139)
        print("THIS IS SOCKET_139 ", socket_139)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)


    async def socket_140(self,user_id):
        global socket_140, socket_in_use, socket_in_use_list
        socket_140[user_id] = time.time()
        socket_in_use[user_id] = '140'
        socket_in_use_list.append(140)
        print("THIS IS SOCKET_140 ", socket_140)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)


    async def socket_141(self,user_id):
        global socket_141, socket_in_use, socket_in_use_list
        socket_141[user_id] = time.time()
        socket_in_use[user_id] = '141'
        socket_in_use_list.append(141)
        print("THIS IS SOCKET_141 ", socket_141)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)


    async def socket_142(self,user_id):
        global socket_142, socket_in_use, socket_in_use_list
        socket_142[user_id] = time.time()
        socket_in_use[user_id] = '142'
        socket_in_use_list.append(142)
        print("THIS IS SOCKET_142 ", socket_142)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)


    async def socket_143(self,user_id):
        global socket_143, socket_in_use, socket_in_use_list
        socket_143[user_id] = time.time()
        socket_in_use[user_id] = '143'
        socket_in_use_list.append(143)
        print("THIS IS SOCKET_143 ", socket_143)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)


    async def socket_144(self,user_id):
        global socket_144, socket_in_use, socket_in_use_list
        socket_144[user_id] = time.time()
        socket_in_use[user_id] = '144'
        socket_in_use_list.append(144)
        print("THIS IS SOCKET_144 ", socket_144)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)


    async def socket_145(self,user_id):
        global socket_145, socket_in_use, socket_in_use_list
        socket_145[user_id] = time.time()
        socket_in_use[user_id] = '145'
        socket_in_use_list.append(145)
        print("THIS IS SOCKET_145 ", socket_145)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)


    async def socket_146(self,user_id):
        global socket_146, socket_in_use, socket_in_use_list
        socket_146[user_id] = time.time()
        socket_in_use[user_id] = '146'
        socket_in_use_list.append(146)
        print("THIS IS SOCKET_146 ", socket_146)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)


    async def socket_147(self,user_id):
        global socket_147, socket_in_use, socket_in_use_list
        socket_147[user_id] = time.time()
        socket_in_use[user_id] = '147'
        socket_in_use_list.append(147)
        print("THIS IS SOCKET_147 ", socket_147)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)


    async def socket_148(self,user_id):
        global socket_148, socket_in_use, socket_in_use_list
        socket_148[user_id] = time.time()
        socket_in_use[user_id] = '148'
        socket_in_use_list.append(148)
        print("THIS IS SOCKET_148 ", socket_148)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)


    async def socket_149(self,user_id):
        global socket_149, socket_in_use, socket_in_use_list
        socket_149[user_id] = time.time()
        socket_in_use[user_id] = '149'
        socket_in_use_list.append(149)
        print("THIS IS SOCKET_149 ", socket_149)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)


    async def socket_150(self,user_id):
        global socket_150, socket_in_use, socket_in_use_list
        socket_150[user_id] = time.time()
        socket_in_use[user_id] = '150'
        socket_in_use_list.append(150)
        print("THIS IS SOCKET_150 ", socket_150)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)


    async def socket_151(self,user_id):
        global socket_151, socket_in_use, socket_in_use_list
        socket_151[user_id] = time.time()
        socket_in_use[user_id] = '151'
        socket_in_use_list.append(151)
        print("THIS IS SOCKET_151 ", socket_151)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)


    async def socket_152(self,user_id):
        global socket_152, socket_in_use, socket_in_use_list
        socket_152[user_id] = time.time()
        socket_in_use[user_id] = '152'
        socket_in_use_list.append(152)
        print("THIS IS SOCKET_152 ", socket_152)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)


    async def socket_153(self,user_id):
        global socket_153, socket_in_use, socket_in_use_list
        socket_153[user_id] = time.time()
        socket_in_use[user_id] = '153'
        socket_in_use_list.append(153)
        print("THIS IS SOCKET_153 ", socket_153)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)


    async def socket_154(self,user_id):
        global socket_154, socket_in_use, socket_in_use_list
        socket_154[user_id] = time.time()
        socket_in_use[user_id] = '154'
        socket_in_use_list.append(154)
        print("THIS IS SOCKET_154 ", socket_154)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)


    async def socket_155(self,user_id):
        global socket_155, socket_in_use, socket_in_use_list
        socket_155[user_id] = time.time()
        socket_in_use[user_id] = '155'
        socket_in_use_list.append(155)
        print("THIS IS SOCKET_155 ", socket_155)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)


    async def socket_156(self,user_id):
        global socket_156, socket_in_use, socket_in_use_list
        socket_156[user_id] = time.time()
        socket_in_use[user_id] = '156'
        socket_in_use_list.append(156)
        print("THIS IS SOCKET_156 ", socket_156)
        print("THIS IS SOCKET_IN_USE ", socket_in_use)
        print("THIS IS SOCKET_IN_USE_LIST ", socket_in_use_list)


    async def socket_use_1(self,user_id):
        global sio
        if socket_1 and time.time() -  socket_1[list(socket_1.keys())[0]] > 180: 
            del socket_in_use[list(socket_1.keys())[0]]
            socket_in_use_list.remove(1)
            socket_1.clear()
            await self.empty_sock_check(user_id)
            await aio.disconnect()
            # sio = socketio.AsyncClient()
            await asyncio.sleep(0.1)
            await aio.connect('http://localhost:5005/socket.io')
        else: 
            pass
    
    async def socket_use_2(self,user_id):
        global tsio
        if socket_2 and time.time() -  socket_2[list(socket_2.keys())[0]] > 180: 
            del socket_in_use[list(socket_2.keys())[0]]
            socket_in_use_list.remove(2)
            socket_2.clear()
            await self.empty_sock_check(user_id)
            await bio.disconnect()
            # tsio = socketio.AsyncClient()
            await asyncio.sleep(0.1)
            await bio.connect('http://localhost:5005/socket.io')
        else: 
            pass

    async def socket_use_3(self,user_id):
        global usio
        if socket_3 and time.time() -  socket_3[list(socket_3.keys())[0]] > 180: 
            del socket_in_use[list(socket_3.keys())[0]]
            socket_in_use_list.remove(3)
            socket_3.clear()
            await self.empty_sock_check(user_id)
            await cio.disconnect()
            # usio = socketio.AsyncClient()
            await asyncio.sleep(0.1)
            await cio.connect('http://localhost:5005/socket.io')
        else: 
            pass

    async def socket_use_4(self,user_id):
        global vsio
        if socket_4 and time.time() -  socket_4[list(socket_4.keys())[0]] > 180: 
            del socket_in_use[list(socket_4.keys())[0]]
            socket_in_use_list.remove(4)
            socket_4.clear()
            await self.empty_sock_check(user_id)
            await dio.disconnect()
            # vsio = socketio.AsyncClient()
            await asyncio.sleep(0.1)
            await dio.connect('http://localhost:5005/socket.io')
        else: 
            pass

    async def socket_use_5(self,user_id):
        global sio
        if socket_5 and time.time() -  socket_5[list(socket_5.keys())[0]] > 180: 
            del socket_in_use[list(socket_5.keys())[0]]
            socket_in_use_list.remove(5)
            socket_5.clear()
            await self.empty_sock_check(user_id)
            await eio.disconnect()
            # wsio = socketio.AsyncClient()
            await asyncio.sleep(0.1)
            await eio.connect('http://localhost:5005/socket.io')
        else: 
            pass
    
    async def socket_use_6(self,user_id):
        global sio
        if socket_6 and time.time() -  socket_6[list(socket_6.keys())[0]] > 180: 
            del socket_in_use[list(socket_6.keys())[0]]
            socket_in_use_list.remove(6)
            socket_6.clear()
            await self.empty_sock_check(user_id)
            await fio.disconnect()
            # wsio = socketio.AsyncClient()
            await asyncio.sleep(0.1)
            await fio.connect('http://localhost:5005/socket.io')
        else: 
            pass
    
    async def socket_use_7(self,user_id):
        global sio
        if socket_7 and time.time() -  socket_7[list(socket_7.keys())[0]] > 180: 
            del socket_in_use[list(socket_7.keys())[0]]
            socket_in_use_list.remove(7)
            socket_7.clear()
            await self.empty_sock_check(user_id)
            await gio.disconnect()
            # wsio = socketio.AsyncClient()
            await asyncio.sleep(0.1)
            await gio.connect('http://localhost:5005/socket.io')
        else: 
            pass
    
    async def socket_use_8(self,user_id):
        global sio
        if socket_8 and time.time() -  socket_8[list(socket_8.keys())[0]] > 180: 
            del socket_in_use[list(socket_8.keys())[0]]
            socket_in_use_list.remove(8)
            socket_8.clear()
            await self.empty_sock_check(user_id)
            await hio.disconnect()
            # wsio = socketio.AsyncClient()
            await asyncio.sleep(0.1)
            await hio.connect('http://localhost:5005/socket.io')
        else: 
            pass
    
    async def socket_use_9(self,user_id):
        global sio
        if socket_9 and time.time() -  socket_9[list(socket_9.keys())[0]] > 180: 
            del socket_in_use[list(socket_9.keys())[0]]
            socket_in_use_list.remove(9)
            socket_9.clear()
            await self.empty_sock_check(user_id)
            await iio.disconnect()
            # wsio = socketio.AsyncClient()
            await asyncio.sleep(0.1)
            await iio.connect('http://localhost:5005/socket.io')
        else: 
            pass
    
    async def socket_use_10(self,user_id):
        global sio
        if socket_10 and time.time() -  socket_10[list(socket_10.keys())[0]] > 180: 
            del socket_in_use[list(socket_10.keys())[0]]
            socket_in_use_list.remove(10)
            socket_10.clear()
            await self.empty_sock_check(user_id)
            await jio.disconnect()
            # wsio = socketio.AsyncClient()
            await asyncio.sleep(0.1)
            await jio.connect('http://localhost:5005/socket.io')
        else: 
            pass
    
    async def socket_use_11(self,user_id):
        global sio
        if socket_11 and time.time() -  socket_11[list(socket_11.keys())[0]] > 180: 
            del socket_in_use[list(socket_11.keys())[0]]
            socket_in_use_list.remove(11)
            socket_11.clear()
            await self.empty_sock_check(user_id)
            await kio.disconnect()
            # wsio = socketio.AsyncClient()
            await asyncio.sleep(0.1)
            await kio.connect('http://localhost:5005/socket.io')
        else: 
            pass
    
    async def socket_use_12(self,user_id):
        global sio
        if socket_12 and time.time() -  socket_12[list(socket_12.keys())[0]] > 180: 
            del socket_in_use[list(socket_12.keys())[0]]
            socket_in_use_list.remove(12)
            socket_12.clear()
            await self.empty_sock_check(user_id)
            await lio.disconnect()
            # wsio = socketio.AsyncClient()
            await asyncio.sleep(0.1)
            await lio.connect('http://localhost:5005/socket.io')
        else: 
            pass
    
    async def socket_use_13(self,user_id):
        global sio
        if socket_13 and time.time() -  socket_13[list(socket_13.keys())[0]] > 180: 
            del socket_in_use[list(socket_13.keys())[0]]
            socket_in_use_list.remove(13)
            socket_13.clear()
            await self.empty_sock_check(user_id)
            await mio.disconnect()
            # wsio = socketio.AsyncClient()
            await asyncio.sleep(0.1)
            await mio.connect('http://localhost:5005/socket.io')
        else: 
            pass
    
    async def socket_use_14(self,user_id):
        global sio
        if socket_14 and time.time() -  socket_14[list(socket_14.keys())[0]] > 180: 
            del socket_in_use[list(socket_14.keys())[0]]
            socket_in_use_list.remove(14)
            socket_14.clear()
            await self.empty_sock_check(user_id)
            await nio.disconnect()
            # wsio = socketio.AsyncClient()
            await asyncio.sleep(0.1)
            await nio.connect('http://localhost:5005/socket.io')
        else: 
            pass
    
    async def socket_use_15(self,user_id):
        global sio
        if socket_15 and time.time() -  socket_15[list(socket_15.keys())[0]] > 180: 
            del socket_in_use[list(socket_15.keys())[0]]
            socket_in_use_list.remove(15)
            socket_15.clear()
            await self.empty_sock_check(user_id)
            await oio.disconnect()
            # wsio = socketio.AsyncClient()
            await asyncio.sleep(0.1)
            await oio.connect('http://localhost:5005/socket.io')
        else: 
            pass

    async def socket_use_16(self,user_id):
        global sio
        if socket_16 and time.time() -  socket_16[list(socket_16.keys())[0]] > 180: 
            del socket_in_use[list(socket_16.keys())[0]]
            socket_in_use_list.remove(16)
            socket_16.clear()
            await self.empty_sock_check(user_id)
            await pio.disconnect()
            # wsio = socketio.AsyncClient()
            await asyncio.sleep(0.1)
            await pio.connect('http://localhost:5005/socket.io')
        else: 
            pass
    
    async def socket_use_17(self,user_id):
        global sio
        if socket_17 and time.time() -  socket_17[list(socket_17.keys())[0]] > 180: 
            del socket_in_use[list(socket_17.keys())[0]]
            socket_in_use_list.remove(17)
            socket_17.clear()
            await self.empty_sock_check(user_id)
            await qio.disconnect()
            # wsio = socketio.AsyncClient()
            await asyncio.sleep(0.1)
            await qio.connect('http://localhost:5005/socket.io')
        else: 
            pass
    
    async def socket_use_18(self,user_id):
        global sio
        if socket_18 and time.time() -  socket_18[list(socket_18.keys())[0]] > 180: 
            del socket_in_use[list(socket_18.keys())[0]]
            socket_in_use_list.remove(18)
            socket_18.clear()
            await self.empty_sock_check(user_id)
            await rio.disconnect()
            # wsio = socketio.AsyncClient()
            await asyncio.sleep(0.1)
            await rio.connect('http://localhost:5005/socket.io')
        else: 
            pass
    
    async def socket_use_19(self,user_id):
        global sio
        if socket_19 and time.time() -  socket_19[list(socket_19.keys())[0]] > 180: 
            del socket_in_use[list(socket_19.keys())[0]]
            socket_in_use_list.remove(19)
            socket_19.clear()
            await self.empty_sock_check(user_id)
            await sio.disconnect()
            # wsio = socketio.AsyncClient()
            await asyncio.sleep(0.1)
            await sio.connect('http://localhost:5005/socket.io')
        else: 
            pass
    
    async def socket_use_20(self,user_id):
        global sio
        if socket_20 and time.time() -  socket_20[list(socket_20.keys())[0]] > 180: 
            del socket_in_use[list(socket_20.keys())[0]]
            socket_in_use_list.remove(20)
            socket_20.clear()
            await self.empty_sock_check(user_id)
            await tsio.disconnect()
            # wsio = socketio.AsyncClient()
            await asyncio.sleep(0.1)
            await tsio.connect('http://localhost:5005/socket.io')
        else: 
            pass
    
    async def socket_use_21(self,user_id):
        global sio
        if socket_21 and time.time() -  socket_21[list(socket_21.keys())[0]] > 180: 
            del socket_in_use[list(socket_21.keys())[0]]
            socket_in_use_list.remove(21)
            socket_21.clear()
            await self.empty_sock_check(user_id)
            await usio.disconnect()
            # wsio = socketio.AsyncClient()
            await asyncio.sleep(0.1)
            await usio.connect('http://localhost:5005/socket.io')
        else: 
            pass

    async def socket_use_22(self,user_id):
        global sio
        if socket_22 and time.time() -  socket_22[list(socket_22.keys())[0]] > 180: 
            del socket_in_use[list(socket_22.keys())[0]]
            socket_in_use_list.remove(22)
            socket_22.clear()
            await self.empty_sock_check(user_id)
            await vsio.disconnect()
            # wsio = socketio.AsyncClient()
            await asyncio.sleep(0.1)
            await vsio.connect('http://localhost:5005/socket.io')
        else: 
            pass
    
    async def socket_use_23(self,user_id):
        global sio
        if socket_23 and time.time() -  socket_23[list(socket_23.keys())[0]] > 180: 
            del socket_in_use[list(socket_23.keys())[0]]
            socket_in_use_list.remove(23)
            socket_23.clear()
            await self.empty_sock_check(user_id)
            await wsio.disconnect()
            # wsio = socketio.AsyncClient()
            await asyncio.sleep(0.1)
            await wsio.connect('http://localhost:5005/socket.io')
        else: 
            pass
    
    async def socket_use_24(self,user_id):
        global sio
        if socket_24 and time.time() -  socket_24[list(socket_24.keys())[0]] > 180: 
            del socket_in_use[list(socket_24.keys())[0]]
            socket_in_use_list.remove(24)
            socket_24.clear()
            await self.empty_sock_check(user_id)
            await xio.disconnect()
            # wsio = socketio.AsyncClient()
            await asyncio.sleep(0.1)
            await xio.connect('http://localhost:5005/socket.io')
        else: 
            pass
    
    async def socket_use_25(self,user_id):
        global sio
        if socket_25 and time.time() -  socket_25[list(socket_25.keys())[0]] > 180: 
            del socket_in_use[list(socket_25.keys())[0]]
            socket_in_use_list.remove(25)
            socket_25.clear()
            await self.empty_sock_check(user_id)
            await yio.disconnect()
            # wsio = socketio.AsyncClient()
            await asyncio.sleep(0.1)
            await yio.connect('http://localhost:5005/socket.io')
        else: 
            pass
    
    async def socket_use_26(self,user_id):
        global sio
        if socket_26 and time.time() -  socket_26[list(socket_26.keys())[0]] > 180: 
            del socket_in_use[list(socket_26.keys())[0]]
            socket_in_use_list.remove(26)
            socket_26.clear()
            await self.empty_sock_check(user_id)
            await zio.disconnect()
            # wsio = socketio.AsyncClient()
            await asyncio.sleep(0.1)
            await zio.connect('http://localhost:5005/socket.io')
        else: 
            pass

    #-----

    async def socket_use_27(self,user_id):
        global sio
        if socket_27 and time.time() -  socket_27[list(socket_27.keys())[0]] > 180: 
            del socket_in_use[list(socket_27.keys())[0]]
            socket_in_use_list.remove(27)
            socket_27.clear()
            await self.empty_sock_check(user_id)
            await aaio.disconnect()
            # sio = socketio.AsyncClient()
            await asyncio.sleep(0.1)
            await aaio.connect('http://localhost:5005/socket.io')
        else: 
            pass
    
    async def socket_use_28(self,user_id):
        global tsio
        if socket_28 and time.time() -  socket_28[list(socket_28.keys())[0]] > 180: 
            del socket_in_use[list(socket_28.keys())[0]]
            socket_in_use_list.remove(28)
            socket_28.clear()
            await self.empty_sock_check(user_id)
            await abio.disconnect()
            # tsio = socketio.AsyncClient()
            await asyncio.sleep(0.1)
            await abio.connect('http://localhost:5005/socket.io')
        else: 
            pass

    async def socket_use_29(self,user_id):
        global usio
        if socket_29 and time.time() -  socket_29[list(socket_29.keys())[0]] > 180: 
            del socket_in_use[list(socket_29.keys())[0]]
            socket_in_use_list.remove(29)
            socket_29.clear()
            await self.empty_sock_check(user_id)
            await cio.disconnect()
            # usio = socketio.AsyncClient()
            await asyncio.sleep(0.1)
            await acio.connect('http://localhost:5005/socket.io')
        else: 
            pass

    async def socket_use_30(self,user_id):
        global vsio
        if socket_30 and time.time() -  socket_30[list(socket_30.keys())[0]] > 180: 
            del socket_in_use[list(socket_30.keys())[0]]
            socket_in_use_list.remove(30)
            socket_30.clear()
            await self.empty_sock_check(user_id)
            await adio.disconnect()
            # vsio = socketio.AsyncClient()
            await asyncio.sleep(0.1)
            await adio.connect('http://localhost:5005/socket.io')
        else: 
            pass

    async def socket_use_31(self,user_id):
        global sio
        if socket_31 and time.time() -  socket_31[list(socket_31.keys())[0]] > 180: 
            del socket_in_use[list(socket_31.keys())[0]]
            socket_in_use_list.remove(31)
            socket_31.clear()
            await self.empty_sock_check(user_id)
            await aeio.disconnect()
            # wsio = socketio.AsyncClient()
            await asyncio.sleep(0.1)
            await aeio.connect('http://localhost:5005/socket.io')
        else: 
            pass
    
    async def socket_use_32(self,user_id):
        global sio
        if socket_32 and time.time() -  socket_32[list(socket_32.keys())[0]] > 180: 
            del socket_in_use[list(socket_32.keys())[0]]
            socket_in_use_list.remove(32)
            socket_32.clear()
            await self.empty_sock_check(user_id)
            await afio.disconnect()
            # wsio = socketio.AsyncClient()
            await asyncio.sleep(0.1)
            await afio.connect('http://localhost:5005/socket.io')
        else: 
            pass
    
    async def socket_use_33(self,user_id):
        global sio
        if socket_33 and time.time() -  socket_33[list(socket_33.keys())[0]] > 180: 
            del socket_in_use[list(socket_33.keys())[0]]
            socket_in_use_list.remove(33)
            socket_33.clear()
            await self.empty_sock_check(user_id)
            await agio.disconnect()
            # wsio = socketio.AsyncClient()
            await asyncio.sleep(0.1)
            await agio.connect('http://localhost:5005/socket.io')
        else: 
            pass
    
    async def socket_use_34(self,user_id):
        global sio
        if socket_34 and time.time() -  socket_34[list(socket_34.keys())[0]] > 180: 
            del socket_in_use[list(socket_34.keys())[0]]
            socket_in_use_list.remove(34)
            socket_34.clear()
            await self.empty_sock_check(user_id)
            await ahio.disconnect()
            # wsio = socketio.AsyncClient()
            await asyncio.sleep(0.1)
            await ahio.connect('http://localhost:5005/socket.io')
        else: 
            pass
    
    async def socket_use_35(self,user_id):
        global sio
        if socket_35 and time.time() -  socket_35[list(socket_35.keys())[0]] > 180: 
            del socket_in_use[list(socket_35.keys())[0]]
            socket_in_use_list.remove(35)
            socket_35.clear()
            await self.empty_sock_check(user_id)
            await aiio.disconnect()
            # wsio = socketio.AsyncClient()
            await asyncio.sleep(0.1)
            await aiio.connect('http://localhost:5005/socket.io')
        else: 
            pass
    
    async def socket_use_36(self,user_id):
        global sio
        if socket_36 and time.time() -  socket_36[list(socket_36.keys())[0]] > 180: 
            del socket_in_use[list(socket_36.keys())[0]]
            socket_in_use_list.remove(36)
            socket_36.clear()
            await self.empty_sock_check(user_id)
            await ajio.disconnect()
            # wsio = socketio.AsyncClient()
            await asyncio.sleep(0.1)
            await ajio.connect('http://localhost:5005/socket.io')
        else: 
            pass
    
    async def socket_use_37(self,user_id):
        global sio
        if socket_37 and time.time() -  socket_37[list(socket_37.keys())[0]] > 180: 
            del socket_in_use[list(socket_37.keys())[0]]
            socket_in_use_list.remove(37)
            socket_37.clear()
            await self.empty_sock_check(user_id)
            await akio.disconnect()
            # wsio = socketio.AsyncClient()
            await asyncio.sleep(0.1)
            await akio.connect('http://localhost:5005/socket.io')
        else: 
            pass
    
    async def socket_use_38(self,user_id):
        global sio
        if socket_38 and time.time() -  socket_38[list(socket_38.keys())[0]] > 180: 
            del socket_in_use[list(socket_38.keys())[0]]
            socket_in_use_list.remove(38)
            socket_38.clear()
            await self.empty_sock_check(user_id)
            await alio.disconnect()
            # wsio = socketio.AsyncClient()
            await asyncio.sleep(0.1)
            await alio.connect('http://localhost:5005/socket.io')
        else:
            pass
    
    async def socket_use_39(self,user_id):
        global sio
        if socket_39 and time.time() -  socket_39[list(socket_39.keys())[0]] > 180: 
            del socket_in_use[list(socket_39.keys())[0]]
            socket_in_use_list.remove(39)
            socket_39.clear()
            await self.empty_sock_check(user_id)
            await amio.disconnect()
            # wsio = socketio.AsyncClient()
            await asyncio.sleep(0.1)
            await amio.connect('http://localhost:5005/socket.io')
        else: 
            pass
    
    async def socket_use_40(self,user_id):
        global sio
        if socket_40 and time.time() -  socket_40[list(socket_40.keys())[0]] > 180: 
            del socket_in_use[list(socket_40.keys())[0]]
            socket_in_use_list.remove(40)
            socket_40.clear()
            await self.empty_sock_check(user_id)
            await anio.disconnect()
            # wsio = socketio.AsyncClient()
            await asyncio.sleep(0.1)
            await anio.connect('http://localhost:5005/socket.io')
        else: 
            pass
    
    async def socket_use_41(self,user_id):
        global sio
        if socket_41 and time.time() -  socket_41[list(socket_41.keys())[0]] > 180: 
            del socket_in_use[list(socket_41.keys())[0]]
            socket_in_use_list.remove(41)
            socket_41.clear()
            await self.empty_sock_check(user_id)
            await aoio.disconnect()
            # wsio = socketio.AsyncClient()
            await asyncio.sleep(0.1)
            await aoio.connect('http://localhost:5005/socket.io')
        else: 
            pass

    async def socket_use_42(self,user_id):
        global sio
        if socket_42 and time.time() -  socket_42[list(socket_42.keys())[0]] > 180: 
            del socket_in_use[list(socket_42.keys())[0]]
            socket_in_use_list.remove(42)
            socket_42.clear()
            await self.empty_sock_check(user_id)
            await apio.disconnect()
            # wsio = socketio.AsyncClient()
            await asyncio.sleep(0.1)
            await apio.connect('http://localhost:5005/socket.io')
        else: 
            pass
    
    async def socket_use_43(self,user_id):
        global sio
        if socket_43 and time.time() -  socket_43[list(socket_43.keys())[0]] > 180: 
            del socket_in_use[list(socket_43.keys())[0]]
            socket_in_use_list.remove(43)
            socket_43.clear()
            await self.empty_sock_check(user_id)
            await aqio.disconnect()
            # wsio = socketio.AsyncClient()
            await asyncio.sleep(0.1)
            await aqio.connect('http://localhost:5005/socket.io')
        else: 
            pass
    
    async def socket_use_44(self,user_id):
        global sio
        if socket_44 and time.time() -  socket_44[list(socket_44.keys())[0]] > 180: 
            del socket_in_use[list(socket_44.keys())[0]]
            socket_in_use_list.remove(44)
            socket_44.clear()
            await self.empty_sock_check(user_id)
            await ario.disconnect()
            # wsio = socketio.AsyncClient()
            await asyncio.sleep(0.1)
            await ario.connect('http://localhost:5005/socket.io')
        else: 
            pass
    
    async def socket_use_45(self,user_id):
        global sio
        if socket_45 and time.time() -  socket_45[list(socket_45.keys())[0]] > 180: 
            del socket_in_use[list(socket_45.keys())[0]]
            socket_in_use_list.remove(45)
            socket_45.clear()
            await self.empty_sock_check(user_id)
            await asio.disconnect()
            # wsio = socketio.AsyncClient()
            await asyncio.sleep(0.1)
            await asio.connect('http://localhost:5005/socket.io')
        else: 
            pass
    
    async def socket_use_46(self,user_id):
        global sio
        if socket_46 and time.time() -  socket_46[list(socket_46.keys())[0]] > 180: 
            del socket_in_use[list(socket_46.keys())[0]]
            socket_in_use_list.remove(46)
            socket_46.clear()
            await self.empty_sock_check(user_id)
            await atio.disconnect()
            # wsio = socketio.AsyncClient()
            await asyncio.sleep(0.1)
            await atio.connect('http://localhost:5005/socket.io')
        else: 
            pass
    
    async def socket_use_47(self,user_id):
        global sio
        if socket_47 and time.time() -  socket_47[list(socket_47.keys())[0]] > 180: 
            del socket_in_use[list(socket_47.keys())[0]]
            socket_in_use_list.remove(47)
            socket_47.clear()
            await self.empty_sock_check(user_id)
            await auio.disconnect()
            # wsio = socketio.AsyncClient()
            await asyncio.sleep(0.1)
            await auio.connect('http://localhost:5005/socket.io')
        else: 
            pass

    async def socket_use_48(self,user_id):
        global sio
        if socket_48 and time.time() -  socket_48[list(socket_48.keys())[0]] > 180: 
            del socket_in_use[list(socket_48.keys())[0]]
            socket_in_use_list.remove(48)
            socket_48.clear()
            await self.empty_sock_check(user_id)
            await avio.disconnect()
            # wsio = socketio.AsyncClient()
            await asyncio.sleep(0.1)
            await avio.connect('http://localhost:5005/socket.io')
        else: 
            pass
    
    async def socket_use_49(self,user_id):
        global sio
        if socket_49 and time.time() -  socket_49[list(socket_49.keys())[0]] > 180: 
            del socket_in_use[list(socket_49.keys())[0]]
            socket_in_use_list.remove(49)
            socket_49.clear()
            await self.empty_sock_check(user_id)
            await awio.disconnect()
            # wsio = socketio.AsyncClient()
            await asyncio.sleep(0.1)
            await awio.connect('http://localhost:5005/socket.io')
        else: 
            pass
    
    async def socket_use_50(self,user_id):
        global sio
        if socket_50 and time.time() -  socket_50[list(socket_50.keys())[0]] > 180: 
            del socket_in_use[list(socket_50.keys())[0]]
            socket_in_use_list.remove(50)
            socket_50.clear()
            await self.empty_sock_check(user_id)
            await axio.disconnect()
            # wsio = socketio.AsyncClient()
            await asyncio.sleep(0.1)
            await axio.connect('http://localhost:5005/socket.io')
        else: 
            pass
    
    async def socket_use_51(self,user_id):
        global sio
        if socket_51 and time.time() -  socket_51[list(socket_51.keys())[0]] > 180: 
            del socket_in_use[list(socket_51.keys())[0]]
            socket_in_use_list.remove(51)
            socket_51.clear()
            await self.empty_sock_check(user_id)
            await ayio.disconnect()
            # wsio = socketio.AsyncClient()
            await asyncio.sleep(0.1)
            await ayio.connect('http://localhost:5005/socket.io')
        else: 
            pass
    
    async def socket_use_52(self,user_id):
        global sio
        if socket_52 and time.time() -  socket_52[list(socket_52.keys())[0]] > 180: 
            del socket_in_use[list(socket_52.keys())[0]]
            socket_in_use_list.remove(52)
            socket_52.clear()
            await self.empty_sock_check(user_id)
            await azio.disconnect()
            # wsio = socketio.AsyncClient()
            await asyncio.sleep(0.1)
            await azio.connect('http://localhost:5005/socket.io')
        else: 
            pass
    
    #---b

    async def socket_use_53(self,user_id):
        global sio
        if socket_53 and time.time() -  socket_53[list(socket_52.keys())[0]] > 180: 
            del socket_in_use[list(socket_53.keys())[0]]
            socket_in_use_list.remove(53)
            socket_53.clear()
            await self.empty_sock_check(user_id)
            await baio.disconnect()
            await asyncio.sleep(0.1)
            await baio.connect('http://localhost:5005/socket.io')
        else: 
            pass   
    

    async def socket_use_54(self,user_id):
        global sio
        if socket_54 and time.time() -  socket_54[list(socket_52.keys())[0]] > 180: 
            del socket_in_use[list(socket_54.keys())[0]]
            socket_in_use_list.remove(54)
            socket_54.clear()
            await self.empty_sock_check(user_id)
            await bbio.disconnect()
            await asyncio.sleep(0.1)
            await bbio.connect('http://localhost:5005/socket.io')
        else:
            pass


    async def socket_use_55(self,user_id):
        global sio
        if socket_55 and time.time() -  socket_55[list(socket_52.keys())[0]] > 180:
            del socket_in_use[list(socket_55.keys())[0]]
            socket_in_use_list.remove(55)
            socket_55.clear()
            await self.empty_sock_check(user_id)
            await bcio.disconnect()
            await asyncio.sleep(0.1)
            await bcio.connect('http://localhost:5005/socket.io')
        else:
            pass


    async def socket_use_56(self,user_id):
        global sio
        if socket_56 and time.time() -  socket_56[list(socket_52.keys())[0]] > 180:
            del socket_in_use[list(socket_56.keys())[0]]
            socket_in_use_list.remove(56)
            socket_56.clear()
            await self.empty_sock_check(user_id)
            await bdio.disconnect()
            await asyncio.sleep(0.1)
            await bdio.connect('http://localhost:5005/socket.io')
        else:
            pass


    async def socket_use_57(self,user_id):
        global sio
        if socket_57 and time.time() -  socket_57[list(socket_52.keys())[0]] > 180:
            del socket_in_use[list(socket_57.keys())[0]]
            socket_in_use_list.remove(57)
            socket_57.clear()
            await self.empty_sock_check(user_id)
            await beio.disconnect()
            await asyncio.sleep(0.1)
            await beio.connect('http://localhost:5005/socket.io')
        else:
            pass


    async def socket_use_58(self,user_id):
        global sio
        if socket_58 and time.time() -  socket_58[list(socket_52.keys())[0]] > 180:
            del socket_in_use[list(socket_58.keys())[0]]
            socket_in_use_list.remove(58)
            socket_58.clear()
            await self.empty_sock_check(user_id)
            await bfio.disconnect()
            await asyncio.sleep(0.1)
            await bfio.connect('http://localhost:5005/socket.io')
        else:
            pass


    async def socket_use_59(self,user_id):
        global sio
        if socket_59 and time.time() -  socket_59[list(socket_52.keys())[0]] > 180:
            del socket_in_use[list(socket_59.keys())[0]]
            socket_in_use_list.remove(59)
            socket_59.clear()
            await self.empty_sock_check(user_id)
            await bgio.disconnect()
            await asyncio.sleep(0.1)
            await bgio.connect('http://localhost:5005/socket.io')
        else:
            pass


    async def socket_use_60(self,user_id):
        global sio
        if socket_60 and time.time() -  socket_60[list(socket_52.keys())[0]] > 180:
            del socket_in_use[list(socket_60.keys())[0]]
            socket_in_use_list.remove(60)
            socket_60.clear()
            await self.empty_sock_check(user_id)
            await bhio.disconnect()
            await asyncio.sleep(0.1)
            await bhio.connect('http://localhost:5005/socket.io')
        else:
            pass


    async def socket_use_61(self,user_id):
        global sio
        if socket_61 and time.time() -  socket_61[list(socket_52.keys())[0]] > 180:
            del socket_in_use[list(socket_61.keys())[0]]
            socket_in_use_list.remove(61)
            socket_61.clear()
            await self.empty_sock_check(user_id)
            await biio.disconnect()
            await asyncio.sleep(0.1)
            await biio.connect('http://localhost:5005/socket.io')
        else:
            pass


    async def socket_use_62(self,user_id):
        global sio
        if socket_62 and time.time() -  socket_62[list(socket_52.keys())[0]] > 180:
            del socket_in_use[list(socket_62.keys())[0]]
            socket_in_use_list.remove(62)
            socket_62.clear()
            await self.empty_sock_check(user_id)
            await bjio.disconnect()
            await asyncio.sleep(0.1)
            await bjio.connect('http://localhost:5005/socket.io')
        else:
            pass


    async def socket_use_63(self,user_id):
        global sio
        if socket_63 and time.time() -  socket_63[list(socket_52.keys())[0]] > 180:
            del socket_in_use[list(socket_63.keys())[0]]
            socket_in_use_list.remove(63)
            socket_63.clear()
            await self.empty_sock_check(user_id)
            await bkio.disconnect()
            await asyncio.sleep(0.1)
            await bkio.connect('http://localhost:5005/socket.io')
        else:
            pass


    async def socket_use_64(self,user_id):
        global sio
        if socket_64 and time.time() -  socket_64[list(socket_52.keys())[0]] > 180:
            del socket_in_use[list(socket_64.keys())[0]]
            socket_in_use_list.remove(64)
            socket_64.clear()
            await self.empty_sock_check(user_id)
            await blio.disconnect()
            await asyncio.sleep(0.1)
            await blio.connect('http://localhost:5005/socket.io')
        else:
            pass


    async def socket_use_65(self,user_id):
        global sio
        if socket_65 and time.time() -  socket_65[list(socket_52.keys())[0]] > 180:
            del socket_in_use[list(socket_65.keys())[0]]
            socket_in_use_list.remove(65)
            socket_65.clear()
            await self.empty_sock_check(user_id)
            await bmio.disconnect()
            await asyncio.sleep(0.1)
            await bmio.connect('http://localhost:5005/socket.io')
        else:
            pass


    async def socket_use_66(self,user_id):
        global sio
        if socket_66 and time.time() -  socket_66[list(socket_52.keys())[0]] > 180:
            del socket_in_use[list(socket_66.keys())[0]]
            socket_in_use_list.remove(66)
            socket_66.clear()
            await self.empty_sock_check(user_id)
            await bnio.disconnect()
            await asyncio.sleep(0.1)
            await bnio.connect('http://localhost:5005/socket.io')
        else:
            pass


    async def socket_use_67(self,user_id):
        global sio
        if socket_67 and time.time() -  socket_67[list(socket_52.keys())[0]] > 180:
            del socket_in_use[list(socket_67.keys())[0]]
            socket_in_use_list.remove(67)
            socket_67.clear()
            await self.empty_sock_check(user_id)
            await boio.disconnect()
            await asyncio.sleep(0.1)
            await boio.connect('http://localhost:5005/socket.io')
        else:
            pass


    async def socket_use_68(self,user_id):
        global sio
        if socket_68 and time.time() -  socket_68[list(socket_52.keys())[0]] > 180:
            del socket_in_use[list(socket_68.keys())[0]]
            socket_in_use_list.remove(68)
            socket_68.clear()
            await self.empty_sock_check(user_id)
            await bpio.disconnect()
            await asyncio.sleep(0.1)
            await bpio.connect('http://localhost:5005/socket.io')
        else:
            pass


    async def socket_use_69(self,user_id):
        global sio
        if socket_69 and time.time() -  socket_69[list(socket_52.keys())[0]] > 180:
            del socket_in_use[list(socket_69.keys())[0]]
            socket_in_use_list.remove(69)
            socket_69.clear()
            await self.empty_sock_check(user_id)
            await bqio.disconnect()
            await asyncio.sleep(0.1)
            await bqio.connect('http://localhost:5005/socket.io')
        else:
            pass


    async def socket_use_70(self,user_id):
        global sio
        if socket_70 and time.time() -  socket_70[list(socket_52.keys())[0]] > 180:
            del socket_in_use[list(socket_70.keys())[0]]
            socket_in_use_list.remove(70)
            socket_70.clear()
            await self.empty_sock_check(user_id)
            await brio.disconnect()
            await asyncio.sleep(0.1)
            await brio.connect('http://localhost:5005/socket.io')
        else:
            pass


    async def socket_use_71(self,user_id):
        global sio
        if socket_71 and time.time() -  socket_71[list(socket_52.keys())[0]] > 180:
            del socket_in_use[list(socket_71.keys())[0]]
            socket_in_use_list.remove(71)
            socket_71.clear()
            await self.empty_sock_check(user_id)
            await bsio.disconnect()
            await asyncio.sleep(0.1)
            await bsio.connect('http://localhost:5005/socket.io')
        else:
            pass


    async def socket_use_72(self,user_id):
        global sio
        if socket_72 and time.time() -  socket_72[list(socket_52.keys())[0]] > 180:
            del socket_in_use[list(socket_72.keys())[0]]
            socket_in_use_list.remove(72)
            socket_72.clear()
            await self.empty_sock_check(user_id)
            await btio.disconnect()
            await asyncio.sleep(0.1)
            await btio.connect('http://localhost:5005/socket.io')
        else:
            pass


    async def socket_use_73(self,user_id):
        global sio
        if socket_73 and time.time() -  socket_73[list(socket_52.keys())[0]] > 180:
            del socket_in_use[list(socket_73.keys())[0]]
            socket_in_use_list.remove(73)
            socket_73.clear()
            await self.empty_sock_check(user_id)
            await buio.disconnect()
            await asyncio.sleep(0.1)
            await buio.connect('http://localhost:5005/socket.io')
        else:
            pass


    async def socket_use_74(self,user_id):
        global sio
        if socket_74 and time.time() -  socket_74[list(socket_52.keys())[0]] > 180:
            del socket_in_use[list(socket_74.keys())[0]]
            socket_in_use_list.remove(74)
            socket_74.clear()
            await self.empty_sock_check(user_id)
            await bvio.disconnect()
            await asyncio.sleep(0.1)
            await bvio.connect('http://localhost:5005/socket.io')
        else:
            pass


    async def socket_use_75(self,user_id):
        global sio
        if socket_75 and time.time() -  socket_75[list(socket_52.keys())[0]] > 180:
            del socket_in_use[list(socket_75.keys())[0]]
            socket_in_use_list.remove(75)
            socket_75.clear()
            await self.empty_sock_check(user_id)
            await bwio.disconnect()
            await asyncio.sleep(0.1)
            await bwio.connect('http://localhost:5005/socket.io')
        else:
            pass


    async def socket_use_76(self,user_id):
        global sio
        if socket_76 and time.time() -  socket_76[list(socket_52.keys())[0]] > 180:
            del socket_in_use[list(socket_76.keys())[0]]
            socket_in_use_list.remove(76)
            socket_76.clear()
            await self.empty_sock_check(user_id)
            await bxio.disconnect()
            await asyncio.sleep(0.1)
            await bxio.connect('http://localhost:5005/socket.io')
        else:
            pass


    async def socket_use_77(self,user_id):
        global sio
        if socket_77 and time.time() -  socket_77[list(socket_52.keys())[0]] > 180:
            del socket_in_use[list(socket_77.keys())[0]]
            socket_in_use_list.remove(77)
            socket_77.clear()
            await self.empty_sock_check(user_id)
            await byio.disconnect()
            await asyncio.sleep(0.1)
            await byio.connect('http://localhost:5005/socket.io')
        else:
            pass


    async def socket_use_78(self,user_id):
        global sio
        if socket_78 and time.time() -  socket_78[list(socket_52.keys())[0]] > 180:
            del socket_in_use[list(socket_78.keys())[0]]
            socket_in_use_list.remove(78)
            socket_78.clear()
            await self.empty_sock_check(user_id)
            await bzio.disconnect()
            await asyncio.sleep(0.1)
            await bzio.connect('http://localhost:5005/socket.io')
        else:
            pass

    #----c

    async def socket_use_79(self,user_id):
        global sio
        if socket_79 and time.time() -  socket_79[list(socket_52.keys())[0]] > 180: 
            del socket_in_use[list(socket_79.keys())[0]]
            socket_in_use_list.remove(79)
            socket_79.clear()
            await self.empty_sock_check(user_id)
            await caio.disconnect()
            await asyncio.sleep(0.1)
            await caio.connect('http://localhost:5005/socket.io')
        else: 
            pass   
    

    async def socket_use_80(self,user_id):
        global sio
        if socket_80 and time.time() -  socket_80[list(socket_52.keys())[0]] > 180: 
            del socket_in_use[list(socket_80.keys())[0]]
            socket_in_use_list.remove(80)
            socket_80.clear()
            await self.empty_sock_check(user_id)
            await cbio.disconnect()
            await asyncio.sleep(0.1)
            await cbio.connect('http://localhost:5005/socket.io')
        else:
            pass


    async def socket_use_81(self,user_id):
        global sio
        if socket_81 and time.time() -  socket_81[list(socket_52.keys())[0]] > 180:
            del socket_in_use[list(socket_81.keys())[0]]
            socket_in_use_list.remove(81)
            socket_81.clear()
            await self.empty_sock_check(user_id)
            await ccio.disconnect()
            await asyncio.sleep(0.1)
            await ccio.connect('http://localhost:5005/socket.io')
        else:
            pass


    async def socket_use_82(self,user_id):
        global sio
        if socket_82 and time.time() -  socket_82[list(socket_52.keys())[0]] > 180:
            del socket_in_use[list(socket_82.keys())[0]]
            socket_in_use_list.remove(82)
            socket_82.clear()
            await self.empty_sock_check(user_id)
            await cdio.disconnect()
            await asyncio.sleep(0.1)
            await cdio.connect('http://localhost:5005/socket.io')
        else:
            pass


    async def socket_use_83(self,user_id):
        global sio
        if socket_83 and time.time() -  socket_83[list(socket_52.keys())[0]] > 180:
            del socket_in_use[list(socket_83.keys())[0]]
            socket_in_use_list.remove(83)
            socket_83.clear()
            await self.empty_sock_check(user_id)
            await ceio.disconnect()
            await asyncio.sleep(0.1)
            await ceio.connect('http://localhost:5005/socket.io')
        else:
            pass


    async def socket_use_84(self,user_id):
        global sio
        if socket_84 and time.time() -  socket_84[list(socket_52.keys())[0]] > 180:
            del socket_in_use[list(socket_84.keys())[0]]
            socket_in_use_list.remove(84)
            socket_84.clear()
            await self.empty_sock_check(user_id)
            await cfio.disconnect()
            await asyncio.sleep(0.1)
            await cfio.connect('http://localhost:5005/socket.io')
        else:
            pass


    async def socket_use_85(self,user_id):
        global sio
        if socket_85 and time.time() -  socket_85[list(socket_52.keys())[0]] > 180:
            del socket_in_use[list(socket_85.keys())[0]]
            socket_in_use_list.remove(85)
            socket_85.clear()
            await self.empty_sock_check(user_id)
            await cgio.disconnect()
            await asyncio.sleep(0.1)
            await cgio.connect('http://localhost:5005/socket.io')
        else:
            pass


    async def socket_use_86(self,user_id):
        global sio
        if socket_86 and time.time() -  socket_86[list(socket_52.keys())[0]] > 180:
            del socket_in_use[list(socket_86.keys())[0]]
            socket_in_use_list.remove(86)
            socket_86.clear()
            await self.empty_sock_check(user_id)
            await chio.disconnect()
            await asyncio.sleep(0.1)
            await chio.connect('http://localhost:5005/socket.io')
        else:
            pass


    async def socket_use_87(self,user_id):
        global sio
        if socket_87 and time.time() -  socket_87[list(socket_52.keys())[0]] > 180:
            del socket_in_use[list(socket_87.keys())[0]]
            socket_in_use_list.remove(87)
            socket_87.clear()
            await self.empty_sock_check(user_id)
            await ciio.disconnect()
            await asyncio.sleep(0.1)
            await ciio.connect('http://localhost:5005/socket.io')
        else:
            pass


    async def socket_use_88(self,user_id):
        global sio
        if socket_88 and time.time() -  socket_88[list(socket_52.keys())[0]] > 180:
            del socket_in_use[list(socket_88.keys())[0]]
            socket_in_use_list.remove(88)
            socket_88.clear()
            await self.empty_sock_check(user_id)
            await cjio.disconnect()
            await asyncio.sleep(0.1)
            await cjio.connect('http://localhost:5005/socket.io')
        else:
            pass


    async def socket_use_89(self,user_id):
        global sio
        if socket_89 and time.time() -  socket_89[list(socket_52.keys())[0]] > 180:
            del socket_in_use[list(socket_89.keys())[0]]
            socket_in_use_list.remove(89)
            socket_89.clear()
            await self.empty_sock_check(user_id)
            await ckio.disconnect()
            await asyncio.sleep(0.1)
            await ckio.connect('http://localhost:5005/socket.io')
        else:
            pass


    async def socket_use_90(self,user_id):
        global sio
        if socket_90 and time.time() -  socket_90[list(socket_52.keys())[0]] > 180:
            del socket_in_use[list(socket_90.keys())[0]]
            socket_in_use_list.remove(90)
            socket_90.clear()
            await self.empty_sock_check(user_id)
            await clio.disconnect()
            await asyncio.sleep(0.1)
            await clio.connect('http://localhost:5005/socket.io')
        else:
            pass


    async def socket_use_91(self,user_id):
        global sio
        if socket_91 and time.time() -  socket_91[list(socket_52.keys())[0]] > 180:
            del socket_in_use[list(socket_91.keys())[0]]
            socket_in_use_list.remove(91)
            socket_91.clear()
            await self.empty_sock_check(user_id)
            await cmio.disconnect()
            await asyncio.sleep(0.1)
            await cmio.connect('http://localhost:5005/socket.io')
        else:
            pass


    async def socket_use_92(self,user_id):
        global sio
        if socket_92 and time.time() -  socket_92[list(socket_52.keys())[0]] > 180:
            del socket_in_use[list(socket_92.keys())[0]]
            socket_in_use_list.remove(92)
            socket_92.clear()
            await self.empty_sock_check(user_id)
            await cnio.disconnect()
            await asyncio.sleep(0.1)
            await cnio.connect('http://localhost:5005/socket.io')
        else:
            pass


    async def socket_use_93(self,user_id):
        global sio
        if socket_93 and time.time() -  socket_93[list(socket_52.keys())[0]] > 180:
            del socket_in_use[list(socket_93.keys())[0]]
            socket_in_use_list.remove(93)
            socket_93.clear()
            await self.empty_sock_check(user_id)
            await coio.disconnect()
            await asyncio.sleep(0.1)
            await coio.connect('http://localhost:5005/socket.io')
        else:
            pass


    async def socket_use_94(self,user_id):
        global sio
        if socket_94 and time.time() -  socket_94[list(socket_52.keys())[0]] > 180:
            del socket_in_use[list(socket_94.keys())[0]]
            socket_in_use_list.remove(94)
            socket_94.clear()
            await self.empty_sock_check(user_id)
            await cpio.disconnect()
            await asyncio.sleep(0.1)
            await cpio.connect('http://localhost:5005/socket.io')
        else:
            pass


    async def socket_use_95(self,user_id):
        global sio
        if socket_95 and time.time() -  socket_95[list(socket_52.keys())[0]] > 180:
            del socket_in_use[list(socket_95.keys())[0]]
            socket_in_use_list.remove(95)
            socket_95.clear()
            await self.empty_sock_check(user_id)
            await cqio.disconnect()
            await asyncio.sleep(0.1)
            await cqio.connect('http://localhost:5005/socket.io')
        else:
            pass


    async def socket_use_96(self,user_id):
        global sio
        if socket_96 and time.time() -  socket_96[list(socket_52.keys())[0]] > 180:
            del socket_in_use[list(socket_96.keys())[0]]
            socket_in_use_list.remove(96)
            socket_96.clear()
            await self.empty_sock_check(user_id)
            await crio.disconnect()
            await asyncio.sleep(0.1)
            await crio.connect('http://localhost:5005/socket.io')
        else:
            pass


    async def socket_use_97(self,user_id):
        global sio
        if socket_97 and time.time() -  socket_97[list(socket_52.keys())[0]] > 180:
            del socket_in_use[list(socket_97.keys())[0]]
            socket_in_use_list.remove(97)
            socket_97.clear()
            await self.empty_sock_check(user_id)
            await csio.disconnect()
            await asyncio.sleep(0.1)
            await csio.connect('http://localhost:5005/socket.io')
        else:
            pass


    async def socket_use_98(self,user_id):
        global sio
        if socket_98 and time.time() -  socket_98[list(socket_52.keys())[0]] > 180:
            del socket_in_use[list(socket_98.keys())[0]]
            socket_in_use_list.remove(98)
            socket_98.clear()
            await self.empty_sock_check(user_id)
            await ctio.disconnect()
            await asyncio.sleep(0.1)
            await ctio.connect('http://localhost:5005/socket.io')
        else:
            pass


    async def socket_use_99(self,user_id):
        global sio
        if socket_99 and time.time() -  socket_99[list(socket_52.keys())[0]] > 180:
            del socket_in_use[list(socket_99.keys())[0]]
            socket_in_use_list.remove(99)
            socket_99.clear()
            await self.empty_sock_check(user_id)
            await cuio.disconnect()
            await asyncio.sleep(0.1)
            await cuio.connect('http://localhost:5005/socket.io')
        else:
            pass


    async def socket_use_100(self,user_id):
        global sio
        if socket_100 and time.time() -  socket_100[list(socket_52.keys())[0]] > 180:
            del socket_in_use[list(socket_100.keys())[0]]
            socket_in_use_list.remove(100)
            socket_100.clear()
            await self.empty_sock_check(user_id)
            await cvio.disconnect()
            await asyncio.sleep(0.1)
            await cvio.connect('http://localhost:5005/socket.io')
        else:
            pass


    async def socket_use_101(self,user_id):
        global sio
        if socket_101 and time.time() -  socket_101[list(socket_52.keys())[0]] > 180:
            del socket_in_use[list(socket_101.keys())[0]]
            socket_in_use_list.remove(101)
            socket_101.clear()
            await self.empty_sock_check(user_id)
            await cwio.disconnect()
            await asyncio.sleep(0.1)
            await cwio.connect('http://localhost:5005/socket.io')
        else:
            pass


    async def socket_use_102(self,user_id):
        global sio
        if socket_102 and time.time() -  socket_102[list(socket_52.keys())[0]] > 180:
            del socket_in_use[list(socket_102.keys())[0]]
            socket_in_use_list.remove(102)
            socket_102.clear()
            await self.empty_sock_check(user_id)
            await cxio.disconnect()
            await asyncio.sleep(0.1)
            await cxio.connect('http://localhost:5005/socket.io')
        else:
            pass


    async def socket_use_103(self,user_id):
        global sio
        if socket_103 and time.time() -  socket_103[list(socket_52.keys())[0]] > 180:
            del socket_in_use[list(socket_103.keys())[0]]
            socket_in_use_list.remove(103)
            socket_103.clear()
            await self.empty_sock_check(user_id)
            await cyio.disconnect()
            await asyncio.sleep(0.1)
            await cyio.connect('http://localhost:5005/socket.io')
        else:
            pass


    async def socket_use_104(self,user_id):
        global sio
        if socket_104 and time.time() -  socket_104[list(socket_52.keys())[0]] > 180:
            del socket_in_use[list(socket_104.keys())[0]]
            socket_in_use_list.remove(104)
            socket_104.clear()
            await self.empty_sock_check(user_id)
            await czio.disconnect()
            await asyncio.sleep(0.1)
            await czio.connect('http://localhost:5005/socket.io')
        else:
            pass

    #----d

    async def socket_use_105(self,user_id):
        global sio
        if socket_105 and time.time() -  socket_105[list(socket_52.keys())[0]] > 180: 
            del socket_in_use[list(socket_105.keys())[0]]
            socket_in_use_list.remove(105)
            socket_105.clear()
            await self.empty_sock_check(user_id)
            await daio.disconnect()
            await asyncio.sleep(0.1)
            await daio.connect('http://localhost:5005/socket.io')
        else: 
            pass


    async def socket_use_106(self,user_id):
        global sio
        if socket_106 and time.time() -  socket_106[list(socket_52.keys())[0]] > 180:
            del socket_in_use[list(socket_106.keys())[0]]
            socket_in_use_list.remove(106)
            socket_106.clear()
            await self.empty_sock_check(user_id)
            await dbio.disconnect()
            await asyncio.sleep(0.1)
            await dbio.connect('http://localhost:5005/socket.io')
        else:
            pass


    async def socket_use_107(self,user_id):
        global sio
        if socket_107 and time.time() -  socket_107[list(socket_52.keys())[0]] > 180:
            del socket_in_use[list(socket_107.keys())[0]]
            socket_in_use_list.remove(107)
            socket_107.clear()
            await self.empty_sock_check(user_id)
            await dcio.disconnect()
            await asyncio.sleep(0.1)
            await dcio.connect('http://localhost:5005/socket.io')
        else:
            pass


    async def socket_use_108(self,user_id):
        global sio
        if socket_108 and time.time() -  socket_108[list(socket_52.keys())[0]] > 180:
            del socket_in_use[list(socket_108.keys())[0]]
            socket_in_use_list.remove(108)
            socket_108.clear()
            await self.empty_sock_check(user_id)
            await ddio.disconnect()
            await asyncio.sleep(0.1)
            await ddio.connect('http://localhost:5005/socket.io')
        else:
            pass


    async def socket_use_109(self,user_id):
        global sio
        if socket_109 and time.time() -  socket_109[list(socket_52.keys())[0]] > 180:
            del socket_in_use[list(socket_109.keys())[0]]
            socket_in_use_list.remove(109)
            socket_109.clear()
            await self.empty_sock_check(user_id)
            await deio.disconnect()
            await asyncio.sleep(0.1)
            await deio.connect('http://localhost:5005/socket.io')
        else:
            pass


    async def socket_use_110(self,user_id):
        global sio
        if socket_110 and time.time() -  socket_110[list(socket_52.keys())[0]] > 180:
            del socket_in_use[list(socket_110.keys())[0]]
            socket_in_use_list.remove(110)
            socket_110.clear()
            await self.empty_sock_check(user_id)
            await dfio.disconnect()
            await asyncio.sleep(0.1)
            await dfio.connect('http://localhost:5005/socket.io')
        else:
            pass


    async def socket_use_111(self,user_id):
        global sio
        if socket_111 and time.time() -  socket_111[list(socket_52.keys())[0]] > 180:
            del socket_in_use[list(socket_111.keys())[0]]
            socket_in_use_list.remove(111)
            socket_111.clear()
            await self.empty_sock_check(user_id)
            await dgio.disconnect()
            await asyncio.sleep(0.1)
            await dgio.connect('http://localhost:5005/socket.io')
        else:
            pass


    async def socket_use_112(self,user_id):
        global sio
        if socket_112 and time.time() -  socket_112[list(socket_52.keys())[0]] > 180:
            del socket_in_use[list(socket_112.keys())[0]]
            socket_in_use_list.remove(112)
            socket_112.clear()
            await self.empty_sock_check(user_id)
            await dhio.disconnect()
            await asyncio.sleep(0.1)
            await dhio.connect('http://localhost:5005/socket.io')
        else:
            pass


    async def socket_use_113(self,user_id):
        global sio
        if socket_113 and time.time() -  socket_113[list(socket_52.keys())[0]] > 180:
            del socket_in_use[list(socket_113.keys())[0]]
            socket_in_use_list.remove(113)
            socket_113.clear()
            await self.empty_sock_check(user_id)
            await diio.disconnect()
            await asyncio.sleep(0.1)
            await diio.connect('http://localhost:5005/socket.io')
        else:
            pass


    async def socket_use_114(self,user_id):
        global sio
        if socket_114 and time.time() -  socket_114[list(socket_52.keys())[0]] > 180:
            del socket_in_use[list(socket_114.keys())[0]]
            socket_in_use_list.remove(114)
            socket_114.clear()
            await self.empty_sock_check(user_id)
            await djio.disconnect()
            await asyncio.sleep(0.1)
            await djio.connect('http://localhost:5005/socket.io')
        else:
            pass


    async def socket_use_115(self,user_id):
        global sio
        if socket_115 and time.time() -  socket_115[list(socket_52.keys())[0]] > 180:
            del socket_in_use[list(socket_115.keys())[0]]
            socket_in_use_list.remove(115)
            socket_115.clear()
            await self.empty_sock_check(user_id)
            await dkio.disconnect()
            await asyncio.sleep(0.1)
            await dkio.connect('http://localhost:5005/socket.io')
        else:
            pass


    async def socket_use_116(self,user_id):
        global sio
        if socket_116 and time.time() -  socket_116[list(socket_52.keys())[0]] > 180:
            del socket_in_use[list(socket_116.keys())[0]]
            socket_in_use_list.remove(116)
            socket_116.clear()
            await self.empty_sock_check(user_id)
            await dlio.disconnect()
            await asyncio.sleep(0.1)
            await dlio.connect('http://localhost:5005/socket.io')
        else:
            pass


    async def socket_use_117(self,user_id):
        global sio
        if socket_117 and time.time() -  socket_117[list(socket_52.keys())[0]] > 180:
            del socket_in_use[list(socket_117.keys())[0]]
            socket_in_use_list.remove(117)
            socket_117.clear()
            await self.empty_sock_check(user_id)
            await dmio.disconnect()
            await asyncio.sleep(0.1)
            await dmio.connect('http://localhost:5005/socket.io')
        else:
            pass


    async def socket_use_118(self,user_id):
        global sio
        if socket_118 and time.time() -  socket_118[list(socket_52.keys())[0]] > 180:
            del socket_in_use[list(socket_118.keys())[0]]
            socket_in_use_list.remove(118)
            socket_118.clear()
            await self.empty_sock_check(user_id)
            await dnio.disconnect()
            await asyncio.sleep(0.1)
            await dnio.connect('http://localhost:5005/socket.io')
        else:
            pass


    async def socket_use_119(self,user_id):
        global sio
        if socket_119 and time.time() -  socket_119[list(socket_52.keys())[0]] > 180:
            del socket_in_use[list(socket_119.keys())[0]]
            socket_in_use_list.remove(119)
            socket_119.clear()
            await self.empty_sock_check(user_id)
            await doio.disconnect()
            await asyncio.sleep(0.1)
            await doio.connect('http://localhost:5005/socket.io')
        else:
            pass


    async def socket_use_120(self,user_id):
        global sio
        if socket_120 and time.time() -  socket_120[list(socket_52.keys())[0]] > 180:
            del socket_in_use[list(socket_120.keys())[0]]
            socket_in_use_list.remove(120)
            socket_120.clear()
            await self.empty_sock_check(user_id)
            await dpio.disconnect()
            await asyncio.sleep(0.1)
            await dpio.connect('http://localhost:5005/socket.io')
        else:
            pass


    async def socket_use_121(self,user_id):
        global sio
        if socket_121 and time.time() -  socket_121[list(socket_52.keys())[0]] > 180:
            del socket_in_use[list(socket_121.keys())[0]]
            socket_in_use_list.remove(121)
            socket_121.clear()
            await self.empty_sock_check(user_id)
            await dqio.disconnect()
            await asyncio.sleep(0.1)
            await dqio.connect('http://localhost:5005/socket.io')
        else:
            pass


    async def socket_use_122(self,user_id):
        global sio
        if socket_122 and time.time() -  socket_122[list(socket_52.keys())[0]] > 180:
            del socket_in_use[list(socket_122.keys())[0]]
            socket_in_use_list.remove(122)
            socket_122.clear()
            await self.empty_sock_check(user_id)
            await drio.disconnect()
            await asyncio.sleep(0.1)
            await drio.connect('http://localhost:5005/socket.io')
        else:
            pass


    async def socket_use_123(self,user_id):
        global sio
        if socket_123 and time.time() -  socket_123[list(socket_52.keys())[0]] > 180:
            del socket_in_use[list(socket_123.keys())[0]]
            socket_in_use_list.remove(123)
            socket_123.clear()
            await self.empty_sock_check(user_id)
            await dsio.disconnect()
            await asyncio.sleep(0.1)
            await dsio.connect('http://localhost:5005/socket.io')
        else:
            pass


    async def socket_use_124(self,user_id):
        global sio
        if socket_124 and time.time() -  socket_124[list(socket_52.keys())[0]] > 180:
            del socket_in_use[list(socket_124.keys())[0]]
            socket_in_use_list.remove(124)
            socket_124.clear()
            await self.empty_sock_check(user_id)
            await dtio.disconnect()
            await asyncio.sleep(0.1)
            await dtio.connect('http://localhost:5005/socket.io')
        else:
            pass


    async def socket_use_125(self,user_id):
        global sio
        if socket_125 and time.time() -  socket_125[list(socket_52.keys())[0]] > 180:
            del socket_in_use[list(socket_125.keys())[0]]
            socket_in_use_list.remove(125)
            socket_125.clear()
            await self.empty_sock_check(user_id)
            await duio.disconnect()
            await asyncio.sleep(0.1)
            await duio.connect('http://localhost:5005/socket.io')
        else:
            pass


    async def socket_use_126(self,user_id):
        global sio
        if socket_126 and time.time() -  socket_126[list(socket_52.keys())[0]] > 180:
            del socket_in_use[list(socket_126.keys())[0]]
            socket_in_use_list.remove(126)
            socket_126.clear()
            await self.empty_sock_check(user_id)
            await dvio.disconnect()
            await asyncio.sleep(0.1)
            await dvio.connect('http://localhost:5005/socket.io')
        else:
            pass


    async def socket_use_127(self,user_id):
        global sio
        if socket_127 and time.time() -  socket_127[list(socket_52.keys())[0]] > 180:
            del socket_in_use[list(socket_127.keys())[0]]
            socket_in_use_list.remove(127)
            socket_127.clear()
            await self.empty_sock_check(user_id)
            await dwio.disconnect()
            await asyncio.sleep(0.1)
            await dwio.connect('http://localhost:5005/socket.io')
        else:
            pass


    async def socket_use_128(self,user_id):
        global sio
        if socket_128 and time.time() -  socket_128[list(socket_52.keys())[0]] > 180:
            del socket_in_use[list(socket_128.keys())[0]]
            socket_in_use_list.remove(128)
            socket_128.clear()
            await self.empty_sock_check(user_id)
            await dxio.disconnect()
            await asyncio.sleep(0.1)
            await dxio.connect('http://localhost:5005/socket.io')
        else:
            pass


    async def socket_use_129(self,user_id):
        global sio
        if socket_129 and time.time() -  socket_129[list(socket_52.keys())[0]] > 180:
            del socket_in_use[list(socket_129.keys())[0]]
            socket_in_use_list.remove(129)
            socket_129.clear()
            await self.empty_sock_check(user_id)
            await dyio.disconnect()
            await asyncio.sleep(0.1)
            await dyio.connect('http://localhost:5005/socket.io')
        else:
            pass


    async def socket_use_130(self,user_id):
        global sio
        if socket_130 and time.time() -  socket_130[list(socket_52.keys())[0]] > 180:
            del socket_in_use[list(socket_130.keys())[0]]
            socket_in_use_list.remove(130)
            socket_130.clear()
            await self.empty_sock_check(user_id)
            await dzio.disconnect()
            await asyncio.sleep(0.1)
            await dzio.connect('http://localhost:5005/socket.io')
        else:
            pass

    #----e

    async def socket_use_131(self,user_id):
        global sio
        if socket_131 and time.time() -  socket_131[list(socket_52.keys())[0]] > 180: 
            del socket_in_use[list(socket_131.keys())[0]]
            socket_in_use_list.remove(131)
            socket_131.clear()
            await self.empty_sock_check(user_id)
            await eaio.disconnect()
            await asyncio.sleep(0.1)
            await eaio.connect('http://localhost:5005/socket.io')
        else:
            pass


    async def socket_use_132(self,user_id):
        global sio
        if socket_132 and time.time() -  socket_132[list(socket_52.keys())[0]] > 180: 
            del socket_in_use[list(socket_132.keys())[0]]
            socket_in_use_list.remove(132)
            socket_132.clear()
            await self.empty_sock_check(user_id)
            await ebio.disconnect()
            await asyncio.sleep(0.1)
            await ebio.connect('http://localhost:5005/socket.io')
        else:
            pass


    async def socket_use_133(self,user_id):
        global sio
        if socket_133 and time.time() -  socket_133[list(socket_52.keys())[0]] > 180:
            del socket_in_use[list(socket_133.keys())[0]]
            socket_in_use_list.remove(133)
            socket_133.clear()
            await self.empty_sock_check(user_id)
            await ecio.disconnect()
            await asyncio.sleep(0.1)
            await ecio.connect('http://localhost:5005/socket.io')
        else:
            pass


    async def socket_use_134(self,user_id):
        global sio
        if socket_134 and time.time() -  socket_134[list(socket_52.keys())[0]] > 180:
            del socket_in_use[list(socket_134.keys())[0]]
            socket_in_use_list.remove(134)
            socket_134.clear()
            await self.empty_sock_check(user_id)
            await edio.disconnect()
            await asyncio.sleep(0.1)
            await edio.connect('http://localhost:5005/socket.io')
        else:
            pass


    async def socket_use_135(self,user_id):
        global sio
        if socket_135 and time.time() -  socket_135[list(socket_52.keys())[0]] > 180:
            del socket_in_use[list(socket_135.keys())[0]]
            socket_in_use_list.remove(135)
            socket_135.clear()
            await self.empty_sock_check(user_id)
            await eeio.disconnect()
            await asyncio.sleep(0.1)
            await eeio.connect('http://localhost:5005/socket.io')
        else:
            pass


    async def socket_use_136(self,user_id):
        global sio
        if socket_136 and time.time() -  socket_136[list(socket_52.keys())[0]] > 180:
            del socket_in_use[list(socket_136.keys())[0]]
            socket_in_use_list.remove(136)
            socket_136.clear()
            await self.empty_sock_check(user_id)
            await efio.disconnect()
            await asyncio.sleep(0.1)
            await efio.connect('http://localhost:5005/socket.io')
        else:
            pass


    async def socket_use_137(self,user_id):
        global sio
        if socket_137 and time.time() -  socket_137[list(socket_52.keys())[0]] > 180:
            del socket_in_use[list(socket_137.keys())[0]]
            socket_in_use_list.remove(137)
            socket_137.clear()
            await self.empty_sock_check(user_id)
            await egio.disconnect()
            await asyncio.sleep(0.1)
            await egio.connect('http://localhost:5005/socket.io')
        else:
            pass


    async def socket_use_138(self,user_id):
        global sio
        if socket_138 and time.time() -  socket_138[list(socket_52.keys())[0]] > 180:
            del socket_in_use[list(socket_138.keys())[0]]
            socket_in_use_list.remove(138)
            socket_138.clear()
            await self.empty_sock_check(user_id)
            await ehio.disconnect()
            await asyncio.sleep(0.1)
            await ehio.connect('http://localhost:5005/socket.io')
        else:
            pass


    async def socket_use_139(self,user_id):
        global sio
        if socket_139 and time.time() -  socket_139[list(socket_52.keys())[0]] > 180:
            del socket_in_use[list(socket_139.keys())[0]]
            socket_in_use_list.remove(139)
            socket_139.clear()
            await self.empty_sock_check(user_id)
            await eiio.disconnect()
            await asyncio.sleep(0.1)
            await eiio.connect('http://localhost:5005/socket.io')
        else:
            pass


    async def socket_use_140(self,user_id):
        global sio
        if socket_140 and time.time() -  socket_140[list(socket_52.keys())[0]] > 180:
            del socket_in_use[list(socket_140.keys())[0]]
            socket_in_use_list.remove(140)
            socket_140.clear()
            await self.empty_sock_check(user_id)
            await ejio.disconnect()
            await asyncio.sleep(0.1)
            await ejio.connect('http://localhost:5005/socket.io')
        else:
            pass


    async def socket_use_141(self,user_id):
        global sio
        if socket_141 and time.time() -  socket_141[list(socket_52.keys())[0]] > 180:
            del socket_in_use[list(socket_141.keys())[0]]
            socket_in_use_list.remove(141)
            socket_141.clear()
            await self.empty_sock_check(user_id)
            await ekio.disconnect()
            await asyncio.sleep(0.1)
            await ekio.connect('http://localhost:5005/socket.io')
        else:
            pass


    async def socket_use_142(self,user_id):
        global sio
        if socket_142 and time.time() -  socket_142[list(socket_52.keys())[0]] > 180:
            del socket_in_use[list(socket_142.keys())[0]]
            socket_in_use_list.remove(142)
            socket_142.clear()
            await self.empty_sock_check(user_id)
            await elio.disconnect()
            await asyncio.sleep(0.1)
            await elio.connect('http://localhost:5005/socket.io')
        else:
            pass


    async def socket_use_143(self,user_id):
        global sio
        if socket_143 and time.time() -  socket_143[list(socket_52.keys())[0]] > 180:
            del socket_in_use[list(socket_143.keys())[0]]
            socket_in_use_list.remove(143)
            socket_143.clear()
            await self.empty_sock_check(user_id)
            await emio.disconnect()
            await asyncio.sleep(0.1)
            await emio.connect('http://localhost:5005/socket.io')
        else:
            pass


    async def socket_use_144(self,user_id):
        global sio
        if socket_144 and time.time() -  socket_144[list(socket_52.keys())[0]] > 180:
            del socket_in_use[list(socket_144.keys())[0]]
            socket_in_use_list.remove(144)
            socket_144.clear()
            await self.empty_sock_check(user_id)
            await enio.disconnect()
            await asyncio.sleep(0.1)
            await enio.connect('http://localhost:5005/socket.io')
        else:
            pass


    async def socket_use_145(self,user_id):
        global sio
        if socket_145 and time.time() -  socket_145[list(socket_52.keys())[0]] > 180:
            del socket_in_use[list(socket_145.keys())[0]]
            socket_in_use_list.remove(145)
            socket_145.clear()
            await self.empty_sock_check(user_id)
            await eoio.disconnect()
            await asyncio.sleep(0.1)
            await eoio.connect('http://localhost:5005/socket.io')
        else:
            pass


    async def socket_use_146(self,user_id):
        global sio
        if socket_146 and time.time() -  socket_146[list(socket_52.keys())[0]] > 180:
            del socket_in_use[list(socket_146.keys())[0]]
            socket_in_use_list.remove(146)
            socket_146.clear()
            await self.empty_sock_check(user_id)
            await epio.disconnect()
            await asyncio.sleep(0.1)
            await epio.connect('http://localhost:5005/socket.io')
        else:
            pass


    async def socket_use_147(self,user_id):
        global sio
        if socket_147 and time.time() -  socket_147[list(socket_52.keys())[0]] > 180:
            del socket_in_use[list(socket_147.keys())[0]]
            socket_in_use_list.remove(147)
            socket_147.clear()
            await self.empty_sock_check(user_id)
            await eqio.disconnect()
            await asyncio.sleep(0.1)
            await eqio.connect('http://localhost:5005/socket.io')
        else:
            pass


    async def socket_use_148(self,user_id):
        global sio
        if socket_148 and time.time() -  socket_148[list(socket_52.keys())[0]] > 180:
            del socket_in_use[list(socket_148.keys())[0]]
            socket_in_use_list.remove(148)
            socket_148.clear()
            await self.empty_sock_check(user_id)
            await erio.disconnect()
            await asyncio.sleep(0.1)
            await erio.connect('http://localhost:5005/socket.io')
        else:
            pass


    async def socket_use_149(self,user_id):
        global sio
        if socket_149 and time.time() -  socket_149[list(socket_52.keys())[0]] > 180:
            del socket_in_use[list(socket_149.keys())[0]]
            socket_in_use_list.remove(149)
            socket_149.clear()
            await self.empty_sock_check(user_id)
            await esio.disconnect()
            await asyncio.sleep(0.1)
            await esio.connect('http://localhost:5005/socket.io')
        else:
            pass


    async def socket_use_150(self,user_id):
        global sio
        if socket_150 and time.time() -  socket_150[list(socket_52.keys())[0]] > 180:
            del socket_in_use[list(socket_150.keys())[0]]
            socket_in_use_list.remove(150)
            socket_150.clear()
            await self.empty_sock_check(user_id)
            await etio.disconnect()
            await asyncio.sleep(0.1)
            await etio.connect('http://localhost:5005/socket.io')
        else:
            pass


    async def socket_use_151(self,user_id):
        global sio
        if socket_151 and time.time() -  socket_151[list(socket_52.keys())[0]] > 180:
            del socket_in_use[list(socket_151.keys())[0]]
            socket_in_use_list.remove(151)
            socket_151.clear()
            await self.empty_sock_check(user_id)
            await euio.disconnect()
            await asyncio.sleep(0.1)
            await euio.connect('http://localhost:5005/socket.io')
        else:
            pass


    async def socket_use_152(self,user_id):
        global sio
        if socket_152 and time.time() -  socket_152[list(socket_52.keys())[0]] > 180:
            del socket_in_use[list(socket_152.keys())[0]]
            socket_in_use_list.remove(152)
            socket_152.clear()
            await self.empty_sock_check(user_id)
            await evio.disconnect()
            await asyncio.sleep(0.1)
            await evio.connect('http://localhost:5005/socket.io')
        else:
            pass


    async def socket_use_153(self,user_id):
        global sio
        if socket_153 and time.time() -  socket_153[list(socket_52.keys())[0]] > 180:
            del socket_in_use[list(socket_153.keys())[0]]
            socket_in_use_list.remove(153)
            socket_153.clear()
            await self.empty_sock_check(user_id)
            await ewio.disconnect()
            await asyncio.sleep(0.1)
            await ewio.connect('http://localhost:5005/socket.io')
        else:
            pass


    async def socket_use_154(self,user_id):
        global sio
        if socket_154 and time.time() -  socket_154[list(socket_52.keys())[0]] > 180:
            del socket_in_use[list(socket_154.keys())[0]]
            socket_in_use_list.remove(154)
            socket_154.clear()
            await self.empty_sock_check(user_id)
            await exio.disconnect()
            await asyncio.sleep(0.1)
            await exio.connect('http://localhost:5005/socket.io')
        else:
            pass


    async def socket_use_155(self,user_id):
        global sio
        if socket_155 and time.time() -  socket_155[list(socket_52.keys())[0]] > 180:
            del socket_in_use[list(socket_155.keys())[0]]
            socket_in_use_list.remove(155)
            socket_155.clear()
            await self.empty_sock_check(user_id)
            await eyio.disconnect()
            await asyncio.sleep(0.1)
            await eyio.connect('http://localhost:5005/socket.io')
        else:
            pass


    async def socket_use_156(self,user_id):
        global sio
        if socket_156 and time.time() -  socket_156[list(socket_52.keys())[0]] > 180:
            del socket_in_use[list(socket_156.keys())[0]]
            socket_in_use_list.remove(156)
            socket_156.clear()
            await self.empty_sock_check(user_id)
            await ezio.disconnect()
            await asyncio.sleep(0.1)
            await ezio.connect('http://localhost:5005/socket.io')
        else:
            pass

    def _add_conversation_reference(self, activity: Activity):
        """
        This populates the shared Dictionary that holds conversation references. In this sample,
        this dictionary is used to send a message to members when /api/notify is hit.
        :param activity:
        :return:
        """
        conversation_reference = TurnContext.get_conversation_reference(activity)
        # print("THIS IS THE CONVERSATION REFERENCE ", conversation_reference)
        self.conversation_references[
            conversation_reference.user.id
        ] = conversation_reference

    def _create_adaptive_card_attachment(self) -> Attachment:
        """
        Load a random adaptive card attachment from file.
        :return:
        """
        card_path = os.path.join(os.getcwd(), CARDS[0])
        with open(card_path, "rb") as in_file:
            card_data = json.load(in_file)

        return CardFactory.adaptive_card(card_data)

    


'''
print("THE ID NOT IN SOCKET IN USE LIST ")
            if len(socket_1) == 0:
                socket_1[id] = time.time()
                socket_in_use[id] = '1'
                print("THIS IS SOCKET_1 ", socket_1)
                print("THIS IS SOCKET_IN_USE ", socket_in_use)
            elif len(socket_2) == 0:
                socket_2[id] = time.time()
                socket_in_use[id] = '2'
                print("THIS IS SOCKET_2 ", socket_2)
                print("THIS IS SOCKET_IN_USE ", socket_in_use)
            elif len(socket_3) == 0:
                socket_3[id] = time.time()
                socket_in_use[id] = '3'
                print("THIS IS SOCKET_3 ", socket_3)
                print("THIS IS SOCKET_IN_USE ", socket_in_use)
            elif len(socket_4) == 0:
                socket_4[id] = time.time()
                socket_in_use[id] = '4'
                print("THIS IS SOCKET_4 ", socket_4)
                print("THIS IS SOCKET_IN_USE ", socket_in_use)
            elif len(socket_5) == 0:
                socket_5[id] = time.time()
                socket_in_use[id] = '5'
                print("THIS IS SOCKET_5 ", socket_5)
                print("THIS IS SOCKET_IN_USE ", socket_in_use)




else:
            print('ID EXISTS INSIDE SOCKET IN USE LIST ')
            if socket_1  and time.time() - socket_1[list(socket_1.keys())[0]] > 120:
                del socket_in_use[list(socket_1.keys())[0]]
                socket_1.clear()
                socket_1[id] = time.time()
                socket_in_use[id] = '1'
                print("THIS IS SOCKET_1 ", socket_1)
                print("THIS IS SOCKET_IN_USE ", socket_in_use)
                await sio.disconnect()
                await sio.connect('http://localhost:5005/socket.io')
            elif socket_2  and time.time() - socket_2[list(socket_2.keys())[0]] > 120:
                del socket_in_use[list(socket_2.keys())[0]]
                socket_2.clear()
                socket_2[id] = time.time()
                socket_in_use[id] = '2'
                print("THIS IS SOCKET_2 ", socket_2)
                print("THIS IS SOCKET_IN_USE ", socket_in_use)
                await tsio.disconnect()
                await tsio.connect('http://localhost:5005/socket.io')
            elif socket_3  and time.time() - socket_3[list(socket_3.keys())[0]]  > 120:
                del socket_in_use[list(socket_3.keys())[0]]
                socket_3.clear()
                socket_3[id] = time.time()
                socket_in_use[id] = '3'
                print("THIS IS SOCKET_3 ", socket_3)
                print("THIS IS SOCKET_IN_USE ", socket_in_use)
                await usio.disconnect()
                await usio.connect('http://localhost:5005/socket.io')
            elif socket_4  and time.time() - socket_4[list(socket_4.keys())[0]] > 120:
                del socket_in_use[list(socket_4.keys())[0]]
                socket_4.clear()
                socket_4[id] = time.time()
                socket_in_use[id] = '4'
                print("THIS IS SOCKET_4 ", socket_4)
                print("THIS IS SOCKET_IN_USE ", socket_in_use)
                await vsio.disconnect()
                await usio.connect('http://localhost:5005/socket.io')
            elif socket_5  and time.time() - socket_5[list(socket_5.keys())[0]]  > 120:
                del socket_in_use[list(socket_5.keys())[0]]
                socket_5.clear()
                socket_5[id] = time.time()
                socket_in_use[id] = '5'
                print("THIS IS SOCKET_5 ", socket_5)
                print("THIS IS SOCKET_IN_USE ", socket_in_use)
                await wsio.disconnect()
                await usio.connect('http://localhost:5005/socket.io')
        # elif len(socket_1) == 0:
        #     socket_1[id] = time.time()
        #     socket_in_use[id] = '1'
        #     print("THIS IS SOCKET_1 ", socket_1)
        #     print("THIS IS SOCKET_IN_USE ", socket_in_use)
        # elif len(socket_2) == 0:
        #     socket_2[id] = time.time()
        #     socket_in_use[id] = '2'
        #     print("THIS IS SOCKET_2 ", socket_2)
        #     print("THIS IS SOCKET_IN_USE ", socket_in_use)
        # elif len(socket_3) == 0:
        #     socket_3[id] = time.time()
        #     socket_in_use[id] = '3'
        #     print("THIS IS SOCKET_3 ", socket_3)
        #     print("THIS IS SOCKET_IN_USE ", socket_in_use)
        # elif len(socket_4) == 0:
        #     socket_4[id] = time.time()
        #     socket_in_use[id] = '4'
        #     print("THIS IS SOCKET_4 ", socket_4)
        #     print("THIS IS SOCKET_IN_USE ", socket_in_use)
        # elif len(socket_5) == 0:
        #     socket_5[id] = time.time()
        #     socket_in_use[id] = '5'
        #     print("THIS IS SOCKET_5 ", socket_5)
        #     print("THIS IS SOCKET_IN_USE ", socket_in_use)

        print("THIS IS SOCKET_1 ", socket_1)
        print("THIS IS SOCKET_2 ", socket_2)
        print("THIS IS SOCKET_3 ", socket_3)
        print("THIS IS SOCKET_4 ", socket_4)
        print("THIS IS SOCKET_5 ", socket_5)
        print("THIS IS CURRENT TIME ",time.time())
        print("I AM SENDING THIS MESSAGE ", turn_context.activity.text, "AND THIS IS THE SENDER ID ", id)
        text = str(turn_context.activity.text)
        a = await Teams.TeamsInfo.get_members(turn_context)
        act_id = turn_context.activity.id
        for i in a:
            print("THIS IS TEAMS INFRO:::",i.email)
        q = turn_context.get_mentions
        text = turn_context.activity.text.lower()
        # if 'hey' in text:
        #     tt = self.activity_id[-1]
        #     self.activity_id.append(tt)
        # id = str(turn_context.get_conversation_reference(turn_context.activity).user.id)
        # id = id.replace('-','')
        print("THIS IS THE SENDER ID ", id)
        if id not in sock_flag.keys():
            print("THIS IS INITIATING SOCK TO 5005")
            sock_flag[id] = '5005'
        # user_flag_5005[id] = time.time()
        print("THIS IS SOCKET_IN_USE ", socket_in_use, " and this is the act_id ", act_id)

'''