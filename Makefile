deploy:
	cd backend && make start for=prod
	cd frontend && make start for=prod

start:
	cd backend && make start for=dev
	cd frontend && make start for=dev