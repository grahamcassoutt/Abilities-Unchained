
def setup_routes(app, userEndpoints):
    app.add_url_rule("/api/user/<userId>", view_func=userEndpoints.get_user_by_id, methods=["GET"])
    app.add_url_rule("/api/user/<userId>", view_func=userEndpoints.delete_user, methods=["DELETE"])
    app.add_url_rule("/api/user/create", view_func=userEndpoints.create_user, methods=["POST"])
    app.add_url_rule("/api/user/update", view_func=userEndpoints.update_user, methods=["POST"])
    app.add_url_rule("/api/user/updateCharacters", view_func=userEndpoints.update_characters, methods=["POST"])
    app.add_url_rule("/api/user/updateChests", view_func=userEndpoints.update_chests, methods=["POST"])
