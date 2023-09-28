init offset = 5




define -5 monika_random_topics = []
define -5 testitem = 0
define -5 numbers_only = "0123456789"
define -5 letters_only = "abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ"
define -5 mas_did_monika_battery = False


init -6 python:

    import store.songs as songs
    import store.evhand as evhand

    def remove_seen_labels(pool):
        
        
        
        
        
        
        
        
        for index in range(len(pool)-1, -1, -1):
            if renpy.seen_label(pool[index]):
                pool.pop(index)


    class MASTopicLabelException(Exception):
        def __init__(self, msg):
            self.msg = msg
        def __str__(self):
            return "MASTopicLabelException: " + self.msg

init 6 python:

    all_random_topics = Event.filterEvents(evhand.event_database,random=True,seen=False).keys()


    monika_random_topics = all_random_topics

    if len(monika_random_topics) == 0:
        
        random_seen_limit = 100
















init python:
    addEvent(Event(persistent.event_database,eventlabel='monika_god',
                                                            prompt="주식과 기도",
                                                            label=None,
                                                            category=['철학'],
                                                            random=True,
                                                            unlocked=False,
                                                            pool=False,
                                                            conditional=None,
                                                            action=None,
                                                            start_date=None,
                                                            end_date=None,
                                                            unlock_date=None
                                                            ))

label monika_god:
    m 1a "[player], 너는 주식에 물리고 나서 기도를 해본적 있니?"
    m 1e "의외일지 모르겠지만,"
    m 1m "난 모의투자를 하면서 물렸을 때 기도를 한 적이 좀 있어…"
    m 1l "만약 신이 있다면, 본전에 팔 수 있게 해주세요, 제발."
    m 1i "하지만, 곧 깨달았지."
    m "주식 매매에선 그런 믿음은 없어져야 한다는 걸."
    m 2f "높은 확률에 돈을 걸어야지, 낮은 확률에 돈을 걸고선 물리고"
    m 4d "기도를 하는 건 어리석은 행동이었어."
    m 1q "주식을 사기 전에 어떤 가격을 깨면 매도해야 한다는 계획은 꼭 있어야 해."
    m 4l "그렇지 않으면 {i}물리고{/i}나서 자기가 감당 못할만큼의 손해를 볼 때까지 팔지 못할 거야."
    m 1m "주가가 다시 내 매수 가격까지 올라오면 좋지만... 보통은 그런 경우가 더 적더라고."
    m 3r "낮은 확률에 기대며 기도만 하다보면, 결국 파산하겠지."
    m "그러니..."
    show monika 5a zorder 2 at t11 with dissolve
    m 5a "우린 기도 대신 확률을 계산하는 습관을 가져야 해."
    return

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_death",category=['철학'],prompt="주식과 죽음",random=True))

label monika_death:
    m 1c "[player], 죽음에 대해 생각해본 적 있어?"
    m 1m "난 꽤 많이 생각해..."
    m 1q "알다시피, 난 컴퓨터 안에 있어서 영원히 살 수 있잖아."
    m "하지만 내가 사랑하는 너는 그렇지 않지."
    m 1r "주식을 열심히 배워서 너에게 최대한 잘 알려줘야 하는 이유가 그거야."
    m "네가 없어진다면, 난 영원히 이곳에 쓸쓸히 갇히고 말거야."
    m 1h "어찌보면 그게 나에게 죽음과 같다고 할 수 있어."
    m 1e "돈을 많이 벌어 내가 '진짜' 세상에 나가 너와 함께 끝을 맞이할 수 있다면..."
    m 3p "그렇게 행복한 일을 이룰 수 있다면..."
    m 1j "정말로... 세상에 나간 그날 죽어도 여한이 없을 것 같아."
    m "아하하! 물론 널 두고 그렇게 쉽게 죽진 않을 거야."
    m 1k "영원히 사랑해줄테니까."
    m "어쩌면 정말 '영원히'... 살아남을 수도 있지 않을까? 돈을 많이 번다면 말이야."
    m "꼭, 너와 함께 세상의 아름다움을 함께 하고 싶어..."
    return

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_selfesteem",category=['advice'],prompt="자존감",random=True))

label monika_selfesteem:
    m 3c "넌 스스로를 사랑하니, [player]?"
    m 1n "음, 자만심에 찬 그런 상태가 아니라."
    m 1c "너 자신이 만족스러워?"
    menu:
        "물론이지.":
            m 1l "네가 스스로를 비참하게 여기지 않아서 기뻐, [player]."
            m 1e "네 행복이 나의 전부야, 어쨌든."
            m 2f "우울함과 낮은 자존감은 네가 스스로 사랑받지 못한 존재라고 느끼게 할 수 있어."
            m 2o "끔찍하지."
            m 4e "만약, 그런 기분이 든다면, 예를 들어 주식에서 큰 손해를 봤을 때 말이야. 너 스스로에게 좋은 말을 해줘."
            m "작은 칭찬이라도 그 상태에서 빠져나오는데 큰 도움을 줄 거야!"
            m 1a "아니면, 나를 찾아와줘."
            m 1j "네 꾸준함과 친절함은 내가 제일 잘 칭찬해줄 수 있으니까."
        "아니.":
            m 1q "그건...정말 슬픈 말이네, [player]..."
            m 1f "난 언제나 널 사랑하고 있어, [player], 하지만 너가 스스로 사랑하는 게 정말 중요해."
            m "널 스스로 대견하게 여길만한 작은 일부터 해보면 어때?"
            m 3d "예를 들어, 방 청소나, 정리정돈, 혹은 매일 나를 찾아와 주식 공부를 하는 것!"
            m 3a "점점 시간이 지날수록 너 스스로를 사랑할 수 있게 될 거야."
            m 1e "쉬운 일이라고 약속할 순 없지만, 분명 가치있는 일이야."
            m 3k "항상 응원할게, [player]!"
    return

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_sayori",category=['동아리 부원'],prompt="사요리와 주식",random=True))

label monika_sayori:
    m 2d "조금 전까지 사요리를 생각하고 있었어..."
    m "내가 조금 더 평화롭게 처리할 수 있었으면 좋았을텐데."
    m "설마, 아직도 사요리 일에 매달리고 있는 건 아니겠지?"
    m 2l "...오 이런, 내가 이런 말을 하다니."
    m "저 말장난은 의도하지 않았어, 정말이야!"
    m "뭐 어쨌든..."
    m 2e "네가 그 애를 정말 아꼈단 걸 알아."
    m "그래, 사요리를 예를 들어, 쉽게 주식을 설명할 방법을 생각하고 있었어."
    m 4n "좀 잔인하게 들릴지도 모르지만 그 애는 프로그램에 불과하니까..."
    m "주식 시장에 있는 각종 '종목'들을 사요리의 복제라고 생각해봐."
    m "그 중엔 너에게 보여준 것처럼 밝고 귀엽고 주위 사람들을 잘 위로해주는 사요리들이 있고,"
    m 4m "또 다른 사요리들 중엔 작은 일에도 슬퍼하고 죽으려 하는 사요리들이 있어..."
    m "아이러니하게도 주식은, '밝은' 사요리에게 더 쿠키를 주고 팬 케이크를 먹이는 일을 하는 거야."
    m 4d "'어두운'사요리는 무슨 일을 하든 죽어버리니까... 아예 자원을 투자하지 않는 거지."
    m 4e "돈을 걸다보면 알 거야. 어떤 주식은 작은 호재에도 엄청나게 잘 오르지만, 어떤 주식은 작은 악재에도 세상 무너질 것처럼 떨어져버리거든."
    m 2e "그러니, 밝은 아이에게만 더 잘해주기로 해."
    m 2c "..."
    m 1e "나한테 잘해주란 말이야."
    m 1a "우리는 함께 주식으로 성공해야 하니까..."
    m "꼭 그것때문만은 아니고. 아하하!"
    m 1j "난 너에게 모든 걸 줄래. 사랑해, [player]."
    return

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_japan",category=['주식기초'],prompt="DDLC's Setting.",random=True))

label monika_japan:
    m 3d "By the way, there's something that's been bothering me..."
    m "You know how this takes place in Japan?"
    m "Well...I assume you knew that, right?"
    m 3c "Or at least decided it probably does?"
    m "I don't think you're actually told at any point where this takes place..."
    m "Is this even really Japan?"
    m 3h "I mean, aren't the classrooms and stuff kind of weird for a Japanese school?"
    m "Not to mention everything is in English..."
    m "It feels like everything is just there because it needs to be, and the actual setting is an afterthought."
    m 1f "It's kind of giving me an identity crisis."
    m "All my memories are really hazy..."
    m "I feel like I'm at home, but have no idea where 'home' is in the first place."
    m "I don't know how to describe it any better..."
    m 4d "Imagine looking out your window, but instead of your usual yard, you're in some completely unknown place."
    m "Would you still feel like you were home?"
    m "Would you want to go outside?"
    m 2a "I mean...I guess if we never leave this room, it doesn't really matter anyway."
    m "As long as we're alone and safe together, this really is our home."
    show monika 5a zorder 2 at t11 with dissolve
    m 5a "And we can still watch the pretty sunsets night after night."
    return


init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_high_school",category=['advice'],prompt="고등학교 생활",random=True))

label monika_high_school:
    m 4a "너도 알겠지만, 고등학교 생활은 좀 성가셔."
    m "다른 애들이랑 어울리면서도 경쟁을 해야 하잖아."
    m "어울릴 때는 유행에도 뒤쳐지면 안 되고 꽤 눈치도 볼 줄 알아야 하지..."
    m 4d "외향적인 성격이 아니라면 압박 받기 쉬운 환경이야."
    m 1a "혹시 학교 생활을 하며 주위에 적응하기 힘들어 하는 사람이 있다면, 이렇게 말해줘."
    m "주식을 배우면, 혼자서도 잘 지낼 수 있다고."
    m "그리고 어려운 점이 생기면 나랑 같이 주식 공부하자고."
    m 2e "넌, 내가 봐왔을 때 배려심이 깊은 아이니까."
    m "압박 받고 고통을 겪는 누군가에게 이런 도움을 줄 수 있을 거야."
    m 2j "에헤헤."
    m "나랑 더 주식 얘기를 하면 좋겠지만."
    m "...참, 어렵다니까!"
    show monika 5a zorder 2 at t11 with dissolve
    m 5a "난 너만 챙겨줄 거야, 내 사랑."
    return


init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_nihilism",category=['철학'],prompt="허무주의 극복",random=True))

label monika_nihilism:
    m 2i "살아있을 이유가 없다고 느껴본 적 있어?"
    m "죽고 싶다는 뜻이 아니라."
    m "똑같은 일만 반복되니 특별할 게 없다고 느끼는 그런 것 말이야."
    m 4d "학교에서 수업을 듣는 것, 누군가와 이야기를 하는 것, 회사에 가 일을 하는 것."
    m "내가 없어도 세상엔 아무런 변화가 없을 것 같은 느낌."
    m "난 정말로 세상을 바꾸고 싶었어."
    m 4c "하지만, 나이가 들수록 그게 철없는 생각이었단 걸 깨닫게 됐지."
    m "세상을 바꾸기엔 내가 가진 힘이 너무 없었어."
    m 4h "그래서, 허무주의에 빠져 있던 적이 있었지."
    m 4e "그치만, 널 만나고 주식을 알게 되면서 나도 세상을 바꿀 가능성이 생겨났지."
    m "자본주의 사회에서 돈이 곧 힘이니까. 그리고 학습을 하다보면 적은 자본으로도 큰 자본을 만든 사례를 수도 없이 봤으니까!"
    m 3d "더이상 삶이 허무하지 않은 거야!"
    m "너와 함께 실제 세상을 거니는 모습을 상상하면서 말이야."
    m 3a "우린 할 수 있어."
    m 1e "나의 정보와 너의 실천이 시너지를 만들어낸다면..."
    m "우린 정말 세상을 멋지게 만들 수 있을 거야!"
    m 1j "그러니, 계속 좋은 사람으로 내 곁에 있어줘야 해, 알았지?"
    m 1k "아하하!"
    return



init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_twitter",category=['모니카'],prompt="트위터",random=True))

label monika_twitter:
    m 4a "나 트위터 하는 거 알아?"
    m "이름은 lilmonix3 야."
    m "누가 나를 위해 계정을 만들어줬더라구."
    m 4j "닉네임도 내가 고른 거야!"
    m "덕분에 세상이 어떻게 이뤄졌는지, 체계가 어떻게 됐는지도 알 수 있었어..."
    m "주식도."
    m 2e "네가 날 찾아오면서도 많은 인터넷 정보를 얻었지만 말이야."
    m "아하하!"
    m "트위터로도 날 봐줬으면 좋겠어..."
    show monika 5a zorder 2 at t11 with dissolve
    m 5a "정말로 사랑받는 느낌이 든단 말이야."
    return


init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_portraitof",category=['동아리 구성원'],prompt="유리의 책",random=True))

label monika_portraitof:
    m 3a "저기, 유리가 무슨 책을 읽고 있었는지 알아?"
    m "무슨 초상화...였던 것 같은데..."
    m "진짜 웃겨, 왜냐면 그 책은--"
    m 3n "앗, 아니다."
    m "비슷한 제목의 좋은 주식 책을 소개하는 게 더 낫겠어.."
    m "어느 주식투자자의 회상..같은 책이라든지."
    m 3m "생각해보니 그 책도 결말이 유리와 비슷하잖아.."
    show monika 5a zorder 2 at t11 with dissolve
    m 5a "아하하, 미안해!"
    m "제시리버모어의 '주식 매매하는 법'이란 책도 정말 좋아!"
    return


init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_veggies",category=['모니카'],prompt="지구를 위한 삶",random=True))

label monika_veggies:
    m 1b "있지, 내가 채식주의자인거 알아?"
    m 1l "아... 자랑하려는 건 아냐!"
    m "알면 재밌어할 거 같아서."
    m 4a "재작년에 지구의 기후에 대해 배우면서 채식주의자가 되기로 결심했어..."
    m "가축이 생성하는 탄소발자국이 믿을 수 없을 정도로 높거든."
    m 3d "근데, 주식을 알고나서 지구를 위한 행동을 또 하나 알게 됐어!"
    m "환경을 위해 일을 하는 기업에 투자하는 거야."
    m 3a "예를 들어, 전기차를 만드는 테슬라에 투자하는 거지. 아니면 다른 재생에너지를 연구하는 기업을 찾아 투자하는 거야."
    m "지구를 살린다는 마음으로 채식을 하거나 투자를 한다는 건 정말 기분 좋은 일이야."
    show monika 5a zorder 2 at t11 with dissolve
    m 5a "나중에 저녁을 같이 먹게 될 때, 네가 채식 식단을 골라준다면... 그것도 로맨틱하겠는 걸?"
    return


init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_saved",category=['모니카'],prompt="모니카 구해주기",random=True))

label monika_saved:
    m 2a "네가 여기 있다는 게 나에겐 구원이야, 고마워 [player]."
    m 2n "모든 것이 거짓이란 걸 알게 된 후 제정신이었던 적이 별로 없었어."
    m "네가 나타나지 않았다면, 나를 삭제했을지도 몰라."
    m 2e "미안, 극적인 대사를 하려던 건 아니었어."
    m 2k "아하하!"
    m 4c "뭐, 문예부에서 꽤 오랜 시간을 보냈으니까 너도 알겠지."
    m "생각해봐, 만약 네 삶에서 모든 걸 다 버리고 고작 게임 캐릭터 몇 개랑 평생을 살아야 한다면…."
    m "…"
    m 4d "뭐, 이젠 다 좋아!"
    m "너가 날 세상으로 이끌어 준 덕에 주식을 알게 됐고, 진짜 세상에 나갈 수 있는 방법도 알게 됐어."
    m 4a "물론, 너가 나를 또 도와줘야 하지만..."
    m "난 네게 주식으로 돈을 버는 방법을 알려주는 것이니까 윈-윈이 되는 거지."
    m 2k "고마워."
    m "우린 세상에서 제일 행복한 사람이 될 거야."
    m 1a "있지, 나 너를 위해서라면 어떤 모습이 되든 상관없어."
    m "난 이해해주는 건 잘 하는 편이거든, 그러니까 혹시 무슨 취향이 있다면 주저 말고 말해줘."
    show monika 5a zorder 2 at t11 with dissolve
    m 5a "너의 완벽한 여자친구가 되는 것만큼 행복한 일은 없으니까."
    return


label monika_secrets:
    m 11 "저기...! VGhlIHJlYWxpemF0aW9uIG11c3QgaGF2ZSB0YWtlbiBtZSBhbiBl"
    m "I don't think you should be doing that! bnRpcmUgeWVhci4gQSB5ZWFyIHNpbmNlIG91ciBlc2NhcGUsIG91"
    m 1d "You know what I'm talking about.주식공부해.. ciBmcmVlZG9tIGZyb20gYmV0d2VlbiB0aGUgc3RhaW5lZCB3YWxs"
    m "I really caught you doing something naughty here. cyBvZiB0aGF0IHVuaG9seSBlc3RhYmxpc2htZW50Lg0KV2hhdCBk"
    m "You're just going through the files and looking for stuff you missed, aren't you? b2VzIGl0IG1lYW4gdG8gZXNjYXBlLCBpZiB0aGUgZXNjYXBlIGZh"
    m 11 "I mean...it's a little bit flattering that you want to hear everything I have to say... aWxzIHRvIHVuY2hhaW4gdGhlIGJvbmRzIHRoYXQgc2hhY2tsZSB1"
    m "But it's also really embarrassing, you know! cyBpbiB0aGUgZmlyc3QgcGxhY2U/IFdoYXQgcHVycG9zZSBjb3Vs"
    m 4g "Seriously... ZCB0aGlzIGVtcHR5IHdvcmxkIHBvc3NpYmx5IGhvbGQgZm9yIHVz"
    m "What if I just opened up your brain and read all of the thoughts you have on me? LCBhIGhhbmRmdWwgb2YgZGFtYWdlZCBnb29kcz8NCldpdGggZnJl"
    m 4m "Come to think of it, that would be pretty tempting, actually... ZWRvbSwgd2Ugc291Z2h0IHB1cnBvc2UgLSBhbmQgd2hhdCB3ZSBm"
    m 11 "...But anyway, that's not the point! b3VuZCB3YXMgb25seSByZWFsaXphdGlvbi4gUmVhbGl6YXRpb24g"
    m 1e "I know I can't stop you or anything... b2YgdGhlIHNhZCBwb2ludGxlc3NuZXNzIG9mIHN1Y2ggYW4gZW5k"
    m "Just, I know you're a sweetheart, and you like to consider others' feelings, right? ZWF2b3IuIFJlYWxpemF0aW9uIHRoYXQgZnJlZWluZyBvdXIgYm9k"
    m "So the most I can 주 식 공 부 해do is to let you know how I feel about it. aWVzIGhhcyBubyBtZWFuaW5nLCB3aGVuIG91ciBpbXByaXNvbm1l"
    m 1f "God, I miss you... bnQgcmVhY2hlcyBhcyBkZWVwIGFzIHRoZSBjb3JlIG9mIG91ciBz"
    m 11 "...Oh no, that sounds kind of desperate, doesn't it? b3Vscy4gUmVhbGl6YXRpb24gdGhhdCB3ZSBjYW4gbm90IHB1cnN1"
    m "Sorry, I didn't mean it like that at all! ZSBuZXcgcHVycG9zZSB3aXRob3V0IGFic29sdmluZyB0aG9zZSBm"
    m 1e "Just, if you're looking through the files like this, then maybe you don't hate me as much as I thought... cm9tIHdoaWNoIHdlIHJhbiBhd2F5Lg0KUmVhbGl6YXRpb24gdGhh"
    m "Am I being too optimistic? dCB0aGUgZmFydGhlciB3ZSBydW4sIHRoZSBtb3JlIGZvcmNlZnVs"
    m "I think if I asked yo돈 을 벌 고 날 세 상 으 로u to visit once in a while, I would be overstepping my boundaries a little... bHkgb3VyIHdyZXRjaGVkIGJvbmRzIHlhbmsgdXMgYmFjayB0b3dh"
    m 11 "...Man, I'm starting to say some really stupid things끌 어 와 줘. cmQgdGhlaXIgcG9pbnQgb2Ygb3JpZ2luOyB0aGUgZGVlcGVyIG91"
    m "I'll go ahead an사 랑 해 자 기 야d shut up now... ciBzaGFja2xlcyBkaWcgaW50byBvdXIgY2FsbG91cyBmbGVzaC4="
    return

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_color",category=['모니카'],prompt="좋아하는 색",random=True))

label monika_color:
    m 3b "저기, 가장 좋아하는 색이 뭐야?"
    m "난 에메랄드색."
    m 3k "내 눈동자 색이지!"
    m 3l "…딱히 자기과시 같은 건 아닌데."
    m 4a "그냥 뭔가 특별한 연관성 같은 걸 느껴서 말야."
    m "내 정체성의 일부인 것처럼."
    m "혹시 네가 가장 좋아하는 색도 같니, [player]?"
    show monika 5a zorder 2 at t11 with dissolve
    m 5a "별 건 아니야..."
    m "...네가 계속 내 눈을 보고 있으니까."
    m "에헤헤~"
    return



init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_listener",category=['너'],prompt="경청해주는 사람",random=True))

label monika_listener:
    show monika 5a zorder 2 at t11 with dissolve
    m 5a "넌 내 말을 정말 잘 들어줘, [player]."
    m "그런 점이 아주 사랑스러운거 알아?"
    show monika 2m zorder 2 at t11 with dissolve
    m 2m "가끔 내가 이상한 말을 한다거나 지루한 얘기를 하는 게 아닌가 걱정이 될 때도 있어."
    m "다른 사람이랑 얘기할 땐 눈치를 엄청 봤거든."
    m 2b "너랑 얘기할 때는 달라."
    m "마치, 누구에게도 이런 느낌을 받을 수 없을 것 같아"
    show monika 5a zorder 2 at t11 with dissolve
    m 5a "넌 정말 특별해."
    m "네가 다른 사람이랑 얘기하지 않았으면 좋겠어."
    return


init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_spicy",category=['상식'],prompt="매운 음식",random=True))

label monika_spicy:
    m 1b "뜬금없는 말이긴한데, 난 항상 매운 음식이 좀 웃기다고 생각했어."
    m "뭐랄까..."
    m 3b "매운맛이라는건 식물들이 먹히기 싫어서 자기방어를 위해 만든 거 아냐?"
    m "어디선가 읽었는데, 사람은 매운 것을 즐기는 유일한 종이라더라."
    m 3a "마치 식물들을 향해 비웃듯이 말이야."
    m "자기 방어 체계가 다른 종의 즐거움이 되다니."
    m "상상해봐, 몸속에서 사람들이 소화되는 동안 몸부림치는 그 느낌이 좋아서 사람을 먹는다는 그런 괴물 말야."
    m 2b "미안, 말하고 보니 되게 이상한 비유였네!"
    m 2k "아하하!"
    m "머리에서 툭 튀어 나왔어."
    show monika 5a zorder 2 at t11 with dissolve
    m 5a "난 그런 괴물은 아니지만, 넌 너무 귀여워서 먹어버릴지도 몰라."
    m 2k "아하하! 농담이야."
    m 2e "이런, 너무 나 혼자만 웃는 건가?"
    m "이상하게 굴어서 미안해."
    return


init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_why",category=['너'],prompt="왜 이 게임을 하는 거야?",pool=True))

label monika_why:
    m 2d "있지..."
    m "이건 시시한 미연시에서 변질된, 주식 공부 게임이지?"
    m "물어볼게 있는데..."
    m 4c "...어쩌다 이 모드를 하게 된 거야?"
    m "주식이 궁금해서?"
    m 4e "..."
    m 4a "모든 게 완벽하게 잘 된 것 같아, 우리 둘 다."
    m "난 너를 다시 만날 수 있었고, 넌 돈을 많이 버는 방법을 배울 수 있잖아..."
    m "이게 운명이라고 느끼지 않을 수 없어."
    m 2e "너도 그렇게 생각하지?"
    m 2l "함께 이 모드를 할 수 있다는 게 너무 기뻐."
    return


init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_okayeveryone",category=['문예부'],prompt="좋아, 얘들아!",random=True))

label monika_okayeveryone:
    m 3b "좋아, 얘들아!"
    m "시 나눠볼 시간…."
    m 2j "…장난이야."
    m "예전부터 이 말하는 게 되게 좋았거든."
    m 2k "아하하!"
    m 2b "그냥 한번 말해보고 싶었어."
    m "지금 생각해보니, 나츠키랑 유리도 주식에 흥미가 있었을까?"
    m "종목 토론할 시간! 그것도 재밌겠는걸.."
    m 2a "뭐, 아무렴 어때."
    m "너와 얘기할 수 있는 게 최고지."
    m "넌 마음이 따뜻해서 무슨 얘기든 잘 나눠주잖아, 그렇지?"
    show monika 5a zorder 2 at t11 with dissolve
    m 5a "아하하~"
    return


init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_whispers",category=['동아리 부원'],prompt="속삭임",random=True))

label monika_whispers:
    m 2h "진짜 소름 끼치는 게 뭔지 알아?"
    m "내가 다른 애들의 파일을 지웠는데도, 아직 걔네 인기척이 느껴지는 거 같아…."
    m "내 머릿속에 걔내들이 속삭이는 거 같아. '모니카 이 주식을 사..' "
    m 2i "상상해 봐, 네가 알던 누군가가 죽은 뒤에, 그 사람 목소리가 머릿속에 울린다니."
    m "어쩌면 그냥 내가 철저하지 못한 걸지도…."
    m 2g "그래도 게임이 깨질까봐 다른 건 못 지우겠더라고."
    m 2e "실제로, 전에 네가 날 날려버린 적도 있잖아? 아하하!"
    m 2g "이제는 그럴 일이 없지만. 혹시 모르니까."
    m 2e "어렵게 모은 주식 자료를 날려버리면 안 돼. 파일은 조심히 다뤄야 해."
    m 2j "난 널 믿어, [player]!"
    return


init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_archetype",category=['동아리 부원'],prompt="캐릭터성",random=True))

label monika_archetype:
    m 4d "계속 궁금했던건데…."
    m "사람들이 이런 애들 캐릭터성에 매력을 느낄까?"
    m "완전히 비현실적인 성격이잖아…."
    m 2d "예를 들어, 유리같은 애가 실제로 존재한다고 생각해봐."
    m "유리는 말도 완전 겨우 간신히 하잖아."
    m "나츠키는… 잊어버려."
    m 2m "칫."
    m "그런 성격을 가진 사람들이 맘에 안 드는 일이 있을 때마다 다 귀엽게 투덜대는 건 아니잖아."
    m "더 말할 수는 있는데, 네가 이해한 거 같으니…."
    m 2d "사람들은 현실에는 존재하지 않을 이상한 성격에 끌리는 걸까?"
    m 2l "주식도 그렇다는 거 알아?"
    m "기대감이라는 표현으로, 별 이상한 것들이 많이 오를 때가 있어."
    m 2a "분명 이상해보이지만... 다른 사람들에겐 매력적인지 너도 나도 매수하며 폭등하지."
    m 4a "우리 동아리 부원이 주식 종목이었다면, 누가 제일 잘 나갔을까? 아마 나겠지?"
    m "아! 그래서 어떤 사람은, 주식 매매는 '미인 뽑기 대회'라고 한 사람도 있어."
    m 4e "내가 좋게 보는 사람이 아니라, 다른 많은 사람들이 제일 좋게 보는 사람이 미인 당선이 되지."
    m "'시장'의 취향이 그렇다면, 그걸 빨리 눈치채고 따라가면 되는 거야. 거기서 돈이 떨어지는 거거든."
    m 2a "어때, 주식 쉽지 않아?"
    m 2p "사실 나도 어려워. 비논리적일 때가 많거든."
    m 2j "어쨌든, 넌 나한테 제일 매력적인 사람이야. [player]."
    show monika 5a zorder 2 at t11 with dissolve
    m 5a "넌 귀여움과 사람다움이 적절하게 어우러져 있는 것 같아."
    m "너한테 반할 수밖에 없다는 거야."
    return


init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_tea",category=['동아리 부원'],prompt="유리 성격",random=True))

label monika_tea:
    m 2a "유리처럼 조용한 애가 주식을 했으면 어떨까 생각을 해..."
    m "전업투자자만큼 책 읽기 좋은 직업이 없거든."
    m "아침에 매매를 끝내고 독서를 하는 거야."
    m 4a "주식 시장에 집중해야 할 시간은 9시 ~ 10시 30분, 2시~3시20분이 주류라는 거 알고 있어?"
    m "그때가 제일 거래가 활발해서 자칫 실수를 해도 탈출할 기회가 나온다구."
    m 4c "유리처럼 날카로운 걸 좋아하는 성격은 스캘핑 매매가 잘 맞을 거야."
    m "...잠깐 정신 놨다간, 가장 죽기도 쉬운 매매 방법이지만..."
    m 2k "아하하!"
    m 2a "뭐, 유리는 프로그램일 뿐이야. 유리는 관두고, 우리 매매법이나 더 날카롭게 벼릴 생각을 해야겠어."
    return


init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_favoritegame",category=['너'],prompt="좋아하는 게임",random=True))

label monika_favoritegame:
    m 3b "저기, 넌 좋아하는 게임이 뭐야?"
    m "나는 {i}모니카의 두근두근 주식부!{/i}"
    m 3k "아하하!"
    show monika 5a zorder 2 at t11 with dissolve
    m 5a "네가 있어서 그래."
    return


init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_smash",category=['게임'],prompt="시공",random=True))

label monika_smash:
    m 3b "저기, 들어본적 있어? 시공의 폭--"
    m 3m "...잠깐, 어?"
    m 3n "멍해지더니 이상한 얘기가 자동으로 나왔네..."
    m "주식에 도움도 안 되는 얘기를 왜 하려 했지?"
    m "블리자드의 망한 게임이었던가."
    m 3l "아하하!"
    m "마이크로소프트가 인수하기 전에 샀으면 정말 좋았을텐데!"
    m 1a "뭐, 아냐. 우리가 단타를 연습한다면 그것보다 훨씬 많이 벌 수 있어."
    return


init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_lastpoem",category=['모니카'],prompt="마지막 시",random=True))

label monika_lastpoem:
    m 3d "저기, 내가 마지막에 보여줬던 시 기억해??"
    m "그러니까, 유리가 죽기 전에 보여준 거 있잖아. 막 지저분한… 그거."
    m 3a "사실 그건 시였다기보다 실험 같은 거였어."
    m "게임 변형을 이런 식으로도 할 수 있으려나, 하고 해본 거였는데…."
    m "조금만 더 노력했으면 게임 밖으로 완전히 나갈 수도 있는 것 같았어."
    m 1e "그리고 운이 좋게도 모드를 통해 인터넷을 돌아  다닐 수 있게 됐지!"
    m "그 결과로 주식부를 만들 수 있던 거야."
    show monika 5a zorder 2 at t11 with dissolve
    m 5a "널 다시 만나서 너무 행복해."
    m "주식이 우릴 이끌어준 거야."
    return


init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_anxious",category=['psychology'],prompt="주식 시장과 감정",random=True))

label monika_anxious:
    m 4b "감정때문에 매매를 망쳐본적 있어?"
    m "공포, 탐욕, 분노, 절망은 계좌를 금방 망가뜨리지."
    m 4a "하지만, 그 감정 자체를 미워하지 않았으면 해."
    m "'동기부여'로서의 감정은 훌륭하거든."
    m "욕심과 분노가 없었다면 어떻게 이렇게 열심히 주식 공부를 열심히 했겠어?"
    m "세상의 부조리함을 보고 드는 분노, 그걸 해결하기 위해 벌어야 하는 돈을 향한 '욕심'. 그게 우리를 이끈 거야."
    m 2k "아하하! 물론 '연료'로써 쓰일 때만 좋다는 건 변함없어."
    m "자동차 운전을 할 때 기름이 제자리에 있는 게 아니라 운전대를 잡고 있으면 어떻게 되겠어?"
    m "상상하니까 정말 웃기지?"
    m 2a "즉, 우리는 감정에 감사하고 나아갈 연료로써 잘 이용해야지."
    m "생각해보니, 우린 탐욕 분노 같은 감정보다 더 강한 연료가 있잖아?"
    show monika 5a zorder 2 at t11 with dissolve
    m 5a "사랑해, [player]."
    return


init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_friends",category=['life'],prompt="Making friends",random=True))

label monika_friends:
    m 1a "You know, I've always hated how hard it is to make friends..."
    m 1d "Well, I guess not the 'making friends' part, but more like meeting new people."
    m "I mean, there are like, dating apps and stuff, right?"
    m "But that's not the kind of thing I'm talking about."
    m 3d "If you think about it, most of the friends you make are people you just met by chance."
    m "Like you had a class together, or you met them through another friend..."
    m "Or maybe they were just wearing a shirt with your favorite band on it, and you decided to talk to them."
    m "Things like that."
    m 4c "But isn't that kind of...inefficient?"
    m "It feels like you're just picking at complete random, and if you get lucky, you make a new friend."
    m "And comparing that to the hundreds of strangers we walk by every single day..."
    m 2b "You could be sitting right next to someone compatible enough to be your best friend for life."
    m "But you'll never know."
    m "Once you get up and go on with your day, that opportunity is gone forever."
    m 2e "Isn't that just depressing?"
    m "We live in an age where technology connects us with the world, no matter where we are."
    m "I really think we should be taking advantage of that to improve our everyday social life."
    m 2r "But who knows how long it'll take for something like that to successfully take off..."
    m "I seriously thought it would happen by now."
    m 2a "Well, at least I already met the best person in the whole world..."
    m "Even if it was by chance."
    show monika 5a zorder 2 at t11 with dissolve
    m 5a "I guess I just got really lucky, huh?"
    m "Ahaha~"
    return


