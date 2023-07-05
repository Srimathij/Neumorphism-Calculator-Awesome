# import requests

# url = "http://localhost:5005/conversations/007ceb2d640c40919fc20cbb1c4fecf0/trigger_intent?output_channel=latest"
# payload = {"name": "greet"}
# headers = {}
# res = requests.post(url, data=payload, headers=headers)

# import requests
# import schedule
# import time
# import psycopg2
# import json




# def condb():
#     check = []
#     conn = psycopg2.connect(dbname="Divabot", user="postgres", password="kgisl123", host="127.0.0.1", port="5432")
#     cursor = conn.cursor()
#     query = "SELECT conversation_id, name FROM diva_test"
#     cursor.execute(query)
#     dataacq = cursor.fetchall()
#     print(dataacq)
#     for count, data in enumerate(dataacq):
#         if data[1] != None:
#             check.append(True)
#         else:
#             check.append(False)
#     print(check)
#     print(dataacq)
#     #print(result)
#     cursor.close()
#     conn.close()
#     return dataacq, check


# def runeveryday9am():
#     result, check = condb()
#     for i, data in enumerate(result):
#         print(data)
#         print("cid: ", data[0])
#         print("data: ", data[1])
#         tre = True
#         fle = False
#         headers = {}
#         if data[1] != None:
#             print("This is 1")
#                 # Already added when you pass json= but not when you pass data=
#                 # 'Content-Type': 'application/json',
#             params = {'output_channel': 'latest',}

#             json_data = {
#                 'name': '9am_name',
#                 'entities': {'morning': "True", 'name': data[1], 'check': "True"}}
#             response = requests.post('http://localhost:5005/conversations/'+data[0]+'/trigger_intent', headers=headers, params=params, json=json_data)
#             print("done1")
#         elif data[1] == None:
#             print("This is 2")
#             # Already added when you pass json= but not when you pass data=
#             # 'Content-Type': 'application/json',
#             params = {'output_channel': 'latest',}

#             json_data = {
#                 'name': '9am_name'}
#             response = requests.post('http://localhost:5005/conversations/'+data[0]+'/trigger_intent', headers=headers, params=params, json=json_data)
#             print("done2")

# def runeveryday6pm():
#     result, check  = condb()
#     for i, data in enumerate(result):       

#         url = "http://localhost:5005/conversations/"+data[0]+"/trigger_intent?output_channel=latest"

#         payload = json.dumps({
#             "name": "9am_name",
#             "entities": {
#                 "morning": "True",
#                 "name": data[1],
#                 "check": "True"
#             }
#             })
#         headers = {
#             'Content-Type': 'application/json'
#         }

#         response = requests.request("POST", url, headers=headers, data=payload)

#         print(response.text)

# def printresult(result):
#    print(result)

#########################################CHECK THIS BOTTOM CODE FOR MAKING FASTER API CALLS 
# https://stackoverflow.com/questions/63166887/how-can-you-speed-up-repeated-api-calls
# # pip install cachetools diskcache
# from cachetools import cached
# from diskcache import Cache

# BASE_URL = "https://ai.chemistryinthecloud.com/smilies/"
# CACHEDIR = "api_cache"

# @cached(cache=Cache(CACHEDIR))
# def get_similies(value):
#     return requests.get(BASE_URL + value).json()


# def parse_eq(eq):
#     reac, _, reag = (set(v.split(".")) for v in eq.partition(">"))
#     return {
#         "reactants": {i: get_similies(i) for i in reac},
#         "reagents": {i: get_similies(i) for i in reag}
#     }

# result = [parse_eq(eq) for eq in eqs]
# schedule.every().day.at("13:16").do(condb)
# print ("schedule",schedule.every().day.at("13:17").do(condb))
# a,b = condb()
# schedule.every().day.at("11:03").do(printresult, dataacq)
# result = condb()
# for i in result:
#    print(i[0])
# a,b = condb()
# print(a,b)
# print(check)
# runeveryday6pm()
# import psycopg2
# try:
#    conn = psycopg2.connect(dbname="Divabot", user="postgres", password="kgisl123", host="127.0.0.1", port="5432")
#    cursor = conn.cursor()
#    #print(cursor)
#    query = "SELECT EXISTS(SELECT conversation_id FROM diva_test WHERE conversation_id = '969c77f5ab8d43e09d39ee8f34073d21')"
#    cursor.execute(query)
#    result = cursor.fetchall()
#    print(result[0][0])
#    print("done")
#    conn.commit()
#    cursor.close()
# except (Exception, psycopg2.DatabaseError) as error:
#    print(error)
# finally:
#    conn.close()
#    print("Database closed")
# schedule.every().day.at("09:00").do(runeveryday9am)
# schedule.every().day.at("18:00").do(runeveryday6pm)

