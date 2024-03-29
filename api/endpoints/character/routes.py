
def setup_routes(app, characterEndpoints):
    app.add_url_rule("/api/characters", view_func=characterEndpoints.get_all_characters, methods=["GET"])
    app.add_url_rule("/api/character/<characterId>", view_func=characterEndpoints.get_character_by_id, methods=["GET"])
    app.add_url_rule("/api/character/<characterId>", view_func=characterEndpoints.delete_character, methods=["DELETE"])
    app.add_url_rule("/api/character", view_func=characterEndpoints.create_or_update_character, methods=["POST"])
    app.add_url_rule("/api/characters/levels", view_func=characterEndpoints.get_characters_by_levels, methods=["POST"])
    app.add_url_rule("/api/characters/levels/<hasAbility>", view_func=characterEndpoints.get_characters_by_levels_specific, methods=["POST"])
