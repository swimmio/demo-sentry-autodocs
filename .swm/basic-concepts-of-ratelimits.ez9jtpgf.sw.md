---
title: Basic concepts of Ratelimits
---
# Ratelimits in Sentry

Ratelimits in Sentry are implemented to control the rate at which users and organizations can perform certain actions, preventing abuse and ensuring fair usage of resources. The system uses configurations like `DEFAULT_CONFIG` in `src/sentry/ratelimits/utils.py` which specifies limits such as the number of invites a user or organization can send per day. These configurations help manage the load on Sentry's infrastructure and maintain service reliability. Ratelimits are enforced through various checks and limits set on endpoints and operations within the Sentry application.

<SwmSnippet path="/src/sentry/ratelimits/config.py" line="72">

---

# Rate Limit Configuration

The `RateLimitConfig` class in `config.py` defines the structure for rate limit configurations, which includes methods to check for custom limits and retrieve rate limits based on HTTP method and category. This configuration is crucial for determining how rate limits are applied to different endpoints.

```python
@dataclass(frozen=True)
class RateLimitConfig:
    group: str = field(default="default")
    limit_overrides: RateLimitOverrideDict | _sentinel = field(default=_sentinel())

    def has_custom_limit(self) -> bool:
        return not isinstance(self.limit_overrides, _sentinel)

    def get_rate_limit(self, http_method: str, category: RateLimitCategory) -> RateLimit:
        if isinstance(self.limit_overrides, _sentinel):
            return get_default_rate_limits_for_group(self.group, category)
        override_rate_limit = self.limit_overrides.get(http_method, {}).get(category, None)
        if isinstance(override_rate_limit, RateLimit):
            return override_rate_limit
        return get_default_rate_limits_for_group(self.group, category)

    @classmethod
    def from_rate_limit_override_dict(
        cls, rate_limit_override_dict: RateLimitConfig | RateLimitOverrideDict
    ) -> RateLimitConfig:
        if isinstance(rate_limit_override_dict, cls):
```

---

</SwmSnippet>

<SwmSnippet path="/src/sentry/ratelimits/utils.py" line="50">

---

# Rate Limit Key Generation

The function `get_rate_limit_key` in `utils.py` is essential for generating a unique key for each rate limit scenario. This key is used to track and limit requests based on the endpoint function, request details, and rate limit group. It handles various conditions to ensure accurate rate limiting, such as checking user authentication and request path.

```python
def get_rate_limit_key(
    view_func: EndpointFunction,
    request: HttpRequest,
    rate_limit_group: str,
    rate_limit_config: RateLimitConfig | None = None,
) -> str | None:
    """Construct a consistent global rate limit key using the arguments provided"""
    from sentry.models.apitoken import ApiToken, is_api_token_auth

    if not hasattr(view_func, "view_class") or request.path_info.startswith(
        settings.ANONYMOUS_STATIC_PREFIXES
    ):
        return None

    view = view_func.view_class.__name__
    http_method = request.method

    # This avoids touching user session, which means we avoid
    # setting `Vary: Cookie` as a response header which will
    # break HTTP caching entirely.
    if request.path_info.startswith(settings.ANONYMOUS_STATIC_PREFIXES):
```

---

</SwmSnippet>

&nbsp;

*This is an auto-generated document by Swimm AI 🌊 and has not yet been verified by a human*

<SwmMeta version="3.0.0" repo-id="Z2l0aHViJTNBJTNBc2VudHJ5JTNBJTNBZ2V0c2VudHJ5" repo-name="sentry"><sup>Powered by [Swimm](/)</sup></SwmMeta>
