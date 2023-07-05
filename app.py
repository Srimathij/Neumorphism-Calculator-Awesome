# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import socket
import sys
import pickle
import signal
import traceback
import uuid
from datetime import datetime
import time
from http import HTTPStatus
from typing import Dict

from aiohttp import web
from aiohttp.web import Request, Response, json_response
from botbuilder.core import (
    BotFrameworkAdapterSettings,
    TurnContext,
    BotFrameworkAdapter,
)
from botbuilder.core.integration import aiohttp_error_middleware
from botbuilder.schema import Activity, ActivityTypes, ConversationReference
from sqlalchemy import null

from bots import ProactiveBot
from config import DefaultConfig
from botbuilder.core import ActivityHandler
from sockio import *
import asyncio
from settings import *
import settings as st

# import threading

# def f(f_stop):
#     global socket_in_use
#     socket_in_use.clear()
#     print("SOCKET HAS BEEN CLEARED", socket_in_use)
#     if not f_stop.is_set():
#         # call f() again in 60 seconds
#         threading.Timer(13, f, [f_stop]).start()

# f_stop = threading.Event()
# # start calling f now and every 60 sec thereafter
# f(f_stop)

# stop the thread when needed
#f_stop.set()



CONFIG = DefaultConfig()
async def run():
    await aio.connect('http://localhost:5005/socket.io')
    await bio.connect('http://localhost:5005/socket.io')
    await cio.connect('http://localhost:5005/socket.io')
    await dio.connect('http://localhost:5005/socket.io')
    await eio.connect('http://localhost:5005/socket.io')
    await fio.connect('http://localhost:5005/socket.io')
    await gio.connect('http://localhost:5005/socket.io')
    await hio.connect('http://localhost:5005/socket.io')
    await iio.connect('http://localhost:5005/socket.io')
    await jio.connect('http://localhost:5005/socket.io')
    await kio.connect('http://localhost:5005/socket.io')
    await lio.connect('http://localhost:5005/socket.io')
    await mio.connect('http://localhost:5005/socket.io')
    await nio.connect('http://localhost:5005/socket.io')
    await oio.connect('http://localhost:5005/socket.io')
    await pio.connect('http://localhost:5005/socket.io')
    await qio.connect('http://localhost:5005/socket.io')
    await rio.connect('http://localhost:5005/socket.io')
    await sio.connect('http://localhost:5005/socket.io')
    await tsio.connect('http://localhost:5005/socket.io')
    await usio.connect('http://localhost:5005/socket.io')
    await vsio.connect('http://localhost:5005/socket.io')
    await wsio.connect('http://localhost:5005/socket.io')
    await xio.connect('http://localhost:5005/socket.io')
    await yio.connect('http://localhost:5005/socket.io')
    await zio.connect('http://localhost:5005/socket.io')
    await aaio.connect('http://localhost:5005/socket.io')
    await abio.connect('http://localhost:5005/socket.io')
    await acio.connect('http://localhost:5005/socket.io')
    await adio.connect('http://localhost:5005/socket.io')
    await aeio.connect('http://localhost:5005/socket.io')
    await afio.connect('http://localhost:5005/socket.io')
    await agio.connect('http://localhost:5005/socket.io')
    await ahio.connect('http://localhost:5005/socket.io')
    await aiio.connect('http://localhost:5005/socket.io')
    await ajio.connect('http://localhost:5005/socket.io')
    await akio.connect('http://localhost:5005/socket.io')
    await alio.connect('http://localhost:5005/socket.io')
    await amio.connect('http://localhost:5005/socket.io')
    await anio.connect('http://localhost:5005/socket.io')
    await aoio.connect('http://localhost:5005/socket.io')
    await apio.connect('http://localhost:5005/socket.io')
    await aqio.connect('http://localhost:5005/socket.io')
    await ario.connect('http://localhost:5005/socket.io')
    await asio.connect('http://localhost:5005/socket.io')
    await atio.connect('http://localhost:5005/socket.io')
    await auio.connect('http://localhost:5005/socket.io')
    await avio.connect('http://localhost:5005/socket.io')
    await awio.connect('http://localhost:5005/socket.io')
    await axio.connect('http://localhost:5005/socket.io')
    await ayio.connect('http://localhost:5005/socket.io')
    await azio.connect('http://localhost:5005/socket.io')
    await baio.connect('http://localhost:5005/socket.io')
    await bbio.connect('http://localhost:5005/socket.io')
    await bcio.connect('http://localhost:5005/socket.io')
    await bdio.connect('http://localhost:5005/socket.io')
    await beio.connect('http://localhost:5005/socket.io')
    await bfio.connect('http://localhost:5005/socket.io')
    await bgio.connect('http://localhost:5005/socket.io')
    await bhio.connect('http://localhost:5005/socket.io')
    await biio.connect('http://localhost:5005/socket.io')
    await bjio.connect('http://localhost:5005/socket.io')
    await bkio.connect('http://localhost:5005/socket.io')
    await blio.connect('http://localhost:5005/socket.io')
    await bmio.connect('http://localhost:5005/socket.io')
    await bnio.connect('http://localhost:5005/socket.io')
    await boio.connect('http://localhost:5005/socket.io')
    await bpio.connect('http://localhost:5005/socket.io')
    await bqio.connect('http://localhost:5005/socket.io')
    await brio.connect('http://localhost:5005/socket.io')
    await bsio.connect('http://localhost:5005/socket.io')
    await btio.connect('http://localhost:5005/socket.io')
    await buio.connect('http://localhost:5005/socket.io')
    await bvio.connect('http://localhost:5005/socket.io')
    await bwio.connect('http://localhost:5005/socket.io')
    await bxio.connect('http://localhost:5005/socket.io')
    await byio.connect('http://localhost:5005/socket.io')
    await bzio.connect('http://localhost:5005/socket.io')
    await caio.connect('http://localhost:5005/socket.io')
    await cbio.connect('http://localhost:5005/socket.io')
    await ccio.connect('http://localhost:5005/socket.io')
    await cdio.connect('http://localhost:5005/socket.io')
    await ceio.connect('http://localhost:5005/socket.io')
    await cfio.connect('http://localhost:5005/socket.io')
    await cgio.connect('http://localhost:5005/socket.io')
    await chio.connect('http://localhost:5005/socket.io')
    await ciio.connect('http://localhost:5005/socket.io')
    await cjio.connect('http://localhost:5005/socket.io')
    await ckio.connect('http://localhost:5005/socket.io')
    await clio.connect('http://localhost:5005/socket.io')
    await cmio.connect('http://localhost:5005/socket.io')
    await cnio.connect('http://localhost:5005/socket.io')
    await coio.connect('http://localhost:5005/socket.io')
    await cpio.connect('http://localhost:5005/socket.io')
    await cqio.connect('http://localhost:5005/socket.io')
    await crio.connect('http://localhost:5005/socket.io')
    await csio.connect('http://localhost:5005/socket.io')
    await ctio.connect('http://localhost:5005/socket.io')
    await cuio.connect('http://localhost:5005/socket.io')
    await cvio.connect('http://localhost:5005/socket.io')
    await cwio.connect('http://localhost:5005/socket.io')
    await cxio.connect('http://localhost:5005/socket.io')
    await cyio.connect('http://localhost:5005/socket.io')
    await czio.connect('http://localhost:5005/socket.io')
    await daio.connect('http://localhost:5005/socket.io')
    await dbio.connect('http://localhost:5005/socket.io')
    await dcio.connect('http://localhost:5005/socket.io')
    await ddio.connect('http://localhost:5005/socket.io')
    await deio.connect('http://localhost:5005/socket.io')
    await dfio.connect('http://localhost:5005/socket.io')
    await dgio.connect('http://localhost:5005/socket.io')
    await dhio.connect('http://localhost:5005/socket.io')
    await diio.connect('http://localhost:5005/socket.io')
    await djio.connect('http://localhost:5005/socket.io')
    await dkio.connect('http://localhost:5005/socket.io')
    await dlio.connect('http://localhost:5005/socket.io')
    await dmio.connect('http://localhost:5005/socket.io')
    await dnio.connect('http://localhost:5005/socket.io')
    await doio.connect('http://localhost:5005/socket.io')
    await dpio.connect('http://localhost:5005/socket.io')
    await dqio.connect('http://localhost:5005/socket.io')
    await drio.connect('http://localhost:5005/socket.io')
    await dsio.connect('http://localhost:5005/socket.io')
    await dtio.connect('http://localhost:5005/socket.io')
    await duio.connect('http://localhost:5005/socket.io')
    await dvio.connect('http://localhost:5005/socket.io')
    await dwio.connect('http://localhost:5005/socket.io')
    await dxio.connect('http://localhost:5005/socket.io')
    await dyio.connect('http://localhost:5005/socket.io')
    await dzio.connect('http://localhost:5005/socket.io')
    await eaio.connect('http://localhost:5005/socket.io')
    await ebio.connect('http://localhost:5005/socket.io')
    await ecio.connect('http://localhost:5005/socket.io')
    await edio.connect('http://localhost:5005/socket.io')
    await eeio.connect('http://localhost:5005/socket.io')
    await efio.connect('http://localhost:5005/socket.io')
    await egio.connect('http://localhost:5005/socket.io')
    await ehio.connect('http://localhost:5005/socket.io')
    await eiio.connect('http://localhost:5005/socket.io')
    await ejio.connect('http://localhost:5005/socket.io')
    await ekio.connect('http://localhost:5005/socket.io')
    await elio.connect('http://localhost:5005/socket.io')
    await emio.connect('http://localhost:5005/socket.io')
    await enio.connect('http://localhost:5005/socket.io')
    await eoio.connect('http://localhost:5005/socket.io')
    await epio.connect('http://localhost:5005/socket.io')
    await eqio.connect('http://localhost:5005/socket.io')
    await erio.connect('http://localhost:5005/socket.io')
    await esio.connect('http://localhost:5005/socket.io')
    await etio.connect('http://localhost:5005/socket.io')
    await euio.connect('http://localhost:5005/socket.io')
    await evio.connect('http://localhost:5005/socket.io')
    await ewio.connect('http://localhost:5005/socket.io')
    await exio.connect('http://localhost:5005/socket.io')
    await eyio.connect('http://localhost:5005/socket.io')
    await ezio.connect('http://localhost:5005/socket.io')
    print("SIS id is ",sio.sid)


@sio.event
def connect():
    print("Im connected")

@sio.event
def connect_error(data):
    print("The connection failed!")

@sio.event
def disconnect():
    print("Im disconnected")

@tsio.event
def connect():
    print("Im connected")

@tsio.event
def connect_error(data):
    print("The connection failed!")

@tsio.event
def disconnect():
    print("Im disconnected")

@usio.event
def connect():
    print("Im connected")

@usio.event
def connect_error(data):
    print("The connection failed!")

@usio.event
def disconnect():
    print("Im disconnected")

@vsio.event
def connect():
    print("Im connected")

@vsio.event
def connect_error(data):
    print("The connection failed!")

@vsio.event
def disconnect():
    print("Im disconnected")

@wsio.event
def connect():
    print("Im connected")

@wsio.event
def connect_error(data):
    print("The connection failed!")

@wsio.event
def disconnect():
    print("Im disconnected")

@aio.event
def connect():
    print("Im connected")

@aio.event
def connect_error(data):
    print("The connection failed!")

@aio.event
def disconnect():
    print("Im disconnected")

@bio.event
def connect():
    print("Im connected")

@bio.event
def connect_error(data):
    print("The connection failed!")

@bio.event
def disconnect():
    print("Im disconnected")

@cio.event
def connect():
    print("Im connected")

@cio.event
def connect_error(data):
    print("The connection failed!")

@cio.event
def disconnect():
    print("Im disconnected")

@dio.event
def connect():
    print("Im connected")

@dio.event
def connect_error(data):
    print("The connection failed!")

@dio.event
def disconnect():
    print("Im disconnected")

@eio.event
def connect():
    print("Im connected")

@eio.event
def connect_error(data):
    print("The connection failed!")

@eio.event
def disconnect():
    print("Im disconnected")

@fio.event
def connect():
    print("Im connected")

@fio.event
def connect_error(data):
    print("The connection failed!")

@fio.event
def disconnect():
    print("Im disconnected")

@gio.event
def connect():
    print("Im connected")

@gio.event
def connect_error(data):
    print("The connection failed!")

@gio.event
def disconnect():
    print("Im disconnected")

@hio.event
def connect():
    print("Im connected")

@hio.event
def connect_error(data):
    print("The connection failed!")

@hio.event
def disconnect():
    print("Im disconnected")

@iio.event
def connect():
    print("Im connected")

@iio.event
def connect_error(data):
    print("The connection failed!")

@iio.event
def disconnect():
    print("Im disconnected")


@jio.event
def connect():
    print("Im connected")

@jio.event
def connect_error(data):
    print("The connection failed!")

