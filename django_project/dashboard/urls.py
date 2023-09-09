from django.urls import re_path, path, include

from dashboard.api_views.reviews import (
    ReadyToReview,
    ReviewList,
    ReviewFilterValue,
    ApproveRevision,
    RejectRevision,
    BatchReviewAPI,
    PendingBatchReviewUploads
)
from dashboard.views.dashboard import DashboardView
from dashboard.views.uploader import UploaderView
from dashboard.views.signup import SignUpView
from dashboard.api_views.layer_upload import (
    LayerUploadView,
    LayersProcessView,
    LayerProcessStatusView,
    LayerRemoveView,
    LayerUploadList,
    UpdateLayerUpload,
    LayerFileAttributes,
    LayerFileEntityTypeList,
    LayerFileChangeLevel,
    LayerFileDownload
)
from dashboard.api_views.upload_session import (
    AddUploadSession,
    UploadSessionList,
    UploadSessionFilterValue,
    UploadSessionDetail,
    UploadSessionSummary,
    UploadSessionUpdateStep, CanAddUpload, UpdateUploadSession,
    DeleteUploadSession,
    ResetUploadSession
)
from dashboard.api_views.entity_upload_status import (
    EntityUploadStatusDetail,
    EntityUploadStatusList,
    EntityUploadLevel1List,
    OverlapsEntityUploadList,
    OverlapsEntityUploadDetail
)
from dashboard.api_views.validate import ValidateUploadSession, \
    LayerUploadPreprocess
from dashboard.api_views.users import (
    UserList,
    UserDetail,
    UserPermissionDetail,
    TokenDetail
)
from dashboard.api_views.groups import (
    GroupList,
    GroupDetail,
    GroupPermissionDetail,
    ManageUserGroup
)
from dashboard.api_views.layer_config import (
    SaveLayerConfig,
    LayerConfigList,
    LoadLayerConfig
)
from dashboard.api_views.id_type import (
    IdTypeList,
    AddIdType
)
from dashboard.api_views.boundary_comparison import (
    BoundaryComparisonSummary,
    BoundaryComparisonMatchTable,
    BoundaryComparisonGeometry,
    RematchClosestEntities,
    CompareBoundary,
    ConfirmRematchBoundary,
    SwapEntityConcept,
    BoundaryLinesMatchTable,
    BoundaryLinesGeometry
)
from dashboard.api_views.dataset import (
    DashboardDatasetFilterValue,
    DashboardDatasetFilter,
    DasboardDatasetEntityList,
    DatasetEntityDetail,
    DatasetMVTTiles, DeleteDataset,
    GroupDatasetList, DatasetEntityList,
    CreateDataset, DatasetDetail,
    DatasetStyle, UpdateDatasetStyle,
    CheckDatasetShortCode, UpdateDataset,
    DatasetAdminLevelNames, DatasetBoundaryTypes,
    DatasetMVTTilesView, DatasetMVTTilesPreviewTilingConfig
)
from dashboard.api_views.notification import NotificationList
from dashboard.api_views.language import LanguageList, FetchLanguages
from dashboard.api_views.module import ModuleDashboard
from dashboard.api_views.entity import (
    EntityRevisionList,
    EntityByConceptUCode,
    EntityEdit
)

from dashboard.api_views.views import (
    CreateNewView, ViewList, DeleteView, ViewDetail,
    UpdateView, QueryViewCheck, SQLColumnsTablesList,
    QueryViewPreview, GetViewTags,
    DownloadView, ViewFilterValue
)
from dashboard.api_views.tiling_config import (
    FetchDatasetTilingConfig, UpdateDatasetTilingConfig,
    FetchDatasetViewTilingConfig, UpdateDatasetViewTilingConfig,
    CreateTemporaryTilingConfig, TemporaryTilingConfigAPIView,
    ConfirmTemporaryTilingConfigAPIView,
    TilingConfigCheckStatus
)
from dashboard.api_views.permission import (
    PermissionActorList,
    GetPermissionUserAndRoles,
    CanCreateDataset,
    GetAvailablePermissionForObject,
    GetAvailableObjectForActor,
    FetchPrivacyLevelLabels
)
from dashboard.api_views.access_request import (
    AccessRequestList,
    AccessRequestDetail,
    SubmitPermissionAccessRequest
)
from dashboard.api_views.media import (
    ErrorReportAPIView
)

