from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.http import (
    HttpResponseBadRequest
)
from django.db.models import Q
from guardian.core import ObjectPermissionChecker
from guardian.shortcuts import get_objects_for_user
from georepo.models.module import Module
from georepo.models.dataset import Dataset
from georepo.models.dataset_view import DatasetView
from georepo.models.role import GeorepoRole
from georepo.utils.permission import (
    PermissionType,
    downgrade_creator_to_viewer,
    get_modules_to_add_dataset,
    get_dataset_for_user,
    EXTERNAL_READ_VIEW_PERMISSION_LIST
)
from dashboard.api_views.common import (
    IsSuperUser,
    get_privacy_level_labels
)
from dashboard.serializers.permission import (
    DatasetViewPermissionSerializer,
    DatasetPermissionSerializer
)


User = get_user_model()
AVAILABLE_ROLES = ['Admin', 'Creator', 'Viewer']
OBJECT_TYPES = ['module', 'dataset', 'datasetview']


class UserList(APIView):
    permission_classes = [IsSuperUser]

    def get(self, request, *args, **kwargs):
        users = User.objects.select_related(
            'georeporole').all().order_by('id')
        search_text = request.GET.get('search_text', None)
        if search_text:
            users = users.filter(
                Q(first_name__icontains=search_text) |
                Q(last_name__icontains=search_text) |
                Q(username__icontains=search_text) |
                Q(email__icontains=search_text)
            )
        response_data = []
        for user in users:
            if user.is_anonymous or user.username == 'AnonymousUser':
                continue
            role = (
                user.georeporole.type if
                user.georeporole and user.georeporole.type else '-'
            )
            if user.is_superuser:
                role = 'Admin'
            response_data.append({
                'id': user.id,
                'name': f'{user.first_name} {user.last_name}',
                'username': user.username,
                'email': user.email,
                'is_active': 'Yes' if user.is_active else 'No',
                'role': role,
                'joined_date': user.date_joined
            })
        return Response(response_data)


class UserDetail(APIView):
    permission_classes = [IsSuperUser]

    def get_current_role(self, user):
        role = (
            user.georeporole.type if
            user.georeporole and user.georeporole.type else '-'
        )
        if user.is_superuser:
            role = 'Admin'
        return role

    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('id')
        user = get_object_or_404(
            User,
            id=user_id
        )
        return Response({
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'username': user.username,
            'email': user.email,
            'is_active': user.is_active,
            'role': self.get_current_role(user),
            'joined_date': user.date_joined,
            'last_login': user.last_login
        })

    def put(self, request, *args, **kwargs):
        user_id = kwargs.get('id')
        user = get_object_or_404(
            User,
            id=user_id
        )
        if user_id == request.user.id:
            return HttpResponseBadRequest(
                'You are not allowed to change yourself!'
            )
        role = request.data.get('role')
        is_active = request.data.get('is_active')
        if role not in AVAILABLE_ROLES:
            return HttpResponseBadRequest('Invalid role!')
        # if downgrade from CREATOR -> VIEWER,
        # then need to handle existing permissions
        prev_role = self.get_current_role(user)
        should_downgrade = False
        if role == 'Admin':
            # set to super admin + creator
            user.is_superuser = True
            user.is_staff = True
            user.georeporole.type = GeorepoRole.RoleType.CREATOR
        else:
            # remove super admin
            user.is_superuser = False
            user.is_staff = False
            if role == GeorepoRole.RoleType.CREATOR.value:
                user.georeporole.type = GeorepoRole.RoleType.CREATOR
            else:
                user.georeporole.type = GeorepoRole.RoleType.VIEWER
                should_downgrade = (
                    prev_role == GeorepoRole.RoleType.CREATOR.value
                )
        user.is_active = is_active
        user.save()
        if should_downgrade:
            downgrade_creator_to_viewer(user)
        return Response(status=201)

    def post(self, request, *args, **kwargs):
        role = request.data.get('role')
        if role not in AVAILABLE_ROLES:
            return HttpResponseBadRequest('Invalid role!')

        return Response(status=201)


class UserPermissionDetail(APIView):
    permission_classes = [IsSuperUser]

    def get_modules(self, user):
        modules = Module.objects.all()
        modules = get_modules_to_add_dataset(
            user,
            modules,
            use_groups=False
        )
        return [
            {
                'id': module.id,
                'name': module.name,
                'uuid': str(module.uuid),
                'permission': PermissionType.WRITE_PERMISSION.value,
                'privacy_level': 0,
                'type': '',
                'object_type': 'module',
                'privacy_label': ''
            }
            for module in modules
        ]

    def get_datasets(self, user, privacy_labels):
        checker = ObjectPermissionChecker(user)
        dataset = Dataset.objects.all()
        dataset = get_dataset_for_user(
            user,
            dataset,
            use_groups=False
        )
        return DatasetPermissionSerializer(
            dataset,
            many=True,
            context={
                'checker': checker,
                'privacy_labels': privacy_labels,
                'is_group': False
            }
        ).data

    def get_dataset_views(self, user, privacy_labels):
        checker = ObjectPermissionChecker(user)
        views = DatasetView.objects.select_related('dataset').all()
        permission_list = ['view_datasetview']
        permission_list.extend(EXTERNAL_READ_VIEW_PERMISSION_LIST)
        views = get_objects_for_user(
            user,
            permission_list,
            klass=views,
            use_groups=False,
            any_perm=True,
            accept_global_perms=False
        )
        # need to exclude permission from group
        return DatasetViewPermissionSerializer(
            views,
            many=True,
            context={
                'checker': checker,
                'privacy_labels': privacy_labels,
                'is_group': False
            }
        ).data

    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('id')
        user = get_object_or_404(
            User,
            id=user_id
        )
        object_type = kwargs.get('object_type')
        if object_type not in OBJECT_TYPES:
            raise ValidationError(f'Invalid object type: {object_type}')
        results = []
        privacy_labels = get_privacy_level_labels()
        if object_type == 'module':
            results = self.get_modules(user)
        elif object_type == 'dataset':
            results = self.get_datasets(user, privacy_labels)
        elif object_type == 'datasetview':
            results = self.get_dataset_views(user, privacy_labels)
        return Response(results)
