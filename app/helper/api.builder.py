def builder(data, status):
    message = "Success"

    if not status:
        status = 200
    elif status == 201:
        message = "Created"
    elif status == 202:
        message = "Accepted"
    elif status == 400:
        message = "Bad Request"
    elif status == 401:
        message = "Unauthorized"
    elif status == 403:
        message = "Forbidden"
    elif status == 404:
        message = "Not Found"
    elif status == 405:
        message = "Method Not Allowed"
    elif status == 500:
        message = "Internal Server Error"
    elif status == 502:
        message = "Bad Gateway"
    elif status == 503:
        message = "Service Unavailable"

    return {
        'status_code': status,
        'message': message,
        'data': data
    }