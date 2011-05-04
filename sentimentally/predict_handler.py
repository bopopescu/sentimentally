#!/usr/bin/env python
#
# Copyright 2011 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""PredictHandler handles requests to predict using our prediction model.

PredictHandler simply yields a text/plain response with a message.
"""


__author__ = 'Dan Holevoet <danielholevoet@google.com>'


from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app


class PredictHandler(webapp.RequestHandler):
  """A webapp.RequestHandler to respond to all prediction requests."""

  def get(self):
    """Yield a simple text message for a request."""
    self.response.headers['Content-Type'] = 'text/plain'
    self.response.out.write('Hello')


# The application container that runs a PredictHandler and maps it to the
# /predict URI.
application = webapp.WSGIApplication(
    [('/predict', PredictHandler)],
    debug=True)

def main():
  """Run the PredictHandler application."""
  run_wsgi_app(application)

if __name__ == "__main__":
    main()
