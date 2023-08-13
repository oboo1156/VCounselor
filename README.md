<u> **App About** </u>
*The app is about students/clients posting/sharing their problems and counsellors help them by commenting and dm'ing students
so basically only counsellors can dm u any other reply should be in the comment section
Client names will be anonymous to everyone else but counsellors and not even mere peer counsellors can know your full details
Details of client is confidential. Just like the Jodel app, anyone can share their story but what make our app different
is that you get counsellors who will talk to you and call you one on one to help you out and we get to see matured advise
from trained people and not just anyone*

Links: Home --> Counsellors(Main/Peers, Contact,site, book) -->  --> Topic Sort --> Everyday Talk/advice(html on sex edu, life, life after n before skuul)
Share/Post(login required)-->Funds(html sick, needy, hunger)

How do we generate money from this:
We get tipped off from serious psychology session
Counselling for non-KNUST undergrad students requires payment
The funding section
ads on site

to do:auto_now_add
change to datetimefield and add auto_now_add of client, counsellor,infact all models, and check at meeta and def to see if it wont create issues, null=true ✅
google_forms on what  to ask audience and make analysis before we create app
the comment reply def section

obstacle:auto_add
Like button(emoji form) and most likes button must go top
comment section must have a reply ✅
peer counsellors have a badge
ban profain words
award most engaging user
basic CRUD on post, comment, commentreply
chat section to talk to counsellors, payment required for nonKnust students
Share button
admin nice section
badge for active frequent user- AI
tackle these and the rest will be way easier: admin-crud-design(freeform)-chat-design(css)-datasetthatpredictwhetheryouhaveschizoorothermentalandthatufoseedoc-


before deployment:
uncomment unecessary comments on models



neccesary codes:
source venv/bin/activate
python manage.py
https://github.com/PacktPublishing/Django-3-by-Example
source /Users/a/PycharmProjects/socketproject/venv/bin/activate



later koraa:
booking section with counsellors
Face recognition to detect depression

Came Across New Knowledge:

1.It is common for developers to store comments in a database as it allows for easy retrieval and management of comments.
However, it is important to implement the comment section in a way that does not waste storage resources.Developers can
also consider using cloud-based solutions, such as Amazon S3 or Google Cloud Storage, to store comments or utilize
automated system that periodically removes older or irrelevant comments or implement a limit on the length of comments.

2.Asynchronous Server Gateway Interface(ASGI), is used specifically for services that are full duplex ie requires real-time
such as a chat app. it is used together with web socket. this ASGI is how python interacts with other servers. we also have
Web Server Gateway Interface(WSGI)is how python interacts with  servers such as http. these services aint real time. so
we consider ASGI in real-time apps and WSGI in non-real time apps. ASGI (Asynchronous Server Gateway Interface) and
WebSockets are related in that ASGI is commonly used to handle WebSockets connections in Python web applications.Django
web framework provides support for WebSockets connections via the Django Channels library, which is built on top of the ASGI specification

3. . Images used for the website's design (e.g., logos, background images) would be part of the static files, while 
user-uploaded images or images used as part of dynamic content would be classified as media files.

so basically, i learnt about the chat app with some video in ProVide so that i can implemenet it in myapp. so we continue
another day. the chat is a little complex than the rest of the features so after tackling that, i am set

4. as i followed github on using ssh to upload a repo, i encontered an error because i ddnt have the ssh key. so i wanted to
swith to using http, which i know is less secured but to save time and hectic correcting codes. and i chatgpt how to use remote http
instead of ssh and it gave me this- "  git remote set-url origin https://github.com/oboo1156/VCounselor.git
" which worked perfectly fine

occured to me on 25/7/23
left side bar for links
right  side bar for flyer/ads
the post should be deleted, even if im waiting on the edit
the box should have colours 

[https://www.kaggle.com/datasets/shariful07/student-mental-health]