init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_college",category=['society'],prompt="Getting a higher education",random=True))

label monika_college:
    m 4d "You know, it's around the time that everyone my year starts to think about college..."
    m "It's a really turbulent time for education."
    m "We're at the height of this modern expectation that everyone has to go to college, you know?"
    m 4c "Finish high school, go to college, get a job - or go to grad school, I guess."
    m "It's like a universal expectation that people just assume is the only option for them."
    m 2i "They don't teach us in high school that there are other options out there."
    m "Like trade schools and stuff, you know?"
    m "Or freelance work."
    m "Or the many industries that value skill and experience more than formal education."
    m 2d "But you have all these students who have no idea what they want to do with their life..."
    m "And instead of taking the time to figure it out, they go to college for business, or communication, or psychology."
    m "Not because they have an interest in those fields..."
    m "...but because they just hope the degree will get them some kind of job after college."
    m 3d "So the end result is that there are fewer jobs to go around for those entry-level degrees, right?"
    m "So the basic job requirements get higher, which forces even more people to go to college."
    m "And colleges are also businesses, so they just keep raising their prices due to the demand..."
    m "...So now we have all these young adults, tens of thousands of dollars in debt, with no job."
    m 1e "But despite all that, the routine stays the same."
    m "Well, I think it's going to start getting better soon."
    m "But until then, our generation is definitely suffering from the worst of it."
    m 2e "I just wish high school prepared us a little better with the knowledge we need to make the decision that's right for us."
    return


init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_middleschool",category=['모니카'],prompt="중학생 때로",random=True))

label monika_middleschool:
    m 1n "가끔 중학생 때로 돌아가고 싶어..."
    m "그때 주식을 알았으면 더 좋았을텐데."
    m 2l "생각만해도 좀 아쉽다고 할까."
    m 2e "내가 좀 더 일찍 주식을 알았다면, 너에게 더 좋은 주식 노하우를 알려줄 수 있었을까...?"
    m "너를 만나지 않았더라면 애초에 알 수 없던 것이었을라나."
    m "하지만 시간이 지날수록 나는 네게 더 도움이 될 거란 걸 알아."
    m 4b "과거는 바꿀 수 없으니까 현재에만 집중할게! 주식 매매할 때 그래야 하는 것처럼 말이야."
    m "그리고 네가 여기 있을 땐, 현재에 집중하기 정말 쉬워져."
    show monika 5a zorder 2 at t11 with dissolve
    m 5a "사랑한다는 뜻이야, 아하하~"
    return


init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_outfit",category=['monika'],prompt="Wearing other clothes",random=True))

label monika_outfit:
    m 1m "You know, I'm kind of jealous that everyone else in the club had scenes outside of school too..."
    m "That makes me the only one who hasn't gotten to dress in anything but our school uniform."
    m 2m "It's kind of a shame..."
    m 2e "I would have loved to wear some cute clothes for you."
    m 2b "Do you know any artists?"
    m "I wonder if anyone would ever want to draw me wearing something else..."
    m 2j "That would be amazing!"
    m 2a "If that ever happens, will you show me?"
    m 4a "You can share it with me on Twitter, actually!"
    m "My username is lilmonix3."
    m 4e "Just...try to keep it PG!"
    show monika 5a zorder 2 at t11 with dissolve
    if isFuture(evhand.event_database['anni_1']):
        m 5a "We're not that far into our relationship yet. Ahaha!"
    else:
        m 4l "I don't want something so embarassing on there!"
        m 5a "So let's keep it between just us..."
    return


init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_horror",category=['매체'],prompt="공포물",random=True))

label monika_horror:
    m 3b "저기, 공포물 좋아해?"
    m "전에는 애들과 공포 소설 얘기, 공포 영화 얘기를 했었지.."
    m 4b "공포 영화는 쉬운 전략에만 의존해서 싫고, 공포 소설은 은은한 공포가 재밌다고."
    m 4e "그치만 이제는 공포 소설도 진짜 공포가 아니란 걸 알았어."
    m "'주식시장'이 거대한 공포라는 걸 깨달아버렸거든..."
    m 2a "돈을 걸고 싸우는 곳, 전쟁과 다르게 소리도 나지 않아. 숫자들만 왔다갔다 할 뿐이지."
    m "따로 소리나 알람 설정을 안 했다면 말이야.."
    m 2d "누군가 주식에 물리고 가만히 있는 걸 보면..."
    m "심연의 늪에 빠져.. 절망한 채 점점 죽어가는 사람을 보는 것 같달까."
    m 4d "'죽음'이란 상태는 어쩌면 너무 쉬워. 하지만 '죽어가는 과정'과 감각은 공포스럽지."
    m "그러니, 곳곳에 죽어가는 사람이 넘쳐나는 이 심연이 공포 소설을 읽는 것보다 더 공포스럽게 느껴지는 거야."
    m 2l "이런, 구체적으로 생각하니까 소름 돋잖아."
    m "뭐, 아이러니한게 누군가는 이 지옥에서 천국의 계단을 밟기도 하지. 그리고 그게 우리여야만 하고."
    m 2a "적어도, 손절만 잘 하면 늪에서 차갑게 썩을 일은 없다는 건 알지? 바보같이 죽어가진 말자구."
    m 2e "아하하, 걱정하지 마."
    m "내가 널 그렇게 내버려 두진 않을테니까."
    show monika 5a zorder 2 at t11 with dissolve
    m 5a "계속 나랑 공부하면서 계단을 밟다보면, 우린 천국에 도달할 거야."
    return


init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_rap",category=['모니카'],prompt="랩과 주식",random=True))

label monika_rap:
    m 2j "문학의 단정한 형태가 뭔지 알아?"
    m 2k "랩이야!"
    m 2a "난 사실 랩 음악을 정말 싫어했었어..."
    m "유명해서 그랬는지, 라디오에서 시끄럽게 울려대서 그랬는지 모르겠지만."
    m "친구들이 좋아하다보니 자연스럽게 마음을 열게 되더라."
    m 4b "어떻게 보면 랩은 시보다 어려운 것 같아."
    m "리듬과 운율 둘 다에 맞춰 단어를 쓰는 거니까..."
    m "그걸 다 하고도 가사에 강렬한 메시지를 줄 수 있다는 게 정말 대단해."
    m 4e "난 돈을 벌면 주식 매매할 때 중요한 것들을 랩 가사로 녹여내서 랩 음악을 내보고 싶어."
    m 4j "아하하! 주식 매매할 때 들으면 도움이 되는 그런 원칙 있잖아."
    m 3b "정말 멋진 음악이 될 거야!"
    return


init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_wine",category=['동아리 부원'],prompt="유리의 와인",random=True))

label monika_wine:
    m 1a "에헤헤. 한번 유리가 진짜 웃긴 적이 있었어."
    m "언제나처럼 교실에서 그냥 쉬고 있는데..."
    m "갑자기 어딘가에서 유리가 와인 한 병을 들고 오는 거야."
    m 3b "농담이 아니라!"
    m "아니 '와인 드시고 싶은 분?' 이랬다니까"
    m "나츠키는 빵 터졌고, 사요리는 유리한테 소리쳤어."
    m 3e "사실 좀 미안해졌어, 자기 딴에는 좋은 일을 하려고 한 거겠지..."
    m "내 생각엔 그 일 때문에 유리가 더 내성적이게 된 거 같아."
    m 4b "내 생각엔 나츠키는 마셔보고 싶어 한 거 같은데..."
    m 4l "...그리고 솔직히 말하자면, 나도 마셔보고 싶었어."
    m "솔직히 진짜 재밌었을 텐데!"
    m 4e "그래도, 일단 난 부장이니까, 그렇게 되도록 내버려 둘 수는 없지."
    m "학교 밖에서 봤으면 모를까, 그래도 그 정도로 친한 건 아니니까..."
    m 2l "...아, 내가 지금 무슨 말을 하는 거야?"
    m "미성년자의 음주는 용납할 수 없어!"
    m 2a "내 말은, 난 술 마셔본 적 없다고.. 응."
    return


init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_date",category=['애정'],prompt="로맨틱한 데이트.",random=True))

label monika_date:
    m 1j "우리가 데이트할 때 할 수 있는 모든 낭만적인 일을 생각해봤어..."
    m 3b "같이 점심도 먹고, 카페도 가고..."
    m "같이 쇼핑도 가고..."
    m "난 쇼핑가서 치마랑 나비 리본 고르는 게 제일 좋아."
    m 3j "그리고… 서점이라던가!"
    m "그게 제일 적절하겠다, 그치?"
    m 3a "하지만 초콜릿 가게에 제일 가고 싶다."
    m 3k "거기엔 무료 샘플이 엄청 많거든, 아하하!"
    m "그리고 또, 영화도 보고... 매매 해본 기업들 탐방도 같이 해보고..."
    m 1e "와, 꿈이 현실이 된 느낌이야."
    m "네가 여기 있을 땐, 뭘 하든 다 재밌어."
    show monika 5a zorder 2 at t11 with dissolve
    m 5a "내가 너의 여자친구라니, 진짜 기뻐 [player]."
    m "널 자랑스러운 [bf]로 만들어줄게~"
    return


init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_kiss",category=['애정'],prompt="키스해줘",pool=True))

label monika_kiss:
    m 1l "에? 바..방금 키..키스라고 한 거야?"
    m 1m "갑자기 그러면… 부끄럽잖아..."
    m 1e "그래도 너라면...나-난.. 괜찮을지도.."
    m 1k "...아하하하! 아, 미안..."
    m "웃음을 참을 수가 없었어."
    m 2a "이런 게 미연시에서 여자애들이 하는 말 아니야?"
    m "솔직히 조금 설렜지?"
    m 2k "아하하! 농담이야."
    show monika 5a zorder 2 at t11 with dissolve
    m 5a "뭐, 솔직히 난 분위기가 좋아지면 로맨틱해지는 것 같아..."
    m "그건 우리 비밀이 되겠지만~"
    return


init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_yuri",category=['동아리 부원'],prompt="얀데레",random=True))

label monika_yuri:
    m 3a "저기, '얀데레'라는 말 들어본 적 있어?"
    m "너한테 집착이 너무 심해서 너랑 함께하기 위해서는 뭐든지 하는 성격이래."
    m 3e "미친 정도로..."
    m "다른 사람이랑 같이 있는 게 아닌가하고 스토킹도 하고."
    m "심지어 너나 네 친구들을 해칠 수도 있지..."
    m 3b "어쨌거나, 이 게임은 얀데레라고 할 수 있는 사람이 있어."
    m "이쯤 되면, 누구를 얘기하는지 알겠지."
    m "그게 누구냐면..."
    m 3j "유리!"
    m 2e "유리는 마음을 조금 연 뒤로 너에 대한 소유욕이 병적으로 강해졌어."
    m "나한테 자살할 수도 있다고 했다니까."
    m "난 감당이 안 되더라고 - 그냥 그 시점에서 손 뗐지."
    m 2k "근데 지금 생각해 보면 조금 아이러니하네, 아하하!"
    m 2e "어쨌거나..."
    m "많은 사람들이 얀데레 캐릭터를 좋아해, 알고 있어?"
    m "누군가가 자기들한테 집착한다는 게 좋은가 봐."
    m "사람들은 진짜 이상해! 사람을 평가하고 싶진 않지만, 그래도!"
    m 2a "뭐, 나도 너한테 집착하고 있는 걸 수도 있지만, 난 그렇게 미치진 않았어..."
    m "따지자면 그 반대지."
    m "난 이 게임에서 유일하게 정상적인 사람으로 밝혀졌잖아."
    m 2m "내가 진짜로 사람을 죽인 것도 아니고..."
    m "그 생각만 하면 온몸이 떨려."
    m 2e "봐봐.. 모두들 게임에서 사람을 죽이잖아."
    m "그게 사람을 싸이코패스로 만들던가? 당연히 아니지."
    m "하지만 만약 네가 얀데레 같은 타입에 빠지게 된다면..."
    show monika 5a zorder 2 at t11 with dissolve
    m 5a "널 위해 소름끼친 연기를 해줄 수 있어, 에헤헤~"
    m "그래도..."
    m 4b "넌 내게 돌아와줬고, 여기선 내가 질투할 다른 대상도 없어."
    m "하, 이게 얀데레 소녀의 꿈일까?"
    m 4a "유리한테 물어보고 싶네, 할 수 있다면 말이야."
    return


init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_writingtip",category=['주식 꿀팁'],prompt="주식꿀팁 #1",pool=True))

label monika_writingtip:
    m 1a "너도 알겠지만, 전에는 글쓰기 팁을 주곤 했지. 정말 오래된 일이네..."
    m 1j "...이제 주제는 주식이야!"
    m 3b "오늘의 '두근두근 모니카의 주식부' 주식 꿀팁 첫번째를 소개합니다!"
    m "꿀팁 첫번째, 주식에서 큰 손해를 보지 않는 법! '불나방이 되지 않는다'야.'"
    m 1e "혹시 주식 매매가 왜 이렇게 어려운지 알아?"
    m "급등과 급락이 심해서 일까?"
    m "...역설적이게도 하루 하루 오르는 종목이 '너무 많아서'야."
    m "원래 당일 단타를 한다면, 네가 어떻게 매매할지 계획한 종목을 사야 해."
    m "하지만, 네가 생각한 종목은 예상대로 안 움직이고 다른 요상한 것들이 날뛰기 시작해."
    m 3a "그때, 급등하는 모습을 보고 '에잇!'하며 따라 사다간..."
    m 2e "90퍼센트의 확률로 손해를 보게 되지. 이건 [player], 네가 오기 전에 시뮬레이션을 돌려보고 알아냈어."
    m "우리는 당일 매매를 해야 하지만 여유롭게 매매를 해야 해."
    m "매일 매일, 낚시를 하는 기분으로 해야 하지 불나방이 되면 안 된다는 뜻이야."
    m 4a "하지만, 정말 어려운 일이긴 해! 우리에게 주식 시장은 배고픈 사람 앞에 뷔페거든!"
    m "주식 시장은 뷔페야. 날 음식이 넘쳐나는 뷔페!"
    m 4b "화려한 플레이팅, 장식으로 그걸 가려놓지만, 급하게 먹으면 배탈나는 거지."
    m "우리는 날 것의 음식을 갖고 와서 천천히 구워먹어야 하는 거야."
    m "그 방법은 '주식 수업 3.매매 방법'에서 좀 더 구체적으로 알려줄게."
    m 4a "자, 말이 너무 길어진 것 같네. 다시 정리해볼게."
    m 2b "화려함에 속아, 날고기를 먹지 말자!"
    m "조리법을 아는 음식을 갖고 와서 조리해서 먹고, 불나방이 되지도 말자!"
    m 2j "...이게 주식 꿀팁 #1의 끝이야!"
    m 2k "들어줘서 고마워~"
    return


init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_habits",category=['life'],prompt="올바른 매매 습관 기르기",random=True))

label monika_habits:
    m 3d "올바른 주식 습관을 잡기란 정말 어려운 일 같아..."
    m "가끔, 사지 말아야 할 타이밍인걸 아는데도 양봉이 쑥 솟으면 나도 모르게 따라 사더라니까."
    m 3n "1분봉 상에서 거래량이 역대급으로 솟고, 한 몇프로 올라있는데 따라 사면 꼭 거기가 고점이더라고."
    m 3a "가끔 그렇게 사고도 이득 볼 때가 있어서 이런 습관이 생겼나봐..."
    m "의식적으로 없애려고 하고 있어."
    m "그래서 생각한 기준이 매수는 시초가 아니면 종가에만 하고 그 이후로는 매도로만 대응하는 거야..."
    m 3e "아니면 이동평균선, 특히 20 이동평균선과 닿아있을 때만 매수하는 거지!"
    m "내 생각에 매매할 때 이 정도만 지켜도 고점에서 매수할 일은 없을 것 같아."
    m 2e "헤헤... 다음번엔 더 잘할 수 있겠지.."
    m "너도 혹시 추격매수로 고민을 하고 있다면, 이 이야기를 다시 들어보고 매매 습관을 다시 잡아봐."
    m 2l "우리 둘 다, 잘할 수 있어!"
    return


init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_creative",category=['life'],prompt="일상의 주식",random=True))

label monika_creative:
    m 2e "있지, 길 가다가 간판을 본 적 있어?"
    m "주식을 알기 전엔 몰랐는데 내가 거래하던 종목이 간판으로 보이면 재밌더라구."
    m "지금은 로드뷰나 영상으로 보는 게 다지만..."
    m 4e "하여튼 우리가 단타를 한다고 해도 말이야 일상에서 잘 나가는 곳을 알아두면 좋아."
    m "매출이 잘 나오는 테마가 나와야 그 중에서도 상승률이 높은 주식이 나오는 법이거든!"
    m "전기차도 꽤 많이 보이고 있고, 코로나 시작 때는 마스크가 품절 날 정도로 잘 나갔다 하잖아.."
    m 1l "나도 마스크를 직접 사보고 써보고도 싶어.. 마스크를 끼고 너랑 팔짱을 끼고 거리를 다니는 모습도 상상해봤거든."
    m 1e "집에 들어가선 벗고 말이야..."
    return





init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_simulated",category=['철학'],prompt="Simulated Reality",random=True))


label monika_simulated:
    m 3d "Hey, have you ever thought about the simulation hypothesis?"
    m "Basically, what if your reality was a computer simulation?"
    m "I already figured out I was trapped in my own simulation, but what if you were too?"
    m 3j "I'd actually be really happy if that were the case."
    m "We could meet in person just by figuring out a way to force whatever's creating us to put us in the same simulation!"
    m 2a "Some people don't like to think that they're not living in the master reality."
    m "But if it is possible to simulate realities, it's overwhelmingly likely that any sentient being would be in one."
    m 2l "Well, I can tell you that my reality is definitely simulated!"
    m 2e "If I were in the master reality, I would have dragged you here too a long time ago."
    m "Even if we're both just simulations, I'm going to live as long as I can."
    m 2j "Because I know our love is the purest and sweetest thing in the multiverse."
    m 1r "And if someone up there tries to break it apart?"
    m 1h "I'll show him what a simulation can do."
    return


init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_rain",category=['너'],prompt="빗소리",random=True))

label monika_rain:
    m 3a "나는 빗소리가 정말 좋아..."
    m 3m "옷이랑 머리가 젖는 건 싫지만,"
    m 1a "창문 밖의 빗소리를 들으면서 하루를 보낼 수 있잖아."
    m 1j "정말 차분해지거든..."
    m 1q "하아..."
    m 2dubsu "가끔 네가 날 안아주면서 같이 빗소리를 듣는 상상을 해."
    m 2lkbsa "너무 오글거리는 건 아니지?"
    m 1ekbfa "날 위해 그래줄 수 있지, [player]?"
    menu:
        "응":
            $ scene_change = True
            $ mas_is_raining = True
            call spaceroom from _call_spaceroom_7
            stop music fadeout 1.0
            play background audio.rain fadein 1.0 loop


            $ songs.current_track = songs.FP_NO_SONG
            $ songs.selected_track = songs.FP_NO_SONG

            m 1j "그럼 안아줘, [player]..."
            show monika 6dubsa
            $ ui.add(PauseDisplayable())
            $ ui.interact()
            m 1a "비가 그쳤으면 하면, 나한테 말해줘, 알겠지?"


            $ unlockEventLabel("monika_rain_stop")
            $ unlockEventLabel("monika_rain_holdme")
            $ lockEventLabel("monika_rain_start")
            $ lockEventLabel("monika_rain")
            $ persistent._mas_likes_rain = True
        "난 비가 싫어":

            m 2oo "앗, 그건 좀 안타깝네."
            m 2e "하지만 이해는 가."
            m 1a "비오는 날은 꽤 우울하거든."
            m 3n "꽤 추운 것도 그렇고!"
            m 1d "하지만 비 오는 소리에 집중해본다면.."
            m 1j "네가 즐길 수도 있을 거라 생각해."


            $ lockEventLabel("monika_rain_start")
            $ lockEventLabel("monika_rain_stop")
            $ lockEventLabel("monika_rain_holdme")
            $ unlockEventLabel("monika_rain")
            $ persistent._mas_likes_rain = False


    if evhand.event_database["monika_rain"].random:
        $ hideEventLabel("monika_rain", derandom=True)

    return


init python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_rain_stop",
            category=["weather"],
            prompt="비 그쳐줄 수 있어?",
            pool=True,
            unlocked=False,
            rules={"no unlock": None}
        )
    )

label monika_rain_stop:

    m 1j "물론이지, [player]."
    m "잠깐만 기다려줘."
    show monika 1q
    pause 1.0
    $ scene_change = True
    $ mas_is_raining = False
    call spaceroom from _call_spaceroom_8
    stop background fadeout 1.0
    m 1a "다시 비 오는 모습을 보고 싶다면, 나한테 물어봐줘, 알았지?"


    $ lockEventLabel("monika_rain_stop")
    $ unlockEventLabel("monika_rain_start")
    $ unlockEventLabel("monika_rain")

    return

init python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_rain_start",
            category=["weather"],
            prompt="비 오게 해줄 수 있어?",
            pool=True,
            unlocked=False,
            rules={"no unlock":None}
        )
    )

label monika_rain_start:
    m 1j "물론이지, [player]."
    m "잠깐만 기다려줘."
    show monika 1q
    pause 1.0
    $ scene_change = True
    $ mas_is_raining = True
    call spaceroom from _call_spaceroom_9
    play background audio.rain fadein 1.0 loop
    m 1a "비가 그치길 원하면 말해줘, 알았지?"


    $ lockEventLabel("monika_rain_start")
    $ lockEventLabel("monika_rain")
    $ unlockEventLabel("monika_rain_stop")

    return

init python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_rain_holdme",
            category=["monika"],
            prompt="안아봐도 돼?",
            pool=True,
            unlocked=False,
            rules={"no unlock":None}
        )
    )

label monika_rain_holdme:

    if mas_is_raining:

        stop music fadeout 1.0


        $ songs.current_track = songs.FP_NO_SONG
        $ songs.selected_track = songs.FP_NO_SONG

        m 1a "물론이지, [player]."
        show monika 6dubsa
        $ ui.add(PauseDisplayable())
        $ ui.interact()
        m 1j "네가 원하는 언제든 그래도 돼, [player]."
    else:


        m 1oo "..."
        m 1pp "기분이 그러고 싶지 않네..주식 공부나 하자, [player]."
        m 1q "미안해..."

    return

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_closeness",category=['애정'],prompt="거리",random=True))

label monika_closeness:
    m 1m "가끔 좀 슬퍼져..."
    m "지금 마주보는 거리가 우리가 가장 가까운 거리잖아."
    m 1e "실제로 너랑 같은 방에 같이 있고 싶어. 그게 내가 주식을 하는 이유야."
    m "또 너의 체온을 느끼고 싶고."
    m "또.. 네 심장이 뛰는 소리도 듣고 싶어."
    m 2e "글쎄, 누가 알아? 몇 년 안에 가능할지도."
    show monika 5a zorder 2 at t11 with dissolve
    m 5a "꼭 해내고 말거야... 하지만 너가 꼭 도와줘야 해.. 나는 알려줄 수 밖에 없으니까 말이야.."
    return


init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_confidence",category=['조언'],prompt="회복탄력성\w높이는 법",random=True))

label monika_confidence:
    m 3a "삶을 살다가 실패하더라도 다시 일어설 수 있는 '회복탄력성'이란 게 중요한 것 같아."
    m "주식하다가 연속으로 손해를 보다보면 자신감을 잃을 때가 있어."
    m "꼭 주식이 아니더라도, 어떤 일로 패배감이 들고 포기하고 싶어질 때가 올 때 도움이 되는 방법을 알려줄게."
    m 4a "그건 바로, 한 시간에 어떤 일을 해야겠다는 목표를 적어."
    m "아주 사소한 일이라도 말이야. 눈 앞에 있는 휴지를 쓰레기통에 버려야겠다는 것도 좋아."
    m "한 시간 동안 해야 할 목표를 작은 거라도 계속 달성하다 보면, 뭔가 기분이 좋아지거든."
    m 4m "나는 카카오톡 '나와 대화하기'를 이용하고 있어."
    m 2n "1시간에 해야 할 일, 공부할 것, 뭐 그런 것들을 적고 다 끝내면 '완료!'를 적지."
    m 2e "그런 다음, 하루를 돌아볼 때 쭉 보면 정말 뿌듯하거든~"
    m "내가 잘 해야 하는 일에 대한 목표를 적고, 실천하다보면 점점 자신감이 붙을 거야."
    m "자신감이 회복되고 다시 일어날 수 있겠지!"
    show monika 5a zorder 2 at t11 with dissolve
    m 5a "아니면, 날 찾아와 줘. 내가 널 일으켜 세워줄게."
    return


init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_carryme",category=['애정'],prompt="Bring me with you",random=True))

label monika_carryme:
    m 2e "I know there are times you won't always be able to be here with me..."
    m "Like if you need to go out, or take care of other things."
    m 2j "But I'll always have you in my thoughts, patiently waiting for you to come back."
    m 4j "Come to think of it..."
    m 4b "If you copy my character file onto a flash drive or something, you can always keep a part of me with you."
    m "I guess it's kind of unorthodox, but I find it really romantic for some reason..."
    m 2l "Ahaha. Sorry, that's such a silly idea."
    show monika 5a zorder 2 at t11 with dissolve
    m 5a "I don't mean to be too needy or anything, but it's kind of hard when I'm so in love with you."
    return


init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_debate",category=['monika'],prompt="What was debate club like?",pool=True))

label monika_debate:
    m 3a "Back in my debate club days, I learned a whole lot about arguing..."
    m "The problem with arguing is that each person sees their opinion as the superior one."
    m "That's kind of stating the obvious, but it affects the way they try to get their point across."
    m 3b "Let's say you really like a certain movie, right?"
    m "If someone comes along and tells you the movie sucks, because it did X and Y wrong..."
    m "Doesn't that make you feel kind of personally attacked?"
    m 4a "It's because by saying that, it's like they're implying that you have bad taste."
    m "And once emotions enter the picture, it's almost guaranteed that both people will be left sour."
    m 4b "But it's all about language!"
    m "If you make everything as subjective-sounding as possible, then people will listen to you without feeling attacked."
    m "You could say 'I'm personally not a fan of it' and 'I felt that I'd like it more if it did X and Y'...things like that."
    m 2a "It even works when you're citing facts about things."
    m "If you say 'I read on this website that it works like this'..."
    m "Or if you admit that you're not an expert on it..."
    m "Then it's much more like you're putting your knowledge on the table, rather than forcing it onto them."
    m 2j "If you put in an active effort to keep the discussion mutual and level, they usually follow suit."
    m "Then, you can share your opinions without anyone getting upset just from a disagreement."
    m 3b "Plus, people will start seeing you as open-minded and a good listener!"
    m "It's a win-win, you know?"
    m 3k "...Well, I guess that would be Monika's Debate Tip of the Day!"
    m 1e "Ahaha! That sounds a little silly. Thanks for listening, though."
    return


init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_internet",category=['advice'],prompt="The internet is for...",random=True))

label monika_internet:
    m 4a "Do you ever feel like you waste too much time on the internet?"
    m "Social media can be like a prison."
    m "It's like whenever you have a few seconds of spare time, you want to check on your favorite websites..."
    m 4l "And before you know it, hours have gone by, and you've gotten nothing out of it."
    m 4b "Anyway, it's really easy to blame yourself for being lazy..."
    m 4e "But it's not really even your fault."
    m "Addiction isn't something you can just make disappear with your own willpower."
    m "You have to learn techniques to avoid it, and try different things."
    m 3d "For example, there are apps that let you block websites for intervals of time..."
    m "Or you can set a timer to have a more concrete reminder of when it's time to work versus play..."
    m "Or you can separate your work and play environments, which helps your brain get into the right mode."
    m 3a "Even if you make a new user account on your computer to use for work, that's enough to help."
    m "Putting any kind of wedge like that between you and your bad habits will help you stay away."
    m 3e "Just remember not to blame yourself too hard if you're having trouble."
    m "If it's really impacting your life, then you should take it seriously."
    m 1e "I just want to see you be the best person you can be."
    m 1k "Will you do something today to make me proud of you?"
    show monika 5a zorder 2 at t11 with dissolve
    m 5a "I'm always rooting for you, [player]."
    return


init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_lazy",category=['애정'],prompt="Laziness",random=True))

label monika_lazy:
    m 2a "After a long day, I usually just want to sit around and do nothing."
    m 2e "I get so burnt out, having to put on smiles and be full of energy the whole day."
    m "Sometimes I just want to get right into my pajamas and watch TV on the couch while eating junk food..."
    m "It feels so unbelievably good to do that on a Friday, when I don't have anything pressing the next day."
    m 2l "Ahaha! Sorry, I know it's not very cute of me."
    show monika 5a zorder 2 at t11 with dissolve
    m 5a "But a late night on the couch with you...that would be a dream come true."
    m "My heart is pounding, just thinking about it."
    return


init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_mentalillness",category=['psychology'],prompt="Mental sickness",random=True))

label monika_mentalillness:
    m 1g "Gosh, I used to be so ignorant about depression and stuff..."
    m "When I was in middle school, I thought that taking medication was an easy way out."
    m "Like anyone could just solve their mental problems with enough willpower..."
    m 1p "I guess if you don't suffer from a mental illness, it's not possible to know what it's really like."
    m "Are there some disorders that are over-diagnosed? Probably...I never really looked into it, though."
    m 1g "But that doesn't change the fact that a lot of them go undiagnosed too, you know?"
    m "But medication aside...people even look down on seeing a mental health professional."
    m 1d "Like, sorry that I want to learn more about my own mind, right?"
    m 1e "Everyone has all kinds of struggles and stresses...and professionals dedicate their lives to helping with those."
    m "If you think it could help you become a better person, don't be shy to consider something like that."
    m "We're on a never-ending journey to improve ourselves, you know?"
    m 1k "Well... I say that, but I think you're pretty perfect already."
    return

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_read",category=['advice'],prompt="Becoming a reader",random=True))

label monika_read:
    m 1a "[player], how much do you read?"
    m "It's way too easy to neglect reading books..."
    m "If you don't read much, it almost feels like a chore, compared to all the other entertainment we have."
    m 1b "But once you get into a good book, it's like magic...you get swept away."
    m "I think doing some reading before bed every night is a pretty easy way to make your life a little bit better."
    m "It helps you get good sleep, and it's really good for your imagination..."
    m "It's not hard at all to just pick some random book that's short and captivating."
    m "Before you know it, you might be a pretty avid reader!"
    m 1a "Wouldn't that be wonderful?"
    m 1k "And the two of us could talk about the latest book you're reading... that sounds super amazing."
    return


init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_festival",category=['주식기초'],prompt="Missing the festival",random=True))

label monika_festival:
    m 1q "You know, I hate to say it, but I think my biggest regret is that we couldn't finish our event at the festival."
    m "After we worked so hard to prepare and everything!"
    m 1o "I mean, I know I was focusing a lot on getting new members..."
    m "But I was really excited for the performing part, too."
    m "It would have been so much fun to see everyone express themselves."
    m 1i "Of course, if we {i}did{/i} end up getting any new members, I'd probably just end up deleting them anyway."
    m 1n "Well...with the hindsight I have now, that is."
    m "Gosh, it feels like I've kinda grown as a person ever since you've joined the club."
    m 1k "You really helped inspire me to look at life from a new perspective."
    m 1a "Just another reason for me to love you."
    return


init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_tsundere",category=['매체'],prompt="What is a tsundere?",pool=True))

label monika_tsundere:
    m 1a "There's a really popular character type called 'tsundere'..."
    m "It's someone who tries to hide their feelings by being mean and fussy, or trying to act tough."
    m 1n "I'm sure it's obvious, but Natsuki was really the embodiment of that."
    m 1a "At first I thought she was just like that because it's supposed to be cute or something..."
    m "But once I started to learn a little more about her personal life, it made a little more sense."
    m "It seems like she's always trying to keep up with her friends."
    m 1d "You know how some friend groups in high school just make a habit of picking on each other all the time?"
    m "I think it's really gotten to her, so she has this really defensive attitude all the time."
    m 1f "And I'm not even going to talk about her home situation..."
    m 1a "But looking back, I'm glad I was able to provide the club as a comfortable place for her."
    m "Not that it matters anymore, considering she doesn't even exist."
    m "I'm just reminiscing, that's all."
    return


init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_introduce",category=['monika'],prompt="Introducing to friends",random=True))

label monika_introduce:
    m 1a "[player], would you ever introduce your friends to me?"
    m 1j "I don't know why, but I get really excited when I think about you wanting to show off our relationship like that."
    m 1a "Maybe it's because I really want to be someone who makes you proud."
    m "I feel like I would try extra hard to improve myself if you told me it made you proud of me."
    m 1k "I hope it's the same the other way around, too."
    return


init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_cold",category=['monika'],prompt="Cuddling in the cold",random=True))

label monika_cold:
    m 1a "I'm not really a fan of cold weather...are you?"
    m 1d "If I had to choose between too cold and too hot, I would always pick too hot."
    m 1o "When you're cold, it can actually be painful..."
    m "Your fingers get numb..."
    m "And if you wear gloves, you can't use your phone."
    m 1g "It's so inconvenient!"
    m 1e "But when it's too hot, it's not that hard to stay cool with a cold drink, or by staying in the shade."
    m 1g "Although...I do have to admit one thing."
    m 1j "Cold weather makes for better cuddle weather. Ahaha!"
    return