@jio.event
def disconnect():
    print("Im disconnected")

@kio.event
def connect():
    print("Im connected")

@kio.event
def connect_error(data):
    print("The connection failed!")

@kio.event
def disconnect():
    print("Im disconnected")

@lio.event
def connect():
    print("Im connected")

@lio.event
def connect_error(data):
    print("The connection failed!")

@lio.event
def disconnect():
    print("Im disconnected")

@mio.event
def connect():
    print("Im connected")

@mio.event
def connect_error(data):
    print("The connection failed!")

@mio.event
def disconnect():
    print("Im disconnected")

@nio.event
def connect():
    print("Im connected")

@nio.event
def connect_error(data):
    print("The connection failed!")

@nio.event
def disconnect():
    print("Im disconnected")

@oio.event
def connect():
    print("Im connected")

@oio.event
def connect_error(data):
    print("The connection failed!")

@oio.event
def disconnect():
    print("Im disconnected")

@pio.event
def connect():
    print("Im connected")

@pio.event
def connect_error(data):
    print("The connection failed!")

@pio.event
def disconnect():
    print("Im disconnected")

@qio.event
def connect():
    print("Im connected")

@qio.event
def connect_error(data):
    print("The connection failed!")

@qio.event
def disconnect():
    print("Im disconnected")

@rio.event
def connect():
    print("Im connected")

@rio.event
def connect_error(data):
    print("The connection failed!")

@rio.event
def disconnect():
    print("Im disconnected")

@xio.event
def connect():
    print("Im connected")

@xio.event
def connect_error(data):
    print("The connection failed!")

@xio.event
def disconnect():
    print("Im disconnected")

@yio.event
def connect():
    print("Im connected")

@yio.event
def connect_error(data):
    print("The connection failed!")

@yio.event
def disconnect():
    print("Im disconnected")

@zio.event
def connect():
    print("Im connected")

@zio.event
def connect_error(data):
    print("The connection failed!")

@zio.event
def disconnect():
    print("Im disconnected")

### ------

@asio.event
def connect():
    print("Im connected")

@asio.event
def connect_error(data):
    print("The connection failed!")

@asio.event
def disconnect():
    print("Im disconnected")

@atio.event
def connect():
    print("Im connected")

@atio.event
def connect_error(data):
    print("The connection failed!")

@atio.event
def disconnect():
    print("Im disconnected")

@auio.event
def connect():
    print("Im connected")

@auio.event
def connect_error(data):
    print("The connection failed!")

@auio.event
def disconnect():
    print("Im disconnected")

@avio.event
def connect():
    print("Im connected")

@avio.event
def connect_error(data):
    print("The connection failed!")

@avio.event
def disconnect():
    print("Im disconnected")

@awio.event
def connect():
    print("Im connected")

@awio.event
def connect_error(data):
    print("The connection failed!")

@awio.event
def disconnect():
    print("Im disconnected")

@aaio.event
def connect():
    print("Im connected")

@aaio.event
def connect_error(data):
    print("The connection failed!")

@aaio.event
def disconnect():
    print("Im disconnected")

@abio.event
def connect():
    print("Im connected")

@abio.event
def connect_error(data):
    print("The connection failed!")

@abio.event
def disconnect():
    print("Im disconnected")

@acio.event
def connect():
    print("Im connected")

@acio.event
def connect_error(data):
    print("The connection failed!")

@acio.event
def disconnect():
    print("Im disconnected")

@adio.event
def connect():
    print("Im connected")

@adio.event
def connect_error(data):
    print("The connection failed!")

@adio.event
def disconnect():
    print("Im disconnected")

@aeio.event
def connect():
    print("Im connected")

@aeio.event
def connect_error(data):
    print("The connection failed!")

@aeio.event
def disconnect():
    print("Im disconnected")

@afio.event
def connect():
    print("Im connected")

@afio.event
def connect_error(data):
    print("The connection failed!")

@afio.event
def disconnect():
    print("Im disconnected")

@agio.event
def connect():
    print("Im connected")

@agio.event
def connect_error(data):
    print("The connection failed!")

@agio.event
def disconnect():
    print("Im disconnected")

@ahio.event
def connect():
    print("Im connected")

@ahio.event
def connect_error(data):
    print("The connection failed!")

@ahio.event
def disconnect():
    print("Im disconnected")

@aiio.event
def connect():
    print("Im connected")

@aiio.event
def connect_error(data):
    print("The connection failed!")

@aiio.event
def disconnect():
    print("Im disconnected")


@ajio.event
def connect():
    print("Im connected")

@ajio.event
def connect_error(data):
    print("The connection failed!")

@ajio.event
def disconnect():
    print("Im disconnected")

@akio.event
def connect():
    print("Im connected")

@akio.event
def connect_error(data):
    print("The connection failed!")

@akio.event
def disconnect():
    print("Im disconnected")

@alio.event
def connect():
    print("Im connected")

@alio.event
def connect_error(data):
    print("The connection failed!")

@alio.event
def disconnect():
    print("Im disconnected")

@amio.event
def connect():
    print("Im connected")

@amio.event
def connect_error(data):
    print("The connection failed!")

@amio.event
def disconnect():
    print("Im disconnected")

@anio.event
def connect():
    print("Im connected")

@anio.event
def connect_error(data):
    print("The connection failed!")

@anio.event
def disconnect():
    print("Im disconnected")

@aoio.event
def connect():
    print("Im connected")

@aoio.event
def connect_error(data):
    print("The connection failed!")

@aoio.event
def disconnect():
    print("Im disconnected")

@apio.event
def connect():
    print("Im connected")

@apio.event
def connect_error(data):
    print("The connection failed!")

@apio.event
def disconnect():
    print("Im disconnected")

@aqio.event
def connect():
    print("Im connected")

@aqio.event
def connect_error(data):
    print("The connection failed!")

@aqio.event
def disconnect():
    print("Im disconnected")

@ario.event
def connect():
    print("Im connected")

@ario.event
def connect_error(data):
    print("The connection failed!")

@ario.event
def disconnect():
    print("Im disconnected")

@axio.event
def connect():
    print("Im connected")

@axio.event
def connect_error(data):
    print("The connection failed!")

@axio.event
def disconnect():
    print("Im disconnected")

@ayio.event
def connect():
    print("Im connected")

@ayio.event
def connect_error(data):
    print("The connection failed!")

@ayio.event
def disconnect():
    print("Im disconnected")

@azio.event
def connect():
    print("Im connected")

@azio.event
def connect_error(data):
    print("The connection failed!")

@azio.event
def disconnect():
    print("Im disconnected")

#----

@asio.event
def connect():
    print("Im connected")

@asio.event
def connect_error(data):
    print("The connection failed!")

@asio.event
def disconnect():
    print("Im disconnected")

@atio.event
def connect():
    print("Im connected")

@atio.event
def connect_error(data):
    print("The connection failed!")

@atio.event
def disconnect():
    print("Im disconnected")

@auio.event
def connect():
    print("Im connected")

@auio.event
def connect_error(data):
    print("The connection failed!")

@auio.event
def disconnect():
    print("Im disconnected")

@avio.event
def connect():
    print("Im connected")

@avio.event
def connect_error(data):
    print("The connection failed!")

@avio.event
def disconnect():
    print("Im disconnected")

@awio.event
def connect():
    print("Im connected")

@awio.event
def connect_error(data):
    print("The connection failed!")

@awio.event
def disconnect():
    print("Im disconnected")

@aaio.event
def connect():
    print("Im connected")

@aaio.event
def connect_error(data):
    print("The connection failed!")

@aaio.event
def disconnect():
    print("Im disconnected")

@abio.event
def connect():
    print("Im connected")

@abio.event
def connect_error(data):
    print("The connection failed!")

@abio.event
def disconnect():
    print("Im disconnected")

@acio.event
def connect():
    print("Im connected")

@acio.event
def connect_error(data):
    print("The connection failed!")

@acio.event
def disconnect():
    print("Im disconnected")

@adio.event
def connect():
    print("Im connected")

@adio.event
def connect_error(data):
    print("The connection failed!")

@adio.event
def disconnect():
    print("Im disconnected")

@aeio.event
def connect():
    print("Im connected")

@aeio.event
def connect_error(data):
    print("The connection failed!")

@aeio.event
def disconnect():
    print("Im disconnected")

@afio.event
def connect():
    print("Im connected")

@afio.event
def connect_error(data):
    print("The connection failed!")

@afio.event
def disconnect():
    print("Im disconnected")

@agio.event
def connect():
    print("Im connected")

@agio.event
def connect_error(data):
    print("The connection failed!")

@agio.event
def disconnect():
    print("Im disconnected")

@ahio.event
def connect():
    print("Im connected")

@ahio.event
def connect_error(data):
    print("The connection failed!")

@ahio.event
def disconnect():
    print("Im disconnected")

@aiio.event
def connect():
    print("Im connected")

@aiio.event
def connect_error(data):
    print("The connection failed!")

@aiio.event
def disconnect():
    print("Im disconnected")


@ajio.event
def connect():
    print("Im connected")

@ajio.event
def connect_error(data):
    print("The connection failed!")

@ajio.event
def disconnect():
    print("Im disconnected")

@akio.event
def connect():
    print("Im connected")

@akio.event
def connect_error(data):
    print("The connection failed!")

@akio.event
def disconnect():
    print("Im disconnected")

@alio.event
def connect():
    print("Im connected")

@alio.event
def connect_error(data):
    print("The connection failed!")

@alio.event
def disconnect():
    print("Im disconnected")

@amio.event
def connect():
    print("Im connected")

@amio.event
def connect_error(data):
    print("The connection failed!")

@amio.event
def disconnect():
    print("Im disconnected")

@anio.event
def connect():
    print("Im connected")

@anio.event
def connect_error(data):
    print("The connection failed!")

@anio.event
def disconnect():
    print("Im disconnected")

@aoio.event
def connect():
    print("Im connected")

@aoio.event
def connect_error(data):
    print("The connection failed!")

@aoio.event
def disconnect():
    print("Im disconnected")

@apio.event
def connect():
    print("Im connected")

@apio.event
def connect_error(data):
    print("The connection failed!")

@apio.event
def disconnect():
    print("Im disconnected")

@aqio.event
def connect():
    print("Im connected")

@aqio.event
def connect_error(data):
    print("The connection failed!")

@aqio.event
def disconnect():
    print("Im disconnected")

@ario.event
def connect():
    print("Im connected")

@ario.event
def connect_error(data):
    print("The connection failed!")

@ario.event
def disconnect():
    print("Im disconnected")

@axio.event
def connect():
    print("Im connected")

@axio.event
def connect_error(data):
    print("The connection failed!")

@axio.event
def disconnect():
    print("Im disconnected")

@ayio.event
def connect():
    print("Im connected")

@ayio.event
def connect_error(data):
    print("The connection failed!")

@ayio.event
def disconnect():
    print("Im disconnected")

@azio.event
def connect():
    print("Im connected")

@azio.event
def connect_error(data):
    print("The connection failed!")

@azio.event
def disconnect():
    print("Im disconnected")

# ---
@asio.event
def connect():
    print("Im connected")

@asio.event
def connect_error(data):
    print("The connection failed!")

@asio.event
def disconnect():
    print("Im disconnected")

@atio.event
def connect():
    print("Im connected")

@atio.event
def connect_error(data):
    print("The connection failed!")

@atio.event
def disconnect():
    print("Im disconnected")

@auio.event
def connect():
    print("Im connected")

@auio.event
def connect_error(data):
    print("The connection failed!")

@auio.event
def disconnect():
    print("Im disconnected")

@avio.event
def connect():
    print("Im connected")

@avio.event
def connect_error(data):
    print("The connection failed!")

@avio.event
def disconnect():
    print("Im disconnected")

@awio.event
def connect():
    print("Im connected")

@awio.event
def connect_error(data):
    print("The connection failed!")

@awio.event
def disconnect():
    print("Im disconnected")

@aaio.event
def connect():
    print("Im connected")

@aaio.event
def connect_error(data):
    print("The connection failed!")

@aaio.event
def disconnect():
    print("Im disconnected")

@abio.event
def connect():
    print("Im connected")

@abio.event
def connect_error(data):
    print("The connection failed!")

@abio.event
def disconnect():
    print("Im disconnected")

@acio.event
def connect():
    print("Im connected")

@acio.event
def connect_error(data):
    print("The connection failed!")

@acio.event
def disconnect():
    print("Im disconnected")

@adio.event
def connect():
    print("Im connected")

@adio.event
def connect_error(data):
    print("The connection failed!")

@adio.event
def disconnect():
    print("Im disconnected")

@aeio.event
def connect():
    print("Im connected")

@aeio.event
def connect_error(data):
    print("The connection failed!")

@aeio.event
def disconnect():
    print("Im disconnected")

@afio.event
def connect():
    print("Im connected")

