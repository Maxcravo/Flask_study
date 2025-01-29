from extensions import db

class Test(db.Model):
  __tableaname__ = "test"
  id = db.Column(db.Integer, primary_key = True)
  title = db.Column(db.String(30))
  content = db.Column(db.Text)
  
  def __repr__(self):
    return f'<Post "{self.title}">'
  
class Ai_summary(db.Model):
  __tablename__ = "ai_summary"
  id = db.Column(db.Integer, primary_key = True)
  title = db.Column(db.String(30))
  summary = db.Column(db.Text)
  
  def __repr__(self):
    return f'<Post "{self.title}">'