from flask import render_template


def get_index(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/
            api/#flask.Flask.make_response>`.
    """

    request_json = request.get_json()
    if request.args and 'message' in request.args:
        return request.args.get('message')
    elif request_json and 'view' in request_json:
        return render_template('view.html', decrypted_message="this is the decrypted message")
    elif request.args and 'textarea-1596005481044' in request.args:
        return render_template('index.html', debuggy=request.args)
    else:
        return render_template('index.html', debuggy=request_json)
