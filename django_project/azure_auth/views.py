"""Views for Azure B2C Authentication."""
import logging

from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import resolve_url
from django.http import HttpResponseRedirect

from .handlers import AzureAuthHandler
from .exceptions import InvalidUserError

logger = logging.getLogger(__name__)


def azure_auth_login(request):
    """Redirect user to Azure B2C authentication page."""
    return HttpResponseRedirect(AzureAuthHandler(request).get_auth_uri())


def azure_auth_logout(request):
    """Redirect user to Azure B2C logout page."""
    logout(request)
    return HttpResponseRedirect(AzureAuthHandler(request).get_logout_uri())


def azure_auth_callback(request):
    """Callback/Reply URL that is called from code grant flow."""
    handler = AzureAuthHandler(request)
    login_path = request.build_absolute_uri(
        resolve_url(settings.USER_NO_ACCESS_URL or settings.LOGIN_URL)
    ) + '?no_access=true'
    output = HttpResponseRedirect(
        handler.get_logout_uri(login_path)
    )
    try:
        token = handler.get_token_from_flow()
        user = authenticate(request, token=token)
        if user:
            login(request, user)
            next_uri = handler.get_auth_flow_next_uri()
            redirect_uri = next_uri or settings.LOGIN_REDIRECT_URL
            output = HttpResponseRedirect(redirect_uri)
    except InvalidUserError as e:
        # thrown when non-unicef user does not exist yet
        logger.exception(e)
    except Exception as e:
        logger.exception(e)
    logger.debug("_azure_auth_callback: %s", output)
    return output


def azure_auth_redirect(request):
    """azure_auth_redirect to handle Django success/error messages."""
    output = HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
    try:
        token = AzureAuthHandler(request).get_token_from_flow()
        user = authenticate(request, token=token)
        if user:
            login(request, user)
    except Exception as e:
        logger.exception(e)
    logger.debug("azure_auth_redirect: %s", output)
    return output