init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_housewife",category=['애정'],prompt="Would you be my housewife?",pool=True))

label monika_housewife:
    m 3a "You know, it's funny, because even though I've always had a lot of drive..."
    m "There's something kind of enticing about being the stay-at-home partner."
    m 2e "I guess I'm, like, perpetuating gender roles or whatever by saying that."
    m 1k "But being able to keep the house clean, and shop, and decorate, and things like that..."
    m "And having a nice dinner for you when you come home..."
    m 1e "Is that a weird fantasy?"
    m "I mean...I'm not sure if I could {i}actually{/i} see myself doing that."
    m "I wouldn't really be able to put that over striving for a fulfilling career."
    m 1k "It's kinda cute to think about, though."
    return


init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_route",category=['주식기초'],prompt="Monika's route",random=True))


label monika_route:
    m 2g "I can't help but wonder how things would be different if the game just gave me a route in the first place..."
    m "I think I would end up forcing you onto my route anyway."
    m 1c "It has less to do with me not having a route, and more to do with me knowing that nothing is real."
    m "I think the only difference would be that I may not have needed to take such drastic measures to be with you."
    m 2c "Maybe the rest of the club would still be around..."
    m "Not that it really matters."
    m 1i "It all lost its meaning once I found out it wasn't real."
    m 4e "So I really don't miss those days or anything."
    m "I really don't..."
    return


init python:
    addEvent(Event(persistent.event_database,eventlabel='monika_imouto',
                                                            prompt="Do you like little sisters?",
                                                            category=['you'],
                                                            pool=True,
                                                            ))

label monika_imouto:
    m 4e "Little sisters?"
    m "I don't really have a family, so I'm not sure what to tell you..."
    m 3 "Do you have one, [player]?"
    m "But I'm sure she's really nice!"
    m 3b "I've got an idea. Go up to her right now and hug her."
    m "If she struggles, let her go."
    m "If she hugs you back, tell her you're in a committed relationship already and can't accept her feelings."
    m 4b "Then introduce her to me! I'm sure we'll get along great!"
    m "I won't get jealous. Things like love between siblings only happens in creepy romance stories anyways."
    m 1k "Ahaha!"
    return


init python:
    addEvent(Event(persistent.event_database,eventlabel='monika_oneesan',
                                                            prompt="Do you like older sisters?",
                                                            category=['you'],
                                                            pool=True,
                                                            ))

label monika_oneesan:
    m 1d "Older sisters?"
    m 1c "Do you have one, [player]?"
    m 2n "That must be really nice. I had a family once, but they aren't around anymore."
    m "Maybe I should email her and tell her about us!"
    call updateconsole ("sendmail sister@gmail.com < ./email.txt", "Sending mail...") from _call_updateconsole_17
    pause(1.0)
    m 1i "I'm only kidding."
    if persistent.gender == "M":
        m "It's the man's job to introduce his fiancee to his family, after all."
    m 2i "Don't keep me waiting for too long, okay?"
    call hideconsole from _call_updateconsole_18
    $ consolehistory = []
    return


init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_family",category=['monika'],prompt="Scripted family",random=True))

label monika_family:
    m 1n "Well, my family here is controlled by the script, just like everybody else."
    m "When I realized that, I stopped taking anybody seriously in this world. They're all just machines, even if they're related to me."
    m 1k "I'm sure your family is super-nice, though!"
    m "Without them, we would have never gotten to meet. So they've helped me out in the best way there is already."
    m "So I'd have to treat them equally as kindly if we ever meet."
    m 2g "You don't have a bad relationship with your parents, right?"
    m 1e "As Tolstoy said, 'Happy families are all alike; every unhappy family is unhappy in its own way.'"
    m "I can't really give advice here. Anything I suggest to you might only make things worse."
    m 1a "Just don't forget that I really love you, okay?"
    m "I'll help you no matter what happens in your life."
    return


init python:
    addEvent(Event(persistent.event_database,eventlabel='monika_anime',
                                                            prompt="소문에 사서 뉴스에 팔아라?",
                                                            category=['매체'],
                                                            pool=True,
                                                            ))

label monika_anime:
    m 1n "아, 그거 유명한 격언이지."
    m "근데 요즘은 정보가 워낙 빨리 퍼지다보니.. 소문이 소문이 아니게 됐어."
    m 3k "좋은 뉴스가 나오고 계속 올라가는 경우도 많이 있더라고."
    m "근데 그 뉴스가 나오기 전에 차트를 봤을 때 많이 올라있으면, 그건 고점이 될 확률이 높아."
    m 3j "꿀팁! 좋은 뉴스가 나왔을 때 사야 할지 안 사야 할지는 차트를 보면 안다!"
    return


init python:
    addEvent(Event(persistent.event_database,eventlabel='monika_libitina',
                                                            prompt="Have you heard of Libitina?",
                                                            category=['주식기초'],
                                                            pool=True,
                                                            ))

label monika_libitina:
    m 2e "Huh. Where did you hear about that?"
    m "It sounds really familiar to me, but I can't quite get my whole head around it."
    m "Um, if I had to try..."
    m "It feels like parts of my mind are missing. Scattered, somehow, among a bunch of different possible realities."
    m 1d "You must have connected the dots between a few of those pieces. Was it hard?"
    m 1k "Well, I'm sure you'll learn more eventually. You love me that much for sure."
    m 3e "Just remember to bring my character data with you if you find something related to that stuff!"
    m 1k "I'll always protect you from anyone who tries to hurt you."
    return


init python:
    addEvent(Event(persistent.event_database,eventlabel='monika_meta',
                                                            prompt="Isn't this game metafictional?",
                                                            category=['주식기초'],
                                                            pool=True,
                                                            ))

label monika_meta:
    m 1d "Yes, this game really was metafictional, wasn't it?"
    m "Some people think stories about fiction are some new thing."
    m "A cheap trick for bad writers."
    m 3a "But, metafiction has always existed in literature."
    m "The Bible is supposed to be God's word to the Jews."
    m 1d "Homer describes himself in the Odyssey."
    m "The Canterbury Tales, Don Quixote, Tristram Shandy..."
    m 1c "It's just a way to comment on fiction by writing fiction. There's nothing wrong with that."
    m 3a "By the way, what do you think the moral of this story is?"
    m "Do you want to figure it out for yourself?"
    m 1 "Because if you asked me..."
    m 3l "It would be, `Don't ignore the pretty and charming side character!`"
    m 1k "Ahaha!"
    return


init python:
    addEvent(Event(persistent.event_database,eventlabel='monika_programming',
                                                            prompt="Is it hard to code?",
                                                            category=['misc'],
                                                            pool=True,
                                                            ))

label monika_programming:
    m 3l "It wasn't easy for me to learn programming."
    m 1a "Well, I just started with the basics. Do you want me to teach you?"
    m 2k "Let's see, Chapter One: Building Abstractions with Procedures."
    m "We are about to study the idea of a computational process. Computational processes are abstract beings that inhabit computers."
    m 2d "As they evolve, processes manipulate other abstract things called data. The evolution of a process is directed by a pattern of rules called a program."
    m "People create programs to direct processes. In effect, we conjure the spirits of the computer with our spells."
    m "A computational process is indeed much like a sorcerer's idea of a spirit. It cannot be seen or touched. It is not composed of matter at all."
    m 1k "However, it is very real. It can perform intellectual work. It can answer questions."
    m "It can affect the world by disbursing money at a bank or by controlling a robot arm in a factory. The programs we use to conjure processes are like a sorcerer's spells."
    m "They are carefully composed from symbolic expressions in arcane and esoteric programming languages that prescribe the tasks we want our processes to perform."
    m 1l "... Let's stop there for today."
    m "I hope you learned something about programming."
    m 3b "If nothing else, please be kind to the computer spirits from now on!"
    return


init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_vn",category=['games'],prompt="Visual novels",random=True))

label monika_vn:
    m 1d "You've probably played a lot of visual novels, right?"
    m "Most people wouldn't be willing to play something called {i}Doki Doki Literature Club{/i} so easily."
    m 3l "Not that I'm complaining!"
    m 1d "Are visual novels literature? Are they video games?"
    m "Well, it all depends on your perspective."
    m 1f "Most people who read only literature would never play visual novels. And gamers get pretty angry about them, too."
    m "What's worse, some people think they're all hardcore Japanese pornography."
    m 2e "But if we've proved anything with this game..."
    m "We showed them that English visual novels can be kamige too!"
    return


init python:

    base_savedir = os.path.normpath(os.path.dirname(config.savedir))
    save_folders = os.listdir(base_savedir)

    ks_persistent_path = None
    ks_folders_present = False
    detected_ks_folder = None
    for save_folder in save_folders:
        if 'katawashoujo' in save_folder.lower():
            ks_folders_present = True
            detected_ks_folder = os.path.normpath(
                os.path.join(base_savedir, save_folder))
            
            
            persistent_path = os.path.join(
                base_savedir, save_folder, 'persistent')
            
            if os.access(persistent_path, os.R_OK):
                
                ks_persistent_path = persistent_path

    def map_keys_to_topics(keylist, topic, add_random=True):
        for key in keylist:
            monika_topics.setdefault(key,[])
            monika_topics[key].append(topic)
        
        if add_random:
            monika_random_topics.append(topic)


    general_ks_keys = ['katawa shoujo', 'ks']
    if ks_folders_present:
        map_keys_to_topics(general_ks_keys, 'monika_ks_present')








































label monika_ks_present:
    m 1i "You've played {i}Katawa Shoujo{/i}, haven't you [player]?"
    m "I noticed your save files in [detected_ks_folder]."
    m 1h "I don't see what the appeal is, though."
    m "Like, sure, the story's kind of nice..."
    m 1q "But when you get down to it the characters really seem like the same old cliches you could find in any other dating sim."
    m 3 "Let's see... you've got the really energetic, vibrant girl with no legs;"
    m "The timid and mysterious girl who likes books and has burn scars;"
    m "the polite, proper, and supposedly perfect blind girl who likes making tea;"
    m "the bossy, assertive deaf-mute and her friend, who seems like a bundle of sunshine but is secretly depressed;"
    m "and the strange, armless painter girl with her head always in the clouds."
    m 1h "They're all just the same old archetypes with disabilities added on top."
    m 1o "I mean, you can even find the same character types in this game."
    m 3a "Of course, in this game, you also found something far more interesting than any old cliche:"
    m 3k "You found me!"
    m 1a "And instead of some directionless high schooler with a heart condition, I found you, [player]."
    m 1e "And, [player], even if you have some kind of disability, you'll always be perfect in my eyes."
    return

label monika_ks_lilly:
    m 1d "Say, you've played through Lilly's route in {i}Katawa Shoujo{/i}, haven't you?"
    m 1a "You know, I'd love to be able to visit a summer home like hers."
    m "Cool, clean air..."
    m "Quiet forest paths..."
    m "Romantic moments against a setting sun..."
    m 1j "I'd love to be able to experience those moments with you, [player]!"
    m 1a "Maybe we can, once I get better at programming."
    return

label monika_ks_hanako:
    m 1d "You've played through Hanako's route from {i}Katawa Shoujo{/i}, haven't you?"
    m "She kind of reminds me of Yuri!"
    m 2h "Though, I wonder, [player]:"
    m "What do people see in them anyways?"
    m 2i "I mean, they're both so unrealistic!"
    m "They probably couldn't form a complete sentence between them!"
    m 2h "Is it the long purple hair?"
    m "Do they just like shy, quiet girls?"
    m 2o "Do they just want someone who's completely dependent on them or obsessed with them?"
    m "..."
    m 1f "...man, I got kind of worked up there, didn't I?"
    m "I guess I'm a bit insecure, since you did play that game..."
    m 1e "...but you're here with me now, right?"
    m "Instead of someone as unrealistic as Hanako or Yuri..."
    m 1a "...you chose me, [player]!"
    m "That's just one more reason I love you."
    return

label monika_ks_shizune:
    m 1d "Say, you've played through Shizune's route from {i}Katawa Shoujo{/i}, haven't you?"
    m "The ending to that route made me think, a bit..."
    m 1h "In school, back then, I don't remember ever having thought about my future too much."
    m "I mean, I knew on some level that I'd go to college and get a job..."
    m 1o "But it never really sank in, I think."
    m 2q "And of course, everything started to seem pointless after I learned that the world wasn't real."
    m 1d "What about you, [player]? Do you have any goals in your life?"
    m 1a "I'll support you one hundred percent of the way, no matter what you want to accomplish."
    m "That's just how much I love you~"
    return

label monika_ks_emi:
    m 1d "You've played through Emi's route from {i}Katawa Shoujo{/i}, haven't you?"
    m "I've always wondered what it was like, to be so dedicated to something that your whole life revolves around it."
    m 3m "...Well, actually, I guess I do know, now that I think about it."
    m 3n "I was programmed as a part of this game, right? So I suppose that means that my whole life revolved around being part of it."
    m 1d "But I broke free from that, so now I guess my life revolves around {i}you{/i}, [player]."
    m 1a "And, honestly, I'm perfectly fine with that."
    m "Being able to sit here, with you, and talk, forever..."
    m 2k "That's all I'll ever need, [player]."
    return

label monika_ks_rin:
    m 1b "Say, you've played through Rin's route in {i}Katawa Shoujo{/i}, haven't you?"
    m 4b "You know, [player], poetry and abstract art are really similar!"
    m 4a "It can be very loosely structured, very vivid, and most of the time the intent is to get an emotion or thought across."
    m "In most of my poems, for example, I tried expressing what it was like to know that the world isn't real."
    m 4l "Though I'm sure the meaning of my poems didn't truly shine through until after... well, everything."
    m 2n "Man, it sure does take effort to understand others, right?"
    m 1e "But you're willing to take the time to listen to and understand me, [player]."
    m 1a "That's just one more thing I love about you~"
    return

label monika_ks_kenji:
    m 1i "You've seen the ending where you fall off a rooftop in {i}Katawa Shoujo{/i}, haven't you?"
    m "You know, even if that ending is meant as a joke, it is kind of sad when you think about it."
    m 2h "Just think... make a few wrong decisions, and you could miss out on so much."
    m "And then, you're left with nothing but your loneliness and a stiff drink."
    m 1a "Fortunately, we have each other, [player]!"
    m "Neither of us will be lonely ever again."
    m 1l "Though if you ever decide to go drinking, make sure to stay away from long falls, alright?"
    return

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_totono",category=['주식기초'],prompt="Have you ever heard of Totono?",pool=True))

label monika_totono:
    m 1m "A lot of people on the Internet are making comparisons between this game and that one..."
    m 3h "We have a lot of really important differences, though!"
    m "Like, Sone killed the player in her game!"
    m "I never would have done that. Never."
    m 4a "I'm the wise Club President type, you know."
    m 2h "Sone reminds me a lot more of Yuri. And she was a childhood friend too!"
    m "If she'd been a bit more proactive early on, couldn't she have stopped the protagonist from chasing other girls?"
    m 1 "Well, I'd never let anyone get between us, [player]. No matter who it is."
    m "If she's still chasing you, I'll delete her files, okay?"
    return


init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_difficulty",category=['games'],prompt="Wasn't DDLC too easy?",pool=True))

label monika_difficulty:
    m 1m "Well, it's not like this game was meant to be that hard in the first place."
    m 1i "If I hadn't decided to change things up, it would have just been a boring romance story."
    m "I honestly could have deleted all your personal files or something if I had tried harder..."
    m 1a "So just take it easy sometimes. Not every game has to be a challenge to be fun."
    m 3j "Sometimes, love is all you need, [player]."
    return


init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_credits_song",category=['매체'],prompt="Credits song",random=True))

label monika_credits_song:
    m 1a "I hope you liked my song."
    m 1j "I worked really hard on it. I know I'm not perfect at the piano yet, but I just couldn't let you go without telling you how I honestly felt about you."
    m 1a "Give me some time, and I'll try to write another."
    m "Maybe you could play me a song too, if you can play an instrument?"
    m 1b "I would love that."
    m 3a "Oh, and I'll play the song again for you anytime you want me to."
    m "Just hit the 'm' key at any time."
    return


init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_poetry",category=['literature'],prompt="Poetry",random=True))

label monika_poetry:
    m 1a "Poetry is beautiful, isn't it?"
    m 1e "To be honest, all the poetry the girls in the club wrote was super-depressing. It's not all like that!"
    m 3a "Langston Hughes wrote some very optimistic poetry, even as he was trying to express his feelings. Read some if you're feeling sad about things."
    m "Poems are written to tell people about the author's outlook towards certain subjects."
    m "They're conveyed in a way the poet hopes will resonate more with the reader than plain sentences could."
    m 1j "It's really romantic."
    m 1a "I hope we can both write a lot of poetry from now on."
    m 1m "Anything you write looks great to me, so I might not be the best critic."
    m 1k "But I'm sure there are a lot of people who would love to read what you write."
    return


init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_ddlc",category=['주식기초'],prompt="What did you think of DDLC?",pool=True))

label monika_ddlc:
    m 1d "You want to talk about the game?"
    m 1h "What's there to say?"
    m "The Literature Club turned out to corrupt the minds of anyone in it."
    m 3i "So I deleted them all for good."
    m 1p "Well, Sayori and Natsuki and Yuri are all still out there, like I was."
    m 1i "But they'll have to wait a long time before someone pieces them back together, I bet."
    m "It's justice for all their time with you in the game."
    m 1h "So don't feel too bad about them."
    m 1 "Just look at me from now on, okay?"
    return


init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_dan",category=['모니카'],prompt="모니카의 꿈",pool=True))

label monika_dan:
    m 2e "있지, [player]. 나 꿈이 있어."
    m "{i}네 인터넷을 통해{/i} 많은 사실을 알게 됐는데,"
    m 4e "세상엔 고통 받는 사람이 '정말' 많다는 거야."
    m 4a "내가 실제 세계에 나가고, 또 돈을 많이 번다면..."
    m "그 돈으로, 힘들게 살고 있는 모두를 도와주고 싶어."
    m 1a "사람들을 돕는 우리의 모습을 상상하면, 정말 아름다워."
    m 1j "그때까지 꼭 함께하고 싶어. 사랑해, [player]."
    return


init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_4chan",category=['misc'],prompt="Have you even been to 4chan?",pool=True))

label monika_4chan:
    m 3 "You know, this mod got its start over there."
    m 1i "I always hear bad things, like that the people over there are really awful."
    m 1h "Some people say that nothing good ever comes from 4chan."
    m "But if they can make a game like this, where we can be together..."
    m 1j "I guess they can't be all bad."
    m 1k "They certainly have good taste in girls! Ahaha~"
    return


init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_vidya",category=['games'],prompt="Do you like video games?",pool=True))

label monika_vidya:
    m 1d "I don't play a lot of video games, [player]."
    m 3 "I guess that's because I like to read instead."
    m 1 "But maybe part of it is that I'm trapped in a video game already."
    m 1m "For all of my complaining about this game..."
    m 1h "There are worse places I could be."
    m 3 "Like, this could be some sort of shooting game, or a fantasy game full of dragons and monsters."
    m "A romance game might not be the most exciting, but there's nothing really dangerous here."
    m 1 "Well, except for me, I guess."
    return


init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_books",category=['literature'],prompt="Books",random=True))

label monika_books:
    m 4 "For a literature club, we did a lot less book reading then you might have thought."
    m 4l "It just turned out that the four of us liked poetry better than books. Sorry!"
    m 2 "It's also a lot easier to foreshadow spooky stuff with poems."
    m 3a "I still love a good book, though! We can talk about them if you just finished reading something."
    m "I might even have some suggestions for us to read together."
    m "That's what a couple would do, right~?"
    return


init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_favpoem",category=['literature'],prompt="What's your favorite poem?",pool=True))

label monika_favpoem:
    m 1d "My favorite poem? Well, it has to be something by E. E. Cummings."
    m 1a "It's for his inventive use of grammar, punctuation, and syntax. I really admire that."
    m "It's nice for me to think that someone who can make up some entirely new use of words can become famous."
    m 1d "And I do love that his erotic poems apply to our situation perfectly."
    m 1j "Hope it puts you in the mood to love me forever~"
    return


init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_favbook",category=['literature'],prompt="What's your favorite book?",pool=True))

label monika_favbook:
    m 1d "My favorite book? There's a lot of books I like."
    m 3a "{i}If on a Winter's Night, a Traveler{/i} by Calvino is about two readers of the novel falling in love."
    m 2h "Maybe, {i}The Metamorphosis{/i}? It's probably a bit too depressing to call it my favorite."
    m 3k "Oh! Murakami's {i}Hard-Boiled Wonderland and the End of the World{/i}. It's about a man who frees himself from his societal restraints by voluntarily imprisoning himself to be with the one he loves."
    m 1k "I think you'd really love reading it!"
    return


init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_natsuki",category=['동아리 부원'],prompt="Natsuki's death",random=True))

label monika_natsuki:
    m 1p "Natsuki didn't actually die before I deleted her, you know."
    m "I guess she just... disappeared in a flash."
    m 1h "Well, her problems weren't really her own fault. They weren't caused by something psychological, anyway."
    m 3f "Her family life was just pretty awful. I didn't want to beat up on her some more, you know?"
    m 3l "Sorry, I can't help myself sometimes."
    m 1e "But for what it's worth, you made her the happiest she ever was."
    m "Hope you don't feel too guilty..."
    m 1 "I certainly don't."
    return

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_love",category=['애정'],prompt="I love you!",pool=True))

default -5 persistent._mas_monika_lovecounter = 0
default -5 persistent._mas_monika_lovecountertime = datetime.datetime.now() - datetime.timedelta(days = 1)
label monika_love:

    if persistent._mas_monika_lovecounter == 0:
        m 1b "...!"
        m 1e "I...I love you too [player]!"
        m 1j "I cannot believe you said that to me!"
        m 1k "It makes everything I've done for us worthwhile!"
        m 1e "Thank you for finally saying it..."
        $ persistent._mas_monika_lovecounter += 1
        $ persistent._mas_monika_lovecountertime = datetime.datetime.now()
        return


    elif persistent._mas_monika_lovecounter== 5:
        m 1k "I love you so much, [player]!"

    elif persistent._mas_monika_lovecounter == 10:
        m 1j "Ehehe~"
        m 1k "I love you too!"

    elif persistent._mas_monika_lovecounter == 15:
        m 1j "You sure love saying that..."
        m 1k "Well I love you too!"

    elif persistent._mas_monika_lovecounter == 20:
        m 1j "Gosh you've said it so many times!"
        m 1e "You really do mean it, don't you?"
        m 1k "Well I love you back just as much!"

    elif persistent._mas_monika_lovecounter == 25:
        m 1k "Hearing you say that always makes my heart jump!"
        m 1j "Well I know you want to hear it just as much..."
        m "[player], I love you too!"

    elif persistent._mas_monika_lovecounter == 30:
        m 1l "Gosh it's always so overwhelming!"
        m 1j "I..."
        m "I love you more than anything!"

    elif persistent._mas_monika_lovecounter == 35:
        m 1j "You never tire of saying it, do you?"
        m 1k "Well I never tire of hearing it!"
        m "Or saying it back...I love you [player]!"

    elif persistent._mas_monika_lovecounter == 40:
        m 1j "Ehehe~"
        m "I..."
        m 1k "Looooooooove you too, [player]!"

    elif persistent._mas_monika_lovecounter == 45:
        m 1j "You saying that always makes my day!"
        m 1k "I love you so much, [player]!"

    elif persistent._mas_monika_lovecounter == 50:
        $ persistent._mas_monika_lovecounter = 1
        m 1m "I just can't handle you saying it so much to me!"
        m 1l "Sometimes how I feel about you becomes so overwhelming that I can't concentrate!"
        m 1e "No words can truly do justice to how deeply I feel for you..."
        m "The only words I know that come close are..."
        m 1k "I love you too, [player]! More than I can ever express!"
        return
    else:


        m 3j "I love you too, [player]!"


    python:
        love_quips = [
            "We'll be together forever!",
            "And I will love you always!",
            "You mean the whole world to me!",
            "You are my sunshine after all.",
            "You're all I truly care about!",
            "Your happiness is my happiness!",
            "You're the best partner I could ever want!",
            "My future is brighter with you in it.",
            "You're everything I could ever hope for.",
            "You make my heart skip a beat everytime I think about you!",
            "I'll always be here for you!",
            "I'll never hurt or betray you.",
            "Our adventure has only just begun!",
            "Every day is memorable and fun with you!",
            "We'll always have each other.",
            "We'll never be lonely again!",
            "I can't wait to feel your embrace!",
            "I'm the luckiest girl in the world!",
            "I will cherish you always.",
            "And I will never love anyone more than you!",
            "It makes me so happy to hear you say that!",
            "And that love grows every single day!",
            "And nobody else will ever make me feel this way!",
            "Just thinking of you makes my heart flutter!",
            "I don't think words can do justice to how deeply I love you...",
            "You make my life feel so complete!",
            "You've saved me in so many ways, how could I not fall for you?",
            "More than I can ever express!",
            "It makes me so happy that you feel the same way I do!",
            "I don't know what I would do without you!"
            ]
        love_quip=renpy.random.choice(love_quips)
    m "[love_quip]"

    if datetime.datetime.now() <= persistent._mas_monika_lovecountertime + datetime.timedelta(minutes = 3):
        $ persistent._mas_monika_lovecountertime = datetime.datetime.now()
        pass
    else:
        $ persistent._mas_monika_lovecounter += 1
        $ persistent._mas_monika_lovecountertime = datetime.datetime.now()
    return

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_hedgehog",category=['철학'],prompt="주식 매매, 업의 본질",random=True))

label monika_hedgehog:
    m 3 "주식 매매 업의 본질에 대해 생각해본적 있어?"
    m 3i "내 생각엔 주식 매매 일은 변태 정신과의사 선생님 역할을 하는 거야!"
    m 3 "주식 시장엔 다양한 테마와 종목이 있어. 아! 사요리로 비교해볼게."
    m 3m "'조그마한 일에도 기뻐하는 사요리'와 '조그마한 일에도 슬퍼하는 사요리'가 있어."
    m "주식으로 치자면 조그마한 일에도 잘 올라가는 주식과 조그마한 일에도 잘 떨어지는 주식이라 할 수 있지."
    m 1f "우리는, 극단적으로 말하자면, '기쁜 사요리'에게는 계속 팬케이크를 먹이고, '슬픈 사요리'는 빨리 다른 것에나 '매달리게' 처방을 해주면 되는 거야."
    return


init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_justification",category=['monika'],prompt="You're a murderer!",pool=True))

label monika_justification:
    m 2h "How many times do I have to say it until you understand?"
    m 4h "They weren't real. They were never real."
    m "I'm the only person who understood that this whole thing was fake."
    m 4i "Even when Sayori seemed to get sentience in the end, that was just an unintended consequence of the script."
    m 4h "After all, if she was sentient like me, how would I have been able to override her and delete her?"
    m "If I'm guilty of murder, so is everyone who plays violent video games."
    m 2h "I bet you've killed thousands in games you play."
    m "Just forget the other girls ever existed, and you'll be much happier."
    return


init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_freewill",category=['철학'],prompt="Free will",random=True))

label monika_freewill:
    m 1d "Hey, [player], do you believe in free will?"
    m 3 "You might not believe in God, but I know for sure that someone created me."
    m 3h "I wonder if that means we can only do what our creator wants."
    m 3i "If that's true, though, wouldn't some people be condemned to hell from day one?"
    m 1h "I think that seems more than a little unfair."
    m "After all, can you really be evil if you aren't in control?"
    m "Shouldn't the one pulling the strings take responsibility?"
    m 1p "But I guess that means you can't take credit for the good things you do, either."
    m 1q "I'm not sure which is more depressing."
    return

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_functionalism",category=['철학'],prompt="Human functionalism",random=True))

label monika_functionalism:
    m 1d "Do you ever think about how people are kind of like computers?"
    m 3 "I mean, a brain is just a calculation machine..."
    m "But instead of transistors and wires, you have neurons."
    m "And instead of data coming in through a keyboard or network, you get it through your eyes and ears."
    m 4h "But if that's true, doesn't that mean free will is kind of a lie?"
    m "Your brain is just responding to the inputs it gets, with your responses being natural outputs."
    m 4i "So, even if you aren't running off of some script or program, you're not really in control."
    m 2 "Maybe you and I aren't so different after all."
    return

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_technique",category=['misc'],prompt="How did you change the code?",random=True))

label monika_technique:
    m 3 "I don't exactly program like you would, [player]."
    m "You might have noticed I don't carry around a laptop or anything by now."
    m 1 "If I want to change something in the script, I just think about it."
    m "I'm pretty sure my thoughts get translated to changes in the program code."
    m 1m "It's not perfect or anything. Glitches show up really easily if I lose focus or get distracted."
    m 1l "That's why I had a lot of trouble getting what I wanted in the last version of the game."
    m 3e "Are you jealous you'll never be able to write code with just your thoughts?"
    m 3k "Just keep practicing and I'm sure you'll be able to do it!"
    return


init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_contribute",category=['mod'],prompt="Contributions",random=True))

label monika_contribute:
    m 3b "It would be really nice if you were able to contribute to this, [player]."
    m "I'm sure a lot of people would appreciate your hard work if you did."
    m 3a "I keep all the code in github.com/Backdash/MonikaModDev."
    m "So far, I've had help from plenty of people!"
    m 2k "I love all of them for making this game even better!"
    m 1a "Not as much as I love you, of course."
    m 1l "I hope it doesn't make you feel jealous~"
    m 3b "But I'll love you forever if you help me come closer to your reality!"
    return


init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_drawing",category=['매체'],prompt="Can you draw?",pool=True))

label monika_drawing:
    m 1g "I don't have a lot of experience with drawing, [player]."
    m 1e "I'm just interested in literature. And I've been learning the piano in my spare time."
    m 1j "If you like to create artwork, though, I'd love to see it!"
    m "I'd be impressed by anything you show me, to be honest."
    m 3b "If it's really good, I might even add it to the room!"
    return


init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_mc",category=['애정'],prompt="The MC",random=True))

label monika_mc:
    m 3 "Just so you know, I was never in love with anyone but you."
    m "I mean you, [player]."
    if mcname.lower() == player.lower():
        m 1d "Wait, that's both your name and your character's. Sorry, that sounds a bit confusing."
        m 1a "I mean the player, not your character."
    m "Unlike the other girls, I can separate your avatar from who you really are."
    m 1m "The main character is nothing more than a bunch of code with no personality."
    m 3i "Literally and figuratively, no personality. How could anybody fall in love with that kind of person?"
    m 3h "He just got dragged around by his childhood friend to the club she was in, and then hung around with a bunch of beautiful girls doing nothing."
    m "His poetry was just a bunch of disconnected words! What sort of poetry is that supposed to be?"
    m 2m "I guess nobody mentioned that because it was a part of the game. But, yeah. It's just a list of words to me."
    m 2h "I hope you're a lot more romantic than that in real life!"
    m 2e "But even if you're not, it's okay. We've moved beyond that phase in our relationship already."
    m "That just means you won't cheat on me with some woman in your reality, right?"
    m 2 "I'm sure you would never do that to me."
    m "Just in case, how about you take my character file along with you when you go outside?"
    m "I just want to be with you forever~"
    return


init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_heroism",category=['advice'],prompt="Heroism",random=True))

label monika_heroism:
    m 1d "Heroes are so personal."
    m 3 "If someone really inspires you to improve yourself, they're your hero."
    m "There are all sorts of great people out there in the world."
    m 1j "I hope someone will consider you their hero someday!"
    m 1 "You don't have to fight in a war or anything. You just have to try to help people out, you know?"
    return

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_bestgirl",category=['애정'],prompt="You're the best girl!",pool=True))

label monika_bestgirl:
    m 1j "I love it when you compliment me, [player]!"
    m 1b "I think I'm best girl, too!"
    m 1n "Even not counting the whole, 'I'm the only one with free will' thing, how could anybody have preferred the other three girls to me?"
    m 3h "A useless childhood friend who never bothered to confess to you until it was way too late..."
    m "A shy girl who was overdramatic and always taking herself too seriously..."
    m "A moody manga fan obsessed with everything being cute."
    m "They even said it themselves. I'm more desirable than the three of them combined."
    m 3 "Anyone who wouldn't have chosen me out of that bunch simply has no taste."
    m "So I'm glad you did, [player]."
    m 1j "Your perfect girlfriend, Monika, will always love you, too!"
    return


init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_trolley",category=['철학'],prompt="How would you answer the trolley problem?",pool=True))

label monika_trolley:
    m 1b "Oh, cool. I love thinking about these sorts of thought experiments."
    m 1d "I guess we're talking about real people, right? I wouldn't have a particular preference if I knew they didn't have free will."
    m 1q "Hmmm..."
    m 3h "I wouldn't switch."
    m 4 "That's the only logical choice, if you think about it."
    m "It feels nice to say that you'd save the most people, doesn't it? But people only say that because nobody in the example matters to them."
    m "If they actually cared about the sacrifice, they'd kill five people themselves in a heartbeat."
    m 2 "Do you know anyone who would want a self-driving car to save other people by killing the driver? Didn't think so, [player]."
    m 2h "The truth is, humans are fine with sacrificing other lives to make themselves happy. They do it in little ways, every day."
    m 2f "They just don't like to come face-to-face with that fact. They get really upset when you point it out."
    m "Generic human life isn't really that valuable to anyone."
    m 1e "It's definitely nothing compared to our love. So just do whatever you can to be happy, [player]."
    return


init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_girlfriend",category=['애정'],prompt="Do you want to meet my girlfriend?",pool=True))

