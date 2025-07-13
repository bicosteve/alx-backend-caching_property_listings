import logging
from django.core.cache import cache
from django_redis import get_redis_connection
from redis.exceptions import RedisError

from .models import Property

logger = logging.getLogger(__name__)


def get_all_properties():
    properties = cache.get("all_properties")
    if not properties:
        properties = list(Property.objects.all().values())
        cache.set("all_properties", properties, timeout=3600)
    return properties


def get_redis_cache_metrics():
    try:
        redis_conn = get_redis_connection("default")
        info = redis_conn.info()

        hits = info.get("keyspace_hits", 0)
        misses = info.get("keyspace_misses", 0)
        total_requests = hits + misses

        hit_ratio = round(hits / total_requests, 4) if total_requests > 0 else 0

        metrics = {
            "keyspace_hits": hits,
            "keyspace_misses": misses,
            "hit_ratio": hit_ratio,
        }

        logger.info(f"REDIS: cache metrics: {metrics}")

        return metrics
    except RedisError as e:
        logger.error("Error")
        return {
            "keyspace_hits": None,
            "keyspace_misses": None,
            "hit_ratio": None,
            "error": str(e),
        }
    except Exception as e:
        logger.exception("Unexpected error while retrieving Redis metrics")
        return {
            "keyspace_hits": None,
            "keyspace_misses": None,
            "hit_ratio": None,
            "error": str(e),
        }
