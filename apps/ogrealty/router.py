class OGRouter:

    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'ogrealty':
            return 'ogadmin'
        else:
            return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'ogrealty':
            return 'ogadmin'
        else:
            return None

    def allow_migration(self, db, app_label, model_name=None, **hints):
        if db == 'onadmin':
            return False
        else:
            return True