@afio.event
def connect_error(data):
    print("The connection failed!")

@afio.event
def disconnect():
    print("Im disconnected")

@agio.event
def connect():
    print("Im connected")

@agio.event
def connect_error(data):
    print("The connection failed!")

@agio.event
def disconnect():
    print("Im disconnected")

@ahio.event
def connect():
    print("Im connected")

@ahio.event
def connect_error(data):
    print("The connection failed!")

@ahio.event
def disconnect():
    print("Im disconnected")

@aiio.event
def connect():
    print("Im connected")

@aiio.event
def connect_error(data):
    print("The connection failed!")

@aiio.event
def disconnect():
    print("Im disconnected")


@ajio.event
def connect():
    print("Im connected")

@ajio.event
def connect_error(data):
    print("The connection failed!")

@ajio.event
def disconnect():
    print("Im disconnected")

@akio.event
def connect():
    print("Im connected")

@akio.event
def connect_error(data):
    print("The connection failed!")

@akio.event
def disconnect():
    print("Im disconnected")

@alio.event
def connect():
    print("Im connected")

@alio.event
def connect_error(data):
    print("The connection failed!")

@alio.event
def disconnect():
    print("Im disconnected")

@amio.event
def connect():
    print("Im connected")

@amio.event
def connect_error(data):
    print("The connection failed!")

@amio.event
def disconnect():
    print("Im disconnected")

@anio.event
def connect():
    print("Im connected")

@anio.event
def connect_error(data):
    print("The connection failed!")

@anio.event
def disconnect():
    print("Im disconnected")

@aoio.event
def connect():
    print("Im connected")

@aoio.event
def connect_error(data):
    print("The connection failed!")

@aoio.event
def disconnect():
    print("Im disconnected")

@apio.event
def connect():
    print("Im connected")

@apio.event
def connect_error(data):
    print("The connection failed!")

@apio.event
def disconnect():
    print("Im disconnected")

@aqio.event
def connect():
    print("Im connected")

@aqio.event
def connect_error(data):
    print("The connection failed!")

@aqio.event
def disconnect():
    print("Im disconnected")

@ario.event
def connect():
    print("Im connected")

@ario.event
def connect_error(data):
    print("The connection failed!")

@ario.event
def disconnect():
    print("Im disconnected")

@axio.event
def connect():
    print("Im connected")

@axio.event
def connect_error(data):
    print("The connection failed!")

@axio.event
def disconnect():
    print("Im disconnected")

@ayio.event
def connect():
    print("Im connected")

@ayio.event
def connect_error(data):
    print("The connection failed!")

@ayio.event
def disconnect():
    print("Im disconnected")

@azio.event
def connect():
    print("Im connected")

@azio.event
def connect_error(data):
    print("The connection failed!")

@azio.event
def disconnect():
    print("Im disconnected")

#---a
@asio.event
def connect():
    print("Im connected")

@asio.event
def connect_error(data):
    print("The connection failed!")

@asio.event
def disconnect():
    print("Im disconnected")

@atio.event
def connect():
    print("Im connected")

@atio.event
def connect_error(data):
    print("The connection failed!")

@atio.event
def disconnect():
    print("Im disconnected")

@auio.event
def connect():
    print("Im connected")

@auio.event
def connect_error(data):
    print("The connection failed!")

@auio.event
def disconnect():
    print("Im disconnected")

@avio.event
def connect():
    print("Im connected")

@avio.event
def connect_error(data):
    print("The connection failed!")

@avio.event
def disconnect():
    print("Im disconnected")

@awio.event
def connect():
    print("Im connected")

@awio.event
def connect_error(data):
    print("The connection failed!")

@awio.event
def disconnect():
    print("Im disconnected")

@aaio.event
def connect():
    print("Im connected")

@aaio.event
def connect_error(data):
    print("The connection failed!")

@aaio.event
def disconnect():
    print("Im disconnected")

@abio.event
def connect():
    print("Im connected")

@abio.event
def connect_error(data):
    print("The connection failed!")

@abio.event
def disconnect():
    print("Im disconnected")

@acio.event
def connect():
    print("Im connected")

@acio.event
def connect_error(data):
    print("The connection failed!")

@acio.event
def disconnect():
    print("Im disconnected")

@adio.event
def connect():
    print("Im connected")

@adio.event
def connect_error(data):
    print("The connection failed!")

@adio.event
def disconnect():
    print("Im disconnected")

@aeio.event
def connect():
    print("Im connected")

@aeio.event
def connect_error(data):
    print("The connection failed!")

@aeio.event
def disconnect():
    print("Im disconnected")

@afio.event
def connect():
    print("Im connected")

@afio.event
def connect_error(data):
    print("The connection failed!")

@afio.event
def disconnect():
    print("Im disconnected")

@agio.event
def connect():
    print("Im connected")

@agio.event
def connect_error(data):
    print("The connection failed!")

@agio.event
def disconnect():
    print("Im disconnected")

@ahio.event
def connect():
    print("Im connected")

@ahio.event
def connect_error(data):
    print("The connection failed!")

@ahio.event
def disconnect():
    print("Im disconnected")

@aiio.event
def connect():
    print("Im connected")

@aiio.event
def connect_error(data):
    print("The connection failed!")

@aiio.event
def disconnect():
    print("Im disconnected")


@ajio.event
def connect():
    print("Im connected")

@ajio.event
def connect_error(data):
    print("The connection failed!")

@ajio.event
def disconnect():
    print("Im disconnected")

@akio.event
def connect():
    print("Im connected")

@akio.event
def connect_error(data):
    print("The connection failed!")

@akio.event
def disconnect():
    print("Im disconnected")

@alio.event
def connect():
    print("Im connected")

@alio.event
def connect_error(data):
    print("The connection failed!")

@alio.event
def disconnect():
    print("Im disconnected")

@amio.event
def connect():
    print("Im connected")

@amio.event
def connect_error(data):
    print("The connection failed!")

@amio.event
def disconnect():
    print("Im disconnected")

@anio.event
def connect():
    print("Im connected")

@anio.event
def connect_error(data):
    print("The connection failed!")

@anio.event
def disconnect():
    print("Im disconnected")

@aoio.event
def connect():
    print("Im connected")

@aoio.event
def connect_error(data):
    print("The connection failed!")

@aoio.event
def disconnect():
    print("Im disconnected")

@apio.event
def connect():
    print("Im connected")

@apio.event
def connect_error(data):
    print("The connection failed!")

@apio.event
def disconnect():
    print("Im disconnected")

@aqio.event
def connect():
    print("Im connected")

@aqio.event
def connect_error(data):
    print("The connection failed!")

@aqio.event
def disconnect():
    print("Im disconnected")

@ario.event
def connect():
    print("Im connected")

@ario.event
def connect_error(data):
    print("The connection failed!")

@ario.event
def disconnect():
    print("Im disconnected")

@axio.event
def connect():
    print("Im connected")

@axio.event
def connect_error(data):
    print("The connection failed!")

@axio.event
def disconnect():
    print("Im disconnected")

@ayio.event
def connect():
    print("Im connected")

@ayio.event
def connect_error(data):
    print("The connection failed!")

@ayio.event
def disconnect():
    print("Im disconnected")

@azio.event
def connect():
    print("Im connected")

@azio.event
def connect_error(data):
    print("The connection failed!")

@azio.event
def disconnect():
    print("Im disconnected")

#-----b
@bsio.event
def connect():
    print("Im connected")

@bsio.event
def connect_error(data):
    print("The connection failed!")

@bsio.event
def disconnect():
    print("Im disconnected")

@btio.event
def connect():
    print("Im connected")

@btio.event
def connect_error(data):
    print("The connection failed!")

@btio.event
def disconnect():
    print("Im disconnected")

@buio.event
def connect():
    print("Im connected")

@buio.event
def connect_error(data):
    print("The connection failed!")

@buio.event
def disconnect():
    print("Im disconnected")

@bvio.event
def connect():
    print("Im connected")

@bvio.event
def connect_error(data):
    print("The connection failed!")

@bvio.event
def disconnect():
    print("Im disconnected")

@bwio.event
def connect():
    print("Im connected")

@bwio.event
def connect_error(data):
    print("The connection failed!")

@bwio.event
def disconnect():
    print("Im disconnected")

@baio.event
def connect():
    print("Im connected")

@baio.event
def connect_error(data):
    print("The connection failed!")

@baio.event
def disconnect():
    print("Im disconnected")

@bbio.event
def connect():
    print("Im connected")

@bbio.event
def connect_error(data):
    print("The connection failed!")

@bbio.event
def disconnect():
    print("Im disconnected")

@bcio.event
def connect():
    print("Im connected")

@bcio.event
def connect_error(data):
    print("The connection failed!")

@bcio.event
def disconnect():
    print("Im disconnected")

@bdio.event
def connect():
    print("Im connected")

@bdio.event
def connect_error(data):
    print("The connection failed!")

@bdio.event
def disconnect():
    print("Im disconnected")

@beio.event
def connect():
    print("Im connected")

@beio.event
def connect_error(data):
    print("The connection failed!")

@beio.event
def disconnect():
    print("Im disconnected")

@bfio.event
def connect():
    print("Im connected")

@bfio.event
def connect_error(data):
    print("The connection failed!")

@bfio.event
def disconnect():
    print("Im disconnected")

@bgio.event
def connect():
    print("Im connected")

@bgio.event
def connect_error(data):
    print("The connection failed!")

@bgio.event
def disconnect():
    print("Im disconnected")

@bhio.event
def connect():
    print("Im connected")

@bhio.event
def connect_error(data):
    print("The connection failed!")

@bhio.event
def disconnect():
    print("Im disconnected")

@biio.event
def connect():
    print("Im connected")

@biio.event
def connect_error(data):
    print("The connection failed!")

@biio.event
def disconnect():
    print("Im disconnected")


@bjio.event
def connect():
    print("Im connected")

@bjio.event
def connect_error(data):
    print("The connection failed!")

@bjio.event
def disconnect():
    print("Im disconnected")

@bkio.event
def connect():
    print("Im connected")

@bkio.event
def connect_error(data):
    print("The connection failed!")

@bkio.event
def disconnect():
    print("Im disconnected")

@blio.event
def connect():
    print("Im connected")

@blio.event
def connect_error(data):
    print("The connection failed!")

@blio.event
def disconnect():
    print("Im disconnected")

@bmio.event
def connect():
    print("Im connected")

@bmio.event
def connect_error(data):
    print("The connection failed!")

@bmio.event
def disconnect():
    print("Im disconnected")

@bnio.event
def connect():
    print("Im connected")

@bnio.event
def connect_error(data):
    print("The connection failed!")

@bnio.event
def disconnect():
    print("Im disconnected")

@boio.event
def connect():
    print("Im connected")

@boio.event
def connect_error(data):
    print("The connection failed!")

@boio.event
def disconnect():
    print("Im disconnected")

@bpio.event
def connect():
    print("Im connected")

@bpio.event
def connect_error(data):
    print("The connection failed!")

@bpio.event
def disconnect():
    print("Im disconnected")

@bqio.event
def connect():
    print("Im connected")

@bqio.event
def connect_error(data):
    print("The connection failed!")

@bqio.event
def disconnect():
    print("Im disconnected")

@brio.event
def connect():
    print("Im connected")

@brio.event
def connect_error(data):
    print("The connection failed!")

@brio.event
def disconnect():
    print("Im disconnected")

@bxio.event
def connect():
    print("Im connected")

@bxio.event
def connect_error(data):
    print("The connection failed!")

@bxio.event
def disconnect():
    print("Im disconnected")

@byio.event
def connect():
    print("Im connected")

@byio.event
def connect_error(data):
    print("The connection failed!")

@byio.event
def disconnect():
    print("Im disconnected")

@bzio.event
def connect():
    print("Im connected")

@bzio.event
def connect_error(data):
    print("The connection failed!")

@bzio.event
def disconnect():
    print("Im disconnected")

#----c
@csio.event
def connect():
    print("Im connected")

@csio.event
def connect_error(data):
    print("The connection failed!")

@csio.event
def disconnect():
    print("Im disconnected")

@ctio.event
def connect():
    print("Im connected")

@ctio.event
def connect_error(data):
    print("The connection failed!")

@ctio.event
def disconnect():
    print("Im disconnected")

@cuio.event
def connect():
    print("Im connected")

@cuio.event
def connect_error(data):
    print("The connection failed!")

@cuio.event
def disconnect():
    print("Im disconnected")

@cvio.event
def connect():
    print("Im connected")

@cvio.event
def connect_error(data):
    print("The connection failed!")

@cvio.event
def disconnect():
    print("Im disconnected")

@cwio.event
def connect():
    print("Im connected")

@cwio.event
def connect_error(data):
    print("The connection failed!")

@cwio.event
def disconnect():
    print("Im disconnected")

@caio.event
def connect():
    print("Im connected")

