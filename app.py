from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

# Configure the database URI. Replace with your actual database connection string.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///journal.db'
db = SQLAlchemy(app)

# Define a simple model for journal entries (using SQLAlchemy)
class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False) # Placeholder for user ID
    title = db.Column(db.String(200), nullable=True)
    date = db.Column(db.Date, default=datetime.utcnow)
    text = db.Column(db.Text, nullable=True)
    intention = db.Column(db.Text, nullable=True)
    gratitude = db.Column(db.Text, nullable=True)
    patience = db.Column(db.Text, nullable=True)
    humility = db.Column(db.Text, nullable=True)
    awareness = db.Column(db.Text, nullable=True)
    spiritual_practice = db.Column(db.Text, nullable=True)
    interactions = db.Column(db.Text, nullable=True)
    personal_improvement = db.Column(db.Text, nullable=True)
    gratitude_blessings = db.Column(db.Text, nullable=True)
    accountability = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f"<Entry {self.id}>"

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'title': self.title,
            'date': self.date.isoformat(),
            'text': self.text,
            'intention': self.intention,
            'gratitude': self.gratitude,
            'patience': self.patience,
            'humility': self.humility,
            'awareness': self.awareness,
            'spiritual_practice': self.spiritual_practice,
            'interactions': self.interactions,
            'personal_improvement': self.personal_improvement,
            'gratitude_blessings': self.gratitude_blessings,
            'accountability': self.accountability,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }


@app.route('/')
def hello():
    return "Hello, Flask is working!"

# Create the database tables
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
