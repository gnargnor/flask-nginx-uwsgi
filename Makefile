run: build
	docker run -m 500M -e ENVIRON='dev' --rm -it -p 3002:80 reflective
build:
	docker build -t reflective .