#everyday(result)
#while True:
#    # Checks whether a scheduled task 
#    # is pending to run or not
#    schedule.run_pending()
#    time.sleep(1)


# import asyncio 
# import logging
# from re import A
# import websockets
# from websockets import WebSocketServerProtocol

# logging.basicConfig(level=logging.INFO)

# class Server:
#     clients = set()

#     async def register(self, ws: WebSocketServerProtocol) -> None:
#         self.clients.add(ws)
#         logging.info(f'{ws.remote_address} connects.')

#     async def unregister(self, ws: WebSocketServerProtocol) -> None:
#         self.clients.remove(ws)
#         logging.info(f'{ws.remote_address} disconncets.')

#     async def send_to_clients(self, message: str) -> None:
#         if self.clients:
#             await asyncio.wait([client.send(message) for client in self.clients])

#     async def ws_handler(self, ws: WebSocketServerProtocol, url: str) -> None:
#         await self.register(ws)
#         try:
#             await self.distribute(ws)
#         finally:
#             await self.unregister(ws)

#     async def distribute(self, ws: WebSocketServerProtocol) -> None:
#         async for message in ws:
#             await self.send_to_clients(message)

# server = Server()
# start_server = websockets.serve(server.ws_handler, 'localhost', 4000)
# loop =asyncio.get_event_loop()
# loop.run_until_complete(start_server)
# loop.run_forever()
# from tkinter import X
# import psycopg2

# candidate_id = '102345'

# conn = psycopg2.connect(dbname = "OnBoarding", user='postgres', password="kgisl123", host = "localhost", port ="5432")
# cursor = conn.cursor()
# query = 'SELECT "Candidate_id", "Name", "Number", "Email" from "onboarding"'
# cursor.execute(query)
# results = cursor.fetchall()
# res = [list(y) for y in results]
# result = [x for xs in res for x in xs]
# print("THIS IS ",result)
# print(type(result[0]))
# print(type(int(candidate_id)))
# print(type(result))
# if int(candidate_id) in result:
#     index = result.index(int(candidate_id))
#     print(result[index+2])
#     print("hello")
#     #return {'name':result[index+1]}
# import socketio
# q = {}
# a = socketio.AsyncClient()
# q['as'] = a
# print(q['as'], a)
# a = 5
# print(q['as'], a)
# import socketio 

# sio = socketio.Client()
# # sio.connect('http://localhost:5004/socket.io')
# import asyncio
# global a, i
# a = [1,2,3,4]
# i = 0
# async def run():  
#     global a, i
#     while i <=20:
#         a.append(i)
#         # asyncio.sleep(5)
#         i = i+1
#         print("THIs is a ",a)
#         await asyncio.sleep(2)

# async def runnn():
#     global a
#     while a:
#         print(a[0], a)
#         a.pop(0)
#         await asyncio.sleep(7)

# async def message():
#     for i in range(10):
#         print(i)
#         await run()
#         await asyncio.sleep(1)

# loop = asyncio.get_event_loop()
# loop.create_task(run())
# loop.create_task(runnn())
# # loop.run_until_complete(message())
# loop.run_forever()
# import asyncio
# import threading

# async def msg(text):
#     await asyncio.sleep(0.1)
#     print(text)

# async def cut():
#     print("this is a seperate process")
#     await msg("hiiiii")

# async def long_operation():
#     print('long_operation started')
#     await asyncio.sleep(3)
#     print('long_operation finished')

# def f(f_stop):
#     print("Hello WOrld")
#     if not f_stop.is_set():
#         # call f() again in 60 seconds
#         threading.Timer(2, f, [f_stop]).start()

# f_stop = threading.Event()
# # start calling f now and every 60 sec thereafter
# f(f_stop)
# async def main():
#     await msg('first')

