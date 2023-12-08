
def setup_routes(app, gameEndpoints):
    app.add_url_rule("/api/game/<gameId>", view_func=gameEndpoints.get_game_by_id, methods=["GET"])
    app.add_url_rule("/api/game/<gameId>", view_func=gameEndpoints.delete_game, methods=["DELETE"])
    app.add_url_rule("/api/game", view_func=gameEndpoints.create_game, methods=["POST"])
