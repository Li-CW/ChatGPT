from rest_framework.views import APIView
from rest_framework.response import Response
import openai
from chatGPT.models import ChatQuestion
from Hasity.settings import OPEN_AI_KEY

class ChatView(APIView):
    openai.api_key = OPEN_AI_KEY
    def post(self, request):
        question = request.data["question"]
        try:
            if question[-1] != "!" and question[-1] != "?" and question[-1] != "." and question[-1] != "。" and question[-1] != "？":
                question = question + "?"
            response = openai.Completion.create(
            model="text-davinci-003",
            prompt=request.data["question"],
            temperature=0.7,
            max_tokens=4000,
            top_p=0.1,
            )
        except:
            return Response({
                'result': "我累了，休息了。等几分钟后再来问我。~~",
            })
        ans1 = response["choices"][0].text
        tail = ans1[-1]; 
        tail = ans1[-1]; 
        ans1 = ans1[:-1]
        ans1 = ans1.strip()
        ans1 = ans1.strip('?')
        ans1 = ans1.strip(';')
        ans1 = ans1.strip('!')
        ans1 = ans1.strip('.')
        ans1 = ans1.strip('。')
        ans1 = ans1.strip(',')
        ans1 = ans1.strip('？')
        ans1 = ans1.strip('，')
        ans1 = ans1.strip('；')
        ans1 = ans1.strip('！')
        ans1 = ans1.strip()
        ans1 = ans1 + tail
        return Response({
            'result': ans1,
        })
