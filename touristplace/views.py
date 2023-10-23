from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.decorators.http import require_POST
from django.http import JsonResponse,HttpResponse
from .models import State,TouristPlace,TouristPlaceImage,Rev
from .forms import RevForm
from django.template.loader import render_to_string
from django.views.generic import TemplateView
from allauth.account.views import SignupView,LoginView
from .forms import CustomSignupForm
from django.db.models import Avg
from .forms import SearchForm

def account_settings(request):
   
    user = request.user
    context = {
        'user': user
    }
    return render(request, 'account_settings.html', context)


def home(request):
    states = State.objects.all()
    context = {
        'states': states,
    }
    return render(request, 'home.html', context)
@login_required
def place_details(request, place_id):
    place = get_object_or_404(TouristPlace, pk=place_id)
    tourist_place = TouristPlace.objects.get(pk=place_id)
    default_image = TouristPlaceImage.objects.filter(touristplace=place, default_image=True).first()
    place_image_url = default_image.image_url if default_image else None

    # Retrieve reviews associated with the tourist place
    reviews = Rev.objects.filter(tourist_place=place)

    return render(request, 'place_details.html', {'place': place, 'place_image_url': place_image_url, 'reviews': reviews})
@login_required
def state_detail(request, state_id):
    state = get_object_or_404(State, pk=state_id)
    tourist_places = TouristPlace.objects.filter(state=state)

    # Calculate average ratings for each tourist place
    for place in tourist_places:
        place.average_rating = Rev.objects.filter(tourist_place=place).aggregate(avg_rating=Avg('rating'))['avg_rating']

    context = {
        'state': state,
        'tourist_places': tourist_places,
    }

    return render(request, 'state_detail.html', context)
def get_large_image(request, image_id):
    try:
        image = TouristPlaceImage.objects.get(id=image_id)
        return JsonResponse({'image_url': image.image.url})
    except TouristPlaceImage.DoesNotExist:
        return JsonResponse({'error': 'Image not found'}, status=404)


class PackageListView(TemplateView):
    template_name = 'package_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Retrieve distinct states
        states = Packages.objects.values('state__id', 'state__name').distinct()
        
        context['states'] = states
        return context
def signup(request):
    return SignupView.as_view(form_class=CustomSignupForm)(request)

@login_required
def add_review(request, tourist_place_id):
    tourist_place = get_object_or_404(TouristPlace, pk=tourist_place_id)

    if request.method == 'POST':
        form = RevForm(request.POST)

        if form.is_valid():
            review = form.save(commit=False)
            review.tourist_place = tourist_place
            review.user = request.user

            # Save the rating
            review.rating = form.cleaned_data['rating']

            review.save()

            return redirect('tourist_place_ratings', tourist_place_id=tourist_place_id)
    else:
        form = RevForm()

        context = {
        'tourist_place': tourist_place,  # Make sure 'tourist_place' is included in the context
        'form': form,
    }
    return render(request, 'add_review.html', context)



@login_required
def edit_review(request, review_id):
    review = get_object_or_404(Rev, pk=review_id)

    if request.method == 'POST':
        form = RevForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('tourist_place_ratings', tourist_place_id=review.tourist_place.id)
    else:
        # Initialize the form with the existing review data
        form = RevForm(instance=review)

    return render(request, 'edit_review.html', {'form': form, 'review': review})

@login_required
def delete_review(request, review_id):
    review = get_object_or_404(Rev, pk=review_id)
    tourist_place_id = review.tourist_place.id
    review.delete()
    return redirect('tourist_place_ratings', tourist_place_id=tourist_place_id)

@login_required
def view_reviews(request, tourist_place_id):
    tourist_place = TouristPlace.objects.get(id=tourist_place_id)  # Fetch the tourist place
    reviews = Rev.objects.filter(tourist_place=tourist_place).order_by('-created_at')  # Fetch reviews for this place

    # Calculate reversed_rating for each review such that 1 maps to the lowest rating and 5 to the highest
    for review in reviews:
        review.reversed_rating = 5 - (review.rating - 1)
        print(f"Review ID: {review.id}, Reversed Rating: {review.reversed_rating}, Original Rating: {review.rating}")

    return render(request, 'tourist_place_ratings.html', {'tourist_place': tourist_place, 'reviews': reviews, 'current_user': request.user})

def search_view(request):
    if 'q' in request.GET:
        query = request.GET['q']
        # Update the search logic to use a valid field (e.g., 'name')
        results = TouristPlace.objects.filter(name__icontains=query)

        context = {
            'query': query,
            'results': results,
        }
        return render(request, 'search_results.html', context)
