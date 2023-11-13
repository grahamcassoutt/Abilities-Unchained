
def setup_routes(app, characterEndpoints):
    app.add_url_rule("/api/characters", view_func=characterEndpoints.get_all_characters, methods=["GET"])
    app.add_url_rule("/api/character/<character_id>", view_func=characterEndpoints.get_character_by_id, methods=["GET"])
    app.add_url_rule("/api/character/<character_id>", view_func=characterEndpoints.update_character, methods=["PUT"])
    app.add_url_rule("/api/character/<character_id>", view_func=characterEndpoints.delete_character, methods=["DELETE"])
    app.add_url_rule("/api/character", view_func=characterEndpoints.create_character, methods=["POST"])
