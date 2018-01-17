# -*- coding: utf-8 -*-
import linepy
from linepy import *
from bs4 import BeautifulSoup
import json, time, random, tempfile, os, sys, codecs, threading, glob, urllib, urllib3,re ,ast , subprocess, requests, pytz
from gtts import gTTS
from googletrans import Translator

#client = LineClient()
client = LineClient(id='yogafermozza@gmail.com', passwd='smokers69')
#client = LineClient(authToken='AUTHTOKEN')
client.log("Auth Token : " + str(client.authToken))

channel = LineChannel(client)
client.log("Channel Access Token : " + str(channel.channelAccessToken))
#id='pinksweetblack@gmail.com', passwd='asukabeh69'
#client = LineClient()
#client2 = LineClient(id='yogafermozza@gmail.com', passwd='smokers69')
#client = LineClient(authToken='AUTHTOKEN')
#client2.log("Auth Token : " + str(client.authToken))

#channel = LineChannel(client)
#client.log("Channel Access Token : " + str(channel.channelAccessToken))

helpMessage ="""「Command me」

「Mention me」
「Mid」
「Mybio」
「Mypicture」
「Myvideoprofile」
「My cover」
「Gn 「Your text」」
「Unsend 「Your text」」
「Copy 「@」」
「backup」
「Announce」
「Getsquare」
「Checkmid 「_MID_」」
「Friendlist」
「Blocklist」
「Lc 「@」」
「Getcontact 「@」」
「Sticker:」
「Yt: 「Your text」」
「Image:」
「Sytr:」
「Tr:」
「Speed」
「Spic 「@」」
「Scover 「@」」
「Tagall」
「Clear」
「Cancel」
「Readstart」
「readfinish」
「Lurking on」
「Lurking off」
「Lurking reset」
「Lurking」
「Ulti 「@@@@」」
「Stag 「@」」
「Mayhem」
「Mode:self」
「Restart」
「Up 「on/off」「num」「Your Text」」
「Listgroup」
「Getmid 「@」」
「Gcreator」"""

clientProfile = client.getProfile()
clientSettings = client.getSettings()
poll = LinePoll(client)
clientMID = client.profile.mid



contact = client.getProfile()
backup = client.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus
#==============================================================================#
settings = {
    "lang":"JP",
    "leaveRoom":True,
    "autoAdd":False,
    "autoJoin":True,
}
read = {
    "readPoint":{},
    "readMember":{},
    "readTime":{},
    "ROM":{},
}
mode='self'
cctv={
    "cyduk":{},
    "point":{},
    "sidermem":{}
}
myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}
myProfile2 = {
	"displayName2": "",
	"statusMessage2": "",
	"pictureStatus2": ""
}
wait2 = {
    'setTime':{},
}

setTime = {}
setTime = wait2['setTime']
mulai = time.time()


myProfile["displayName"] = clientProfile.displayName
myProfile["statusMessage"] = clientProfile.statusMessage
myProfile["pictureStatus"] = clientProfile.pictureStatus

#==============================================================================#
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def RECEIVE_MESSAGE(op):
    '''
        This is sample for implement BOT in LINE group
        Invite your BOT to group, then BOT will auto accept your invitation
        Command availabe :
        > hi
        > /author
    '''
    msg = op.message
    
    text = msg.text
    msg_id = msg.id
    receiver = msg.to
    sender = msg._from

