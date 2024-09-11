
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Profile, Post,Notification, DonationRequest
from .forms import ProfileForm, SignupForm, PostForm
from django.core.paginator import Paginator
from django.views.decorators.http import require_POST
from django.utils import timezone
from django.db import transaction
from django.http import JsonResponse
from collections import defaultdict
from django.contrib import messages
from django.db.models import Q  # Add this import



CATEGORY_CHOICES = [
        ('EMERGENCY', 'Emergency Relief'),
        ('MEDICAL', 'Medical Aid'),
        ('EDUCATION', 'Education'),
        ('ENVIRONMENT', 'Environmental Causes'),
        ('ANIMAL', 'Animal Welfare'),
        ('COMMUNITY', 'Community Development'),
        ('HUNGER', 'Hunger Relief'),
        ('HOUSING', 'Housing and Shelter'),
        ('OTHER', 'Other Causes'),
    ]


def analytics_redirect(request):
    return redirect('https://app.powerbi.com/groups/me/reports/a77d757b-cc3d-4344-bd36-a45313451b99/ReportSection?experience=power-bi')

def redirect_to_powerbi(request):
    return redirect('https://app.powerbi.com/groups/me/reports/a77d757b-cc3d-4344-bd36-a45313451b99/ReportSection?experience=power-bi')

def profile_view(request):
    return render(request, 'profile.html')

def search_view(request):
    query = request.GET.get('q')
    search_results = []
    if query:
        search_results = Post.objects.filter(title__icontains=query)
    return render(request, 'search.html', {'search_results': search_results})

def landing(request):
    return render(request, 'landing.html')

def about(request):
    return render(request, 'about.html')

def donorInfo(request):
    # Filter posts that are donation offers (post_type='OFFER')
    posts = Post.objects.filter(post_type='OFFER', public=True)

    # Get the selected category and search query from the request
    selected_category = request.GET.get('category')
    search_query = request.GET.get('search')

    # Filter posts by category if a category is selected
    if selected_category:
        posts = posts.filter(category=selected_category)

    # Filter posts by search query if provided
    if search_query:
        posts = posts.filter(
            Q(title__icontains=search_query) |
            Q(body__icontains=search_query) |
            Q(author__name__icontains=search_query)
        )

    # Order posts by date
    posts = posts.order_by('-date')

    # Pagination
    paginator = Paginator(posts, 20)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)

    context = {
        'posts': posts,
        'categories': CATEGORY_CHOICES,
        'selected_category': selected_category,
        'search_query': search_query,
    }

    return render(request, 'donorInfo.html', context)

def recipientInfo(request):
    # Filter posts that are donation requests (post_type='REQUEST')
    posts = Post.objects.filter(post_type='REQUEST', public=True)

    # Get the selected category and search query from the request
    selected_category = request.GET.get('category')
    search_query = request.GET.get('search')

    # Filter posts by category if a category is selected
    if selected_category:
        posts = posts.filter(category=selected_category)

    # Filter posts by search query if provided
    if search_query:
        posts = posts.filter(
            Q(title__icontains=search_query) |
            Q(body__icontains=search_query) |
            Q(author__name__icontains=search_query)
        )

    # Order posts by date
    posts = posts.order_by('-date')

    # Pagination
    paginator = Paginator(posts, 20)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)

    context = {
        'posts': posts,
        'categories': CATEGORY_CHOICES,
        'selected_category': selected_category,
        'search_query': search_query,
    }

    return render(request, 'recipientInfo.html', context)
    
def showProfile(request, user_id):
    profile = Profile.objects.get(user=user_id)
    user = Profile.objects.select_related().get(user=user_id)
    posts = Post.objects.filter(author_id=user_id)
    context = {
        'profile': profile,
        'posts': posts,
        'user': user,
    }
    return render(request, 'profile/show.html', context)

def profileIndex(request):
    profiles = Profile.objects.all()
    context = {'profiles': profiles}
    return render(request, 'profile/index.html', context)

@login_required
def addProfile(request):
    profile = get_object_or_404(Profile, user=request.user)
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
        if profile_form.is_valid():
            updated_profile = profile_form.save(commit=False)
            updated_profile.user = request.user
            updated_profile.save()
            return redirect('showProfile', request.user.id)
        else:
            error_message = 'Something went wrong - please check your inputs and try again'
    else:
        profile_form = ProfileForm(instance=profile)
    
    context = {
        'profile_form': profile_form,
        'error_message': error_message if 'error_message' in locals() else ''
    }
    return render(request, 'profile/add.html', context)


@login_required
def myProfile(request):
    profile = Profile.objects.get(user=request.user)
    posts = Post.objects.filter(author_id=profile.id)
    context = {
        'profile': profile,
        'posts': posts,
    }
    return render(request, 'profile/show.html', context)

@login_required
def editProfile(request):
    error_message = ''
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if profile_form.is_valid():
            edited_profile = profile_form.save()
            return redirect('showProfile')
        else:
            error_message = 'Something went wrong - try again'
    else:
        profile_form = ProfileForm(instance=request.user.profile)
    context = {
        'profile_form': profile_form, 
        'error_message': error_message
    }
    return render(request, 'profile/edit.html', context)

@login_required
def deleteProfile(request):
    if request.method == 'POST':
        Profile.objects.get(user=request.user).delete()
        return redirect('landing')
    else:
        error_message = 'Something went wrong - try again'
        return render(request, 'showProfile')

