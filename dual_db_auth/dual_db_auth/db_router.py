class AuthRouter:
     def db_for_write(self, model, **hints):
        """Direct write operations to write_db."""
        return 'write_db'

     def db_for_read(self, model, **hints):
        """Direct read operations to read_db."""
        return 'read_db'

     def allow_relation(self, obj1, obj2, **hints):
        """Allow relations between models in both databases."""
        return True

     def allow_migrate(self, db, app_label, model_name=None, **hints):
        """Allow migrations on both databases."""
        return db in ['write_db', 'read_db']