#     # Now you want to start long_operation, but you don't want to wait it finised:
#     # long_operation should be started, but second msg should be printed immediately.
#     # Create task to do so:
#     task = asyncio.ensure_future(long_operation())

#     await msg('second')

#     # Now, when you want, you can await task finised:
#     await cut()
#     await task
#     await msg("hello")

# async def msg2(text):
#     m = 0
#     while m<=10:
#         m = m+1
#     print(text, m)

# async def cut2():
#     print("this is a seperate process2")
#     await msg2("hiiiii2")

# async def long_operation2():
#     print('long_operation started2')
#     await asyncio.sleep(10)
#     print('long_operation finished2') 


# if __name__ == "__main__":
#     loop = asyncio.get_event_loop()
#     loop2 = asyncio.get_event_loop()
#     loop.run_until_complete(main())
#     loop2.run_until_complete(cut2())


# a = {'1':'1','2':'2'}

# a[list(a.keys())[0]] = '456'

# print(a[list(a.keys())[0]])

# import time

# a = time.time()

# time.sleep(5)

# b = time.time()

# print(time.time()-a)


# import socketio
# hola0 = socketio.AsyncClient()
# hola1 = socketio.AsyncClient()
# hola2 = socketio.AsyncClient()
# hola3 = socketio.AsyncClient()
# hola4 = socketio.AsyncClient()
# hola5 = socketio.AsyncClient()
# hola6 = socketio.AsyncClient()
# hola7 = socketio.AsyncClient()
# hola8 = socketio.AsyncClient()
# hola9 = socketio.AsyncClient()

# def dyanmicFuncs(activity_id_sio):
#     exec('''
# @'''+activity_id_sio+'''.on("bot_uttered")
# async def as_send_proactive_message(data=None):
#     print("HELLLOO")
#     print("THIS IS THE DATA in chacha ", data, ksio.sid)
#     for conversation_reference in CONVERSATION_REFERENCES.values():
#         print("THIS SI CONVERSATION REFERENCE ::::: ",conversation_reference.user)
#         await ADAPTER.continue_conversation(
#             conversation_reference,
#             lambda turn_context: turn_context.send_activity(data['text']),
#             APP_ID,
#         )
#         @'''+activity_id_sio+'''.event
#         def connect():
#             print("Im connected")
#         @'''+activity_id_sio+'''.event
#         def connect_error(data):
#             print("The connection failed!")
#         @'''+activity_id_sio+'''.event
#         def disconnect():
#             print("Im disconnected")'''
#         , globals())

# for i in range(10):
#     dyanmicFuncs("hola"+str(i))
#     print("THIS IS ", i)

# as_send_proactive_message()

# as

# from multiprocessing import Process
# import time

# def func1():
#   print ('func1: starting')
#   for i in range(100):
#         time.sleep(10)
#         print("True1")
#   print ('func1: finishing')

# def func2():
#   print ('func2: starting')
#   for i in range(10):
#         time.sleep(2) 
#         print("True2")
#   print ('func2: finishing')

# if __name__ == '__main__':
#   p1 = Process(target=func1)
#   p1.start()
#   p2 = Process(target=func2)
#   p2.start()
#   p1.join()
#   p2.join()


# listlist = [1,2,3,4,5]
# inuse = [1,2,3,5,4]

# if free = list(sorted(set(listlist) - set(inuse))):
#     print('haha')
# def socket_1(id):
#     print(id)

# def socket_2(id):
#     print(id, '2')


# for i in [1,2]:
#     exec('socket_'+str(i)+'("dasdasd")')

# global i 
# i = 1
# def on1():
#     if i == 1:
#         print('qqq')
#         on2()
#     else: 
#         print('sss')

# def on2():
#     global i
#     i = 2
#     print('rrr')
#     on1()

# on1()




# import socketio
# import time

# sio = socketio.Client()

# print("ALUGHT ")
# sio.connect('http://localhost:5005/socket.io')

# @sio.event
# def connect():
#     print("Im connected")

# @sio.event
# def connect_error(data):
#     print("The connection failed!")

# @sio.event
# def disconnect():
#     print("Im disconnected")


# def check():
#     print("Im inside")
#     time.sleep(10)
#     sio.disconnect()
#     sio.connect('http://localhost:5005/socket.io')

