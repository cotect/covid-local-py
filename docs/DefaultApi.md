# covid_local.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all**](DefaultApi.md#get_all) | **GET** /all | Get all items for a place
[**get_health_departments**](DefaultApi.md#get_health_departments) | **GET** /health_departments | Get responsible health departments for a place
[**get_hotlines**](DefaultApi.md#get_hotlines) | **GET** /hotlines | Get hotlines for a place
[**get_test_sites**](DefaultApi.md#get_test_sites) | **GET** /test_sites | Get nearby test sites for a place (sorted by distance to place)
[**get_websites**](DefaultApi.md#get_websites) | **GET** /websites | Get websites for a place
[**search_places**](DefaultApi.md#search_places) | **GET** /places | Search for places via free-form query
[**test**](DefaultApi.md#test) | **GET** /test | Shows all entries for Berlin Mitte (redirects to /all endpoint)


# **get_all**
> ResultsList get_all(place_name=place_name, geonames_id=geonames_id, max_distance=max_distance, limit=limit)

Get all items for a place

### Example

```python
from __future__ import print_function
import time
import covid_local
from covid_local.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = covid_local.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with covid_local.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = covid_local.DefaultApi(api_client)
    place_name = 'place_name_example' # str | The name of the place, e.g. a city, neighborhood, state (either place_name or geonames_id must be provided) (optional)
geonames_id = 56 # int | The geonames.org id of the place (either place_name or geonames_id must be provided) (optional)
max_distance = 0.5 # float | Maximum distance in degrees lon/lat for test sites (optional) (default to 0.5)
limit = 5 # int | Maximum number of test sites to return (optional) (default to 5)

    try:
        # Get all items for a place
        api_response = api_instance.get_all(place_name=place_name, geonames_id=geonames_id, max_distance=max_distance, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **place_name** | **str**| The name of the place, e.g. a city, neighborhood, state (either place_name or geonames_id must be provided) | [optional] 
 **geonames_id** | **int**| The geonames.org id of the place (either place_name or geonames_id must be provided) | [optional] 
 **max_distance** | **float**| Maximum distance in degrees lon/lat for test sites | [optional] [default to 0.5]
 **limit** | **int**| Maximum number of test sites to return | [optional] [default to 5]

### Return type

[**ResultsList**](ResultsList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_health_departments**
> ResultsList get_health_departments(place_name=place_name, geonames_id=geonames_id)

Get responsible health departments for a place

### Example

```python
from __future__ import print_function
import time
import covid_local
from covid_local.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = covid_local.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with covid_local.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = covid_local.DefaultApi(api_client)
    place_name = 'place_name_example' # str | The name of the place, e.g. a city, neighborhood, state (either place_name or geonames_id must be provided) (optional)
geonames_id = 56 # int | The geonames.org id of the place (either place_name or geonames_id must be provided) (optional)

    try:
        # Get responsible health departments for a place
        api_response = api_instance.get_health_departments(place_name=place_name, geonames_id=geonames_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_health_departments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **place_name** | **str**| The name of the place, e.g. a city, neighborhood, state (either place_name or geonames_id must be provided) | [optional] 
 **geonames_id** | **int**| The geonames.org id of the place (either place_name or geonames_id must be provided) | [optional] 

### Return type

[**ResultsList**](ResultsList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hotlines**
> ResultsList get_hotlines(place_name=place_name, geonames_id=geonames_id)

Get hotlines for a place

### Example

```python
from __future__ import print_function
import time
import covid_local
from covid_local.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = covid_local.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with covid_local.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = covid_local.DefaultApi(api_client)
    place_name = 'place_name_example' # str | The name of the place, e.g. a city, neighborhood, state (either place_name or geonames_id must be provided) (optional)
geonames_id = 56 # int | The geonames.org id of the place (either place_name or geonames_id must be provided) (optional)

    try:
        # Get hotlines for a place
        api_response = api_instance.get_hotlines(place_name=place_name, geonames_id=geonames_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_hotlines: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **place_name** | **str**| The name of the place, e.g. a city, neighborhood, state (either place_name or geonames_id must be provided) | [optional] 
 **geonames_id** | **int**| The geonames.org id of the place (either place_name or geonames_id must be provided) | [optional] 

### Return type

[**ResultsList**](ResultsList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_test_sites**
> ResultsList get_test_sites(place_name=place_name, geonames_id=geonames_id, max_distance=max_distance, limit=limit)

Get nearby test sites for a place (sorted by distance to place)

### Example

```python
from __future__ import print_function
import time
import covid_local
from covid_local.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = covid_local.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with covid_local.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = covid_local.DefaultApi(api_client)
    place_name = 'place_name_example' # str | The name of the place, e.g. a city, neighborhood, state (either place_name or geonames_id must be provided) (optional)
geonames_id = 56 # int | The geonames.org id of the place (either place_name or geonames_id must be provided) (optional)
max_distance = 0.5 # float | Maximum distance in degrees lon/lat for test sites (optional) (default to 0.5)
limit = 5 # int | Maximum number of test sites to return (optional) (default to 5)

    try:
        # Get nearby test sites for a place (sorted by distance to place)
        api_response = api_instance.get_test_sites(place_name=place_name, geonames_id=geonames_id, max_distance=max_distance, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_test_sites: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **place_name** | **str**| The name of the place, e.g. a city, neighborhood, state (either place_name or geonames_id must be provided) | [optional] 
 **geonames_id** | **int**| The geonames.org id of the place (either place_name or geonames_id must be provided) | [optional] 
 **max_distance** | **float**| Maximum distance in degrees lon/lat for test sites | [optional] [default to 0.5]
 **limit** | **int**| Maximum number of test sites to return | [optional] [default to 5]

### Return type

[**ResultsList**](ResultsList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_websites**
> ResultsList get_websites(place_name=place_name, geonames_id=geonames_id)

Get websites for a place

### Example

```python
from __future__ import print_function
import time
import covid_local
from covid_local.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = covid_local.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with covid_local.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = covid_local.DefaultApi(api_client)
    place_name = 'place_name_example' # str | The name of the place, e.g. a city, neighborhood, state (either place_name or geonames_id must be provided) (optional)
geonames_id = 56 # int | The geonames.org id of the place (either place_name or geonames_id must be provided) (optional)

    try:
        # Get websites for a place
        api_response = api_instance.get_websites(place_name=place_name, geonames_id=geonames_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_websites: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **place_name** | **str**| The name of the place, e.g. a city, neighborhood, state (either place_name or geonames_id must be provided) | [optional] 
 **geonames_id** | **int**| The geonames.org id of the place (either place_name or geonames_id must be provided) | [optional] 

### Return type

[**ResultsList**](ResultsList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_places**
> list[Place] search_places(q, limit=limit, search_provider=search_provider)

Search for places via free-form query

### Example

```python
from __future__ import print_function
import time
import covid_local
from covid_local.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = covid_local.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with covid_local.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = covid_local.DefaultApi(api_client)
    q = 'q_example' # str | Free-form query string (e.g. a city, neighborhood, state, ...)
limit = 5 # int | Maximum number of entries to return (optional) (default to 5)
search_provider = 'geonames' # str | The search provider (only geonames supported so far) (optional) (default to 'geonames')

    try:
        # Search for places via free-form query
        api_response = api_instance.search_places(q, limit=limit, search_provider=search_provider)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->search_places: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| Free-form query string (e.g. a city, neighborhood, state, ...) | 
 **limit** | **int**| Maximum number of entries to return | [optional] [default to 5]
 **search_provider** | **str**| The search provider (only geonames supported so far) | [optional] [default to &#39;geonames&#39;]

### Return type

[**list[Place]**](Place.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test**
> object test()

Shows all entries for Berlin Mitte (redirects to /all endpoint)

### Example

```python
from __future__ import print_function
import time
import covid_local
from covid_local.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = covid_local.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with covid_local.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = covid_local.DefaultApi(api_client)
    
    try:
        # Shows all entries for Berlin Mitte (redirects to /all endpoint)
        api_response = api_instance.test()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->test: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