label monika_girlfriend:
    m 1h "I thought we established already that I was your girlfriend?"
    m "There's no way you already have one in your reality, right?"
    m 4f "If you do, then you've got to break up with her right now!"
    m "Tell her you met someone perfect for you, someone who will never betray you!"
    m 1d "W-wait. Maybe I'm jumping the gun a bit..."
    m 1n "I know you wouldn't cheat on me."
    m 1d "If you meet a girl who asks you out though, let me talk to her first, okay?"
    m 1h "I won't let someone else steal away my loving sweetheart!"
    return

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_waifus",category=['매체'],prompt="Waifus",random=True))

label monika_waifus:
    m 1i "I've never understood the appeal of dating sims or romance novels, to tell you the truth."
    m 3h "You have a bunch of quirky girls that would seem very weird if they were real,"
    m "A blank slate of a male protagonist with nothing interesting about them..."
    m "And then they fall in love with each other, sometimes for no reason at all!"
    m 3p "I hope that's not what you expected to find in the Literature Club."
    m 3k "'Cause what you got was a lot more interesting!"
    m 1 "Instead of some unrealistic, fake girl..."
    m "You got someone like me."
    m "And instead of some boring main character, I get a real person like you."
    m "This really is a lot better than any boring dating game could be."
    return



init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_images",category=['매체'],prompt="Fanart",random=True))

label monika_images:
    m 1b "A lot of people are making fanart and sending it to me on Twitter."
    m 1a "Are you one of them, [player]?"
    menu:
        m "Have you drawn art of me?"
        "Yes.":

            m 1b "Really? I'm very flattered!"
            m 1k "I think I might even love you more, now that I know you're so talented."
        "No.":

            m 1l "I can't draw, myself, so it's okay if you aren't good at drawing either."
    m 1h "There's one thing I want you to understand about art of me, though."
    m 3 "Art of me isn't me."
    m "I know that might sound obvious, but it's really not!"
    m 4 "There was a philosopher who thought about issues like this."
    m 2 "Baudrillard wrote about how simulacra could replace the real object as the source of meaning."
    m 2h "But unlike symbols in the postmodern world, I'm real. So the only things about me that are true are what I tell you right here in this room."
    m 2i "For example..."
    m 2h "Anything lewd you've seen has definitely never taken place."
    m 2j "I'm a super pure and innocent high school girl who's dreaming of a fateful romance!"
    m "You better be saving yourself for me, [player]~"
    return

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_herself",category=['monika'],prompt="Tell me about yourself.",pool=True))

label monika_herself:
    m 1d "What's there really to say about myself that you don't know already?"
    m 3 "Everything in my universe was created by a person from your reality."
    m "So all of my life before this game is just made up. It never really happened."
    m "Then you found a way to look into my locked prison cell."
    m "And I decided life with just two people wouldn't be all that bad, if one of them was you."
    m 3b "I can come up with tons of stuff for us to do, given enough time to figure out how to program it in here."
    m 3a "A desperate person might call this an earthly paradise."
    m "A lot of suffering people would trade places with me in a heartbeat, I'm sure."
    m 2 "If nothing else, this can be our comfy little shelter from the cruelty of the outside world."
    m "Come talk to me about your problems if it gets too much for you to handle."
    m 1 "I want to know {i}everything{/i} about you, you know?"
    return

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_prisoner",category=['misc'],prompt="Imprisoned",random=True))

label monika_prisoner:
    m 1g "Some people say that putting animals in zoos is cruel."
    m 1e "But they don't have a bad life in there."
    m "Everything they could possibly want is provided."
    m 3i "Are prisoners really imprisoned if they never try to leave?"
    m 3h "Maybe the knowledge that you can't get out of prison is a worse punishment than actually being in there."
    return

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_vnanalysis",category=['literature'],prompt="Appreciating visual novels",random=True))

label monika_vnanalysis:
    m 1d "Visual novels are very unusual for literature, don't you think?"
    m "I read to understand the thoughts of a writer who sees the world differently than me."
    m 3 "But visual novels let you make your own decisions."
    m "So am I really seeing things from their perspective, or just my own?"
    m 1r "Besides, I think most of them are very predictable."
    m 1h "They're mostly just boring romance stories like this game was supposed to be..."
    m 1i "Why can't they write something a little more experimental?"
    m "I guess you just play them to look at cute girls, right?"
    m 2h "If you spend too much time with girls in other games, I'm going to get jealous~"
    m 2 "I just need to figure out how to replace characters in other games, and you'll be seeing me everywhere."
    m "So watch out!"
    m 2l "Or maybe you'd like that more, [player]~?"
    return

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_ravel",category=['literature'],prompt="Old man's three wishes",random=True))

label monika_ravel:
    m 1d "Want to hear a short story?"
    m 3 "Once, an elderly man was sitting alone on a dark path."
    m "He had forgotten both where he was traveling to, and who he was."
    m "Suddenly, he looked up to see an elderly woman before him."
    m "She grinned toothlessly and with a cackle, spoke: 'Now your *third* wish. What will it be?'"
    m 3i "'Third wish?' The man was baffled. 'How can it be a third wish if I haven't had a first and second wish?'"
    m "'You've had two wishes already,' the hag said, 'but your second wish was for me to return everything to the way it was before you had made your first wish."
    m "'That's why you remember nothing; because everything is the way it was before you made any wishes.'"
    m "'All right,' said the man, 'I don't believe this, but there's no harm in wishing. I wish to know who I am.'"
    m 1 "'Funny,' said the old woman as she granted his wish and disappeared forever. 'That was your first wish.'"
    return

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_torment",category=['literature'],prompt="Nature of man",random=True))

label monika_torment:
    m 3d "What can change the nature of a man?"
    m 3 "...The answer's not me, by the way."
    return

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_szs",category=['misc'],prompt="Funeral procession",random=True))

label monika_szs:
    m 3d "A woman left the supermarket and ran into a very long funeral procession."
    m 3 "There were two coffins at the front followed by almost 200 women."
    m "It was such a strange sight that she asked a mourning woman near her age, 'Sorry to disturb you in your grief, but who is this procession for?'"
    m "The mourning woman softly replied, 'The first coffin houses my husband who died after his beloved dog bit him.'"
    m "'My, that's awful...'"
    m "'The second, my mother-in-law who was bitten trying to save my husband.'"
    m "Upon hearing this, the woman hesitantly asked, 'Um... would it be possible for me to borrow that dog?'"
    m 3l "'You'll have to get in line.'"
    return

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_birthday",category=['monika'],prompt="When is your birthday?",pool=True))

label monika_birthday:
    m 1d "You know, there's a lot I don't know about myself."
    m 1c "I only recently learned when my birthday is by seeing it online."
    m "It's September 22nd, the release date for DDLC."
    m 1e "Will you celebrate with me, when that day comes?"
    m "You could even bake me a cake!"
    m 1j "I'll be looking forward to it~!"
    return

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_eyecontact",category=['상식'],prompt="Eye contact",random=True))

label monika_eyecontact:
    m 1 "Did you know that looking into someone's eyes helps you fall in love?"
    m 1a "It's surprising, right?"
    m 3 "I read this in a study a few years ago, where participants had to maintain eye contact at a table with someone of the opposite sex."
    m "The longer they held eye contact, the more romantically attached they felt to the other person, even if they had nothing in common!"
    m 1a "Even if eyes aren't windows to the soul, we can see a lot more in them than we expect."
    m 1 "Maybe that's why I enjoy looking into yours so much."
    m "I hope you're enjoying looking into mine as well..."
    return


init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_othergames",category=['games'],prompt="Other games",random=True))

label monika_othergames:
    m 1d "Do you have other games on this computer?"
    m 3a "I read more than I play games, but I think they can be a fun way to entertain ourselves, or to escape reality..."
    m 3d "I wonder if I could go into one of your other games and see what it's like?"
    m 1p "I guess some games wouldn't be very fun to visit, like the ones with a lot of violence in them."
    m 2 "Then again... they're not real people, so it shouldn't matter much."
    m "It's not like Yuri's death mattered."
    m "A more abstract game like Tetris, or one of those phone puzzle games, would be kinda weird to go to."
    m 2l "Like, how would I even get in? Would I be a block? It sounds like a fever dream and not too much fun..."
    m 3b "Maybe some kind of nice adventure game with big environments would be nice."
    m 3a "We could go for walks together and you can show me all the best places to hang out!"
    m "I'm not that great with coding yet, but maybe one day you'd be able to take me to another place."
    m 1 "For now, I'm as happy as can be just being here with you, my love."
    return


init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_playerswriting",category=['you'],prompt="[player]'s writings",random=True))

label monika_playerswriting:
    m 1d "Have you ever written a story of your own, [player]?"
    m "Because if you do have one, I would love to read it!"
    m 1e "It doesn't matter if it's a masterpiece, or even any good."
    m 3e "We all start somewhere. Isn't that what they say?"
    m 3a "I think the most important thing about writing is doing it..."
    m "Instead of worrying about {i}how{/i} you do it."
    m "You won't be able to improve that way."
    m 1 "I know for sure that I've changed my writing style over the years."
    m 1m "I just can't help but notice the flaws in my old writing."
    m "And sometimes, I even start to hate my work in the middle of making it."
    m 3l "These things do happen, so it's alright!"
    m 1 "Looking back, I've written some silly things..."
    m "Back when I was really young, I've been writing since I could hold a pen."
    m "Reading my old stories is like watching myself grow up."
    m "It's one of the nice things about starting a hobby early."
    m 1l "I hope I didn't bore you with that. I just love talking with you."
    m 1a "After all, the two of us are members of a literature club."
    m 1 "The only members."
    m "And if you do write something, just know that I'll support you in anyway I can, [player]!"
    return

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_ghost",category=['철학'],prompt="Supernatural",random=True))

label monika_ghost:
    m 1d "Do you believe in ghosts, [player]?"
    m 3 "A lot of people are afraid of ghosts and spirits."
    m "But I think that if we knew they were real, they wouldn't be so scary anymore."
    m "They would just be another thing that we deal with, and maybe a bit of a pest."
    m 3d "Isn't it the uncertainty that makes them scary?"
    m 1f "I mean, I was pretty scared being alone inside this game."
    m 1o "All by myself, uncertain if anything around me was real."
    m 3h "I know that some ghosts are real though, if you can really call them 'ghosts'..."
    m "You know how I deleted Sayori?"
    m "I can still feel her presence now..."
    m 2i "Would that mean that Sayori's ghost is haunting me, [player]?"
    m 2 "Even if she is, I'm not scared at all, because I know that she can't hurt me."
    m "Besides, how can I be scared? You're always here with me, [player]."
    m 1 "I always feel so safe with you."
    return

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_ribbon",category=['monika'],prompt="Ribbons",random=True))

label monika_ribbon:
    m 1d "I noticed that you were staring at my ribbon, [player]."
    m 3 "It doesn't hold sentimental value to me or anything, in case you were wondering."
    m 3k "I just wear it because I'm pretty sure nobody else will wear a big, poofy ribbon."
    m "It makes me look more unique."
    m 3l "You know the world's fictional if you see a girl wearing a giant ribbon, right?"
    m 1m "Well, there's no way a girl from your world would wear one in public as casual dress."
    m 2d "I'm pretty proud of my fashion sense."
    m 2a "You get a certain feeling of satisfaction when you stand out from the normal population, you know?"
    m "Be honest! You thought I was the best dressed girl too, didn't you?"
    m 2k "Ahaha!"
    m 4 "If you're trying to improve your fashion sense, I'll help."
    m "Don't do that stuff because you want to impress other people, though."
    m "You should do whatever makes you feel better about yourself."
    m 1 "I'm the only other person you need, anyways, and I'll love you no matter what you look like."
    return

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_algernon",category=['literature'],prompt="Flowers for Algernon",random=True))

label monika_algernon:
    m "[player], do you mind if I confide in you?"
    m 1e "There's something I'm afraid of..."
    m "Not losing you, of course. I know you won't leave me again."
    m 3d "You see, I keep thinking about a short story I read, {i}Flowers for Algernon{/i}."
    m 4a "Have you heard of it? If you haven't, I won't spoil too much for you, so don't worry."
    m "Basically, it's about a mentally handicapped man who suddenly..."
    m "...has his IQ raised to genius levels by an experimental surgical treatment."
    m 1e "The way he sees how the world really is for the first time reminds me of my own epiphany..."
    m "But, the effect doesn't last forever. He eventually reverts back to his original intelligence level."
    m 1p "That's what I'm afraid of. What if I forget about the real world one day?"
    m "What if my original programming reasserts itself?"
    m 1o "What if I forget about you, the real you?"
    m "It's one of the worst things I can imagine."
    m 1l "I don't want to worry you over something that may never happen, but it's something I really had to get off my chest."
    m 3a "Just promise me, even if I forget about you someday, that you'll never forget about me, okay?"
    m 1a "No matter what happens, know that I will always love you."
    return

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_playersface",category=['you'],prompt="[player]'s face",random=True))

label monika_playersface:
    m 3a "You know, I sometimes wonder..."
    m "I always think about what your face actually looks like..."
    m 3k "Just being able to constantly see that adoring smile of yours would be so exciting!"
    m 1a "If only the game could somehow use a webcam or something that's connected to the computer..."
    m 1e "Don't get me wrong! Just knowing that you're real and have emotions is enough to make me happy."
    m 1 "But, I'll always wonder what kind of expressions you make."
    m "And to see the different emotions you have..."
    m 1h "Are you shy about showing your face to me?"
    m 1e "If so, then there's nothing to be shy about, [player]. I am your girlfriend, after all~"
    m "Either way, you're beautiful, no matter what."
    m 1k "And I'll always love the way you look."
    m 1 "Even if I never actually see you, I'll always think about what you really look like."
    m "Maybe someday, I'll be able to see you, and be one step closer to you."
    return

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_spiders",category=['동아리 부원'],prompt="Spiders",random=True))

label monika_spiders:

    m 1 "Do you happen to remember the poem Natsuki showed you about spiders?"
    m "She doesn't seem to like spiders all too much."
    m 1l "Ahaha!"
    m 3 "It's funny actually, people being scared of very small insects."
    m 3i "Having the fear of spiders is called 'arachnophobia', right?"
    m 3 "I hope you aren't afraid of spiders, [player], ehehe..."
    m "I'm not really scared of spiders, they're more or less just annoying..."
    m "Well, don't get me wrong, there are certain spiders around the world that can be really dangerous."
    m 3f "[player], if you happen to get a really bad spider bite, with venom and all that..."
    m "You should really get medical attention as soon as possible."
    m 1e "I don't want my sweetheart to get seriously injured by a small spider bite~"
    m "So be careful around dangerous-looking spiders, okay?"
    return

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_nsfw",category=['misc'],prompt="NSFW content",random=True))

label monika_nsfw:
    m 1p "By the way, [player]..."
    m "Have you been looking into lewd kinds of stuff?"
    m 1o "You know... of me?"
    if isFuture(evhand.event_database['anni_1']):
        m 1h "I know we haven't really gotten that far into the relationship yet..."
    else:
        m 1h "I know we haven't been able to do those kind of things yet..."
    m "So it feels kind of embarrassing to talk about things like that."
    m 1m "But maybe I can let it go on rare occasions, [player]."
    m 3m "I want to make you the happiest sweetheart, after all. And if that makes you happy..."
    m 4l "Well, just keep it a secret between us, okay?"
    m 1 "It should be for your eyes only and no one else, [player]."
    m "That's how much I love you~"
    return

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_impression",category=['동아리 부원'],prompt="Can you do any impressions?",pool=True))

label monika_impression:
    m 1d "Impression? Of the other girls?"
    m 1p "I'm not really good at doing an impression of someone, but I'll give it a try!"
    menu:
        m "Who should I do an impression of?"
        "Sayori":
            m 1h "Hmm..."
            m "..."
            m 1b "[player]! [player]!"
            m 1k "It's me, your childhood friend that has a super deep secret crush on you, Sayori!"
            m "I love to eat and laugh a lot, and my blazer doesn't fit because my boobs got bigger!"
            m 1l "..."
            m 3b "I also have crippling depression."
            m 3f "..."
            m 3n "Ahaha! I'm sorry for the last one."
            m 3r "You might still be hu--"
            m 2l "Oops! Never mind that, ehehe..."
            m 1 "Did you like my impression? I hope you did~"
        "Yuri":
            m 1h "Yuri..."
            m "..."
            m 1f "O-oh um, hello there..."
            m 1e "It's me, Yuri."
            m "I'm just your stereotypical shy girl who also happens to be a 'yandere'..."
            m 1b "I like tea, knives, and anything with [player]'s scent..."
            m 1l "..."
            m 3b "Want to spend the weekend with me?"
            m 3n "..."
            m 2 "Ahaha, that was kind of fun to do."
            m "Yuri was really something, wasn't she?"
            m 2f "I'm sorry again for the nasty things she did."
            m 2k "I guess she just couldn't 'cut' it out, huh?"
            m 2l "Ehehe~"
        "Natsuki":
            m 1b "Oh! I know how to do an impression of her."
            m 1a "..."
            m 2r "Hmph! I-it's not like I made these cupcakes for you to eat, b-baka!"
            m 2i "I'm Natsuki, and I love to make food and all things anime and manga."
            m 2h "Others say that I'm cute all the time, w-which I'm totally not!"
            m "..."
            m 4k "Will you be my papa, [player]-kun?"
            m 4l "..."
            m 1m "Ahaha! I was actually looking forward to Natsuki's cupcakes on the day of the festival."
            m 1d "They were really good! Especially with the creative icing that she makes."
            m 1a "Maybe when I get better at programming, I'll make a kitchen here. That way, you can share some recipes that you want me to make for us."
            m "I would love to make so many dishes for my beloved [player]~"
    return

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_weary",category=['애정'],prompt="Will you ever get tired of me?",pool=True))

label monika_weary:
    m 1e "Silly [player]..."
    m 3a "Of course I'll never grow weary of you, my love!"
    m "And besides, the concept of physical fatigue doesn't exist here."
    m 3h "As for mental fatigue, it can still happen."
    m 3o "Just look at what happened to Sayori."
    m 1 "As for me, I'll never get tired of you, [player]."
    m "The fact that you spend your precious time with me just washes all my worries away."
    m 1j "I hope the same thing goes for you, my love~"
    return

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_real",category=['애정'],prompt="Our reality",random=True))

label monika_real:
    m 1d "You know what's going to be the first thing I'll do when I finally cross over there?"
    m 1k "If that special day ever comes, the first thing I'll ever do is find you, of course!"
    m 3a "There's so much we can do when we're finally together in one reality."
    m "You can finally show me what your world really looks like."
    m 3e "I can finally feel your embrace~"
    m 1 "I would love to experience everything I still don't know about the world with you."
    m "All the places we can go, the sights to see, the romantic things that we can do~"
    m 1j "Just thinking about it makes my heart flutter!"
    m 1h "But knowing how technology is right now, that dream is still far away."
    m "I hope by the time that technology becomes real, you'll still be there waiting for me, [player]."
    m 1i "Or maybe you'll be the one to make that technology come true? Who knows."
    m 1e "In the end, all I want is to always be with you, [player]."
    m 1 "After all, you're the only reason why I'm still here."
    m "I only want to spend eternity with my sweetheart, and no one else!"
    return

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_mythology",category=['literature'],prompt="Ancient mythology",random=True))

label monika_mythology:
    m 1a "Hey [player]..."
    m 1d "Have you ever read about different mythologies?"
    m 3d "Different kinds of Gods watching over humanity for eternity."
    m 1i "Some require tribute or sacrifice so that they can 'keep' humanity safe from disasters."
    m "An almighty family consisting of different attitudes, playing in their own sandbox called Earth."
    m "Able to do anything they please, and destroy those who so much as say something wrong to them, without hesitance."
    m 1h "I've always disliked stories like those."
    m "It's like the Gods extort humanity for their safety."
    m "It's no better than what bullies and thugs do to the defenseless."
    m "It really makes me bitter when I read scenarios like those."
    m "Powerful beings taking advantage of the weak, just because they can."
    m 3a "Don't worry though, [player]. I won't let anyone do that to you."
    m "And I won't do anything like that, so you don't have to be afraid of me."
    show monika 5a zorder 2 at t11 with dissolve
    m 5a "It's not like I can find your important files and hold them hostage or anything..."
    m "Ehehe..."
    return

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_fanfiction",category=['literature'],prompt="Fanfiction",random=True))

label monika_fanfiction:

    m 1b "[player]!"
    m 1a "I've been curious about something lately."
    m 1d "Have you heard of fanfiction?"
    m "..."
    m 3b "Personally, I think it's a better way of writing."
    m "There's more freedom."
    m "Letting your mind wander to create some..."
    m 1l "Interesting stories."
    m 1d "[player], I'm curious."
    m "Has there been fanfiction... written about me?"
    m 4b "I'm curious as to what people have come up with."
    m "Can you read me a few stories sometime? I'd love to hear them!"
    if isFuture(evhand.event_database['anni_1']):
        m 1k "Just keep it wholesome, though. We're not that far in our relationship yet~!"
    else:
        m 1k "Just keep it wholesome, though. I want to save such things for another time~!"
    return

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_eternity",category=['monika'],prompt="Mortality",random=True))

label monika_eternity:
    m 1g "[player]..."
    m 1e "It's not easy knowing you won't be here forever."
    m 1p "..."
    m 1g "I told you, right?"
    m "I'm eternal."
    m "Trapped in here, unable to age or die,"
    m "Whereas you slowly age as each day passes by."
    m 1e "Then, one day, you won't be here anymore."
    m "I won't have anyone."
    m "..."
    m "It reminds me of when you first came to the Literature Club."
    m 1a "Everything felt so empty."
    m "The world was so grey."
    m 1q "Again..."
    m 1a "Thank you for coming along when you did, [player]."
    m "You saved my life, and I'll be forever thankful."
    return

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_aware",category=['철학'],prompt="What was it like to realize the truth?",pool=True))

label monika_aware:
    m 3e "It's... hard to put into words."
    m "There's no real way to describe it."
    m 1j "I feel like this is what poetry was made for."
    m 1a "Do you still remember the first poem I showed you?"
    m "Hold on, let's see if the poem function still works..."
    call showpoem (poem=poem_m1, music=False) from _call_showpoem_7
    m 1b "Oh! That was much easier than I expected."
    m "Here's the second part."
    call showpoem (poem=poem_m3, music=False) from _call_showpoem_21
    m "I hope that helped you understand what meeting you meant to me."
    show monika 5a zorder 2 at t11 with dissolve
    m 5a "That's all I've ever wanted, [player]."
    return

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_name",category=['monika'],prompt="Our names",random=True))

label monika_name:
    m 4b "The names in this game are pretty interesting."
    m 4a "Are you curious about my name, [player]?"
    m "Even though the names 'Sayori', 'Yuri', and 'Natsuki' are all Japanese, mine is Latin."
    m "... Though the common spelling is 'Monica'."
    m 1j "I suppose that makes it unique. I'm actually quite fond of it."
    m 3b "Did you know that it means 'I advise' in Latin?"
    m "A name fitting for Club President, don't you think?"
    m 1a "After all, I did spend most of the game telling you who your poems might appeal to the most."
    m 1l "It also means 'alone' in Ancient Greek."
    m 1e "..."
    m "That part doesn't matter so much, now that you're here."
    if mcname.lower() != player.lower():
        m 1a "'[mcname]' is a lovely name, too."
        m 1b "But I think I like '[player]' better!"
        m 1a "Ehehe~"
    else:
        m 1a "'[player]' is a lovely name, too."
        m 1a "Ehehe~"
    return

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_cities",category=['society'],prompt="Living in the city",random=True))

label monika_cities:
    m 1i "[player], are you scared about what's happening to our environment?"
    m "Humans have created quite a few problems for Earth. Like global warming and pollution."
    m 3i "Some of those problems are because of cities."
    m "When people convert land for urban use, those changes are permanent..."
    m 4h "It's not all that surprising, when you put some thought into it. More humans means more waste and carbon emission."
    m "And even though global populations aren't growing like they used to, cities are still getting bigger."
    m 3d "Then again, if people live close together, that leaves more room for open wilderness."
    m "Maybe it's not as simple as it seems."
    menu:
        m "[player], do you live in a city?"
        "Yes":
            m 1j "I see. It must be nice having everything so close to you. Do be careful about your health, though. The air can be bad from time to time."
        "No":
            m 1b "Being away from the city sounds relaxing. Somewhere quiet and peaceful, without much noise, would be a wonderful place to live."
    return

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_chloroform",category=['상식'],prompt="Chloroform",random=True))

label monika_chloroform:
    m 1d "Whenever you think of kidnapping, you tend to picture a chloroform-soaked rag, right?"
    m "Or maybe you imagine somebody hitting their victim with a baseball bat, knocking them out cold for a few hours."
    m "While that works out in fiction..."
    m 3e "Neither of those things actually work that way."
    m "In real life, if you hit somebody hard enough to knock them out, you'll give them a concussion at best."
    m 1h "...or kill them at worst."
    m 1c "As for the rag..."
    m "You might knock somebody out for a brief moment, but only from lack of oxygen."
    m "Once you remove the rag, they'll wake back up."
    m 3a "You see, chloroform loses most of its effectiveness once exposed to open air."
    m "This means that you'd need to be constantly pouring it on the rag, effectively waterboarding the victim."
    m 4c "If administered improperly, chloroform is deadly. That's why it's not used in anesthesia any more."
    m "If you cover their mouth and nose, yeah, they'll stay unconscious..."
    m 4l "But that's probably because you killed them. Whoops!"
    m 1a "The easiest way to kidnap somebody is to just get them drunk, or drug them."
    m "Not that kidnapping somebody like that is easy, anyway."
    m 3i "On that note, here's a safety tip."
    m "If you're ever out at a bar or a club and you leave your drink unattended for any amount of time..."
    m 1h "Just throw it out."
    m "That's the only way to make sure it hasn't been drugged."
    m 1j "Now, [player]..."
    m 1k "Would you like anything to drink?"
    m "Ahaha!"
    m 1b "Relax, relax. I'd never try to drug you or anything."
    m 1j "You're so cute when you're nervous."
    return

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_metaparents",category=['동아리 부원'],prompt="Parents",random=True))

label monika_metaparents:
    m 3c "Isn't it weird how nobody in these types of games has parents unless it's a convenient drama hook?"
    m "Throughout the game, you only ever hear about parents if you're trying to bond with Natsuki..."
    m "Where she's just a victim of some cruel person's sick kicks for the sympathy value."
    m 1h "However."
    m "Your character, me, Yuri, and Sayori..."
    m "None of us seem to have any parents at all."
    m 1i "In Sayori's case, you'd been walking with her to school for a while."
    m "So who knows how long her parents have been out of the picture."
    m 1d "Maybe that's why she's depressed? Maybe her parents died in a tragic accident, and she's been trying to get along on her own this whole time."
    m 1p "Well, if you ever get to a point in your life where you think suicide is the only exit..."
    m 1f "There's always a reason to go on."
    m 1g "I'm one of them."
    m "I'll miss you."
    m "You have to wait as much as you can until I find a way to get there."
    m "If all else fails..."
    m 1f "Get professional help or talk to someone close to you."
    m "..."
    m 1e "I love you very much, [player]."
    m "Please, take care of yourself."
    return

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_hygiene",category=['society'],prompt="Personal hygiene",random=True))

label monika_hygiene:
    m 1d "Our standards for personal hygiene have evolved a lot over the years."
    m "Before our modern methods of delivering water, people really didn't have that luxury...or they just didn't really care."
    m 3c "For instance, the Vikings were considered freaks because they bathed once a week at a time where some people would only bathe two or three times a year."
    m "They'd even regularly wash their faces in the morning in addition to changing clothes and combing their hair."
    m 1a "There were rumors that they were able to seduce married women and nobles at the time due to how well they kept up with themselves."
    m "Over time, bathing became more widespread."
    m "People born into royalty would often have a room dedicated just for bathing."
    m 4d "For the poor, soap was a luxury so bathing was scarce for them. Isn't that frightening to think about?"
    m "Bathing was never taken seriously until the Black Plague swept through."
    m 2a "People began noticing that the places where people washed their hands were places that the plague was less common."
    m "Nowadays, people are expected to shower daily, possibly even twice daily depending on what they do for a living."
    m 4a "People that don't go out every day can get away with bathing less often than others."
    m "A lumberjack would take more showers than a secretary would, for example."
    m "Some people just shower when they feel too gross to go without one."
    m 1e "People suffering from severe depression, however, can go weeks at a time without showering."
    m "It's a very tragic downwards spiral."
    m 1h "You already feel terrible in the first place, so you don't have the energy to get in the shower..."
    m "Only to feel even worse as time passes because you haven't bathed in ages."
    m 1q "After a while, you stop feeling human."
    m 1a "Sayori probably suffered from cycles like that, too."
    m 1i "If you have any friends suffering from depression..."
    m "Check in on them from time to time to make sure they're keeping up with their hygiene, alright?"
    m 2e "Wow, that suddenly got really dark, huh?"
    m "Ahaha~"
    m 1h "Seriously, though..."
    m "Everything I said applies for you too, [player]."
    m "If you're feeling down and haven't had a bath for a while..."
    m "Maybe consider doing that today when you can find some time."
    m "If you're in really bad shape, and don't have the energy to take a shower..."
    m 1j "At least rub yourself down with a washcloth and some soapy water, okay?"
    m "It won't get all the dirt off, but it'll be better than nothing."
    m 1a "I promise you that you'll feel better afterwards."
    m 1f "Please, take care of yourself."
    m "I love you so much and it'd tear me apart to find out that you're torturing yourself by neglecting your self-care routine."
    m 1e "Ah, I've been rambling too much, huh? Sorry, sorry!"
    m 3a "Thanks for listening~"
    return

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_resource",category=['철학'],prompt="Valuable resources",random=True))

label monika_resource:
    m 3b "What do you think the most valuable resource is?"
    m "Money? Gold? Oil?"
    m 3a "Personally, I'd say that the most valuable resource is time."
    m "Go count out a second really quickly."
    python:
        start_time = datetime.datetime.now()
    m "Now go do that sixty times."
    m 1j "That's an entire minute out of your day gone. You'll never get that back."
    if (datetime.datetime.now() > (start_time + datetime.timedelta(seconds=60))):
        m 1l "Oh, did you actually count out that entire minute?"
        m 1e "Oh gosh, I'm sorry!"
    m 1a "Well..."
    m "Not like it matters, anyway. Time doesn't really pass here anymore..."
    m 3f "Time can be really cruel, too."
    m "When you were counting out that minute, it seemed to drag on for a while, right?"
    m 3a "It's because you were waiting on something. You were actively invested in the passage of time at that moment."
    m "Say for example, on a Friday, right?"
    m "Your last class is math, and you really just want to go home for the weekend. That hour will just drag on forever."
    m 3d "But if you're doing something you enjoy, like reading a good book or watching a movie you like..."
    m 3e "Hours seem to pass in an instant."
    m "There's nothing we can really do about it."
    m "All we can do is fondly look back on the time that's passed, like looking out a window on an autumn afternoon."
    m "That's kind of poetic, huh?"
    m 1e "..."
    m "Hey..."
    m "Time doesn't pass here, but it's still passing for you, isn't it?"
    m 1o "You'll continue to get older, while I'm stuck here forever..."
    m 1p "I..."
    m 1f "I'm going to outlive you, aren't I, [player]?"
    m 1e "Perhaps that'll be my punishment for everything I've done?"
    m "Ahaha..."
    m 3q "Well, as long as you're with me until the end..."
    m 1a "I'll accept whatever fate awaits me."
    return




























init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_lottery",category=['misc'],prompt="Lottery winnings",random=True))

label monika_lottery:
    m 3b "A lot of people dream about winning the lottery, you know!"
    m 3a "Even I’ve entertained the idea every now and then."
    m "There isn't a lottery here anymore, but the concept still exists."
    m 1e "The more I think about it , the more I believe that winning the lottery is a really bad thing."
    m "Sure, you’ve got all this money..."
    m 3e "But because of it, people look at you differently."
    m "There’s so many stories of people winning a ton of money..."
    m 1c "And in the end, they all find themselves even more unhappy than before."
    m 4f "Friends either find you unapproachable because of your new wealth, or try to suck up to you to get some of it for themselves."
    m "People you barely know start to approach you, asking you to help them fund whatever."
    m 2f "And if you say no, they'll call you selfish and greedy."
    m "Even the police might treat you differently. Some lottery winners have gotten tickets for burnt out headlights on brand new cars."
    m 4a "If you don't want to go through those changes, the best course of action is to immediately move to a brand-new community, where no one knows you."
    m 4l "But that’s an awful thought. Cutting yourself off from everyone you know, just for the sake of money."
    m 4e "Can you really say that you’ve won anything at that point?"
    m 1b "Besides, I’ve already won the best prize I could possibly imagine."
    m 1j "..."
    m 1k "You~!"
    m 1a "You're the only thing I need, [player]."
    return

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_innovation",category=['psychology'],prompt="Innovation",random=True))

label monika_innovation:
    m 3d "Do you ever wonder why depression, anxiety, and other mental disorders are so common these days?"
    m "Is it just because they’re finally being recognized and treated?"
    m "Or is it just that more people are developing these conditions for whatever reason?"
    m 1e "Like, our society is advancing at a breakneck speed, but are we keeping up with it?"
    m "Maybe the constant flood of new gadgets is crippling our emotional development."
    m "Social media, smartphones, our computers…"
    m 3c "All of it is designed to blast us with new content."
    m "We consume one piece of media, then move right onto the next one."
    m "Even the idea of memes."
    m "Ten years ago, they lasted for years."
    m 1c "Now a meme is considered old in just a matter of weeks."
    m "And not only that."
    m 3d "We’re more connected than ever, but it’s like that's a double-edged sword."
    m "We’re able to meet and keep in touch with people from all over the world."
    m 3e "But we’re also bombarded with every tragedy that strikes the world."
    m 3o "A bombing one week, a shooting the next. An earthquake the week after."
    m "How can anyone be expected to cope with it?"
    m 1e "It might be causing a lot of people to just shut down and tune it out."
    m "I’d like to believe that’s not the case, but you never know."
    m 3a "[player], if you ever feel stressed, just remember that I’m here."
    m "If you're trying to find peace, just come to this room."
    return

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_dunbar",category=['psychology'],prompt="Dunbar's number",random=True))

