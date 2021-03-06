from project.api.looker_api_handler import LookerApiHandler


class Builder(object):
    def __init__(self, db_model):
        self.db_model = db_model

    def build_cache(self):
        cache = []
        rows = self.db_model.query.all()
        for r in rows:
            cache.append(r.to_json())
        return cache


class DBCache(object):
    def __init__(self, db_model):
        self.cache = []
        self.db_model = db_model
        self.builder = Builder(self.db_model)

    def refresh_cache(self):
        cache = self.builder.build_cache()
        self.cache = cache
        return cache


class Look(object):
    def __init__(self, look_id: int, handler: LookerApiHandler):
        self.look_id = look_id
        self.handler = handler

    def load_db(self):
        json_object = self.handler.run_look(look_id=self.look_id)

