# """Model and database functions for Pixlee Instachallenge project"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# ##############################################################################
# # Model definitions

class Search(db.Model):
    """search data for instachallenge"""

    __tablename__ = "searches"

    search_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    tag = db.Column(db.String(164), nullable=True)
    start_date = db.Column(db.String(80), nullable=True)
    end_date = db.Column(db.String(64), nullable=True)

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Search search_id=%s tag=%s start_date=%s end_date=%s>" % (self.search_id, self.tag, self.start_date, self.end_date)


# ##############################################################################

def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our PostgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///instas'
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    from server import app
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.
    
    connect_to_db(app)
    print "Connected to DB."