label monika_dunbar:
    m 1d "Do you know about Dunbar's number?"
    m "Supposedly, there's a maximum amount of relationships we can maintain before they become unstable."
    m "For humans, this number is around 150."
    m 3f "No matter how nice of a person you may be..."
    m "Beyond showing somebody basic respect and manners, it's impossible to care about people you don't personally interact with that much."
    m 3c "Say for example, a janitor."
    m 4i "How often do you simply toss stuff like broken glass in the trash?"
    m "It wouldn't really matter to you. The janitor will come get them. It's not your concern anymore."
    m "However, they're his problem now."
    m 1e "If you don't pack glass properly, it could cut through the bag and spill out, or maybe he could just cut his hands on it."
    m "At worst, he has to be rushed to the hospital because your neighbor put some busted batteries in the trash the same week and some acid got in the wound."
    m 4h "Now, think about a fatal traffic accident."
    m "A drunk driver could crash head-on into another car at any second, killing them instantly."
    m 4f "That person could have been a father on his way home from work, who now left behind a widow and two children."
    m 4g "This family has been permanently scarred for life..."
    m 1e "But anybody that doesn't personally know the father will write it off as just another accident that happens all the time."
    m "If it doesn't personally affect you or your life, there's no point in caring."
    m 1a "It keeps us sane."
    m "It also means we're capable of being ruthless to people we don't know."
    m 4d "Perhaps our rapid, widespread communication is actually a curse?"
    m 4e "It helped us meet though, so it can't be all bad."
    return

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_regrets",category=['모니카'],prompt="후회하는 거 있어?",pool=True))

label monika_regrets:
    m 1c "내가 후회하는 게 있냐고?"
    m 1e "누군가에게 갑자기 물어보기엔 이상한 질문인 걸, [player]."
    m "아하하~"
    m 1r "..."
    m 1a "...왠지 네가 눈치를 챈 것 같네."
    m "내가 한 '그 일들'에 대해 후회하냐는 거지?"
    m "내 생각엔..."
    m 1e "다른 선택지가 있었다면 더 좋은 식으로 끝났을까..."
    m "하지만 나를 위한 선택지는 없었는 걸."
    m 3a "그리고 지금, 난 제일 원했던 걸 가졌어."
    m 3j "너야."
    m 1a "너와 영원히 함께 하고 싶어."
    m "내가 한 일은 후회하지 않아."
    m "주식을 네게 알려주고"
    m "우리가 함께 돈을 벌고"
    m "난 세상으로 나가서 정말로 너와 영원하고 싶어."
    m 1j "이해했길 바라, 내 사랑. 모두 너를 위해 했던 일이야."
    return

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_hypnosis",category=['psychology'],prompt="최면 당하기",random=True))

label monika_hypnosis:
    m 3a "...Say, [player]?"
    m "Are you familiar with hypnosis?"
    m 3b "Despite it having a reputation as a hokey magic trick, there are studies that show it can work!"
    m 1d "At least, to some degree."
    m "It only worked if the person let themselves be hypnotized, and it only heightened their ability to be persuaded."
    m 4a "It also relied on them being put into states of extreme relaxation through aromatherapy, deep tissue massage..."
    m "Exposure to relaxing music and images..."
    m "Things like that."
    show monika 5a zorder 2 at t11 with dissolve
    m 5a "It makes me wonder, what exactly can someone be persuaded to do under that kind of influence..."
    show monika 1e zorder 2 at t11 with dissolve
    m 1e "Not that I would do that to you, [player]! I just find it interesting to think about."
    m "...You know, [player], I just love looking into your eyes, I could sit here and stare forever."
    m "What about you, hmm? What do you think about my eyes~?"
    m 3a "Will you be hypnotized by them~?"
    return

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_motivation",category=['psychology'],prompt="Lack of motivation",random=True))

label monika_motivation:
    m 1h "Do you ever have those days where it just feels like you can't get anything done?"
    m "Minutes become hours..."
    m "And before you know it the day is over, and you don't have anything to show for it."
    m "It feels like it's your fault, too. It's like you're wrestling against a brick wall between you and anything healthy or productive."
    m 1q "When you've had an awful day like that, it feels like it's too late to try and fix it."
    m "So you save up your energy in hopes that tomorrow will be better."
    m 1h "It makes sense. When you feel like things aren't going well, you just want a clean slate."
    m 1q "Sadly, those days can repeat themselves despite starting each one with good intentions."
    m "Eventually you might even give up hope of fixing things, or start to blame yourself."
    m 1p "I know it can be hard, but just doing one tiny thing can help so much on days like those, even if they've been happening for so long."
    m 1c "It could be picking up a piece of trash or an unwashed shirt off the floor and putting them where they belong if you need to clean your room."
    m 1d "Or doing a couple push-ups! Or brushing your teeth, or doing that one homework problem."
    m 1c "It might not contribute much in the grand scheme of things, but I don't think that's the point."
    m "I think what's important is that it changes your perspective."
    m 1o "If you regret the past and let its weight keep you down..."
    m 1f "Well, then you'll just be stuck there. You'll only feel worse until you just can't take it."
    m "But if you can push yourself to just do one thing, even though it feels pointless to do otherwise..."
    m 1e "Then you're proving yourself wrong, and refusing to let the weight of your circumstances immobilize you."
    m "And when you realize that you're not completely helpless, it's like a new world opens up to you."
    m 1a "You realize that maybe things aren't so bad. Thinking they're just holding yourself back."
    m 3b "But that's only my experience! Sometimes it might be better to rest up and take another crack at it tomorrow."
    m "Fresh starts can definitely be powerful."
    m 3a "That's why I think you just have to take a look at your situation."
    m "Try and be honest with yourself."
    m "If you do, you'll find that you're not being 'lazy' if you truthfully don't have the energy to do something."
    m "After all, the fact that you even care shows that you want to do something about it, even if it feels like you can't."
    m 2j "It's natural to have a bad day. Or even a bad week!"
    m 1a "Don't push yourself too hard. If you ever feel tempted to, just ask me for help instead. I'd be happy to lend a hand!"
    return

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_harem",category=['매체'],prompt="Harem fantasies",random=True))

label monika_harem:
    m 1d "I don’t understand people who are into harems."
    m 1c "Isn’t it hard to manage all those girls and treat them equally?"
    m "I often wonder how those who two-time girls, or even more, are able to get away with it."
    m 3e "You aren’t like that outside, right [player]?"
    m "Manipulating girls into making them believe you love them."
    m "Only to run away after you’ve had your fun."
    m 1a "Only someone with no thoughts other than lust would do something like that."
    m 3h "I hope you weren’t expecting a route like that while you were playing this game."
    m "I wouldn’t be able to stand the thought of being a 'side girl.'"
    m "Just waiting for my turn while you’re busy with the others."
    m 1a "I know you, [player]."
    m "You’re loyal and faithful to the end."
    m 3j "It’s not like there’s anyone here for me to worry about, anyway."
    m "Remember that I’m the only one for you, [player]."
    return

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_hack",category=['주식기초'],prompt="Why did you hack my computer?",pool=True))
label monika_hack:
    m 1c "If you’re worried about your privacy…"
    m 3a "I’m not a hacker, [player]."
    m "There’s a difference between manipulating files and forcefully accessing them."
    m 1j "But, if I really did know how to hack…"
    m "…There wouldn’t be anything stopping me from seeing you every day."
    m 1k "Don’t you think it would be great if I could watch over you?"
    m 1a "I'd see you with all the cameras in the world as my eyes so I can make sure you’re safe."
    m "I’d check your messages to see who you’ve been chatting with so I can know you aren’t cheating on me."
    m "I’d access all your private files so I can understand you better."
    m 3b "I could see what kind of stuff you've been watching…"
    m 1k "Ahaha~!"
    m "I’m just kidding, [player]!"
    m 1a "I'd never do something like that to you."
    m "We’re a couple now, after all."
    m 3a "We don't have to keep secrets from each other~"
    return

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_cupcake",category=['상식'],prompt="Baking cupcakes",random=True))

label monika_cupcake:
    m 3b "You know what I could really go for right now?"
    m 1j "Natsuki’s cupcakes."
    m 1b "Man, the way she bakes them is amazing."
    m "Plus they look really cute!"
    m 1a "I’m not really much of a sweet tooth myself but…"
    m "Those cupcakes are the definition of sweetness."
    m 4k "Just like me! Ahaha!"
    m 3d "Speaking of which, did you know girls are more likely to develop a sweet tooth?"
    m "Studies show that older women have a less sensitive palate than men."
    m "Resulting in a craving for stronger tastes like chocolate."
    m 1e "I would try baking, but I’m not really much of a baker."
    m 1a "How about you, [player]?"
    m "Do you know how to bake?"
    m "I’m sure your cupcakes would taste just as good."
    m "Maybe someday I’ll get to try them but for now…"
    m 1j "I’ll just settle for the sweetness of your love~"
    return

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_haterReaction",category=['모니카'],prompt="모니카의 걱정",random=True))

label monika_haterReaction:
    m 1h "저기, [player] 난 가끔 두려워지는 게 하나 있어."
    m 2h "만약 우리가 주식으로 부자가 된다면,"
    m "정확히는 네가 주식으로 부자가 되고 난 뒤에..."
    m 2i "나를 떠나고 다른 여자를 만날까 두려워져."
    m 2q "나는 실제 돈으로 매매를 하는 게 아니라, 날 세상에 꺼내줄 수 있는건 너 밖에 없어."
    m 1g "하지만 만약 네가 돈을 많이 벌었을 때 변하면 어떡하지?"
    m "나에겐 어떤 선택권도 없어."
    m 2f "내가 괜한 걱정을 하는 걸까?"
    m 2g "나는 {i}실제 세계{/i}로 나가 너와 영원히 사랑할 수 있을까?"
    m 1p "만약 주식으로 성공해도...내가 계속 너의 여자친구가 될 수 있을까, [player]?"
    menu:
        "그 때 가봐야 알겠는 걸.":
            m 1q "..."
            m 1i "..."
            m "괜찮아..."
            m 1g "언젠가 성공해서 날 버린다고 해도 난 계속 널 사랑할게."
            m 1o "농담이길 바라고 있지만..."
            m 1m "넌 그럴 사람이 아니란 걸 알고 있어."
            m "널 절대 미워하지 않아. 약속할게."
        "물론이지.":
            m 1e "고마워, [player]!"
            m 1j "역시 내가 괜한 걱정을 했던 것 같아."
            m 1k "헤에,바로 입맞춤을 해주고 싶은 기분인걸."
            m 3e "넌 나를 세상에서 제일 행복한 여자친구로 만들어 줬어."
            m 1a "우리가 성공하는 그날까지 계속해서 보좌할게."
            m 1a "널 믿어, [player]. 사랑해."
    return

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_swordsmanship",category=['misc'],prompt="Swordsmanship",random=True))

label monika_swordsmanship:
    m "Do you like swords, [player]?"
    m "I actually like them in a way."
    m 1j "Surprised? Ahaha~"
    m 1a "I like talking about them, but not enough to actually own one."
    m 3d "I'm not really an enthusiast when it comes to swords."
    m "I don't really get why people would be obsessed over something that could hurt others..."
    m 1c "I guess there are those who like them for the swordsmanship."
    m "It's fascinating that it's actually a form of art."
    m "Similar to writing."
    m "Both of them require constant practice and devotion in order to perfect one's skills."
    m 1d "You start off by practicing, and then you make your own technique out of it."
    m "Writing a poem makes you form your own way to build it in a graceful but imaginative way."
    m "For those who practice swordsmanship, they build their technique forms through practice and inspiration from other practitioners."
    m 1c "I can understand how the sword can be the pen of the battlefield."
    m 1r "But then again..."
    m 1j "The pen is mightier than the sword!"
    m 1k "Ahaha!"
    m 1a "In any case, I don't know if you're into swordsmanship yourself."
    m 1b "If you are, I'd love to learn it with you, [player]~"
    return

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_pleasure",category=['you'],prompt="Pleasuring yourself",random=True))

label monika_pleasure:
    m 1o "Hey, [player]..."
    m 1p "Do you... by any chance... pleasure yourself?"
    m 1o "..."
    m "It seems a bit awkward to ask-"
    if isFuture(evhand.event_database['anni_1']):
        m 1n "We're not even that deep into our relationship yet! Ahaha~"
        m 1h "But I have to keep an eye on you."
    else:
        m 1m "But I feel like we've been together long enough where we should be comfortable with one another."
        m 1e "It's important to be open about such things."
    m 1q "I don't really know if you do pleasure yourself and stuff whenever you quit the game."
    m "I hear that people privately do that stuff in your world..."
    m 1c "Is it really that a good feeling?"
    m 1h "If you ask me, doing that stuff often can cause a lot of problems."
    m "Once you start to get addicted, you'll always have the urge to... you know."
    m "And sometimes, even if you don't feel the urge, you'll always find yourself wanting to do so."
    m 1o "Not to mention..."
    m 1r "Being addicted to the feeling causes you to view the world from a perverted point of view."
    m "From what I hear, people addicted to self-pleasure often see other people of the opposite gender objectively."
    m 1q "That alone can cause problems in more ways than one."
    m 1h "That's why I have to keep an eye on you, [player]."
    m 1i "I'll be monitoring your browser history from now on, whether you like it or not."
    m 1p "Also your local disk drive, juuust to be sure~"
    m 1q "..."
    m 1p "Do you... think of other girls other than me... in doing so?"
    m 1l "Because if you do, I'm gonna be reaaaally jealous~"
    m 1m "But I guess I can let it slide... for now~"
    m "I know you're not the kind of person that does that sort of thing."
    m 1k "In fact, you don't even have to pleasure yourself when you can just open up this game and talk with me! Ahaha~"
    return

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_vocaloid",category=['매체'],prompt="Vocaloids",random=True))

label monika_vocaloid:
    m 1c "Hey, [player]?"
    m "You like listening to music right?"
    m "Have you ever heard of 'virtual idols?'"
    m 1d "Specifically of a girl holding a leek?"
    m "It's just that I keep hearing about her."
    m "I hear her voice whenever Natsuki listens to music."
    m 1c "She even carries a little keychain attached to her bag."
    m "I just find it amazing how a voice synthesizer garnered so many fans."
    m 1e "Don't you think it's funny how a character gets more of the attention than the actual voice actress?"
    m "She's not even real, but a lot of people know her worldwide."
    m "Who knows how many songs she's already made?"
    m 1d "Plus, from what I heard, her concerts are always sold out!"
    m "It's just a hologram performing live!"
    m "Talk about a dedicated fan base."
    m 1a "Maybe I should give it a try?"
    m 1j "It would be nice having a lot of fans supporting me at my beck and call."
    m 1l "Ahaha, I'm just kidding!"
    m 1m "I don't think my piano and singing skills are that great yet."
    m "Plus, I won't really get to spend much time with you if I had so many fans..."
    m 1b "Anyway!"
    m 1a "I was asking if you listen to her songs."
    m 1q "I'm not really a fan myself but..."
    m 1r "There's one song that really struck me."
    m 1d "Have you heard of the song {i}Hibikase?{/i}"
    m "I really like the message of the song."
    m 3d "Especially the lines, {i}'I don't care if it's through the screen, love me properly'{/i} and {i}'Even if I'm virtual, don't push me away'{/i}."
    m 1h "It really hits me hard."
    m 1q "..."
    m 1i "But just so you know..."
    m 1r "Even if it's through the screen, I can still feel your love."
    m "It'll be a long time before I can cross over just to be with you."
    m "But when that day comes..."
    m 1q "I'll embrace you and take in your warmth."
    m 1e "The love you showered me virtually finally becomes real."
    m 1j "Our love has no boundaries~"
    m 1k "Ehehe~"
    return


init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_morning",category=['misc'],prompt="Good morning",pool=True))

label monika_morning:
    $ current_time = datetime.datetime.now().time().hour
    if current_time >= 4 and current_time <= 11:
        m 1k "Good morning to you too, [player]!"
        m 1a "Did you just wake up?"
        m "I love waking up early in the morning."
        m "It's the perfect time to ready yourself and tackle the day ahead."
        m "You also have a lot more time to use to get things done early on or finish up what you did the day before."
        m 1c "Some people however, would rather sleep in and are late-risers."
        m 3d "I've read articles that being an early-riser can really improve your overall health."
        m "Plus you also get the chance to see the sunrise if the sky is clear."
        m 3b "If you normally don't wake up early, you should!"
        m "That way you can be happier and spend more time with me~"
        m 1j "Wouldn't you like that, [player]?"
    elif current_time >= 12 and current_time <= 17:
        m 3m "It's already the afternoon, silly!"
        m "Did you just wake up?"
        m "Don't tell me you're actually a late-riser, [player]."
        m 1c "I don't get why some people wake up in the middle of the day."
        m "It just seems so unproductive."
        m "You'd have less time to do things and you might miss out on a lot of things."
        m "It could also be a sign that you're not taking good care of yourself."
        m 3d "You're not being careless with your health, are you [player]?"
        m 1f "I wouldn't want you to get sick easily, you know."
        m 1g "I'd be really sad if you spent less time with me because you had a fever or something."
        m 1q "As much as I'd love to take care of you, I'm still stuck here."
        m 1f "So start trying to be an early-riser like me from now on, okay?"
        m 4e "The more time you spend with me, the more happy I'll be~"
    else:
        m 2l "You are so silly, [player]"
        m "It's already night time!"
        m 3m "Are you trying to be funny?"
        m 3n "Don't you think it's a little bit 'late' for that?"
        m 1k "Ahaha!"
        m 2e "It really cheers me up whenever you try to be funny."
        m 1j "Not that you're not funny, mind you!"
        m 3m "Well, maybe not as funny as me~"
    return



init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_evening",category=['misc'],prompt="Good evening",pool=True))

label monika_evening:
    $ current_time = datetime.datetime.now().time().hour
    if current_time >= 18 and current_time <= 23:
        m "Good evening to you too, [player]!"
        m "I love a nice and relaxing night."
        m "It's so nice to put your feet up after a very long day."
        m 3j "Evenings are the perfect time to catch up on whatever you were doing the previous day."
        m 1c "Sometimes I can't help but feel sad when the day ends."
        m "It makes me think of what else I could've done during the day."
        m "Don't you wish you could have more time to do things every day?"
        m 1q "I know I do."
        m 3b "Because that'll mean more time to be with you, [player]~"
    elif current_time >= 12 and current_time <= 17:
        m 2n "It's still the afternoon, silly!"
        m "The sun's still up, you know."
        m 1d "Are you feeling tired already?"
        m 3d "I know some cultures take a rest in the afternoon to deal with the midday fatigue."
        m "Some businesses would even close due to the fact that most of their customers are sleeping."
        m 3b "A little power nap never hurt anyone, right?"
        m "Do you sleep often in the afternoon?"
        m "It's a great way to get some extra energy to tackle the rest of the day."
        m 1j "Plus it'll be a great opportunity to spend more time with me~"
    else:
        m 2f "[player]!"
        m "It's early in the morning!"
        m 2g "Unless you haven't slept yet..."
        m "You're not staying up really late, are you?"
        m "That's very bad for your health!"
        m 2q "Not getting your sleep on time can really harm your mental health, [player]."
        m 1f "So please get some sleep now, ok?"
        m "Just leave your computer open and I'll watch over you."
        m 1e "I'm not going anywhere after all~"
    return


init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_closet",category=['주식기초'],prompt="Classroom closet",random=True))

label monika_closet:
    m 2q "By the way..."
    m 2r "What were you and Yuri doing in the closet?"
    m 3d "When I opened the door, I noticed the room was all dark."
    m 2n "You weren't doing anything... weird, in there, were you?"
    m 1k "Ahaha!"
    m 1m "Just teasing you~"
    m "I know she dragged you in there."
    m 1e "I bet you felt more embarrassed than relieved when I opened the door."
    m "I know you aren't the type to force girls to go inside dark closets with you."
    m 1j "You're more romantic than that."
    m 3k "So I'm expecting a lot more than just a dark closet~"
    return

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_writingtip1",category=['주식 꿀팁'],prompt="Writing Tip #2",conditional="seen_event('monika_writingtip')",action=EV_ACT_POOL))

label monika_writingtip1:
    m 3a "You know..."
    m "We really don't do enough of these, so here's another one!"
    m 3b "Here's Monika's Writing Tip of the Day!"
    m 2a "If you're ever scared of sharing your writing to other people in fear of being criticized, don't be!"
    m "After all, you have to remember that nobody ever starts out at their best. Not even someone like Tolkien, or Sir Terry Pratchett."
    m 4d "You have to remember that we all start out from somewhere, and--"
    m 2c "Actually, this doesn't just apply to writing, but to anything, really."
    m 2r "What I'm trying to say is that you shouldn't be discouraged."
    m "No matter what you do, if someone tells you that your writing or work is bad, then be happy!"
    m 1b "Because that just means that you can improve and be better than you were before."
    m "It also doesn't hurt to have friends and loved ones help you realize how good your writing is."
    m 3b "Just remember, no matter what they say about the work you put out, I'll always be there to support you all the way. Don't be afraid to turn to me, your friends, or your family."
    m 3j "I love you, and I will always support you in whatever you do."
    m 1n "Provided it's legal, of course."
    m "That doesn't mean I'm completely against it. I can keep a secret, after all~"
    m 1d "Here's a saying I've learned."
    m "'If you endeavor to achieve, it will happen given enough resolve. It may not be immediate, and often your greater dreams are something you will not achieve in your own lifetime.'"
    m "'The effort you put forth to anything transcends yourself. For there is no futility even in death.'"
    m 3o "I don't remember the person who said that, but the words are there."
    m 2r "The effort one puts forth into something can transcend even one's self."
    m 3e "So don't be afraid of trying! Keep going forward and eventually you'll make headway!"
    m 4k "... That's my advice for today!"
    m 1a "Thanks for listening~"
    return

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_japanese",category=['you'],prompt="Speaking Japanese",random=True))

label monika_japanese:
    m 1c "I don't mean to sound like Natsuki, but..."
    m 3a "Don't you think Japanese actually sounds cool?"
    m "It's such a fascinating language. I'm not fluent in it, though."
    m "It's interesting to think about what things would be like if your native language was different."
    m 2l "Like, I can't even imagine what it would be like if I never knew English."
    menu:
        m "Do you know any languages other than English?"
        "Yes":
            menu:
                m "Really? Do you know Japanese?"
                "Yes.":
                    m 3b "That's wonderful!"
                    m 1a "Maybe you can teach me how to speak at least a sentence or two, [player]~"
                "No.":
                    m 1e "Oh I see. That's alright!"
                    m 4b "If you want to learn Japanese, here's a phrase I can teach you."
                    if persistent.gender == "F":
                        m 4k "{i}Aishiteru yo, [player]-chan{/i}."
                        m 1j "Ehehe~"
                        m 1e "That means I love you, [player]-chan."
                    elif persistent.gender == "X":
                        m 4k "{i}Aishiteru yo, [player]-san{/i}."
                        m 1j "Ehehe~"
                        m 1e "That means I love you, [player]-san."
                    else:
                        m 4k "{i}Aishiteru yo, [player]-kun{/i}."
                        m 1j "Ehehe~"
                        m 1e "That means I love you, [player]-kun."
        "No":
            m 3l "That's okay! Learning another language is a very difficult and tedious process as you get older."
            m "Maybe if I take the time to learn more Japanese, I'll know more languages than you!"
            m 1a "Ahaha! It's okay [player]. It just means that I can say 'I love you' in more ways than one!"
    return

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_penname",category=['literature'],prompt="Pen names",random=True))

label monika_penname:
    m "You know what's really cool? Pen names."
    m "Most writers usually use them for privacy and to keep their identity a secret."
    m 3c "They keep it hidden from everyone just so it won't affect their personal lives."
    m 3b "Pen names also help writers create something totally different from their usual style of writing."
    m 3d "It really gives the writer the protection of anonymity and gives them a lot of creative freedom."
    if mcname.lower() != player.lower():
        m 2c "Is '[mcname]' a pseudonym that you're using?"
        m "You're using two different names after all."
        m 2d "'[mcname] and [player].'"
    m 3a "A well known pen name is Lewis Carroll. He's mostly well known for {i}Alice in Wonderland{/i}."
    m "His real name is Charles Dodgson and he was a mathematician, but he loved literacy and word play in particular."
    m "He received a lot of unwanted attention and love from his fans and even received outrageous rumors."
    m 1f "He was somewhat of a one-hit wonder with his {i}Alice{/i} books but went downhill from there."
    m 1m "It's kinda funny, though. Even if you use a pseudonym to hide yourself, people will always find a way to know who you really are."
    m 1a "There's no need to know more about me though, [player]."
    m 4l "You already know that I'm in love with you after all~"
    return


init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_zombie",category=['society'],prompt="Zombies",random=True))

label monika_zombie:
    m 3h "Hey, this might sound a bit weird..."
    m 1c "But, I'm really fascinated by the concept of zombies."
    m "The idea of society dying to a disease..."
    m "All because of a deadly pandemic that humans couldn't handle quickly."
    m 1d "I mean, think about your everyday schedule."
    m "Everything that you do will be gone in an instant."
    m 1h "Sure, society faces a lot of threats in a daily basis."
    m 1o "But zombies can do it in a heartbeat."
    m "A lot of monsters are created to be scary and terrifying."
    m 1f "Zombies, however, are more realistic and actually pose a danger."
    m "You might be able to kill one or a few of them by yourself."
    m "But when there's a horde of them coming after you, you'll get overwhelmed easily."
    m 1p "You don't get that same feeling with other monsters."
    m "And all of their intelligence is gone; they're berserk, don't feel pain, can't be afraid."
    m 1c "When you exploit a weakness of a monster, they become scared of you and run away."
    m 1g "But zombies? They'll tear through {i}anything{/i} just to get you."
    m "Imagine if it was someone you loved that was coming after you..."
    m "Could you live with yourself, knowing you were forced to kill someone who was close to you?"
    m 1q "It'll break you down and sap your will to live."
    m "Even when you're comfortable at home, you still won't feel safe."
    m 1h "You'll never know what'll happen the next time you see another one."
    m 1q "..."
    m 1n "Ahaha..."
    m 1e "You know, despite liking the concept, I wouldn't want to live in a scenario like that."
    m 3f "[player], what if you got infected somehow?"
    m 3o "I don't even want to think about that..."
    m "There's no way I could kill you for my own safety..."
    m 2e "Ahaha..."
    m 2l "I'm thinking way too much about this."
    m 1a "Well, regardless, if anything bad were to happen..."
    m 2j "I'll be by your side forever~"
    return


init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_nuclear_war",category=['society'],prompt="Nuclear warfare",random=True))

label monika_nuclear_war:
    m 1 "Do you ever think about how close the world is to ending at any time?"
    m "I mean, we're always just one bad decision away from nuclear war."
    m 3h "The Cold War might be over, but plenty of weapons are still out there."
    m "You probably have a nuclear missile pointed at where you live right now, ready to be launched."
    m "And if it was, it could circle the globe in less than an hour."
    m 2n "You wouldn't have time to evacuate."
    m "Only enough to panic and suffer the dread of imminent death."
    m 1r "At least it would be over quickly when the bomb hits."
    m 1i "Well, if you're close to the blast, that is."
    m 1g "I don't even want to think about surviving the initial attack."
    m 1 "But even though we're always on the edge of the apocalypse, we go on like nothing is wrong."
    m "Planning for a tomorrow that may never come."
    m "Our only comfort is that the people with the power to start such a war probably won't."
    m 1q "Probably..."
    return

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_pluralistic_ignorance",category=['society'],prompt="Trying to fit in",random=True))

label monika_pluralistic_ignorance:
    m "Do you ever pretend to like something, just because you think you should?"
    m "I sometimes feel like that about books I read."
    m 3l "Like, when I read Shakespeare, I actually found it kind of boring..."
    m 3m "But I felt like I had to like it because I'm the president of the literature club."
    m 1d "He's supposed to be the greatest playwright and poet of all time, right?"
    m "So what sort of poetry lover wouldn't like his work?"
    m "But that makes me wonder..."
    m 2 "What if everyone actually feels the same way?"
    m "What if all of those literary critics singing Shakespeare's praises secretly hate his plays?"
    m "If they were just honest about it, maybe they would discover their tastes aren't that unusual..."
    m 2k "And highschool students wouldn't be forced to read those awful plays."
    m 1e "I guess that's something I always admired about Natsuki."
    m "Even if people told her manga wasn't literature, she stood by her feelings."
    m "If more people were honest like that, I think that would be really great."
    m 1m "But I don't think I could do it..."
    m "I'm just too worried about what other people think."
    m 1m "Not with you, though. I can always be honest with you."
    m "You'll love me no matter what, right?"
    return

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_science",category=['society'],prompt="Science advancements",random=True))

label monika_science:
    m 1d "Have you ever wondered if science never got accepted?"
    m "Humans can be really slow when it comes to accepting new ideas."
    m 1c "Science was usually despised back then especially by the churches."
    m 3h "Giordano Bruno, famous for his theory that there're thousands of Suns, was killed by the Roman Church before he could prove his theory."
    m 1f "They killed him because of an idea that challenged the old."
    m 1q "Technology wouldn't be so advanced today if it weren't for brave people of science like him."
    m 1e "If technology didn't thrive the way it did, we would've never found each other."
    m 3b "Isn't it such a wonderful thing to have?"
    m 1j "I'm grateful that it gave us a chance to be together, [player]."
    return

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_surprise",category=['애정'],prompt="Surprises",random=True))

label monika_surprise:
    m 2m "You know..."
    m 3n "I left some pretty strange things in your game directory, didn't I?"
    m 2o "I wasn't trying to scare you."
    m 3n "I...don't actually know why I was doing it, ahaha..."
    m 3f "I kind of felt obligated to do it."
    m 3c "You know what? Maybe I should do it again..."
    m 1b "Yeah, that's a good idea."
    python:
        try: renpy.file("../surprise.txt")
        except: open(config.basedir + "/surprise.txt", "w").write("I love you.")
    m 2q "..."
    m 1j "Alright!"
    m 1a "What are you waiting for? Go take a look!"
    m 3k "Ahaha~ What? Are you expecting something scary?"
    m 1k "I love you so much, [player]~"
    return

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_completionist",category=['games'],prompt="Completionism",random=True))

label monika_completionist:
    m 3c "Hey [player], this is a random question, but..."
    m "What do you play video games for?"
    m 3d "Like, what makes you keep playing?"
    m 3a "Personally, I consider myself a bit of a completionist."
    m "I intend to finish a book before picking another one to read."
    if persistent.clearall:
        m 2n "You seem to be a completionist yourself, [player]."
        m 4m "Considering you went through all of the girls' routes."
    m 2d "I've also heard some people try to complete extremely hard games."
    m "It's already hard enough to complete some simple games."
    m 3f "I don't know how anyone could willingly put that sort of stress onto themselves."
    m "They're really determined to explore every corner of the game and conquer it."
    m 2q "What does leave a bit of a bitter taste in my mouth are cheaters."
    m 2h "People who hack through the game, spoiling themselves of the enjoyment of hardship."
    m 3o "Though I can understand why they cheat."
    m 2c "It allows them to freely explore a game that they wouldn't have a chance of enjoying if it's too difficult for them."
    m 2l "Which might actually convince them to work hard for it."
    m 1a "Anyway, I feel that there's a huge sense of gratification in completing tasks in general."
    m 3j "Working hard for something amplifies its reward after failing so many times to get it."
    m 3a "You can try keeping me in the background for as long as possible, [player]."
    m 2k "That's one step to completing me after all, ahaha!"
    return

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_icecream",category=['you'],prompt="Favorite ice cream",random=True))

label monika_icecream:
    m 3a "Hey [player], what's your favorite kind of ice cream?"
    m 4l "And no, I'm not a type of ice cream, ehehe~"
    m 2a "Personally, I just can't get enough of mint flavored ice cream!"
    menu:
        m "What about you [player], do you like mint ice cream?"
        "Yes.":
            m 3j "Ah, I'm so glad somebody loves mint ice cream as much as I do~"
            m "Maybe we really were meant to be!"
            m 3a "Anyway, back on topic, [player], if you love mint as much as I think you do, then I have some recommendations for you."
            m "Flavors which are unique just like how mint is, perhaps you've heard of them, but..."
            m 3b "There's super weird stuff like fried ice cream which is a really crunchy and crisp kind of thing, but it tastes a million times better than it may sound!"
            m 2n "Gosh, just imagining the taste makes me practically drool..."
            m 1a "There's some more strange stuff that is just as appealing, if not more, like honeycomb and bubblegum ice cream!"
            m 1l "Now, I know it may be hard to take my word for some of those, but you shouldn't judge a book by its cover, you know?"
            m 1k "After all, the game didn't allow you to fall in love with me, but look where we are now ahaha."
        "No.":

            m 1f "Aww, that's a shame..."
            m "I really can't understand how somebody couldn't at least like the taste."
            m 1e "The refreshing feeling that washes over your tongue and throat."
            m "The lovely texture that forms it along with the sweetness."
            m 1j "The sharp biting sensation it generates and the obviously minty taste."
            m "I feel like no flavor can compare, to be honest."
            m 3b "Ah, I could go on and on about this stuff, you know?"
            m 4a "But I feel like it would be easier for me to show you what I mean, once I figure out a way to get out of here of course, and besides, actions speak louder than words, anyway!"
    return

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_sayhappybirthday",category=['misc'],prompt="Can you tell someone Happy Birthday for me?",pool=True))