# check()


# listtt = [5,4,3,2,1,0]

# listtt.remove(5)
# print(listtt)


# class MyClassss:
#     def __str__(self):
#         return type(self).__name__

# SecondClass = MyClassss

# instance = SecondClass()
# print(instance)
# import socketio
# import time

# sio = socketio.Client()
# def con():
#     sio.connect('http://localhost:5005/socketio')

# @sio.event
# def connect():
#     print("Im connected")

# @sio.event
# def connect_error(data):
#     print("The connection failed!")

# @sio.event
# def disconnect():
#     print("Im disconnected")


# def send_message():
#     sio.emit('session_request', {'session_id':'abcdefghijkljaksd'})
#     sio.emit('user_uttered',{'session_id':'abcdefghijkljaksd',
#                                 'message' : 'Hey',
#                                 'metadata': {'name':'Sahil'}
#                             })

# def send_message1():
#     # sio.emit('session_request', {'session_id':'abcdefghijkljaksd'})
#     sio.emit('user_uttered',{'session_id':'abcdefghijkljaksd',
#                                 'message' : 'great',
#                                 'metadata':{}
                            # })

# @sio.on('bot_uttered')
# def response(data):
#     print("THIS IS DATA ", data)

# con()
# send_message()
# time.sleep(15)
# send_message1()


# import requests
# import json

# url = "https://mtalentx.kgisl.com/talentx/web/api/get-emp-information?security_token=b4a2591f4dec919fa3954523bf35a8c9&ad_account=muthukumaran.g&category=TAX Details"

# payload={}
# headers = {}

# response = requests.request("GET", url, headers=headers, data=payload)
# res = json.loads(response.text)
# # print(res)
# if res['message'] == 'Records Found':
#     print("Tax Regime : "+str(res['response'][0]['Tax Regime'])+
#          "\nTax Applicable : "+str(res['response'][0]['Tax Applicable']))
#          "\nPF Applicable : "+str(res['response'][0]['PF Applicable'])+
#          "\nUAN Number : "+str(res['response'][0]['UAN Number']))
#          "\nProject : "+str(res['response'][0]['Project'])+
#          "\nsub Project : "+str(res['response'][0]['sub Project'])+
#          "\nSub Division : "+str(res['response'][0]['Sub Division']))
#          "\nPermanent Phone : "+str(res['response'][0]['Permanent Phone'])+
#          "\nCurrent Address : "+str(res['response'][0]['Current Address'])+
#          "\nCurrent City : "+str(res['response'][0]['Current City'])+
#          "\nCUrrent State : "+str(res['response'][0]['Current State'])+
#          "\nCurrent Pincode : "+str(res['response'][0]['Current Pincode'])+
#          "\nCurrent Phone : "+str(res['response'][0]['Current Phone'])+
#          "\nVaccination Status : "+str(res['response'][0]['Vaccination Status'])+
#          "\nBlood Group : "+str(res['response'][0]['Blood Group'])+
#          "\nHobbies : "+str(res['response'][0]['Hobbies'])+
#          "\nT Shirt Size : "+str(res['response'][0]['T Shirt Size'])+
#          "\nHoodie Size : "+str(res['response'][0]['Hoodie Size'])+
#          "\nOffice Ext No : "+str(res['response'][0]['Office Ext No']))
     
# else:
#     dispatcher.utter_message(text = "Shhhh its okay, we're sure you did some certification you must have just fOrgOTteN to give it to us. ")
# for data in json.loads(response.text)['response']:
#     print("Insurance name - "+data['Insurance Name']+
#                                         "Relationship - "+str(data['Relationship'])+
#                                         "\nGender -"+str(data['Gender'])+
#                                         "]nInsuranced No -"+str(data['Insurance Ecard No'])+
#                                         "\nSum Insured -"+str(data['Sum Insured'])+
#                                         "\nDate of Commencement -"+str(data['Date of Commencement'])+
#                                         "\nInsurance Details -"+str(data['Insurance Details']))
# print(type(json.loads(response.text)))
# import requests
# import json

# url = "https://mtalentx.kgisl.com/talentx/web/api/get-emp-information?security_token=b4a2591f4dec919fa3954523bf35a8c9&ad_account=sahil.k&category=Probationary Details"

