import yagmail
import os
from dotenv import load_dotenv

def first_appreciation_mail(email_address, name):
    yag = yagmail.SMTP("celebeindia@gmail.com", os.getenv("INDIA_GMAIL_PASSWORD"))

    html_msg = f"""
    <strong>Dear {name},</strong>

    We, the CELEBe India team, would like to welcome you to our CELEBe app and thank you for joining us.
    We recognized you and would like to appreciate your efforts and unique videos, which you uploaded to our app a few days ago.&nbsp;
    <strong>Your first video upload paved the way for your success on our app and you&rsquo;re becoming a celebrity.</strong>&nbsp;
    Stay tuned with us and keep uploading your exquisite content like videos and photos on the CELEBe app, and we will stride towards showcasing your videos as our priority on the recommendation board.
    
    <strong>As you already know, for each video that you upload, like, share, and get comments on, you are going to win reward points for it.</strong>&nbsp;
    The creativity, insight, and commitment you presented through your content have no doubt remarkably enriched our platform. This led to enhancing the overall experience for all our users. We want you to know how much we value your contributions and your passion for creating such high-quality videos.
    
    Thus, there&rsquo;s some great news for you! We are currently working on adjusting our recommendation algorithm for our recommendation feed.&nbsp;<strong>The changes will ensure that creators like you, who consistently deliver fantastic content, receive the visibility they deserve.</strong>&nbsp;This way, you get recognition and discover new opportunities through your own videos.
    
    <strong>It&rsquo;s high time now!</strong>&nbsp;to share this great news with your families, friends, colleagues, followers, or anyone else who might be interested. Let them dive too into CELEBE&#39;s&nbsp; ocean of fresh and engaging new content, along with recognizing your talent.
    
    We are always striving to improve our platform and provide our creators like you with the best experience possible. If you have any questions or need assistance with anything, please do not hesitate to reply to this email.
    
    Please follow officialcelebeindia account on Instagram. Click at the link below.
    <a href="https://www.instagram.com/officialcelebeindia/" style="text-decoration:none"><span style="font-size:12pt"><span style="font-family:'Times New Roman'"><span style="color:#1155cc"><u>https://www.instagram.com/celebe_official/?hl=en</u></span></span></span></a>
    <a href="https://www.instagram.com/celebe_official/?hl=en" style="text-decoration:none"><span style="font-size:12pt"><span style="font-family:'Times New Roman'"><span style="color:#1155cc"><u>https://www.instagram.com/celebe_official/?hl=en</u></span></span></span></a>
    <a href="https://youtu.be/0IrG7MuSmBg" style="text-decoration:none"><span style="font-size:11pt"><span style="font-family:Arial"><span style="color:#1155cc"><span style="background-color:#ffffff"><u>https://youtu.be/0IrG7MuSmBg</u></span></span></span></span></a>
    
    Once again, thank you for your significant contributions. We are excited to feature your work on our priority list!
    
    Warm Regards,&nbsp;💕
    <strong>Celebe India Team</strong>
    """

    yag.send(email_address, "Welcome to CELEBe India!", html_msg)
