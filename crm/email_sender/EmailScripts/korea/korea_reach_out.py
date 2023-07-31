import yagmail
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os 
from dotenv import load_dotenv
load_dotenv()
def korean_email(email_address, name):
    yag = yagmail.SMTP("martin@celebe.io", os.getenv("KOREAN_GMAIL_PASSWORD"))
    html_msg = f"""
           <span style="font-size:small"><span style="color:#222222"><span style="font-family:Arial,Helvetica,sans-serif"><span style="background-color:#ffffff"><span style="font-size:15px"><span style="color:#000000"><span style="font-family:Arial">안녕하세요 :-) {name}님!</span></span></span></span></span></span></span>
<span style="font-size:small"><span style="color:#222222"><span style="font-family:Arial,Helvetica,sans-serif"><span style="background-color:#ffffff"><span style="font-family:&quot;Google Sans&quot;,Roboto,RobotoDraft,Helvetica,Arial,sans-serif"><span style="font-family:Arial,Helvetica,sans-serif"><span style="font-size:15px"><span style="color:#000000"><span style="font-family:Arial"><strong>저희는 대한민국 숏폼 플랫폼,&nbsp;</strong></span></span></span><span style="font-size:15px"><span style="color:#000000"><span style="font-family:Arial"><strong>셀러비코리아&nbsp;</strong></span></span></span><span style="font-size:15px"><span style="color:#000000"><span style="font-family:Arial"><strong>입니다.</strong></span></span></span></span></span></span></span></span></span>
&nbsp;
<span style="font-size:small"><span style="color:#222222"><span style="font-family:Arial,Helvetica,sans-serif"><span style="background-color:#ffffff"><span style="font-family:&quot;Google Sans&quot;,Roboto,RobotoDraft,Helvetica,Arial,sans-serif"><span style="font-family:Arial,Helvetica,sans-serif"><span style="font-size:15px"><span style="color:#000000"><span style="font-family:Arial">수 많은 유튜버 분들의 다양한 컨텐츠를 관찰하던 중,{name}님 채널만의 개성있고 매력적인</span></span></span></span></span></span></span></span></span>
<span style="font-size:small"><span style="color:#222222"><span style="font-family:Arial,Helvetica,sans-serif"><span style="background-color:#ffffff"><span style="font-family:&quot;Google Sans&quot;,Roboto,RobotoDraft,Helvetica,Arial,sans-serif"><span style="font-family:Arial,Helvetica,sans-serif"><span style="font-size:15px"><span style="color:#000000"><span style="font-family:Arial">쇼츠들이 더 알려져야한다고 생각해 저희 셀러비 내 영상 업로드 제안을 드립니다.</span></span></span></span></span></span></span></span></span>


<span style="font-size:large"><span style="color:#222222"><span style="font-family:Arial,Helvetica,sans-serif"><span style="background-color:#ffffff"><strong><span style="color:#ff0000">셀러비 가입 후 계정 말씀주시면 지속적으로 추천 피드에&nbsp;</span></strong><strong><span style="color:#ff0000">{name}님의 영상들이 노출되도록 도와드리겠습니다!</span></strong></span></span></span></span>
<span style="font-size:small"><span style="color:#222222"><span style="font-family:Arial,Helvetica,sans-serif"><span style="background-color:#ffffff"><span style="font-size:15px"><span style="color:#000000"><span style="font-family:Arial">또한 활동을 하시다 C등급이 되시면 한국전파진흥협회을 통해</span></span></span></span></span></span></span>
<span style="font-size:small"><span style="color:#222222"><span style="font-family:Arial,Helvetica,sans-serif"><span style="background-color:#ffffff"><span style="font-size:15px"><span style="color:#000000"><span style="font-family:Arial">촬영 스튜디오 및 촬영장비에 대한 적극 지원을 해드리고 있습니다!</span></span></span></span></span></span></span>
<span style="font-size:small"><span style="color:#222222"><span style="font-family:Arial,Helvetica,sans-serif"><span style="background-color:#ffffff"><span style="font-size:15px"><span style="color:#000000"><span style="font-family:Arial">(자세한 사항은&nbsp;<a href="http://www.meplex.co.kr/" style="color:#1155cc" target="_blank">http://www.meplex.co.kr</a>&nbsp;에서 참고해주세요!)</span></span></span></span></span></span></span>
&nbsp;
<span style="font-size:small"><span style="color:#222222"><span style="font-family:Arial,Helvetica,sans-serif"><span style="background-color:#ffffff"><span style="font-size:15px"><span style="color:#000000"><span style="font-family:Arial">저희 셀러비에 대해서 간략히 설명을 드리자면</span></span></span></span></span></span></span>
<span style="font-size:small"><span style="color:#222222"><span style="font-family:Arial,Helvetica,sans-serif"><span style="background-color:#ffffff"><span style="font-size:15px"><span style="color:#000000"><span style="font-family:Arial">① 해외 7개국 진출(인도/인도네시아/태국/베트남/필리핀/영국 등)</span></span></span></span></span></span></span>
<span style="font-size:small"><span style="color:#222222"><span style="font-family:Arial,Helvetica,sans-serif"><span style="background-color:#ffffff"><span style="font-size:15px"><span style="color:#000000"><span style="font-family:Arial">② 블랙핑크 지수와 캠페인 진행 (2022년 6월)&nbsp;</span></span></span>&nbsp;<a href="https://youtu.be/0IrG7MuSmBg" style="color:#1155cc" target="_blank">https://youtu.be/0IrG7MuSmBg</a>&nbsp;&nbsp;</span></span></span></span>
<span style="font-size:small"><span style="color:#222222"><span style="font-family:Arial,Helvetica,sans-serif"><span style="background-color:#ffffff"><span style="font-size:15px"><span style="color:#000000"><span style="font-family:Arial">③ JTBC &#39;셀럽이 되고싶어&#39; 방송 프로그램 총 제작 지원</span></span></span></span></span></span></span>
<span style="font-size:small"><span style="color:#222222"><span style="font-family:Arial,Helvetica,sans-serif"><span style="background-color:#ffffff"><span style="font-size:15px"><span style="color:#000000"><span style="font-family:Arial">④ 홀리뱅의 허니제이, T1등 파트너십 체결, 독점 콘텐츠 진행 중</span></span></span></span></span></span></span>
<span style="font-size:small"><span style="color:#222222"><span style="font-family:Arial,Helvetica,sans-serif"><span style="background-color:#ffffff"><span style="font-size:15px"><span style="color:#000000"><span style="font-family:Arial">⑤ 김지현, 박결, 오지현, 김재희 프로골퍼와 공식 스폰서십 체결, 독점 콘텐츠 진행 중 입니다.</span></span></span></span></span></span></span>
&nbsp;
<span style="font-size:small"><span style="color:#222222"><span style="font-family:Arial,Helvetica,sans-serif"><span style="background-color:#ffffff"><span style="font-size:15px"><span style="color:#000000"><span style="font-family:Arial">2023년 하반기부터는 빅모델을 활용해 40억 비용의 대대적인 마케팅 캠페인을 진행할 예정이며 그 전에 미리</span></span></span></span></span></span></span>
<span style="font-size:small"><span style="color:#222222"><span style="font-family:Arial,Helvetica,sans-serif"><span style="background-color:#ffffff"><span style="font-size:15px"><span style="color:#000000"><span style="font-family:Arial">콘텐츠의 가치 및 가능성이&nbsp;</span></span></span><span style="font-size:15px"><span style="color:#000000"><span style="font-family:Arial">매우 높은&nbsp;</span></span></span><span style="font-size:15px"><span style="color:#000000"><span style="font-family:Arial">크리에이터 분들을&nbsp;</span></span></span><span style="font-size:15px"><span style="color:#000000"><span style="font-family:Arial">선정하여 저희 플랫폼의 활동을 권유드리고자 메일을 보내게 되었습니다. :-)</span></span></span></span></span></span></span>
<span style="font-size:small"><span style="color:#222222"><span style="font-family:Arial,Helvetica,sans-serif"><span style="background-color:#ffffff"><span style="font-size:15px"><span style="color:#000000"><span style="font-family:Arial">저희 셀러비는 영상을 업로드 하거나, 다른 사람의 영상을 보는 것 만으로도 무조건 수익이 발생합니다!</span></span></span></span></span></span></span>
<span style="font-size:small"><span style="color:#222222"><span style="font-family:Arial,Helvetica,sans-serif"><span style="background-color:#ffffff"><span style="font-size:15px"><span style="color:#000000"><span style="font-family:Arial">이미 쇼츠 영상을 다수 보유하고 있는 크리에이터분들께선 당연히 더 쉽고 빠르게 수익을 얻고 계십니다.</span></span></span></span></span></span></span>
<span style="font-size:small"><span style="color:#222222"><span style="font-family:Arial,Helvetica,sans-serif"><span style="background-color:#ffffff"><span style="font-size:15px"><span style="color:#000000"><span style="font-family:Arial">(쇼츠 및 타 플랫폼 영상들을 그대로 올려주셔도 무방합니다.)&nbsp;</span></span></span></span></span></span></span>
&nbsp;
<span style="font-size:small"><span style="color:#222222"><span style="font-family:Arial,Helvetica,sans-serif"><span style="background-color:#ffffff"><span style="font-size:15px"><span style="color:#000000"><span style="font-family:Arial"><strong>크리에이터님</strong></span></span></span><span style="font-size:15px"><span style="color:#000000"><span style="font-family:Arial"><strong>께서 저희 셀러비 앱에 계정을 만들고 영상을 업로드해 주신다면&nbsp;</strong></span></span></span></span></span></span></span>
&nbsp;
<span style="font-size:small"><span style="color:#222222"><span style="font-family:Arial,Helvetica,sans-serif"><span style="background-color:#ffffff"><span style="font-size:15px"><span style="color:#000000"><strong><span style="font-family:Arial">Step1. 콘텐츠, 해시태그 모두 100% 노출 &rarr; 조회 수 보장&nbsp;</span></strong></span></span></span></span></span></span>
<span style="font-size:small"><span style="color:#222222"><span style="font-family:Arial,Helvetica,sans-serif"><span style="background-color:#ffffff"><span style="font-size:15px"><span style="color:#000000"><strong><span style="font-family:Arial">① 업로드하는 모든 콘텐츠 추천 피드 및 추천 카테고리에 100% 노출&nbsp;</span></strong></span></span></span></span></span></span>
<span style="font-size:small"><span style="color:#222222"><span style="font-family:Arial,Helvetica,sans-serif"><span style="background-color:#ffffff"><span style="font-size:15px"><span style="color:#000000"><strong><span style="font-family:Arial">② 콘텐츠 업로드 시 #닉네임 등록 &rarr; 해시태그 100% 노출&nbsp;</span></strong></span></span></span></span></span></span>
<span style="font-size:small"><span style="color:#222222"><span style="font-family:Arial,Helvetica,sans-serif"><span style="background-color:#ffffff"><span style="font-size:15px"><span style="color:#000000"><strong><span style="font-family:Arial">③ 콘텐츠 업로드 시 #닉네임 등록 &rarr; 추천검색어 100% 노출</span></strong></span></span>&nbsp;</span></span></span></span>
&nbsp;
&nbsp;
<span style="font-size:small"><span style="color:#222222"><span style="font-family:Arial,Helvetica,sans-serif"><span style="background-color:#ffffff"><img alt="IMG_7074.png" class="CToWUd a6T" src="https://nftmassets.s3.ap-northeast-2.amazonaws.com/upload/IMG_7074.png" style="cursor:pointer; height:542px; outline:0px; width:250px" /><img alt="IMG_7077.png" class="CToWUd a6T" src="https://nftmassets.s3.ap-northeast-2.amazonaws.com/upload/IMG_7077.png" style="cursor:pointer; height:542px; outline:0px; width:250px" /><img alt="IMG_7080.png" class="CToWUd a6T" src="https://nftmassets.s3.ap-northeast-2.amazonaws.com/upload/IMG_7080.png" style="cursor:pointer; height:542px; outline:0px; width:250px" /></span></span></span></span>
&nbsp;
&nbsp;
<span style="font-size:small"><span style="color:#222222"><span style="font-family:Arial,Helvetica,sans-serif"><span style="background-color:#ffffff"><span style="font-size:15px"><span style="color:#000000"><strong><span style="font-family:Arial">Step2. 꾸준하게 활동(레벨 5 달성) 시 크리 등급(최상위등급) 부여 &rarr; 수익 무제한</span></strong></span></span></span></span></span></span>
<span style="font-size:small"><span style="color:#222222"><span style="font-family:Arial,Helvetica,sans-serif"><span style="background-color:#ffffff"><span style="font-size:15px"><span style="color:#000000"><strong><span style="font-family:Arial">Step3. 태국/베트남/필리핀/인도/인도네시아에서도 노출</span></strong></span></span></span></span></span></span>
<span style="font-size:small"><span style="color:#222222"><span style="font-family:Arial,Helvetica,sans-serif"><span style="background-color:#ffffff"><span style="font-size:15px"><span style="color:#000000"><strong><span style="font-family:Arial">Step4. 셀러비 모델 제안&nbsp;</span></strong></span></span></span></span></span></span>
&nbsp;
<span style="font-size:small"><span style="color:#222222"><span style="font-family:Arial,Helvetica,sans-serif"><span style="background-color:#ffffff"><span style="font-size:15px"><span style="color:#000000"><span style="font-family:Arial">또한 대규모 앱 기능 업데이트로 많은 이벤트들도 준비되어 있으니 기대해주세요.</span></span></span></span></span></span></span>
<span style="font-size:small"><span style="color:#222222"><span style="font-family:Arial,Helvetica,sans-serif"><span style="background-color:#ffffff"><span style="font-size:15px"><span style="color:#000000"><span style="font-family:Arial">해당 내용 확인해 보시고 셀러비와 함께 다양한 활동을 이어나가길 기다리겠습니다!</span></span></span></span></span></span></span>
&nbsp;
<span style="font-size:small"><span style="color:#222222"><span style="font-family:Arial,Helvetica,sans-serif"><span style="background-color:#ffffff"><span style="font-size:15px"><span style="color:#000000"><span style="font-family:Arial">감사합니다! :-)</span></span></span></span></span></span></span>
&nbsp;
    """
    yag.send(email_address, f"[셀러비코리아] {name}님, 안녕하세요! 영상들 잘 보고 연락드립니다. :-)", html_msg)
    credentials = os.getenv("KOREAN_CREDENTIAL")

    gc = gspread.service_account_from_dict(credentials)
    spreadsheet = gc.open('[유튜버] 크리에이터 컨택')
    worksheet = spreadsheet.get_worksheet(0)
    worksheet.append_row([name, email_address])