# payload={}
# headers = {}

# response = requests.request("GET", url, headers=headers, data=payload)
# res = json.loads(response.text)
# # print(res)
# if res['message'] == 'Records Found':
#     print("Confirmation Period : "+str(res['response'][0]['Confirmation Period'])+"   "+
#          "\nProbation Confirmation : "+str(res['response'][0]['Probation Confirmation'])+"   "+
#          "\nDate of Confirmation : "+str(res['response'][0]['Date of Confirmation']))
# k = "sahil"
# k = k.capitalize()
# print(k)
# a = []
# for i in range(1,157):
#     a.append(i)
# print(a)

# a = {}
# k = 97
# for i in range(0,26):
#     a[i+1] = chr(k+i)
# print(a)

# i = str(98)

# a = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j', 11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z'}

# for i in range(131,157):
#     print("""            
#     async def socket_use_"""+str(i)+"""(self,user_id):
#         global sio
#         if socket_"""+str(i)+""" and time.time() -  socket_"""+str(i)+"""[list(socket_52.keys())[0]] > 180: 
#             del socket_in_use[list(socket_"""+str(i)+""".keys())[0]]
#             socket_in_use_list.remove("""+str(i)+""")
#             socket_"""+str(i)+""".clear()
#             await self.empty_sock_check(user_id)
#             await e"""+a[i-130]+"""io.disconnect()
#             await asyncio.sleep(0.1)
#             await e"""+a[i-130]+"""io.connect('http://localhost:5005/socket.io')
#         else: 
#             pass   
#     """)


# for i in range(53,157):
#     print("""       print("THIS IS SOCKET_"""+str(i)+""" ", socket_"""+str(i)+""")""")


# import requests
# import json

# name = "sahil.k"
# url = "https://mtalentx.kgisl.com/talentx/web/api/leave-balance-details?security_token=b4a2591f4dec919fa3954523bf35a8c9&username="+name

# payload={'security_token': 'b4a2591f4dec919fa3954523bf35a8c9',
# 'username': name}
# files=[

# ]
# headers = {}
# response = requests.request("GET", url, headers=headers, data=payload, files=files)
# # response = json.loads(response.text)
# # for i in response['response']:
# #     for j in i:
# #         print(j['LeaveDescription'])
# # res = json.loads(response.text[0])
# res = '{"s'.join(response.text.split('{"s', 2)[:2])
# res = json.loads(res)
# # print(res['response'])
# for i in res['response']:
#     print(i['LeaveDescription'],i['LeaveDays'])
# res = json.loads(json.dumps(response.text))
# re = json.loads(res)
# print(re)





# import pickle 

# class MyClass():
#     def __init__(self,param):
#         self.param = param


# def save_object(obj):
#     try: 
#         with open('data.pickle', 'wb') as f:
#             pickle.dump(obj, f, protocol=pickle.HIGHEST_PROTOCOL)
#     except Exception as ex:
#         print(ex)

# def load_object(filename):
#     try: 
#         with open(filename, 'rb') as f:
#             return pickle.load(f)
#     except Exception as ex:
#         print("Error during unplicking object ", ex)


# obj = MyClass(10)
# save_object(obj)

# import smtplib
# # obj = load_object('data.pickle')

# # print(obj.param)
# # print(isinstance(obj, MyClass))

# toaddrs = ['chandrasekhar.m@kgisl.com', "ramya.v@kgisl.com"]

#     #toaddrs = ["yogita.shyam@kgisl.com","naveenkanna.t@kgisl.com","prashanth.s@kgisl.com"]

# fromaddr = 'diva@kgisl.com'
# random_no = '123123'
# description = 'Laptop overheating'

# message_subject = "Raising tickets "
# message_text = "Ticket No:# %s\r\n" % random_no +"Description: %s\r\n" % description + "\n Respective team will get back to you soon to rectify you're problem" + "\n Thanks"+ "\n Diva - kgisl"
# message = "From: %s\r\n" % fromaddr+ "To: %s\r\n" % ",".join(toaddrs)+ "Subject: %s\r\n" % message_subject+ "\r\n" + message_text
# s = smtplib.SMTP('smtp.office365.com', 587)
# s.ehlo()
# s.starttls()
# s.login('diva@kgisl.com','Welcome@12345')
# s.set_debuglevel(1)
# # s.sendmail('diva@kgisl.com', 'chandrasekhar.m@kgisl.com', message)
# # s.quit()


