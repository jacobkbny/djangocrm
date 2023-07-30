import yagmail
import gspread
from oauth2client.service_account import ServiceAccountCredentials
def reach_out_mail(email_address, nickname):
    yag = yagmail.SMTP("celebeindia@gmail.com", "kornrorckntdslzz")
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
    
    credentials = {
  "type": "service_account",
  "project_id": "emailtracker-393823",
  "private_key_id": "dd5891be6a27a0282bf76dda9401affb1ffb397e",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDVU/zf2Im3AIyH\neBxQWDnBKS97DfSJ8DP9bHqck+o8Y8a5XNosmv7wP/dgEyyPsPXy8b968Ot3NTva\n2NYUFrKI6Y7hMuyDnn08YWz185dlvjK9BSAD8ldx3OiXnAnzIWf/FrEzwrGpToLu\n61QCrldvfxGBIKPGSitlHnk+SgfGi2UY6QHUFLyvKPB2wxrmF4dDRI7AmIsS8GRh\nkiNu1hHs2lqncT7ZWdT5oYjlGajATuqLRWLgpnODtjU7S4yxgCtMuk+GdqX7rSLe\nW/ddE3Hls9hmZ1LwibLOOVa7Uia8Sm6XLGSxoSAC3NyFmQZoxHWwVyTaNJA+Lzb0\nQtm1jxTZAgMBAAECggEACt0jmBy1arHm9jEqM/dCPbGEvv4HcYzfgOzo05d+ysOE\nB8WQQMxF5mNDjEt9rfWjmNMx3qdtPl1iJnN7d3tubSWDxrkqrUtBcnU9sMrOb3p/\np/ueVUUeqehHmgzyvsR5QNbdgFbOaGJcraEjXp2VS1LLx+krHfqB+jzSjNcFTVmN\nJtczibX8hNqj6AnCqd6Fm7zTNqN2CJH6K4iobLDWFW03Nnr0g02l6Oqf1A4Qg3Si\nIbzYu7SopM9/BidGzi6e/1IUoC6/AO1APvU6tlj+i9Huqf71flYCyOd703GDuh5M\nCEFbneC7xmssJCWFJTE5AirIroBttgVY3rH3sn3qlwKBgQDtefn5hwS9LijbJAId\n38cps7Vb+ZT9kOx8ayWN1uSy7Sa44adrujkQv3VeD8YPwb2fviuOG0NoiNscCx6k\nc6f+PRBEV/1hmmPhJNaRL5PgmF7RLWKGo4e6tbYPyHCxCMmwbvLKTb60ObjL99IQ\noNqbsCpBhByRyQN/oiFdZTu1KwKBgQDl986E6eHXyI2VGUBXELtBHzs2CkUfINSP\nrODLVhxXuunZ3dxPl7HMMxMkm0UOlI0a6MrxdFGkgWwomB/yhenhgxkTtr+XKzqE\nLDvnTZ8Z41Qlt9buBysSwcc4JoPKfMXNpbisW/UCkwe3yF3kMwp5SQWWua+Bs8uT\na4hHAezkCwKBgHFWW7V5eQuI8jrUTqZPXNBMUmwZC8CQ4CzpPj0ZqIC0qlxmZe8G\nK6IQnkVMJezzPDr3GfZykJNdbaVOsUsvX6f5IMBddjKU6sJTQIx+NodkcSxICtPT\nTD4R51hVA2OanBe2e+2NeUyul8HQ/tKs0minhSNLmA8D7sWFbYMTg5GNAoGAWBti\nR3AoM/lFrWs4SGNDqwahM+opY2y7o7RTh/Qc9cvKDsu+vcvbteWXnv3SLmzhxv6L\nyoiLQyDG5KKsEsoVum307KWmr+9DAyLDbLJDk7KSKcVOlnGuoggWIMA43BqD2m90\n2qx8qZjVaydcObMIf0Fn38CSqnnNNFUNqE7niNMCgYEA3SYVgw5sx+b9EHuKxUxj\njKEytOVlc19mn5qzFhN0/pOxkEV2r5bo7Z0USWQdAk7QqxyO9FsA/O8zaqTXXExt\nlMM1YB0GVELJ09N7htsBsxuPbEf0seELeMTnKcMNuRobketyoUeKDMLYmZkUuXyF\nSAYDhZco+1XBj/ZQ3ULIJx4=\n-----END PRIVATE KEY-----\n",
  "client_email": "emailtracker@emailtracker-393823.iam.gserviceaccount.com",
  "client_id": "118034276744647254656",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/emailtracker%40emailtracker-393823.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
    }
    gc = gspread.service_account_from_dict(credentials)
    spreadsheet = gc.open('ReachOutTracker')
    worksheet = spreadsheet.get_worksheet(0)
    worksheet.append_row([nickname, email_address])