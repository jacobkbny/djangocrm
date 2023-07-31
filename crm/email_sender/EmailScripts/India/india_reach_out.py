import yagmail
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
from dotenv import load_dotenv

load_dotenv()
def reach_out_mail(email_address, nickname):
    yag = yagmail.SMTP("celebeindia@gmail.com", os.getenv("INDIA_GMAIL_PASSWORD"))
    html_msg = f"""
    <span style="font-size:12pt"><span style="font-family:'Times New Roman'"><span style="color:#222222">Hello&nbsp;</span></span></span>
<span style="font-size:12pt"><span style="font-family:'Times New Roman'"><span style="color:#222222"><strong><em>Dear {nickname},&nbsp;</em></strong></span></span></span>
<span style="font-size:12pt"><span style="font-family:'Times New Roman'"><span style="color:#222222">We are from the CELEBe India.</span></span></span><br/>
<span style="font-size:12pt"><span style="font-family:'Times New Roman'"><span style="color:#222222">CELEBe is the market leader in Korea&rsquo;s short-form service, where a wide diversity of content is produced and communicated with users.</span></span></span>
<span style="font-size:12pt"><span style="font-family:'Times New Roman'"><span style="color:#222222">We have been following and observing you for a while on your social media platforms, and we must say that we are impressed with your unique content and engaging profile.</span></span></span><br/>
<span style="font-size:12pt"><span style="font-family:'Times New Roman'"><span style="color:#222222">How about giving recognition and popularity to your short videos?&nbsp;</span></span></span>
<span style="font-size:12pt"><span style="font-family:'Times New Roman'"><span style="color:#222222">Do you want to make your videos famous? Then CELEBe is the right platform to jump on and grab this rare opportunity knocking on your door!</span></span></span>
<span style="font-size:12pt"><span style="font-family:'Times New Roman'"><span style="color:#222222">So, here we&#39;d like to offer you the opportunity to upload your videos to CELEBe. For every video you upload, view, like, and share, you&rsquo;ll get a chance to earn points in the CELEBe Application.</span></span></span><br/>
<span style="font-size:12pt"><span style="font-family:'Times New Roman'"><span style="color:#222222"><strong><em>Sign Up for the CELEBe app for FREE</em></strong></span></span></span><span style="font-size:12pt"><span style="font-family:'Times New Roman'"><span style="color:#222222"><strong>.</strong></span></span></span><span style="font-size:12pt"><span style="font-family:'Times New Roman'"><span style="color:#222222"> During registration in the CELEBe App, you will get a chance to choose any nickname of your choice. Once registered, please let us know.&nbsp;</span></span></span>
<span style="font-size:12pt"><span style="font-family:'Times New Roman'"><span style="color:#222222"><strong><em>We will showcase your short videos for our </em></strong></span></span></span><span style="font-size:12pt"><span style="font-family:'Times New Roman'"><span style="color:#222222"><strong><em><u>Daily Recommendations&rsquo; Feed!</u></em></strong></span></span></span><br/>
<span style="font-size:12pt"><span style="font-family:'Times New Roman'"><span style="color:#222222">You can re-upload your existing videos, and your video will be exposed to our CELEBe global platform to </span></span></span><span style="font-size:12pt"><span style="font-family:'Times New Roman'"><span style="color:#252525">India, Philippines, Indonesia, Thailand, Vietnam, UK, and Korea</span></span></span><span style="font-size:12pt"><span style="font-family:'Times New Roman'"><span style="color:#222222">.</span></span></span>
<span style="font-size:12pt"><span style="font-family:'Times New Roman'"><span style="color:#222222"><strong><em>This global exposure will help you to maximise followers, views, and engagements for your profile.</em></strong></span></span></span><br/>
<span style="font-size:12pt"><span style="font-family:'Times New Roman'"><span style="color:#222222">Still confused? look at </span></span></span><span style="font-size:12pt"><span style="font-family:'Times New Roman'"><span style="color:#222222"><strong>who we are!</strong></span></span></span>
<span style="font-size:12pt"><span style="font-family:'Times New Roman'"><span style="color:#222222">1. Expansion to 7 overseas countries (India, Indonesia, Thailand, Vietnam, the Philippines, the UK, etc.)</span></span></span>
<span style="font-size:12pt"><span style="font-family:'Times New Roman'"><span style="color:#222222">2. Campaign with the BLACKPINK Index (K-POP Superstar Band)</span></span></span>
<span style="font-size:12pt"><span style="font-family:'Times New Roman'"><span style="color:#222222">3. Supported JTBC&#39;s &quot;I Want to Be a Celebrity&quot; broadcast program</span></span></span>
<span style="font-size:12pt"><span style="font-family:'Times New Roman'"><span style="color:#222222">4. Partnered with Hollybang&#39;s Honey J, T1, etc. for exclusive CELEBe content</span></span></span>
<span style="font-size:12pt"><span style="font-family:'Times New Roman'"><span style="color:#222222">5. Official sponsorship with professional golfers Kim Ji-hyun, Park Jeol, Oh Ji-hyun, and Kim Jae-hee, for exclusive CELEBe content</span></span></span><br/>
<span style="font-size:12pt"><span style="font-family:'Times New Roman'"><span style="color:#222222"><strong><em>Now it&rsquo;s your turn to be the next CELEBe Celebrity!</em></strong></span></span></span>
<span style="font-size:12pt"><span style="font-family:'Times New Roman'"><span style="color:#222222">Soon we&#39;ll be launching some various campaigns featuring CELEBe Mega Models! Thus, before moving ahead, we want to assure you that we&#39;ve selected creators whose content are of high value and potential and deserves to be highlighted on our platform.</span></span></span><br/>
<span style="font-size:12pt"><span style="font-family:'Times New Roman'"><span style="color:#222222">Have you ever earned something just by watching and liking others&rsquo; videos? CELEBe is a platform that understands the value of time, so the viewer gets paid for it.</span></span></span>
<span style="font-size:12pt"><span style="font-family:'Times New Roman'"><span style="color:#222222">So, what are you waiting for?</span></span></span>
<span style="font-size:12pt"><span style="font-family:'Times New Roman'"><span style="color:#222222">Install the CELEBe App Now!! to get exposure to bigger platforms and be a popular creator!</span></span></span><br/>
<span style="font-size:12pt"><span style="font-family:'Times New Roman'"><span style="color:#222222">This is our CELEBe Korea Instagram Link You should check out :-</span></span></span>
<a href="https://www.instagram.com/officialcelebeindia/" style="text-decoration:none"><span style="font-size:12pt"><span style="font-family:'Times New Roman'"><span style="color:#1155cc"><u>https://www.instagram.com/celebe_official/?hl=en</u></span></span></span></a>
<a href="https://www.instagram.com/celebe_official/?hl=en" style="text-decoration:none"><span style="font-size:12pt"><span style="font-family:'Times New Roman'"><span style="color:#1155cc"><u>https://www.instagram.com/celebe_official/?hl=en</u></span></span></span></a>
<a href="https://youtu.be/0IrG7MuSmBg" style="text-decoration:none"><span style="font-size:11pt"><span style="font-family:Arial"><span style="color:#1155cc"><span style="background-color:#ffffff"><u>https://youtu.be/0IrG7MuSmBg</u></span></span></span></span></a><br/>
<span style="font-size:12pt"><span style="font-family:'Times New Roman'"><span style="color:#222222">Thanks and Regards,</span></span></span>
<span style="font-size:12pt"><span style="font-family:'Times New Roman'"><span style="color:#222222">CELEBe India Team</span></span></span><span style="font-size:12pt"><span style="font-family:Arial"><span style="color:#222222"><img alt="💕" src="https://lh6.googleusercontent.com/zWJShdnWPyU5heBInMAMXGbzg8Ch30lOqnx4Pp3KZOvi3lDdlufwyq8F0GWcB6h5MEcxEyULXMkmCCtPquj7jt2nkq1IQ3JYYjoO0Um3tiOygXgsBqzQJXuPQ3QVR9jBe8xkZs5V2jG9Ws0_mYIy2A" style="height:72px; width:72px" /></span></span></span>
        """
    yag.send(email_address, "Greetings from Celebe India!", html_msg)
    
    credentials = os.getenv("INDIA_CREDENTIAL")
    gc = gspread.service_account_from_dict(credentials)
    spreadsheet = gc.open('ReachOutTracker')
    worksheet = spreadsheet.get_worksheet(0)
    worksheet.append_row([nickname, email_address])