# # print('\033[1mHello')

# import smtplib
# from email.mime.text import MIMEText

# def mail(frm_user,description, random_no):
#     frm_addr='diva@kgisl.com'

#     #cc = ['murshid.vp@kgisl.com','selvakumar.k@kgisl.com']
#     toaddrs = ['chandrasekhar.m@kgisl.com']
#     #toaddrs = ["yogita.shyam@kgisl.com","naveenkanna.t@kgisl.com","prashanth.s@kgisl.com"]

#     message_subject = "Raising tickets"
#     mesg = """\
# 	  <html>
# 		<head></head>
# 	  <body>
# 		<p>Ticket Number: <b>"""+str(random_no)+"""</b></p><br>
# 		<p>Employee Email ID: <b>"""+str(frm_user)+"""</b></p><br>
# 		<p><b>Description</b>: """+str(description)+"""</b><br><br><br>
# 		<p>Respective team will get back to you soon to rectify you're problem</p>
# 		<p>Regards</p>
# 		<p>DIVA - KGiSL</p>
		
# 	  </body>



# 	</html>
# 	"""
#     message_text = message_text.attach(MIMEText(mesg, "html"))
#     #message_text = "Ticket No:# %s\r\n" % random_no +"Employee Email ID: %s\r\n" % frm_user+ "\n\nDescription: %s\r\n" % description + "\n\nRespective team will get back to you soon to rectify you're problem" + "\nThanks"+ "\nDiva - kgisl"
#     #message = "From: %s\r\n" % frm_addr+ "To: %s\r\n" % ",".join(toaddrs)+ "Subject: %s\r\n" % message_subject+ "\r\n" + message_text
#     s = smtplib.SMTP('smtp.office365.com', 587)
#     s.ehlo()
#     s.starttls()
#     s.login('diva@kgisl.com','Welcome@12345')
#     s.set_debuglevel(1)
#     s.sendmail('diva@kgisl.com','chandrasekhar.m@kgisl.com', message_text.as_string())
#     s.quit() 
 
# import json
# import requests


# name='yogita.shyam'
# url = "https://mtalentx.kgisl.com/talentx/web/api/get-emp-information?security_token=b4a2591f4dec919fa3954523bf35a8c9&ad_account="+name+"&category=Family Details"

# payload={}
# headers = {}

# response = requests.request("GET", url, headers=headers, data=payload)
# res = json.loads(response.text)
#                 # print(res)
# if res['message'] == 'Records Found':
#     for data in res['response']:
#         print("First Name : "+str(data['First Name'])+"   "+
#                              "\nDate of Wedding : "+str(data['Date of Wedding'])+"   "+
#                              "\nDate of Birth : "+str(data['Date of Birth'])+"   "+
#                              "\nRelationship : "+str(data['Relationship'])+"   "+
#                              "\nMarital Status : "+str(data['Marital Status']))

import pickle
import signal
import time

class Myclass():
    def __init__(self, x):
        self.x = x+1
        print(self.x,x)
    
    def add(self):
        y = self.x+self.x
        print(y)

def save_object(signum, frame):
    print('done1')
    try:
        with open('data.pickle','wb') as f:
            pickle.dump(one, f, protocol= pickle.HIGHEST_PROTOCOL)
            print("Done")
            exit(1)
    except Exception as e:
        print("ERROR ", e)
        # exit(1)

def load_object(filename):
    try:
        with open(filename, 'rb') as f:
            return pickle.load(f)
    except Exception as e:
        print("ERror ", e)

def hello(signum, frame):
    print('hello')
        
obj = Myclass(8)
obh = Myclass(10)
ojk = Myclass(15)
nnn = Myclass(925)
global one 
one = []
one = [obj,obh, ojk, nnn]

signal.signal(signal.SIGINT, save_object)

count = 0
while True: 
    print(f"{count}", end='\r', flush= True )
    count = count+1
    time.sleep(0.5)
onn = load_object('data.pickle')

# for i in onn:
#     print(isinstance(i, Myclass), i.x)
# print(isinstance(onn, Myclass))
