import requests

   def test_streaming_mode():
       # Add tests for streaming mode
       response = requests.post('http://localhost:5000/stream', json={'key':'value'})
       assert response.status_code == 200
       assert response.json() == {'key':'value'}
       # ...

   if __name__ == '__main__':
       test_streaming_mode()