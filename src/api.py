   # ... existing code ...

   # Add a new endpoint for streaming mode
   @app.route('/stream', methods=['POST'])
   def stream():
       data = request.get_json()
       # Add logic to handle streaming data
       # ...

   # ... existing code ...