def showPost(request, post_id):
    post = Post.objects.get(id=post_id)
    context = { 'post': post }
    return render(request, 'post/show.html', context)

@login_required
def addPost(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST, request.FILES)
        if post_form.is_valid():
            new_post = post_form.save(commit=False)
            new_post.author = request.user.profile
            new_post.post_type = post_form.cleaned_data['post_type']  # Explicitly set post_type
            new_post.save()
            return redirect('showPost', new_post.id)
    else:
        post_form = PostForm()
    context = {'post_form': post_form, 'author': request.user}
    return render(request, 'post/add.html', context)

@login_required
def deletePost(request, post_id):
    Post.objects.get(id=post_id).delete()
    return redirect('recipientInfo')

@login_required
def editPost(request, post_id):
    found_post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        post_form = PostForm(request.POST, request.FILES, instance=found_post)
        if post_form.is_valid():
            updated_post = post_form.save()
            return redirect('showPost', updated_post.id)
    else:
        post_form = PostForm(instance=found_post)
    
    context = {
        'post': found_post,
        'post_form': post_form
    }
    return render(request, 'post/edit.html', context)


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            profile = Profile.objects.create(
                user=user,
                name=user.username,
                date_of_birth=timezone.now().date(),
                location="Not specified",
                bio="No bio yet.",
            )
            login(request, user)
            return redirect('addProfile')
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})

from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Post, Profile, DonationRequest, Notification

@login_required
def add_donation_request(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    requester_profile = request.user.profile
    
    # Check if the post is a donation offer (OFFER type)
    if post.post_type != 'OFFER':
        messages.error(request, "You can only request donations for 'Donation Offer' posts.")
        return redirect('showPost', post_id=post_id)
    
    # Check if the requester is not the author of the post
    if post.author == requester_profile:
        messages.error(request, "You cannot request your own donation offer.")
        return redirect('showPost', post_id=post_id)
    
    # Check if a request already exists
    existing_request = DonationRequest.objects.filter(
        post=post,
        recipient=requester_profile,
        status='PENDING'
    ).exists()
    
    if existing_request:
        messages.warning(request, "You have already requested this donation.")
        return redirect('showPost', post_id=post_id)
    
    # Create the donation request
    donation_request = DonationRequest.objects.create(
        post=post,
        recipient=requester_profile,
        donor=post.author,
        status='PENDING'
    )
    
    # Create notification for the donor
    Notification.objects.create(
        user=post.author.user,
        message=f"New donation request: {post.title} from user {requester_profile.user.username}",
        donation_request=donation_request
    )
    
    messages.success(request, "Your donation request has been sent successfully!")
    return redirect('showPost', post_id=post_id)

@login_required
def get_notification_count(request):
    count = Notification.objects.filter(user=request.user, is_read=False).count()
    return JsonResponse({'count': count})

@login_required
def notifications_list(request):
    notifications = Notification.objects.filter(user=request.user).select_related('donation_request__post').order_by('-created_at')
    
    grouped_notifications = defaultdict(list)
    for notification in notifications:
        if notification.donation_request:
            post = notification.donation_request.post
            key = (post.id, post.title)
        else:
            key = ('other', 'Other Notifications')
        grouped_notifications[key].append(notification)
    
    # Sort the groups by the most recent notification in each group
    sorted_groups = sorted(grouped_notifications.items(), key=lambda x: max(n.created_at for n in x[1]), reverse=True)
    
    return render(request, 'notifications/list.html', {'grouped_notifications': sorted_groups})


@login_required
@require_POST
def handle_donation_action(request):
    notification_id = request.POST.get('notification_id')
    action = request.POST.get('action')
    
    try:
        with transaction.atomic():
            notification = Notification.objects.select_related(
                'donation_request__post__author',
                'donation_request__recipient',
                'donation_request__donor'
            ).get(id=notification_id, user=request.user)
            
            if not notification.donation_request:
                return JsonResponse({'success': False, 'error': 'This notification is not associated with a donation request'})
            
            donation_request = notification.donation_request
            post = donation_request.post
            requester = donation_request.recipient
            
            if action == 'accept':
                post_title = post.title
                new_message = f"Donation request for '{post_title}' accepted"
                
                notification.message = new_message
                notification.is_read = True
                notification.donation_request = None
                notification.save()
                
                Notification.objects.create(
                    user=requester.user,
                    message=f"Your donation request for '{post_title}' has been accepted!",
                )
                
                donation_request.status = 'ACCEPTED'
                donation_request.donor = request.user.profile
                donation_request.save()
                
                post.delete()

                
            elif action == 'decline':
                donation_request.status = 'CANCELLED'
                donation_request.save()
                new_message = f"Donation request for '{post.title}' declined"
                
                notification.message = new_message
                notification.is_read = True
                notification.save()
                
                Notification.objects.create(
                    user=requester.user,
                    message=f"Your donation request for '{post.title}' has been declined.",
                )
                
            else:
                return JsonResponse({'success': False, 'error': 'Invalid action'})
            
            return JsonResponse({
                'success': True, 
                'status': donation_request.status,
                'message': new_message
            })
    except Notification.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Invalid notification'})
    
@login_required
@require_POST
def mark_notification_as_read(request):
    notification_id = request.POST.get('notification_id')
    try:
        notification = Notification.objects.get(id=notification_id, user=request.user)
        notification.is_read = True
        notification.save()
        return JsonResponse({'success': True})
    except Notification.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Invalid notification'})