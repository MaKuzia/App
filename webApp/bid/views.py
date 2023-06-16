from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from bid.models import Bid, Status
from bid.utils import paginate_bids
from bid.forms import BidForm

User = get_user_model()

@login_required
def index(request):
    template = 'bid/index.html'
    title = 'Последние обновления'
    context = {
        'title': title,
        'page_obj': paginate_bids(request, Bid.objects.all()),
    }
    return render(request, template, context)

@login_required
def profile(request, username):
    template = 'bid/profile.html'
    user = get_object_or_404(User, username=username)
    user_bids = user.bids.all()
    context = {
        'user': user,
        'page_obj': paginate_bids(request, user_bids)
    }
    return render(request, template, context)
 
@login_required
def bid_detail(request, bid_id): 
    template = 'bid/bid_detail.html'
    bid_req = get_object_or_404(Bid, pk=bid_id)
    context = {
        'bid': bid_req,
    }
    return render(request, template, context)


@login_required
def bid_create(request):
    template = 'bid/create_bid.html'
    form = BidForm(
        request.POST or None,
        files=request.FILES or None,)
    if form.is_valid():
        bid = form.save(False)
        bid.user = request.user
        bid.status = Status.objects.get(status='New')
        bid.save()
        return redirect('bid:profile', bid.user.username)
    return render(request, template, {'form': form})

@login_required
def bid_edit(request, bid_id):
    template = 'bid/create_bid.html'
    current_bid = get_object_or_404(Bid, pk=bid_id)
    if request.user != current_bid.user or current_bid.status.status != 'New':
        return redirect('bid:bid_detail', current_bid.pk)
    form = BidForm(
        request.POST or None,
        files=request.FILES or None,
        instance=current_bid,
    )
    if form.is_valid():
        current_bid.save()
        return redirect('bid:bid_detail', current_bid.pk)
    context = {
        'form': form,
        'is_edit': True,
    }
    return render(request, template, context)