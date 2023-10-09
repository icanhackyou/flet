import flet as ft
import smtplib
import firebase_admin
from firebase_admin import db, credentials
from datetime import datetime
from pytz import timezone
import threading
import validate_email
import random
from email.message import EmailMessage


global db1, db2

cred=credentials.Certificate("credentials.json")
default_app1=firebase_admin.initialize_app(cred, {"databaseURL":"https://plug-and-play-29933-default-rtdb.firebaseio.com/"})

cred2=credentials.Certificate("credentials2.json")
default_app2=firebase_admin.initialize_app(cred2, {"databaseURL":"https://tempuserdataplugandplay-default-rtdb.firebaseio.com/"})

db1 = db.reference("/", app=default_app1)
db2 = db.reference("/", app=default_app2)

def main(page: ft.Page):
    def update_temproary_user_data():
        global main_dir
        def threaded():
            global main_dir
            pass
        threading.Thread(target=main())

    #-------------------------------------------------------------------------------functions--------------------------------------------------------------------------------------------------------------------------------------------------
    def register_load_user_data(user_email):
        pass
    # list of work to do tomorrow
    # check if user exists 
    # if yes load data using bookings body loader
    # if not register the user and show that he/she has no bookings
    # have the option to logout
    # remove remember me by default keep it there any simply have logout option simplify the code lower memory usage
    # also check if user has chosen remember me do the needful
    # if user clicks on account before loading the login_signup page first check for remember me then check verify the ip address and other security checks

    def security_check_remember_me(i):
        pass

    def change_page(i):
        global main_dir
        index=page.navigation_bar.selected_index
        if index==main_dir[ip_adress_user+browser_user]["current_page"]:
            pass
        else:
            main_dir[ip_adress_user+browser_user]["current_page"]=index
            page.controls.clear()
            add_plug_and_play_logo("pass")
            if index==0:
                homepage_body("pass")
            elif index==1:
                play_bookings_body("pass")
            elif index==2:
                send_sended_otp("pass") # till send_otp_body function use it after that use function create account which check if there is local storage auth key if no forward to send_otp+body
            
            page.close_banner()
            page.update()

    def close_banner(i):
        page.banner.open = False
        page.update()

    #------------------------------------------------------------------------------------end---------------------------------------------------------------------------------------------------------------------------------------------

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.title="Plug and Play"
    page.padding=18 #its very important otherwise the resend otp and change email buttons don't work well
    page.scroll = "hidden"
    page.on_keyboard_event=lambda i :[close_banner("pass")]
    page.on_disconnect=close_banner
    page.bgcolor="#F5F5F5"  
    size_=30
    weight_=ft.FontWeight.W_900

    #---------------------------------------------navigation bar(footer)---------------------------------------------------------------------------------------------------------------------------------------------
    play_text=ft.Row(controls=[ft.Row(controls=[ft.Text("P", size=size_, weight=weight_, color="#F73F6F"),
                                        ft.Text("l", size=size_, weight=weight_, color="#F76F6F"),
                                        ft.Text("a", size=size_, weight=weight_, color="#FA755B"),
                                        ft.Text("y", size=size_, weight=weight_, color="#FEA743"),],spacing=1),
                                        ], alignment="center", spacing =10)
    page.navigation_bar = ft.NavigationBar(on_change=change_page,
        destinations=[
            ft.NavigationDestination(
                icon=ft.icons.HOME_OUTLINED,
                selected_icon=ft.icons.HOME_ROUNDED,
                label="Home",
                ),
            ft.NavigationDestination(icon_content=play_text,
                                    label="Book seat"),
            ft.NavigationDestination(
                icon=ft.icons.ACCOUNT_CIRCLE_OUTLINED,
                selected_icon=ft.icons.ACCOUNT_CIRCLE_ROUNDED,
                label="Account",
            ),
        ],
    )

    #---------------------------------------------------------end----------------------------------------------------------------------------------------------------------------------------

    #---------------------------------------------Plug and Play Logo(header)------------------------------------------------------------------------------------------------------------------
    def add_plug_and_play_logo(i):
        size_=40
        plug_and_play_text=ft.Row(controls=[ft.Row(controls=[ft.Text("P", size=size_, weight=weight_, color="#F73F6F"),
                                            ft.Text("l", size=size_, weight=weight_, color="#F76F6F"),
                                            ft.Text("u", size=size_, weight=weight_, color="#FA755B"),
                                            ft.Text("g", size=size_, weight=weight_, color="#FEA743"),],spacing=1),

                                            ft.Row(controls=[ft.Text("&", size=size_, weight=weight_ , color="#FA755B")
                                            ]),

                                            ft.Row(controls=[ft.Text("P", size=size_, weight=weight_, color="#F73F6F"),
                                            ft.Text("l", size=size_, weight=weight_, color="#F76F6F"),
                                            ft.Text("a", size=size_, weight=weight_, color="#FA755B"),
                                            ft.Text("y", size=size_, weight=weight_, color="#FEA743"),],spacing=1),
                                            ], alignment="center", spacing =10)

        page.add(plug_and_play_text)
    #---------------------------------------------------------end-------------------------------------------------------------------------------------------------------------------------------

    #---------------------------------------------body(login_signup)----------------------------------------------------------------------------------------------------------------------------------------
    
    def send_sended_otp(choice):
        global main_dir

        #---------------------------------------------------------(check for remember me)-------------------------------------------------------------------------------------------------------------------------

        security_check_remember_me("pass")

        #------------------------------------------------------------------end------------------------------------------------------------------------------------------------------------------------------------
        def check_otp(i):
            global main_dir
            if db2.child(ip_adress_user+browser_user).child("otp_").get()==0:
                pass
            else:
                otp=main_dir[ip_adress_user+browser_user]["otp_login_singup"].value
                current_time=datetime.now(timezone("Asia/Kolkata")).strftime("%Y-%m-%d %H:%M:%S:%f")
                value=datetime.strptime(current_time, "%Y-%m-%d %H:%M:%S:%f")-datetime.strptime(main_dir[ip_adress_user+browser_user]["otp_gen_time"], "%Y-%m-%d %H:%M:%S:%f")
                passed_minutes=value.seconds//60
                if len(otp)==6 or len(otp)>6 or i=="continue_user":# here has to put condition ==5 and >5 since the reponse is always 1 keyword buffer so to fullfill the requirement of 6 char otp simply lower it to 5 hence when user type 6 dig simply logic gets true
                    if main_dir[ip_adress_user+browser_user]["try_"]<=6 and int(passed_minutes)<=4: #if have to set time for 5 minutes set condition : int(passed_minutes)<4
                        if i=="continue_user":
                            pass
                        else:
                            if int(otp)==main_dir[ip_adress_user+browser_user]["otp_"]:
                                main_dir[ip_adress_user+browser_user]["otp_"]=0
                                main_dir[ip_adress_user+browser_user]["trys_"]=0
                                main_dir[ip_adress_user+browser_user]["otp_gen_time"]=0
                                main_dir[ip_adress_user+browser_user]["login_status"]=main_dir[ip_adress_user+browser_user]["email_"] #hence if user logs out simply set login_status=none and use it to forward from account page to bookings page
                                register_load_user_data(main_dir[ip_adress_user+browser_user]["email_"])
                                bookings_user_login(main_dir[ip_adress_user+browser_user]["email_"])
                            else: # fast typing attack safety feature even if fast typing is there nothing will happen even if this code was not there but user will get stuck
                                main_dir[ip_adress_user+browser_user]["otp_login_singup"].read_only=True # fast wpm attack protection vvi security feature
                                page.update()
                                main_dir[ip_adress_user+browser_user]["otp_login_singup"].value=""
                                main_dir[ip_adress_user+browser_user]["otp_login_singup"].read_only=False
                                main_dir[ip_adress_user+browser_user]["try_"]+=1
                                page.update()
                    else:
                        main_dir[ip_adress_user+browser_user]["otp_login_singup"].value=""
                        main_dir[ip_adress_user+browser_user]["otp_login_singup"].label=""
                        main_dir[ip_adress_user+browser_user]["otp_login_singup"].hint_text="Sending New OTP"
                        main_dir[ip_adress_user+browser_user]["otp_login_singup"].read_only=True

                        send_sended_otp("resend_otp")
                else:
                    if len(otp)>6:
                        main_dir[ip_adress_user+browser_user]["otp_login_singup"].read_only=True # fast wpm attack protection vvi security feature
                        page.update()
                        main_dir[ip_adress_user+browser_user]["otp_login_singup"].value=""
                        main_dir[ip_adress_user+browser_user]["otp_login_singup"].read_only=False
                        page.update()
        def reset_user_data():
            global main_dir
            main_dir[ip_adress_user+browser_user]["otp_"]=0
            main_dir[ip_adress_user+browser_user]["trys_"]=0
            main_dir[ip_adress_user+browser_user]["otp_gen_time"]=0
            main_dir[ip_adress_user+browser_user]["email_"]=""

        def send_mail(i,email,messagee,subject):
            def threaded():
                global main_dir
                try:
                    message=EmailMessage()
                    message["Subject"]=subject
                    message["From"]="Plug and Play"
                    message["To"]=email
                    message.set_content(messagee)
                    server=smtplib.SMTP_SSL("smtp.gmail.com",465)
                    server.login("plugandplay90742@gmail.com","mfwoymsiceafchup")
                    server.send_message(message)
                    server.quit()
                    if i=="resend_otp":
                        pass
                    else:
                        row_remember_load.controls.pop()
                    if i=="resend_otp":
                        main_dir[ip_adress_user+browser_user]["otp_login_singup"].label="OTP"
                        main_dir[ip_adress_user+browser_user]["otp_login_singup"].hint_text=""
                        main_dir[ip_adress_user+browser_user]["otp_login_singup"].read_only=False
                    else:
                        main_dir[ip_adress_user+browser_user]["otp_login_singup"].read_only=False

                    if i=="resend_otp":
                        main_dir[ip_adress_user+browser_user]["page_banner"]=ft.Banner(content=ft.Text("New OTP Sent!"),actions=[ft.TextButton("Dismiss", on_click=close_banner),],bgcolor=ft.colors.GREEN_200,leading=ft.Icon(ft.icons.GPP_GOOD, size=40))
                        page.banner=main_dir[ip_adress_user+browser_user]["page_banner"]
                        main_dir[ip_adress_user+browser_user]["page_banner"].open=True
                    else:
                        main_dir[ip_adress_user+browser_user]["page_banner"]=ft.Banner(content=ft.Text("OTP sent!"),actions=[ft.TextButton("Dismiss", on_click=close_banner),],bgcolor=ft.colors.GREEN_200,leading=ft.Icon(ft.icons.GPP_GOOD, size=40))
                        page.banner=main_dir[ip_adress_user+browser_user]["page_banner"]
                        main_dir[ip_adress_user+browser_user]["page_banner"].open=True

                except Exception as e:
                    if i=="resend_otp":
                        pass
                    else:
                        row_remember_load.controls.pop()
                    main_dir[ip_adress_user+browser_user]["page_banner"]=ft.Banner(content=ft.Text("Please check your Email!"),actions=[ft.TextButton("Dismiss", on_click=close_banner),],bgcolor=ft.colors.AMBER_100,leading=ft.Icon(ft.icons.WARNING_AMBER_ROUNDED, color=ft.colors.AMBER, size=40))
                    page.banner=main_dir[ip_adress_user+browser_user]["page_banner"]
                    main_dir[ip_adress_user+browser_user]["page_banner"].open=True
                page.update()
            threading.Thread(target=lambda:[threaded()]).start()

        def send_otp(i):
            global main_dir
            def resend_otp():
                main_dir[ip_adress_user+browser_user]["otp_login_singup"].value=""
                main_dir[ip_adress_user+browser_user]["otp_login_singup"].label=""
                main_dir[ip_adress_user+browser_user]["otp_login_singup"].hint_text="Sending New OTP"
                main_dir[ip_adress_user+browser_user]["otp_login_singup"].read_only=True

            if i=="resend_otp" or validate_email.validate_email(main_dir[ip_adress_user+browser_user]["email_login_signup"].value) or i=="continue_user":
                main_dir[ip_adress_user+browser_user]["email_login_signup"].read_only=True
                if i=="continue_user":
                    pass
                else:
                    main_dir[ip_adress_user+browser_user]["otp_"]=random.randrange(100000,999999)
                    main_dir[ip_adress_user+browser_user]["try_"]=0
                    main_dir[ip_adress_user+browser_user]["otp_gen_time"]=datetime.now(timezone("Asia/Kolkata")).strftime("%Y-%m-%d %H:%M:%S:%f")
                if i=="resend_otp":
                    pass
                else:
                    if i=="continue_user":
                        pass
                    else:
                        main_dir[ip_adress_user+browser_user]["email_"]=main_dir[ip_adress_user+browser_user]["email_login_signup"].value
                if i=="resend_otp":
                    send_mail("resend_otp",main_dir[ip_adress_user+browser_user]["email_"], f"{main_dir[ip_adress_user+browser_user]['otp_']} is OTP to Login/Singup to PlugandPlay don't share this OTP with anyone we never call or ask for OTP.", "PlugandPlay OTP verification message")

                else:
                    if i=="continue_user":
                        pass
                    else:
                        row_remember_load.controls.append(loading_circle)
                    row_send_change_resend.controls.pop()
                    row_send_change_resend.controls=[ft.Container(content=ft.TextButton(text="Resend OTP", on_click=lambda e:[resend_otp(),send_otp("resend_otp")]), border=ft.border.all(2, ft.colors.BLACK),border_radius=19, bgcolor="#FFD630", expand=True, height=40),
                                                    ft.Container(content=ft.TextButton(text="Change Email", on_click=lambda e: [page.controls.clear(),add_plug_and_play_logo("pass"), reset_user_data(), send_sended_otp("pass")]),border=ft.border.all(2, ft.colors.BLACK),border_radius=19, bgcolor="#FFD630", expand=True, height=40)]
                    if i=="continue_user":
                        main_dir[ip_adress_user+browser_user]["email_login_signup"].read_only=False
                        main_dir[ip_adress_user+browser_user]["email_login_signup"].value=main_dir[ip_adress_user+browser_user]["email_"]
                        main_dir[ip_adress_user+browser_user]["email_login_signup"].read_only=True
                        main_dir[ip_adress_user+browser_user]["otp_login_singup"].read_only=False
                        check_otp("continue_user")
                        page.update()
                    else:
                        send_mail("pass",main_dir[ip_adress_user+browser_user]["email_"], f"{main_dir[ip_adress_user+browser_user]['otp_']} is OTP to Login/Singup to PlugandPlay don't share this OTP with anyone we never call or ask for OTP.", "PlugandPlay OTP verification message")
            
            else:
                main_dir[ip_adress_user+browser_user]["email_login_signup"].read_only=False
                main_dir[ip_adress_user+browser_user]["page_banner"]=ft.Banner(content=ft.Text("Invalid Email Address"),actions=[ft.TextButton("Retry", on_click=close_banner),],bgcolor=ft.colors.AMBER_100,leading=ft.Icon(ft.icons.WARNING_AMBER_ROUNDED, color=ft.colors.AMBER, size=40))
                page.banner=main_dir[ip_adress_user+browser_user]["page_banner"]
                main_dir[ip_adress_user+browser_user]["page_banner"].open=True

            page.update()

        if choice=="resend_otp":
            send_otp("resend_otp")
            return
        
        if main_dir[ip_adress_user+browser_user]["login_status"]==None:
            pass
        else:
            bookings_user_login(main_dir[ip_adress_user+browser_user]["login_status"])
            return
        
        main_dir[ip_adress_user+browser_user]["email_login_signup"]=ft.TextField(expand=True,height=53,suffix_icon=ft.icons.EMAIL_OUTLINED,label="Email")
        main_dir[ip_adress_user+browser_user]["otp_login_singup"]=ft.TextField(expand=True,height=53,password=True, can_reveal_password=True, label="OTP", read_only=True, on_change=lambda i:[check_otp(main_dir[ip_adress_user+browser_user]["otp_login_singup"].value)])
        remember_me=ft.Switch(label="  Remember me", value=True)
        loading_circle=ft.Column([ft.ProgressRing(height=18, width=18), ft.Text("*Sending OTP", size=10, color="red")],horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        row_remember_load=ft.Row(controls=[remember_me])
        row_send_change_resend=ft.Row(controls=[ft.Container(content=ft.TextButton(text="Send OTP", on_click=send_otp),border=ft.border.all(2, ft.colors.BLACK),border_radius=19, bgcolor="#FFD630", expand=True, height=40)])

        body_login_signup=ft.Column(controls=[ft.Text(),
                                ft.Container(content=ft.Column(controls=[ft.Row(controls=[ft.Text("Login / Sign Up", size=22, color="#062A70", text_align="center", weight=ft.FontWeight.W_900)], alignment="center"),
                                                                        ft.Row(controls=[main_dir[ip_adress_user+browser_user]["email_login_signup"]]),
                                                                        ft.Row(controls=[main_dir[ip_adress_user+browser_user]["otp_login_singup"]]),
                                                                        row_remember_load,
                                                                        row_send_change_resend,
                                                                        ], spacing=20),height=330, width=400, bgcolor="#D9D9D9", border_radius=15, padding=10)], alignment="center", spacing=15)

        if main_dir[ip_adress_user+browser_user]["otp_"]==0: # therefore always set value of otp_=0 after user logs in successfully
            pass
        else:
            print(ip_adress_user+browser_user, "here")
            print(page.client_user_agent, page.client_ip)
            send_otp("continue_user")
        page.add(body_login_signup)

    

    #----------------------------------------------end----------------------------------------------------------------------------------------------------------------------------------------

    #---------------------------------------------body(homepage)---------------------------------------------------------------------------------------------------------------------------------

    def homepage_body(i):

        controllers_hot_deals=ft.Row(controls=[ft.Container(width=120, height=120, border_radius=15, bgcolor=ft.colors.GREEN_200, ink=True, on_click=lambda e:print("hello world")),
                                        ft.Container(width=120, height=120, border_radius=15, bgcolor=ft.colors.GREEN_200, ink=True, on_click=lambda e:print("hello world")),
                                        ft.Container(width=120, height=120, border_radius=15, bgcolor=ft.colors.GREEN_200, ink=True, on_click=lambda e:print("hello world")),
                                        ], scroll="hidden", alignment="center")
        controllers_games_toplay=ft.Row(controls=[ft.Container(width=120, height=70, border_radius=15, bgcolor=ft.colors.GREEN_200, ink=True, on_click=lambda e:print("hello world")),
                                        ft.Container(width=120, height=70, border_radius=15, bgcolor=ft.colors.GREEN_200, ink=True, on_click=lambda e:print("hello world")),
                                        ft.Container(width=120, height=70, border_radius=15, bgcolor=ft.colors.GREEN_200, ink=True, on_click=lambda e:print("hello world")),
                                        ], scroll="hidden")

        hot_deals_label=ft.Text(value="Hot Deal", size=24, color="#062A70", weight=ft.FontWeight.BOLD,)
        gamestoplay_label=ft.Text(value="Games to Play", size=25, color="#062A70", weight=ft.FontWeight.BOLD,)
        homepage=ft.Column(controls=[ft.Row(controls=[hot_deals_label], alignment="center"),
                        controllers_hot_deals,
                        ft.Text(),
                        ft.Row(controls=[gamestoplay_label], alignment="center"),
                        controllers_games_toplay,
                        controllers_games_toplay,
                        controllers_games_toplay,
                        controllers_games_toplay,
                        controllers_games_toplay,
                        controllers_games_toplay,
                        controllers_games_toplay
                        ], width=400,spacing=10)
        
        page.add(homepage)

    #----------------------------------------------end------------------------------------------------------------------------------------------------------------------------------------------------------------------

    #---------------------------------------------body(play(bookings))------------------------------------------------------------------------------------------------------------------------------------------------------------

    def play_bookings_body(i):
        
        page.add(ft.Text("Page under construction", text_align="center"))

    #----------------------------------------------end---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #---------------------------------------------body(bookings_user_login_loaduserdata)------------------------------------------------------------------------------------------------------------------------------------------------------------

    def bookings_user_login(user_email):

        ref=db.reference()
        try:
            page.controls.clear()
            add_plug_and_play_logo("pass")
            page.add(
                ft.Row(controls=[
                    ft.Text(f"Welcome {user_email}",
                            text_align="center",
                            size=20)
                ],
                        alignment="center"))
        except:
            pass # don't store tpin locally only store tid and match if local storage tid match with tid in payments node of user/user_email hence less data used if they match pass only one tpin shown at a time and tpin data never stored in local storage
                # if user has opted out for remember me load the data similarly and store it to session storage instead of local storage hence data gets deleted when user logs out in this case too don't store tpin tpin loads when user clicks on a particular booking

    #----------------------------------------------end---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    #----------------------------------------------------------------------starter code---------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
    global  main_dir
    main_dir={} # just one global variable and its way simpler easier to implement just iclude glabl variables in this
    ip_adress_user=page.client_ip
    browser_user=page.client_user_agent
    main_dir[ip_adress_user+browser_user]={'otp_': None, 'trys_': None, 'otp_gen_time': None, 'email_': None, 'login_status': None, 'current_page': None, 'page_banner': None, 'otp_login_singup': None, 'email_login_signup': None}
    main_dir[ip_adress_user+browser_user]["otp_"]=0
    main_dir[ip_adress_user+browser_user]["current_page"]=0
    main_dir[ip_adress_user+browser_user]["page_banner"]=ft.Banner(content=ft.Text("There was an Error"),actions=[ft.TextButton("Dismiss", on_click=close_banner),],bgcolor=ft.colors.AMBER_100,leading=ft.Icon(ft.icons.WARNING_AMBER_ROUNDED, size=40))
    page.banner=main_dir[ip_adress_user+browser_user]["page_banner"]
    add_plug_and_play_logo("pass")
    homepage_body("pass")
    update_temproary_user_data("pass")

    #-----------------------------------------------------------------------------end-----------------------------------------------------------------------------------------------------------------------------------

ft.app(target=main, view=ft.WEB_BROWSER)