@caio.event
def connect_error(data):
    print("The connection failed!")

@caio.event
def disconnect():
    print("Im disconnected")

@cbio.event
def connect():
    print("Im connected")

@cbio.event
def connect_error(data):
    print("The connection failed!")

@cbio.event
def disconnect():
    print("Im disconnected")

@ccio.event
def connect():
    print("Im connected")

@ccio.event
def connect_error(data):
    print("The connection failed!")

@ccio.event
def disconnect():
    print("Im disconnected")

@cdio.event
def connect():
    print("Im connected")

@cdio.event
def connect_error(data):
    print("The connection failed!")

@cdio.event
def disconnect():
    print("Im disconnected")

@ceio.event
def connect():
    print("Im connected")

@ceio.event
def connect_error(data):
    print("The connection failed!")

@ceio.event
def disconnect():
    print("Im disconnected")

@cfio.event
def connect():
    print("Im connected")

@cfio.event
def connect_error(data):
    print("The connection failed!")

@cfio.event
def disconnect():
    print("Im disconnected")

@cgio.event
def connect():
    print("Im connected")

@cgio.event
def connect_error(data):
    print("The connection failed!")

@cgio.event
def disconnect():
    print("Im disconnected")

@chio.event
def connect():
    print("Im connected")

@chio.event
def connect_error(data):
    print("The connection failed!")

@chio.event
def disconnect():
    print("Im disconnected")

@ciio.event
def connect():
    print("Im connected")

@ciio.event
def connect_error(data):
    print("The connection failed!")

@ciio.event
def disconnect():
    print("Im disconnected")


@cjio.event
def connect():
    print("Im connected")

@cjio.event
def connect_error(data):
    print("The connection failed!")

@cjio.event
def disconnect():
    print("Im disconnected")

@ckio.event
def connect():
    print("Im connected")

@ckio.event
def connect_error(data):
    print("The connection failed!")

@ckio.event
def disconnect():
    print("Im disconnected")

@clio.event
def connect():
    print("Im connected")

@clio.event
def connect_error(data):
    print("The connection failed!")

@clio.event
def disconnect():
    print("Im disconnected")

@cmio.event
def connect():
    print("Im connected")

@cmio.event
def connect_error(data):
    print("The connection failed!")

@cmio.event
def disconnect():
    print("Im disconnected")

@cnio.event
def connect():
    print("Im connected")

@cnio.event
def connect_error(data):
    print("The connection failed!")

@cnio.event
def disconnect():
    print("Im disconnected")

@coio.event
def connect():
    print("Im connected")

@coio.event
def connect_error(data):
    print("The connection failed!")

@coio.event
def disconnect():
    print("Im disconnected")

@cpio.event
def connect():
    print("Im connected")

@cpio.event
def connect_error(data):
    print("The connection failed!")

@cpio.event
def disconnect():
    print("Im disconnected")

@cqio.event
def connect():
    print("Im connected")

@cqio.event
def connect_error(data):
    print("The connection failed!")

@cqio.event
def disconnect():
    print("Im disconnected")

@crio.event
def connect():
    print("Im connected")

@crio.event
def connect_error(data):
    print("The connection failed!")

@crio.event
def disconnect():
    print("Im disconnected")

@cxio.event
def connect():
    print("Im connected")

@cxio.event
def connect_error(data):
    print("The connection failed!")

@cxio.event
def disconnect():
    print("Im disconnected")

@cyio.event
def connect():
    print("Im connected")

@cyio.event
def connect_error(data):
    print("The connection failed!")

@cyio.event
def disconnect():
    print("Im disconnected")

@czio.event
def connect():
    print("Im connected")

@czio.event
def connect_error(data):
    print("The connection failed!")

@czio.event
def disconnect():
    print("Im disconnected")

#----d
@dsio.event
def connect():
    print("Im connected")

@dsio.event
def connect_error(data):
    print("The connection failed!")

@dsio.event
def disconnect():
    print("Im disconnected")

@dtio.event
def connect():
    print("Im connected")

@dtio.event
def connect_error(data):
    print("The connection failed!")

@dtio.event
def disconnect():
    print("Im disconnected")

@duio.event
def connect():
    print("Im connected")

@duio.event
def connect_error(data):
    print("The connection failed!")

@duio.event
def disconnect():
    print("Im disconnected")

@dvio.event
def connect():
    print("Im connected")

@dvio.event
def connect_error(data):
    print("The connection failed!")

@dvio.event
def disconnect():
    print("Im disconnected")

@dwio.event
def connect():
    print("Im connected")

@dwio.event
def connect_error(data):
    print("The connection failed!")

@dwio.event
def disconnect():
    print("Im disconnected")

@daio.event
def connect():
    print("Im connected")

@daio.event
def connect_error(data):
    print("The connection failed!")

@daio.event
def disconnect():
    print("Im disconnected")

@dbio.event
def connect():
    print("Im connected")

@dbio.event
def connect_error(data):
    print("The connection failed!")

@dbio.event
def disconnect():
    print("Im disconnected")

@dcio.event
def connect():
    print("Im connected")

@dcio.event
def connect_error(data):
    print("The connection failed!")

@dcio.event
def disconnect():
    print("Im disconnected")

@ddio.event
def connect():
    print("Im connected")

@ddio.event
def connect_error(data):
    print("The connection failed!")

@ddio.event
def disconnect():
    print("Im disconnected")

@deio.event
def connect():
    print("Im connected")

@deio.event
def connect_error(data):
    print("The connection failed!")

@deio.event
def disconnect():
    print("Im disconnected")

@dfio.event
def connect():
    print("Im connected")

@dfio.event
def connect_error(data):
    print("The connection failed!")

@dfio.event
def disconnect():
    print("Im disconnected")

@dgio.event
def connect():
    print("Im connected")

@dgio.event
def connect_error(data):
    print("The connection failed!")

@dgio.event
def disconnect():
    print("Im disconnected")

@dhio.event
def connect():
    print("Im connected")

@dhio.event
def connect_error(data):
    print("The connection failed!")

@dhio.event
def disconnect():
    print("Im disconnected")

@diio.event
def connect():
    print("Im connected")

@diio.event
def connect_error(data):
    print("The connection failed!")

@diio.event
def disconnect():
    print("Im disconnected")

@djio.event
def connect():
    print("Im connected")

@djio.event
def connect_error(data):
    print("The connection failed!")

@djio.event
def disconnect():
    print("Im disconnected")

@dkio.event
def connect():
    print("Im connected")

@dkio.event
def connect_error(data):
    print("The connection failed!")

@dkio.event
def disconnect():
    print("Im disconnected")

@dlio.event
def connect():
    print("Im connected")

@dlio.event
def connect_error(data):
    print("The connection failed!")

@dlio.event
def disconnect():
    print("Im disconnected")

@dmio.event
def connect():
    print("Im connected")

@dmio.event
def connect_error(data):
    print("The connection failed!")

@dmio.event
def disconnect():
    print("Im disconnected")

@dnio.event
def connect():
    print("Im connected")

@dnio.event
def connect_error(data):
    print("The connection failed!")

@dnio.event
def disconnect():
    print("Im disconnected")

@doio.event
def connect():
    print("Im connected")

@doio.event
def connect_error(data):
    print("The connection failed!")

@doio.event
def disconnect():
    print("Im disconnected")

@dpio.event
def connect():
    print("Im connected")

@dpio.event
def connect_error(data):
    print("The connection failed!")

@dpio.event
def disconnect():
    print("Im disconnected")

@dqio.event
def connect():
    print("Im connected")

@dqio.event
def connect_error(data):
    print("The connection failed!")

@dqio.event
def disconnect():
    print("Im disconnected")

@drio.event
def connect():
    print("Im connected")

@drio.event
def connect_error(data):
    print("The connection failed!")

@drio.event
def disconnect():
    print("Im disconnected")

@dxio.event
def connect():
    print("Im connected")

@dxio.event
def connect_error(data):
    print("The connection failed!")

@dxio.event
def disconnect():
    print("Im disconnected")

@dyio.event
def connect():
    print("Im connected")

@dyio.event
def connect_error(data):
    print("The connection failed!")

@dyio.event
def disconnect():
    print("Im disconnected")

@dzio.event
def connect():
    print("Im connected")

@dzio.event
def connect_error(data):
    print("The connection failed!")

@dzio.event
def disconnect():
    print("Im disconnected")

#-----e

@esio.event
def connect():
    print("Im connected")

@esio.event
def connect_error(data):
    print("The connection failed!")

@esio.event
def disconnect():
    print("Im disconnected")

@etio.event
def connect():
    print("Im connected")

@etio.event
def connect_error(data):
    print("The connection failed!")

@etio.event
def disconnect():
    print("Im disconnected")

@euio.event
def connect():
    print("Im connected")

@euio.event
def connect_error(data):
    print("The connection failed!")

@euio.event
def disconnect():
    print("Im disconnected")

@evio.event
def connect():
    print("Im connected")

@evio.event
def connect_error(data):
    print("The connection failed!")

@evio.event
def disconnect():
    print("Im disconnected")

@ewio.event
def connect():
    print("Im connected")

@ewio.event
def connect_error(data):
    print("The connection failed!")

@ewio.event
def disconnect():
    print("Im disconnected")

@eaio.event
def connect():
    print("Im connected")

@eaio.event
def connect_error(data):
    print("The connection failed!")

@eaio.event
def disconnect():
    print("Im disconnected")

@ebio.event
def connect():
    print("Im connected")

@ebio.event
def connect_error(data):
    print("The connection failed!")

@ebio.event
def disconnect():
    print("Im disconnected")

@ecio.event
def connect():
    print("Im connected")

@ecio.event
def connect_error(data):
    print("The connection failed!")

@ecio.event
def disconnect():
    print("Im disconnected")

@edio.event
def connect():
    print("Im connected")

@edio.event
def connect_error(data):
    print("The connection failed!")

@edio.event
def disconnect():
    print("Im disconnected")

@eeio.event
def connect():
    print("Im connected")

@eeio.event
def connect_error(data):
    print("The connection failed!")

@eeio.event
def disconnect():
    print("Im disconnected")

@efio.event
def connect():
    print("Im connected")

@efio.event
def connect_error(data):
    print("The connection failed!")

@efio.event
def disconnect():
    print("Im disconnected")

@egio.event
def connect():
    print("Im connected")

@egio.event
def connect_error(data):
    print("The connection failed!")

@egio.event
def disconnect():
    print("Im disconnected")

@ehio.event
def connect():
    print("Im connected")

@ehio.event
def connect_error(data):
    print("The connection failed!")

@ehio.event
def disconnect():
    print("Im disconnected")

@eiio.event
def connect():
    print("Im connected")

@eiio.event
def connect_error(data):
    print("The connection failed!")

@eiio.event
def disconnect():
    print("Im disconnected")

@ejio.event
def connect():
    print("Im connected")

@ejio.event
def connect_error(data):
    print("The connection failed!")

@ejio.event
def disconnect():
    print("Im disconnected")

@ekio.event
def connect():
    print("Im connected")

@ekio.event
def connect_error(data):
    print("The connection failed!")

@ekio.event
def disconnect():
    print("Im disconnected")

@elio.event
def connect():
    print("Im connected")

@elio.event
def connect_error(data):
    print("The connection failed!")

@elio.event
def disconnect():
    print("Im disconnected")

@emio.event
def connect():
    print("Im connected")

@emio.event
def connect_error(data):
    print("The connection failed!")

@emio.event
def disconnect():
    print("Im disconnected")

@enio.event
def connect():
    print("Im connected")

@enio.event
def connect_error(data):
    print("The connection failed!")

@enio.event
def disconnect():
    print("Im disconnected")

@eoio.event
def connect():
    print("Im connected")

@eoio.event
def connect_error(data):
    print("The connection failed!")

@eoio.event
def disconnect():
    print("Im disconnected")

@epio.event
def connect():
    print("Im connected")

@epio.event
def connect_error(data):
    print("The connection failed!")

@epio.event
def disconnect():
    print("Im disconnected")

@eqio.event
def connect():
    print("Im connected")

@eqio.event
def connect_error(data):
    print("The connection failed!")

@eqio.event
def disconnect():
    print("Im disconnected")

@erio.event
def connect():
    print("Im connected")

@erio.event
def connect_error(data):
    print("The connection failed!")

@erio.event
def disconnect():
    print("Im disconnected")

@exio.event
def connect():
    print("Im connected")

@exio.event
def connect_error(data):
    print("The connection failed!")

@exio.event
def disconnect():
    print("Im disconnected")

@eyio.event
def connect():
    print("Im connected")

@eyio.event
def connect_error(data):
    print("The connection failed!")

@eyio.event
def disconnect():
    print("Im disconnected")

@ezio.event
def connect():
    print("Im connected")

@ezio.event
def connect_error(data):
    print("The connection failed!")

@ezio.event
def disconnect():
    print("Im disconnected")


