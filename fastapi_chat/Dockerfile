FROM python
WORKDIR /app 
ENV worker_count=8 
ENV port=80 
ENV timeout=60 
CMD ["/bin/sh" ,"-c", "pip install -r requirements.txt && pip install uvicorn[standard] && pip install gunicorn && gunicorn main:app -w $worker_count -k uvicorn.workers.UvicornWorker -b 0.0.0.0:$port --log-level debug --timeout $timeout"]