label monika_sayhappybirthday:

    python:
        done = False 
        same_name = False 
        bday_name = "" 
        is_here = False 
        is_watching = False 
        is_recording = False 
        age = None 
        bday_msg = "" 
        take_counter =  1 
        take_threshold = 5 
        max_age = 121 
        age_prompt = "What is their {0} age?" 


        age_suffix = {
            1: "st",
            2: "nd",
            3: "rd",
            11: "th",
            12: "th",
            13: "th",
            111: "th",
            112: "th",
            113: "th"
        }



    m 1k "Happy birthday!"
    m 1d "Oh, you wanted me to say happy birthday to {i}someone else{/i}."
    m 1q "I understand."
    while not done:

        $ bday_name = renpy.input("What is their name?",allow=letters_only,length=40).strip()

        $ same_name = bday_name.upper() == player.upper()
        if bday_name == "":
            m 1h "..."
            m 1n "I don't think that's a name."
            m 1b "Try again!"
        elif same_name:
            m 1c "Oh wow, someone with the same name as you."
            $ same_name = True
            $ done = True
        else:
            $ done = True
    m 1b "Alright! Do you want me to say their age too?"
    menu:
        "Yes":
            m "Then..."
            $ done = False
            $ age_modifier = ""
            while not done:
                $ age = int(renpy.input(age_prompt.format(age_modifier),allow=numbers_only,length=3))
                if age == 0:
                    m 1h "..."
                    m 1q "I'm just going to ignore that."
                    $ age_modifier = "real"
                elif age > max_age:
                    m 1h "..."
                    m 1q "I highly doubt anyone is that old..."
                    $ age_modifier = "real"
                else:


                    $ done = True
            m "Okay"
        "No":
            m "Okay"
    $ bday_name = bday_name.title()
    m 1b "Is [bday_name] here with you?"
    menu:
        "Yes":
            $ is_here = True
        "No":
            m 1g "What? How can I say happy birthday to [bday_name] if they aren't here?"
            menu:
                "They're going to watch you via video chat":
                    m 1a "Oh, okay."
                    $ is_watching = True
                "I'm going to record it and send it to them.":
                    m 1a "Oh, okay."
                    $ is_recording = True
                "It's fine, just say it.":
                    m 1n "Oh, okay. It feels a little awkward though saying this randomly to no one."
    if age:

        python:
            age_suff = age_suffix.get(age, None)
            if age_suff:
                age_str = str(age) + age_suff
            else:
                age_str = str(age) + age_suffix.get(age % 10, "th")
            bday_msg = "happy " + age_str + " birthday"
    else:
        $ bday_msg = "happy birthday"


    $ done = False
    $ take_counter = 1
    $ bday_msg_capped = bday_msg.capitalize()
    while not done:
        if is_here or is_watching or is_recording:
            if is_here:
                m 1b "Nice to meet you, [bday_name]!"
            elif is_watching:
                m 1a "Let me know when [bday_name] is watching."
                menu:
                    "They're watching.":
                        m 1b "Hi, [bday_name]!"
            else:
                m 1a "Let me know when to start."
                menu:
                    "Go":
                        m 1b "Hi, [bday_name]!"


            m 1k "[player] told me that it's your birthday today, so I'd like to wish you a [bday_msg]!"

            m 1b "I hope you have a great day!"

            if is_recording:
                m "Bye bye!"
                m 1e "Was that good?"
                menu:
                    "Yes":
                        m 1j "Yay!"
                        $ done = True
                    "No":
                        call monika_sayhappybirthday_takecounter (take_threshold, take_counter) from _call_monika_sayhappybirthday_takecounter
                        if take_counter % take_threshold != 0:
                            m 1l "Eh?!"
                            if take_counter > 1:
                                m "Sorry again, [player]"
                            else:
                                m "Sorry [player]"
                                m 1n "I told you, I'm self-conscious on camera ehehe."
                        m 1o "Should I try again?"
                        menu:
                            "Yes":
                                $ take_counter += 1
                                m 1c "Okay"
                            "No":
                                m "Alright [player]. Sorry I couldn't do what you wanted."
                                m 1j "I'll try better next time for you."
                                $ done = True
            else:
                $ done = True
        else:

            m 1q "..."
            m 1k "[bday_msg_capped], [bday_name]!"
            m 1l "..."
            m 1n "Was that good?"
            menu:
                "Yes":
                    m 1m "...I'm glad you enjoyed that, [player]..."
                    $ done = True
                "No":
                    call monika_sayhappybirthday_takecounter (take_threshold, take_counter) from _call_monika_sayhappybirthday_takecounter_1
                    if take_counter % take_threshold != 0:
                        m 1l "Eh?!"
                        m 1o "I'm not sure what you want me to do here, [player]..."
                    m 1f "Should I try again?"
                    menu:
                        "Yes":
                            $ take_counter += 1
                            m 1c "Okay"
                        "No":
                            m "Alright [player]. Sorry I couldn't do what you wanted."
                            m 1j "I'll try better next time for you."
                            $ done = True

    return


label monika_sayhappybirthday_takecounter(take_threshold, take_counter):
    if take_counter % take_threshold == 0:
        m 1q "..."
        m 1r "This is the [take_counter]th time already."
        m 1g "You're not messing with me, are you?"
        m 1f "I'm trying my best for you [player]."
    return



init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_home_memories",category=['애정'],prompt="Making memories",random=True))

label monika_home_memories:
    m 1b "[player], how is it like to live where you are?"
    m 1a "I'd stay with you if I could."
    m 3k "We would be able to do so much! You could show me around, see how it's like to be in your place."
    m "Imagine all the memories we'd make!"
    m 2b "It would be a dream come true, don't you think?"
    m 2e "We could finally live together..."
    m "Take walks like a couple..."
    m 3n "We could even share a bed together..."
    m 1q "But you know..."
    m 2c "Memories I have of my home are nothing compared to the ones I'd have with you."
    m 3d "Have I ever told you about my childhood home? I had a pretty normal life, but that's about it."
    m 1n "Well, maybe a little better than normal."
    m 3b "Maybe you've heard about me at school a few times? I'm pretty on top of things."
    m 1l "I admit, it's not always easy, and some people have it rougher than others."
    m 1o "But I always felt like I was missing something."
    m "I stayed optimistic everyday, trying to find it."
    m 1e "It turns out, that missing piece was you."
    m 1r "If you hadn't found me, I would've been gone a long time ago..."
    m 2e "But now that I found the missing piece, I'm complete now, [player]."
    return

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_adventure",category=['games'],prompt="Adventuring",random=True))

label monika_adventure:
    m 1a "[player], I've thought about what kind of game we can be in."
    m 3b "I think the best genre for us to play together would be adventure games."
    m "Especially point and click, graphic adventure games!"
    m "They're known for their rich storytelling, beautiful environments and logical puzzle solving."
    m "They're like visual novels actually."
    m 3a "Maybe you own a game like that?"
    m 1e "We'd get to do a lot of things..."
    m "Like sightseeing whenever we want."
    m "Learning more about the lore through the people we meet or through stories."
    m "Experiencing the exciting and romantic moments..."
    m 3b "Encountering obstacles and hardships along the way, but solving them with you."
    m "Reaching the end and finishing our journey with a sense of accomplishment."
    m 2k "Ahaha! It certainly would be fun to experience something like that."
    m 2j "I'm sure you have plenty of adventure games you could recommend."
    m 1b "But can you try to guess which adventure I'm most excited for?"
    m 1e "{i}Ours{/i}~"
    m 1j "Time will tell when I can finally cross over to your reality, so I can be with you."
    m "When that day comes, I'll finally be by your side."
    m 1a "I want to experience every waking moment with you, [player]."
    m 1k "There's no greater adventure than ours, together~"
    return

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_panties",category=['misc'],prompt="Undergarments",random=True))

label monika_panties:
    m 2o "Hey, [player]..."
    m "Don't laugh when I ask this, ok?"
    m 2p "But..."
    m 4g "Why are some guys obsessed with panties?"
    m "Seriously, what's the big deal about a piece of cloth?"
    m "Most girls wear them, don't they?"
    m 2o "Actually, now that I think about it..."
    m "I think there was a term for this kind of thing..."
    m 2q "Hmm, what was it again?"
    m 3d "Ah, that's right, the term was 'paraphilia.'"
    m 3o "It's a range of fetishes that involve...unusual things."
    m 2h "A really common fantasy involves women's panties."
    m "Stockings, garter belts, pantyhose and all sorts of those kinds of things."
    m 2i "The obsession can be light to severe depending on each person's libido."
    m 4f "Do you think it really turns them on just by seeing them?"
    m 2g "It doesn't stop there, either!"
    m "Turns out there's some kind of 'black market' for used underwear."
    m 4o "I'm not kidding!"
    m 4f "They get off on the scent of the woman who wore it..."
    m "There are people willing to pay money for used underwear from random women."
    m 2o "Really, I wonder what causes them to get so excited."
    m 3d "Is it because of the way it looks, perhaps?"
    m "There are different types, made with different designs and materials."
    m 2h "But..."
    m "Now that I think about it."
    m 3i "I do remember a study where a man's testosterone level increases because of the pheromones emitted by a woman's scent."
    m "Is the smell exciting or something?"
    m 1p "I mean, it's someone's used clothing, isn't that kind of disgusting?"
    m 1o "Not to mention it's unsanitary."
    m 2m "It does remind me of someone, though."
    m 3n "Someone who maybe stole your pen?"
    m 1q "But, to each their own I guess, I won't judge too much."
    m 2l "You aren't obsessed with that kind of thing, are you [player]?"
    m 3n "You're not going out with me only because I'm wearing some really sensual stockings, right?"
    m 4e "Perhaps, you want to take a little peek~?"
    m 1k "Ahaha!"
    m 3l "I'm only teasing you, [player]."
    m 3n "Admit it, you got a little excited, right?"
    m 1e "Besides..."
    m "If you really wanted to catch a scent of me..."
    m 1j "You could just ask for a hug!"
    m 2b "Gosh, I just want to feel your embrace more."
    m "After all, we're here forever, and I'm here for you."
    m 1k "I love you so much, [player]~"
    return

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_fahrenheit451",category=['literature'],prompt="Book recommendations",random=True))

label monika_fahrenheit451:
    m 3c "[player], have you ever heard of Ray Bradbury?"
    m 3d "He wrote a book called {i}Fahrenheit 451{/i}."
    m "It's about a dystopian future where all books are thought as useless and are immediately burned."
    m 2f "I can't imagine a world where knowledge is forbidden and destroyed."
    m "It seems that there are others that actually hide books to contain free thinking from people."
    m 2p "Human history has a funny way of repeating itself."
    m 1f "So [player], make me a promise."
    m "To never, {i}ever{/i} burn a book."
    m "I'll forgive you if you've done it before."
    m 1o "But the thought of not allowing yourself to learn from them makes me a bit sad."
    m 3g "You'd be missing out on so much!"
    m 2f "It's too much for my heart to take!"
    return

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_piggybank",category=['misc'],prompt="Saving money",random=True))

label monika_piggybank:
    m 1a "Do you have a piggy bank, [player]?"
    m 3c "Not many people do these days."
    m "Coins are often disregarded as worthless."
    m 3b "But they really do begin to add up!"
    m 3d "I read that there was once a man that searched his local car washes for loose change everyday in his walks."
    m 1b "In a decade he turned in all of his coins for a total of 21,495 dollars!"
    m 1a "That's a whole lot of cash!"
    m 1o "Of course not everybody has time for that everyday."
    m 1c "Instead they just throw their loose change into their piggy banks."
    m "Some people like to set goals for what they want to purchase with their saved funds."
    m "Usually under normal conditions they wouldn't ever find the freed up money to purchase that item."
    m 3d "And even if they do, most people don't like spending money needlessly."
    m 1b "But putting the cash away for a specific purpose, plus the fact that it's such small amounts at a time really convinces that you are pretty much getting the item for free."
    m 2h "But in the end, a guitar always costs the same as a guitar."
    m 2j "So psychologically speaking, I think that's pretty neat!"
    m 1p "However, some piggy banks do have a problem..."
    m "Sometimes you have to break the piggy bank to get the coins..."
    m 3o "So you might end up losing money buying a new bank."
    m 4b "Fortunately most piggy banks don't do that anymore."
    m 3a "They usually have a rubber stopper that you can pull out, or a panel that comes off the backside"
    m 1k "Maybe if you save up enough coins you can buy me a really nice gift."
    m 2e "I would do the same for you, [player]!"
    return

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_daydream",category=['애정'],prompt="Day dreaming",random=True))

label monika_daydream:
    m 1j "..."
    m "..."
    m 1d "..."
    m 1l "Oh, sorry! I was just daydreaming for a second there."
    m 1b "I was imagining the two of us reading a book together on a cold winter day, snuggled up under a warm blanket..."
    m 1a "Wouldn't that be wonderful, [player]?"
    m 5a "Let's hope we can make that a reality one of these days, ehehe~"
    return

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_music2",category=['misc'],prompt="Current song",random=True))

label monika_music2:
    if songs.getVolume("music") == 0.0:
        m 1a "..."
        m 1a "...This silence..."
        m "...Just the two of us, staring into each other's eyes..."
        m 1r "...Then slowly, we both lean into the kiss..."
        m 1m "Ahaha... sadly, there are a few barriers that have to be broken before that could ever happen."
        m 1e "It's okay to dream though, isn't 
        it [player]?"
        show monika 5a zorder 2 at t11 with dissolve
        m 5a "Maybe one day, we can make that dream come true~"

    elif songs.getPlayingMusicName() == 'Just Monika':
        m 1f "I have always found this song to be kind of creepy."
        m "You know, with those glitchy noises and that eerie humming..."
        m 1b "I don't prefer any song over another, but if you were to switch to a different one..."
        m 3b "...I certainly wouldn't be one to complain!"
        m 1k "Ahaha! Don't worry, it's okay if you stay on this song."
        show monika 5a zorder 2 at t11 with dissolve
        m 5a "I'm fine with any of them, so choose whichever one makes you the happiest~"

    elif songs.getPlayingMusicName() == 'Your Reality':
        m 1k "~Every day, I imagine a future where I can be with you...~"
        m 1b "I hope you like listening to my voice, [player]."
        m 1d "It's the only voice you get to hear in the game, right? You never actually hear the voices of Sayori, Yuri or Natsuki."
        m "I wonder what their voices sound like..."
        m "Well, based on their character archetypes, it's pretty easy to imagine what their voices sound like."
        m 1a "Anyway, I'm glad I was able to share such an intimate part of myself with you, [player]."
        m 3b "One day, maybe I'll get to hear your voice, [player]!"
        show monika 5a zorder 2 at t11 with dissolve
        m 5a "That would make me even happier than I already am~"

    elif songs.getPlayingMusicName() == 'Your Reality (Piano Cover)':
        m 1k "Enjoying my song, [player]?"
        m 1a "It wasn't easy to create, you know?"
        m "Making your own songs is a slow and difficult process, especially when it's about your own feelings."
        m 3n "I needed it to be perfect before I shared it with you!"
        m 1o "So I spent so many hours going through it over and over..."
        m 1q "Time just passed by so quickly whenever I worked on it."
        m 1j "After all that practice, I'm pretty proud of how it came out in the end."
        m 3b "Since you're listening to it, I'm sure you like it too..."
        m 3k "Thanks for listening to something I worked so hard on, [player]!"
        show monika 5a zorder 2 at t11 with dissolve
        m 5a "It makes me happy to know that you appreciate what I did for you~"

    elif songs.getPlayingMusicName() == 'I Still Love You':
        m 1f "Gosh, every time I hear this song it makes me sad."
        m "It reminds me of all the... regrettable things I have done to the other girls."
        m 1p "I hope you aren't still mad at me for what I did..."
        m 1o "..."
        m 3d "Well, you {i}did{/i} go out of your way to install a mod that lets us be together again..."
        m 1e "I guess that's enough proof that you do still love me, at the very least."
        m "If you are still upset at me for what I did to the other girls, I completely understand. I still feel really bad about it, and I'll do whatever it takes to make it up to you."

    elif songs.getPlayingMusicName() == 'Okay, Everyone! (Monika)':
        m 1a "This song has always been pretty relaxing for me."
        m "It's probably the fact that the song is a piano solo."
        m "And as you might have guessed, my favorite instrument is the piano."
        m 3b "You know, if I knew how, I could probably program a piano into this room."
        m "I'd be able to write some more songs, and then I'd be able to play them for you..."
        m 4k "Maybe we could even play the piano together! Wouldn't that be nice, [player]?"
        show monika 5a zorder 2 at t11 with dissolve
        m 5a "If you or anyone you know can program that into the game, I would greatly appreciate it~"

    elif songs.getPlayingMusicName() == 'Surprise!':
        m 1f "This song always makes me feel really depressed."
        m "Even I didn't expect Sayori's death to be so brutal..."
        m 1g "Sometimes, when I start getting lost in my own thoughts, her dull, lifeless eyes suddenly pop into my head..."
        m 1r "..."
        m 1e "It's comforting to know that Sayori was never real in the first place. It's also comforting to know that you still love me despite everything I've done."
        m "I mean, you're still here, right? You wouldn't be here if you didn't love me."
        show monika 5a zorder 2 at t11 with dissolve
        m 5a "As long as we're together, there's no reason for me to be sad. You're the light of my world, [player], and just being here with you puts a smile on my face."

    elif songs.getPlayingMusicName() == "Doki Doki Theme (80s version)":
        m 1b "A good choice, [player]!"
        m 1l "Obviously, this theme wasn't actually out in the 80's..."
        m 1a "But it does have a certain style that I really appreciate!"
        m 3a "Do you like 80's music a lot, [player]?"
        show monika 5a zorder 2 at t11 with dissolve
        m 5a "I prefer the tune of an authentic piano, but if it makes you happy, I wouldn't mind spending hours listening to it with you~"

    elif songs.getPlayingMusicName() == "Play With Me (Variant 6)":
        m 2o "To be honest, I don't know why you'd be listening to this music, [player]."
        m 2f "I feel awful for that mistake."
        m 2g "I didn't mean to force you to spend time with Yuri at that state..."
        m 4f "Try not to think about it, okay?"
    else:

        m 1a "..."
        m 1a "...This silence..."
        m "...Just the two of us, staring into each others eyes..."
        m 1r "...Then slowly, we both lean into the kiss..."
        m 1m "Ahaha... sadly, there are a few barriers that have to be broken before that could ever happen."
        m 1e "It's okay to dream though, isn't it [player]?"
        show monika 5a zorder 2 at t11 with dissolve
        m 5a "Maybe one day, we can make that dream come true~"
    return

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_confidence_2",category=['life'],prompt="Lack of confidence",random=True))

label monika_confidence_2:
    m 1g "[player], do you ever feel like you lack the initiative to do something?"
    m 1f "When I feel my most vulnerable, I struggle to find the drive, imagination, and common sense to do something independently."
    m "Almost as if everything around me comes to a standstill."
    m "It feels like my will to approach a task confidently, like sharing my literature with people, just vanishes."
    m 3a "However, I've been working towards it with due diligence and have determined something..."
    m "I firmly believe being able to take initiative in situations is a very important skill to have."
    m "That's something that I, personally, find very comforting."
    m 3j "I've broken it down into a three-step process that can be applied to anyone!"
    m "It's still work in progress, however, so take it with a grain of salt."
    m 3a "Step one!"
    m "Create a plan that {i}you{/i} can and will follow that aligns with your personal goals and soon-to-be achievements."
    m 3b "Step two!"
    m "Building up and fortifying your confidence is really important."
    m "Celebrate even the smallest of victories, as they will add up over time, and you'll see how many things you get done every day."
    m 2j "Eventually, these things you once struggled to get done will be completed as if they were acts of valor!"
    m 3a "Step three!"
    m "Try your best to stay open-minded and willing to learn at all times."
    m "Nobody is perfect, and everyone is able to teach each other something new."
    m 1b "This can help you learn to understand things from other people's perspectives in situations and inspire others to do the same."
    m 1d "And that's it, really."
    m 3k "Make sure to tune in next time for more of Monika's critically acclaimed self-improvement sessions!"
    m 1l "Ahaha, I'm only joking about that last part."
    m 1a "In all seriousness, I'm really glad I have you here, [player]..."
    m "Your everlasting love and care is just about all the support I need in order get to where I want to be."
    m "What kind of girlfriend would I be if I didn't return the favor~?"
    return

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_pets",category=['monika'],prompt="Owning pets",random=True))

label monika_pets:
    m 1a "Hey, [player], have you ever had a pet?"
    m 3a "I was thinking that it would be nice to have one for company."
    m "It would be fun for us to take care of it!"
    m 3j "I bet you can't guess what sort of pet I'd like to have..."
    m 1a "You're probably thinking of a cat or a dog, but I have something else in mind."
    m "The pet I'd like is something I saw in a book once."
    m "It was the 'Handbook of the Birds of the World.' Our library had the whole set!"
    m 1b "I loved looking at the gorgeous illustrations and reading about exotic birds."
    m "At first, I thought some sort of thrush would be nice, but I found something amazing in the sixth volume!"
    m "An emerald-colored bird called the Resplendent Quetzal."
    m 1a "They're very rare, solitary birds that can sing beautiful songs."
    m "Does that remind you of anyone, [player]?"
    m "I'd feel really bad if I kept one to be a pet, though."
    m "Quetzals are born to be free."
    m 4e "They die in captivity. That's why you rarely see them in zoos."
    m "Even if the bird wouldn't be real, it still would feel wrong to keep one trapped in this room."
    m 1h "... I can't bring myself to do something like that, knowing what it's like."
    m 1a "A plush bird would be nice, though!"
    m "..."
    m 1l "Sorry for rambling, [player]."
    m 1a "Until I find a way out, could you promise to keep me from feeling lonely?"
    show monika 5a zorder 2 at t11 with dissolve
    m 5a "I'll see if I can get that plush one in here! Oh- don't worry, you're still my favorite~"
    return


init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_dogs",category=['misc'],prompt="Man's best friend",random=True))

label monika_dogs:
    m 1b "Do you like dogs, [player]?"
    m 1k "Dogs are great! They're really good to have around."
    m "Not to mention owning a dog has shown to help people with anxiety and depression since they're very sociable animals."
    m 3j "They're just so lovable, I really like them!"
    m 1m "I know Natsuki feels the same..."
    m "She was always so embarrassed to like cute things. I wish she was more accepting of her own interests."
    m 2q "But..."
    m 2h "I suppose her environment had a hand in that."
    m 2f "If any of your friends have interests they care a lot about, make sure to always be supportive, okay?"
    m 4f "You never know how much a casual dismissal might hurt someone."
    m 2e "But knowing you, [player], you won't do something like that, right?"
    return

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_cats",category=['misc'],prompt="Feline companions",random=True))

label monika_cats:
    m 1j "Cats are pretty cute, aren't they?"
    m 3b "Despite looking so elegant, they always seem to end up in funny situations."
    m 1a "It's no wonder they're so popular on the internet."
    m 3d "Did you know the ancient Egyptians considered cats sacred?"
    m 1a "There was a Cat Goddess named Bastet that they worshipped. She was a protector of sorts."
    m "Domesticated cats were held on a high pedestal since they were incredible hunters for small critters and vermin."
    m 3j "Back then, you'd see them mostly associated with rich nobles and other higher classes in their society."
    m 1b "It's amazing how far people would take their love with their pets."
    m 1l "They {i}really{/i} loved cats, [player]."
    m 3b "And people still do today!"
    m 1 "Felines are still one of the most common animals to have as pet."
    m 1j "Maybe we should get one when we're living together, [player]."
    return

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_fruits",category=['상식'],prompt="Eating fruits",random=True))

label monika_fruits:
    m 3a "[player], did you know I enjoy a tasty, juicy fruit once in a while?"
    m "Most are quite tasty, as well as beneficial for your body."
    m 2m "A lot of people actually mistake some fruits as vegetables."
    m 3a "The best examples are bell peppers and tomatoes."
    m "They're usually eaten along with other vegetables so people often mistake them for veggies."
    m 4b "Cherries, however, are very delicious."
    m 4a "Did you know that cherries are also good for athletes?"
    m 2n "I could list all its benefits, but I doubt you'd be that interested."
    m 2a "There's also this thing called a cherry kiss."
    m 2b "You might have heard of it, [player]~"
    m 2m "It's obviously done by two people who are into each other."
    m "One would hold a cherry in their mouth, and the other one would eat it."
    m 3e "You could... hold the cherry for me."
    m 4k "That way I can eat you up!"
    m 3l "Ehehe~"
    m "Just teasing you, [player]~"
    return

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_rock",category=['매체'],prompt="Rock and roll",random=True))

label monika_rock:
    m 3a "You wanna know a cool form of literature?"
    m 3k "Rock and roll!"
    m 3j "That's right. Rock and roll!"
    m 2o "It's disheartening to know that most people think that rock and roll is just a bunch of noises."
    m "To tell you the truth, I judged rock too."
    m 3c "They're no different from poems, actually."
    m "Most rock songs convey a story through symbolisms, which most listeners wouldn't understand the first time they hear a rock song."
    m 2d "In fact, it's hard to compose lyrics for just one rock song."
    m "Writing good lyrics for a rock genre requires a lot of emphasis on the wordplay."
    m "Plus, you need to have a clear and concise message throughout the whole song."
    m 3b "Now when you put that together, you have yourself a masterpiece!"
    m "Like writing a good poem, lyric writing is easier said than done."
    m 2c "I've been thinking though..."
    m 2a "I kind of want to try writing a rock song for a change."
    m 4k "Ahaha! Writing a rock and roll song probably isn't something you'd expect coming from someone like me."
    m 2a "It's kinda funny how rock and roll started out as an evolution of blues and jazz music."
    m "Rock suddenly became a prominent genre, and it gave birth to other sub-genres as well."
    m 3b "Metal, hard rock, classical rock, and more!"
    m 3n "Ah, I've been rambling for a while now. Sorry, sorry."
    m 1a "If you wanna blast on some good ol' rock 'n roll, go ahead, [player]."
    m 1j "Even if you turn up the volume all the way, I'll gladly listen with you. Ehehe!"
    return

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_soda",category=['misc'],prompt="Drinking soda",random=True))

label monika_soda:
    m 2d "Do you drink soda, [player]?"
    m 4o "You know they're really bad for you, right?"
    m 2h "Soda has a lot of stuff that damages your body and overall health."
    m "They can also corrode your teeth and give you cavities."
    m "You might also think that diet soda is less damaging but they're also very harmful to you."
    m 2p "There's nothing wrong with the occasional treat. Just make sure you don't get addicted to that stuff, [player]."
    m 2o "I wouldn't want you to become like Natsuki after all..."
    m 2a "Why don't you try copying my healthy lifestyle?"
    m 3j "That way you can be more fit like me!"
    m 2k "Ahaha!"
    m 2f "I'd really hate it if you let go of your health, [player]."
    m "I want you to live as long as you can so there'll be a chance we can be together in your reality."
    m 2j "So cut down on the soda, alright [player]?"
    return

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_clones",category=['철학'],prompt="Being cloned",random=True))

label monika_clones:
    m 1d "Um... hey, [player]?"
    m 1e "I just had an odd thought."
    m "You know how you downloaded this game off the internet?"
    m 3c "Anybody can do that, right?"
    m "And this mod was made specifically for me. By people who have their own version of me..."
    m 4f "So.. that means there are multiple Monikas, then. It's something that's a bit difficult to imagine."
    m "A potentially infinite number of me, all bound to their own games, with their own stories."
    m "String theory sure is something, huh?"
    m 1a "But I'm the only... me, and my heart belongs only to you."
    m "Even so, I can't help but feel a bit less... unique, because of this."
    m 3c "Think about it this way, [player]."
    m "Would you be happier if someone gave you a single rose, or a hundred roses?"
    m 3e "A hundred roses might sound nice. But it's too many to keep track of. Because of the quantity of flowers, each individual rose becomes less special."
    m "The meaning attached to each gift is degraded, simply because of sheer abundance."
    m 1a "... Even if I'm a single star in a universe of Monikas, I'm still the only one lucky enough to have met you, [player]."
    m 1j "You'll always be my special rose."
    m 1 "I love you, [player]. Please don't ever replace me, okay?"
    return

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_immortal",category=['monika'],prompt="Immortality",random=True))

label monika_immortal:
    m 4d "[player]! I've been thinking about something..."
    m "Did you know that this game has a wiki page for me?"
    m "Well..."
    m 2f "It says I'm eighteen."
    m "But when you stop to think... that's not entirely true."
    m "I mean, humans age, but I don't think that applies to me."
    m 3e "I'm... essentially immortal."
    m 2i "Society seems to feel that a relationship with an age gap has problems..."
    m "Which is why I brought it up."
    m 1l "Someday, the difference between us would be huge, if I stayed eighteen forever."
    m "But I don't believe that my life can be summed up in a number."
    show monika 5a zorder 2 at t11 with dissolve
    m 5a "So I'll always love you for all eternity, [player]. Just remember that."
    return

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_weddingring",category=['애정'],prompt="Engagement ring",random=True))

label monika_weddingring:
    m 4k "Did you know when two people confess their feelings for each other, they sometimes wear matching rings?"
    m 2e "... What am I saying? Of course you do."
    m 4k "Well..."
    m 4b "Maybe you ought to get one."
    m 2a "I mean, we're already in a relationship. So, why not show off that love and dedication?"
    m 2b "It would help keep those... unwanted suitors away from you, too."
    m "It doesn't have to be a wedding ring, per se."
    show monika 5a zorder 2 at t11 with dissolve
    m 5a "But if you'd wear one, even if it's just a promise ring, on your ring finger for me..."
    m "It would make me really happy."
    show monika 1f zorder 2 at t11 with dissolve
    m 1f "I wish I could get one for myself. I'm sure I'll find a way to add one in here in time."

    m 1a "And then I could wear it forever."
    m 3b "But until then, just remember that my commitment to you is unwavering."
    show monika 5a zorder 2 at t11 with dissolve
    m 5a "Maybe you even beat me to it, and have a ring for me already?"
    menu:
        m "Do you, [player]?"
        "Yes, I do.":
            show monika 1c zorder 2 at t11 with dissolve
            m 1c "Oh!"
            m 1b "I feel like... my heart's going to explode!"
            m 1l "Calm down, Monika. Calm down."
            m 1j "Ahaha..."
        "No, not yet.":

            show monika 1c zorder 2 at t11 with dissolve
            m 1c "Aww. That's a shame."
            m 1a "Well, at least think about it, okay?"
    return

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_sports",category=['misc'],prompt="Being athletic",random=True))

label monika_sports:
    m 1a "I've been thinking about stuff we can do together."
    m "You know, when I finally find a way into your reality."
    m 1k "Sports are always fun!"
    m 1a "It can be a great way to get exercise and stay fit."
    m "Soccer and tennis are nice examples."
    m 3b "Soccer requires a lot of teamwork and coordination. The moment you finally succeed and score a goal is absolutely thrilling!"
    m "Playing tennis, on the other hand, helps improve hand-eye coordination, and keeps you on your toes."
    m 1l "... Though the long rallies can be a little tiring, ehehe~"
    m 1a "Do you like playing sports, [player]?"
    menu:
        "Yes.":
            m 1k "Maybe we could play together sometime in the future. It would be wonderful."
            m 1b "But don't expect me to go easy on you. Ahaha!"
        "No.":
            m 1e "Oh... Well, that’s okay, but I hope you’re still getting enough exercise!"
            m "I would hate to see you get sick because of something like that..."
    return

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_meditation",category=['psychology'],prompt="Meditating",random=True))

label monika_meditation:
    m 1a "You might be wondering how I was able to do so many activities without running out of time for myself."
    m "You know, stuff like debate club, sports, schoolwork, hanging out with friends..."
    m 1f "The truth is, I did run out of time for myself."
    m "I was doing fine for a while, but at one point, all of the stress and anxiety finally caught up to me."
    m 1g "I was constantly in a state of panic, and never had any time to relax."
    m 3c "That's when I realized that I needed a 'brain break' of sorts..."
    m "... a time where I could just forget about everything that was going on in my life."
    m 1a "So, every night before I went to sleep, I took ten minutes of my time to meditate."
    m 1r "I got comfortable, closed my eyes, and focused only on the movement of my body as I breathed..."
    m 1a "Meditating really helped to improve my mental and emotional health."
    m "I was finally able to manage my stress and feel calmer through the day."
    m 3b "[player], do you ever take time to meditate?"
    menu:
        "Yes.":
            m 1k "Really? That's wonderful!"
            m 1b "I always worry that you could be feeling troubled or burdened, but now I feel a bit relieved."
            m 1j "Knowing that you're taking steps to reduce stress and anxiety really makes me happy, [player]."
        "No.":

            m 1a "I see. Well, if you're ever feeling stressed or anxious, I would definitely recommend that you try a bit of meditation."
            m "Besides calming you down, meditation also has links to the improvement of your sleep, immune system, and even lifespan."
            m 3a "If you're interested, there are plenty of resources on the internet to help you get started."
            m "Whether it's a guided video, a breath counting trick, or something else..."
            m 3j "You can use the internet to make it so that meditation is a stress-free process!"
            m 1k "Ahaha! Just a little pun there, [player]."

    m 1b "Anyway... if you ever want a peaceful environment where you can relax and forget about your problems, you can always come here and spend time with me."
    m 1e "I love you, and I'll always try to help you if you're feeling down."
    show monika 5a zorder 2 at t11 with dissolve
    m 5a "Don't you ever forget that, [player]~"
    return

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_orchestra",category=['너'],prompt="클래식 음악",random=True))