loop = asyncio.get_event_loop()
loop.run_until_complete(run())

# Create adapter.
# See https://aka.ms/about-bot-adapter to learn more about how bots work.
SETTINGS = BotFrameworkAdapterSettings(CONFIG.APP_ID, CONFIG.APP_PASSWORD)
ADAPTER = BotFrameworkAdapter(SETTINGS)


# Catch-all for errors.
async def on_error(context: TurnContext, error: Exception):
    # This check writes out errors to console log .vs. app insights.
    # NOTE: In production environment, you should consider logging this to Azure
    #       application insights.
    print(f"\n [on_turn_error] unhandled error: {error}", file=sys.stderr)
    traceback.print_exc()

    # Send a message to the user
    await context.send_activity("Psst, I might be a little stuck here.")
    await context.send_activity(
        "Please re-send the message or try contacting my creators, they know how to fix me :p"
    )
    # Send a trace activity if we're talking to the Bot Framework Emulator
    if context.activity.channel_id == "emulator":
        # Create a trace activity that contains the error object
        trace_activity = Activity(
            label="TurnError",
            name="on_turn_error Trace",
            timestamp=datetime.utcnow(),
            type=ActivityTypes.trace,
            value=f"{error}",
            value_type="https://www.botframework.com/schemas/error",
        )
        # Send a trace activity, which will be displayed in Bot Framework Emulator
        await context.send_activity(trace_activity)


ADAPTER.on_turn_error = on_error

# Create a shared dictionary.  The Bot will add conversation references when users
# join the conversation and send messages.
# st.CONVERSATION_REFERENCES: Dict[str, ConversationReference] = dict()

# If the channel is the Emulator, and authentication is not in use, the AppId will be null.
# We generate a random AppId for this case only. This is not required for production, since
# the AppId will have a value.
APP_ID = SETTINGS.app_id if SETTINGS.app_id else uuid.uuid4()

try:
    with open('conversation_ref.pickle','rb') as f:
        st.CONVERSATION_REFERENCES = pickle.load(f)
        print("CONVERSATION REFERENCE LOADED", st.CONVERSATION_REFERENCES)
except Exception as e:
    print("SMALL ERROR ", e)
# Create the Bot
BOT = ProactiveBot(st.CONVERSATION_REFERENCES)



# Listen for incoming requests on /api/messages.]
async def messages(req: Request) -> Response:
    global activity_list, activity_id, temp
    #q = str(TurnContext.get_conversation_reference(TurnContext.activity).user.id)
    #print("THIS IS THE USER ", q)
    print("THERE IS A DEALY HERE")
    # Main bot message handler.
    if "application/json" in req.headers["Content-Type"]:
        body = await req.json()
    else:
        return Response(status=HTTPStatus.UNSUPPORTED_MEDIA_TYPE)
    activity = Activity().deserialize(body)
    # print("this is activity ", activity.id, 'and this is the type :::::',activity.entities)
    # activity_id.append(activity.id)
    # print("THIS IS ID OF ACTIVITY ", activity_id)
    check = True
    ##### Approaches:
    ##### Multi Processing - But each process has seperate pools of data and dont interact with the other process 
    ##### Multi Threading - A joke in Python. For now. 
    ##### Check here itself if the socket is used or not and if used if the previous message that used it has been there for more than 5 seconds or not. Check all sockets if empty or not. 
    ##### If not empty then check if exisitng id has been ther for more than 5-10 seconds or not. 
    ##### check if req can be stored instead of req

    auth_header = req.headers["Authorization"] if "Authorization" in req.headers else ""
    response = await ADAPTER.process_activity(activity, auth_header, BOT.on_turn)
    if response:
        return json_response(data=response.body, status=response.status)
    return Response(status=HTTPStatus.OK)


# Listen for requests on /api/notify, and send a messages to all conversation members.
async def notify(req: Request) -> Response:  # pylint: disable=unused-argument
    print('THIS IS BEING SENT OVER CURL')
    await _send_proactive_message()
    return Response(status=HTTPStatus.OK, text="Proactive messages have been sent")



################################### sock.on ######################################

@aio.on("bot_uttered")
async def get_response_t(data=None):


    print("THIS IS THE DATA inside socket_1", data)
    socket_list_1 = list(socket_1.keys())

    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_1[0] == conversation_reference.user.id:
            # print("THIS SI CONVERSATION REFERENCE ::::: ",conversation_reference.conversation)
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )  

@bio.on("bot_uttered")
async def get_response_t(data=None):


    print("THIS IS THE DATA inside socket_2", data)
    socket_list_2 = list(socket_2.keys())

    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_2[0] == conversation_reference.user.id:
            # print("THIS SI CONVERSATION REFERENCE ::::: ",conversation_reference.conversation)
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )  

@cio.on("bot_uttered")
async def get_response_t(data=None):


    print("THIS IS THE DATA inside socket_3", data)
    socket_list_3 = list(socket_3.keys())

    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_3[0] == conversation_reference.user.id:
            # print("THIS SI CONVERSATION REFERENCE ::::: ",conversation_reference.conversation)
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )  

@dio.on("bot_uttered")
async def get_response_t(data=None):


    print("THIS IS THE DATA inside socket_4", data)
    socket_list_4 = list(socket_4.keys())

    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_4[0] == conversation_reference.user.id:
            # print("THIS SI CONVERSATION REFERENCE ::::: ",conversation_reference.conversation)
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )  

@eio.on("bot_uttered")
async def get_response_t(data=None):


    print("THIS IS THE DATA inside socket_5", data)
    socket_list_5 = list(socket_5.keys())

    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_5[0] == conversation_reference.user.id:
            # print("THIS SI CONVERSATION REFERENCE ::::: ",conversation_reference.conversation)
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )  

@fio.on("bot_uttered")
async def get_response_t(data=None):

    print("THIS IS THE DATA inside socket_6", data)
    socket_list_6 = list(socket_6.keys())

    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_6[0] == conversation_reference.user.id:
            # print("THIS SI CONVERSATION REFERENCE ::::: ",conversation_reference.conversation)
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )  

@gio.on("bot_uttered")
async def get_response_t(data=None):

    print("THIS IS THE DATA inside socket_2", data)
    socket_list_7 = list(socket_7.keys())

    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_7[0] == conversation_reference.user.id:
            # print("THIS SI CONVERSATION REFERENCE ::::: ",conversation_reference.conversation)
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )  

@hio.on("bot_uttered")
async def get_response_t(data=None):
 

    print("THIS IS THE DATA inside socket_8", data)
    socket_list_8 = list(socket_8.keys())

    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_8[0] == conversation_reference.user.id:
            # print("THIS SI CONVERSATION REFERENCE ::::: ",conversation_reference.conversation)
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )  

@iio.on("bot_uttered")
async def get_response_t(data=None):

    print("THIS IS THE DATA inside socket_9", data)
    socket_list_9 = list(socket_9.keys())

    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_9[0] == conversation_reference.user.id:
            # print("THIS SI CONVERSATION REFERENCE ::::: ",conversation_reference.conversation)
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )  

@jio.on("bot_uttered")
async def get_response_t(data=None):

    print("THIS IS THE DATA inside socket_10", data)
    socket_list_10 = list(socket_10.keys())

    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_10[0] == conversation_reference.user.id:
            # print("THIS SI CONVERSATION REFERENCE ::::: ",conversation_reference.conversation)
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )  

@kio.on("bot_uttered")
async def get_response_t(data=None):

    print("THIS IS THE DATA inside socket_11", data)
    socket_list_11 = list(socket_11.keys())

    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_11[0] == conversation_reference.user.id:
            # print("THIS SI CONVERSATION REFERENCE ::::: ",conversation_reference.conversation)
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )  

@lio.on("bot_uttered")
async def get_response_t(data=None):


    print("THIS IS THE DATA inside socket_12", data)
    socket_list_12 = list(socket_12.keys())

    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_12[0] == conversation_reference.user.id:
            # print("THIS SI CONVERSATION REFERENCE ::::: ",conversation_reference.conversation)
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )  

@mio.on("bot_uttered")
async def get_response_t(data=None):


    print("THIS IS THE DATA inside socket_13", data)
    socket_list_13 = list(socket_13.keys())

    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_13[0] == conversation_reference.user.id:
            # print("THIS SI CONVERSATION REFERENCE ::::: ",conversation_reference.conversation)
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )  

@nio.on("bot_uttered")
async def get_response_t(data=None):


    print("THIS IS THE DATA inside socket_14", data)
    socket_list_14 = list(socket_14.keys())

    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_14[0] == conversation_reference.user.id:
            # print("THIS SI CONVERSATION REFERENCE ::::: ",conversation_reference.conversation)
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )  

@oio.on("bot_uttered")
async def get_response_t(data=None):


    print("THIS IS THE DATA inside socket_15", data)
    socket_list_15 = list(socket_15.keys())

    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_15[0] == conversation_reference.user.id:
            # print("THIS SI CONVERSATION REFERENCE ::::: ",conversation_reference.conversation)
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )  

@pio.on("bot_uttered")
async def get_response_t(data=None):


    print("THIS IS THE DATA inside socket_16", data)
    socket_list_16 = list(socket_16.keys())

    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_16[0] == conversation_reference.user.id:
            # print("THIS SI CONVERSATION REFERENCE ::::: ",conversation_reference.conversation)
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )  

@qio.on("bot_uttered")
async def get_response_t(data=None):

    print("THIS IS THE DATA inside socket_17", data)
    socket_list_17 = list(socket_17.keys())

    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_17[0] == conversation_reference.user.id:
            # print("THIS SI CONVERSATION REFERENCE ::::: ",conversation_reference.conversation)
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )  

@rio.on("bot_uttered")
async def get_response_t(data=None):

    print("THIS IS THE DATA inside socket_18", data)
    socket_list_2 = list(socket_2.keys())

    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_2[0] == conversation_reference.user.id:
            # print("THIS SI CONVERSATION REFERENCE ::::: ",conversation_reference.conversation)
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )  

@sio.on("bot_uttered")
async def get_response_s(data=None):
    global activity_id
    # hert=activity_id.copy()
    # activity_id=[]
    print("THIS IS THE DATA inside socket_19", data)
    socket_list_19 = list(socket_19.keys())
    # while socket_list_1:
    # print("ACTIVITY ID INSIDE WHILE ," ,activity_id)
        # if not activity_id :
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        # print("THIS IS CONVERSATION REF INSIDE 1 and id is :::: ", conversation_reference.user.id, 'and ::::: ', socket_list_1[0])
        if socket_list_19[0] == conversation_reference.user.id:
            print("INSIDE 1 bruv")
            # print("THIS SI CONVERSATION REFERENCE ::::: ",conversation_reference.conversation)
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )
    # try:
    #     del socket_in_use[socket_list_1[0]]
    #     print("THIS IS UPDATED SOCKET_IN_USE ", socket_in_use)
    # except: 
    #     print("ALREADY DELETED")
    # print("\n****************\n",hert)
    # print('RESPONSE FROM RASA ', data)
    # for active_id in hert:
    #     for conversation_reference in st.CONVERSATION_REFERENCES.values():
    #             if active_id == conversation_reference.activity_id:
    #                 print("THIS SI CONVERSATION REFERENCE ::::: ",conversation_reference.conversation)
    #                 await ADAPTER.continue_conversation(
    #                     conversation_reference,
    #                     lambda turn_context: turn_context.send_activity(data['text']),
    #                     APP_ID,
    #                 )
    #     # hert.remove(active_id)
    #     print(activity_id,"****")
    #     if activity_id:
    #         activity_id.pop(0)           
    # activity_id = []

@tsio.on("bot_uttered")
async def get_response_t(data=None):


    print("THIS IS THE DATA inside socket_20", data)
    socket_list_20 = list(socket_20.keys())

    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_20[0] == conversation_reference.user.id:
            # print("THIS SI CONVERSATION REFERENCE ::::: ",conversation_reference.conversation)
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )     

@usio.on("bot_uttered")
async def get_response_u(data=None):

    print("THIS IS THE DATA inside socket_21", data)
    socket_list_21 = list(socket_21.keys())
    # while socket_list_3:
            # print("ACTIVITY ID INSIDE WHILE ," ,activity_id)
        # if not activity_id :
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_21[0] == conversation_reference.user.id:
            # print("THIS SI CONVERSATION REFERENCE ::::: ",conversation_reference.conversation)
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )

@vsio.on("bot_uttered")
async def get_response_v(data=None):

    print("THIS IS THE DATA inside socket_22", data)
    socket_list_22 = list(socket_22.keys())
    # w?hile socket_list_4:
        #   print("ACTIVITY ID INSIDE WHILE ," ,activity_id)
        # if not activity_id :
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_22[0] == conversation_reference.user.id:
            # print("THIS SI CONVERSATION REFERENCE ::::: ",conversation_reference.conversation)
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            ) 

