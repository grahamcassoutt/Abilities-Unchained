
def setup_routes(app, relationshipEndpoints):
    app.add_url_rule("/api/relationships", view_func=relationshipEndpoints.get_all_relationships_by_status, methods=["POST"])
    app.add_url_rule("/api/relationship/<user1>/<user2>", view_func=relationshipEndpoints.get_relationship_by_user_ids, methods=["GET"])
    app.add_url_rule("/api/relationship/<user1>/<user2>", view_func=relationshipEndpoints.delete_relationship, methods=["DELETE"])
    app.add_url_rule("/api/relationship", view_func=relationshipEndpoints.create_or_update_relationship, methods=["POST"])
