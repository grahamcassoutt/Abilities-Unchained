
def setup_routes(app, chestEndpoints):
    app.add_url_rule("/api/chest/<chestId>", view_func=chestEndpoints.get_chest_by_id, methods=["GET"])
    app.add_url_rule("/api/chest/<chestId>", view_func=chestEndpoints.delete_chest, methods=["DELETE"])
    app.add_url_rule("/api/chest", view_func=chestEndpoints.create_or_update_chest, methods=["POST"])