def mention(to, nama):
    aa = ""
    bb = ""
    strt = int(0)
    akh = int(0)
    nm = nama
    myid = client.getProfile().mid
    if myid in nm:    
        nm.remove(myid)
    for mm in nm:
        akh = akh + 6
        aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
        strt = strt + 7
        akh = akh + 1
        bb += "@nrik \n"
        aa = (aa[:int(len(aa)-1)])
        text = bb
    try:
        client.sendMessage(to, text, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        print(error)

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    return '「 %02d нσυяѕ %02d мιиυтє %02d ѕє¢σи∂」' % (hours, mins, secs)

def NOTIFIED_INVITE_INTO_GROUP(op):
    try:
        group_id=op.param1
        # Accept group invitation
        client.acceptGroupInvitation(group_id)
    except Exception as e:
        client.log("[NOTIFIED_INVITE_INTO_GROUP] ERROR : " + str(e))

# Add function to poll
poll.addOpInterruptWithDict({
    OpType.RECEIVE_MESSAGE: RECEIVE_MESSAGE,
    OpType.NOTIFIED_INVITE_INTO_GROUP: NOTIFIED_INVITE_INTO_GROUP
})

#===================================================================================#

while True:
    try:
        ops=poll.singleTrace(count=50)
        if ops != None:
          for op in ops:

#=========================================================================================================================================#
            #if op.type in OpType._VALUES_TO_NAMES:
            #    print("[ {} ] {}".format(str(op.type), str(OpType._VALUES_TO_NAMES[op.type])))
#=========================================================================================================================================#
            if op.type == 5:
                print ("AUTO ADD MESSAGE CLIENT")
                if settings["autoAdd"] == True: 
                    client.findAndAddContactsByMid(op.param1)
                    xname = client.getContact(op.param1).displayName
                    client.sendMessage(op.param1, xname + " ,тнαикѕ fσя α∂∂є∂ мє")
                    
 #           if op.type == 5:
  #              print ("AUTO ADD MESSAGE CLIENT2")
   #             if settings["autoAdd"] == True: 
    #                client2.findAndAddContactsByMid(op.param1)
     #               xname = client2.getContact(op.param1).displayName
      #              client2.sendMessage(op.param1, xname + " ,тнαикѕ fσя α∂∂є∂ мє")
                    
            if op.type == 13:
                print ("[NOTIFIED_INVITE_INTO_GROUP] CLIENT")
                if clientMID in op.param3:
                    G = client.getGroup(op.param1)
                    if settings["autoJoin"] == True:
                        client.acceptGroupInvitation(op.param1)
                    else:
                        pass

#            if op.type == 13:
#                print ("[NOTIFIED_INVITE_INTO_GROUP] CLIENT2")
#                if clientMID in op.param3:
#                    G = client2.getGroup(op.param1)
#                    if settings["autoJoin"] == True:
#                        client2.acceptGroupInvitation(op.param1)
#                    else:
#                        pass
            if op.type == 26:
                msg = op.message
                if msg.text != None:
                    if msg.toType == 2:
                        may = client.getProfile().mid
                        if may in str(msg.contentMetadata) and 'MENTION' in str(msg.contentMetadata):
                            pilih = ['「αυтσ яєѕρσиѕє тαg」\n¢αи ι нєℓρ уσυ?']
                            rslt = random.choice(pilih)
                            client.sendText(msg.to, str(rslt))
                        else:
                            pass
                    else:
                        pass
                else:
                    pass

            if op.type == 17:
                ginfo = client.getGroup(op.param1)
                contact = client.getContact(op.param2)
                #image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                #client.sendImageWithURL(op.param1,image)
                client.sendText(op.param1, client.getContact(op.param2).displayName +"\nωєℓ¢σмє тσ"+"\n>>"+ str(ginfo.name) +"<<")

            if op.type == 25:
                msg = op.message


                if msg.toType == 1:
                    if settings["leaveRoom"] == True:
                        client.leaveRoom(msg.to)

            if op.type == 25:
                msg = op.message
                text = msg.text
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                try:
                    if msg.contentType == 0:
                        if msg.toType == 2:
                            client.sendChatChecked(receiver, msg_id)
                            contact = client.getContact(sender)
                            if text.lower() == 'mention me':
                                client.sendMessage(receiver, None, contentMetadata={'mid': sender}, contentType=13)
                                client.sendText(receiver, '「Auto respon tag」')
                                client.tag(receiver, sender)
                                print ("[COMMAND] MENTION ME")
                            if text.lower() == 'tag @fery':
                                client.tag(receiver, sender)
                                client.tag(receiver, sender)
                                client.tag(receiver, sender)
                                client.tag(receiver, sender)
                                client.tag(receiver, sender)
                                client.tag(receiver, sender)
                                client.tag(receiver, sender)
                                client.tag(receiver, sender)
                                client.tag(receiver, sender)
                                client.tag(receiver, sender)
                            elif text.lower() == 'mid':
                                client.sendMessage(msg.to,"「My mid」\n" +  clientMID)
                                print ("[COMMAND] MID")
                            elif text.lower() == 'myname':
                                me = client.getContact(clientMID)
                                client.sendMessage(msg.to,"「Display my name」\n" + me.displayName)
                                print ("[COMMAND] DISPLAY NAME")
                            elif text.lower() == 'mybio':
                                me = client.getContact(clientMID)
                                client.sendMessage(msg.to,"「Status」\n" + me.statusMessage)
                                print ("[COMMAND] MY BIO")
                            elif text.lower() == 'mypicture':
                                me = client.getContact(clientMID)
                                client.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus)
                                print ("[COMMAND] MY PICTURE")
                            elif text.lower() == 'myvideoprofile':
                                me = client.getContact(clientMID)
                                client.sendVideoWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus + "/vp")
                            elif text.lower() == 'mycover':
                                me = client.getContact(clientMID)
                                cover = channel.getProfileCoverURL(clientMID)    
                                client.sendImageWithURL(msg.to, cover)
                                print ("[COMMAND] MY COVER")
                            elif ("Gn " in msg.text):
                                 X = client.getGroup(msg.to)
                                 X.name = msg.text.replace("Gn ","")
                                 client.updateGroup(X)
                                 print ("[COMMAND] GNAME")
                            elif ("Unsend " in msg.text):
                                 k = msg.text.replace("Unsend ","")
                                 client.unsendMessage(msg_id)
                            elif "copy" in msg.text.lower():
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    for mention in mentionees:
                                        contact = mention["M"]
                                        break
                                    try:
                                        client.cloneContactProfile(contact)
                                        client.sendMessage(msg.to, "「Clone sucses」")
                                    except:
                                        client.sendMessage(msg.to, "「Clone failed」")
                                        print ("[COMMAND] COPY OK")
                            elif text.lower() == 'backup':
                                try:
                                    clientProfile.displayName = str(myProfile["displayName"])
                                    clientProfile.statusMessage = str(myProfile["statusMessage"])
                                    clientProfile.pictureStatus = str(myProfile["pictureStatus"])
                                    client.updateProfileAttribute(8, clientProfile.pictureStatus)
                                    client.updateProfile(clientProfile)
                                    client.sendMessage(msg.to, "「Backup my profile sucses」")
                                except:
                                    client.sendMessage(msg.to, "「Backup my profile failed」")
                                    print ("[COMMAND] BACKUP OK")
                            elif text.lower() == 'announce':
                                gett = client.getChatRoomAnnouncements(receiver)
                                for a in gett:
                                    aa = client.getContact(a.creatorMid).displayName
                                    bb = a.contents
                                    cc = bb.link
                                    textt = bb.text
                                    client.sendText(receiver, '「Link」: ' + str(cc) + '\n「Text」: ' + str(textt) + '\n「Maker」: ' + str(aa))
                            elif text.lower() == 'ngentot':
                                client.unsendMessage(msg_id)
                                print ("UNSEND MESSAGE")
                            elif text.lower() == 'getsquare':
                                a = client.getJoinedSquares()
                                squares = a.squares
                                members = a.members
                                authorities = a.authorities
                                statuses = a.statuses
                                noteStatuses = a.noteStatuses
                                txt = str(squares)+'\n\n'+str(members)+'\n\n'+str(authorities)+'\n\n'+str(statuses)+'\n\n'+str(noteStatuses)+'\n\n'
                                txt2 = ''
                                for i in range(len(squares)):
                                    txt2 += str(i+1)+'. '+str(squares[i].invitationURL)+'\n'
                                client.sendText(receiver, txt2)
                                print ("[COMMAND] GET ALL SQUARE OK")
                            elif "checkmid" in msg.text.lower():
                                separate = msg.text.split(" ")
                                saya = msg.text.replace(separate[0] + " ","")
                                client.sendMessage(receiver, None, contentMetadata={'mid': saya}, contentType=13)
                                print ("[Command] checkmid ok")
                                
                            elif text.lower() == 'friendlist':
                                contactlist = client.getAllContactIds()
                                kontak = client.getContacts(contactlist)
                                num=1
                                msgs="═════════「Friendlist」═════════"
                                for ids in kontak:
                                    msgs+="\n[%i] %s" % (num, ids.displayName)
                                    num=(num+1)
                                msgs+="\n═════════「Friendlist」═════════\n\nтσтαℓ : %i" % len(kontak)
                                client.sendMessage(msg.to, msgs)
                                print ("List friend ok")
                                
                            elif text.lower() == 'blocklist':
                                blockedlist = client.getBlockedContactIds()
                                kontak = client.getContacts(blockedlist)
                                num=1
                                msgs="═════════「Block listfriend」═════════"
                                for ids in kontak:
                                    msgs+="\n[%i] %s" % (num, ids.displayName)
                                    num=(num+1)
                                msgs+="\n═════════「Block listfriend」═════════\n\n「Total」 : %i" % len(kontak)
                                client.sendMessage(msg.to, msgs)
                                print ("list blocked ok")
                            elif 'lc ' in text.lower():
                                try:
                                    typel = [1001,1002,1003,1004,1005,1006]
                                    key = eval(msg.contentMetadata["MENTION"])
                                    u = key["MENTIONEES"][0]["M"]
                                    a = client.getContact(u).mid
                                    s = client.getContact(u).displayName
                                    hasil = channel.getHomeProfile(mid=a)
                                    st = hasil['result']['feeds']
                                    for i in range(len(st)):
                                        test = st[i]
                                        result = test['post']['postInfo']['postId']
                                        channel.like(str(sender), str(result), likeType=random.choice(typel))
                                        channel.comment(str(sender), str(result), '「This auto like worked」')
                                    client.sendText(receiver, '「Already for like」'+str(len(st))+' 「Post from」' + str(s))
                                except Exception as e:
                                    client.sendText(receiver, str(e))
                            elif 'getcontact ' in text.lower():
                                try:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    u = key["MENTIONEES"][0]["M"]
                                    cname = client.getContact(u).displayName
                                    cmid = client.getContact(u).mid
                                    cstatus = client.getContact(u).statusMessage
                                    cpic = client.getContact(u).picturePath
                                    #print(str(a))
                                    client.sendText(receiver, '「Name」 : '+cname+'\n「Mid」 : '+cmid+'\n「Status」 : '+cstatus+'\n「Picture」 : http://dl.profile.line.naver.jp'+cpic)
                                    client.sendMessage(receiver, None, contentMetadata={'mid': cmid}, contentType=13)
                                    if "videoProfile='{" in str(client.getContact(u)):
                                        client.sendVideoWithURL(receiver, 'http://dl.profile.line.naver.jp'+cpic+'/vp.small')
                                    else:
                                        client.sendImageWithURL(receiver, 'http://dl.profile.line.naver.jp'+cpic)
                                except Exception as e:
                                    client.sendText(receiver, str(e))
                            elif 'sticker:' in msg.text.lower():
                                try:
                                    query = msg.text.replace("sticker:", "")
                                    query = int(query)
                                    if type(query) == int:
                                        client.sendImageWithURL(receiver, 'https://stickershop.line-scdn.net/stickershop/v1/product/'+str(query)+'/ANDROID/main.png')
                                        client.sendText(receiver, 'https://line.me/S/sticker/'+str(query))
                                    else:
                                        client.sendText(receiver, '「Use a key, not number」')
                                except Exception as e:
                                    client.sendText(receiver, str(e))
                            elif "yt:" in msg.text.lower():
                                try:
                                    query = msg.text.replace("yt:", "")
                                    query = query.replace(" ", "+")
                                    x = client.youtube(query)
                                    client.sendText(receiver, x)
                                except Exception as e:
                                    client.sendText(receiver, str(e))
                            elif "image:" in msg.text.lower():
                                try:
                                    query = msg.text.replace("image:", "")
                                    images = client.image_search(query)
                                    client.sendImageWithURL(receiver, images)
                                except Exception as e:
                                    client.sendText(receiver, str(e))

                            elif 'apakah ' in msg.text.lower():
                                try:
                                    txt = ['iya','tidak','bisa jadi']
                                    isi = random.choice(txt)
                                    tts = gTTS(text=isi, lang='id', slow=False)
                                    tts.save('temp2.mp3')
                                    client.sendAudio(receiver, 'temp2.mp3')
                                except Exception as e:
                                    client.sendText(receiver, str(e))
                            elif "sytr:" in msg.text:
                                try:
                                    isi = msg.text.split(":")
                                    translator = Translator()
                                    hasil = translator.translate(isi[2], dest=isi[1])
                                    A = hasil.text
                                    tts = gTTS(text=A, lang=isi[1], slow=False)
                                    tts.save('temp3.mp3')
                                    client.sendAudio(receiver, 'temp3.mp3')
                                except Exception as e:
                                    client.sendText(receiver, str(e))
                            elif "tr:" in msg.text:
                                try:
                                    isi = msg.text.split(":")
                                    translator = Translator()
                                    hasil = translator.translate(isi[2], dest=isi[1])
                                    A = hasil.text                               
                                    client.sendText(receiver, str(A))
                                except Exception as e:
                                    client.sendText(receiver, str(e))
                            elif text.lower() == 'speed':
                                start = time.time()
                                client.sendText(receiver, "「Speed testing」")
                                elapsed_time = time.time() - start
                                client.sendText(receiver, "「Speed fasting」\n「%sSeconds」" % (elapsed_time))
                            elif text.lower() == 'sp':
                                start = time.time()
                                client.sendText(receiver, "「Speed testing」")
                                elapsed_time = time.time() - start
                                client.sendText(receiver, "「Speed fasting」\n「%sSeconds」" % (elapsed_time))
                            elif 'spic' in text.lower():
                                try:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    u = key["MENTIONEES"][0]["M"]
                                    a = client.getContact(u).pictureStatus
                                    if "videoProfile='{" in str(client.getContact(u)):
                                        client.sendVideoWithURL(receiver, 'http://dl.profile.line.naver.jp/'+a+'/vp.small')
                                    else:
                                        client.sendImageWithURL(receiver, 'http://dl.profile.line.naver.jp/'+a)
                                except Exception as e:
                                    client.sendText(receiver, str(e))
                            elif 'scover' in text.lower():
                                try:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    u = key["MENTIONEES"][0]["M"]
                                    a = channel.getProfileCoverURL(mid=u)
                                    client.sendImageWithURL(receiver, a)
                                except Exception as e:
                                    client.sendText(receiver, str(e))
                            elif text.lower() == 'tagall':
                                group = client.getGroup(receiver)
                                nama = [contact.mid for contact in group.members]
                                nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                                if jml <= 100:
                                    client.mention(receiver, nama)
                                if jml > 100 and jml < 200:
                                    for i in range(0, 100):
                                        nm1 += [nama[i]]
                                    client.mention(receiver, nm1)
                                    for j in range(101, len(nama)):
                                        nm2 += [nama[j]]
                                    client.mention(receiver, nm2)
                                if jml > 200 and jml < 300:
                                    for i in range(0, 100):
                                        nm1 += [nama[i]]
                                    client.mention(receiver, nm1)
                                    for j in range(101, 200):
                                        nm2 += [nama[j]]
                                    client.mention(receiver, nm2)
                                    for k in range(201, len(nama)):
                                        nm3 += [nama[k]]
                                    client.mention(receiver, nm3)
                                if jml > 300 and jml < 400:
                                    for i in range(0, 100):
                                        nm1 += [nama[i]]
                                    client.mention(receiver, nm1)
                                    for j in range(101, 200):
                                        nm2 += [nama[j]]
                                    client.mention(receiver, nm2)
                                    for k in range(201, len(nama)):
                                        nm3 += [nama[k]]
                                    client.mention(receiver, nm3)
                                    for l in range(301, len(nama)):
                                        nm4 += [nama[l]]
                                    client.mention(receiver, nm4)
                                if jml > 400 and jml < 501:
                                    for i in range(0, 100):
                                        nm1 += [nama[i]]
                                    client.mention(receiver, nm1)
                                    for j in range(101, 200):
                                        nm2 += [nama[j]]
                                    client.mention(receiver, nm2)
                                    for k in range(201, len(nama)):
                                        nm3 += [nama[k]]
                                    client.mention(receiver, nm3)
                                    for l in range(301, len(nama)):
                                        nm4 += [nama[l]]
                                    client.mention(receiver, nm4)
                                    for m in range(401, len(nama)):
                                        nm5 += [nama[m]]
                                    client.mention(receiver, nm5)             
                                client.sendText(receiver, "「Total list member」="+str(jml))

