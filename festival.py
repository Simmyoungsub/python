class cookie(object):
  def sentence_cookie(self):
    print "cookie"

class run(object):
  def sentence_run(self):
    print "run"
  
class CookieRun(cookie,run):
  def sentence(self):
    cookie.sentence_cookie(self)
    run.sentence_run(self)
    self.sentence_cookie()
    self.sentence_run()
 
cr = CookieRun()
cr.sentence()
