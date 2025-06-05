from django.shortcuts import render

# Create your views here.
from django.http import HttpRequest
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from .models import CustomUser
from django.shortcuts import redirect
from django.contrib.auth import login
from .services import send_sign_in_email, decode_uid, get_user_by_uid
from .forms import CreateUserForm
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.decorators import login_required

def verify_email(request: HttpRequest, uidb64: str, token: str) -> HttpResponse:
    """
    Verify user email after the user clicks on the email link.
    """
    uid = decode_uid(uidb64)
    user = get_user_by_uid(uid) if uid else None

    if user and default_token_generator.check_token(user, token):
        user.has_verified_email = True
        user.save()
        login(request, user)
        return redirect('todo_home')

    print("Email verification failed")
    return redirect('signup')

class SendSignInEmail(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        if not request.user.is_anonymous and request.user.has_verified_email:
            return redirect('todo_home')
        form = CreateUserForm()
        return render(request, 'email_signin.html', {'form': form})

    def post(self, request: HttpRequest) -> HttpResponse:
        data = {
            'username': request.POST['email'],
            'email': request.POST['email'],
            'password': request.POST['email']
        }
        user, created = CustomUser.objects.get_or_create(
            email=data['email'],
            defaults={'username': data['email'], 'password': data['email']}
        )
        return self._send_verification_and_respond(user)

    @staticmethod
    def _send_verification_and_respond(user: CustomUser) -> HttpResponse:
        send_sign_in_email(user)
        message = (
            f"We've sent an email ✉️ to "
            f'<a href=mailto:{user.email}" target="_blank">{user.email}</a> '
            "Please check your email to verify your account"
        )
        return HttpResponse(message)

@login_required(login_url='/loginn')
def todo_home(request: HttpRequest) -> HttpResponse:
    if not request.user.is_anonymous and request.user.has_verified_email:
        return redirect('/todopage')
    else:
        return redirect('signup')   #signup is the name of the url that opens signup page