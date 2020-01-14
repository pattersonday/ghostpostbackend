from rest_framework import viewsets
from ghosts import models, serializers
from rest_framework.response import Response
from rest_framework.decorators import action


class BoastsAndRoastsView(viewsets.ModelViewSet):

    queryset = models.BoastsAndRoasts.objects.all()
    serializer_class = serializers.BoastsAndRoastsSerializer

    @action(detail=True, methods=['get'])
    def upvote(self, request, pk=None):
        like = models.BoastsAndRoasts.objects.get(pk=pk)
        like.total_votes += 1
        like.save()
        return Response({'status': 'liked'})

    @action(detail=True, methods=['get'])
    def downvote(self, request, pk=None):
        like = models.BoastsAndRoasts.objects.get(pk=pk)
        like.total_votes -= 1
        like.save()
        return Response({'status': 'disliked'})

# from django.shortcuts import HttpResponseRedirect, render, reverse


# from .models import BoastsAndRoasts
# from .forms import BoastsAndRoastsAddForm


# def index(request):
#     html = 'index.html'

#     boastsandroasts = BoastsAndRoasts.objects.all().order_by('-post_date')

#     return render(request, html, {'boastsandroasts': boastsandroasts})


# def BoastsAndRoastsFormView(request):
#     html = 'boastandroast_form.html'

#     if request.method == 'POST':
#         form = BoastsAndRoastsAddForm(request.POST)

#         if form.is_valid():
#             data = form.cleaned_data
#             BoastsAndRoasts.objects.create(
#                 is_boast=data['is_boast'],
#                 content=data['content']
#             )
#             return HttpResponseRedirect(reverse('homepage'))

#     form = BoastsAndRoastsAddForm()

#     return render(request, html, {'form': form})


# def UpvoteAddView(request, id):

#     html = 'index.html'

#     try:
#         upvotes = BoastsAndRoasts.objects.get(id=id)
#     except BoastsAndRoasts.DoesNotExist():
#         return HttpResponseRedirect(reverse('homepage'))

#     upvotes.upvote += 1
#     upvotes.total_votes += 1

#     upvotes.save()

#     return HttpResponseRedirect(reverse('homepage'))

#     upvotes = UpvoteAddView()

#     return render(request, html, {'upvotes': upvotes})


# def DownvoteAddView(request, id):

#     html = 'index.html'

#     try:
#         downvotes = BoastsAndRoasts.objects.get(id=id)
#     except BoastsAndRoasts.DoesNotExist():
#         return HttpResponseRedirect(reverse('homepage'))

#     downvotes.downvote -= 1
#     downvotes.total_votes -= 1

#     downvotes.save()

#     return HttpResponseRedirect(reverse('homepage'))

#     downvotes = DownvoteAddView()

#     return render(request, html, {'downvotes': downvotes})


# def Boasts(request):

#     html = 'all_boasts.html'

#     all_boasts = BoastsAndRoasts.objects.all().filter(
#         is_boast=True).order_by('-post_date')

#     return render(request, html, {'all_boasts': all_boasts})


# def Roasts(request):

#     html = 'all_roasts.html'

#     all_roasts = BoastsAndRoasts.objects.all().filter(
#         is_boast=False).order_by('-post_date')

#     return render(request, html, {'all_roasts': all_roasts})


# def NetVotes(request):

#     html = 'net_votes.html'

#     net_votes = BoastsAndRoasts.objects.all().order_by('-total_votes')

#     return render(request, html, {'net_votes': net_votes})


# def DeletePost(request, id):

#     deleting = BoastsAndRoasts.objects.get(id=id)

#     deleting.delete()

#     return HttpResponseRedirect(reverse('homepage'))

#     deleting = DeletePost()

#     return render(request, {'deleting': deleting})