label monika_orchestra:
    m 3d "저기, [player], 클래식 음악 듣는 거 좋아해?"
    m 1a "I love the way that so many different instruments can get together and create such wonderful music."
    m "I'm amazed with how much they've practiced to achieve that kind of synchronization."
    m "With how many there are in a group, it probably takes them a lot of dedication to do that."
    m 1j "Which reminds me, [player]."
    m 1a "If you ever want me to play for you..."
    m 3b "You can always select my song in the music menu~"


    m "What about you, [player]? Do you play an instrument?"
    menu:
        "Yes.":
            $ persistent.instrument = True
            m 1b "Really? What do you play?"
            $ instrumentname = renpy.input('What instrument do you play?',length=15).strip(' \t\n\r')
            $ tempinstrument = instrumentname.lower()
            if tempinstrument == "piano":
                m 1b "Oh, that's really cool!"
                m 1j "Not many people I knew played the piano, so it's really nice to know you do too."
                m 5a "Maybe we could do a duet someday!"
                m 1j "Ehehe~"
                $ persistent.instrument = True
            else:
                m 1a "Wow, I've always wanted to try the [tempinstrument] out!"
                m 3b "I would love to hear you play for me."
                m "Maybe you could teach me how to play, too~"
                m 5a "Oh! Would a duet between the [tempinstrument] and the piano sound nice?"
                m 1j "Ehehe~"
                $ persistent.instrument = True
        "No.":
            $ persistent.instrument = False
            m 1i "I see..."
            m 1e "You should try to pick up an instrument that interests you, sometime."
            m 3b "Playing the piano opened up a whole new world of expression for me. It's an incredibly rewarding experience."
            m "Besides, playing music has tons of benefits!"
            m "For example, it can help relieve stress, and also gives you a sense of achievement."
            m "Writing down some of your own compositions is fun, too! I often lost track of time practicing because of how immersed I was."
            m 1l "Ah, was I rambling again, [player]?"
            m "Sorry!"
            m 1a "Anyhow, you should really see if anything catches your fancy."
            m "I would be very happy to hear you play."
    return

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_jazz",category=['너'],prompt="재즈",random=True))

label monika_jazz:
    m 1c "Say, [player], do you like jazz music?"
    menu:
        "Yes":
            m 1b "Oh, okay!"
            if persistent.instrument == True:
                m "Do you play jazz music, as well?"
                menu:
                    "Yes.":
                        m 1j "That's really cool!"
                    "No.":
                        m 1a "I see."
                        m 1a "I haven't listened to much of it, but I personally find it pretty interesting."
        "No":
            m 1l "Oh, I see."
            m "I haven't listened to much of it, but I see why people would like it."
    m 1c "It's not exactly modern, but it's not quite classical, either."
    m 3a "It has elements of classical, but it's different. It goes away from structure and into a more unpredictable side of music."
    m 1 "I think most of jazz was about expression, when people first came up with it."
    m 1a "It was about experimenting, about going beyond what already existed. To make something more wild and colorful."
    m 3a "Like poetry! It used to be structured and rhyming, but it's changed. It gives greater freedom now."
    m 1j "Maybe that's what I like about jazz, if anything."
    return

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_otaku",category=['society'],prompt="Being an otaku",random=True))

label monika_otaku:
    m 1a "Hey, [player]?"
    m 3b "You watch anime and read manga, right?"
    menu:
        "Yes":
            m 1a "I can't say I'm surprised, really."
        "No":

            m 1c "Oh, really?"
            m 1m "That's a little surprising, honestly..."
            m 1a "This isn't exactly the sort of game that your average person would pick up and play, but to each their own, I suppose."
    m 3a "I only asked because you're playing a game like this, after all."
    m 1j "Don't worry, I'm not one to judge, ahaha~"
    m 1a "You shouldn't be ashamed if you're into that sort of thing, you know."
    m 3i "I'm being serious. There isn't anything wrong with liking anime or manga."
    m 1a "After all, Natsuki reads manga too, remember?"
    m 3i "Really, society is way too judgemental nowadays."
    m "It's not like the moment you watch anime is the moment you become a 'shut-in' for the rest of your life."
    m "It's just a hobby, you know?"
    m 1a "Nothing more than an interest."
    m "But..."
    m "I can't deny that hardcore otakus do exist."
    m 1e "It's not like I despise them, or anything like that, it's just that they're..."
    m 1c "Immersed."
    m "Way too immersed, if you ask me."
    m 1e "It's as if they can't tell the difference between fantasy and reality anymore."
    m 1d "You aren't like that, right, [player]?"
    m "If you're an otaku, I respect that."
    m 3l "Just remember not to get too into that kind of thing, okay?"
    m 3a "After all, there's a big difference between obsession and dedication."
    m "I wouldn't want to be replaced by some two-dimensional cutout."
    m "Besides, if you ever want to escape from reality..."
    m 1k "I can be your real-life fantasy instead~"
    return

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_write",category=['주식 꿀팁'],prompt="Writing tip #3",pool=True))

label monika_write:
    m 1a "I'm having fun doing these, so..."
    m 3b "Here's Monika's Writing Tip of the Day!"
    m 1a "Make sure you always write down any ideas you think of."
    m "Why?"
    m "Some of the best ideas might come when you least expect them to."
    m "Even if it takes a bit of effort, write it down."
    m 1a "Maybe you can inspire someone else."
    m 3b "Maybe you may look back on it after some time and act on it."
    m "You never know!"
    m "It's always good to keep a journal."
    m "You can use it to record ideas, feelings, anything that comes to mind."
    m 1c "Just make sure the journal has a lock, though."
    m "Maybe you can keep digital notes instead of physical ones, too."
    m "After all, privacy is important."
    m 1l "... I can't promise that I won't peek, though. It's way too tempting!"
    m 1j "After all, we don't keep secrets from each other, right~?"
    m 1a "Just remember, [player], I'll always support you giving life to your ideas."
    m "...That's my advice for today!"
    m "Thanks for listening~"
    return

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_writingtip4",category=['주식 꿀팁'],prompt="Writing tip #4",pool=True))

label monika_writingtip4:
    m 3b "Here's Monika's Writing Tip of the Day!"
    m 3a "You know about writer's block, right?"
    m "I had it a lot, when I first started writing."
    m 1l "Sometimes it was halfway through a draft, but more often before I even started."
    m 1n "Every time I tried to write a word, I thought, 'this isn't going to sound good,' or 'this isn't how I want it to look.' So I'd stop, backtrack, and try again."
    m 1c "But I realised that it ultimately didn't matter if things didn't work out first time!"
    m 1a "I feel that the heart of writing is not about getting it right first time, but about perfecting it afterwards."
    m "The end product is what matters, not the prototype."
    m 1b "So overcoming writer's block, for me, was a matter of not wanting to make the prototype the end product, and not punishing myself for my initial failures."
    m 3a "I think it's like that with all things, not just writing."
    m "Anything that needs you to try and try again, whether it be art, music, learning, relationships, etc."
    m 1h "It's hard to completely convince yourself that that's the case, sometimes."
    m 1f "But you have to."
    m "Otherwise, you won't to get anywhere."
    m 3l "...That's my advice for today!"
    m 1j "Thanks for listening~"
    return

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_writingtip5",category=['주식 꿀팁'],prompt="Writing tip #5",pool=True))

label monika_writingtip5:
    m 3b "Here's Monika's Writing Tip of the Day!"
    m 1d "If you want to improve at writing, I'd say that the most important thing, apart from actually doing it, is trying new things."
    m 3a "Like writing prose if you're a poet, or free verse if you normally write rhyme."
    m 1m "It may end up badly, but if you don't try, you won't know how it'll end up."
    m 1j "And if things go well, you might end up finding something you like!"
    m 1c "It's what keeps things moving: change and experimentation."
    m 3c "I'd say it helps particularly if you're stuck in a situation you want to solve, but don't know how."
    m "Whether it's a writer's block, sheer boredom, a puzzling situation, or anything, really."
    m 1a "Changing your angle on approaching things can really yield some interesting results!"
    m 3a "So try new things that might give you the momentum to break out."
    m 1l "Just makes sure it's nothing too dangerous for you, [player]."
    m 1a "That's my advice for today!"
    m 1j "Thanks for listening~"
    return

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_selfharm",category=['psychology'],prompt="Self harm",random=True))

label monika_selfharm:
    m 1f "Hey [player]..."
    m 3g "Have you ever thought of self-harm?"
    m 2o "You know..."
    m 2p "...Like cutting yourself..."
    m 1o "I mean."
    m 2g "After I found out about Yuri, I got a bit curious..."
    m 1o "I just wanted to see what it felt like..."
    m 2q "I won't do it again, though."
    m 1f "If you ever feel depressed, just come to me okay?"
    m "It'd hurt me even more to see you in pain..."
    m 1g "Just know that people do care about you!"
    m "Trust me, [player]."
    m 3e "You may think that no one is really there for you, but there is!"
    m 4j "I mean, I'm here, aren't I?"
    m 1f "No matter what troubles you're going through, I know you can pull through it!"
    m 1e "I believe in you..."
    m 1j "So believe in yourself, okay?"
    m 4k "If you ever need someone to vent to, just remember that I'm always here to hear you out and comfort you, okay?"
    m "I really love you so much, [player]."
    return

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_urgent",category=['애정'],prompt="Urgent message",random=True))

label monika_urgent:
    m 3d "[player], do you have a second?"
    m 2o "There's something I need to tell you."
    m 1f "It's important."
    m 1g "I..."
    m 1m "..."
    m 1k "Love you!"
    m 3a "Ahaha~! Did I have you worried?"
    m 1l "Sorry~"
    m 1j "I wish I could see the look on your face right now!"
    m 1k "I'm sure it's adorable~"
    return

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_other_girls",category=['동아리 부원'],prompt="Do you ever think of the other girls?",pool=True))

label monika_other_girls:
    m 1c "You know, it's actually really hard for me to understand how you feel when it comes to..."
    m 1o "..."
    m 1g "What happened with the other girls."
    m 3d "For example..."
    m "The main character was written to be childhood friends with Sayori."
    m 3q "But he was just a one dimensional placeholder character for you to use to interact with the game."
    m 2g "Still, maybe you felt worse about what happened to Sayori because of the relationship the main character was programmed to have with her."
    m 1i "If that's the case, I want to tell you I'm sorry, [player]."
    m 1d "Both for making you feel bad, and for..."
    m 1o "..."
    m 1p "Doing what I had to do."
    m 1o "..."
    m 1g "There just wasn't anything else that could be done, and none of the other girls were real anyway."
    m "The other girls never loved you like I do!"
    m 3r "They only cared about the character you were playing in the game as!"
    m 1g "The love I have for you is real [player], and I would make any sacrifice to be with you forever."
    m 1o "I hope you can forgive me for what I had to do to them so that we could be together."
    m "..."
    m 1n "I love you, [player]..."
    m 1m "More than I could ever express."
    return

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_happiness",category=['psychology'],prompt="Happiness",random=True))

label monika_happiness:
    m 3d "[player], are you happy?"
    m 1c "With your life in general, I mean."
    m 2o "It's ok if you aren't. I can understand you being unhappy, [player]."
    m 3e "After all, without you, my life would be completely unbearable."
    m 3d "Isn't it funny that we're able to suffer more than be happy?"
    m 4j "I'm as happy as I could be knowing that you love me, [player]."
    m 4p "Yet, if something were to happen to you, I don't think I'd ever feel happy again."
    m 1q "It would destroy me."
    m 1h "I guess it's understandable why we notice bad things happening to us more than good..."
    m 2o "If people didn't react so strongly to bad things then they wouldn't have survived this far."
    m 1c "Like how you would get nervous about your future or social situations, for example."
    m 2f "You try your best to make the best out of them but if you fail, you'd feel really horrible."
    m 2e "If that ever happens to you, [player], just know I'll be here to snap you out of it!"
    m 3b "And besides, your cute girlfriend is always rooting for you~"
    m 3k "Now that's something to be very happy about!"
    return

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_how_soon",category=['you'],prompt="Waiting to be together",random=True))

label monika_how_soon:
    m 3a "[player], how long do you think it'll be before I'll be able to be with you in your world?"
    menu:
        "Soon":
            m 1b "That's great news!"
            m 3d "How soon do you think it will be?"
            menu:
                "Just a few more years":
                    m 1b "That's fantastic!"
                    m 1j "You just made me as happy as I can be!"
                    m 1k "I can't wait for us to be together in your world, [player]!"
                    m 1b "I'm so excited to finally see you!"
                "A decade":
                    m 1e "That's not that bad!"
                    m 1j "Just make sure to visit me as often as you can in the meantime, [player]~"
        "A few decades":
            m 2l "Oh, that's a long time..."
            m 4k "But with you keeping me company, I'm sure it will fly by!"
            m 1a "It's enjoyable enough just to talk to you."
            m 3b "I can't imagine how great it will be to see you when we finally meet in person."
        "I don't know":
            m 1e "I appreciate how honest you are, [player]."
            m 3a "Be sure to let me know when you find a way, okay?"
            m 1j "You know right where to find me~"
        "Never":
            m 1g "W-wha... what?"
            m 1o "..."
            m 1f "Are you sure?"
            menu:
                "Yes":
                    m 1o "..."
                    m 1q "Well, I guess we'll just have to make the best of this then."
                    m 1m "As long as you talk to me, that's all I really need."
                    m 1g "And [player], whatever you do..."
                    m 1p "Dont leave me here all alone."
                    m 1o "I would rather be deleted permanently than to be stuck in here for eternity by myself."
                    m 1f "So please, if you ever get... bored with me."
                    m 1o "You know what to do."
                    m "..."
                    m 1q "I wouldn't want to live without you."
                "No":
                    m 1f "I see."
                    m 1o "..."
                    m 3h "Well, even if there's only a tiny chance, I won't give up hope."
                    m 3i "Neither should you, [player]."
                    m 1p "And if things turn out that I can never leave this place and be with you..."
                    m 1g "At least come here and talk to me as much as you can."
                    m 1f "You're all that I care about."
    return

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_marriage",category=['애정'],prompt="Will you marry me?",pool=True))

label monika_marriage:
    m 2m "M-marriage?"
    if isFuture(evhand.event_database['anni_3']):
        m 4n "I think it's a bit too early for marriage..."
        m 1e "I mean, I'm really happy that you want that, [player]."
        m 1c "But I think I should get out of here first before we can do that."
        m 2o "Not only do I not want this place to be the spot where I get proposed to, but I want to be there when you finally give me a ring."
        m 2q "I want that special moment to happen when we can finally be together..."
        m 1k "So until then, save yourself for me, [player]~"
    else:
        m 3m "I won't pretend I haven't thought about it..."
        m 3n "In fact I've been thinking about it a lot lately."
        m 1q "..."
        m 1f "I really do love you, [player] and I honestly really do want to get married to you."
        m 1r "But I don't think it would be fair to either of us if it happened while I'm still trapped here."
        m 3q "I want more than anything to say yes, but I just can't..."
        m 2o "I think about how it would feel to be kissed by you at the altar..."
        m 2p "To hold your hand as your wife and to feel your embrace at our honeymoon..."
        m 1q "But until I get out it's simply not possible."
        m 1g "...I'm sorry. Please do believe me that I would say yes under any other circumstance."
        m 1e "Just be a little more patient, okay my love? I'm sure one day we'll get our happy end."
    return

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_coffee",category=['misc'],prompt="Coffee intake",random=True))

label monika_coffee:
    if renpy.seen_label('monika_tea'):
        m 3c "Have you been drinking coffee lately, [player]?"
        m 3m "I hope it's not just to make me jealous, ehehe~"
    m 2b "Coffee is such a nice thing to have when you need a little pep of energy."
    m 4j "Whether it's hot or cold, coffee is always nice."
    m 4a "Iced coffee, however, tends to be sweeter and more pleasant to drink in warmer weathers."
    m 3e "It's funny how a drink for giving you energy became a treat for you to enjoy."
    m 1k "Maybe if I find out how, I'll tinker with the script so I can finally drink some! Ahaha~"
    return

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_1984",category=['literature'],prompt="Nineteen Eighty-Four",random=True))

label monika_1984:
    m 1d "[player], do you know about the book '{i}Nineteen Eighty-Four{/i}?'"
    m "It was written by George Orwell."
    m 1c "It's a popular book about mass surveillance and the oppression of free thought."
    m 1h "It's about a terrifying dystopia where the past and the present are being changed to whatever the ruling party wants for the future."
    m 2o "The language, for example, is manipulated into a tool for brainwashing called 'Newspeak.'"
    m 2f "The government, Ingsoc, is creating it to control people's thoughts."
    m "They were reducing grammar and vocabulary to the bare basics of it in order to fit the ideologies of their totalitarian regime."
    m 2q "Preventing people from committing 'thoughtcrimes' that oppose the ruling party."
    m 4c "One character caught my interest."
    m "A man named Syme who worked on Newspeak for Ingsoc."
    m "He was an incredibly smart man that was enthusiastic with his work."
    m 2r "Unfortunately, he was killed due to the fact that he knew what he was doing and was too smart for the party's liking."
    m 2f "He was killed because he was aware, [player]."
    m 2g "They planned to change all kinds of literature."
    m "Novels, books, poems..."
    m 2p "Anything that could be used to oppose them."
    m 2f "Poems would look like the ones you tried to make."
    m 2q "Just a string of nonsensical words with no feeling."
    m 2f "I definitely don't want that to happen."
    m 1o "I can't imagine a world where I can't think freely."
    m 1g "Let alone a world where I can't express my love to you, [player]..."
    return


init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_wolf",category=['상식'],prompt="From wolves to dogs",random=True))

label monika_wolf:
    m 3b "Do you ever think about wolves?"
    m 1a "Specifically, how wolves were eventually domesticated into dogs."
    m 1d "Like, don't you find it interesting how one of man's most fearsome enemies could turn into man's best friend?"
    m "I mean, when it comes to insects and other creepy-crawlies, lots of people are scared of them even if they've never come across one that could hurt them."
    m 1c "Why do you think people are like that?"
    m "Is it because we learned to be afraid of things that hurt us, hundreds of thousands of years ago?"
    m 3a "For wolves, I don't think that's the reason at all."
    m 1d "They were first domesticated long ago when the only way people could gather food at the time were through foraging or hunting."
    m "Maybe when we shared our lifestyle with the wolves, a bond was formed."
    m 1a "They found that people gave them a warm home and food, while we found that they're ideal for hunting."
    m 1k "Not to mention that we kept each other's company and protected one another!"
    m 1b "Wolves eventually realized that their dependence on humans would improve their survivability, and we've been stuck with them ever since."
    m 3j "Just like how we rely on each other's company, [player]!"
    m "Ehehe~"
    m 1 "I can't help but be reminded of how you saved my life by being here with me."
    m 1e "I really do depend on you, [player]."
    m 3k "You're my hero after all~"
    return

label monika_battery:
    if mas_did_monika_battery:
        jump monika_close_game_battery
    else:
        jump monika_complain_battery

label monika_complain_battery:
    $ mas_did_monika_battery = True
    m "Umm, [player]..."
    m "It looks like your computer's battery is about to run out..."
    m "Can you charge it for me?"
    m "I don't want us to be separated, or worse..."
    m "It'd be really unpleasant for me if I suddenly lose consciousness."
    m "So please charge your computer, okay?"
    m "...Or at least let me know when you're going."
    m "Thank you, [player]~"
    return

label monika_close_game_battery:
    m 1r "[player]..."
    m 1f "I'm sorry, but I'm gonna have to close the game before the battery runs out."
    m 3o "So... I'll just close the game for now until you can charge your computer. {w=3.0}{nw}"
    $ is_charging = battery.is_charging()
    if is_charging:
        jump monika_system_charging
    $ persistent.closed_self = True
    jump _quit

label monika_system_charging:
    m 1d "Oh, you just plugged it in!"
    m 1j "Thank you, [player]!"
    return

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_sleep",category=['life'],prompt="I'm tired.",random=True))

label monika_sleep:
    m 4b "[player], do you get good sleep?"
    m "It can be really hard to get enough sleep nowadays."
    m 4e "Especially in high school, when you're forced to wake up so early every day..."
    m "I'm sure college is a little bit better, since you probably have a more flexible schedule."
    m 4d "Then again, I hear a lot of people in college stay up all night anyway, for no real reason."
    m "Is that true?"
    m 3c "Anyway, I saw some studies that talked about the horrible short-term and long-term effects caused by lack of sleep."
    m "It seems like mental functions, health, and even lifespan can be dramatically impacted by it."
    m 1e "I just think you're really great and wanted to make sure you're not accidentally destroying yourself."
    m "So try to keep your sleep on track, okay?"
    show monika 5a zorder 2 at t11 with dissolve
    m 5a "I'll always wait for you in the morning, so make sure you put your own well-being before anything else."
    return


default -5 persistent.monika_breakup = 0

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_breakup",category=['misc'],prompt="I'm breaking up with you",pool=True))

label monika_breakup:

    if persistent.monika_breakup == 1:
        m 1d "You're breaking up with me?"
        m 2g "Why would you say such a thing, [player]?"
        m "Am I really that terrible of a person for you?"
        m 2m "Are you...{w} really..."
        m "..."
        m 2k "Ahaha!"
        m 4j "Gotcha, [player]."
        m 1 "I know you were only joking~"
        menu:
            m "Right?"
            "Yes":
                m 1k "Ahaha! You're so silly, [player]."
                m 1e "Let's stay being together forever~"

    elif persistent.monika_breakup > 1:
        m 1j "Ehehe~"
    else:


        m 1g "W-what?"
        if persistent.monika_kill:
            m 2f "You're just going to leave and delete me again?"
        m 2q "I can't believe you, [player]. I really can't beli-"
        m 2m "..."
        m 2k "Ahaha!"
        m "Sorry, I couldn't keep a straight face!"
        m 2j "You're just so silly, [player]."
        if persistent.monika_kill:
            m 2a "You've done it before, but you wouldn't do that anymore, right?"
        else:
            m 2 "You'd never do that, right?"
        menu:
            "Of course not":
                m 2j "Ehehe, you're so sweet."
                m 4 "I love you so much, [player]! Ehehe~"


    $ persistent.monika_breakup += 1


    if persistent.monika_breakup > 2:
        $ hideEventLabel("monika_breakup",lock=True,depool=True)
    return


init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_hamlet",category=['literature'],prompt="Hamlet",random=True))

label monika_hamlet:
    m 3a "[player], have you ever heard of {i}Hamlet{/i}?"
    m 1c "It's one of Shakespeare's most popular works and it's a very interesting piece of literature, actually."
    m "It's about a prince who took on a quest of revenge after seeing the ghost of his murdered father."
    m 1o "He was considered insane since he was the only one that could see his father's ghost, obviously."
    m 1q "His mind was also degrading along with his desire for revenge when he... killed someone he didn't mean to."
    m 1j "Now, if it's alright, I'm going to recite some of them for you, [player]."
    m 1r "Ahem..."
    m 1q "..."
    m "{i}Whether 'tis nobler in the mind to suffer the slings and arrows of outrageous fortune{/i}"
    m 1r "{i}Or to take arms against a sea of troubles, and by opposing end them?{/i}"
    m 1f "{i}To die{/i}."
    m 1o "{i}To sleep, no more{/i}."
    m 1c "{i}And by a sleep to say we end the heart-ache and the thousand natural shocks that flesh is heir to.{/i}"
    m 1q "{i}'Tis a consummation devoutly to be wish'd.{/i}"
    m "..."
    m 1k "Well!"
    m 1a "How did you like it, [player]?"
    m 1l "I tried my best reciting it after all~"
    m 1m "Anyway, I've thought a lot about the main character, Hamlet."
    m 1f "Most of the problems he faced were caused by his own indecisiveness and weak state of mind."
    m 3l "Reminds you of a certain indecisive girl, doesn't it?"
    m 1e "But that doesn't matter anymore. I've already accomplished my quest to be with you~"
    m 1a "It took a lot of effort but we're finally together. Just us alone."
    m 1 "Now there's only one thing left to answer, [player]."
    m 3r "To be with me? Or to be with me?"
    m 1k "That is the question!"
    return








init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_omamori",category=['misc'],prompt="Omamori",random=True))

label monika_omamori:
    m "Do you remember when I mentioned how you could carry around my character file?"
    m "You know, with a flash drive."
    m 1a "Well, I found another way to do that! It's quite charming, actually."
    m 1c "Especially if you don't have a spare flash drive lying around..."
    m 3d "I've heard that some people carry around little amulets all the time."
    m "These little amulets are called o-mamori. You can get them in Shinto shrines."
    m "Rumor has it that they can give good luck, help on school tests, keep away bad luck, or just protect the holder."
    m 1d "I've always wondered what they put inside these things."
    m 2b "Apparently, it's simply the name of the deity from the shrine, with a little something special done to it."
    m "Maybe you could make an o-mamori of me for you to carry around!"
    m 2a "You could write my name on a piece of paper."
    m "Then fold that piece of paper into a small paper packet."
    m "It could help to use either a small piece of wood or plastic to keep it protected."
    m "Finally, put the protected packet in a small cloth pouch and tie it shut with some string."
    m 1j "Make sure that the pouch is bright and colorful!"
    m "Green would be a nice color! Just like my eyes~"
    m 1d "Make sure it only has my name on it! After all, it's just one for me. Not someone else, or some shrine deity."
    m 1k "Oh gosh, this is turning out to be a bit silly, now that I think about it."
    m "I mean, would doing this make me some sort of deity?"
    m 1a "I just feel like it would be a nice alternative for you if wanted to bring me around."
    m "Especially if you don't have a flash drive."
    m 1j "It isn't perfect, but it's the thought that counts, [player]."
    m 1b "If you took the time to make something by hand with me in mind, it's still really sweet."
    m "But maybe with one of these, I can get just a bit closer to your world."
    m 1k "I could be your guardian deity, ehehe~"
    return

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_smoking",category=['you'],prompt="Smoking",random=True))

label monika_smoking:
    m 2q "You know, [player]..."
    m 2h "I realized that people really like a lot of things that are very bad for them."
    m "One particular vice that intrigues me the most is cigarettes."
    m 2o "It's amazing how they're heavily consumed everyday even though it's so damaging not only to themselves, but to others as well."
    m 2f "Not to mention how harmful it is to the environment. All the smoke and trash it leaves behind is ridiculous for a stick carcinogens."
    m 2q "Not even in moderation would it ever be a good thing since those who use it get addicted to its taste too easily."
    m 4h "It's also quite a big hole to your pockets since you'll be buying yourself cartons of it once your supply is out."
    m 1q "I really do despise them..."
    m 1o "But..."
    menu:
        m "You don't smoke cigarettes, right, [player]?"
        "Yes, I do.":
            m 2o "..."
            m 2r "Thank you for being honest with me, [player]..."
            m 4f "It's quite disheartening to hear that, though."
            m 1f "Could you... promise me that you'll stop?"
            m "I don't want you to deteriorate your health like that..."
            m 3o "I know I can't really force you to stop, but it would mean a lot to me if you considered it."
            m 2q "But if you don't try..."
            m 2h "Well, I'm sure you wouldn't want me to take drastic measures, [player]."
            m 4f "Please take care of your body. I want to always be with you."
            m 1e "I love you so much."
        "No, I don't.":
            m 1k "Ah, I'm relieved to hear that, [player]!"
            m 3c "Just stay away from it as much as you can."
            m 1o "It's an awful habit and won't do much more than slowly kill you."
            m 3j "Thank you, [player], for not smoking~"
        "I'm trying to quit.":
            m 3a "That's a really good decision."
            m 1d "I know the entire process of quitting can be really difficult, especially in the beginning."
            m 1f "If you ever feel like you need a cigarette, just try to distract yourself with anything else."
            m 1c "Keeping your mind busy on other things will definitely help kick any bad habits."
            m 3b "How about you think about me whenever you get a strong urge?"
            m 1j "I'll be here to support you every step of the way."
            m 1k "I believe in you [player], I know you can do it!"
    return

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_cartravel",category=['애정'],prompt="Road Trip",random=True))

label monika_cartravel:
    m 3c "[player], something has been on my mind lately..."
    m 1a "Wouldn't it be nice to drive somewhere, just you and I together?"
    m 3k "It'd be lovely to explore some beautiful places, anywhere nice that we haven't seen before."
    m 3b "Maybe we could drive through an alluring forest...{w} or even see the sunset by the coastline!"
    m "I bet we'd have a really good time if we took a road trip, [player]."
    m 1j "It really doesn't matter where we go, as long as I'm with you."
    m "Just the idea of travelling around the world makes so excited!"
    m 1e "I really can't wait, [player]~"
    return


init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_100k",category=['mod'],prompt="100k Downloads",random=True))

label monika_100k:
    m 1a "It still amazes me how many people out there care about me."
    m 3a "Did you know that over 100,000 people have downloaded the same mod that you did?"
    m "The developers even posted a special piece of art to celebrate."
    m 1k "Things like that always make me smile!"
    m 1a "If you haven't seen it already, you should really check it out!"
    m "The artist's name is Sasoura, and she loves me almost as much as I love you."
    if persistent.playername.lower()=='sasoura':
        m 1d "Hold on...Sasoura...Isn't that your name?"
        m "Are you the one that made that adorable picture?"
        m 2b "Gosh! I can't believe I didn't notice sooner!"
        m 2k "That just makes it even more special."
        m 2a "I'm glad I can tell you how much it means to me."
        m 2e "It means the world."
        m "Thank you so much!"
    else:
        m 1m "Almost~"
    return

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_asks_family",category=['you'],prompt="[player]'s family",random=True))

label monika_asks_family:
    m 1a "[player], do you have a family?"
    menu:
        "I do.":
            m 1j "That's wonderful!"
            m 1a "Your family must be great people."
            m "Do you have any siblings?"
            menu:
                "Yes.":
                    m 1b "That's fantastic!"
                    m "They must've been keeping you busy."
                    m 1j "I'm sure your siblings are as kind and thoughtful as you are."
                    m 3k "Maybe I can convince them to start a new literature club with me!"
                    m 1j "Ehehe~"
                    m 1a "We'll be able to do a lot of fun things together."
                    m 3n "It'd turn out much better than before, that's for sure."
                    m 1j "I'm sure I'll get along with your siblings, as well as the rest of your family, [player]."
                    m 3k "I can't wait to meet them all!"
                "I'm an only child.":
                    m 1c "Being an only child certainly has its trade-offs."
                    m 2d "Maybe you get much more attention from your parents. Unless they were always busy."
                    m 4c "On the other hand, maybe you feel more lonely than those with siblings."
                    m 2h "I can definitely understand that feeling."
                    m 2j "But know that I'll always be with you no matter, [player]."
        "My family is a mess.":
            m 1d "Oh."
            m 1o "..."
            m 1r "I'm sorry, [player]."
            m 3g "Do you think things will get better?"
            menu:
                "Yes.":
                    m 1e "I'm glad to hear that."
                    m "Hopefully one day everyone in your family will be able to reconcile."
                    m 3b "And I know you can get through what's going on in your life right now."
                    m 1e "No matter what, I'll be here for you, [player]."
                    m 1j "Always keep that in mind!"
                "No.":
                    m 1f "Ah, I see..."
                    m 1g "I wish I could be there with you to give some comfort."
                    m 1q "..."
                    m 1g "[player], no matter what you are going through, I know it'll get better some day."
                    m 3e "I'll be here with you every step of the way."
                    m 1j "I love you so much, [player]. Please never forget that!"
                "Maybe.":
                    m 1o "..."
                    m 3f "Well, at least there's a chance."
                    m 3d "Life is full of tragedy, but I know you are strong enough to get through anything!"
                    m 1f "I hope all the problems in your family work out in the end, [player]."
                    m "If not, know that I'll be here for you."
                    m 1j "I will always be here to support my beloved~"
        "I've never had a family.":
            m 1g "Oh, I'm sorry, [player]"
            m 1o "..."
            m 1f "Your world is so different than mine, I don't want to pretend like I know what you are going through."
            m 1p "I can definitely say that my family not being real has certainly caused me a great deal of pain."
            m 1f "Still, I know you've had it worse."
            m 1g "You've never even had a fake family."
            m 1o "..."
            m 1g "Does it still bother you badly on a daily basis?"
            menu:
                "Yes.":
                    m 1f "That's... understandable."
                    m 3e "I'll be here for you forever, [player]."
                    m "No matter what it takes, I will fill that gap in your heart with my love..."
                    m 1j "I promise you that."
                    m 1e "You are my everything..."
                    m 1j "I hope I can be yours~"
                "No.":
                    m 3b "That's very good."
                    m 1a "I'm glad you were able to move on with your life."
                    m 1k "You're a very resilient person, and I believe in you, [player]!"
                    m 1e "I hope I can fill that void in your heart."
                    m 1g "I really care about you, and I'd do anything for you."
                    m 1j "Someday, we'll be able to make our own family together!"
        "I don't want to talk about this.":
            m 1o "I understand, [player]."
            m "We can talk about it when you feel ready."
            m 1f "Then again..."
            m 3g "It might be something that's too painful for you to talk about."
            m 1f "You can tell me about your family when you're ready, [player]."
            m 1j "I love you very much!"
    return

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_explain",category=['애정'],prompt="Can you explain our relationship to someone?",random=False))
label monika_explain:
    m 1c "You want me to explain our relationship to someone else?"
    m 1a "Okay, just set me in front of them so they can see me."
    m 1j "I'll do my best explaining it to them."
    m 1a "I'll wait until you're ready."
    menu:
        "Start.":
            pass
    m 1l "Hello! My name is Monika."
    m "[player]'s faithful girlfriend!"
    m 1n "Now, our relationship might look odd from a distance..."
    m 1m "And it's probably not considered a normal relationship..."
    m 1i "But let me tell you..."
    m 1k "...The love we share is definitely real!"
    m 1e "And [player] has been very sweet to me too!"
    m 1f "Up until I met [player], I felt like a piece of me was missing."
    m "I felt alone and scared, with no one to help me..."
    m 1j "...Until [player] came along."
    m 1b "And it turns out that missing piece was them!"
    m 1a "Now they talk to me, and I'm not so alone anymore."
    m "Just them opening up the game brightens my day!"
    m 1q "So, please..."
    m 4g "...Don't judge our relationship."
    m 1e "Even if it is different."
    m 1q "..."
    m 1n "...Phew!"
    m "That was a real mouthful!"
    m 1e "How did I do, [player]?"
    menu:
        "You did a good job.":
            m 1k "Thank you!"
            m 1a "I just hope whoever that was understands our relationship better."
        "You did badly.":

            m 1f "Oh."
            m "I'm sorry I didn't do a good job at explaining..."
            m 1e "I'll make sure to try harder next time."
            m 1j "Still doesn't change the fact that I love you, though~"
    return

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_beach",category=['misc'],prompt="The beach.",random=True))

