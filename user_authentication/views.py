from django.shortcuts import render, get_object_or_404
# Same app importing
from user_authentication.models import Profile


# Logic for manual input and output using URL

# Logic function: 1
def input(request):
    """Input Authenticated User's info"""

    # Returns all instances with 'name and id' into server output
    saved_data = Profile.objects.values_list('id', 'name').distinct()
    print(saved_data)

    # Verify 'saved user' by 'username'
    if request.method == 'POST':
        username = request.POST['username']
        print(username)

        # Mapping with saved data
        profile = get_object_or_404(Profile, username=username)

        # Template
        template = 'user_authentication/single_user.html'
        # Context
        context = {'profile': profile}

        # Renders template with data
        return render(request, template, context)

    # Returns 'input page template' if no submission
    template = 'user_authentication/input.html'

    return render(request, template)


# Logic function: 2
def single_user(request, username=None):
    """Returns single user's info"""

    # Querying object by 'username' from Profile table
    profile = get_object_or_404(Profile, username=username)

    # Template
    template = 'user_authentication/single_user.html'
    # Context
    context = {'profile': profile}

    # Renders template with data
    return render(request, template, context)


# Logic function: 3
def all_users(request):
    """Returns all user's info"""

    # Querying all saved objects from Profile table
    user_data_all = Profile.objects.all().order_by('-id')

    # Template
    template = 'user_authentication/all_users.html'
    # Context
    context = {'user_data_all': user_data_all}

    # Renders template with data
    return render(request, template, context)




