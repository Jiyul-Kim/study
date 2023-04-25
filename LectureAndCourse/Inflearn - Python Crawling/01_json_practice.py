import json

# 네이버 뉴스에서, android 라는 키워드로 검색한 상품 리스트 결과
data = """
{
    "lastBuildDate": "Thu, 13 Apr 2023 13:05:35 +0900",
    "total": 29742,
    "start": 1,
    "display": 10,
    "items": [
        {
            "title": "조시큐리티, 악성코드 정밀 분석 솔루션 조샌드박스 v37 &apos;베릴&apos; 출시",
            "originallink": "http://www.itdaily.kr/news/articleView.html?idxno=213498",
            "link": "http://www.itdaily.kr/news/articleView.html?idxno=213498",
            "description": "이 밖에도 조샌드박스 v37 베릴은 △크롬 캐시 추출 기능을 추가해 피싱 탐지 기능 향상 △새로운 쿡북(Cookbook) 명령 추가 _JBDisableSampleRenaming() △안드로이드(<b>Android</b>)용 v3 시그니처 데이터 추가 △ISO 파일... ",
            "pubDate": "Thu, 13 Apr 2023 12:10:00 +0900"
        },
        {
            "title": "조시큐리티, 악성코드 정밀 분석 솔루션 조샌드박스 v37 &apos;베릴&apos; 선봬",
            "originallink": "http://www.koit.co.kr/news/articleView.html?idxno=111799",
            "link": "http://www.koit.co.kr/news/articleView.html?idxno=111799",
            "description": "이 밖에도 조샌드박스 v37 베릴은 △Chrome 캐시 추출 기능을 추가하여 피싱 탐지 기능 향상 △새로운 Cookbook 명령 추가 _JBDisableSampleRenaming △<b>Android</b>용 v3 시그니처 데이터 추가 △ISO 파일 지원 강화 △특정... ",
            "pubDate": "Thu, 13 Apr 2023 11:52:00 +0900"
        },
        {
            "title": "LG화학, 美지보와 바이오플라스틱 경쟁력 강화..&quot;2026년까지 바이오 프로필렌...",
            "originallink": "http://kpenews.com/View.aspx?No=2784714",
            "link": "http://kpenews.com/View.aspx?No=2784714",
            "description": "노국래 LG화학 석유화학사업본부장은 &quot;바이오 원료 중심의 사업 포트폴리오 강화로 미래 지속가능한 친환경 사업을 지속 확대해 나갈 것&quot;이라고 말했다./data/user/0/com.samsung.<b>android</b>.app.notes/files/clipdata/clipdata... ",
            "pubDate": "Thu, 13 Apr 2023 11:40:00 +0900"
        },
        {
            "title": "도서 플랫폼 제공 전자책 뷰어, 시각장애인에겐 &apos;그림의 떡&apos;",
            "originallink": "http://www.ablenews.co.kr/news/articleView.html?idxno=202814",
            "link": "http://www.ablenews.co.kr/news/articleView.html?idxno=202814",
            "description": "웹/<b>Android</b>/iOS)를 대상으로 시각장애인의 접근성 실태를 조사한 결과 전자책 뷰어에 대한 시각장애인의... <b>Android</b>/iOS에서는 제어버튼이 화면에 제공되지 않아 제어버튼이 제공되었음을 알기 어려웠고, 일부 버튼에... ",
            "pubDate": "Wed, 12 Apr 2023 18:34:00 +0900"
        },
        {
            "title": "Paid subscribers growing at a fast rate",
            "originallink": "http://www.businesskorea.co.kr/news/articleView.html?idxno=112700",
            "link": "http://www.businesskorea.co.kr/news/articleView.html?idxno=112700",
            "description": "and 3) release of the DearU Bubble app for <b>Android</b> smartphone users in China. We expect the number of paid subscribers to grow at a fast rate throughout the year, backed by: 1) effects of the... ",
            "pubDate": "Wed, 12 Apr 2023 18:16:00 +0900"
        },
        {
            "title": "넥슨, ‘블루 아카이브’ 공식 온라인 굿즈샵 ‘샬레 스토어’ 오픈",
            "originallink": "http://www.breaknews.com/959136",
            "link": "http://www.breaknews.com/959136",
            "description": "The 11 themes provided during the last year&apos;s anniversary recorded 130,000 cumulative downloads, and with this partnership, 22 free themes that can be used on <b>Android</b> and iOS devices will be sequentially released every... ",
            "pubDate": "Wed, 12 Apr 2023 17:52:00 +0900"
        },
        {
            "title": "How Samsung, Hyundai tackle the China dilemma",
            "originallink": "https://www.koreaherald.com/view.php?ud=20230412000589",
            "link": "https://n.news.naver.com/mnews/article/044/0000245278?sid=104",
            "description": "In the lower price segment, China&apos;s local brands such as Oppo, Xiaomi and Vivo -- all operating with <b>Android</b> -- hold an upper hand. As Samsung continues to struggle to secure its footing in the... ",
            "pubDate": "Wed, 12 Apr 2023 16:04:00 +0900"
        },
        {
            "title": "솔라나, 스마트폰 출시 임박에 시세 10% 이상 급등",
            "originallink": "https://www.khgames.co.kr/news/articleView.html?idxno=211774",
            "link": "https://www.khgames.co.kr/news/articleView.html?idxno=211774",
            "description": "&apos;모바일 지갑 어댑터(Mobile Wallet Adapter)&apos;, &apos;시드 볼트(Seed Vault&apos;), &apos;안드로이드용 솔라나 페이(Solana Pay for <b>Android</b>)&apos;는 &apos;솔라나 모바일 스택&apos;의 초기 기능으로 소개됐다. &apos;모바일 지갑 어댑터&apos;는 기존 안드로이드 앱에... ",
            "pubDate": "Wed, 12 Apr 2023 09:36:00 +0900"
        },
        {
            "title": "Google fined W42b for abusing market dominance",
            "originallink": "https://www.koreaherald.com/view.php?ud=20230411000626",
            "link": "https://n.news.naver.com/mnews/article/044/0000245234?sid=104",
            "description": "It is only downloadable on mobile devices with an <b>Android</b> operating system. Under shady... Google’s <b>Android</b> algorithm, according to the FTC. But the case is pending at the Seoul High Court, as... ",
            "pubDate": "Tue, 11 Apr 2023 15:33:00 +0900"
        },
        {
            "title": "[KH explains] Samsung Pay safe &apos;for now&apos; as Apple Pay enters Korea",
            "originallink": "https://www.koreaherald.com/view.php?ud=20230411000619",
            "link": "https://n.news.naver.com/mnews/article/044/0000245230?sid=104",
            "description": "&quot; Korea was never expected to be an easy market for Apple Pay, partly because more than 70 percent of smartphone users here use Samsung or <b>Android</b> devices, with iPhone users comprising less than... ",
            "pubDate": "Tue, 11 Apr 2023 15:26:00 +0900"
        }
    ]
}
"""

json_data = json.loads(data)
print(json_data['items'][0]['title'])
print(json_data['items'][0]['link'])