urlpatterns = [
    path('tinymce/', include('tinymce.urls')),
    re_path(
        r'api/dataset-group/list/?$',
        GroupDatasetList.as_view(),
        name='dataset-group-list'),
    re_path(
        r'api/dataset-entity/list/?$',
        DatasetEntityList.as_view(),
        name='dataset-entity-list'),
    re_path(
        r'api/entity-revisions/?$',
        EntityRevisionList.as_view(),
        name='entity-revisions'
    ),
    re_path(
        r'api/dashboard-entity-by-cucode/detail/'
        r'(?P<concept_ucode>#[^/]+)/?$',
        EntityByConceptUCode.as_view(),
        name='entity-by-concept-ucode'
    ),
    re_path(
        r'api/entity/edit/'
        r'(?P<entity_id>\d+)/?$',
        EntityEdit.as_view(),
        name='entity-edit'
    ),
    re_path(
        r'api/language/list/?$',
        LanguageList.as_view(),
        name='language-list'
    ),
    re_path(
        r'api/module/detail/(?P<uuid>[\da-f-]+)/?$',
        ModuleDashboard.as_view(),
        name='module-detail-update'
    ),
    re_path(
        r'api/module-list/?$',
        ModuleDashboard.as_view(),
        name='module-list'
    ),
    re_path(
        r'api/check-dataset-short-code/?$',
        CheckDatasetShortCode.as_view(),
        name='check-dataset-short-code'
    ),
    re_path(
        r'api/check-user-write-permission/?$',
        CanCreateDataset.as_view(),
        name='check-user-write-permission'
    ),
    re_path(
        r'api/create-dataset/?$',
        CreateDataset.as_view(),
        name='create-dataset'
    ),
    re_path(
        r'api/update-dataset/(?P<uuid>[\da-f-]+)/?$',
        UpdateDataset.as_view(),
        name='update-dataset'
    ),
    re_path(
        r'api/dataset-detail/(?P<id>[\da-f-]+)/?$',
        DatasetDetail.as_view(),
        name='dataset-detail'
    ),
    re_path(
        r'api/add-upload-session/(?P<id>\d+)/?$',
        AddUploadSession.as_view(),
        name='add-upload-session'
    ),
    re_path(
        r'api/update-upload-session/?$',
        UpdateUploadSession.as_view(),
        name='update-upload-session'
    ),
    re_path(
        r'api/delete-upload-session/(?P<id>\d+)/?$',
        DeleteUploadSession.as_view(),
        name='delete-upload-session'
    ),
    re_path(
        r'api/reset-upload-session/(?P<id>\d+)/(?P<step>\d+)/?$',
        ResetUploadSession.as_view(),
        name='reset-upload-session'
    ),
    re_path(
        r'api/upload-sessions/?$',
        UploadSessionList.as_view(),
        name='upload-session-list'
    ),
    re_path(
        r'api/upload-session-filter/values/(?P<criteria>\w+)/?$',
        UploadSessionFilterValue.as_view(),
        name='upload-session-filter-value'
    ),
    re_path(
        r'api/upload-session/(?P<id>\d+)/?$',
        UploadSessionDetail.as_view(),
        name='upload-session-detail'
    ),
    re_path(
        r'api/upload-session-update-step/?$',
        UploadSessionUpdateStep.as_view(),
        name='upload-session-update-step'
    ),
    re_path(
        r'api/upload-session-summary/(?P<pk>\d+)/?$',
        UploadSessionSummary.as_view(),
        name='upload-session-summary'
    ),
    re_path(
        r'upload/?$',
        UploaderView.as_view(),
        name='upload'
    ),
    re_path(
        r'api/layer-upload/?$',
        LayerUploadView.as_view(),
        name='layer-upload'
    ),
    re_path(
        r'api/layer-remove/?$',
        LayerRemoveView.as_view(),
        name='layer-remove'
    ),
    re_path(
        r'api/layers-process/?$',
        LayersProcessView.as_view(),
        name='layers-process'
    ),
    re_path(
        r'api/layers-process-status/?$',
        LayerProcessStatusView.as_view(),
        name='layers-process-status'
    ),
    re_path(
        r'api/layer-upload-list/?$',
        LayerUploadList.as_view(),
        name='layer-upload-list'
    ),
    re_path(
        r'api/entity-upload-status-detail/(?P<id>\d+)/?$',
        EntityUploadStatusDetail.as_view(),
        name='entity-upload-status-detail'
    ),
    re_path(
        r'api/entity-upload-error-download/(?P<upload_id>\d+)/?$',
        ErrorReportAPIView.as_view(),
        name='entity-upload-error-download'
    ),
    re_path(
        r'api/entity-upload-status-list/?$',
        EntityUploadStatusList.as_view(),
        name='entity-upload-status-list'
    ),
    re_path(
        r'api/entity-upload-level1-list/?$',
        EntityUploadLevel1List.as_view(),
        name='entity-upload-level1-list'
    ),
    re_path(
        r'api/update-layer-upload/?$',
        UpdateLayerUpload.as_view(),
        name='update-layer-upload'
    ),
    re_path(
        r'api/validate-upload-session/?$',
        ValidateUploadSession.as_view(),
        name='validate-upload-session'
    ),
    re_path(
        r'api/layer-upload-preprocess/?$',
        LayerUploadPreprocess.as_view(),
        name='layer-upload-preprocess'
    ),
    re_path(
        r'api/layer-attributes/?$',
        LayerFileAttributes.as_view(),
        name='layer-attributes'
    ),
    re_path(r'api/can-add-upload/(?P<id>\d+)/?$',
            CanAddUpload.as_view(),
            name='can-add-upload'),
    re_path(r'api/user-list/?$',
            UserList.as_view(),
            name='user-list'),
    re_path(r'api/user/(?P<id>\d+)/?$',
            UserDetail.as_view(),
            name='user-detail'),
    re_path(r'api/token/(?P<id>\d+)/?$',
            TokenDetail.as_view(),
            name='token-detail'),
    re_path(r'api/user/?$',
            UserDetail.as_view(),
            name='user-create'),
    re_path(r'api/user/permission/'
            r'(?P<object_type>(module|dataset|datasetview))/'
            r'(?P<id>\d+)/?$',
            UserPermissionDetail.as_view(),
            name='user-permission-detail'),
    re_path(r'api/group-list/?$',
            GroupList.as_view(),
            name='group-list'),
    re_path(r'api/group/(?P<id>\d+)/user/list/?$',
            ManageUserGroup.as_view(),
            name='manage-group-members'),
    re_path(r'api/group/(?P<id>\d+)/user/(?P<user_id>\d+)/manage/?$',
            ManageUserGroup.as_view(),
            name='manage-user-group'),
    re_path(r'api/group/(?P<id>\d+)/?$',
            GroupDetail.as_view(),
            name='group-detail'),
    re_path(r'api/group/permission/'
            r'(?P<object_type>(module|dataset|datasetview))/'
            r'(?P<id>\d+)/?$',
            GroupPermissionDetail.as_view(),
            name='group-permission-detail'),
    re_path(r'api/layer-config/save/?$',
            SaveLayerConfig.as_view(),
            name='save-layer-config'),
    re_path(r'api/layer-config/list/?$',
            LayerConfigList.as_view(),
            name='layer-config-list'),
    re_path(r'api/layer-config/load/?$',
            LoadLayerConfig.as_view(),
            name='load-layer-config'),
    re_path(r'api/id-type/list/?$',
            IdTypeList.as_view(),
            name='id-type-list'),
    re_path(r'api/id-type/add/?$',
            AddIdType.as_view(),
            name='add-id-type'),
    re_path(r'api/id-type/list/?$',
            IdTypeList.as_view(),
            name='id-type-list'),
    re_path(
        r'api/ready-to-review/?$',
        ReadyToReview.as_view(),
        name='ready-to-review'
    ),
    re_path(
        r'api/review-list/?$',
        ReviewList.as_view(),
        name='review-list'
    ),
    re_path(
        r'^api/review-filter/values/'
        r'(?P<criteria>\w+)/?$',
        ReviewFilterValue.as_view(),
        name='review-filter-value'
    ),
    re_path(
        r'api/boundary-comparison-summary/(?P<entity_upload_id>\d+)/?$',
        BoundaryComparisonSummary.as_view(),
        name='boundary-comparison-summary'
    ),
    re_path(
        r'api/boundary-comparison-match-table/'
        r'(?P<entity_upload_id>\d+)/(?P<level>\d+)/?$',
        BoundaryComparisonMatchTable.as_view(),
        name='boundary-comparison-match-table'
    ),
    re_path(
        r'api/boundary-comparison-geometry/'
        r'(?P<boundary_comparison_id>\d+)',
        BoundaryComparisonGeometry.as_view(),
        name='boundary-comparison-geometry'
    ),
    re_path(
        r'api/boundary-comparison-closest/'
        r'(?P<boundary_comparison_id>\d+)/?',
        RematchClosestEntities.as_view(),
        name='boundary-comparison-closest'
    ),
    re_path(
        r'api/boundary-compare-entities/'
        r'(?P<entity_upload_id>\d+)/'
        r'(?P<boundary_comparison_id>\d+)/(?P<source_id>\d+)/?',
        CompareBoundary.as_view(),
        name='boundary-compare-entities'
    ),
    re_path(
        r'api/boundary-comparison-rematch/'
        r'(?P<boundary_comparison_id>\d+)/?',
        ConfirmRematchBoundary.as_view(),
        name='boundary-comparison-rematch'
    ),
    re_path(
        r'api/boundary-swap-entity-concept/?',
        SwapEntityConcept.as_view(),
        name='boundary-swap-entity-concept'
    ),
    re_path(
        r'api/boundary-lines-match-table/'
        r'(?P<entity_upload_id>\d+)/(?P<type>[^/]+)/?$',
        BoundaryLinesMatchTable.as_view(),
        name='boundary-lines-match-table'
    ),
    re_path(
        r'api/boundary-lines-geometry/'
        r'(?P<id>\d+)/?$',
        BoundaryLinesGeometry.as_view(),
        name='boundary-lines-geometry'
    ),
    re_path(
        r'api/approve-revision/(?P<uuid>[\da-f-]+)/?$',
        ApproveRevision.as_view(),
        name='approve-revision'
    ),
    re_path(
        r'api/reject-revision/(?P<uuid>[\da-f-]+)/?$',
        RejectRevision.as_view(),
        name='reject-revision'
    ),
    re_path(
        r'api/review/batch/identifier/(?P<review_id>[\d]+)/?$',
        BatchReviewAPI.as_view(),
        name='batch-review-status'
    ),
    re_path(
        r'api/review/batch/uploads/?$',
        PendingBatchReviewUploads.as_view(),
        name='pending-uploads-batch-review'
    ),
    re_path(
        r'api/review/batch/?$',
        BatchReviewAPI.as_view(),
        name='batch-review-submit'
    ),
    re_path(
        r'api/layer-file-change-level/?$',
        LayerFileChangeLevel.as_view(),
        name='layer-file-change-level'
    ),
    re_path(
        r'api/layer-file-download/?$',
        LayerFileDownload.as_view(),
        name='layer-file-download'
    ),
    re_path(r'^api/entity-type/list/?$',
            LayerFileEntityTypeList.as_view(),
            name='layer-entity-type-list'),
    re_path(r'^api/dashboard-dataset-filter/values/'
            r'(?P<id>\d+)/(?P<criteria>\w+)/?$',
            DashboardDatasetFilterValue.as_view(),
            name='dashboard-dataset-filter-values'),
    re_path(r'^api/dashboard-dataset-filter/'
            r'(?P<id>\d+)/?$',
            DashboardDatasetFilter.as_view(),
            name='dashboard-dataset-filter'),
    re_path(r'^api/dashboard-dataset/detail/'
            r'(?P<id>\d+)/entity/(?P<entity_id>\d+)/?$',
            DatasetEntityDetail.as_view(),
            name='dashboard-dataset-detail'),
    re_path(r'^api/dashboard-dataset/list/'
            r'(?P<id>\d+)/(?P<session>[\da-f-]+)/?$',
            DasboardDatasetEntityList.as_view(),
            name='dashboard-dataset'),
    re_path(r'^api/notification/list/?$',
            NotificationList.as_view(),
            name='notification-list'),
    re_path(r'api/dashboard-tiles/maps/tile-preview/'
            r'dataset/(?P<dataset>[\da-f-]+)/'
            r'(?P<session>[\da-f-]+)/'
            r'(?P<z>\d+)/(?P<x>\d+)/(?P<y>\d+)/?$',
            DatasetMVTTilesPreviewTilingConfig.as_view(),
            name='dashboard-tiles-preview-tiling-config'),
    re_path(r'api/dashboard-tiles/maps/tile-preview/'
            r'view/(?P<dataset_view>[\da-f-]+)/'
            r'(?P<session>[\da-f-]+)/'
            r'(?P<z>\d+)/(?P<x>\d+)/(?P<y>\d+)/?$',
            DatasetMVTTilesPreviewTilingConfig.as_view(),
            name='dashboard-tiles-preview-tiling-config-view'),
    re_path(r'api/dashboard-tiles/maps/view/(?P<dataset_view>[\da-f-]+)/'
            r'(?P<session>[\da-f-]+)/'
            r'(?P<z>\d+)/(?P<x>\d+)/(?P<y>\d+)/?$',
            DatasetMVTTilesView.as_view(),
            name='dashboard-tiles-view'),
    re_path(r'api/dashboard-tiles/maps/review/(?P<dataset>[\da-f-]+)/'
            r'(?P<level>\d+)/(?P<revised_entity>[\da-f-]+)/'
            r'(?P<z>\d+)/(?P<x>\d+)/(?P<y>\d+)/?$',
            DatasetMVTTiles.as_view(),
            name='dashboard-tiles-review'),
    re_path(r'api/dashboard-tiles/maps/review/(?P<dataset>[\da-f-]+)/'
            r'revision/(?P<revision>\d+)/'
            r'boundary_type/(?P<boundary_type>[^/]+)/'
            r'(?P<z>\d+)/(?P<x>\d+)/(?P<y>\d+)/?$',
            DatasetMVTTiles.as_view(),
            name='dashboard-tiles-review-boundary-lines'),
    re_path(r'api/dashboard-tiles/maps/(?P<session>(dataset_)?[\da-f-]+)/'
            r'(?P<z>\d+)/(?P<x>\d+)/(?P<y>\d+)/?$',
            DatasetMVTTiles.as_view(),
            name='dashboard-tiles'),
    re_path(r'api/create-new-view/?$',
            CreateNewView.as_view(),
            name='create-new-view'),
    re_path(r'api/view-list/?$',
            ViewList.as_view(),
            name='view-list'),
    re_path(r'^api/view-filter/values/'
            r'(?P<criteria>\w+)/?$',
            ViewFilterValue.as_view(),
            name='view-filter-value'),
    re_path(r'api/tag-list/?$',
            GetViewTags.as_view(),
            name='get-tag-list'),
    re_path(r'api/columns-tables-list/?$',
            SQLColumnsTablesList.as_view(),
            name='columns-tables-list'),
    re_path(r'api/view-detail/(?P<id>[\da-f-]+)?$',
            ViewDetail.as_view(),
            name='view-detail'),
    re_path(r'api/view-download/(?P<id>[\da-f-]+)/?$',
            DownloadView.as_view(),
            name='view-download'),
    re_path(r'api/delete-view/(?P<id>[\da-f-]+)?$',
            DeleteView.as_view(),
            name='delete-view'),
    re_path(r'api/update-view/(?P<id>[\da-f-]+)?$',
            UpdateView.as_view(),
            name='update-view'),
    re_path(r'api/query-view-check/?$',
            QueryViewCheck.as_view(),
            name='query-view-check'),
    re_path(r'api/query-view-preview/?$',
            QueryViewPreview.as_view(),
            name='query-view-preview'),
    re_path(r'api/delete-dataset/(?P<id>[\da-f-]+)?$',
            DeleteDataset.as_view(),
            name='delete-dataset'),
    re_path(r'api/dataset-style/review/(?P<dataset>[\da-f-]+)/'
            r'(?P<level>\d+)/(?P<revised_entity>[\da-f-]+)/?$',
            DatasetStyle.as_view(),
            name='get-dataset-style-review'),
    re_path(r'api/dataset-style/review/(?P<dataset>[\da-f-]+)/'
            r'revision/(?P<revision>\d+)/boundary_type/'
            r'(?P<boundary_type>[^/]+)/?$',
            DatasetStyle.as_view(),
            name='get-dataset-style-review'),
    re_path(r'api/dataset-style/view/(?P<dataset_view>[\da-f-]+)/?$',
            DatasetStyle.as_view(),
            name='get-dataset-style-view'),
    re_path(r'api/dataset-style/dataset/(?P<dataset>[\da-f-]+)/?$',
            DatasetStyle.as_view(),
            name='get-dataset-style'),
    re_path(r'api/update-dataset-style/(?P<uuid>[\da-f-]+)/'
            r'(?P<source_name>[\w-]+)/?$',
            UpdateDatasetStyle.as_view(),
            name='update-dataset-style'),
    re_path(r'api/fetch-languages/',
            FetchLanguages.as_view(),
            name='fetch-languages'),
    re_path(r'api/tiling-configs/temporary/create/?$',
            CreateTemporaryTilingConfig.as_view(),
            name='tiling-configs-temp-create'),
    re_path(r'api/tiling-configs/temporary/detail/(?P<session>[\da-f-]+)/?$',
            TemporaryTilingConfigAPIView.as_view(),
            name='tiling-configs-temp-detail'),
    re_path(r'api/tiling-configs/temporary/apply/?$',
            ConfirmTemporaryTilingConfigAPIView.as_view(),
            name='tiling-configs-temp-apply'),
    re_path(r'api/tiling-configs/status/'
            r'(?P<object_type>(dataset|datasetview))/'
            r'(?P<uuid>[\da-f-]+)/?$',
            TilingConfigCheckStatus.as_view(),
            name='tiling-configs-status'),
    re_path(r'api/fetch-tiling-configs/dataset/(?P<uuid>[\da-f-]+)/?$',
            FetchDatasetTilingConfig.as_view(),
            name='fetch-tiling-configs'),
    re_path(r'api/update-tiling-configs/dataset/(?P<uuid>[\da-f-]+)/?$',
            UpdateDatasetTilingConfig.as_view(),
            name='update-tiling-configs'),
    re_path(r'api/fetch-tiling-configs/view/(?P<view>[\da-f-]+)/?$',
            FetchDatasetViewTilingConfig.as_view(),
            name='fetch-view-tiling-configs'),
    re_path(r'api/update-tiling-configs/view/(?P<view>[\da-f-]+)/?$',
            UpdateDatasetViewTilingConfig.as_view(),
            name='update-view-tiling-configs'),
    re_path(r'api/entity-upload-status/fetch-overlaps/'
            r'(?P<upload_id>\d+)/?$',
            OverlapsEntityUploadList.as_view(),
            name='fetch-entity-overlaps'),
    re_path(r'api/entity-upload-status/fetch-overlaps-detail/'
            r'(?P<entity_id_1>\d+)/(?P<entity_id_2>\d+)/?$',
            OverlapsEntityUploadDetail.as_view(),
            name='fetch-entity-overlaps-detail'),
    re_path(r'api/dataset-admin-level-names/(?P<uuid>[\da-f-]+)/?$',
            DatasetAdminLevelNames.as_view(),
            name='dataset-admin-level-names'),
    re_path(r'api/boundary-lines/boundary-types/(?P<uuid>[\da-f-]+)/?$',
            DatasetBoundaryTypes.as_view(),
            name='dataset-boundary-types'),
    re_path(r'api/permission/list/'
            r'(?P<object_type>(module|dataset|datasetview))/'
            r'(?P<uuid>[\da-f-]+)/identifier/(?P<id>[\da-f-]+)/?$',
            PermissionActorList.as_view(),
            name='delete-permission-list'),
    re_path(r'api/permission/list/'
            r'(?P<object_type>(module|dataset|datasetview))/'
            r'(?P<uuid>[\da-f-]+)/?$',
            PermissionActorList.as_view(),
            name='fetch-permission-list'),
    re_path(r'api/permission/actors/'
            r'(?P<object_type>(module|dataset|datasetview))/'
            r'(?P<uuid>[\da-f-]+)/?$',
            GetPermissionUserAndRoles.as_view(),
            name='fetch-actor-and-role-list'),
    re_path(r'api/permission/objects/'
            r'(?P<object_type>(module|dataset|datasetview))/'
            r'(?P<actor_id>[\d]+)/?$',
            GetAvailableObjectForActor.as_view(),
            name='fetch-available-objects-for-user'),
    re_path(r'api/permission/privacy-levels/?$',
            FetchPrivacyLevelLabels.as_view(),
            name='fetch-privacy-levels'),
    re_path(r'api/permission/object/'
            r'(?P<object_type>(module|dataset|datasetview))/'
            r'(?P<uuid>[\da-f-]+)/?$',
            GetAvailablePermissionForObject.as_view(),
            name='fetch-permission-list-for-object'),
    re_path(r'api/access/request/'
            r'(?P<type>(user|permission))/'
            r'list/?$',
            AccessRequestList.as_view(),
            name='fetch-access-request-list'),
    re_path(r'api/access/request/detail/'
            r'(?P<request_id>[\d]+)/?$',
            AccessRequestDetail.as_view(),
            name='fetch-access-request-detail'),
    re_path(r'api/access/request/permission/submit/?$',
            SubmitPermissionAccessRequest.as_view(),
            name='create-permission-access-request'),
    re_path(r'sign-up/$',
            SignUpView.as_view(),
            name='signup-view'),
    re_path(r'', DashboardView.as_view(), name='dashboard-view'),
]