#============================================================#cancel#=========================================================#
                            elif text.lower() == 'cancel':
                                if msg.toType == 2:
                                    X = client.getGroup(msg.to)
                                    if X.invitee is not None:
                                        gInviMids = [contact.mid for contact in X.invitee]
                                        client.cancelGroupInvitation(msg.to, gInviMids)
                                        
                            elif msg.text in ["Clear"]:
                                if msg.toType == 2:
                                    group = client.getGroup(msg.to)
                                    gMembMids = [contact.mid for contact in group.invitee]
                                    for _mid in gMembMids:
                                        client.cancelGroupInvitation(msg.to,[_mid])
                                    client.sendText(msg.to,"「Sorry nobody absen」")
#==============================================================================================================================#
                            elif text.lower() == 'gurl':
                                if msg.toType == 2:
                                    x = client.getGroup(msg.to)
                                    if x.preventJoinByTicket == True:
                                        x.preventJoinByTicket = False
                                        client.updateGroup(x)
                                    gurl = client.reissueGroupTicket(msg.to)
                                    client.sendText(msg.to,"line://ti/g/" + gurl)
#============================================================#READ#=========================================================#
                            elif text.lower() == 'readstart':
                                try:
                                    del cctv['point'][receiver]
                                    del cctv['sidermem'][receiver]
                                    del cctv['cyduk'][receiver]
                                except:
                                    pass
                                cctv['point'][receiver] = msg.id
                                cctv['sidermem'][receiver] = ""
                                cctv['cyduk'][receiver]=True
                            elif text.lower() == 'readfinish':
                                if msg.to in cctv['point']:
                                    cctv['cyduk'][receiver]=False
                                    client.sendText(receiver, '====ALL JUST READ====\n\n'+cctv['sidermem'][msg.to])
                                else:
                                    client.sendText(receiver, "「Set first」")
                            elif text.lower() == 'lurking on':
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                if msg.to in read['readPoint']:
                                        try:
                                            del read['readPoint'][msg.to]
                                            del read['readMember'][msg.to]
                                            del read['readTime'][msg.to]
                                        except:
                                            pass
                                        read['readPoint'][msg.to] = msg.id
                                        read['readMember'][msg.to] = ""
                                        read['readTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                                        read['ROM'][msg.to] = {}
                                        with open('sider.json', 'w') as fp:
                                            json.dump(read, fp, sort_keys=True, indent=4)
                                            client.sendMessage(msg.to,"「LURKING ACTIVE」")
                                else:
                                    try:
                                        del read['readPoint'][msg.to]
                                        del read['readMember'][msg.to]
                                        del read['readTime'][msg.to]
                                    except:
                                        pass
                                    read['readPoint'][msg.to] = msg.id
                                    read['readMember'][msg.to] = ""
                                    read['readTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                                    read['ROM'][msg.to] = {}
                                    with open('sider.json', 'w') as fp:
                                        json.dump(read, fp, sort_keys=True, indent=4)
                                        client.sendMessage(msg.to, "「SET READING POINT」:\n" + readTime)
                                        
                            elif text.lower() == 'lurking off':
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                if msg.to not in read['readPoint']:
                                    client.sendMessage(msg.to,"「LURKING OFF」")
                                else:
                                    try:
                                            del read['readPoint'][msg.to]
                                            del read['readMember'][msg.to]
                                            del read['readTime'][msg.to]
                                    except:
                                          pass
                                    client.sendMessage(msg.to, "「∂єℓєтє яєα∂ιиg ρσιит」:\n" + readTime)
                
                            elif text.lower() == 'lurking reset':
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                if msg.to in read["readPoint"]:
                                    try:
                                        read["readPoint"][msg.to] = True
                                        read["readMember"][msg.to] = {}
                                        read["readTime"][msg.to] = readTime
                                        read["ROM"][msg.to] = {}
                                    except:
                                        pass
                                    client.sendMessage(msg.to, "「RESET READING POINT」:\n" + readTime)
                                else:
                                    client.sendMessage(msg.to, "「LURKING NOT ACTIVE」")
                                    
                            elif text.lower() == 'lurking':
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                if receiver in read['readPoint']:
                                    if read["ROM"][receiver].items() == []:
                                        client.sendMessage(receiver,"「LIST READER」:\nNone")
                                    else:
                                        chiya = []
                                        for rom in read["ROM"][receiver].items():
                                            chiya.append(rom[1])
                                        cmem = client.getContacts(chiya) 
                                        zx = ""
                                        zxc = ""
                                        zx2 = []
                                        xpesan = 'Lurkers:\n'
                                    for x in range(len(cmem)):
                                        xname = str(cmem[x].displayName)
                                        pesan = ''
                                        pesan2 = pesan+"@c\n"
                                        xlen = str(len(zxc)+len(xpesan))
                                        xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                        zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                                        zx2.append(zx)
                                        zxc += pesan2
                                    text = xpesan+ zxc + "\nLurking time: \n" + readTime
                                    try:
                                        client.sendMessage(receiver, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                    except Exception as error:
                                        print (error)
                                    pass
                                else:
                                    client.sendMessage(receiver,"「LURKING NOT SET.」")
#============================================================#READ FINISH#=========================================================#
                            elif msg.text in ["Autojoin on"]:
                                if settings['autoJoin'] == True:
                                    if settings["lang"] == "JP":
                                        client.sendText(msg.to, "「Auto join set to on」")
                                    else:
                                        client.sendText(msg.to, "「Auto join set to on」")
                                else:
                                    settings["autoJoin"] = True
                                    if settings["lang"] == "JP":
                                        client.sendText(msg.to,"「Auto join set to on」")
                                    else:
                                        client.sendText(msg.to,"「Auto join set to on」")

                            elif msg.text in ["Autojoin off"]:
                                if settings['autoJoin'] == False:
                                    if settings["lang"] == "JP":
                                        client.sendText(msg.to, "「Auto join set to off」")
                                    else:
                                        client.sendText(msg.to, "「Auto join set to off」")
                                else:
                                    settings["autoJoin"] = False
                                    if settings["lang"] == "JP":
                                        client.sendText(msg.to,"「Auto join set to off」")
                                    else:
                                        client.sendText(msg.to,"「Auto join set to off」")

                            elif msg.text in ["Leave on"]:
                                if settings['leaveRoom'] == True:
                                    if settings["lang"] == "JP":
                                        client.sendText(msg.to, "「Auto leave set to on」")
                                    else:
                                        client.sendText(msg.to, "「Auto leave set to on」")
                                else:
                                    settings["leaveRoom"] = True
                                    if settings["lang"] == "JP":
                                        client.sendText(msg.to,"「Auto leave set to on」")
                                    else:
                                        client.sendText(msg.to,"「Auto leave set to on」")

                            elif msg.text in ["Leave off"]:
                                if settings['leaveRoom'] == False:
                                    if settings["lang"] == "JP":
                                        client.sendText(msg.to, "「Auto leave set to off」")
                                    else:
                                        client.sendText(msg.to, "「Auto leave set to off」")
                                else:
                                    settings["leaveRoom"] = False
                                    if settings["lang"] == "JP":
                                        client.sendText(msg.to,"「Auto leave set to off」")
                                    else:
                                        client.sendText(msg.to,"「Auto leave set to off」")
                                        
                            elif msg.text in ["Gcreator"]:
                              if msg.toType == 2:
                                    ginfo = client.getGroup(msg.to)
                                    gCreator = ginfo.creator.mid
                                    try:
                                        gCreator1 = ginfo.creator.displayName

                                    except:
                                        gCreator = "Error"
                                    client.sendMessage(receiver, None, contentMetadata={'mid': gCreator}, contentType=13)
                                    client.sendText(msg.to, "「Group Creator」 : " + gCreator1)
                                    client.tag(receiver, gCreator)
#============================================================#RUNTIMESTART#=========================================================#
                            elif text.lower() == 'runtime':
                                eltime = time.time() - mulai
                                van = "「Bot running」\n"+waktu(eltime)
                                client.sendText(receiver, van)
#============================================================#RUNTIMEFINISHED#=========================================================#
#-----------------------------------------------
                            elif "Up " in msg.text:
                                   txt = msg.text.split(" ")
                                   jmlh = int(txt[2])
                                   teks = msg.text.replace("Up "+str(txt[1])+" "+str(jmlh)+ " ","")
                                   tulisan = jmlh * (teks+"\n")
                                   if txt[1] == "on":
                                    if jmlh <= 9999:
                                         for x in range(jmlh):
                                               client.sendText(msg.to,teks)
                                    elif txt[1] == "off":
                                         if jmlh <= 9999:
                                               client.sendText(msg.to, tulisan)
                                         else:
                                               client.sendText(msg.to, "Out of range! ")
#-------------------------------------------------------------------#
                            elif "Mid @" in msg.text:
                                _name = msgtext.replace("Mid @","")
                                _nametarget = _name.rstrip(' ')
                                gs = client.getGroup(msg.to)
                                for g in gs.members:
                                    if _nametarget == g.displayName:
                                        client.sendText(msg.to, g.mid)
                                    else:
                                        pass
#----------------Commandtambahan----------------------#
                            elif msg.text in ["Listgroup"]:
                               gid = client.getGroupIdsJoined()
                               h = ""
                               for i in gid:
                                h += "[>] %s  \n" % (client.getGroup(i).name + " | 「Members 」: " + str(len (client.getGroup(i).members)))
                               client.sendText(msg.to, "☆「Group List」☆\n"+ h +"「Total Group」 : " +str(len(gid)))
#============================================================#Mystatus start#=========================================================#
                            elif msg.text in ["Mystatus"]:
                                md = ""
                                if settings["autoJoin"] == True: md+=" 「❧Status : Auto join set to on」\n"
                                else: md +=" 「❧Status : Auto join set to off」\n"
                                if settings["leaveRoom"] == True: md+=" 「❧Status : Auto leave set to on」\n"
                                else: md +=" 「❧Status : Auto leave set to off」\n"
                                client.sendText(msg.to,md)
#============================================================#Mystatus Finish#=========================================================#
#============================================================#ULTI STARTR#=========================================================#
                            elif 'ulti' in text.lower():
                                   targets = []
                                   key = eval(msg.contentMetadata["MENTION"])
                                   key["MENTIONEES"] [0] ["M"]
                                   for x in key["MENTIONEES"]:
                                       targets.append(x["M"])
                                   for target in targets:
                                       try:
                                           client.kickoutFromGroup(msg.to,[target])                           
                                       except:
                                           client.sendText(msg.to,"Error")
                                           
#                            elif 'boom' in text.lower():
 #                                  targets = []
  #                                 key = eval(msg.contentMetadata["MENTION"])
   #                                key["MENTIONEES"] [0] ["M"]
    #                               for x in key["MENTIONEES"]:
     #                                  targets.append(x["M"])
      #                             for target in targets:
       #                                try:
        #                                   client2.kickoutFromGroup(msg.to,[target])                           
         #                              except:
          #                                 client2.sendText(msg.to,"Error")
#============================================================#ULTI FINISH#=========================================================#
                            elif 'stag @' in text.lower():
                                _name = msg.text.replace("Stag @","")
                                _nametarget = _name.rstrip(' ')
                                gs = client.getGroup(msg.to)
                                for g in gs.members:
                                    if _nametarget == g.displayName:
                                        xname = g.displayName
                                        xlen = str(len(xname)+1)
                                        msg.contentType = 0
                                        msg.text = "@"+xname+" "
                                        msg.contentMetadata ={'MENTION':'{"MENTIONEES":[{"S":"0","E":'+json.dumps(xlen)+',"M":'+json.dumps(g.mid)+'}]}','EMTVER':'4'}
                                        client.sendMessage(msg)
                                    else:
                                        pass
#============================================================#KICKER MAYHEM#=========================================================#
                            elif text.lower() == 'mayhem':
                                if msg.toType == 2:
                                    print ("ok")
                                    _name = msg.text.replace("mayhem","")
                                    gs = client.getGroup(receiver)
#                                    gs = client2.getGroup(receiver)
                                    client.sendText(msg.to,"「Mayhem」\nιѕ ѕтαят ♪")
                                    targets = []
                                    for g in gs.members:
                                        if _name in g.displayName:
                                            targets.append(g.mid)
                                    if targets == []:
                                        client.sendText(msg.to,"Not found.")
                                    else:
                                        for target in targets:
                                            try:
                                                klist=[client]#,client2]
                                                kicker=random.choice(klist)
                                                kicker.kickoutFromGroup(msg.to,[target])
                                                print (msg.to,[g.mid])
                                            except:
                                                client.sendText(msg.to,"group cleanse")
#============================================================#KICKER FINISHED#=========================================================#

#============================================================#HELPSTART#=========================================================#
                            elif text.lower() == 'myhelp':
                                client.sendText(msg.to,helpMessage)
                                print ("[COMMAND] HELP")
#====================================================#HELP FINISHED========================================================#
#============================================================#MODE / RESTART#=========================================================#
                            elif text.lower() == 'mode:self':
                                mode = 'self'
                                client.sendText(receiver, '「Self mode active」')
                                print ("[COMMAND] MODE")

                            elif text.lower() == 'restart':
                                client.sendText(receiver, '「Bot restart」')
                                print ("BOT RESTART")
                                restart_program()
                except Exception as e:
                    client.log("[SEND_MESSAGE] ERROR : " + str(e))
#=======================================================#MODE FINISHED#=============================================================#

#============================================================#SIDER START#=========================================================#
            elif op.type == 55:
                try:
                    if cctv['cyduk'][op.param1]==True:
                        if op.param1 in cctv['point']:
                            Name = client.getContact(op.param2).displayName
                            if Name in cctv['sidermem'][op.param1]:
                                pass
                            else:
                                cctv['sidermem'][op.param1] += "\n~ " + Name
                                pref=['「Auto check reader」\nHello you can join chat']
                                client.sendText(op.param1, str(random.choice(pref))+' '+Name)
                                print ("[COMMAND] CCTV")
                        else:
                            pass
                    else:
                        pass
                except:
                    pass

            else:
                pass

#============================================================#SIDER FINISHED#=========================================================#

#=========================================================================================================================================#
            # Don't remove this line, if you wan't get error soon!
            poll.setRevision(op.revision)
            
    except Exception as e:
        client.log("[SINGLE_TRACE] ERROR : " + str(e))
