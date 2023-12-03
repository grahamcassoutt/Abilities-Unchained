
def setup_routes(app, abilityEndpoints):
    app.add_url_rule("/api/abilites", view_func=abilityEndpoints.get_all_abilities, methods=["GET"])
    app.add_url_rule("/api/ability/<abilityId>", view_func=abilityEndpoints.get_ability_by_id, methods=["GET"])
    app.add_url_rule("/api/ability/<abilityId>", view_func=abilityEndpoints.delete_ability, methods=["DELETE"])
    app.add_url_rule("/api/ability", view_func=abilityEndpoints.create_or_update_ability, methods=["POST"])
    app.add_url_rule("/api/abilities/levels", view_func=abilityEndpoints.get_abilities_by_levels, methods=["POST"])