@wsio.on("bot_uttered")
async def get_response_w(data=None):


    print("THIS IS THE DATA inside socket_23", data)
    socket_list_23 = list(socket_23.keys())
    # print("ACTIVITY ID INSIDE WHILE ," ,activity_id)
    # if not activity_id :
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_23[0] == conversation_reference.user.id:
            # print("THIS SI CONVERSATION REFERENCE ::::: ",conversation_reference.conversation)
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )    

@xio.on("bot_uttered")
async def get_response_t(data=None):

    print("THIS IS THE DATA inside socket_24", data)
    socket_list_24 = list(socket_24.keys())
    # while socket_list_2:
    # print("ACTIVITY ID INSIDE WHILE ," ,activity_id)
        # if not activity_id :
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_24[0] == conversation_reference.user.id:
            # print("THIS SI CONVERSATION REFERENCE ::::: ",conversation_reference.conversation)
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )  

@yio.on("bot_uttered")
async def get_response_t(data=None):

    print("THIS IS THE DATA inside socket_25", data)
    socket_list_25 = list(socket_25.keys())
    # while socket_list_2:
    # print("ACTIVITY ID INSIDE WHILE ," ,activity_id)
        # if not activity_id :
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_25[0] == conversation_reference.user.id:
            # print("THIS SI CONVERSATION REFERENCE ::::: ",conversation_reference.conversation)
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )  

@zio.on("bot_uttered")
async def get_response_t(data=None):

    print("THIS IS THE DATA inside socket_26", data)
    socket_list_26 = list(socket_26.keys())
    # while socket_list_2:
    # print("ACTIVITY ID INSIDE WHILE ," ,activity_id)
        # if not activity_id :
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_26[0] == conversation_reference.user.id:
            # print("THIS SI CONVERSATION REFERENCE ::::: ",conversation_reference.conversation)
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )  
               
### -------a

@aaio.on("bot_uttered")
async def get_response_t(data=None):


    print("THIS IS THE DATA inside socket_27", data)
    socket_list_27 = list(socket_27.keys())

    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_27[0] == conversation_reference.user.id:
            # print("THIS SI CONVERSATION REFERENCE ::::: ",conversation_reference.conversation)
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )  

@abio.on("bot_uttered")
async def get_response_t(data=None):


    print("THIS IS THE DATA inside socket_28", data)
    socket_list_28 = list(socket_28.keys())

    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_28[0] == conversation_reference.user.id:
            # print("THIS SI CONVERSATION REFERENCE ::::: ",conversation_reference.conversation)
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )  

@acio.on("bot_uttered")
async def get_response_t(data=None):


    print("THIS IS THE DATA inside socket_29", data)
    socket_list_29 = list(socket_29.keys())

    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_29[0] == conversation_reference.user.id:
            # print("THIS SI CONVERSATION REFERENCE ::::: ",conversation_reference.conversation)
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )  

@adio.on("bot_uttered")
async def get_response_t(data=None):


    print("THIS IS THE DATA inside socket_30", data)
    socket_list_30 = list(socket_30.keys())

    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_30[0] == conversation_reference.user.id:
            # print("THIS SI CONVERSATION REFERENCE ::::: ",conversation_reference.conversation)
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )  

@aeio.on("bot_uttered")
async def get_response_t(data=None):


    print("THIS IS THE DATA inside socket_31", data)
    socket_list_31 = list(socket_31.keys())

    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_31[0] == conversation_reference.user.id:
            # print("THIS SI CONVERSATION REFERENCE ::::: ",conversation_reference.conversation)
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )  

@afio.on("bot_uttered")
async def get_response_t(data=None):

    print("THIS IS THE DATA inside socket_32", data)
    socket_list_32 = list(socket_32.keys())

    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_32[0] == conversation_reference.user.id:
            # print("THIS SI CONVERSATION REFERENCE ::::: ",conversation_reference.conversation)
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )  

@agio.on("bot_uttered")
async def get_response_t(data=None):

    print("THIS IS THE DATA inside socket_33", data)
    socket_list_33 = list(socket_33.keys())

    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_33[0] == conversation_reference.user.id:
            # print("THIS SI CONVERSATION REFERENCE ::::: ",conversation_reference.conversation)
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )  

@ahio.on("bot_uttered")
async def get_response_t(data=None):
 

    print("THIS IS THE DATA inside socket_34", data)
    socket_list_34 = list(socket_34.keys())

    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_34[0] == conversation_reference.user.id:
            # print("THIS SI CONVERSATION REFERENCE ::::: ",conversation_reference.conversation)
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )  

@aiio.on("bot_uttered")
async def get_response_t(data=None):

    print("THIS IS THE DATA inside socket_35", data)
    socket_list_35 = list(socket_35.keys())

    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_35[0] == conversation_reference.user.id:
            # print("THIS SI CONVERSATION REFERENCE ::::: ",conversation_reference.conversation)
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )  

@ajio.on("bot_uttered")
async def get_response_t(data=None):

    print("THIS IS THE DATA inside socket_36", data)
    socket_list_36 = list(socket_36.keys())

    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_36[0] == conversation_reference.user.id:
            # print("THIS SI CONVERSATION REFERENCE ::::: ",conversation_reference.conversation)
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )  

@akio.on("bot_uttered")
async def get_response_t(data=None):

    print("THIS IS THE DATA inside socket_37", data)
    socket_list_37 = list(socket_37.keys())

    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_37[0] == conversation_reference.user.id:
            # print("THIS SI CONVERSATION REFERENCE ::::: ",conversation_reference.conversation)
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )  

@alio.on("bot_uttered")
async def get_response_t(data=None):


    print("THIS IS THE DATA inside socket_38", data)
    socket_list_38 = list(socket_38.keys())

    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_38[0] == conversation_reference.user.id:
            # print("THIS SI CONVERSATION REFERENCE ::::: ",conversation_reference.conversation)
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )  

@amio.on("bot_uttered")
async def get_response_t(data=None):


    print("THIS IS THE DATA inside socket_39", data)
    socket_list_39 = list(socket_39.keys())

    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_39[0] == conversation_reference.user.id:
            # print("THIS SI CONVERSATION REFERENCE ::::: ",conversation_reference.conversation)
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )  

@anio.on("bot_uttered")
async def get_response_t(data=None):


    print("THIS IS THE DATA inside socket_40", data)
    socket_list_40 = list(socket_40.keys())

    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_40[0] == conversation_reference.user.id:
            # print("THIS SI CONVERSATION REFERENCE ::::: ",conversation_reference.conversation)
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )  

@aoio.on("bot_uttered")
async def get_response_t(data=None):


    print("THIS IS THE DATA inside socket_41", data)
    socket_list_41 = list(socket_41.keys())

    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_41[0] == conversation_reference.user.id:
            # print("THIS SI CONVERSATION REFERENCE ::::: ",conversation_reference.conversation)
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )  

@apio.on("bot_uttered")
async def get_response_t(data=None):


    print("THIS IS THE DATA inside socket_42", data)
    socket_list_42 = list(socket_42.keys())

    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_42[0] == conversation_reference.user.id:
            # print("THIS SI CONVERSATION REFERENCE ::::: ",conversation_reference.conversation)
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )  

@aqio.on("bot_uttered")
async def get_response_t(data=None):

    print("THIS IS THE DATA inside socket_43", data)
    socket_list_43 = list(socket_43.keys())

    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_43[0] == conversation_reference.user.id:
            # print("THIS SI CONVERSATION REFERENCE ::::: ",conversation_reference.conversation)
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )  

@ario.on("bot_uttered")
async def get_response_t(data=None):

    print("THIS IS THE DATA inside socket_44", data)
    socket_list_44 = list(socket_44.keys())

    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_44[0] == conversation_reference.user.id:
            # print("THIS SI CONVERSATION REFERENCE ::::: ",conversation_reference.conversation)
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )  

@asio.on("bot_uttered")
async def get_response_s(data=None):
    global activity_id
    # hert=activity_id.copy()
    # activity_id=[]
    print("THIS IS THE DATA inside socket_45", data)
    socket_list_45 = list(socket_45.keys())
    # while socket_list_1:
    # print("ACTIVITY ID INSIDE WHILE ," ,activity_id)
        # if not activity_id :
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        # print("THIS IS CONVERSATION REF INSIDE 1 and id is :::: ", conversation_reference.user.id, 'and ::::: ', socket_list_1[0])
        if socket_list_45[0] == conversation_reference.user.id:
            print("INSIDE 1 bruv")
            # print("THIS SI CONVERSATION REFERENCE ::::: ",conversation_reference.conversation)
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )
    # try:
    #     del socket_in_use[socket_list_1[0]]
    #     print("THIS IS UPDATED SOCKET_IN_USE ", socket_in_use)
    # except: 
    #     print("ALREADY DELETED")
    # print("\n****************\n",hert)
    # print('RESPONSE FROM RASA ', data)
    # for active_id in hert:
    #     for conversation_reference in st.CONVERSATION_REFERENCES.values():
    #             if active_id == conversation_reference.activity_id:
    #                 print("THIS SI CONVERSATION REFERENCE ::::: ",conversation_reference.conversation)
    #                 await ADAPTER.continue_conversation(
    #                     conversation_reference,
    #                     lambda turn_context: turn_context.send_activity(data['text']),
    #                     APP_ID,
    #                 )
    #     # hert.remove(active_id)
    #     print(activity_id,"****")
    #     if activity_id:
    #         activity_id.pop(0)           
    # activity_id = []

@atio.on("bot_uttered")
async def get_response_t(data=None):


    print("THIS IS THE DATA inside socket_46", data)
    socket_list_46 = list(socket_46.keys())

    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_46[0] == conversation_reference.user.id:
            # print("THIS SI CONVERSATION REFERENCE ::::: ",conversation_reference.conversation)
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )     

@auio.on("bot_uttered")
async def get_response_u(data=None):

    print("THIS IS THE DATA inside socket_47", data)
    socket_list_47 = list(socket_47.keys())
    # while socket_list_3:
            # print("ACTIVITY ID INSIDE WHILE ," ,activity_id)
        # if not activity_id :
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_47[0] == conversation_reference.user.id:
            # print("THIS SI CONVERSATION REFERENCE ::::: ",conversation_reference.conversation)
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )

@avio.on("bot_uttered")
async def get_response_v(data=None):

    print("THIS IS THE DATA inside socket_48", data)
    socket_list_48 = list(socket_48.keys())
    # w?hile socket_list_4:
        #   print("ACTIVITY ID INSIDE WHILE ," ,activity_id)
        # if not activity_id :
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_48[0] == conversation_reference.user.id:
            # print("THIS SI CONVERSATION REFERENCE ::::: ",conversation_reference.conversation)
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            ) 

@awio.on("bot_uttered")
async def get_response_w(data=None):


    print("THIS IS THE DATA inside socket_49", data)
    socket_list_49 = list(socket_49.keys())
    # print("ACTIVITY ID INSIDE WHILE ," ,activity_id)
    # if not activity_id :
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_49[0] == conversation_reference.user.id:
            # print("THIS SI CONVERSATION REFERENCE ::::: ",conversation_reference.conversation)
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )    

@axio.on("bot_uttered")
async def get_response_t(data=None):

    print("THIS IS THE DATA inside socket_50", data)
    socket_list_50 = list(socket_50.keys())
    # while socket_list_2:
    # print("ACTIVITY ID INSIDE WHILE ," ,activity_id)
        # if not activity_id :
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_50[0] == conversation_reference.user.id:
            # print("THIS SI CONVERSATION REFERENCE ::::: ",conversation_reference.conversation)
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )  

@ayio.on("bot_uttered")
async def get_response_t(data=None):

    print("THIS IS THE DATA inside socket_51", data)
    socket_list_51 = list(socket_51.keys())
    # while socket_list_2:
    # print("ACTIVITY ID INSIDE WHILE ," ,activity_id)
        # if not activity_id :
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_51[0] == conversation_reference.user.id:
            # print("THIS SI CONVERSATION REFERENCE ::::: ",conversation_reference.conversation)
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )  

@azio.on("bot_uttered")
async def get_response_t(data=None):

    print("THIS IS THE DATA inside socket_52", data)
    socket_list_52 = list(socket_52.keys())
    # while socket_list_2:
    # print("ACTIVITY ID INSIDE WHILE ," ,activity_id)
        # if not activity_id :
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_52[0] == conversation_reference.user.id:
            # print("THIS SI CONVERSATION REFERENCE ::::: ",conversation_reference.conversation)
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )  

#-----b
@baio.on("bot_uttered")
async def get_response_t(data=None):
    print("THIS IS THE DATA inside socket_53", data)
    socket_list_53 = list(socket_53.keys())
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_53[0] == conversation_reference.user.id:
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )  

    

@bbio.on("bot_uttered")
async def get_response_t(data=None):
    print("THIS IS THE DATA inside socket_54", data)
    socket_list_54 = list(socket_54.keys())
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_54[0] == conversation_reference.user.id:
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )  



