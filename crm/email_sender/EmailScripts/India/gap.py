import yagmail
def gap_mail(email_address, nickname):
    yag = yagmail.SMTP("celebeindia@gmail.com", "kornrorckntdslzz")
    html_msg = f"""
    <span style="font-size:13.999999999999998pt"><span style="font-family:'Times New Roman'"><span style="color:#222222"><strong><em>Dear {nickname},</em></strong></span></span></span>

<span style="font-size:13.999999999999998pt"><span style="font-family:'Times New Roman'"><span style="color:#252525">We hope this mail finds you happy and healthy. We recognized you and would like to appreciate your efforts and unique videos, which you uploaded to our app a few days ago.&nbsp;</span></span></span>
<span style="font-size:13.999999999999998pt"><span style="font-family:'Times New Roman'"><span style="color:#252525"><strong><em>Your first video upload paved the way for your success on our app!</em></strong></span></span></span>

<span style="font-size:13.999999999999998pt"><span style="font-family:'Times New Roman'"><span style="color:#252525">Thus, we would like to share with you that we have been missing your videos on our platform since your&nbsp;first video upload.</span></span></span><span style="font-size:13.999999999999998pt"><span style="font-family:'Times New Roman'"><span style="color:#252525"><strong><em>&nbsp;All our users are missing your content too!!</em></strong></span></span></span><span style="font-size:13.999999999999998pt"><span style="font-family:'Times New Roman'"><span style="color:#252525"><strong>&nbsp;</strong></span></span></span><span style="font-size:13.999999999999998pt"><span style="font-family:'Times New Roman'"><span style="color:#222222">If there</span></span></span><span style="font-size:13.999999999999998pt"><span style="font-family:'Times New Roman'"><span style="color:#222222"><strong>&nbsp;</strong></span></span></span><span style="font-size:13.999999999999998pt"><span style="font-family:'Times New Roman'"><span style="color:#222222">are any issues or discomforts which you have been facing currently, please update us.&nbsp;</span></span></span>

<span style="font-size:13.999999999999998pt"><span style="font-family:'Times New Roman'"><span style="color:#222222">Our mission is to provide a seamless experience for our&nbsp;app users like </span></span></span><span style="font-size:13.999999999999998pt"><span style="font-family:'Times New Roman'"><span style="color:#222222"><strong><em>you</em></strong></span></span></span><span style="font-size:13.999999999999998pt"><span style="font-family:'Times New Roman'"><span style="color:#222222">, who already set a </span></span></span><span style="font-size:13.999999999999998pt"><span style="font-family:'Times New Roman'"><span style="color:#222222"><strong><em>remark on our platform</em></strong></span></span></span><span style="font-size:13.999999999999998pt"><span style="font-family:'Times New Roman'"><span style="color:#222222">, thus your feedback would be always&nbsp;precious to us.</span></span></span>

<span style="font-size:13.999999999999998pt"><span style="font-family:'Times New Roman'"><span style="color:#222222"><strong><em>So, what are you waiting for?</em></strong></span></span></span><span style="font-size:13.999999999999998pt"><span style="font-family:'Times New Roman'"><span style="color:#222222">&nbsp;Get started with uploading your favourite videos again to the CELEBe App, and this time no doubt, you will win double reward points for all your shares, likes and comments.</span></span></span>

<span style="font-size:13.999999999999998pt"><span style="font-family:'Times New Roman'"><span style="color:#222222">Furthermore, you&#39;ll be rewarded for other user&#39;s liking your content as well. Sounds crazy right?</span></span></span>

<span style="font-size:13.999999999999998pt"><span style="font-family:'Times New Roman'"><span style="color:#222222">How about becoming a&nbsp;</span></span></span><span style="font-size:13.999999999999998pt"><span style="font-family:'Times New Roman'"><span style="color:#222222"><strong><em>CELEBRITY&nbsp;</em></strong></span></span></span><span style="font-size:13.999999999999998pt"><span style="font-family:'Times New Roman'"><span style="color:#222222">on&nbsp;</span></span></span><span style="font-size:13.999999999999998pt"><span style="font-family:'Times New Roman'"><span style="color:#222222"><strong><em>CELEBeIndia</em></strong></span></span></span><span style="font-size:13.999999999999998pt"><span style="font-family:'Times New Roman'"><span style="color:#222222">&nbsp;platform. Opportunity is knocking at your door. Grab it quickly!!</span></span></span>

<span style="font-size:13.999999999999998pt"><span style="font-family:'Times New Roman'"><span style="color:#222222">We are excited to feature your work on our Recommendation feed again!!</span></span></span>

<span style="font-size:13.999999999999998pt"><span style="font-family:'Times New Roman'"><span style="color:#222222">Best Regards,</span></span></span>

<span style="font-size:13.999999999999998pt"><span style="font-family:'Times New Roman'"><span style="color:#222222"><strong><em>Celebe India Team</em></strong></span></span></span>

&nbsp;
    """
    yag.send(email_address, "We Miss You!", html_msg)