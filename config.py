#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

""" Bot Configuration """


class DefaultConfig:
    """ Bot Configuration """

    PORT = 8080
    APP_ID = os.environ.get("MicrosoftAppId", "411e5344-9ba9-43b7-9701-3b05ea25b988")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "TBm8Q~ZIfAmQDTms_eDN2jAIIr01UIZAmE0gea~x")


#XnN8Q~FCPM4RKLd5QF1EnD9W2AdztkybZbXgFcBy
# 1Ua8Q~kvjfmcC8GPLPWgZhax5O~LCDJlhVArRc2f


# 411e5344-9ba9-43b7-9701-3b05ea25b988
# TBm8Q~ZIfAmQDTms_eDN2jAIIr01UIZAmE0gea~x


# global activity_id, acitivty_list, auth_header
# activity_id = ''
# activity_list = []
# auth_header = []
# async def messages(req: Request) -> Response:
#     global activity_id, activity_list, auth_header
#     # Main bot message handler.
#     if "application/json" in req.headers["Content-Type"]:
#         body = await req.json()
#     else:
#         return Response(status=HTTPStatus.UNSUPPORTED_MEDIA_TYPE)
#     #print("THIS IS BODY ", body, type(body))
#     activity_id = []
#     auth_header = []
#     activity = Activity().deserialize(body)
#     print("THIS IS ACTIVITYT::::: ", activity)
#     print("this is activity ", activity.id, 'and this is the type :::::',type(activity))
#     activity_id = activity.id
#     activity_list.append(activity)
#     auth_header.append(req.headers["Authorization"] if "Authorization" in req.headers else "")
#     print("THIS IS LEN OF ACTIVITY LIST ", len(activity_list))
#     await delay_activity()

# async def delay_activity():
#     global activity_list, auth_header, activity_id
#     i = 0
#     print("This is delay_activity")
#     while i < len(activity_list):
#         print("inside delay_activity")
#         activity_id = activity_list[i].id
#         await process_delayed_acvitiy(activity_list[i], auth_header[i])
#         await asyncio.sleep(1)
#         i = i+1
#     activity_list = []
#     auth_header = []

# async def process_delayed_acvitiy(activity, auth_header):
#     print("This is inside process_delayed_activity")
#     response = await ADAPTER.process_activity(activity, auth_header, BOT.on_turn)
#     if response:
#         return json_response(data=response.body, status=response.status)
#     return Response(status=HTTPStatus.OK)

# global activity_id, activity_list, auth_header
# activity_list = []
# activity_id = []
# auth_header_list = []
# async def messages(req: Request):
#     global activity_id, activity_list, auth_header_list
#     # Main bot message handler.
#     if "application/json" in req.headers["Content-Type"]:
#         body = await req.json()
#     else:
#         return Response(status=HTTPStatus.UNSUPPORTED_MEDIA_TYPE)
#     #print("THIS IS BODY ", body, type(body))
#     activity = Activity().deserialize(body)
#     print("THIS IS ACTIVITYT::::: ", activity)
#     print("this is activity ", activity.id, 'and this is the type :::::',type(activity))
#     activity_id = activity.id
#     auth_header = req.headers["Authorization"] if "Authorization" in req.headers else ""
#     activity_list.append(activity)
#     auth_header_list.append(auth_header)

# async def delay_message() -> Response:
#     global activity_list, auth_header_list
#     while activity_list:
#         response = await ADAPTER.process_activity(activity_list[0], auth_header_list[0], BOT.on_turn)
#         await asyncio.sleep(2)
#         if response:
#             return json_response(data=response.body, status=response.status)
#         return Response(status=HTTPStatus.OK)
# loop = asyncio.get_event_loop()
# loop.create_task(delay_message())
# loop.run_forever()

# # Listen for requests on /api/notify, and send a messages to all conversation members.
# async def notify(req: Request) -> Response:  # pylint: disable=unused-argument
#     await _send_proactive_message()
#     return Response(status=HTTPStatus.OK, text="Proactive messages have been sent")
