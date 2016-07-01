# """Model and database functions for Pixlee Instachallenge project"""

# from flask_sqlalchemy import SQLAlchemy

# db = SQLAlchemy()

# ##############################################################################
# # Model definitions



# ##############################################################################

# def connect_to_db(app, db_uri="postgresql:///instadb"):
#     """Connect the database to our Flask app."""

#     # Configure to use our PostgreSQL database
#     app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
#     db.app = app
#     db.init_app(app)

# if __name__ == "__main__":
#     from server import app
    
#     connect_to_db(app)
#     print "Connected to DB."

#     db.create_all()
