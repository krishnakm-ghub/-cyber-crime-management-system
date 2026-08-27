```
from time import sleep
from tkinter import messagebox

import PIL
import customtkinter as ctk
import mysql.connector
from PIL import Image
from scripts.regsetup import description

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="Krishna@sql",
        database="cyber_crime_db"
    )
    cursor = connection.cursor(buffered=True)

except mysql.connector.Error as e:
    messagebox.showerror("Database Error", str(e))



ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

#splash
loading_screen = ctk.CTk()
loading_screen.geometry("1366x900")
loading_screen.title("Loading")
sc_width = loading_screen.winfo_screenwidth()
sc_height = loading_screen.winfo_screenheight()
splash_bg = ctk.CTkImage(
    light_image = Image.open(r"C:\Users\HP\Desktop\python\screen1.jpg"),
    dark_image = Image.open(r"C:\Users\HP\Desktop\python\screen1.jpg"),
    size=(sc_width,sc_height)
)
#loading_screen.attributes("-fullscreen", True)
loading_screen.state("zoomed")

ltitle = ctk.CTkLabel(
    loading_screen,
    image = splash_bg,
    text="                 \n\n\n\n\n\n\n\n\n       CYBER MANAGEMENT PORTAL",
    font=("arial", 35,"bold")
)
ltitle.place(x=0,y=0,relwidth=1,relheight=1)
#ltitle.pack(pady=100)

loading = ctk.CTkLabel(
    loading_screen,
    text="Initializing Security system...",
    text_color="white",
    font=("arial", 16)
)
loading.pack(pady=(50,0))

def open_login():
    loading_screen.quit()
    loading_screen.destroy()

loading_screen.after(3000, open_login)
loading_screen.mainloop()

#creating main windows

app = ctk.CTk()
app.title("Cybercrime Management Portal")
app.geometry("1366x768")
login_bg = ctk.CTkImage(
    light_image=Image.open(r"C:\Users\HP\Desktop\python\login3.jpeg"),
    dark_image=Image.open(r"C:\Users\HP\Desktop\python\login3.jpeg"),
    size=(1500,1000)
)

google_icon = ctk.CTkImage(
    light_image = Image.open(r"D:\logo\google.png.webp"),
    dark_image =    Image.open(r"D:\logo\google.png.webp"),
    size=(20,20)
)
facebook_icon = ctk.CTkImage(
    light_image = Image.open(r"D:\logo\facebook.png"),
    dark_image = Image.open(r"D:\logo\facebook.png"),
    size=(20,20)
)
apple_icon = ctk.CTkImage(
    light_image = Image.open(r"D:\logo\appleid.png"),
    dark_image = Image.open(r"D:\logo\appleid.png"),
    size=(20,20)
)

#"#0B1020"
#bg
bg = ctk.CTkFrame(app,fg_color="transparent",corner_radius=20)
bg.pack(fill="both",expand="yes")

bg_lable = ctk.CTkLabel(
    bg,
    image=login_bg,
    text=""
)
bg_lable.place(x=0,y=0,relwidth=1,relheight=1)

#home page button
def open_homebtn():
    open_h()
home_btn = ctk.CTkButton(
    bg,
    text = "Go To HomePage",
    width = 120,
    height = 35,
    fg_color = "#2F3C7E",
    hover_color = "#4455AA",
    corner_radius = 20,
    command=open_homebtn
)
home_btn.place(x = 50, y = 60)

#login card

card = ctk.CTkFrame(
    bg,
    width = 650,
    height = 600,
    fg_color="#1A2238",
    corner_radius=30,
    border_width=2,
    border_color="#4A90E2"
)
card.place(relx = 0.5, rely= 0.5, anchor= "center")

#welcome title
title = ctk.CTkLabel(
    card,
    text="Welcome",
    font=("Times new roman", 34,"bold")
)
title.pack(pady=(15,0))
#subtitles
subtitle = ctk.CTkLabel(
    card,
    text="Please login into your account",
    font=("arial",14)
)
subtitle.pack(pady=(0,25))

#home
def open_h():
    def load_complaint():
        cursor.execute("""
        select 
        complaint_id,crime_type,status_info 
        from complaints
        order by 
        complaint_id desc
        """
        )
        records = cursor.fetchall()
        return records

    def dash_board_cards():
        cursor.execute("""
            select count(*) from complaints""")
        total = cursor.fetchone()[0]
        cursor.execute("""
            select count(*) from complaints where status_info ="pending" """)
        pending = cursor.fetchone()[0]
        cursor.execute("""
            select count(*) from complaints where status_info = "resolved" """)
        resolved = cursor.fetchone()[0]
        total_label.configure(
            text =f"\n{total}\n\nTotal\nComplaints",
            font=("times new roman", 22,"bold")
        )
        pending_label.configure(
            text =f"\n{pending}\n\nPending\nComplaints",
            font=("times new roman", 22,"bold")
        )
        resolved_label.configure(
            text = f"\n{resolved}\n\nResolved\nComplaints",
            font=("timesnew roman", 22, "bold")
        )



    app.withdraw()

    home_pg = ctk.CTkToplevel(app)
    home_pg.title("Cyber crime management system")
    home_pg.geometry("1400x800")
    BG_COLOR = "#0B1020"
    SIDEBAR_COLOUR = "#16213E"
    BUTTON_COLOUR = "#2563EB"
    BUTTON_HOVER = "#1D4ED8"
    main_frame = ctk.CTkFrame(
        home_pg,
        fg_color = BG_COLOR
    )
    main_frame.pack(fill="both",expand="yes")
    sidebar = ctk.CTkFrame(
        main_frame,
        width = 300,
        fg_color=SIDEBAR_COLOUR,
        corner_radius=0
    )
    sidebar.pack(side="left",fill="y")

    portal_title = ctk.CTkLabel(
        sidebar,
        text = "       CYBER PORTAL       ",
        font=("arial",19,"bold")
    )
    portal_title.pack(padx=20,pady=65)
    #open_bot
    def open_bot():
        bot_window = ctk.CTkToplevel(home_pg)
        bot_window.title("Cybe Bot Assistance")
        bot_window.geometry("1300x750")
        bot_window.configure(fg_color=BG_COLOR)
        bot_window.grab_set()

        #creating main container
        bot_main = ctk.CTkFrame(
            bot_window,
            fg_color=BG_COLOR
        )
        bot_main.pack(fill="both",expand="yes")

        #left_side bar
        bot_sidebar = ctk.CTkFrame(
            bot_main,
            width = 280,
            fg_color=SIDEBAR_COLOUR
        )
        bot_sidebar.pack(side="left",fill="y",padx=10,pady=10)
        #side bar title
        ctk.CTkButton(
            bot_sidebar,
            text="Cyber Portal",
            font=("arial",24,"bold")
        ).pack(pady=30)

        #buttons
        menu = [
            "📝 Register Complaint",
            "📊 Dashboard",
            "👁 View Complaint",
            "⚙ Settings",
            "👤 Help",
            "🤖 Cyber Bot"
        ]


        for i in menu:

            bot_btn = ctk.CTkButton(
                bot_sidebar,
                text=i,
                width=220,
                height=45,
                fg_color=BUTTON_COLOUR,
                hover_color=BUTTON_HOVER
            )
            bot_btn.pack(pady=8)
        #content
        content = ctk.CTkFrame(
            bot_main,
            fg_color="#0F172A"
        )
        content.pack(side="left",fill="both",expand="yes",padx=10,pady=10)

        #header
        top_frame = ctk.CTkFrame(
            content,
            fg_color="#0F172A"
        )

        top_frame.pack(fill="x", pady=10)

        title = ctk.CTkLabel(
            top_frame,
            text="🤖 CYBER BOT ASSISTANT",
            font=("Arial", 28, "bold")
        )
        title.pack(side="left", padx=20)

        online = ctk.CTkLabel(
            top_frame,
            text="🟢 Online",
            font=("Arial", 16)
        )
        online.pack(side="right", padx=20)

        #quick button
        quick_frame= ctk.CTkFrame(
            content,
            fg_color="#0F172A"
        )
        quick_frame.pack(fill="x", pady=10)
        for qitem in [
            "Complaint Help",
            "Security Tips",
            "FAQ",
            "Contact Admin"
        ]:
            ctk.CTkButton(
                quick_frame,
                text=qitem,
                width=180,
                height=45,
                fg_color="#16213E"
            ).pack(side="left",padx=10)

            #chat area
        chat_box_bot = ctk.CTkTextbox(
            content,
            fg_color="#1E293B",
            corner_radius=15,
            height=450
        )
        chat_box_bot.pack(
            fill="both",
            expand="yes",
            padx=15,
            pady=10
        )

        # default msg

        chat_box_bot.insert(
            "end",
            "Bot: Hello! I am cyber bot.\n\n"
        )
        chat_box_bot.insert(
            "end",
            "I can help with:\n"
            "* complaint registeration\n"
            "* complaint status\n"
            "* security tips\n\n"
        )

        #bottom frame
        bot_bottom_frame = ctk.CTkFrame(
            content,
            fg_color="#0F172A"
        )
        bot_bottom_frame.pack(fill="x", pady=10)

        #----------------------------------------------------------------------------bot Questions

        def send_message():
            user_msg = bot_msg_entry.get().strip()
            if user_msg=="":
                messagebox.showerror("warning", "Please enter a message")
                return
            chat_box_bot.insert("end",f"you: {user_msg}\n")
            msg = user_msg.lower()
            #msg = bot_msg_entry.get().strip().lower()

            if "hello" in msg:
                bot_reply = "Hello! Welcome to Cyber Crime Management Portal. How can I help you?"

            elif "hi" in msg:
                bot_reply = "Hi! How can I assist you today?"

            elif "register complaint" in msg:
                bot_reply = "Go to Register Complaint and fill in your details to submit a complaint."

            elif "complaint" in msg:
                bot_reply = "You can register, view, update, or track complaints from the portal."

            elif "how to register complaint" in msg:
                bot_reply = "Open Register Complaint, enter your details, select crime type, and click Submit."

            elif "status" in msg:
                bot_reply = "You can check complaint status in the View Complaint section."

            elif "complaint status" in msg:
                bot_reply = "Enter your Complaint ID in View Complaint to check the current status."

            elif "pending" in msg:
                bot_reply = "Pending means your complaint is waiting for review."

            elif "resolved" in msg:
                bot_reply = "Resolved means the complaint has been successfully completed."

            elif "investigation" in msg:
                bot_reply = "Investigation means the complaint is currently being reviewed by the authorities."

            elif "dashboard" in msg:
                bot_reply = "The Dashboard shows complaint statistics such as total, pending, and resolved complaints."

            elif "total complaints" in msg:
                bot_reply = "The Dashboard displays the total number of complaints registered."

            elif "pending complaints" in msg:
                bot_reply = "The Dashboard displays all pending complaints."

            elif "resolved complaints" in msg:
                bot_reply = "The Dashboard displays all resolved complaints."

            elif "view complaint" in msg:
                bot_reply = "Open View Complaint and search using the Complaint ID."

            elif "search complaint" in msg:
                bot_reply = "Enter the Complaint ID in the search box and click Search."

            elif "edit complaint" in msg:
                bot_reply = "Use the Edit button in the complaint card to modify complaint details."

            elif "delete complaint" in msg:
                bot_reply = "Use the Delete button to remove a complaint from the database."

            elif "crime types" in msg:
                bot_reply = "Available crime types include Phishing, UPI Fraud, Identity Theft, Social Media Scam, and Other."

            elif "phishing" in msg:
                bot_reply = "Phishing is a fraudulent attempt to steal personal information using fake websites or emails."

            elif "upi fraud" in msg:
                bot_reply = "UPI Fraud involves unauthorized transactions through UPI applications."

            elif "identity theft" in msg:
                bot_reply = "Identity Theft occurs when someone uses your personal information without permission."

            elif "social media scam" in msg:
                bot_reply = "Social Media Scam involves fraud through social networking platforms."

            elif "settings" in msg:
                bot_reply = "The Settings page allows you to manage application preferences."

            elif "profile" in msg:
                bot_reply = "The Profile section contains administrator information."

            elif "security" in msg:
                bot_reply = "Never share OTPs, passwords, or banking information with anyone."

            elif "notifications" in msg:
                bot_reply = "Notification settings allow you to manage alerts and updates."

            elif "backup" in msg:
                bot_reply = "Backup & Restore helps you secure your application data."

            elif "language" in msg:
                bot_reply = "Language settings allow you to change the application language."

            elif "appearance" in msg:
                bot_reply = "Appearance settings allow you to customize the interface."

            elif "forgot password" in msg:
                bot_reply = "Please contact the administrator to reset your password."

            elif "admin" in msg:
                bot_reply = "For administrative support, contact the system administrator."

            elif "help" in msg:
                bot_reply = "Please describe your issue in detail and I will assist you."

            elif "thank you" in msg:
                bot_reply = "You're welcome! Stay safe online."

            elif "bye" in msg:
                bot_reply = "Thank you for using Cyber Crime Management Portal. Have a great day!"

            else:
                bot_reply = "Sorry, I didn't understand your question. Please try again."
            chat_box_bot.insert("end",f"BOT: {bot_reply}\n")
            chat_box_bot.see("end")
            bot_msg_entry.delete(0,"end")
#--------------------------------------------------------------------------------------------------





        #message entry
        bot_msg_entry = ctk.CTkEntry(
            bot_bottom_frame,
            height=50,
            placeholder_text="Type Your question here..."
        )
        bot_msg_entry.pack(side="left",fill="x",expand=True,padx=10)

        #send button
        send_btn=ctk.CTkButton(
            bot_bottom_frame,
            text="send",
            width=180,
            height=50,
            fg_color=BUTTON_COLOUR,
            hover_color=BUTTON_HOVER,
            command=send_message
        )
        send_btn.pack(side="right",padx=10)






    #open_settings

    # _________________________________________________________open setting
    def open_setting():
        setting_window = ctk.CTkToplevel(home_pg)
        setting_window.title("Settings")
        setting_window.geometry("950x700")
        setting_window.configure(fg_color=BG_COLOR)
        setting_window.grab_set()
        setting_main = ctk.CTkFrame(
            setting_window,
            fg_color=BG_COLOR
        )
        setting_main.pack(fill="both", expand=True)

        # ------------------------------------------------------------------left sidebar
        setting_sidebar = ctk.CTkFrame(
            setting_main,
            width=250,
            fg_color=SIDEBAR_COLOUR
        )
        setting_sidebar.pack(side="left", fill="y")

        # -----------------------------------------------------------------right side frame
        setting_content = ctk.CTkScrollableFrame(
            setting_main,
            fg_color="#1E293B"
        )
        setting_content.pack(
            side="left",
            fill="both",
            expand=True,
            padx=15,
            pady=15
        )
        # ------------------------------------------------------------------sidebar title
        sidebar_title = ctk.CTkLabel(
            setting_sidebar,
            text="⚙ SETTINGS",
            font=("arial", 24, "bold")
        )
        sidebar_title.pack(pady=30)
        profile_card = ctk.CTkFrame(
            setting_sidebar,
            fg_color="#1E293B",
            corner_radius=10
        )
        profile_card.pack(fill="x",padx=10,pady=10)
        ctk.CTkLabel(
            profile_card,
            text="👤 Administrator",
            font=("arial",16,"bold")
        ).pack(pady=(10.2))
        ctk.CTkLabel(
            profile_card,
            text="admin@cyberportal.com"
        ).pack(pady=(0,10))

        # -------------------------------------------------------------------------menu_items
        menu_items = [
            "⚙ General",
            "👤 Profile",
            "🔒 Security",
            "🔑 Password",
            "🔔 Notifications",
            "🛡 Privacy",
            "🖥 Appearance",
            "🌐 Language",
            "☁ Backup & Restore",
            "ℹ About"

        ]
        for items in menu_items:

            color = BUTTON_COLOUR
            if items == "⚙ General":
                color = "#1D4ED8"
            btn = ctk.CTkButton(
                setting_sidebar,
                text=items,
                fg_color=BUTTON_COLOUR,
                hover_color=BUTTON_HOVER,
                width=200,
                height=40
            )
            btn.pack(pady=5)


        main_heading = ctk.CTkLabel(
            setting_content,
            text="⚙ General SETTINGS",
            font=("arial", 28, "bold")
        )
        main_heading.pack(anchor="w", padx=20, pady=(20, 5))

        # SUB TITLE
        set_subtitle = ctk.CTkLabel(
            setting_content,
            text="Manage Your application Preferences."
        )
        set_subtitle.pack(anchor="w", padx=20)

        # APP CARD
        app_card = ctk.CTkFrame(
            setting_content,
            fg_color="#0F172A",
            corner_radius=15
        )
        app_card.pack(fill="x",
                      padx=20,
                      pady=20)
        # CARD TITLE
        ctk.CTkLabel(
            app_card,
            text="⚙ Application Settings",
            font=("arial", 18, "bold")
        ).pack(anchor="w", padx=20, pady=20)

        # switch
        ctk.CTkSwitch(
            app_card,
            text="Auto Login"
        ).pack(anchor="w", padx=20, pady=5)

        ctk.CTkSwitch(
            app_card,
            text="Minimize To Tray"

        ).pack(anchor="w", padx=20, pady=5)
        ctk.CTkSwitch(
            app_card,
            text="Check for updates"
        ).pack(anchor="w", padx=20, pady=5)

        # dashboard_card
        dashboard_card = ctk.CTkFrame(
            setting_content,
            fg_color="#0F172A",
            corner_radius=15
        )
        dashboard_card.pack(
            fill="x",
            padx=20,
            pady=15
        )
        ctk.CTkLabel(
            dashboard_card,
            text="Dashboard Preferences",
            font=("arial", 18, "bold")
        ).pack(anchor="w", padx=20, pady=10)

        # DROP down menu
        ctk.CTkOptionMenu(
            dashboard_card,
            values=[
                "overview",
                "Complaints",
                "Reports"
            ]
        ).pack(anchor="w", padx=20, pady=10)

        # data card
        data_card = ctk.CTkFrame(
            setting_content,
            fg_color="#0F172A",
            corner_radius=15
        )
        data_card.pack(fill="x", padx=20, pady=10)
        ctk.CTkLabel(
            data_card,
            text="Data Managment",
            font=("arial", 18, "bold")
        ).pack(anchor="w", padx=20, pady=10)

        # buttons
        ctk.CTkButton(
            data_card,
            text="clearcache",
            fg_color=BUTTON_COLOUR
        ).pack(anchor="w", padx=20, pady=5)
        ctk.CTkButton(
            data_card,
            text="Export Data",
            fg_color=BUTTON_COLOUR
        ).pack(anchor="w", padx=20, pady=5)

        # -----------------------------------------------------main HEADING



    # --------------------------------------------------------------------------------main frame

    # open register complain
    def open_reg_complaint():
        reg_complaint_window = ctk.CTkToplevel(home_pg)
        reg_complaint_window.configure(fg_color=BG_COLOR)
        reg_complaint_window.title("Register Complaint")
        reg_complaint_window.geometry("1000x700")
        reg_complaint_window.grab_set()

        def submit_complaint():
            name = name_entry.get()
            email = email_entry.get()
            phone = phone_entry.get()
            crime = crime_type.get()
            desc = description.get("1.0","end")

            cursor.execute("""
            INSERT INTO complaints
            (name_full,email,phone,crime_type,description_info,status_info)
            values (%s,%s,%s,%s,%s,%s)""",
                           (name,email,phone,crime,desc,"pending"))
            connection.commit()
            dash_board_cards()

            tree.delete(*tree.get_children())
            complaints = load_complaint()
            for row in complaints:
                tree.insert('', 'end', values=row)

            messagebox.showinfo(
                "success",
                "complaint Registered successful"
            )


        header = ctk.CTkLabel(
            reg_complaint_window,
            text = " 🛡️ Cyber Crime Report Filing",
            font=("arial",24,"bold"),
            text_color="white"
        )
        header.pack(pady=20)


        #main frame
        reg_main_frame = ctk.CTkFrame(
            reg_complaint_window,
            fg_color=BG_COLOR
        )
        reg_main_frame.pack(fill="both",expand="yes",padx=20,pady=10)

        #creating side bar
        reg_sidebar = ctk.CTkFrame(
            reg_main_frame,
            width = 300,
            fg_color=SIDEBAR_COLOUR
        )
        reg_sidebar.pack(side="left",fill="y",padx=10,pady=10)

        form_frame = ctk.CTkFrame(
            reg_main_frame,
            fg_color="#1E293B"
        )
        form_frame.pack(side="left",fill="both",expand="yes",padx=20,pady=10)

        #name entyr
        ctk.CTkLabel(
            form_frame,
            text="Full Name : "
        ).pack(anchor="w",padx=20,pady=(20,5))
        name_entry = ctk.CTkEntry(
            form_frame,
            width = 500
        )
        name_entry.pack(padx=20)
        #email
        reg_mail= ctk.CTkLabel(
            form_frame,
            text="Email Address : "
        )
        reg_mail.pack(anchor="w",padx=20,pady=(15,5))

        email_entry = ctk.CTkEntry(
            form_frame,
            width=500
        )
        email_entry.pack(padx=20)

        #phone number
        ctk.CTkLabel(
            form_frame,
            text= "Mobile Number : "
        ).pack(anchor="w",padx=20,pady=(15,5))
        phone_entry = ctk.CTkEntry(
            form_frame,
            width=500
        )
        phone_entry.pack(padx=20)

        #complaint drop box
        ctk.CTkLabel(
            form_frame,
            text="Type of Cyber Crime"
        ).pack(anchor="w",padx=20,pady=(15,5))
        crime_type = ctk.CTkOptionMenu(
            form_frame,
            values = ["Phishing",
        "UPI Fraud",
        "Identity Theft",
        "Social Media Scam",
        "Other"],
        width = 500)
        crime_type.pack(padx=20)


        #discripotion box
        ctk.CTkLabel(
            form_frame,
            text = "Incident Description"
        ).pack(anchor="w",padx=20,pady=(15,5))
        description = ctk.CTkTextbox(
            form_frame,
            width = 500,
            height = 120
        )
        description.pack(padx=20)
        #submit button
        submit_btn = ctk.CTkButton(
            form_frame,
            text="Submit",
            fg_color=BUTTON_COLOUR,
            hover_color=BUTTON_HOVER,
            width=200,
            height=40,
            command=submit_complaint
        )
        submit_btn.pack(pady=25)












        regcomplain_btn = ctk.CTkButton(
            reg_sidebar,
            text="📝Register Complaint",
            fg_color=BUTTON_COLOUR,
            hover_color=BUTTON_HOVER,
            height=40,
            width=180,

        )
        regcomplain_btn.pack(pady=5)


        def go_dashboard():
            reg_complaint_window.destroy()

        dashboard_btn = ctk.CTkButton(
            reg_sidebar,
            text="📊 Dashboard",
            fg_color=BUTTON_COLOUR,
            hover_color=BUTTON_COLOUR, height=40,
            width=180,
            command=go_dashboard

        )
        dashboard_btn.pack(pady=5)

        viewcomplain_btn = ctk.CTkButton(
            reg_sidebar,
            text="👁️ View Complaint",
            fg_color=BUTTON_COLOUR,
            hover_color=BUTTON_HOVER, height=40,
            width=180
        )
        viewcomplain_btn.pack(pady=5)









        settings_btn = ctk.CTkButton(
            reg_sidebar,
            text="⚙️ Settings",
            fg_color=BUTTON_COLOUR,
            hover_color=BUTTON_HOVER, height=40,
            width=180,
            command=open_setting
        )
        settings_btn.pack(pady=5)

        help_btn = ctk.CTkButton(
            reg_sidebar,
            text="👤 Help",
            fg_color=BUTTON_COLOUR,
            hover_color=BUTTON_HOVER, height=40,
            width=180
        )
        help_btn.pack(pady=5)

        bot_btn = ctk.CTkButton(
            reg_sidebar,
            text="🤖 CYBE.. bot",
            fg_color=BUTTON_COLOUR,
            hover_color=BUTTON_HOVER, height=40,
            width=180
        )
        bot_btn.pack(pady=5)

    #buttons

    regcomplain_btn = ctk.CTkButton(
        sidebar,
        text="📝Register Complaint",
        fg_color=BUTTON_COLOUR,
        hover_color=BUTTON_HOVER,
        height=40,
        width=180,
        command=open_reg_complaint,
    )
    regcomplain_btn.pack(pady=5)



    dashboard_btn = ctk.CTkButton(
        sidebar,
        text = "👁️ View Complaint",
        fg_color=BUTTON_COLOUR,
        hover_color=BUTTON_COLOUR,height=40,
        width=180

    )
    dashboard_btn.pack(pady=5)

    def open_view_complaint():
        import tkinter as tk
        from pydoc import text
        from tkinter import ttk
        import customtkinter as ctk
        from PIL.ImageOps import expand

        BACKGROUNG = "#0D1117"
        CARD_COOUR = "#161B22"
        ACCENT = "#00C853"
        TEXT = "WHITE"

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")

        dashboard = ctk.CTkToplevel(home_pg)
        dashboard.title("ICCMS Dashboard")
        dashboard.geometry("1366x768")

        # creating main container

        bo_main_frame = ctk.CTkFrame(
            dashboard,
            fg_color=CARD_COOUR,
        )
        bo_main_frame.pack(fill="both", expand=True)

        bo_side_bar = ctk.CTkFrame(
            bo_main_frame,
            width=200,
            corner_radius=0,
            fg_color="#0A0F0D"
        )
        bo_side_bar.pack(side="left", fill="y")
        bo_side_bar.pack_propagate(False)

        bo_logo = ctk.CTkLabel(
            bo_side_bar,
            text="ICCMS",
            font=("arial", 32, "bold"),
            text_color="#00C853"
        )
        bo_logo.pack(pady=40)

        bo_menu = [
            "Dashboard",
            "Complaints",
            "Cases",
            "Users",
            "Reports",
            "Analysis",
            "Settings",
            "Profile",
            "Logout"
        ]
        for i in bo_menu:
            btn = ctk.CTkButton(
                bo_side_bar,
                text=i,
                height=45
            )
            btn.pack(fill="x", padx=15, pady=5)

        # content area
        bo_content = ctk.CTkFrame(
            bo_main_frame,
            fg_color="transparent",
        )
        bo_content.pack(side="right", fill="both", expand=True)

        bo_header = ctk.CTkFrame(
            bo_content,
            fg_color="#1E293B",
            corner_radius=15,
            border_width=1,
            border_color="#3B82F6"
        )
        bo_header.pack(fill="x", padx=20, pady=10)
        bo_header.pack_propagate(False)
        # title
        bo_header_title = ctk.CTkLabel(
            bo_header,
            text="Integrated Cyber Crime Management System",
            font=("arial", 32, "bold"),
        )
        bo_header_title.pack(anchor="center", pady=(70,0))
        # admin
        bo_admin = ctk.CTkLabel(
            bo_header,
            text="Administration",
            font=("arial", 20)
        )
        bo_admin.pack(side="right", padx=20)

        # card_frame
        bo_card_frame = ctk.CTkFrame(
            bo_content,
            fg_color="transparent"
        )
        bo_card_frame.pack(fill="x", padx=20, pady=10)
        def cards_value():
            cursor.execute("""
            select count(*) from complaints""")
            total_comp = cursor.fetchone()[0]

            cursor.execute("""select count(*) from complaints where status_info = "resolved" """)
            resolved_comp = cursor.fetchone()[0]

            cursor.execute("""select count(*) from complaints where status_info = "pending" """)
            pending_comp = cursor.fetchone()[0]

            cursor.execute("""select count(*) from complaints where status_info = "investigation" """)
            inv_comp = cursor.fetchone()[0]

            return total_comp, resolved_comp, pending_comp, inv_comp

        total_comp, resolved_comp, pending_comp, inv_comp = cards_value()

        card1 = ctk.CTkFrame(
            bo_card_frame,
            width=250,
            height=120,
            fg_color="#1B263B",
            corner_radius=15,
            border_width=1,
            border_color="#2E4A62"
        )
        card1.pack(side="left", padx=10)
        card1.pack_propagate(False)
        card1_lable = ctk.CTkLabel(
            card1,
            text="📁 Total Cases",
            font=("arial", 18, "bold")
        )
        card1_lable.pack(pady=(20, 5))
        card1_value = ctk.CTkLabel(
            card1,
            text=str(total_comp),
            font=("arial", 32, "bold"),
            text_color="#00C853"
        )
        card1_value.pack()

        card2 = ctk.CTkFrame(
            bo_card_frame,
            width=250,
            height=120,
            fg_color="#1B263B",

            corner_radius=15,

            border_width=1,

            border_color="#2E4A62"
        )
        card2.pack(side="left", padx=10)
        card2.pack_propagate(False)
        card2_lable = ctk.CTkLabel(
            card2,
            text="✔ Resolved",
            font=("arial", 18, "bold")
        )
        card2_lable.pack(pady=(20, 5))
        card2_value = ctk.CTkLabel(
            card2,
            text=str(resolved_comp),
            font=("arial", 32, "bold"),
            text_color="#00C853"
        )
        card2_value.pack()

        card3 = ctk.CTkFrame(
            bo_card_frame,
            width=250,
            height=120,
            fg_color="#1B263B",

            corner_radius=15,

            border_width=1,

            border_color="#2E4A62"
        )
        card3.pack(side="left", padx=10)
        card3.pack_propagate(False)
        card3_lable = ctk.CTkLabel(
            card3,
            text="⏳ Pending",
            font=("arial", 18, "bold")
        )
        card3_lable.pack(pady=(20, 5))
        card3_value = ctk.CTkLabel(
            card3,
            text=str(pending_comp),
            font=("arial", 32, "bold"),
            text_color="#00C853"
        )
        card3_value.pack()

        card4 = ctk.CTkFrame(
            bo_card_frame,
            width=250,
            height=120,
            fg_color="#1B263B",

            corner_radius=15,

            border_width=1,

            border_color="#2E4A62"
        )
        card4.pack(side="left", padx=10)
        card4.pack_propagate(False)
        card4_lable = ctk.CTkLabel(
            card4,
            text="🔍 Investigation",
            font=("arial", 18, "bold")
        )
        card4_lable.pack(pady=(20, 5))
        card4_value = ctk.CTkLabel(
            card4,
            text=str(inv_comp),
            font=("arial", 32, "bold"),
            text_color="#00C853"
        )
        card4_value.pack()

        # chart frame
        chart_frame = ctk.CTkFrame(
            bo_content,
            fg_color="transparent",
            height=350
        )
        chart_frame.pack(fill="x", padx=20, pady=10)
        chart_frame.pack_propagate(False)

        from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
        from matplotlib.figure import Figure

        def get_crime_data():
            cursor.execute("""
            select crime_type,count(*) from complaints group by crime_type order by count(*) desc""")
            return cursor.fetchall()

        # barchart

        bar_frame = ctk.CTkFrame(
            chart_frame,
            width=850,
            height=350,
            fg_color="#1B263B",  # lighter than background
            corner_radius=20,
            border_width=1,
            border_color="#2E4A62"
        )
        bar_frame.pack(side="left", fill="both", expand=True, padx=(0, 10))
        bar_frame.pack_propagate(False)
        ctk.CTkLabel(
            bar_frame,
            text="Most Type Of Crimes",
            font=("arial", 22, "bold"),
            text_color="#00C853"
        ).pack(pady=10)

        crime_data = get_crime_data()

        crime_names = [row[0] for row in crime_data]
        crime_counts = [row[1] for row in crime_data]

        fig = Figure(figsize=(8, 3), dpi=100)

        ax = fig.add_subplot(111)
        fig.patch.set_facecolor("#161B22")
        ax.set_facecolor("#161B22")
        ax.set_title(
            "Crime Categories",
            color="white",
            fontsize=14
        )

        ax.set_ylabel(
            "Complaints",
            color="white"
        )

        ax.tick_params(
            axis='x',
            colors='white'
        )

        ax.tick_params(
            axis='y',
            colors='white'
        )
        ax.spines['bottom'].set_color("#00C853")
        ax.spines['left'].set_color("#00C853")

        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.grid(
            color="#2D3748",
            linestyle="--",
            alpha=0.5
        )

        ax.bar(
            crime_names,
            crime_counts,
            width=0.45,
            color="#00C853",
            edgecolor="#00E676"
        )

        ax.set_title("Crime Categories")
        ax.set_ylabel("Number of Complaints")

        fig.tight_layout()

        canvas = FigureCanvasTkAgg(
            fig,
            master=bar_frame
        )

        canvas.draw()

        canvas.get_tk_widget().pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        def update_chart():

            crime_data = get_crime_data()

            crime_names = [row[0] for row in crime_data]
            crime_counts = [row[1] for row in crime_data]

            ax.clear()

            ax.bar(crime_names, crime_counts)

            ax.set_title("Crime Categories")
            ax.set_ylabel("Number of Complaints")

            canvas.draw()
            connection.commit()
            update_chart()

        def get_status_data():
            cursor.execute("""
                SELECT status_info, COUNT(*)
                FROM complaints
                GROUP BY status_info
            """)
            return cursor.fetchall()



        status_data = get_status_data()

        status_names = [row[0] for row in status_data]
        status_counts = [row[1] for row in status_data]
        # pie_chart frame
        pie_frame = ctk.CTkFrame(
            chart_frame,
            width=380,
            height=350,
            fg_color="#1B263B",
            corner_radius=20,
            border_width=1,
            border_color="#2E4A62"
        )
        pie_frame.pack(side="right")
        pie_frame.pack_propagate(False)
        ctk.CTkLabel(
            pie_frame,
            text="Case Status Overview",
            font=("arial", 22, "bold"),
            text_color="#00C853"
        ).pack(pady=10)
        status_data = get_status_data()

        status_names = [row[0] for row in status_data]
        status_counts = [row[1] for row in status_data]
        from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
        from matplotlib.figure import Figure

        pie_fig = Figure(figsize=(4.8,4.2), dpi=100)

        pie_ax = pie_fig.add_subplot(111)

        colors = [
            "#00C853",
            "#2563EB",
            "#F59E0B",
            "#EF4444"
        ]

        pie_ax.pie(
            status_counts,
            labels=status_names,
            autopct="%1.1f%%",
            startangle=90,
            colors=colors,
            radius=1.15,
            textprops={"color": "white"}
        )
        pie_fig.patch.set_facecolor("#161B22")
        pie_ax.set_facecolor("#161B22")
        pie_ax.set_title(
            "Complaint Status",
            color="white",
            fontsize=14
        )

        pie_ax.set_title("Complaint Status")

        pie_canvas = FigureCanvasTkAgg(
            pie_fig,
            master=pie_frame
        )

        pie_canvas.draw()

        pie_canvas.get_tk_widget().pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        # table_frame
        table_frame = ctk.CTkFrame(
            bo_content,
            fg_color="#1B263B",
            corner_radius = 20,
            border_width = 1,
            border_color = "#2E4A62"
        )
        table_frame.pack(fill="both", expand=True, padx=20, pady=15)

        columns = (
            "ID",
            "Name",
            "Crime",
            "Status",
            "Priority",
            "Date"
        )

        table = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings"
        )

        for col in columns:
            table.heading(col, text=col)
            table.column(col, anchor="center")

        table.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

#------------------------------------------------------------------------
    viewcomplain_btn = ctk.CTkButton(
        sidebar,
        text = "📊 Dashboard",
        fg_color=BUTTON_COLOUR,
        hover_color=BUTTON_HOVER,height=40,
        width=180,
        command=open_view_complaint
    )
    viewcomplain_btn.pack(pady=5)

    settings_btn = ctk.CTkButton(
        sidebar,
        text = "⚙️ Settings",
        fg_color=BUTTON_COLOUR,
        hover_color=BUTTON_HOVER,height=40,
        width = 180,
        command=open_setting
    )
    settings_btn.pack(pady=5)

    help_btn = ctk.CTkButton(
        sidebar,
        text = "👤 Help",
        fg_color=BUTTON_COLOUR,
        hover_color=BUTTON_HOVER,height=40,
        width = 180
    )
    help_btn.pack(pady=5)

    bot_btn = ctk.CTkButton(
        sidebar,
        text="🤖 CYBE.. bot",
        fg_color=BUTTON_COLOUR,
        hover_color=BUTTON_HOVER,height=40,
        width=180,
        command=open_bot
    )
    bot_btn.pack(pady=5)

    #center frame
    center_frame = ctk.CTkFrame(
        main_frame,
        fg_color=BG_COLOR
    )
    center_frame.pack(
        side="left",
        fill="both",
        expand="yes",
        padx=10,
        pady=10
    )

    #heading
    heading = ctk.CTkLabel(
        center_frame,
        text = "🛡️View Complaint Status",
        font=("arial",28,"bold")
    )
    heading.pack(pady=20)

    card_db = ctk.CTkFrame(
        center_frame,
        fg_color=BG_COLOR
    )
    card_db.pack(fill="x",pady=40)

    resolved_card = ctk.CTkFrame(
        card_db,
        width = 180,
        height = 140,
        fg_color="#1E293B"
    )
    resolved_card.pack(side = "left",padx=10)

    resolved_label = ctk.CTkLabel(
        resolved_card,
        text = "\n\n0 Resolved",
        font=("arial",19,"bold")
    )
    resolved_label.place(relx=0.5,rely=0.5,anchor="center")

    high_card = ctk.CTkFrame(
        card_db,
        width = 180,
        height = 140,
        fg_color="#1E293B"
    )
    high_card.pack(side = "left",padx=10)
    pending_label = ctk.CTkLabel(
        high_card,
        text = "\n\n0 pending",
        font=("arial",19,"bold")
    )
    pending_label.place(relx=0.5,rely=0.5,anchor="center")

    open_card = ctk.CTkFrame(
        card_db,
        width = 180,
        height = 140,
        fg_color="#1E293B"
    )
    open_card.pack(side = "left",padx=10)


    total_label = ctk.CTkLabel(
        open_card,
        text = "\n\n0 total",
        font=("arial",19,"bold")
    )
    total_label.place(relx=0.5,rely=0.5,anchor="center")
    dash_board_cards()

    def search_id():
        complaint_id = search_box.get().strip()

        if complaint_id == "":
            return

        for item in tree.get_children():

            values = tree.item(item, "values")

            if str(values[0]) == complaint_id:
                tree.selection_set(item)  # Select row
                tree.focus(item)  # Focus row
                tree.see(item)  # Scroll to row

                # Trigger details display
                show_details(None)

                return

        messagebox.showinfo(
            "Not Found",
            "Complaint ID not found"
        )

    search_box = ctk.CTkEntry(
        center_frame,
        width= 500,
        height= 40,
        placeholder_text= "Search Complaint ID...",
        corner_radius=15

    )
    search_box.bind("<Return>", lambda event: search_id())
    search_box.pack(anchor="w",padx=20,pady=20)

    import pandas as pd
    from tkinter import ttk

    data = {
        "ID": [1001, 1002, 1003],
        "Type": ["Phishing", "UPI Fraud", "Social Media Scam"],
        "Status": ["Pendng", "Invistigation", "Resolved"]
    }
    df = pd.DataFrame(data)

    #recent complain panel
    recent_comp = ctk.CTkFrame(
        center_frame,
        width = 1100,
        height = 450,
        fg_color="#1E293B",
        corner_radius=15
    )
    recent_comp.pack(padx=10,pady=(80,0))
    recent_comp.pack_propagate(False)

    recent_comptitle = ctk.CTkLabel(
        recent_comp,
        text = "Recent Complaints",
        font=("arial",18,"bold")
    )
    recent_comptitle.pack(pady=10)

    style = ttk.Style()
    style.theme_use("default")
    style.configure("Treeview",
                    background="#1E293B",
                    foreground="white",
                    fieldbackground="#1E293B",
                    rowheight=30,
                    font = ("arial",11))
    style.configure("Treeview.heading",
                    background="#16213E",
                    foreground="white",
                    font = ("arial",12,"bold"))
    style.map("Treeview",
              background=[
                  ("selected","#2563EB")
              ]
              )

    #tree view

    tree = ttk.Treeview(
        recent_comp,
        columns = ("ID", "Type", "Status"),
        show = "headings",
        height = 8,
    )
    tree.heading("ID", text = "Complaint ID")
    tree.heading("Type", text = "Complaint Type")
    tree.heading("Status", text = "Complaint Status")

    tree.column("ID",width=120)
    tree.column("Type",width=350)
    tree.column("Status",width=150)



    def show_details(event):

        selected = tree.focus()

        if not selected:
            return

        values = tree.item(selected, "values")

        complaint_id = values[0]

        cursor.execute("""
        SELECT
            complaint_id,
            name_full,
            email,
            phone,
            crime_type,
            status_info,
            description_info
        FROM complaints
        WHERE complaint_id=%s
        """, (complaint_id,))

        row = cursor.fetchone()

        if row:
            id_label.configure(
                text=f"Complaint ID : {row[0]}"
            )

            name_label.configure(
                text=f"Name : {row[1]}"
            )

            email_label.configure(
                text=f"Email : {row[2]}"
            )

            phone_label.configure(
                text=f"Phone : {row[3]}"
            )

            crime_type_lable.configure(
                text=f"Crime Type : {row[4]}"
            )

            status_lable.configure(
                text=f"Status : {row[5]}"
            )

            description_label.configure(
                text=f"Description :\n{row[6]}"
            )

    tree.pack(fill="both", expand="yes", padx=20, pady=10)
    tree.bind(
        "<<TreeviewSelect>>",
        show_details)

    complaints = load_complaint()
    for row in complaints:
        tree.insert("","end",values = row)

    detail_frame = ctk.CTkFrame(
        center_frame,
        width = 330,
        height = 350,
        fg_color="#1E293B",
        corner_radius=15
    )
    detail_frame.place(x=650,y=80)
    detail_frame.pack_propagate(False)


    detail_label = ctk.CTkLabel(
        detail_frame,
        text = "Complaint Details",
        font=("arial",20,"bold")
    )
    detail_label.pack(pady=15)

    id_label = ctk.CTkLabel(detail_frame,text = "Complaint ID : ")
    id_label.pack(anchor= "w",padx=15,pady=5)

    name_label = ctk.CTkLabel(detail_frame,text = "Name : ")
    name_label.pack(anchor= "w",padx=15,pady=5)

    email_label = ctk.CTkLabel(detail_frame,text = "Email : ")
    email_label.pack(anchor= "w",padx=15,pady=5)

    phone_label = ctk.CTkLabel(detail_frame,text = "Phone Number : ")
    phone_label.pack(anchor= "w",padx=15,pady=5)

    crime_type_lable = ctk.CTkLabel(detail_frame,text = "Crime Type : ")
    crime_type_lable.pack(anchor= "w",padx=15,pady=5)

    status_lable = ctk.CTkLabel(detail_frame,text = "Status : ")
    status_lable.pack(anchor= "w",padx=15,pady=5)

    description_label = ctk.CTkLabel(detail_frame,text = "Description : ",wraplength=250,justify="left")
    description_label.pack(anchor= "w",padx=15,pady=5)

    button_card = ctk.CTkFrame(
        center_frame,
        width=200,
        height=350,
        fg_color="#1E293B",
        corner_radius=15
    )
    button_card.place(x=1000, y=80)
    button_card.pack_propagate(False)
    button_lable = ctk.CTkLabel(
        button_card,
        text = "Editor",
        font=("arial", 17, "bold")
    )
    button_lable.pack(pady=15)

    update_btn = ctk.CTkButton(
        button_card,
        text="✏ Update",
        width=140
    )
    update_btn.pack(pady=8)

    resolve_btn = ctk.CTkButton(
        button_card,
        text="✔ Resolve",
        width=140,
        fg_color="green"
    )
    resolve_btn.pack(pady=8)

    delete_btn = ctk.CTkButton(
        button_card,
        text="🗑 Delete",
        width=140,
        fg_color="red"
    )
    delete_btn.pack(pady=8)

    refresh_btn = ctk.CTkButton(
        button_card,
        text="🔄 Refresh",
        width=140
    )
    refresh_btn.pack(pady=8)


#email
def login():
    email = email_entry.get()
    password = password_entry.get()
    if not email or not password:
        messagebox.showwarning(
            "Warning",
            "Please enter Email and Password"
        )

    elif email == "cy" and password == "2255":
        messagebox.showinfo(
            "Success",
            "Admin Access Granted"
        )
        open_h()


    else:
        messagebox.showerror(
            "Failed",
            "Invalid Credentials"
        )


email_entry = ctk.CTkEntry(
    card,
    width=300,
    height=40,
    placeholder_text="Enter Your Email",
    corner_radius=20
)
email_entry.pack(anchor="w",padx=50 ,pady=(20,5))

password_entry = ctk.CTkEntry(
    card,
    width=300,
    height=40,
    placeholder_text="Enter Your Password",show = "*",
    corner_radius=20
)
password_entry.pack(pady=(10,10))

#chekbox

remember = ctk.CTkCheckBox(
    card,
    text="Remember me"
)
remember.pack(pady=(10,10))

#login button
login_btn = ctk.CTkButton(
    card,
    text = "Login",
    width = 150,
    height = 35,
    fg_color = "#5B5EF7",
    hover_color = "#7073FF",
    corner_radius = 20,
    command=login
)
login_btn.pack(pady=(10,10))

#divider
divider = ctk.CTkLabel(
    card,
    text="____________________ or ____________________"
)
divider.pack(pady=(10,10))

#google_btn
google_btn = ctk.CTkButton(
    card,
    image= google_icon,
    compound="left",
    text = "Login with Google",
    width = 250,
    height = 35,
    fg_color = "transparent",
    border_width = 1
)

facebook_btn = ctk.CTkButton(
    card,
    text = "Login with Facebook",
    image= facebook_icon,
    compound="left",
    width = 250,
    height = 35,
    fg_color = "transparent",
    border_width = 1
)

apple_btn = ctk.CTkButton(
    card,
    image= apple_icon,
    compound="left",
    text = "Login with Apple ID",
    width = 250,
    height = 35,
    fg_color = "transparent",
    border_width = 1
)
google_btn.pack(pady=(10,7))
facebook_btn.pack(pady=(7,7))
apple_btn.pack(pady=(7,10))



#signip text
signup_text = ctk.CTkLabel(
    card,
    text="Don't Have an Account ? Signup",
)
signup_text.pack(pady=(0,10))






app.mainloop()
```