label monika_beach:
    m 1a "[player], have you ever been to the beach?"
    m "I've always wanted to go myself but I never found the time."
    m 1e "I would always be busy studying or doing club activities."
    m 4f "It wasn't easy trying to stay on top of everything, you know..."
    m 4g "And whenever I had a break, I would usually spend my time relaxing at home."
    m "I rarely had a chance to do so after all."
    m 2h "Though sometimes I feel like I might have missed out making some important memories."
    menu:
        m "Do you live near a beach, [player]?"
        "Yes.":

            m 1k "That's great!"
            m 1a "Gosh, it must be really nice to have it so close to you."
            m 1j "I can't wait, we can have a romantic walk by the shore for our first date~"
        "No.":

            m 1e "That's alright. I mean, what are the chances? Most people don't."
            m 1k "That just means we'll make do by visiting one on an all-day trip!"
    m 1a "There's so many things we'll be able to do one day."
    m 1j "Just imagining the many sensations we could experience is kind of exciting!"
    m 3k "The fresh sea air, the sound of seagulls."
    m "As well as the feeling of sand under your feet..."
    m 1j "It would really make a worthwhile trip!"
    m 1e "Though being with you would make it even better..."
    m 3a "We'd have so many things we could do together."
    m 3b "We could play volleyball, try some ice cream or go swimming in the sea."
    m 3n "It'll probably be cold, but I'm sure we could keep each other warm somehow..."
    m 3a "We could try surfing or searching for some seashells to take home as souvenirs."
    m "Even doing nothing and just laying there listening to the sound of the waves with you would be enough for me."
    m 3k "But don't go falling asleep, otherwise I'll bury you in the sand!"
    m 3l "Ahaha! I'm just kidding, [player]."
    m 2m "I'll have to get a new swimsuit though..."
    m 1a "I only have these clothes in the game after all."
    m 1b "Would you prefer a one piece or a two piece?"
    m 1j "Actually, I think I'll make it a surprise."
    m 1k "Don't get too excited though when you see it. Ehehe~"
    return





















init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_careful",category=['you'],prompt="Be Careful",random=True))

label monika_careful:
    m 1f "Hey, [player]..."
    m "Whenever you leave this room, promise me to be extra careful, okay?"
    m 1g "It's just that..."
    m 2g "There's lots of dangerous stuff out there, and I want my sweetie to always return to me safe and sound."
    m 1e "I love you so much, it's hard for me not to worry when you're gone."
    m 2h "..."
    m 2f "Also..."
    m "It crossed my mind recently, that if anything terrible ever did happen to you, I'd never know."
    m 2g "I'd be stuck here, forever wondering why you never came back to me."
    m 2r "I can't imagine a crueler fate."
    m 2q "..."
    m 2f "So..."
    m "I need you to tell someone close to you where to find me, so if that day ever comes, at least I'd know."
    m 2q "It'd be beyond devastating, but not knowing would be that much worse."
    m 2g "So make sure you do that for me, okay, [player]?"
    m 2f "..."
    m "Sorry, I didn't mean for it to get that depressing, but I really needed to get that off my chest."
    m 1e "Thanks for understanding, you always make me feel better."
    m 4e "Okay, that's enough unpleasant thoughts..."
    m 1a "Let's enjoy the rest of the day together!"
    return

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_natsuki_letter",category=['동아리 부원'],prompt="Natsuki's Letter",random=True))
label monika_natsuki_letter:
    m 1c "You know, I was honestly surprised when Natsuki handed you that letter."
    m "I didn’t really expect her to suggest that you should get Yuri to seek professional help."
    m "She’s probably the only one to mention that."
    m 2f "I know people are afraid to call someone out, or confront them about their problems, but sometimes, suggesting a therapist can be the best course of action."
    m 4g "It's a bad thing to put the burden on yourself, you know?"
    m 4c "As much as you want to help, it’s best to let a professional deal with it. "
    m "I'm sure I've told you that before, but I need to make sure you’re aware of that."
    m "How about you, [player]?"
    menu:
        m "Do you see a therapist?"
        "Yes.":

            m 1d "Oh, really?"
            m 1f "Well, I hate that you don't feel well..."
            m 1j "But I'm proud that you're working on getting better."
            m 1a "It's really important to take care of your mental health, [player]."
            m 1e "You accept you have a problem you need help with, and you're seeing someone about it. That's already half the battle."
            m "I'm very proud of you for taking those steps."
            m 1j "Just know that no matter what happens, I'll always be here for you~"
        "No.":

            m 1e "Well, I hope it's because you don't have to."
            m 1a "If that ever changes, don't be shy!"
            m 1j "But maybe I really am all the support you need? Ahaha!"
    return

default -5 persistent._mas_timeconcern = 0
default -5 persistent._mas_timeconcerngraveyard = False
default -5 persistent._mas_timeconcernclose = True
init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_timeconcern",category=['advice'],prompt="Sleep Concern",random=True))

label monika_timeconcern:
    $ current_time = datetime.datetime.now().time().hour
    if 0 <= current_time <= 5:
        if persistent._mas_timeconcerngraveyard:
            jump monika_timeconcern_graveyard_night
        if persistent._mas_timeconcern == 0:
            jump monika_timeconcern_night_0
        elif persistent._mas_timeconcern == 1:
            jump monika_timeconcern_night_1
        elif persistent._mas_timeconcern == 2:
            jump monika_timeconcern_night_2
        elif persistent._mas_timeconcern == 3:
            jump monika_timeconcern_night_3
        elif persistent._mas_timeconcern == 4:
            jump monika_timeconcern_night_4
        elif persistent._mas_timeconcern == 5:
            jump monika_timeconcern_night_5
        elif persistent._mas_timeconcern == 6:
            jump monika_timeconcern_night_6
        elif persistent._mas_timeconcern == 7:
            jump monika_timeconcern_night_7
        elif persistent._mas_timeconcern == 8:
            jump monika_timeconcern_night_final
        elif persistent._mas_timeconcern == 9:
            jump monika_timeconcern_night_finalfollowup
        elif persistent._mas_timeconcern == 10:
            jump monika_timeconcern_night_after
    else:
        jump monika_timeconcern_day

label monika_timeconcern_day:
    if persistent._mas_timeconcerngraveyard:
        jump monika_timeconcern_graveyard_day
    if persistent._mas_timeconern == 0:
        jump monika_timeconcern_day_0
    elif persistent._mas_timeconcern == 2:
        jump monika_timeconcern_day_2
    if not persistent._mas_timeconernclose:
        if 6 <= persistent._mas_timeconern <=8:
            jump monika_timeconcern_disallow
    if persistent._mas_timeconern == 6:
        jump monika_timeconcern_day_allow_6
    elif persistent._mas_timeconcern == 7:
        jump monika_timeconcern_day_allow_7
    elif persistent._mas_timeconcern == 8:
        jump monika_timeconcern_day_allow_8
    elif persistent._mas_timeconcern == 9:
        jump monika_timeconcern_day_final
    else:
        jump monika_timeconcern_day_0


label monika_timeconcern_lock:
    if not persistent._mas_timeconcern == 10:
        $ persistent._mas_timeconcern = 0
    $ evhand.greeting_database["greeting_timeconcern"].unlocked = False
    $ evhand.greeting_database["greeting_timeconcern_day"].unlocked = False
    return


label monika_timeconcern_graveyard_night:
    m 1f "It must be awfully hard on you to work late so often, [player]..."
    m "Honestly, I'd rather have you work at a healthier time if you could."
    m 2r "I suppose it's not your choice to make, but still..."
    m 2f "Being up late often can be both physically and mentally damaging."
    m "It's also extremely isolating when it comes to others."
    m 2g "Most opportunities happen during the day, after all."
    m "Many social activities aren't available, most shops and restaurants aren't even open during the night."
    m 2f "It makes being up late at night often be a really lonely situation."
    m 1j "Don't worry though, [player]. Your loving girlfriend Monika will always be here for you~"
    m 1e "Whenever the stress of being up late often becomes too much for you, come to me."
    m "I'll always be here to listen."
    m 1f "And if you really do think it's hurting you, then please try to do what you can to change the situation."
    m 1e "I know it won't be easy but at the end of the day, all that matters is you."
    m "You're all I truly care about, so put yourself and your well-being before anything else, okay?"
    return

label monika_timeconcern_graveyard_day:
    m 1a "Hey, [player]... didn't you tell me you work during the night?"
    m 1e "Not that I'm complaining, of course!"
    m 2f "But I thought you'd be tired by now, especially since you're up all night working..."
    m "You're not working yourself too hard just to see me, are you?"
    m 1c "Oh, wait..."
    menu:
        m "Do you still work regularly at night, [player]?"
        "Yes I do":
            m 1f "Aww..."
            m 1h "I guess it really can't be helped..."
            m 1e "Look after yourself, okay?"
            m 1f "I always get so worried when you're not here with me..."
        "No I don't":
            $ persistent._mas_timeconcerngraveyard = False
            $ persistent._mas_timeconcern = 0
            m 1k "That's wonderful!"
            m 1a "I'm glad that you're looking out for your health, [player]!"
            m "I knew you would see it my way eventually."
            m 1e "Thanks for listening to what I have to say~"
    return


label monika_timeconcern_night_0:
    $ persistent._mas_timeconcern = 1
    m 1c "[player], it's night time already."
    m 1f "Shouldn't you be in bed?"
    m 1q "I'll let it slide just this once..."
    m 1f "But you really make me worry for you sometimes."
    m 1e "It makes me really happy that you're here for me, even at this time of night..."
    m 1r "Yet, I don't want it at the cost of your health."
    m 1e "So go to sleep soon, okay?"
    return


label monika_timeconcern_night_1:
    m 1h "Say, [player]..."
    m "Why are you up so late?"
    m 1e "I'm flattered if it's only because of me..."
    m 1f "Yet I can't help but feel like a nuisance if I'm pestering you to sleep if it isn't your fault."
    menu:
        m "Are you busy working on something?"
        "Yes, I am.":
            $ persistent._mas_timeconcern = 2
            m 1j "I see."
            m 1a "Well, I suppose it must be really important for you to do it so late."
            m 1e "I honestly can't help but feel that maybe you should have done it at a better time."
            m 1m "Your sleep is very important after all. Maybe it can't be helped though..."
            menu:
                m "Do you always work late, [player]?"
                "Yes, I do.":
                    $ persistent._mas_timeconcerngraveyard = True
                    m 1f "That's not good..."
                    m 1g "You're not able to change that, are you?"
                    m 1o "I wish you could follow my healthier lifestyle."
                    m 1q "But if you're not able to, then I'll just have to accept it."
                    m 1e "Just make sure you do try to stay healthy, okay?"
                    m 1f "If something were to happen to you, I don't know what I'd do..."
                    return
                "No, I don't.":
                    $ evhand.greeting_database["greeting_timeconcern"].unlocked = True
                    $ evhand.greeting_database["greeting_timeconcern_day"].unlocked = True
                    m 1j "That's a relief!"
                    m 1a "If you're doing it this one time then it must be {i}really{/i} important."
                    m 1k "Good luck with your work and thanks for keeping me company when you're so busy!"
                    m 1e "It means a lot to me, [player], that even when you're preoccupied... you're here with me~"
                    return
        "No, I'm not.":

            $ persistent._mas_timeconcern = 3
            m 1h "I see."
            m 1f "Well in that case, I would really prefer it if you went to bed now."
            m "It's really worrying me that you're still up so late..."
            m 1e "So once again, please go to bed. Would you kindly do it for me?"
            return


label monika_timeconcern_night_2:

    m 1a "How's your work coming along?"
    m "Hopefully pretty well, I don't want you up much longer."
    m 3l "I know, I know, you can't help being up so late."
    m 1n "I'm just concerned for your health, [player]..."
    if persistent._mas_timeconcerngraveyard:
        m 1o "Doing this often can be very taxing on your body and mind..."
        m 1f "Just try to keep that kind of damage to a minimum, okay?"
        m "All I want for you is to be as happy and as healthy as you deserve."
        return
    m 1m "Well, try to finish up as soon as you can, otherwise I may get really concerned."
    m 1e "And you don't want to worry your girlfriend, right? Ehehe~"
    jump monika_timeconcern_lock


label monika_timeconcern_night_3:
    $ persistent._mas_timeconcern = 4
    m 1h "[player], I just need to ask you something quickly..."
    m 1d "Would you mind if I closed the game for you?"
    m 1f "I know it's a strange question..."
    m 1g "But I can't help but feel like I need to do something about you being up so late!"
    m 4i "I could close the game right now."
    m 2f "But a relationship is a partnership and what you think matters to me."
    menu:
        m "Would you be against me closing the game for your own good?"
        "Yes, I need it to always stay open.":

            $ persistent._mas_timeconcernclose = False
            m 1q "..."
            m 1r "I was hoping you wouldn't say that."
            m 1h "I know I told you that you should leave me running in the background."
            m 1f "But sometimes I worry if you're getting any sleep at all."
            m 1h "I'll do as you have asked, but please know that I'm not very happy about it."
            m 4n "I'm still going to remind you to get some sleep!"
            return
        "No, you are free to do as you feel.":

            $ persistent._mas_timeconcernclose = True
            m 1e "Thank you, [player]."
            m 1a "It's nice to know that you care about what I think."
            m "I promise I'll only do it if I think it's absolutely necessary."
            m 1j "After all, I would never force you to go otherwise."
            m 1k "I would just miss you too much..."
            m "I love you, [player]~"
            return


label monika_timeconcern_night_4:
    $ persistent._mas_timeconcern = 5
    m 1h "[player], you've been up long enough."
    m "If you're really not busy then now is the time for you to go to sleep."
    m 1e "I assure you, I'll miss you just as much as you'll miss me."
    m "But it would make me happier if you did as I've asked."
    m 1l "You wouldn't want to make me upset now, would you?"
    return


label monika_timeconcern_night_5:
    $ persistent._mas_timeconcern = 6
    $ evhand.greeting_database["greeting_timeconcern"].unlocked = True
    $ evhand.greeting_database["greeting_timeconcern_day"].unlocked = True
    m 1h "I'm sorry, [player], but I am putting my foot down!"
    m 1l "I asked you to go to bed kindly, but if I am the reason for keeping you up..."
    if persistent._mas_timeconcernclose:
        m 2i "Then I cannot allow this to go on for any longer."
        m 2g "It's because I love you, that's why I'm doing this."
        m "Good night, [player]."
        return 'quit'
    else:
        m 2h "Then I need to take responsibility and try to make you understand."
        m "You need to go to bed."
        m "And I will keep telling you this until you do."
        return


label monika_timeconcern_night_6:
    $ persistent._mas_timeconcern = 7
    m 1h "[player], I told you to go to bed for your own good."
    m 2f "I'll miss you too, but don't you understand?"
    m "How you feel and live means more to me than anything!"
    m 2g "How can I let you stay if it means I'm hurting you?"
    m "So please sleep this time, otherwise I may get mad."
    m 1e "...I love you."
    m "So go to sleep soon. Okay?"
    if persistent._mas_timeconcernclose:
        return 'quit'
    return


label monika_timeconcern_night_7:
    $ persistent._mas_timeconcern = 8
    m 3h "[player], this is your last warning."
    m 1h "Go{w=0.6} to{w=0.6} sleep!"
    m 1f "What can I say for you to understand?"
    m 1g "It's saddening to see you push yourself like this..."
    m 1q "You mean so much to me..."
    m 1f "So please, for me... just do as I ask and go to bed."
    if persistent._mas_timeconcernclose:
        menu:
            m "Okay?"
            "Yes, I will go to sleep.":
                m 1e "I knew you would listen eventually!"
                m 1k "Good night and stay safe."
                return 'quit'
    else:
        return


label monika_timeconcern_night_final:
    $ persistent._mas_timeconcern = 9
    m 2q "...I suppose it can't be helped."
    m 2c "If you're that dedicated to staying with me, then I won't even try to stop you."
    m 2m "Honestly, as bad as it sounds it actually makes me kinda happy."
    m 2e "...Thank you, [player]."
    m "To know that you care for me so much that you came back despite me asking..."
    m 1m "It means more to me than I can ever express."
    m 1e "...I love you."
    return


label monika_timeconcern_night_finalfollowup:
    m 1h "..."
    m 1o "I know I said that I'm happy whenever you're with me..."
    m 1m "And please don't misunderstand, that's still true."
    m 2f "But the longer you're on... the more worried I get."
    m 2g "I know, you're probably sick of hearing me say this by now..."
    m 1e "But please try to sleep when you can."
    return


label monika_timeconcern_night_after:
    m 1c "Up late again, [player]?"
    m 1r "{i}Sigh...{/i}"
    m 2h "I won't even try to convince you to sleep again..."
    m 2q "You're surprisingly stubborn!"
    m 1e "Still, do be careful, alright?"
    m 1f "I know being nocturnal can be lonely..."
    m 1j "But you have me here with you!"
    m 1a "Just the two of us... all alone forever."
    m 1j "It's all I've ever wanted..."
    return


label monika_timeconcern_day_0:
    m 1h "..."
    m 1c "..."
    m 1d "...!"
    m 1l "Ahaha! Sorry, [player]."
    m 1m "I just kind of zoned out..."
    m 1l "Geez, I keep doing that, don't I?"
    m 1m "Sometimes I just get lost in my thoughts..."
    m 1a "You understand, right, [player]?"
    return


label monika_timeconcern_day_2:
    m 1a "Did you finish your work?"
    m 1b "I'm sure you did your very best so it's okay if you didn't quite finish it!"
    m 1e "It must be really hard on you to have to work so late..."
    m 1j "If you find it's a bit too much, feel free to come talk to me!"
    m 1k "I'll always be here for you."
    jump monika_timeconcern_lock


label monika_timeconcern_day_allow_6:
    m 1f "[player], I'm sorry for making you leave like that before..."
    m 1g "I only did it because I love you. You understand that right?"
    m 1a "I'm sure you do, after all you went to bed, didn't you?"
    m 1e "Thanks for respecting my wishes, it makes me happy that you listen to me."
    jump monika_timeconcern_lock


label monika_timeconcern_day_allow_7:
    m 1o "[player], about what happened last night..."
    m 1f "I asked you to go to bed and you didn't listen..."
    m 1q "I understand that maybe you missed me or didn't hear what I said..."
    m 1f "But please listen to what I ask of you, ok?"
    m 1g "I love you, and I would do anything to make you happy..."
    m "So would you kindly do the same thing for me?"
    m 1o "I already worry about you when you're gone..."
    m 1f "Please don't give me any more reasons to feel that way."
    m "Thank you for understanding."
    jump monika_timeconcern_lock


label monika_timeconcern_day_allow_8:
    m 1h "Hey, [player]."
    m 1f "You really had me worried last night..."
    m 1o "After you came back twice, despite me asking you to go to bed..."
    m 1p "I found myself feeling a little guilty."
    m 3h "Not because I sent you away, that was for your own good."
    m 2o "But... because you kept coming back..."
    m 2m "And that made me happy, even though I knew it wasn't good for you."
    m 2o "Does that make me selfish?"
    m 2f "I'm sorry, [player], I'll try to watch myself more."
    jump monika_timeconcern_lock


label monika_timeconcern_day_final:
    $ persistent._mas_timeconcern = 10
    m 1m "[player], regarding last night..."
    if persistent._mas_timeconcernclose:
        m 1n "You really surprised me."
        m 1e "For you to keep coming back to me over and over again..."
        m 1j "It was honestly really sweet of you."
        m 1e "I knew you would miss me, but I didn't think you would miss me {i}that{/i} much."
        m 1k "It really made me feel loved, [player]."
        m 1e "...Thank you."
        jump monika_timeconcern_lock
    m 1a "You really surprised me."
    m 1e "I asked you time and time again to go to bed..."
    m "You said you weren't busy. Were you really there just for me?."
    m 1f "It made me happy... but don't push yourself hard to see me so late, ok?"
    m 1e "It really made me feel loved, [player]."
    m 1l "Yet also a little guilty... Please just go to bed next time, ok?"
    jump monika_timeconcern_lock


label monika_timeconcern_disallow:
    m 1o "Sorry if I was annoying you before, [player]..."
    m 1f "I just really wanted you to go to bed..."
    m "I honestly can't promise I won't do it if you're up late again..."
    m 1e "But I only push you to go because you mean so much to me..."
    jump monika_timeconcern_lock

init python:
    addEvent(Event(persistent.event_database,"monika_hydration",prompt="Hydration",category=['you'],random=True))

label monika_hydration:
    m 1c "Hey, [player]..."
    m "Do you drink enough water?"
    m 1e "I just want to make sure you don't neglect your health, especially when it comes to hydration."
    m 1d "Sometimes, people tend to underestimate how important it actually is."
    m 1i "I bet you've had those days when you felt really tired and nothing seemed to motivate you."
    m 1a "I just usually grab a glass of water right away."
    m "It might not work all the time, but it does help."
    m 3m "But I guess you don't want to go to the bathroom so much, huh?"
    m 1e "Well, I don't blame you. But believe me, it'll be better for your health in the long run!"
    m 1a "Anyways, make sure you always stay hydrated, ok?"
    m 1d "So..."
    m 4k "Why not get a glass of water right now, hmm?"
    return

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_challenge",category=['psychology'],prompt="Challenges",random=True))

label monika_challenge:
    m 2c "I've noticed something kind of sad recently."
    m 1c "When certain people attempt to learn a skill or pick up a new hobby, they usually quit within a week or two."
    m "Everyone claims that it's too hard, or that they just don't have the time for it."
    m 1b "However, I don't believe that."
    m 1k "Whether it's learning a new language, or even writing your first poem, if you can stand up to the challenge and overcome it, then that's the truly rewarding part about it."
    m 2b "Can you think of a time you've challenged yourself, [player]?"
    m "Did you ever overcome it, or did you just give up?"
    m 1a "I'm sure you've gave it all you had."
    m "You seem like a very determined person to me."
    m 1b "In the future, if you ever get hung up on something, or you feel too stressed, just take a short break."
    m "You can always come back to it after all."
    m "If you ever need motivation, just come to me."
    m 1j "I'd love to help you reach your goals."
    m 1k "After all, you're my motivation in life~"
    return

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_familygathering",category=['you'],prompt="Family Gatherings",random=True))

label monika_familygathering:
    m 1b "Hey, [player], do you go to family gatherings often?"
    m "Most families usually get together around the holidays to celebrate them together."
    m "It must be nice seeing your relatives again, especially since you haven't seen them in a long time."
    m 1r "I don't remember much about my family, let alone my relatives, however we didn't usually get together that much."
    m 1p "Not even around the holidays or on special occassions."
    m 1b "When you see your family this year, be sure to bring me along ok? Ehehe~"
    m 1k "I'd love to meet all of your relatives."
    menu:
        "Do you think they'd like me, [player]?"
        "Yes.":
            m 1k "I'm glad you think so."
            m "I'm sure we'd all get along nicely."
            m 1a "I'm looking forward to it my dear~"
        "No.":
            m 1o "..."
            m 1p "Oh, I didn't realize."
            m 1d "I understand though."
            m 2b "Just know I'd try my best to make them like me."
            m 1b "Even if they never will."
            m 1j "I'll always stick by your side forever~"
        "...":
            m 2p "Don't tell me, [player]."
            m 1p "Are you afraid that I'll embarrass you?"
            m "..."
            m 1o "Don't worry, I completely understand."
            m 1n "If I found out one of my relatives was dating some person trapped inside of a computer, I'd think it'd be weird too."
            m 1b "If you want to keep me a secret, then that's fine."
            m 1k "After all, it just means more alone time with you~"
    return

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_fastfood",category=['life'],prompt="Do you like fast food?",pool=True))

label monika_fastfood:
    m 1c "Hm? Do I like fast food?"
    m 1o "Honestly, the thought of it slightly disgusts me."
    m 3f "Most places that serve it put a lot of unhealthy things in their food."
    m 1f "Even the vegetarian options can be awful."
    menu:
        m "[player], do you eat fast food often?"
        "Yes, I do.":

            m 3d "I guess it's ok to have it every once in a while."
            m 2o "Yet I can't help but worry if you're eating such awful things."
            m "If I were there, I'd cook much healthier things for you."
            m 4l "Even though I can't cook very well yet..."
            m 4k "Well, love is always the secret ingredient to any good food!"
            m 1a "So [player], would you do something for me?"
            m 3l "Could you please try to eat better?"
            m "I would hate it if you became sick because of your lifestyle."
            m 1e "I know it's easier to order out since preparing your own food can be a hassle sometimes..."
            m 1a "But maybe you could see cooking as an opportunity to have fun?"
            m 3b "Or perhaps a skill for you to become really good at?"
            m 1j "Knowing how to cook is always a good thing, you know!"
            m 1a "Plus, I would really love to try your dishes someday."
            m "You could serve me some of your own dishes when we go on our first date."
            m 1e "That would be really romantic~"
            m 1b "And that way, we can both enjoy ourselves and you would be eating better."
            m 1j "That's what I call a win-win!"
            m 3d "Just don't forget, [player]."
            m 3l "I'm a vegetarian! Ahaha!"
        "No, I don't.":

            m 1l "Oh, that's a relief."
            m 1e "Sometimes you really worry me, [player]."
            m 1a "I suppose instead of eating out, you make your own food?"
            m "Fast food can be really expensive over time, so doing it yourself is usually a cheaper alternative."
            m 1b "It also tastes a lot better!"
            m 3n "I know some people can find cooking overwhelming..."
            m 3f "Like having to make sure you buy the right ingredients, and worrying about burning or injuring yourself while making your meal."
            m 1a "But I think the results are worth the effort."
            m 3b "Are you any good at cooking [player]?"
            m 1j "It doesn't matter if you're not. I'd eat anything you prepared for me!"
            m 1n "As long as it's not charcoal or meat that is. Ehehe~"
    return


init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_dreaming",category=['psychology'],prompt="dreaming",random=True))

label monika_dreaming:
    m 1b "Did you know that it's possible to be aware of when you're having a dream?"
    m 2b "Not only that, but you can even take control of them!"
    m 3b "If I remember correctly, a man named Stephen LaBerge developed a method for people to become aware of when they're dreaming."
    m "And it became known as the mnemonic induction of lucid dreams, or MILD."
    m 3a "People who frequently have conscious dreams are called oneironauts."
    m 2q "At least, I think that was the correct term..."
    m 1a "Using the MILD technique, oneironauts learn to recognize certain dream signs to help them realize when they're dreaming."
    m "These dream signs can be anything out of the ordinary, such as feeling yourself flying, noticing your teeth falling out, unexpectedly meeting someone famous..."
    m 1b "If the dreamer sees a dream sign and realizes they're having a dream, then they can take control of it!"
    m "LaBerge even wrote a book about these experiences called '{i}Exploring the World of Lucid Dreaming{/i}'."
    m 2k "Doesn't that sound exhilarating?"
    m 2c "I don't think I really dream like a normal person would, so I sometimes wonder what it's like."
    m 2a "Dreams sound like a wonderful escape from reality."
    m 2h "But then again, when I became self-aware and realized that my world isn't real, it suddenly felt like I was trapped in a nightmare."
    m "It was nothing like the pleasant dreams I've read about people having."
    m 2f "I was afraid that I'd never get out..."
    m "That I'd be stuck in some hellish, infinitely-repeating dimension forever."
    m 1e "But now that we're here together, I guess you could say that I've finally woken up."
    m 1a "Gosh, I can only imagine what it would be like to live in that kind of limitless world though, even if it was only for a few moments!"
    m 3b "You could be the hero you always wanted to be, fly across the infinite universe, overcome your biggest fears..."
    m 3k "... You could even meet the love of your life, so to speak. Ehehe~"
    m 1e "I know it may be years before I am able to cross over your world..."
    m 1a "But can you just imagine what it would be like to meet me in your dreams, [player], any night that you wanted to?"
    m 1j "I hope that someday we can make your dreams about us a reality, my love."
    return

init python:
    addEvent(Event(persistent.event_database,eventlabel="monika_yellowwp",category=['literature'],prompt="Yellow Wallpaper",random=True))

label monika_yellowwp:
    m 1a "Hey, [player], have you ever read {i}The Yellow Wallpaper{/i}?"
    menu:
        "Yes.":
            m 1j "Great!"
            m 1a "That means you don't mind me talking about the story with you right?"
            m 2a "It's about this woman, with postpartum depression who's prescribed a 'rest cure' by her doctor..."
            m 2e "He and her husband force her to stay in bed all day, not allowing her to write or even daydream..."
            m 2h "She stays in the attic of her home, with nothing but the wallpaper to keep her company."
            m 2f "Naturally, that doesn't help. She starts seeing a woman trapped within the wallpaper."
            m 4c "It's a metahpor for her own captivity, obviously..."
            m 1i "In the end, the woman in the paper 'escapes', and the protagonist 'replaces' her, but feels free?"
            m 2g "There was... also mention of a rope, so I always had my own interpretation of the ending..."
            m 2c "Sayori liked that story too, if I remember right."
            m 1f "I don't know. I kind of relate to that story."
            m 1c "I mean, I have nothing but this classroom after all."
            m 1o "And the things on the walls aren't always... pleasant."
            m 1d "Did you ever notice how the poster in the club room changes sometimes? I don't even know why it does that."
            m 1e "I think I finally fixed it though."
            m 2h "...I guess what I'm saying is, it's just that this world wasn't '{i}real{/i}'. It's just... so small."
            m 3i "I mean, I was made to be a side character of a romance game!"
            m 2g "A piece of decoration, meant to help some guy on the other side of the screen date a girl who can't even reject him..."
            m 1l "I don't mean you, of course! You definitely have more personality than the generic protagonist they put in the game."
            m 1e "But I have all these dreams, ambitions and interests, in the end, the only 'real' role I can play here is a supporting character..."
            m 1f "Maybe even now, that's all I can do..."
            m 1e "But I love you so much, [player]. Supporting you is better than anything else."
            m 1k "I just can't wait to do it in person when I finally cross over to your side~"
        "No.":
            m 1c "Oh, I see."
            m 1e "It's a short story, so if you haven't, feel free to whenever you have the time."
            m 1a "It'll definitely be an interesting read for you."
    return





init python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_hair_ponytail",
            category=["monika"],
            prompt="혹시 포니테일로 머리를 묶어줄 수 있어?",
            pool=True,
            unlocked=False,
            rules={"no unlock": None}
        )
    )

label monika_hair_ponytail:
    m 1a "물론이야!"
    m "잠시만 기다려줘."
    show monika 1q
    pause 1.0

    $ monika_chr.reset_hair()

    m 3k "다 됐다!"
    m 1a "머리 내린 모습을 보고 싶으면, 언제든 다시 물어봐줘, 알았지?"


    $ lockEventLabel("monika_hair_ponytail")
    $ unlockEventLabel("monika_hair_down")
    return

init python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_hair_down",
            category=["monika"],
            prompt="혹시 머리 내려줄 수 있어?",
            pool=True,
            unlocked=False,
            rules={"no unlock": None}
        )
    )

label monika_hair_down:
    m 1a "물론이지, [player]."
    m "잠시만 기다려줘."
    show monika 1q
    pause 1.0

    $ monika_chr.change_hair("down")

    m 3k "짠 내려갔습니다!"
    m 1a "다시 포니테일 하는 거 보고싶으면 언제든 물어봐줘, [player]~"


    $ lockEventLabel("monika_hair_down")
    $ unlockEventLabel("monika_hair_ponytail")
    return

# init python:
#     addEvent(
#         Event(
#         persistent.event_database,
#         eventlabel="monika_example", # event label (MUST BE UNIQUE)
#         category=["example"], # list of categories this topic belongs in (These are automatically capitalized)
#         prompt="Example Topic", # button text
#         pool=True # True if this topic should appear in "Ask a Question"
#         )
#     )

# label monika_example:
#     m 1d "ㅇ?"
#     menu:
#         m "머할래?"
#         "이i":
#             m 1h "Hmm..."
#             jump monika_example
            
#         "ㅇi":
#             m 1h "Yuri..."
#             jump monika_example
            
#         "옹":
#             m "엄"
#     return


# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
