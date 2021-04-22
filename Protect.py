import face_recognitionimport cv2import numpy as npimport pyautoguifrom selenium import webdriverimport datetime as dtimport osimport timeimport capture as cpimport info import mailimport logdef current_date_time():    curretndatetime=str(dt.datetime.now())    return currentdatetimedef current_time():    current_time=str(dt.datetime.now().time())    return current_timedef detect():    current_time = current_date_time()    file=log.open_file()    readfile=log.read_file()    if not readfile.read():        log_data="################### file created at "+ f'{current_time}' + " . ###################################### \n"    else :        log_data="\n\n\n\n\n################### file updated at "+ f'{current_time}' + " . ###################################### \n"    log.write_file(file,log_data)    User = "dheeraj"    From = "dheeraj.gametattav@gmail.com"    Password = "8700243345"    To = "prayansjain1311@gmail.com"    server=mail.login_mail(User,From,Password)    #User =data[0] # knownface name    #From=data[1]    #Password=data[2]    ##To=data[3]    if  server :        current_time = str(dt.datetime.now().time())        Message =  f'{User}' + " login at " + current_time+" . \n\n"        if not file.closed:            log_data=f'{User}' + " login at " + current_time + ". \n"            log.write_file(file,log_data)    root_encoding = cp.capturephoto(file) # main pic    if not file.closed :        log_data="Image captured at "+ f'{dt.datetime.now().time()}' + ".\n "        log.write_file(file,log_data)    video_capture=cv2.VideoCapture(0,cv2.CAP_DSHOW)    start_time=dt.datetime.now()    undetect_start_time=time.perf_counter()    face_match_start_time=time.perf_counter()    total_undetect_time=0    total_detect_time=0    total_unknown_detect_time=0    while True and not file.closed:        ret, frame = video_capture.read()        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)        face_locations = face_recognition.face_locations(frame)        #  findig if face located or not        if len(face_locations) == 0:            last_undetect_time=time.perf_counter()            face_match_start_time=time.perf_counter() # setting face match start time            #print("last undetct time ==>"+ str(last_undetect_time))            undetect_time=last_undetect_time-undetect_start_time # important undect time 1 minute            if undetect_time>=60:                total_undetect_time+=undetect_time # important total undect time                print("unable to identify face for "+ str(undetect_time))                log_data="Unable to identify the face for "+ str(undetect_time)+ " sec.\n"                if not file.closed :                    log.write_file(file,log_data)                               undetect_time=0                undetect_start_time=time.perf_counter()            log_data="Unable to identify the faces => Time  : " + f'{dt.datetime.now().time()}'+" .\n"            if not file.closed :                log.write_file(file,log_data)            print("Unable to identify the faces => Time  : " + f'{dt.datetime.now().time()}')        # lopp in a faces............        for a,b,c,d in face_locations:            cv2.rectangle(frame,(d,a),(b,c),(255,0,255),3)            face_encodings = face_recognition.face_encodings(frame,face_locations)            # check have face encodings or not                    if len(face_encodings) != 0:                               result = face_recognition.compare_faces(root_encoding,face_encodings[0],tolerance=0.55)                face_distance = face_recognition.face_distance(root_encoding,face_encodings[0])                            # checking face is matching or not....            if result[0] == True  :                last_face_match_time=time.perf_counter()                #print("last face match time ==> "+  str(last_face_match_time))                detect_time=last_face_match_time-face_match_start_time                                if detect_time>=60:                    print(" face match time is ==> "+ str(detect_time)+ " sec.")                    total_detect_time+=detect_time                    log_data="user is matching "+ str(detect_time)+ " sec.\n"                    if not file.closed :                        log.write_file(file,log_data)                    #print("total detect time is ==> "+ str(total_detect_time))                    # if detect time is greater than 60 then undetect_start_time=time.perf_counter()                    undetect_start_time=time.perf_counter()                    detect_time=0                    face_match_start_time=time.perf_counter()                log_data="[Match Found] ==> Time : "+f'{dt.datetime.now().time()}' +" .\n"                if not file.closed :                    log.write_file(file,log_data)                print("Face is matching ==> Time : " + f'{dt.datetime.now().time()}')                cv2.putText(frame,f'{User}',(b-100,c+50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2,cv2.LINE_AA)                print(face_distance)            else:                last_undetect_time=time.perf_counter()                face_match_start_time=time.perf_counter() # setting face match start time                #print("last unknown face detect time ==>"+ str(last_undetect_time))                undetect_time=last_undetect_time-undetect_start_time # important undect time 1 minute                if undetect_time>=60:                    print("user is unknown "+ str(undetect_time)+ " sec.")                    log_data="user is unknown "+ str(undetect_time)+ " sec .\n"                    if not file.closed :                        log.write_file(file,log_data)                    total_unknown_detect_time+=undetect_time                    total_undetect_time+=undetect_time # important total undect time                    #print(" unknown face is decting for "+ str(total_undetect_time)+ " sec.")                    undetect_time=0                    undetect_start_time=time.perf_counter()                log_data="[UNKNOWN]  Face is not matching => Time :"+f'{dt.datetime.now().time()}'+" .\n"                print("UNKNOWN FACE ==> Face is not matching => Time : "+f'{dt.datetime.now().time()}')                cv2.putText(frame,"Unknown",(b-100,c+50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2,cv2.LINE_AA)                print(face_distance)        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)        cv2.imshow("capturing",frame)                        k = cv2.waitKey(1)        if k % 256 == 27:            current_time = str(dt.datetime.now().time())            end_time=dt.datetime.now()            video_capture.release()            cv2.destroyAllWindows()            total_active_time=str(end_time-start_time)            total_active_time=str(total_active_time)            total_detect_time=str(total_detect_time)            total_undetect_time=str(total_undetect_time)            total_unknown_detect_time=str(total_unknown_detect_time)                     print("window is closing...")            Message+= f'{User}' + " logged out at " + current_time + " .\n"            Message+=" Total active time is "+ total_active_time + " sec . \n"            Message+="face is  detecting for "+ f"{total_detect_time}"+ "  sec .\n"            Message+="face is not detecting for "+ f"{total_undetect_time}"+ "  sec  .\n"            Message+=" unknown face is  detecting for "+ f"{total_unknown_detect_time}"+ "sec  .\n\n"                       value=mail.send_mail(server,User,From,Password,To,Message)            if value:                log_data=" mail send successfully . \n"                if not file.closed :                    log.write_file(file,log_data)            log_data=f'{User}' + " logged out at " + current_time + ".\n"            log_data+="Total active time is "+ total_active_time+" sec . \n"            log_data+=" ==============  face is  detecting for "+ f"{total_detect_time}"+ " sec .           ========================\n"            log_data+=" ==============  face is not detecting for "+ f"{total_undetect_time}"+ "  sec .          ======================== \n"            log_data+=" ==============   unknown face is  detecting for "+ f"{total_unknown_detect_time}"+ " sec .            ======================== \n"            if not file.closed :                log.write_file(file,log_data)                log.close_file(file)            break        video_capture.release()        cv2.destroyAllWindows()    else:        if not file.closed :            log.close_file()        print("\n\n\n\n")        print(" you are not logged in yet try again")        s