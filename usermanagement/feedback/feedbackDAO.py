from .models import Feedback

class FeedbackDAO:
  def save_feedback(is_anonymous, user_id, title, content, feedbackId):
    new_feedback = Feedback(feedbackid=feedbackId, anonimity=is_anonymous, title=title, content=content, userid=user_id)
    new_feedback.save()
    
