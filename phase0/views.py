from django.http.response import HttpResponse, HttpResponseBadRequest
from rest_framework.views import APIView

from helpers.permissions import TeamPermission


class Phase0View(APIView):
    permission_classes = [TeamPermission]

    def get(self, request, *args, **kwargs):
        return HttpResponse(request.team.text)

    def post(self, request, *args, **kwargs):
        answer = request.data.get('answer')
        member = request.data.get('member')
        text = request.team.text

        checklist = {'1': text.smallest_repeated_word, '2': str(text.distinct_longest_words)}
        if member in checklist:
            if answer == checklist[member]:
                return HttpResponse("Correct answer! You've completed your phase0 part! Congrats!")
            else:
                return HttpResponse("Wrong answer:( Keep trying...")
        return HttpResponseBadRequest("Invalid request data! Make sure you declared 'member' "
                                      "correctly in your request. It should be either '1' or '2' ")