@bcio.on("bot_uttered")
async def get_response_t(data=None):
    print("THIS IS THE DATA inside socket_55", data)
    socket_list_55 = list(socket_55.keys())
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_55[0] == conversation_reference.user.id:
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )



@bdio.on("bot_uttered")
async def get_response_t(data=None):
    print("THIS IS THE DATA inside socket_56", data)
    socket_list_56 = list(socket_56.keys())
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_56[0] == conversation_reference.user.id:
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )



@beio.on("bot_uttered")
async def get_response_t(data=None):
    print("THIS IS THE DATA inside socket_57", data)
    socket_list_57 = list(socket_57.keys())
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_57[0] == conversation_reference.user.id:
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )



@bfio.on("bot_uttered")
async def get_response_t(data=None):
    print("THIS IS THE DATA inside socket_58", data)
    socket_list_58 = list(socket_58.keys())
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_58[0] == conversation_reference.user.id:
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )



@bgio.on("bot_uttered")
async def get_response_t(data=None):
    print("THIS IS THE DATA inside socket_59", data)
    socket_list_59 = list(socket_59.keys())
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_59[0] == conversation_reference.user.id:
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )



@bhio.on("bot_uttered")
async def get_response_t(data=None):
    print("THIS IS THE DATA inside socket_60", data)
    socket_list_60 = list(socket_60.keys())
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_60[0] == conversation_reference.user.id:
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )



@biio.on("bot_uttered")
async def get_response_t(data=None):
    print("THIS IS THE DATA inside socket_61", data)
    socket_list_61 = list(socket_61.keys())
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_61[0] == conversation_reference.user.id:
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )



@bjio.on("bot_uttered")
async def get_response_t(data=None):
    print("THIS IS THE DATA inside socket_62", data)
    socket_list_62 = list(socket_62.keys())
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_62[0] == conversation_reference.user.id:
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )



@bkio.on("bot_uttered")
async def get_response_t(data=None):
    print("THIS IS THE DATA inside socket_63", data)
    socket_list_63 = list(socket_63.keys())
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_63[0] == conversation_reference.user.id:
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )



@blio.on("bot_uttered")
async def get_response_t(data=None):
    print("THIS IS THE DATA inside socket_64", data)
    socket_list_64 = list(socket_64.keys())
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_64[0] == conversation_reference.user.id:
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )



@bmio.on("bot_uttered")
async def get_response_t(data=None):
    print("THIS IS THE DATA inside socket_65", data)
    socket_list_65 = list(socket_65.keys())
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_65[0] == conversation_reference.user.id:
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )



@bnio.on("bot_uttered")
async def get_response_t(data=None):
    print("THIS IS THE DATA inside socket_66", data)
    socket_list_66 = list(socket_66.keys())
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_66[0] == conversation_reference.user.id:
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )



@boio.on("bot_uttered")
async def get_response_t(data=None):
    print("THIS IS THE DATA inside socket_67", data)
    socket_list_67 = list(socket_67.keys())
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_67[0] == conversation_reference.user.id:
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )



@bpio.on("bot_uttered")
async def get_response_t(data=None):
    print("THIS IS THE DATA inside socket_68", data)
    socket_list_68 = list(socket_68.keys())
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_68[0] == conversation_reference.user.id:
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )



@bqio.on("bot_uttered")
async def get_response_t(data=None):
    print("THIS IS THE DATA inside socket_69", data)
    socket_list_69 = list(socket_69.keys())
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_69[0] == conversation_reference.user.id:
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )



@brio.on("bot_uttered")
async def get_response_t(data=None):
    print("THIS IS THE DATA inside socket_70", data)
    socket_list_70 = list(socket_70.keys())
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_70[0] == conversation_reference.user.id:
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )



@bsio.on("bot_uttered")
async def get_response_t(data=None):
    print("THIS IS THE DATA inside socket_71", data)
    socket_list_71 = list(socket_71.keys())
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_71[0] == conversation_reference.user.id:
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )



@btio.on("bot_uttered")
async def get_response_t(data=None):
    print("THIS IS THE DATA inside socket_72", data)
    socket_list_72 = list(socket_72.keys())
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_72[0] == conversation_reference.user.id:
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )



@buio.on("bot_uttered")
async def get_response_t(data=None):
    print("THIS IS THE DATA inside socket_73", data)
    socket_list_73 = list(socket_73.keys())
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_73[0] == conversation_reference.user.id:
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )



@bvio.on("bot_uttered")
async def get_response_t(data=None):
    print("THIS IS THE DATA inside socket_74", data)
    socket_list_74 = list(socket_74.keys())
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_74[0] == conversation_reference.user.id:
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )



@bwio.on("bot_uttered")
async def get_response_t(data=None):
    print("THIS IS THE DATA inside socket_75", data)
    socket_list_75 = list(socket_75.keys())
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_75[0] == conversation_reference.user.id:
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )



@bxio.on("bot_uttered")
async def get_response_t(data=None):
    print("THIS IS THE DATA inside socket_76", data)
    socket_list_76 = list(socket_76.keys())
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_76[0] == conversation_reference.user.id:
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )



@byio.on("bot_uttered")
async def get_response_t(data=None):
    print("THIS IS THE DATA inside socket_77", data)
    socket_list_77 = list(socket_77.keys())
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_77[0] == conversation_reference.user.id:
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )



@bzio.on("bot_uttered")
async def get_response_t(data=None):
    print("THIS IS THE DATA inside socket_78", data)
    socket_list_78 = list(socket_78.keys())
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_78[0] == conversation_reference.user.id:
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )
#----c

@caio.on("bot_uttered")
async def get_response_t(data=None):
    print("THIS IS THE DATA inside socket_79", data)
    socket_list_79 = list(socket_79.keys())
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_79[0] == conversation_reference.user.id:
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )  

    

@cbio.on("bot_uttered")
async def get_response_t(data=None):
    print("THIS IS THE DATA inside socket_80", data)
    socket_list_80 = list(socket_80.keys())
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_80[0] == conversation_reference.user.id:
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )  

    

@ccio.on("bot_uttered")
async def get_response_t(data=None):
    print("THIS IS THE DATA inside socket_81", data)
    socket_list_81 = list(socket_81.keys())
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_81[0] == conversation_reference.user.id:
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )



@cdio.on("bot_uttered")
async def get_response_t(data=None):
    print("THIS IS THE DATA inside socket_82", data)
    socket_list_82 = list(socket_82.keys())
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_82[0] == conversation_reference.user.id:
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )



@ceio.on("bot_uttered")
async def get_response_t(data=None):
    print("THIS IS THE DATA inside socket_83", data)
    socket_list_83 = list(socket_83.keys())
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_83[0] == conversation_reference.user.id:
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )



@cfio.on("bot_uttered")
async def get_response_t(data=None):
    print("THIS IS THE DATA inside socket_84", data)
    socket_list_84 = list(socket_84.keys())
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_84[0] == conversation_reference.user.id:
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )



@cgio.on("bot_uttered")
async def get_response_t(data=None):
    print("THIS IS THE DATA inside socket_85", data)
    socket_list_85 = list(socket_85.keys())
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_85[0] == conversation_reference.user.id:
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )



@chio.on("bot_uttered")
async def get_response_t(data=None):
    print("THIS IS THE DATA inside socket_86", data)
    socket_list_86 = list(socket_86.keys())
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_86[0] == conversation_reference.user.id:
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )



@ciio.on("bot_uttered")
async def get_response_t(data=None):
    print("THIS IS THE DATA inside socket_87", data)
    socket_list_87 = list(socket_87.keys())
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_87[0] == conversation_reference.user.id:
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )



@cjio.on("bot_uttered")
async def get_response_t(data=None):
    print("THIS IS THE DATA inside socket_88", data)
    socket_list_88 = list(socket_88.keys())
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_88[0] == conversation_reference.user.id:
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )



@ckio.on("bot_uttered")
async def get_response_t(data=None):
    print("THIS IS THE DATA inside socket_89", data)
    socket_list_89 = list(socket_89.keys())
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_89[0] == conversation_reference.user.id:
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )



@clio.on("bot_uttered")
async def get_response_t(data=None):
    print("THIS IS THE DATA inside socket_90", data)
    socket_list_90 = list(socket_90.keys())
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_90[0] == conversation_reference.user.id:
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )



@cmio.on("bot_uttered")
async def get_response_t(data=None):
    print("THIS IS THE DATA inside socket_91", data)
    socket_list_91 = list(socket_91.keys())
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_91[0] == conversation_reference.user.id:
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )



@cnio.on("bot_uttered")
async def get_response_t(data=None):
    print("THIS IS THE DATA inside socket_92", data)
    socket_list_92 = list(socket_92.keys())
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_92[0] == conversation_reference.user.id:
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )



@coio.on("bot_uttered")
async def get_response_t(data=None):
    print("THIS IS THE DATA inside socket_93", data)
    socket_list_93 = list(socket_93.keys())
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_93[0] == conversation_reference.user.id:
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )



@cpio.on("bot_uttered")
async def get_response_t(data=None):
    print("THIS IS THE DATA inside socket_94", data)
    socket_list_94 = list(socket_94.keys())
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_94[0] == conversation_reference.user.id:
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )



@cqio.on("bot_uttered")
async def get_response_t(data=None):
    print("THIS IS THE DATA inside socket_95", data)
    socket_list_95 = list(socket_95.keys())
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_95[0] == conversation_reference.user.id:
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )



@crio.on("bot_uttered")
async def get_response_t(data=None):
    print("THIS IS THE DATA inside socket_96", data)
    socket_list_96 = list(socket_96.keys())
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_96[0] == conversation_reference.user.id:
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )



@csio.on("bot_uttered")
async def get_response_t(data=None):
    print("THIS IS THE DATA inside socket_97", data)
    socket_list_97 = list(socket_97.keys())
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_97[0] == conversation_reference.user.id:
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )



@ctio.on("bot_uttered")
async def get_response_t(data=None):
    print("THIS IS THE DATA inside socket_98", data)
    socket_list_98 = list(socket_98.keys())
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_98[0] == conversation_reference.user.id:
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )



@cuio.on("bot_uttered")
async def get_response_t(data=None):
    print("THIS IS THE DATA inside socket_99", data)
    socket_list_99 = list(socket_99.keys())
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_99[0] == conversation_reference.user.id:
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )



@cvio.on("bot_uttered")
async def get_response_t(data=None):
    print("THIS IS THE DATA inside socket_100", data)
    socket_list_100 = list(socket_100.keys())
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_100[0] == conversation_reference.user.id:
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )



@cwio.on("bot_uttered")
async def get_response_t(data=None):
    print("THIS IS THE DATA inside socket_101", data)
    socket_list_101 = list(socket_101.keys())
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_101[0] == conversation_reference.user.id:
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )



@cxio.on("bot_uttered")
async def get_response_t(data=None):
    print("THIS IS THE DATA inside socket_102", data)
    socket_list_102 = list(socket_102.keys())
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_102[0] == conversation_reference.user.id:
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )



@cyio.on("bot_uttered")
async def get_response_t(data=None):
    print("THIS IS THE DATA inside socket_103", data)
    socket_list_103 = list(socket_103.keys())
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_103[0] == conversation_reference.user.id:
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )



@czio.on("bot_uttered")
async def get_response_t(data=None):
    print("THIS IS THE DATA inside socket_104", data)
    socket_list_104 = list(socket_104.keys())
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_104[0] == conversation_reference.user.id:
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )  

#----d

@daio.on("bot_uttered")
async def get_response_t(data=None):
    print("THIS IS THE DATA inside socket_105", data)
    socket_list_105 = list(socket_105.keys())
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_105[0] == conversation_reference.user.id:
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )



@dbio.on("bot_uttered")
async def get_response_t(data=None):
    print("THIS IS THE DATA inside socket_106", data)
    socket_list_106 = list(socket_106.keys())
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_106[0] == conversation_reference.user.id:
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )



@dcio.on("bot_uttered")
async def get_response_t(data=None):
    print("THIS IS THE DATA inside socket_107", data)
    socket_list_107 = list(socket_107.keys())
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_107[0] == conversation_reference.user.id:
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )



@ddio.on("bot_uttered")
async def get_response_t(data=None):
    print("THIS IS THE DATA inside socket_108", data)
    socket_list_108 = list(socket_108.keys())
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_108[0] == conversation_reference.user.id:
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )



@deio.on("bot_uttered")
async def get_response_t(data=None):
    print("THIS IS THE DATA inside socket_109", data)
    socket_list_109 = list(socket_109.keys())
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_109[0] == conversation_reference.user.id:
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )



@dfio.on("bot_uttered")
async def get_response_t(data=None):
    print("THIS IS THE DATA inside socket_110", data)
    socket_list_110 = list(socket_110.keys())
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_110[0] == conversation_reference.user.id:
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )



