import json
import random
import time

from django.contrib.auth.mixins import UserPassesTestMixin
from django.db.models.expressions import RawSQL
from django.views.generic import TemplateView
from django.conf import settings
from core.models.token_detail import ApiKey
from core.models.preferences import SitePreferences
from azure_auth.handlers import AzureAuthHandler

from georepo.models import Dataset, DatasetView, GeographicalEntity,\
    DatasetViewResource
from georepo.models.dataset_tile_config import (
    DatasetTilingConfig,
    AdminLevelTilingConfig
)
from georepo.models.dataset_view_tile_config import (
    DatasetViewTilingConfig,
    ViewAdminLevelTilingConfig
)


def get_max_zoom_level(dataset_view: DatasetView):
    tiling_configs = DatasetViewTilingConfig.objects.filter(
        dataset_view=dataset_view
    ).order_by('zoom_level')
    if tiling_configs.exists():
        return tiling_configs.last().zoom_level
    tiling_configs = DatasetTilingConfig.objects.filter(
        dataset=dataset_view.dataset
    ).order_by('zoom_level')
    if tiling_configs.exists():
        return tiling_configs.last().zoom_level
    return 8


def get_view_zoom_level(level: int, dataset_view: DatasetView):
    tiling_configs = ViewAdminLevelTilingConfig.objects.filter(
        level=level,
        view_tiling_config__dataset_view=dataset_view
    ).order_by('view_tiling_config__zoom_level')
    if tiling_configs.exists():
        return {
            'min': tiling_configs.first().view_tiling_config.zoom_level,
            'max': tiling_configs.last().view_tiling_config.zoom_level
        }
    entity_conf = AdminLevelTilingConfig.objects.filter(
        level=level,
        dataset_tiling_config__dataset=dataset_view.dataset
    ).order_by('dataset_tiling_config__zoom_level')
    if entity_conf.exists():
        return {
            'min': entity_conf.first().dataset_tiling_config.zoom_level,
            'max': entity_conf.last().dataset_tiling_config.zoom_level
        }
    return {
        'min': 1,
        'max': 8
    }


class LayerTestView(UserPassesTestMixin, TemplateView):
    template_name = 'test_layer.html'

    def test_func(self):
        if not self.request.user.is_authenticated:
            return False
        if settings.USE_AZURE:
            token = AzureAuthHandler(self.request).get_token_from_cache()
            if token is None:
                return False
        else:
            if (
                not ApiKey.objects.filter(
                    token__user=self.request.user).exists()
            ):
                return False
        return True

    def get_context_data(self, **kwargs):
        ctx = super(LayerTestView, self).get_context_data(**kwargs)
        dataset_string = self.request.GET.get('dataset')
        dataset_view = self.request.GET.get('dataset_view')
        dataset_view_resource = self.request.GET.get('dataset_view_resource')
        entity_type = None
        dataset = None
        if (not dataset_string and not dataset_view and
                not dataset_view_resource):
            return ctx

        if dataset_string:
            dataset = Dataset.objects.filter(
                label__iexact=dataset_string
            ).first()
            entity = dataset.geographicalentity_set.filter(
                level=0
            ).first()
            ctx['label'] = dataset.label.replace(' ', '_')
            ctx['dataset'] = dataset
            ctx['vector_tiles_path'] = dataset.vector_tiles_path
            ctx['center'] = json.loads(entity.geometry.centroid.json)
            levels = dataset.geographicalentity_set.values_list(
                'level', flat=True).order_by('-level').distinct()
            # add max zoom
            ctx['max_zoom'] = 8
        else:
            if dataset_view_resource:
                dataset_view_resource = DatasetViewResource.objects.get(
                    id=dataset_view_resource
                )
                ctx['vector_tiles_path'] = (
                    '/layer_tiles/{name}/{{z}}/{{x}}/{{y}}?t={time}'.format(
                        name=dataset_view_resource.uuid,
                        time=int(time.time())
                    )
                )
                dataset_view = dataset_view_resource.dataset_view
                if dataset_view_resource.bbox:
                    ctx['bbox'] = dataset_view_resource.bbox.split(',')
            else:
                dataset_view = DatasetView.objects.get(
                    id=dataset_view
                )
                ctx['vector_tiles_path'] = (
                    '/layer_tiles/{name}/{{z}}/{{x}}/{{y}}?t={time}'.format(
                        name=dataset_view.uuid,
                        time=int(time.time())
                    )
                )
                ctx['bbox'] = dataset_view.bbox.split(',')
            ctx['label'] = dataset_view.name.replace(' ', '_')
            ctx['center'] = ''
            # count levels
            entities = GeographicalEntity.objects.filter(
                dataset=dataset_view.dataset,
                is_approved=True
            )
            # raw_sql to view to select id
            raw_sql = (
                'SELECT id from "{}"'
            ).format(str(dataset_view.uuid))
            entities = entities.filter(
                id__in=RawSQL(raw_sql, [])
            )
            levels = entities.order_by('-level').values_list(
                'level',
                flat=True
            ).distinct()
            # add max zoom
            ctx['max_zoom'] = get_max_zoom_level(dataset_view)

        ctx['layer_tiles_base_url'] = settings.LAYER_TILES_BASE_URL
        if settings.DEBUG:
            ctx['layer_tiles_base_url'] = (
                'http://localhost:8000' if
                not settings.USE_AZURE else 'https://localhost:51102'
            )
        ctx['layers_configs'] = []
        for level in levels:
            color = "#" + (
                ''.join([random.choice('0123456789ABCDEF') for j in range(6)])
            )
            if dataset:
                entity_type = dataset.geographicalentity_set.filter(
                    level=level
                ).first().type
                layers_config_id = entity_type.label.lower()
                source_layer = f'Level-{level}'
            else:
                source_layer = f'Level-{level}'
                layers_config_id = f'{source_layer}_{dataset_view.id}'
            layers_config = {
                'id': layers_config_id,
                'source': ctx['label'],
                'source-layer': source_layer,
                'type': 'line',
                'paint': {
                    'line-color': color,
                    'line-width': 1
                }
            }
            if dataset:
                entity_conf = AdminLevelTilingConfig.objects.filter(
                    level=level,
                    dataset_tiling_config__dataset=dataset
                ).order_by('dataset_tiling_config__zoom_level')
                if entity_conf.exists():
                    layers_config['minzoom'] = (
                        entity_conf.first().dataset_tiling_config.zoom_level
                    )
            else:
                zoom_configs = get_view_zoom_level(level, dataset_view)
                layers_config['minzoom'] = zoom_configs['min']

            ctx['layers_configs'].append(layers_config)
        # add map tiler api key
        ctx['maptiler_api_key'] = (
            SitePreferences.preferences().maptiler_api_key
        )
        return ctx
