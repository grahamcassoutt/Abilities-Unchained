def setup_routes(app, characterEndpoints):
    app.add_url_rule("/api/characters", view_func=characterEndpoints.get_all, methods=["GET"])
    app.add_url_rule("/api/character/<character_id>", view_func=characterEndpoints.get, methods=["GET"])
    app.add_url_rule("/api/character/<character_id>", view_func=characterEndpoints.put, methods=["PUT"])
    app.add_url_rule("/api/character/<character_id>", view_func=characterEndpoints.delete, methods=["DELETE"])
    app.add_url_rule("/api/characters", view_func=characterEndpoints.get_all, methods=["GET"])