@dgio.on("bot_uttered")
async def get_response_t(data=None):
    print("THIS IS THE DATA inside socket_111", data)
    socket_list_111 = list(socket_111.keys())
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_111[0] == conversation_reference.user.id:
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )



@dhio.on("bot_uttered")
async def get_response_t(data=None):
    print("THIS IS THE DATA inside socket_112", data)
    socket_list_112 = list(socket_112.keys())
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_112[0] == conversation_reference.user.id:
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )



@diio.on("bot_uttered")
async def get_response_t(data=None):
    print("THIS IS THE DATA inside socket_113", data)
    socket_list_113 = list(socket_113.keys())
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_113[0] == conversation_reference.user.id:
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )



@djio.on("bot_uttered")
async def get_response_t(data=None):
    print("THIS IS THE DATA inside socket_114", data)
    socket_list_114 = list(socket_114.keys())
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_114[0] == conversation_reference.user.id:
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )



@dkio.on("bot_uttered")
async def get_response_t(data=None):
    print("THIS IS THE DATA inside socket_115", data)
    socket_list_115 = list(socket_115.keys())
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_115[0] == conversation_reference.user.id:
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )



@dlio.on("bot_uttered")
async def get_response_t(data=None):
    print("THIS IS THE DATA inside socket_116", data)
    socket_list_116 = list(socket_116.keys())
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_116[0] == conversation_reference.user.id:
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )



@dmio.on("bot_uttered")
async def get_response_t(data=None):
    print("THIS IS THE DATA inside socket_117", data)
    socket_list_117 = list(socket_117.keys())
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_117[0] == conversation_reference.user.id:
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )



@dnio.on("bot_uttered")
async def get_response_t(data=None):
    print("THIS IS THE DATA inside socket_118", data)
    socket_list_118 = list(socket_118.keys())
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_118[0] == conversation_reference.user.id:
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )



@doio.on("bot_uttered")
async def get_response_t(data=None):
    print("THIS IS THE DATA inside socket_119", data)
    socket_list_119 = list(socket_119.keys())
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_119[0] == conversation_reference.user.id:
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )



@dpio.on("bot_uttered")
async def get_response_t(data=None):
    print("THIS IS THE DATA inside socket_120", data)
    socket_list_120 = list(socket_120.keys())
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_120[0] == conversation_reference.user.id:
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )



@dqio.on("bot_uttered")
async def get_response_t(data=None):
    print("THIS IS THE DATA inside socket_121", data)
    socket_list_121 = list(socket_121.keys())
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_121[0] == conversation_reference.user.id:
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )



@drio.on("bot_uttered")
async def get_response_t(data=None):
    print("THIS IS THE DATA inside socket_122", data)
    socket_list_122 = list(socket_122.keys())
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_122[0] == conversation_reference.user.id:
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )



@dsio.on("bot_uttered")
async def get_response_t(data=None):
    print("THIS IS THE DATA inside socket_123", data)
    socket_list_123 = list(socket_123.keys())
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_123[0] == conversation_reference.user.id:
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )



@dtio.on("bot_uttered")
async def get_response_t(data=None):
    print("THIS IS THE DATA inside socket_124", data)
    socket_list_124 = list(socket_124.keys())
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_124[0] == conversation_reference.user.id:
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )



@duio.on("bot_uttered")
async def get_response_t(data=None):
    print("THIS IS THE DATA inside socket_125", data)
    socket_list_125 = list(socket_125.keys())
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_125[0] == conversation_reference.user.id:
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )



@dvio.on("bot_uttered")
async def get_response_t(data=None):
    print("THIS IS THE DATA inside socket_126", data)
    socket_list_126 = list(socket_126.keys())
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_126[0] == conversation_reference.user.id:
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )



@dwio.on("bot_uttered")
async def get_response_t(data=None):
    print("THIS IS THE DATA inside socket_127", data)
    socket_list_127 = list(socket_127.keys())
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_127[0] == conversation_reference.user.id:
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )



@dxio.on("bot_uttered")
async def get_response_t(data=None):
    print("THIS IS THE DATA inside socket_128", data)
    socket_list_128 = list(socket_128.keys())
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_128[0] == conversation_reference.user.id:
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )



@dyio.on("bot_uttered")
async def get_response_t(data=None):
    print("THIS IS THE DATA inside socket_129", data)
    socket_list_129 = list(socket_129.keys())
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_129[0] == conversation_reference.user.id:
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )



@dzio.on("bot_uttered")
async def get_response_t(data=None):
    print("THIS IS THE DATA inside socket_130", data)
    socket_list_130 = list(socket_130.keys())
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_130[0] == conversation_reference.user.id:
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )  

#----e

@eaio.on("bot_uttered")
async def get_response_t(data=None):
    print("THIS IS THE DATA inside socket_131", data)
    socket_list_131 = list(socket_131.keys())
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_131[0] == conversation_reference.user.id:
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )



@ebio.on("bot_uttered")
async def get_response_t(data=None):
    print("THIS IS THE DATA inside socket_132", data)
    socket_list_132 = list(socket_132.keys())
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_132[0] == conversation_reference.user.id:
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )



@ecio.on("bot_uttered")
async def get_response_t(data=None):
    print("THIS IS THE DATA inside socket_133", data)
    socket_list_133 = list(socket_133.keys())
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_133[0] == conversation_reference.user.id:
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )



@edio.on("bot_uttered")
async def get_response_t(data=None):
    print("THIS IS THE DATA inside socket_134", data)
    socket_list_134 = list(socket_134.keys())
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_134[0] == conversation_reference.user.id:
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )



@eeio.on("bot_uttered")
async def get_response_t(data=None):
    print("THIS IS THE DATA inside socket_135", data)
    socket_list_135 = list(socket_135.keys())
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_135[0] == conversation_reference.user.id:
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )



@efio.on("bot_uttered")
async def get_response_t(data=None):
    print("THIS IS THE DATA inside socket_136", data)
    socket_list_136 = list(socket_136.keys())
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_136[0] == conversation_reference.user.id:
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )



@egio.on("bot_uttered")
async def get_response_t(data=None):
    print("THIS IS THE DATA inside socket_137", data)
    socket_list_137 = list(socket_137.keys())
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_137[0] == conversation_reference.user.id:
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )



@ehio.on("bot_uttered")
async def get_response_t(data=None):
    print("THIS IS THE DATA inside socket_138", data)
    socket_list_138 = list(socket_138.keys())
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_138[0] == conversation_reference.user.id:
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )



@eiio.on("bot_uttered")
async def get_response_t(data=None):
    print("THIS IS THE DATA inside socket_139", data)
    socket_list_139 = list(socket_139.keys())
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_139[0] == conversation_reference.user.id:
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )



@ejio.on("bot_uttered")
async def get_response_t(data=None):
    print("THIS IS THE DATA inside socket_140", data)
    socket_list_140 = list(socket_140.keys())
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_140[0] == conversation_reference.user.id:
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )



@ekio.on("bot_uttered")
async def get_response_t(data=None):
    print("THIS IS THE DATA inside socket_141", data)
    socket_list_141 = list(socket_141.keys())
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_141[0] == conversation_reference.user.id:
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )



@elio.on("bot_uttered")
async def get_response_t(data=None):
    print("THIS IS THE DATA inside socket_142", data)
    socket_list_142 = list(socket_142.keys())
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_142[0] == conversation_reference.user.id:
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )



@emio.on("bot_uttered")
async def get_response_t(data=None):
    print("THIS IS THE DATA inside socket_143", data)
    socket_list_143 = list(socket_143.keys())
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_143[0] == conversation_reference.user.id:
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )



@enio.on("bot_uttered")
async def get_response_t(data=None):
    print("THIS IS THE DATA inside socket_144", data)
    socket_list_144 = list(socket_144.keys())
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_144[0] == conversation_reference.user.id:
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )



@eoio.on("bot_uttered")
async def get_response_t(data=None):
    print("THIS IS THE DATA inside socket_145", data)
    socket_list_145 = list(socket_145.keys())
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_145[0] == conversation_reference.user.id:
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )



@epio.on("bot_uttered")
async def get_response_t(data=None):
    print("THIS IS THE DATA inside socket_146", data)
    socket_list_146 = list(socket_146.keys())
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_146[0] == conversation_reference.user.id:
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )



@eqio.on("bot_uttered")
async def get_response_t(data=None):
    print("THIS IS THE DATA inside socket_147", data)
    socket_list_147 = list(socket_147.keys())
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_147[0] == conversation_reference.user.id:
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )



@erio.on("bot_uttered")
async def get_response_t(data=None):
    print("THIS IS THE DATA inside socket_148", data)
    socket_list_148 = list(socket_148.keys())
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_148[0] == conversation_reference.user.id:
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )



@esio.on("bot_uttered")
async def get_response_t(data=None):
    print("THIS IS THE DATA inside socket_149", data)
    socket_list_149 = list(socket_149.keys())
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_149[0] == conversation_reference.user.id:
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )



@etio.on("bot_uttered")
async def get_response_t(data=None):
    print("THIS IS THE DATA inside socket_150", data)
    socket_list_150 = list(socket_150.keys())
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_150[0] == conversation_reference.user.id:
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )



@euio.on("bot_uttered")
async def get_response_t(data=None):
    print("THIS IS THE DATA inside socket_151", data)
    socket_list_151 = list(socket_151.keys())
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_151[0] == conversation_reference.user.id:
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )



@evio.on("bot_uttered")
async def get_response_t(data=None):
    print("THIS IS THE DATA inside socket_152", data)
    socket_list_152 = list(socket_152.keys())
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_152[0] == conversation_reference.user.id:
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )



@ewio.on("bot_uttered")
async def get_response_t(data=None):
    print("THIS IS THE DATA inside socket_153", data)
    socket_list_153 = list(socket_153.keys())
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_153[0] == conversation_reference.user.id:
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )



@exio.on("bot_uttered")
async def get_response_t(data=None):
    print("THIS IS THE DATA inside socket_154", data)
    socket_list_154 = list(socket_154.keys())
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_154[0] == conversation_reference.user.id:
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )



@eyio.on("bot_uttered")
async def get_response_t(data=None):
    print("THIS IS THE DATA inside socket_155", data)
    socket_list_155 = list(socket_155.keys())
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_155[0] == conversation_reference.user.id:
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )



@ezio.on("bot_uttered")
async def get_response_t(data=None):
    print("THIS IS THE DATA inside socket_156", data)
    socket_list_156 = list(socket_156.keys())
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        if socket_list_156[0] == conversation_reference.user.id:
            await ADAPTER.continue_conversation(
                conversation_reference,
                lambda turn_context: turn_context.send_activity(data['text']),
                APP_ID,
            )  

async def _send_proactive_message():
    f = open("/app/Botframework_V1/pro_message.txt", "r")
    message = f.read()
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        print("THIS SI CONVERSATION REFERENCE ::::: ",conversation_reference.conversation)
        await ADAPTER.continue_conversation(
            conversation_reference,
            lambda turn_context: turn_context.send_activity(message),
            APP_ID,
        )

def save_con_ref(req: Response) -> Response:
    print("Saving data")
    try:
        with open('conversation_ref.pickle','wb') as f:
            pickle.dump(st.CONVERSATION_REFERENCES, f, protocol=pickle.HIGHEST_PROTOCOL)
            print("Done saving conversation references")
            return Response(status=HTTPStatus.OK, text = "Conversation References have been saved")
    except Exception as e:
        print("Pickle could not be saved ", e)
        return Response(status=HTTPStatus.OK, text = "Conversation References could not be saved")

def num_users(req: Response) -> Response:
    print("Printing num users")
    i = 0 
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        i = i + 1
    return Response(status=HTTPStatus.OK, text = f"Number of users is {i}")
    
def user_list(req: Response) -> Response:
    print("Generating List")
    f = ''
    for conversation_reference in st.CONVERSATION_REFERENCES.values():
        f = f+conversation_reference.user.name+"\n"
    with open("user_list.txt",'w') as file:
        file.write(f)
    return Response(status=HTTPStatus.OK, text = "Done")

APP = web.Application(middlewares=[aiohttp_error_middleware])
APP.router.add_post("/api/messages", messages)
APP.router.add_get("/api/notify", notify)
APP.router.add_get("/api/references", save_con_ref)
APP.router.add_get("/api/num_users",num_users)
APP.router.add_get("/api/user_list",user_list)


#signal.signal(signal.SIGINT, save_con_ref)


if __name__ == "__main__":
    #try:
    #    with open('conversation_ref.pickle', 'rb') as f:
    #        st.CONVERSATION_REFERENCES = pickle.load(f)
    #        print("CONVERSATION LOADED")
    #except Exception as e:
    #    print("Error loading pickle ", e)
    try:
        web.run_app(APP, host="192.168.100.5", port=CONFIG.PORT)
    except Exception as error:
        raise error
