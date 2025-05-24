from app import app
from flask import render_template, jsonify

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/search', methods=['GET'])
def api_search():
    return jsonify({"message": "Search API endpoint"})

@app.route('/api/subscribe', methods=['POST'])
def api_subscribe():
    return jsonify({"message": "Subscribe API endpoint"})

@app.route('/api/featured_content', methods=['GET'])
def api_featured_content():
    featured_items = [
        {
            "id": 1,
            "title": "The Midnight Sun",
            "description": "A gripping thriller.",
            "image_url": "https://lh3.googleusercontent.com/aida-public/AB6AXuD-vtlZRBLqqmjMM3cIkMk6n-yQunH_XfNJsA2wiR6Gdx2RDb08OusyQG8W3aU6Mwz55y9RNn15NsnWav8GHgYda8duwKaKTSTVV72vnLozDg8aHDKKIMuntv9q-rfk_681SPzBMA6lDfWcg8cQDEyzicZv7GQttlj2wW5ivMkFyprgL3TKEDvk4sZoTqzSfBM-5EdMpDH18swI76Obb1ng8uEDZx350XuOBXcMhJgeWfPExzzYStk8Sv6R_wSm5a3OH5Krlkr7qf0",
            "type": "movie"
        },
        {
            "id": 2,
            "title": "Echoes of the Past",
            "description": "A historical drama.",
            "image_url": "https://lh3.googleusercontent.com/aida-public/AB6AXuBtzoOhCRYxmX-ynpXuPnwvXLYowxpdh0M3HZaUanhW8M6_3Xb9FLEBt0HWVeMApzgbc0K3NfexxOcMX10aCOxEv7xC4jj9oD5nTo5FdaoAQ9Ke2G052rxd9bbvTf8DrIT2ui68AeMx7bk2PXCu5Dztov2269BAYn08zQGCtdQbcGJwsfc6V9G-mxHs2fNxxAMHFBAyXfGr0hmYGiQXRqpvk48utepQMTVWFCcGe5J7K7lEqgBFbkHQLj6MabKal46LeylO5FaOQXA",
            "type": "movie"
        },
        {
            "id": 3,
            "title": "The Last Frontier",
            "description": "An adventure film.",
            "image_url": "https://lh3.googleusercontent.com/aida-public/AB6AXuBG1vwjQ4BiDtviQS3F39xq7Ti5EegOz04pTcXEZ0zt13Hcm4eUbejHW0-tN5h3VqWQ760_K-sCZmcyOP4YMT4oRV5x7sIHKSIbj6ze4gtfiy2U8KnJ8ho_U7SOULqunCoe8h_quAns32_oHnMnR8Ufr5llt99rbQUGMhjx-Yt2oQjp-rnjY0Lfcr2Nc6gdYPQzTKx0njc8ZWK7ZPyA7hu5CXNr-h-_q5fxYvUvH5GrGUbSpV4V7JxuzQOAsxbt4l9XkzP3lvAw4So",
            "type": "movie"
        },
        {
            "id": 4,
            "title": "City of Dreams",
            "description": "A romantic comedy.",
            "image_url": "https://lh3.googleusercontent.com/aida-public/AB6AXuASCGoWf5mX8Q3cB1auzzYOBDHNCdmIGAMs2djrWe7WnZZSqGqFi6_S7iUkQWm0xVbd7r1uZ1Bqv_yDg4zSYj3ZB2l1-ZcKbbEx-P5L7Z4rq5qLz0EH2bcqIc5BmLQ1LZgqPxCbJ1SOfw88jCSHoSCVUuXj9821OsTP_yKP-olbzfjVwm-YgdGYZiz07AtkCq_9xqhgQb5OLMAPRoKvMA6-RA0DcW--O-SzDkDInJgSthgeTfyA5V732nqU6Ri8bPox9EKGYEFfa_4",
            "type": "movie"
        },
        {
            "id": 5,
            "title": "Whispers of the Wind",
            "description": "A fantasy adventure.",
            "image_url": "https://lh3.googleusercontent.com/aida-public/AB6AXuDL1oZLDbhc82v_5rvf9q5nQqotOoIUuYNNBo6wypMr86cabn_IfO50gGEWwMQ_QBRGuf1jcQE1JXrr1f5sttR5Cm0J6AB63FZfzDtQVaHjUhWitk1MMjZveqKALB--6ypYpQtOZJYeKTDFT9oV3h-UD7xISnq1sLhpD1yIGF6BjjvEpergJDaAsBNnb0TjUWk6-s4OfaX0E8Cx4LgXgkbCoQ9iyQiXnr2PERT00YBifHhCW9vuvKksE6N3qZZwNIQhNE9PjwoGfaU",
            "type": "movie"
        }
    ]
    return jsonify(featured_items)

@app.route('/api/subscription_plans', methods=['GET'])
def api_subscription_plans():
    subscription_plans = [
        {
            "id": 1,
            "name": "Basic",
            "price_monthly": 9.99,
            "features": [
                "Access to all movies and series",
                "Standard definition streaming",
                "Watch on one device at a time"
            ],
            "most_popular": False
        },
        {
            "id": 2,
            "name": "Standard",
            "price_monthly": 14.99,
            "features": [
                "Access to all movies and series",
                "High definition streaming",
                "Watch on two devices at a time",
                "Download content for offline viewing"
            ],
            "most_popular": True
        },
        {
            "id": 3,
            "name": "Premium",
            "price_monthly": 19.99,
            "features": [
                "Access to all movies and series",
                "Ultra high definition streaming",
                "Watch on four devices at a time",
                "Download content for offline viewing",
                "Exclusive content and early access"
            ],
            "most_popular": False
        }
    ]
    return jsonify(subscription_plans)
